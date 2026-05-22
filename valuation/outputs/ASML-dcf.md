# DCF Valuation — ASML

*Generated: 2026-05-22 | Model: Damodaran FCFF two-stage (fcffginzu methodology)*

## 🔴 Decision: SELL / AVOID

| Metric | Value |
|---|---|
| **Intrinsic Value** | **$1,122.64** |
| Current Price | $1,592.00 |
| Margin of Safety | **-29.5%** |
| Enterprise Value | $415,755M |
| PV Stage 1 FCFFs | $123,716M |
| PV Terminal Value | $292,039M |
| Terminal Value (undiscounted) | $699,408M |
| WACC (high growth) | 9.13% |
| WACC (stable) | 8.64% |
| Stable ROIC | 42.84% |
| Stable Reinvestment Rate | 7.0% |
| R&D Capitalized | $17,721M |
| Adj. EBIT addition (R&D cap) | $2,995M |

## Story → Numbers

> ASML is the sole supplier of EUV lithography machines — without them there are no chips below 7nm. Every leading-edge fab (TSMC, Samsung, Intel, SK Hynix) must buy from ASML. TSMC's decision to defer High-NA EUV adoption until 2029 — citing cost discipline at €350-400M per unit vs. €150-200M for standard EUV — actually validates the machine's premium economics rather than undermining them. Low-NA EUV demand is accelerating from TSMC N2 capacity ramp, SK Hynix HBM4 production lines, and Samsung 2nm. FY2026 guidance of €36-40B (+16% YoY) reflects Low-NA-driven strength already in the order book. Intel and memory players are taking first High-NA deliveries; ASML CEO confirmed first High-NA chips expected 'in coming months.' The €45B order backlog provides 12-18 months of revenue visibility. At $725B hyperscaler CapEx in 2026, TSMC N2/A14 expansion is structurally guaranteed — ASML machine orders follow with 12-18 month lag.

## Assumptions & Justifications

| Input | Value | Story Justification |
|---|---|---|
| Revenue CAGR (high growth) | 16.0% | 16% reflects Low-NA EUV volume ramp (TSMC N2/A14, Samsung 2nm, SK Hynix HBM4) — validated by €36-40B FY2026 guidance — plus gradual High-NA ramp at 2x ASP from Intel and memory customers from 2027-2028. TSMC deferred High-NA to 2029 (cost, not confidence), moderating the ASP uplift in years 3-5 vs. prior thesis but not eliminating it. |
| Target EBIT margin | 34.0% | 34% reflects scale leverage on EBIT as revenue doubles. Currently ~30–32% EBIT margin; High NA machines carry higher margin than prior generation. |
| High growth years | 10 | 10 years — two full EUV generations (current EUV → High NA → beyond). ASML's roadmap extends to 2030 and beyond with backlog visibility. |
| Stable growth rate | 3.0% | 3% — once leading-edge transition slows, replacement and upgrade cycle sustains modest growth aligned with global semiconductor capex. |
| Stable EBIT margin | 28.0% | 28% stable EBIT margin — service/install base revenue becomes more significant proportion; lower margin than new machine sales but recurring. |
| Sales/Capital (high) | 1.50x | 1.5x — ASML is asset-light for a capital goods company; the value is in IP (EUV optics, source technology). Physical CapEx is moderate relative to revenue. |
| Sales/Capital (stable) | 1.80x | 1.8x — service and upgrade revenue requires very little incremental capital investment. |
| Beta (high growth) | 0.95 | 0.95 — cyclical but backlog visibility reduces realized volatility. Dutch company with EUR/USD exposure adds slight currency risk. |
| R&D amortization years | 10 | 10-year amortization — EUV IP (optics design, laser source, lithography algorithms) has useful life of a full technology generation, typically 8–12 years. |
| Uncertainty level | medium | Medium — monopoly position is clear but China export controls, customer concentration (TSMC ~30% of revenue), and EUR/USD currency exposure justify medium uncertainty. |

## Base Year (Year 0) — Actual Financials

| Item | Value ($M) |
|---|---|
| Reported Revenue | 39,214 |
| Reported EBIT | 13,220 |
| R&D Adj. to EBIT | 2,995 |
| Adjusted EBIT | 16,215 |
| CapEx | 1,963 |
| D&A | 1,207 |
| ΔWorking Capital | 0 |
| FCFF (Year 0) | 10,032 |

## Year-by-Year FCF Projection

| Year | Revenue ($M) | EBIT Margin | NOPAT ($M) | Reinvestment ($M) | FCFF ($M) | PV ($M) |
|---|---|---|---|---|---|---|
| 1 | 45,488 | 40.6% | 15,704 | 4,183 | 11,521 | 10,557 |
| 2 | 52,766 | 39.9% | 17,887 | 4,852 | 13,034 | 10,946 |
| 3 | 61,209 | 39.1% | 20,366 | 5,628 | 14,738 | 11,341 |
| 4 | 71,002 | 38.4% | 23,181 | 6,529 | 16,652 | 11,742 |
| 5 | 82,363 | 37.7% | 26,376 | 7,574 | 18,802 | 12,150 |
| 6 | 95,541 | 36.9% | 29,999 | 8,785 | 21,213 | 12,561 |
| 7 | 110,827 | 36.2% | 34,106 | 10,191 | 23,915 | 12,977 |
| 8 | 128,560 | 35.5% | 38,760 | 11,822 | 26,938 | 13,395 |
| 9 | 149,129 | 34.7% | 44,030 | 13,713 | 30,317 | 13,814 |
| 10 | 172,990 | 34.0% | 49,994 | 15,907 | 34,087 | 14,233 |

## Sensitivity — Intrinsic Value per Share

*Rows = Revenue CAGR (high growth period); Columns = approximate WACC*

| Revenue CAGR | WACC ~8% | WACC ~10% | WACC ~12% |
|---|---|---|---|
| 8% | $943 | $537 | $370 |
| 12% | $1,240 | $669 | $438 |
| 16% | $1,641 | $844 | $528 |
| 20% | $2,177 | $1,075 | $643 |
| 25% | $3,102 | $1,468 | $838 |

---
*Inputs: `valuation/inputs/ASML.json` — populate from earnings + web search.*
*R&D capitalization follows Damodaran methodology for tech/semiconductor firms.*
*Model: Damodaran FCFF two-stage. Matches fcffginzu.xls approach.*