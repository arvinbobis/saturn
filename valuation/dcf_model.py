#!/usr/bin/env python3
"""
Damodaran FCFF Valuation Model — Saturn Portfolio
Closely follows the fcffginzu Excel spreadsheet methodology.

Key design choices matching fcffginzu:
  - Year 0 FCFF computed from actual financial statement inputs
    (EBIT, CapEx, D&A, ΔWorking Capital) — not estimated
  - R&D capitalization: converts R&D from expense to asset, adjusting
    EBIT, book equity, and invested capital (critical for tech stocks)
  - Projected years use Sales-to-Capital ratio for reinvestment
    (same approach as fcffginzu high-growth projection)
  - Terminal value uses stable ROIC to derive reinvestment rate
  - "Stories to Numbers": every assumption in the input JSON has a
    story_* field — the narrative that justifies the number

Usage:
    python3 dcf_model.py <TICKER>          # single ticker
    python3 dcf_model.py all               # all tickers

Reads:  valuation/inputs/<TICKER>.json
Writes: valuation/outputs/<TICKER>-dcf.md
"""

import json
import math
import os
import sys
from datetime import date


# ── R&D Capitalization ────────────────────────────────────────────────────────

def capitalize_rd(rd_current: float, rd_history: list, amortization_years: int,
                  book_equity: float) -> dict:
    """
    Convert R&D from expense to asset (Damodaran method).

    rd_history: list of R&D spend in prior years, oldest first.
                Length should be >= amortization_years.
    Returns:
        capitalized_rd:     asset value on balance sheet
        annual_amortization: current year amortization charge
        adj_ebit_addition:  amount to ADD to reported EBIT
                            = rd_current - annual_amortization
        adj_book_equity:    book equity after adding capitalized R&D
    """
    if amortization_years <= 0 or rd_current == 0:
        return {
            "capitalized_rd": 0,
            "annual_amortization": 0,
            "adj_ebit_addition": 0,
            "adj_book_equity": book_equity,
        }

    # Build amortization schedule: each year's R&D is amortized over N years
    # Most recent year gets fraction (N-1)/N remaining, prior year (N-2)/N, etc.
    history = rd_history[-amortization_years:] if len(rd_history) >= amortization_years \
              else rd_history

    capitalized_rd = 0.0
    annual_amortization = 0.0

    # Current year: not yet amortized at all in book value sense
    # (but amortization hits income statement)
    # Include all years in the amortization window
    all_rd = history + [rd_current]  # oldest → newest (current)
    n = amortization_years

    for i, spend in enumerate(reversed(all_rd)):  # i=0 is current year
        remaining_life = (n - i) / n
        if remaining_life <= 0:
            break
        capitalized_rd += spend * remaining_life
        annual_amortization += spend / n  # straight-line each year

    # EBIT adjustment: add back current R&D, subtract amortization
    adj_ebit_addition = rd_current - annual_amortization

    return {
        "capitalized_rd": round(capitalized_rd, 1),
        "annual_amortization": round(annual_amortization, 1),
        "adj_ebit_addition": round(adj_ebit_addition, 1),
        "adj_book_equity": round(book_equity + capitalized_rd, 1),
    }


# ── WACC Calculator ───────────────────────────────────────────────────────────

def compute_wacc(risk_free: float, beta: float, erp: float,
                 pre_tax_cost_of_debt: float, tax_rate: float,
                 debt: float, equity_market_value: float) -> float:
    cost_of_equity = risk_free + beta * erp
    after_tax_cost_of_debt = pre_tax_cost_of_debt * (1 - tax_rate)
    total = debt + equity_market_value
    if total == 0:
        return cost_of_equity
    wacc = cost_of_equity * (equity_market_value / total) + \
           after_tax_cost_of_debt * (debt / total)
    return wacc


# ── FCFF DCF Engine ───────────────────────────────────────────────────────────

def fcff_dcf(inp: dict) -> dict:
    """
    Two-stage FCFF DCF closely following fcffginzu methodology.

    Stage 0: Base year — FCFF from actual financial statements.
    Stage 1: High growth — explicit revenue/margin/reinvestment projection.
    Stage 2: Terminal value — stable growth with ROIC-derived reinvestment.
    """

    ticker  = inp["ticker"]
    tax     = inp["effective_tax_rate"]

    # ── R&D Capitalization ─────────────────────────────────────────────────
    rd = capitalize_rd(
        rd_current        = inp.get("rd_expense_usd_m", 0),
        rd_history        = inp.get("rd_history_usd_m", []),
        amortization_years= inp.get("rd_amortization_years", 0),
        book_equity       = inp.get("book_value_equity_usd_m", 0),
    )
    capitalized_rd     = rd["capitalized_rd"]
    adj_ebit_addition  = rd["adj_ebit_addition"]
    adj_book_equity    = rd["adj_book_equity"]

    # ── Base Year (Year 0) — Actual FCFF from financials ──────────────────
    reported_ebit     = inp["current_ebit_usd_m"]
    adj_ebit          = reported_ebit + adj_ebit_addition

    capex             = inp["capex_usd_m"]
    da                = inp["depreciation_usd_m"]
    net_capex         = capex - da

    # If capitalizing R&D, net capex includes R&D spend less amortization
    if inp.get("rd_amortization_years", 0) > 0:
        net_capex += inp.get("rd_expense_usd_m", 0) - rd["annual_amortization"]

    change_wc         = inp["change_working_capital_usd_m"]
    nopat_0           = adj_ebit * (1 - tax)
    reinvestment_0    = net_capex + change_wc
    fcff_0            = nopat_0 - reinvestment_0

    revenue           = inp["current_revenue_usd_m"]
    current_margin    = adj_ebit / revenue if revenue > 0 else 0

    # ── Cost of Capital (High Growth) ─────────────────────────────────────
    equity_market_val = inp["current_stock_price"] * inp["shares_outstanding_m"]
    book_debt         = inp["book_value_debt_usd_m"]

    wacc_high = compute_wacc(
        risk_free             = inp["risk_free_rate"],
        beta                  = inp["beta_high"],
        erp                   = inp["equity_risk_premium"],
        pre_tax_cost_of_debt  = inp["pre_tax_cost_of_debt"],
        tax_rate              = tax,
        debt                  = book_debt,
        equity_market_value   = equity_market_val,
    )

    # ── Stage 1: High Growth Projection ───────────────────────────────────
    n_high            = inp["high_growth_years"]
    g_high            = inp["revenue_cagr_high"]
    target_margin     = inp["target_ebit_margin_high"]
    s2c_high          = inp["sales_to_capital_ratio_high"]

    pv_fcff     = 0.0
    cumdisc     = 1.0
    fcff_rows   = []
    prev_rev    = revenue

    for yr in range(1, n_high + 1):
        rev         = prev_rev * (1 + g_high)

        # Margin transitions linearly from current to target over high growth period
        margin      = current_margin + (target_margin - current_margin) * (yr / n_high)
        ebit        = rev * margin
        nopat       = ebit * (1 - tax)

        # Reinvestment via sales-to-capital ratio (fcffginzu method for projections)
        reinv       = (rev - prev_rev) / s2c_high
        fcff        = nopat - reinv

        cumdisc     = cumdisc / (1 + wacc_high)
        pv          = fcff * cumdisc
        pv_fcff    += pv

        fcff_rows.append({
            "year": yr, "revenue": round(rev, 1),
            "ebit_margin": round(margin * 100, 2),
            "nopat": round(nopat, 1), "reinvestment": round(reinv, 1),
            "fcff": round(fcff, 1), "pv": round(pv, 1),
        })
        prev_rev = rev

    # ── Stage 2: Terminal Value ────────────────────────────────────────────
    stable_g        = inp["stable_growth_rate"]
    stable_margin   = inp["stable_ebit_margin"]
    s2c_stable      = inp["sales_to_capital_ratio_stable"]

    wacc_stable = compute_wacc(
        risk_free             = inp["risk_free_rate"],
        beta                  = inp.get("beta_stable", 1.0),
        erp                   = inp["equity_risk_premium"],
        pre_tax_cost_of_debt  = inp["pre_tax_cost_of_debt"],
        tax_rate              = tax,
        debt                  = book_debt,
        equity_market_value   = equity_market_val,
    )

    # Stable ROIC (after-tax operating return on invested capital)
    # ROIC = NOPAT margin × sales-to-capital ratio
    stable_roic         = stable_margin * (1 - tax) * s2c_stable
    reinv_rate_stable   = stable_g / stable_roic if stable_roic > 0 else 0.5

    term_rev    = prev_rev * (1 + stable_g)
    term_ebit   = term_rev * stable_margin
    term_nopat  = term_ebit * (1 - tax)
    term_reinv  = term_nopat * reinv_rate_stable
    term_fcff   = term_nopat - term_reinv

    if wacc_stable <= stable_g:
        raise ValueError(f"WACC ({wacc_stable:.2%}) must exceed stable growth rate ({stable_g:.2%})")

    terminal_value  = term_fcff / (wacc_stable - stable_g)
    pv_terminal     = terminal_value * cumdisc   # discounted from end of high growth

    # ── Equity Value ───────────────────────────────────────────────────────
    cash            = inp["cash_usd_m"]
    non_op_assets   = inp.get("non_operating_assets_usd_m", 0)
    minority_int    = inp.get("minority_interests_usd_m", 0)

    enterprise_val  = pv_fcff + pv_terminal
    equity_val      = enterprise_val - book_debt + cash + non_op_assets \
                      + capitalized_rd - minority_int
    shares          = inp["shares_outstanding_m"]
    intrinsic       = equity_val / shares if shares > 0 else 0
    price           = inp["current_stock_price"]
    mos             = (intrinsic - price) / price * 100 if price > 0 else 0

    return {
        "ticker":             ticker,
        "date":               str(date.today()),
        "intrinsic_value":    round(intrinsic, 2),
        "current_price":      price,
        "margin_of_safety":   round(mos, 1),
        "enterprise_value":   round(enterprise_val, 1),
        "equity_value":       round(equity_val, 1),
        "pv_stage1":          round(pv_fcff, 1),
        "pv_terminal":        round(pv_terminal, 1),
        "terminal_value":     round(terminal_value, 1),
        "wacc_high":          round(wacc_high * 100, 2),
        "wacc_stable":        round(wacc_stable * 100, 2),
        "stable_roic":        round(stable_roic * 100, 2),
        "reinv_rate_stable":  round(reinv_rate_stable * 100, 1),
        "fcff_0":             round(fcff_0, 1),
        "rd_capitalized":     round(capitalized_rd, 1),
        "adj_ebit_addition":  round(adj_ebit_addition, 1),
        "fcff_rows":          fcff_rows,
        "inputs":             inp,
    }


# ── Sensitivity Table ─────────────────────────────────────────────────────────

def sensitivity(inp: dict,
                cagr_range: list = None,
                wacc_range: list = None) -> list:
    if cagr_range is None:
        cagr_range = [0.08, 0.12, 0.16, 0.20, 0.25]
    if wacc_range is None:
        wacc_range = [0.08, 0.10, 0.12]

    rows = []
    for cagr in cagr_range:
        row = {"cagr": f"{cagr*100:.0f}%"}
        for w in wacc_range:
            test = inp.copy()
            test["revenue_cagr_high"] = cagr
            test["risk_free_rate"]    = w - inp.get("equity_risk_premium", 0.049) \
                                        * inp.get("beta_high", 1.0)
            # Simpler: override WACC indirectly via beta
            # Easier: just adjust risk_free to hit target WACC approximately
            # Best: recompute directly
            eq_mv   = inp["current_stock_price"] * inp["shares_outstanding_m"]
            debt    = inp["book_value_debt_usd_m"]
            tax     = inp["effective_tax_rate"]
            cod     = inp["pre_tax_cost_of_debt"]
            total   = eq_mv + debt
            # Solve for beta that gives desired WACC
            after_tax_debt_contrib = cod * (1 - tax) * debt / total if total else 0
            eq_contrib_needed = w - after_tax_debt_contrib
            req_ke = eq_contrib_needed * total / eq_mv if eq_mv else w
            req_beta = (req_ke - inp["risk_free_rate"]) / inp["equity_risk_premium"] \
                       if inp["equity_risk_premium"] else 1.0
            test["beta_high"]   = max(0.5, req_beta)
            test["beta_stable"] = max(0.8, req_beta * 0.9)
            try:
                r = fcff_dcf(test)
                row[f"w{int(w*100)}"] = f"${r['intrinsic_value']:,.0f}"
            except Exception:
                row[f"w{int(w*100)}"] = "err"
        rows.append(row)
    return rows


# ── Decision Logic ────────────────────────────────────────────────────────────

def recommendation(mos: float, inp: dict) -> str:
    """Simple rules matching Damodaran's margin-of-safety framing."""
    uncertainty = inp.get("uncertainty", "medium")  # low / medium / high

    thresholds = {
        "low":    {"buy": 10, "wait": 0,   "hold": -10},
        "medium": {"buy": 20, "wait": 5,   "hold": -10},
        "high":   {"buy": 30, "wait": 10,  "hold": -15},
    }.get(uncertainty, {"buy": 20, "wait": 5, "hold": -10})

    if mos >= thresholds["buy"]:
        return "BUY"
    elif mos >= thresholds["wait"]:
        return "WAIT — approaching fair value"
    elif mos >= thresholds["hold"]:
        return "HOLD"
    else:
        return "SELL / AVOID"


# ── Markdown Output ───────────────────────────────────────────────────────────

def format_markdown(r: dict) -> str:
    inp  = r["inputs"]
    mos  = r["margin_of_safety"]
    rec  = recommendation(mos, inp)
    sign = "+" if mos > 0 else ""
    verdict_line = f"**{rec}** (MoS: {sign}{mos:.1f}%)"

    # Emoji indicator
    if "BUY" in rec:       emoji = "🟢"
    elif "WAIT" in rec:    emoji = "🟡"
    elif "HOLD" in rec:    emoji = "🟡"
    else:                  emoji = "🔴"

    lines = [
        f"# DCF Valuation — {r['ticker']}",
        f"",
        f"*Generated: {r['date']} | Model: Damodaran FCFF two-stage (fcffginzu methodology)*",
        f"",
        f"## {emoji} Decision: {rec}",
        f"",
        f"| Metric | Value |",
        f"|---|---|",
        f"| **Intrinsic Value** | **${r['intrinsic_value']:,.2f}** |",
        f"| Current Price | ${r['current_price']:,.2f} |",
        f"| Margin of Safety | **{sign}{mos:.1f}%** |",
        f"| Enterprise Value | ${r['enterprise_value']:,.0f}M |",
        f"| PV Stage 1 FCFFs | ${r['pv_stage1']:,.0f}M |",
        f"| PV Terminal Value | ${r['pv_terminal']:,.0f}M |",
        f"| Terminal Value (undiscounted) | ${r['terminal_value']:,.0f}M |",
        f"| WACC (high growth) | {r['wacc_high']:.2f}% |",
        f"| WACC (stable) | {r['wacc_stable']:.2f}% |",
        f"| Stable ROIC | {r['stable_roic']:.2f}% |",
        f"| Stable Reinvestment Rate | {r['reinv_rate_stable']:.1f}% |",
        f"| R&D Capitalized | ${r['rd_capitalized']:,.0f}M |",
        f"| Adj. EBIT addition (R&D cap) | ${r['adj_ebit_addition']:,.0f}M |",
        f"",
    ]

    # Story → Numbers
    story = inp.get("story_narrative", "")
    if story:
        lines += [
            f"## Story → Numbers",
            f"",
            f"> {story}",
            f"",
        ]

    # Assumption justifications
    lines += [
        f"## Assumptions & Justifications",
        f"",
        f"| Input | Value | Story Justification |",
        f"|---|---|---|",
        f"| Revenue CAGR (high growth) | {inp['revenue_cagr_high']*100:.1f}% | {inp.get('story_revenue_cagr', '—')} |",
        f"| Target EBIT margin | {inp['target_ebit_margin_high']*100:.1f}% | {inp.get('story_target_margin', '—')} |",
        f"| High growth years | {inp['high_growth_years']} | {inp.get('story_growth_years', '—')} |",
        f"| Stable growth rate | {inp['stable_growth_rate']*100:.1f}% | {inp.get('story_stable_growth', '—')} |",
        f"| Stable EBIT margin | {inp['stable_ebit_margin']*100:.1f}% | {inp.get('story_stable_margin', '—')} |",
        f"| Sales/Capital (high) | {inp['sales_to_capital_ratio_high']:.2f}x | {inp.get('story_s2c_high', '—')} |",
        f"| Sales/Capital (stable) | {inp['sales_to_capital_ratio_stable']:.2f}x | {inp.get('story_s2c_stable', '—')} |",
        f"| Beta (high growth) | {inp['beta_high']:.2f} | {inp.get('story_beta', '—')} |",
        f"| R&D amortization years | {inp.get('rd_amortization_years', 0)} | {inp.get('story_rd_cap', '—')} |",
        f"| Uncertainty level | {inp.get('uncertainty', 'medium')} | {inp.get('story_uncertainty', '—')} |",
        f"",
    ]

    # Year 0
    lines += [
        f"## Base Year (Year 0) — Actual Financials",
        f"",
        f"| Item | Value ($M) |",
        f"|---|---|",
        f"| Reported Revenue | {inp['current_revenue_usd_m']:,.0f} |",
        f"| Reported EBIT | {inp['current_ebit_usd_m']:,.0f} |",
        f"| R&D Adj. to EBIT | {r['adj_ebit_addition']:,.0f} |",
        f"| Adjusted EBIT | {inp['current_ebit_usd_m'] + r['adj_ebit_addition']:,.0f} |",
        f"| CapEx | {inp['capex_usd_m']:,.0f} |",
        f"| D&A | {inp['depreciation_usd_m']:,.0f} |",
        f"| ΔWorking Capital | {inp['change_working_capital_usd_m']:,.0f} |",
        f"| FCFF (Year 0) | {r['fcff_0']:,.0f} |",
        f"",
    ]

    # Projection table
    lines += [
        f"## Year-by-Year FCF Projection",
        f"",
        f"| Year | Revenue ($M) | EBIT Margin | NOPAT ($M) | Reinvestment ($M) | FCFF ($M) | PV ($M) |",
        f"|---|---|---|---|---|---|---|",
    ]
    for row in r["fcff_rows"]:
        lines.append(
            f"| {row['year']} | {row['revenue']:,.0f} | {row['ebit_margin']:.1f}% "
            f"| {row['nopat']:,.0f} | {row['reinvestment']:,.0f} "
            f"| {row['fcff']:,.0f} | {row['pv']:,.0f} |"
        )

    # Sensitivity table
    try:
        sens = sensitivity(inp)
        lines += [
            f"",
            f"## Sensitivity — Intrinsic Value per Share",
            f"",
            f"*Rows = Revenue CAGR (high growth period); Columns = approximate WACC*",
            f"",
            f"| Revenue CAGR | WACC ~8% | WACC ~10% | WACC ~12% |",
            f"|---|---|---|---|",
        ]
        for row in sens:
            lines.append(
                f"| {row['cagr']} | {row.get('w8','—')} | {row.get('w10','—')} | {row.get('w12','—')} |"
            )
    except Exception as e:
        lines.append(f"\n*Sensitivity table error: {e}*")

    lines += [
        f"",
        f"---",
        f"*Inputs: `valuation/inputs/{r['ticker']}.json` — populate from earnings + web search.*",
        f"*R&D capitalization follows Damodaran methodology for tech/semiconductor firms.*",
        f"*Model: Damodaran FCFF two-stage. Matches fcffginzu.xls approach.*",
    ]

    return "\n".join(lines)


# ── Runner ────────────────────────────────────────────────────────────────────

def run_ticker(ticker: str, verbose: bool = True) -> dict | None:
    base         = os.path.dirname(os.path.abspath(__file__))
    input_path   = os.path.join(base, "inputs",  f"{ticker}.json")
    output_dir   = os.path.join(base, "outputs")
    output_path  = os.path.join(output_dir, f"{ticker}-dcf.md")

    if not os.path.exists(input_path):
        if verbose:
            print(f"[{ticker}] No input file at {input_path} — skipping.")
        return None

    with open(input_path) as f:
        inp = json.load(f)

    # Skip unpopulated inputs
    if inp.get("current_revenue_usd_m", 0) == 0:
        if verbose:
            print(f"[{ticker}] Inputs not yet populated (revenue=0) — skipping.")
        return None

    try:
        result = fcff_dcf(inp)
    except Exception as e:
        if verbose:
            print(f"[{ticker}] Model error: {e}")
        return None

    md = format_markdown(result)
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(md)

    if verbose:
        mos  = result["margin_of_safety"]
        sign = "+" if mos > 0 else ""
        rec  = recommendation(mos, inp)
        print(f"[{ticker}] ${result['current_price']:,.2f} → IV ${result['intrinsic_value']:,.2f} "
              f"| MoS {sign}{mos:.1f}% | {rec}")

    return result


TICKERS = ["TSM", "MU", "ASML", "NVDA", "MRVL", "ANET", "ALAB"]


if __name__ == "__main__":
    targets = TICKERS if len(sys.argv) < 2 or sys.argv[1] == "all" \
              else [sys.argv[1].upper()]
    for t in targets:
        run_ticker(t)
