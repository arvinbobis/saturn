# NVIDIA Corporation (NVDA)

> The dominant AI training hardware company — every major AI model is trained on NVIDIA GPUs.
> In this portfolio, NVDA is tracked as both a holding and the primary demand signal for TSM and MU.

*Last updated: 2026-05-20 | Wisesheets data as of: not yet pulled*

---

## Overview

- **Business model:** Fabless semiconductor company. Designs GPUs and networking hardware; manufacturing outsourced entirely to TSMC. Revenue = hardware (GPUs, networking) + software/services (CUDA ecosystem, NIM, DGX Cloud).
- **Value chain position:** Sits between TSMC (manufacturer) and hyperscalers/enterprises (buyers). NVIDIA's data center revenue is the most direct demand signal for TSMC CoWoS capacity and Micron HBM.
- **Founded:** 1993, Santa Clara, California. HQ in Santa Clara.
- **Listed:** NASDAQ: NVDA
- **Scale:** ~36,000+ employees.
- **Market cap:** *(update)*

### Why NVDA Is in This Portfolio
NVIDIA is the clearest expression of the AI hardware buildout — it captures the largest margin at the system level. The CUDA software moat compounds independently of hardware, making switching costs extraordinarily high. Data center GPU demand is the single most important leading indicator for the rest of the satellite portfolio.

### CUDA Moat
CUDA (Compute Unified Device Architecture) is NVIDIA's GPU programming framework — released 2006, now deeply embedded into every major AI training framework (PyTorch, TensorFlow, JAX). 15+ years of developer tooling, libraries (cuDNN, NCCL, cuBLAS), and institutional knowledge. Re-implementing this ecosystem for a competitor's hardware is a multi-year undertaking even with unlimited resources. AMD ROCm is the closest alternative; it has improved but remains meaningfully behind CUDA in adoption and capability.

---

## Moat

### CUDA Ecosystem Lock-in
*(Populate: developer ecosystem depth, switching cost quantification, enterprise training pipeline lock-in)*

### Blackwell Architecture Performance Lead
*(Populate: H100 → H200 → Blackwell performance step-ups; competitive position vs. AMD MI-series; Google TPU, Amazon Trainium as custom silicon alternatives)*

### Supply Chain Relationships
NVIDIA has priority access to TSMC's most advanced nodes and CoWoS packaging capacity. These relationships took years to build and give NVIDIA structural supply advantages over competitors.

### Networking — InfiniBand and Ethernet
*(Populate: Mellanox acquisition; InfiniBand for GPU clusters; transition to Ethernet with Spectrum-X; Arista as complementary/competitive)*

---

## Financials

*(Pull from Wisesheets — note pull date when populating)*

**Segment note:** NVIDIA reports Data Center, Gaming, Professional Visualization, Automotive, OEM & Other. Data Center is the primary segment for this thesis — track it as % of total revenue.

---

## Revenue Segments

*(Update quarterly — Data Center absolute revenue and YoY growth is the critical number; Gaming secondary; extract Blackwell commentary from earnings)*

---

## Growth Drivers

*(Populate: Hyperscaler AI CapEx growth; Sovereign AI (government GPU buildouts); Enterprise AI adoption; Blackwell ramp; NIM/software revenue growth)*

---

## Risks

*(Populate: Hyperscaler custom silicon risk (Google TPU, Amazon Trainium taking share over time); Export controls to China (historically ~20% of data center revenue); AMD ROCm closing the gap; Valuation multiple compression; Supply constraints)*

---

## Catalysts

### Active Catalysts
*(Populate: Blackwell full ramp; NVLink/NVSwitch GB200 system adoption; Sovereign AI deals; China export waiver decisions)*

### Archived Catalysts
*(Move here once played out)*

---

## Monitoring Checklist

*(Quarterly: Data Center revenue absolute + YoY growth; Blackwell shipment commentary; Gross margin (supply mix signal); China revenue %; Management commentary on hyperscaler demand visibility; AMD competitive update; Leading for TSM/MU: any NVIDIA guidance revision is a 1–2 quarter forward signal)*

---

## Investment View

*(Populate: Valuation, WACC, DCF, Reverse DCF, Scenarios, Decision Log)*

### Decision Log

*(Append-only — no entries yet)*

---

## Recent Updates

### 2026-05-17

**Q1 FY2027 earnings — May 20 (3 days out):** NVIDIA reports Q1 FY2027 on May 20, 2026. Most anticipated earnings report of 2026 per analyst commentary. Consensus expects another blowout quarter. This is the single most important near-term event for the entire satellite portfolio — NVDA guidance revision will flow through to TSM CoWoS and MU HBM demand outlook. Source: Motley Fool, 2026-05-15/16.

**Price target raised:** TD Cowen raised PT to $275 from $235. Source: Search results, 2026-05.

**Stock selloff May 15:** NVDA fell 4.42% (from $235.74 to $225.32) on reports China did not proceed with expected H200 chip purchases, raising demand concerns for China revenue (~historically 20% of data center revenue). 52-week range: $129.16–$236.54. Source: StockInvest.us, 2026-05-15. *Risk flag: China export control enforcement and demand elasticity remain a persistent overhang — watch Q1 FY2027 China revenue commentary.*

**NVIDIA + IREN strategic partnership:** NVIDIA and IREN (AI infrastructure operator) announced a partnership to accelerate deployment of up to 5 gigawatts of AI infrastructure. Underscores the scale of hyperscaler and sovereign AI infrastructure buildout that NVIDIA sits at the center of. Source: Search results, 2026-05.

**Board addition:** Suzanne Nora Johnson added to NVIDIA board of directors. Source: Search results, 2026-05.

**Market position:** NVDA up 67% in market value YTD; currently world's second-largest asset by market cap. Source: Search results, 2026-05.

**Watch at May 20 earnings:**
- Data Center revenue absolute and YoY growth
- Blackwell shipment and demand commentary
- China revenue %
- Management visibility language (12-month demand forward signals)
- Any CoWoS capacity commentary (leading for TSM)

---

### 2026-05-18

**Q1 FY2027 earnings tomorrow (May 20) — consensus and setup:** Wall Street consensus: revenue ~$78.8B (+78% YoY), EPS $1.77. Data center revenue expected >$65B. Gross margins expected >74%. The market focus will be on Q2 guidance and commentary on Blackwell ramp, Vera Rubin supply availability, and China revenue. NVDA market cap at $5.71 trillion; stock up ~20% over the past month. Source: S&P Global / HeyGoTrade / TradingKey / TIKR, 2026-05. *For the portfolio: management's Q2 guidance and forward demand commentary is the most important data point for TSM CoWoS and MU HBM demand outlook over the next 1–2 quarters.*

**Vera Rubin in full production — 2H 2026 availability:** NVIDIA announced at CES 2026 that Vera Rubin NVL72 is in full production. Cloud providers (AWS, Google Cloud, Microsoft Azure, OCI) plus CoreWeave, Lambda, Nebius, and Nscale will offer Vera Rubin instances in 2H 2026. Key specs: 5x inference performance, 10x lower cost per token, and 4x fewer GPUs to train MoE models vs. Blackwell. First Vera Rubin rack is already running at Microsoft Azure. Source: NVIDIA Newsroom / Tom's Hardware / DataCenterDynamics, CES 2026. *Thesis bearing: Confirms — Vera Rubin extends the AI hardware capex cycle well into 2027; sustains demand for TSMC advanced nodes and next-gen HBM from Micron.*

**Jensen Huang — $1 trillion Blackwell + Vera Rubin order book (GTC March 2026):** At GTC 2026, Jensen Huang stated combined purchase orders for Blackwell and Vera Rubin are expected to reach $1 trillion through 2027. Computing demand has increased one million times in the last two years. Source: CNBC / TechCrunch / Axios, 2026-03-16. *Context for portfolio: The $1T NVIDIA order book represents the most concrete proof of hyperscaler CapEx commitment to the AI infrastructure buildout. Every dollar flows through TSMC CoWoS and requires HBM from MU/SKH.*

---

### 2026-05-19

**US H200 clearance granted to 10 Chinese firms — deliveries in limbo:** The US Department of Commerce cleared approximately 10 Chinese companies — including Alibaba, Tencent, and ByteDance — to purchase NVIDIA H200 chips, capped at 75,000 units per customer. However, no deliveries have been completed; the deal remains stalled due to Beijing's supply chain regulations and ongoing US-China tech policy friction. Source: CNBC / Taipei Times, 2026-05-14–15. *Thesis bearing: Ambiguous — US clearance is constructive for NVDA China revenue recovery, but Beijing's blocking is the immediate constraint. Net: zero HBM/CoWoS impact until physical deliveries occur.*

**Jensen Huang at Trump-Xi summit (May 18) — expects China opening:** NVIDIA CEO Jensen Huang accompanied President Trump on his state visit to China and stated he expects Chinese authorities to eventually allow US AI chip imports. Huang confirmed NVIDIA has received purchase orders from Chinese customers and is restarting H200 manufacturing for that market. Source: Bloomberg / CNBC, 2026-05-18. *Thesis bearing: Confirms demand appetite; the political pathway for China revenue recovery appears more open than it did two weeks ago. Key risk remains Beijing enforcement unpredictability.*

**Pre-earnings final setup (earnings tonight, May 20 after close):** Wall Street consensus sits at $79.2B revenue (+77% YoY) and $1.78 adjusted EPS. Data Center segment projected at ~$72.8B. Gross margin expected >74%. Market will focus on Q2 FY2027 guidance and commentary on: Blackwell demand, Vera Rubin shipment cadence, China revenue, and whether hyperscaler capex commitments are holding. Stock closed May 19 at $222.32 (−1.33%), with $4.71 pre-market upside. Polymarket prices 97% probability of a beat. Source: S&P Global / Kiplinger / 247WallSt, 2026-05-19. *For the portfolio: Q2 guidance is the primary output to watch — it propagates directly into TSM CoWoS demand and MU HBM capacity allocation for 2H 2026.*

**Hyperscaler capex reaches $725B in 2026 (+77% YoY):** Analysis from Tom's Hardware and Futurum Group puts combined Amazon, Microsoft, Google, and Meta capex for 2026 at $725B, up 77% from 2025, with ~75% ($450B+) directed at AI infrastructure. Individual estimates: Amazon ~$200B, Alphabet ~$175–$185B, Meta ~$115–$135B, Microsoft ~$120B. This is the largest concentrated infrastructure cycle in tech history. Source: Tom's Hardware / Futurum / Yahoo Finance, 2026-05. *Thesis bearing: Strongly confirms — the $725B figure represents 2.3× the ~$320B+ baseline framed in the portfolio thesis. Every dollar flowing into AI infrastructure chips, packaging, memory, and networking benefits one or more of the six satellite picks.*

---

### 2026-05-20

**Q1 FY2027 earnings — tonight after close (results pending):** NVIDIA reports Q1 FY2027 results after market close today. Actual numbers not yet available for this scan; they will be captured in tomorrow's update. Setup: Wall Street consensus $78.8–$79.2B revenue (+77–78% YoY), $1.77–$1.78 adjusted EPS, Data Center >$65B. Q2 FY2027 guidance consensus is ~$87B; the market has flagged that guidance needs to land materially above that to re-rate the stock higher. Options markets priced an 8–10% move in either direction. Source: Kiplinger / HeyGoTrade / TradingKey, 2026-05-20. *Watch for tomorrow: Q2 guidance, Blackwell demand cadence, Vera Rubin supply, and China revenue commentary — these are the portfolio's leading indicators for TSM CoWoS and MU HBM demand through 2H 2026.*

**Pre-earnings rally — stock at $236 (+4.5%), market cap $5.71T:** NVDA rallied 4.5% to $236 heading into the earnings print, capping a ~20% monthly rally. Market cap is $5.71 trillion, making NVIDIA one of the two most valuable public companies in the world. Stock's 52-week range: $129.16–$236.54; closed May 20 near the top of the range. Source: 247WallSt / BitMEX, 2026-05-20. *Context: The pre-earnings rally implies significant beat-and-raise is already priced in — Q2 guidance execution will determine the post-earnings direction.*

### 2026-05-21

**Q1 FY2027 ACTUAL RESULTS — BLOCKBUSTER BEAT AND RAISE (THESIS CONFIRMATION):** NVIDIA reported Q1 FY2027 on May 20, 2026, after market close. Key results:
- **Revenue:** $81.6B (+85.2% YoY), beat $80.4B consensus by $1.2B
- **Data Center:** $75B (+92% YoY, +21% QoQ) — dominant segment
- **Net income:** $58.3B (+210.6% YoY)
- **Diluted EPS (non-GAAP):** $2.39, beat $1.79 estimate by ~34%
- **Gross profit:** $61.2B (+129.3% YoY)
- **Cash from operations:** $50.3B (+83.6% YoY)
- **Q2 FY2027 guidance:** $91B ± 2% — substantially above consensus of $85–87B and whisper number of ~$90B
- **Dividend raise:** Quarterly dividend raised from $0.01 to $0.25 per share
Source: CNBC / Quiver Quantitative / StockTitan / Motley Fool Transcript, 2026-05-20.

*Jensen Huang quote:* "This was an extraordinary quarter. Demand has gone parabolic. The reason is simple: Agentic AI has arrived." *Thesis bearing: STRONGLY CONFIRMS the entire portfolio thesis. The $91B Q2 guide vs. $85–87B consensus is the most important single number of the scan — it implies the AI infrastructure buildout is accelerating, not plateauing. Data Center at $75B (+92% YoY) flows directly through TSMC CoWoS and HBM demand from Micron and SK Hynix. The beat-and-raise propagates forward: every TSM wafer and every MU HBM4 contract is underpinned by this demand trajectory. This print confirms the investment thesis for all six satellite positions simultaneously.*

**Portfolio read-through:** Q2 guidance of $91B, up from Q1's $81.6B, requires proportionally more TSMC CoWoS capacity and HBM from Micron/SK Hynix. The cadence: NVDA guidance → TSM CoWoS ramp → MU HBM contract extensions → ASML machine orders (18-month lag). All four are directly connected.

**$80B share repurchase + 25× dividend hike:** Alongside earnings, NVIDIA announced $80B in additional buyback authorization and raised its quarterly dividend from $0.01 to $0.25/share — a 25× increase. Source: NVIDIA 8-K, 2026-05-20. *Thesis bearing: Confirms — management is signaling that FCF generation ($96.7B in FY2026) is sustainable and durable enough to return capital at scale. This is the behavior of a structurally profitable monopoly, not a cyclical hardware vendor.*

**Post-earnings stock reaction:** NVDA fell ~1.26% after hours following the print, despite the significant beat-and-raise. Intraday price on May 21: $220.66 (52-week range $129.16–$236.54). The muted reaction reflects that the consensus (97% Polymarket beat probability) had already priced in an extraordinary quarter — incremental upside required guidance materially above the ~$90B whisper. $91B guidance landed at the whisper, not above it. Source: Reuters / CNBC / Polymarket, 2026-05-21. *Thesis bearing: Neutral — the execution is exceptional; the stock's non-reaction is a valuation signal, not a thesis signal.*

**DCF valuation — Session 1 (2026-05-21):** Damodaran FCFF model with FY2026 inputs ($215.9B revenue, $137.3B EBIT, 63.6% EBIT margin) and 22% 10-year revenue CAGR assumption yields **Intrinsic Value $156.27 vs. current price $220.66 → MoS -29.2% → SELL/AVOID** under high-uncertainty framework. WACC 13.06% (high growth), 9.88% (stable). Key sensitivity: bull case 30% CAGR → IV ~$210; bear case 15% CAGR → IV ~$110. The DCF reflects conservative mean-reversion of growth from FY2027's ~60% YoY trajectory toward long-run 22%; the stock is priced for a more aggressive scenario. See `valuation/outputs/NVDA-dcf.md`. *Thesis bearing: Challenges market price but not the business thesis — NVDA is the strongest business in this portfolio; it is simply priced for perfection. Hold if already owned; do not add at current levels.*

### 2026-05-24

**Rubin GPU 2026 production target cut ~25% due to HBM4 shortage:** KeyBanc analyst John Vinh reported NVIDIA has reduced its 2026 Vera Rubin GPU production plan from ~2 million to ~1.5 million units. The bottleneck is HBM4 certification delays at SK Hynix and Micron — both are still qualifying their HBM4 stacks for Rubin's memory interface. KeyBanc maintains Overweight, raised PT to $300, and characterized the cut as "limited impact" given sustained Blackwell demand absorbing any near-term Rubin shortfall. Source: SDxCentral / BigGo Finance / KeyBanc analyst note, May 2026. *Thesis bearing: Challenges (supply-side) — HBM4 certification delays defer Rubin volume to late 2H 2026 or early 2027 rather than mid-2026. Does not change the thesis that NVDA captures the AI buildout; does imply revenue recognition from Rubin is backend-loaded. Read-through for MU: HBM4 qualification race remains active — Micron is a contender; first certification win is a major catalyst.*

**H200 China deliveries remain at zero despite US approval:** No H200 chips have been physically delivered to any Chinese buyer, despite the US Department of Commerce approving 10 Chinese firms (Alibaba, Tencent, ByteDance, JD.com, Lenovo, Foxconn) for 75,000-unit purchases. The stall is structural: US terms require chips be "used only in China," while Beijing has instructed its tech companies to limit Nvidia use to overseas operations — making compliance with both simultaneously impossible. USTR Jamieson Greer confirmed semiconductors were not on the Trump-Xi bilateral summit agenda (May 13-15). Source: Tom's Hardware / WinBuzzer / TechRepublic / CNBC, May 2026. *Thesis bearing: Challenges — China revenue recovery is effectively frozen indefinitely by conflicting jurisdictional requirements. Zero H200 deliveries since December 2025. No NVDA data center China revenue until one government changes its terms. Risk to model: the DCF does not assume China revenue recovery; this is a confirmed zero-contribution line.*

**Wall of analyst upgrades post-Q1 FY2027 earnings (May 21-22):** Following the $81.6B Q1 beat and $91B Q2 guide, multiple analysts raised PTs: KeyBanc $300 (from $275, Overweight), HSBC $325 (from $295, Buy), DA Davidson $300 (from $250, Buy), Morgan Stanley $285 (from $260, Overweight), Wedbush $300 (Outperform, Dan Ives). Consensus across 62 analysts: Strong Buy, average PT $294.22 — representing ~37% upside to current ~$214 price. Source: StockAnalysis / Benzinga / MarketBeat, May 21-22, 2026. *Thesis bearing: Confirms — the street's consensus PT of $294 is nearly 2× the model's IV of $156 and underscores that the market is pricing a far more aggressive growth scenario than the conservative DCF. The DCF is right to flag SELL/AVOID; the business remains exceptional.*

**AMD competitive position update (May 2026):** AMD launched Ryzen AI 400/AI Max+ and extended MI455 accelerator roadmap. ROCm software narrowing the gap with CUDA but remains meaningfully behind — adoption rates in major AI training workloads still heavily NVIDIA. Custom ASIC programs (Trainium, TPU, Maia) continue to gain traction specifically for inference, not training. No major design win shifts to report. Source: SDxCentral / Deriv analysis, May 2026. *Thesis bearing: Neutral — CUDA moat intact at this assessment interval. Custom ASIC substitution risk is long-dated (2027+) for training workloads; inference substitution is happening but the overall market growing fast enough that NVIDIA absolute revenue is unaffected.*

---

## Cross-links

- [[TSM]] — sole manufacturer; Blackwell on N4/N3 + CoWoS; NVIDIA supply constrained by TSMC CoWoS
- [[MU]] — Blackwell requires HBM3E; Micron is a qualified supplier alongside SK Hynix
- [[ASML]] — upstream; NVDA demand drives TSMC EUV machine orders
- [[MRVL]] — Marvell designs custom ASICs that may partially substitute for NVIDIA GPUs at hyperscalers; complementary and competitive
- [[ANET]] — Arista networking connects NVIDIA GPU clusters; co-dependent
- [[HBM]] — Blackwell HBM3E requirement drives MU and SK Hynix HBM revenue
- [[cowos]] — TSMC CoWoS packages HBM onto Blackwell; was the binding supply constraint
