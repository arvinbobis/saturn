#!/usr/bin/env python3
"""
Damodaran FCFF Valuation Model — Saturn Portfolio
Based on Aswath Damodaran's fcffginzu model (FCFF approach).

Usage:
    python3 dcf_model.py <TICKER>
    python3 dcf_model.py all

Reads inputs from valuation/inputs/<TICKER>.json
Writes results to valuation/outputs/<TICKER>-dcf.md
"""

import json
import math
import sys
import os
from datetime import date

# ─── FCFF DCF Engine ───────────────────────────────────────────────────────────

def fcff_dcf(inputs: dict) -> dict:
    """
    Damodaran FCFF two-stage DCF model.

    Stage 1: High growth period (years 1–N) with explicit revenue, margin,
             reinvestment assumptions.
    Stage 2: Terminal value using stable growth rate.

    Returns dict with intrinsic value per share and key outputs.
    """
    # ── Unpack inputs ──────────────────────────────────────────────────────────
    ticker          = inputs["ticker"]
    current_revenue = inputs["current_revenue_usd_m"]       # USD millions
    current_ebit    = inputs["current_ebit_usd_m"]           # USD millions (operating income)
    tax_rate        = inputs["effective_tax_rate"]            # e.g. 0.13
    capex           = inputs["capex_usd_m"]                   # USD millions
    depreciation    = inputs["depreciation_usd_m"]            # USD millions
    chg_working_cap = inputs["change_working_capital_usd_m"]  # USD millions
    book_debt       = inputs["book_value_debt_usd_m"]         # USD millions
    cash            = inputs["cash_usd_m"]                    # USD millions
    shares          = inputs["shares_outstanding_m"]          # millions
    stock_price     = inputs["current_stock_price"]           # USD

    # Growth and margin assumptions
    high_growth_years   = inputs["high_growth_years"]         # e.g. 10
    revenue_cagr_high   = inputs["revenue_cagr_high"]         # e.g. 0.20
    target_ebit_margin  = inputs["target_ebit_margin_high"]   # e.g. 0.35
    stable_growth_rate  = inputs["stable_growth_rate"]        # e.g. 0.03
    stable_ebit_margin  = inputs["stable_ebit_margin"]        # e.g. 0.30

    # Reinvestment: sales-to-capital ratio (revenue / invested capital)
    # Higher ratio = more capital-efficient growth
    sales_to_capital_high   = inputs["sales_to_capital_ratio_high"]   # e.g. 1.5
    sales_to_capital_stable = inputs["sales_to_capital_ratio_stable"] # e.g. 1.2

    # Cost of capital
    wacc_high   = inputs["wacc_high"]    # e.g. 0.10
    wacc_stable = inputs["wacc_stable"]  # e.g. 0.08

    # ── Stage 1: Explicit FCF projection ──────────────────────────────────────
    pv_fcff = 0.0
    revenue = current_revenue
    cumulative_discount = 1.0

    fcff_rows = []
    for year in range(1, high_growth_years + 1):
        # Revenue grows at CAGR
        revenue = revenue * (1 + revenue_cagr_high)

        # EBIT transitions linearly from current margin to target margin
        current_margin = current_ebit / current_revenue if current_revenue > 0 else 0
        margin = current_margin + (target_ebit_margin - current_margin) * (year / high_growth_years)
        ebit = revenue * margin

        # NOPAT = EBIT * (1 - tax rate)
        nopat = ebit * (1 - tax_rate)

        # Reinvestment = change in revenue / sales-to-capital ratio
        if year == 1:
            reinvestment = (revenue - current_revenue) / sales_to_capital_high
        else:
            reinvestment = (revenue - prev_revenue) / sales_to_capital_high

        # FCFF = NOPAT - Reinvestment
        fcff = nopat - reinvestment

        # Discount at WACC
        cumulative_discount = cumulative_discount / (1 + wacc_high)
        pv = fcff * cumulative_discount
        pv_fcff += pv

        fcff_rows.append({
            "year": year,
            "revenue": round(revenue, 1),
            "ebit_margin": round(margin * 100, 1),
            "nopat": round(nopat, 1),
            "reinvestment": round(reinvestment, 1),
            "fcff": round(fcff, 1),
            "pv": round(pv, 1),
        })

        prev_revenue = revenue

    # ── Stage 2: Terminal value ────────────────────────────────────────────────
    # Terminal FCFF in year N+1
    terminal_revenue = revenue * (1 + stable_growth_rate)
    terminal_ebit    = terminal_revenue * stable_ebit_margin
    terminal_nopat   = terminal_ebit * (1 - tax_rate)
    terminal_reinvestment = terminal_revenue * stable_growth_rate / sales_to_capital_stable
    terminal_fcff    = terminal_nopat - terminal_reinvestment

    # Terminal value at end of high growth period
    terminal_value   = terminal_fcff / (wacc_stable - stable_growth_rate)

    # PV of terminal value (discounted from end of year N)
    pv_terminal = terminal_value * cumulative_discount

    # ── Equity value per share ─────────────────────────────────────────────────
    enterprise_value  = pv_fcff + pv_terminal
    equity_value      = enterprise_value - book_debt + cash
    intrinsic_value   = equity_value / shares if shares > 0 else 0

    margin_of_safety  = (intrinsic_value - stock_price) / stock_price * 100

    return {
        "ticker":            ticker,
        "date":              str(date.today()),
        "intrinsic_value":   round(intrinsic_value, 2),
        "current_price":     stock_price,
        "margin_of_safety":  round(margin_of_safety, 1),
        "enterprise_value":  round(enterprise_value, 1),
        "equity_value":      round(equity_value, 1),
        "pv_fcff_stage1":    round(pv_fcff, 1),
        "pv_terminal":       round(pv_terminal, 1),
        "terminal_value":    round(terminal_value, 1),
        "fcff_rows":         fcff_rows,
        "inputs":            inputs,
    }


def sensitivity_table(inputs: dict, price_targets: list, wacc_range: list) -> list:
    """
    Run the DCF across a range of revenue CAGRs and WACCs.
    Returns a matrix of intrinsic values.
    """
    rows = []
    for cagr in price_targets:
        row = {"revenue_cagr": f"{cagr*100:.0f}%"}
        for wacc in wacc_range:
            inp = inputs.copy()
            inp["revenue_cagr_high"] = cagr
            inp["wacc_high"] = wacc
            result = fcff_dcf(inp)
            row[f"wacc_{wacc*100:.0f}%"] = f"${result['intrinsic_value']:,.0f}"
        rows.append(row)
    return rows


# ── Output formatter ──────────────────────────────────────────────────────────

def format_markdown(result: dict) -> str:
    inp = result["inputs"]
    mos = result["margin_of_safety"]
    mos_str = f"+{mos:.1f}%" if mos > 0 else f"{mos:.1f}%"
    verdict = "UNDERVALUED" if mos > 15 else ("FAIRLY VALUED" if mos > -15 else "OVERVALUED")

    lines = [
        f"# DCF Valuation — {result['ticker']}",
        f"",
        f"*Generated: {result['date']} | Model: Damodaran FCFF two-stage*",
        f"",
        f"## Summary",
        f"",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Intrinsic Value | **${result['intrinsic_value']:,.2f}** |",
        f"| Current Price | ${result['current_price']:,.2f} |",
        f"| Margin of Safety | **{mos_str}** |",
        f"| Verdict | **{verdict}** |",
        f"| Enterprise Value | ${result['enterprise_value']:,.0f}M |",
        f"| PV Stage 1 FCFFs | ${result['pv_fcff_stage1']:,.0f}M |",
        f"| PV Terminal Value | ${result['pv_terminal']:,.0f}M |",
        f"| Terminal Value (undiscounted) | ${result['terminal_value']:,.0f}M |",
        f"",
        f"## Key Assumptions",
        f"",
        f"| Input | Value |",
        f"|---|---|",
        f"| High growth years | {inp['high_growth_years']} |",
        f"| Revenue CAGR (high growth) | {inp['revenue_cagr_high']*100:.1f}% |",
        f"| Target EBIT margin (high growth) | {inp['target_ebit_margin_high']*100:.1f}% |",
        f"| Stable growth rate | {inp['stable_growth_rate']*100:.1f}% |",
        f"| Stable EBIT margin | {inp['stable_ebit_margin']*100:.1f}% |",
        f"| WACC (high growth) | {inp['wacc_high']*100:.1f}% |",
        f"| WACC (stable) | {inp['wacc_stable']*100:.1f}% |",
        f"| Sales-to-capital (high growth) | {inp['sales_to_capital_ratio_high']:.1f}x |",
        f"| Tax rate | {inp['effective_tax_rate']*100:.1f}% |",
        f"",
        f"## Year-by-Year FCF Projection",
        f"",
        f"| Year | Revenue ($M) | EBIT Margin | NOPAT ($M) | Reinvestment ($M) | FCFF ($M) | PV ($M) |",
        f"|---|---|---|---|---|---|---|",
    ]

    for row in result["fcff_rows"]:
        lines.append(
            f"| {row['year']} | {row['revenue']:,.0f} | {row['ebit_margin']:.1f}% "
            f"| {row['nopat']:,.0f} | {row['reinvestment']:,.0f} "
            f"| {row['fcff']:,.0f} | {row['pv']:,.0f} |"
        )

    # Sensitivity table
    cagrS = [0.10, 0.15, 0.20, 0.25, 0.30]
    waccS = [0.08, 0.10, 0.12]
    sens  = sensitivity_table(inp, cagrS, waccS)

    lines += [
        f"",
        f"## Sensitivity Table — Intrinsic Value",
        f"",
        f"*Rows = Revenue CAGR during high growth; Columns = WACC*",
        f"",
        f"| Revenue CAGR | WACC 8% | WACC 10% | WACC 12% |",
        f"|---|---|---|---|",
    ]
    for row in sens:
        lines.append(
            f"| {row['revenue_cagr']} | {row.get('wacc_8%','—')} "
            f"| {row.get('wacc_10%','—')} | {row.get('wacc_12%','—')} |"
        )

    lines += [
        f"",
        f"---",
        f"*Inputs source: see `valuation/inputs/{result['ticker']}.json` — populate from Wisesheets 10Y data.*",
        f"*Model: Damodaran FCFF two-stage. Does not include options dilution or non-operating assets beyond cash.*",
    ]

    return "\n".join(lines)


# ── Main ───────────────────────────────────────────────────────────────────────

def run_ticker(ticker: str):
    base  = os.path.dirname(os.path.abspath(__file__))
    input_path  = os.path.join(base, "inputs",  f"{ticker}.json")
    output_dir  = os.path.join(base, "outputs")
    output_path = os.path.join(output_dir, f"{ticker}-dcf.md")

    if not os.path.exists(input_path):
        print(f"[{ticker}] No input file found at {input_path} — skipping.")
        return

    with open(input_path) as f:
        inputs = json.load(f)

    # Skip if inputs are still placeholders
    if inputs.get("current_revenue_usd_m", 0) == 0:
        print(f"[{ticker}] Inputs not yet populated — skipping.")
        return

    result = fcff_dcf(inputs)
    md     = format_markdown(result)

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(md)

    mos = result["margin_of_safety"]
    sign = "+" if mos > 0 else ""
    print(f"[{ticker}] Intrinsic: ${result['intrinsic_value']:,.2f} | "
          f"Price: ${result['current_price']:,.2f} | "
          f"MoS: {sign}{mos:.1f}% → {output_path}")


TICKERS = ["TSM", "MU", "ASML", "NVDA", "MRVL", "ANET", "ALAB"]

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "all":
        for t in TICKERS:
            run_ticker(t)
    else:
        run_ticker(sys.argv[1].upper())
