# DCF Valuation — ANET

*Generated: 2026-05-22 | Model: Damodaran FCFF two-stage (fcffginzu methodology)*

## 🔴 Decision: SELL / AVOID

| Metric | Value |
|---|---|
| **Intrinsic Value** | **$126.94** |
| Current Price | $146.44 |
| Margin of Safety | **-13.3%** |
| Enterprise Value | $144,222M |
| PV Stage 1 FCFFs | $39,184M |
| PV Terminal Value | $105,038M |
| Terminal Value (undiscounted) | $263,776M |
| WACC (high growth) | 9.65% |
| WACC (stable) | 8.91% |
| Stable ROIC | 66.00% |
| Stable Reinvestment Rate | 4.5% |
| R&D Capitalized | $3,248M |
| Adj. EBIT addition (R&D cap) | $274M |

## Story → Numbers

> Arista is the networking backbone of AI data centers — every GPU cluster requires ultra-low-latency spine-leaf ethernet switching, and Arista is the dominant market leader. Q1 2026 demonstrated GAAP operating margin expansion to 42.7% (from FY2025 average 32.7%), confirming that EOS software and services operating leverage is materializing ahead of schedule. FY2026 revenue guidance is $11.5B (+27.7% YoY) with AI fabric specifically doubling to $3.5B for 100+ customers. Hyperscaler CapEx of $725B in 2026 (+77% YoY) provides direct multi-quarter demand visibility: GPU cluster buildouts at this scale require proportionally more 400G/800G ethernet switches. XPO MSA and EBO MSA optical interconnect initiatives extend Arista's addressable market beyond switching into the next AI cluster architecture layer. Primary near-term risk: silicon, memory, and optical component supply constraints limit gross margin expansion (64% actual in Q1 vs. potential 66%+). Primary structural risks: customer concentration (Microsoft + Meta can be >50% of revenue) and InfiniBand competition for GPU-to-GPU scale-up networks (ANET's Ethernet is primarily used in scale-out/spine-leaf, less so for NVLink/InfiniBand clusters).

## Assumptions & Justifications

| Input | Value | Story Justification |
|---|---|---|
| Revenue CAGR (high growth) | 20.0% | 20% — raised from 17% given Q1 2026 +35.1% YoY actual and FY2026 guidance of +27.7% YoY (+$11.5B). Even assuming growth decelerates from 27% in 2026 to ~10-12% by years 8-10 as the base exceeds $30B, the blended 10-year CAGR is ~18-20%. The $725B hyperscaler CapEx cycle and 800G→1.6T ethernet upgrade wave support sustained above-consensus growth through 2027-2028. |
| Target EBIT margin | 40.0% | 40% EBIT margin — already achieved and exceeded in Q1 2026 (42.7% GAAP, 47.8% non-GAAP). The 40% target is conservative; as software/services mix grows and operating leverage compounds, structural margin could reach 42-45%. Using 40% to match the conservative lower bound already demonstrated in practice. |
| High growth years | 10 | 10 years — GPU cluster scale-out extends through multiple AI infrastructure build cycles (Blackwell → Vera Rubin → Feynman). Each generation of larger clusters (10K → 100K → 1M GPU equivalents) requires proportional networking spend. Enterprise AI campus networking adds a second, more durable growth leg. |
| Stable growth rate | 3.0% | 3% — mature networking market grows with global enterprise IT spend and international data center builds. Conservative given Arista's international expansion underway. |
| Stable EBIT margin | 33.0% | 33% stable EBIT — as hardware commoditizes in the terminal period, software and service revenue sustains margin above commodity networking peers (Cisco enterprise at ~25-30% EBIT margin). |
| Sales/Capital (high) | 2.20x | 2.2x — asset-light relative to chip companies. Arista is fabless for networking silicon (uses Broadcom/Marvell merchant silicon), earns software margin on EOS. Moderate capital intensity for supply chain logistics and working capital as revenue scales. |
| Sales/Capital (stable) | 2.50x | 2.5x — further efficiency as EOS software and support revenue grows relative to hardware; less working capital per dollar of revenue in the stable period. |
| Beta (high growth) | 1.05 | 1.05 high-growth beta — near-market. More predictable than pure semis due to recurring software/support revenue stream, but CapEx-cycle dependent. 0.90 stable beta as company matures. |
| R&D amortization years | 5 | 5-year amortization — EOS software platform and switch ASIC design cycles have 3-5 year relevance. Network OS features ship continuously but major architectural cycles (e.g., 400G platform, 800G platform) are 4-5 year cycles. |
| Uncertainty level | medium | Medium — strong hyperscaler relationships (Microsoft, Meta, Google are deeply co-invested in EOS) and recurring service revenue provide multi-quarter visibility. Customer concentration (top 3 can be ~60% of revenue) and macro CapEx sensitivity are primary risks. EOS switching costs are high but not absolute — a determined hyperscaler could build custom networking over 3-4 years. |

## Base Year (Year 0) — Actual Financials

| Item | Value ($M) |
|---|---|
| Reported Revenue | 9,700 |
| Reported EBIT | 3,400 |
| R&D Adj. to EBIT | 274 |
| Adjusted EBIT | 3,674 |
| CapEx | 120 |
| D&A | 80 |
| ΔWorking Capital | 200 |
| FCFF (Year 0) | 2,425 |

## Year-by-Year FCF Projection

| Year | Revenue ($M) | EBIT Margin | NOPAT ($M) | Reinvestment ($M) | FCFF ($M) | PV ($M) |
|---|---|---|---|---|---|---|
| 1 | 11,640 | 38.1% | 3,547 | 882 | 2,665 | 2,430 |
| 2 | 13,968 | 38.3% | 4,280 | 1,058 | 3,222 | 2,680 |
| 3 | 16,762 | 38.5% | 5,164 | 1,270 | 3,894 | 2,954 |
| 4 | 20,114 | 38.7% | 6,231 | 1,524 | 4,707 | 3,257 |
| 5 | 24,137 | 38.9% | 7,518 | 1,828 | 5,690 | 3,591 |
| 6 | 28,964 | 39.1% | 9,072 | 2,194 | 6,877 | 3,958 |
| 7 | 34,757 | 39.4% | 10,945 | 2,633 | 8,312 | 4,363 |
| 8 | 41,708 | 39.6% | 13,205 | 3,160 | 10,045 | 4,809 |
| 9 | 50,050 | 39.8% | 15,931 | 3,792 | 12,139 | 5,300 |
| 10 | 60,060 | 40.0% | 19,219 | 4,550 | 14,669 | 5,841 |

## Sensitivity — Intrinsic Value per Share

*Rows = Revenue CAGR (high growth period); Columns = approximate WACC*

| Revenue CAGR | WACC ~8% | WACC ~10% | WACC ~12% |
|---|---|---|---|
| 8% | $98 | $55 | $39 |
| 12% | $129 | $69 | $46 |
| 16% | $171 | $86 | $55 |
| 20% | $227 | $110 | $67 |
| 25% | $325 | $151 | $87 |

---
*Inputs: `valuation/inputs/ANET.json` — populate from earnings + web search.*
*R&D capitalization follows Damodaran methodology for tech/semiconductor firms.*
*Model: Damodaran FCFF two-stage. Matches fcffginzu.xls approach.*