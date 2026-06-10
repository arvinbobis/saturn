# DCF Valuation — TSM

*Generated: 2026-06-10 | Model: Damodaran FCFF two-stage (fcffginzu methodology)*

## 🟡 Decision: HOLD

| Metric | Value |
|---|---|
| **Intrinsic Value** | **$414.11** |
| Current Price | $427.89 |
| Margin of Safety | **-3.2%** |
| Enterprise Value | $2,067,208M |
| PV Stage 1 FCFFs | $506,508M |
| PV Terminal Value | $1,560,701M |
| Terminal Value (undiscounted) | $3,640,027M |
| WACC (high growth) | 8.84% |
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
| Reported Revenue | 131,700 |
| Reported EBIT | 70,600 |
| R&D Adj. to EBIT | 2,111 |
| Adjusted EBIT | 72,711 |
| CapEx | 41,000 |
| D&A | 22,600 |
| ΔWorking Capital | 2,000 |
| FCFF (Year 0) | 40,748 |

## Year-by-Year FCF Projection

| Year | Revenue ($M) | EBIT Margin | NOPAT ($M) | Reinvestment ($M) | FCFF ($M) | PV ($M) |
|---|---|---|---|---|---|---|
| 1 | 155,406 | 53.9% | 72,859 | 26,340 | 46,519 | 42,742 |
| 2 | 183,379 | 52.6% | 83,866 | 31,081 | 52,785 | 44,561 |
| 3 | 216,387 | 51.2% | 96,476 | 36,676 | 59,800 | 46,384 |
| 4 | 255,337 | 49.9% | 110,907 | 43,278 | 67,629 | 48,197 |
| 5 | 301,298 | 48.6% | 127,407 | 51,067 | 76,340 | 49,987 |
| 6 | 355,531 | 47.3% | 146,255 | 60,260 | 85,995 | 51,737 |
| 7 | 419,527 | 46.0% | 167,759 | 71,106 | 96,653 | 53,428 |
| 8 | 495,042 | 44.6% | 192,267 | 83,905 | 108,361 | 55,036 |
| 9 | 584,149 | 43.3% | 220,162 | 99,008 | 121,153 | 56,536 |
| 10 | 689,296 | 42.0% | 251,869 | 116,830 | 135,039 | 57,899 |

## Sensitivity — Intrinsic Value per Share

*Rows = Revenue CAGR (high growth period); Columns = approximate WACC*

| Revenue CAGR | WACC ~8% | WACC ~10% | WACC ~12% |
|---|---|---|---|
| 8% | $279 | $161 | $111 |
| 12% | $364 | $198 | $130 |
| 16% | $477 | $247 | $154 |
| 20% | $629 | $312 | $186 |
| 25% | $890 | $421 | $238 |

---
*Inputs: `valuation/inputs/TSM.json` — populate from earnings + web search.*
*R&D capitalization follows Damodaran methodology for tech/semiconductor firms.*
*Model: Damodaran FCFF two-stage. Matches fcffginzu.xls approach.*