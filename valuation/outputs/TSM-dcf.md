# DCF Valuation — TSM

*Generated: 2026-05-23 | Model: Damodaran FCFF two-stage (fcffginzu methodology)*

## 🟡 Decision: HOLD

| Metric | Value |
|---|---|
| **Intrinsic Value** | **$384.28** |
| Current Price | $407.15 |
| Margin of Safety | **-5.6%** |
| Enterprise Value | $1,912,672M |
| PV Stage 1 FCFFs | $454,865M |
| PV Terminal Value | $1,457,806M |
| Terminal Value (undiscounted) | $3,398,909M |
| WACC (high growth) | 8.83% |
| WACC (stable) | 8.35% |
| Stable ROIC | 30.45% |
| Stable Reinvestment Rate | 9.9% |
| R&D Capitalized | $19,206M |
| Adj. EBIT addition (R&D cap) | $2,111M |

## Story → Numbers

> TSMC is the sole manufacturer of leading-edge AI chips and the structural beneficiary of the $725B hyperscaler CapEx supercycle. FY2025 operating margin reached 50.8% (above the modeled 42% target), driven by AI HPC mix rising to 51%+ of revenue and CoWoS packaging becoming a monopoly constraint. Arizona Fab 21 posted $514M profit in its first year — directly refuting the 'overseas fabs are uneconomical' thesis. CapEx peaks in 2025-2026 ($41B actual / $52-56B guided for 2026); as N2 and CoWoS capacity fills, FCF inflects sharply. The moat — sole supplier of sub-3nm nodes and advanced AI packaging — is unassailable over the investment horizon. Main risks: Taiwan Strait geopolitical tail, overseas fab cost creep (Arizona ~30-50% more expensive per wafer), and High-NA EUV delay pushing sub-A16 nodes to 2029+.

## Assumptions & Justifications

| Input | Value | Story Justification |
|---|---|---|
| Revenue CAGR (high growth) | 18.0% | 18% reflects HPC/AI segment growing >30% yr/yr dragging blended foundry revenue. N2 at premium ASPs, Arizona adds USD exposure. Bear case 12% if AI CapEx cools. |
| Target EBIT margin | 42.0% | 42% is current trajectory; overseas fab cost headwind (Arizona ~30% more expensive than Taiwan) caps upside. Damodaran would note TSMC's historical range is 30–45% EBIT margin. |
| High growth years | 10 | 10 years: N2 → A16 → next node. Leading-edge nodes have 3–5 year product cycles; 10 years covers 2 full cycles. |
| Stable growth rate | 3.0% | 3% = global semiconductor long-run growth. TSMC in stable phase grows with the market. |
| Stable EBIT margin | 35.0% | 35% is the mature foundry equilibrium — enough pricing power to stay above commodity margins but offshore fabs normalize cost structure. |
| Sales/Capital (high) | 0.90x | 0.9x reflects foundry's CapEx intensity (~40–50% of revenue). Sales-to-Capital < 1.0 means TSMC must invest nearly as much as revenue it generates. |
| Sales/Capital (stable) | 1.00x | 1.0x — as legacy fabs fully depreciate and capacity utilization stabilizes, incremental revenue requires less new capital. |
| Beta (high growth) | 0.90 | 0.9 — foundry is less cyclical than fabless or memory; backlogged orders reduce volatility. Geopolitical premium pushes beta above pure defensive. |
| R&D amortization years | 5 | 5-year amortization for process node R&D. Each new node (N2, A16) has a useful IP life of ~5 years before superseded. |
| Uncertainty level | medium | Medium — moat is clear but geopolitical tail risk (Taiwan Strait) creates asymmetric downside that makes wide MoS prudent. Offshore fab execution risk adds uncertainty. |

## Base Year (Year 0) — Actual Financials

| Item | Value ($M) |
|---|---|
| Reported Revenue | 122,900 |
| Reported EBIT | 62,400 |
| R&D Adj. to EBIT | 2,111 |
| Adjusted EBIT | 64,511 |
| CapEx | 41,000 |
| D&A | 22,600 |
| ΔWorking Capital | 2,000 |
| FCFF (Year 0) | 33,614 |

## Year-by-Year FCF Projection

| Year | Revenue ($M) | EBIT Margin | NOPAT ($M) | Reinvestment ($M) | FCFF ($M) | PV ($M) |
|---|---|---|---|---|---|---|
| 1 | 145,022 | 51.4% | 64,904 | 24,580 | 40,324 | 37,051 |
| 2 | 171,126 | 50.4% | 75,024 | 29,004 | 46,020 | 38,852 |
| 3 | 201,929 | 49.3% | 86,686 | 34,225 | 52,460 | 40,695 |
| 4 | 238,276 | 48.3% | 100,114 | 40,386 | 59,729 | 42,572 |
| 5 | 281,165 | 47.2% | 115,569 | 47,655 | 67,914 | 44,477 |
| 6 | 331,775 | 46.2% | 133,343 | 56,233 | 77,110 | 46,401 |
| 7 | 391,495 | 45.1% | 153,772 | 66,355 | 87,417 | 48,333 |
| 8 | 461,964 | 44.1% | 177,234 | 78,299 | 98,935 | 50,262 |
| 9 | 545,117 | 43.0% | 204,161 | 92,393 | 111,768 | 52,173 |
| 10 | 643,238 | 42.0% | 235,039 | 109,024 | 126,016 | 54,049 |

## Sensitivity — Intrinsic Value per Share

*Rows = Revenue CAGR (high growth period); Columns = approximate WACC*

| Revenue CAGR | WACC ~8% | WACC ~10% | WACC ~12% |
|---|---|---|---|
| 8% | $259 | $149 | $103 |
| 12% | $337 | $183 | $120 |
| 16% | $443 | $229 | $142 |
| 20% | $584 | $288 | $171 |
| 25% | $827 | $390 | $220 |

---
*Inputs: `valuation/inputs/TSM.json` — populate from earnings + web search.*
*R&D capitalization follows Damodaran methodology for tech/semiconductor firms.*
*Model: Damodaran FCFF two-stage. Matches fcffginzu.xls approach.*