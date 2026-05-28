# Astera Labs, Inc. (ALAB)

> The connectivity chip company that makes AI GPU clusters physically possible at scale —
> high-speed PCIe/CXL retimers and optical interconnects for hyperscaler AI infrastructure.

*Last updated: 2026-05-28 (Session 33) | Q1 2026 financials pulled from 10-Q/8-K SEC filings*

---

## Overview

- **Business model:** Fabless semiconductor company. Designs high-speed connectivity chips that ensure signal integrity across cables and connectors in large-scale AI GPU clusters. Manufacturing outsourced to TSMC.
- **Value chain position:** Sits between the GPU (NVIDIA/AMD) and the rest of the data center infrastructure — cables, switches, servers. Without reliable high-speed interconnects, large GPU clusters suffer signal degradation that reduces utilization.
- **Founded:** 2017, Santa Clara, California. HQ in Santa Clara.
- **Listed:** NASDAQ: ALAB (IPO March 2024)
- **Scale:** ~500+ employees (lean fabless model).
- **Market cap:** *(update)*

### Why ALAB Is in This Portfolio
As AI clusters scale from hundreds to tens of thousands of GPUs, the physical interconnect layer becomes a bottleneck. Running PCIe Gen 5/6 and CXL across the lengths of cables required in a rack or between racks introduces signal degradation. Astera's retimers solve this — they clean and re-amplify the signal, ensuring full-speed operation. Every major hyperscaler building large-scale GPU clusters needs retimers. ALAB is Atreides Management (Gavin Baker) top holding at $369M.

### Product Lines
| Product | Protocol | Use Case |
|---|---|---|
| Aries | PCIe / CXL | Smart cable modules and retimers for GPU-to-CPU and GPU-to-GPU connectivity |
| Taurus | Ethernet | High-speed ethernet retimers for AI networking switches |
| Leo | Optical / CXL | Active electrical cables and optical interconnects for rack-scale AI systems |

**CXL (Compute Express Link):** CXL is the next-generation interconnect that allows GPUs, CPUs, and memory to share a unified memory pool. As AI models grow too large for a single GPU's HBM, CXL enables memory pooling across devices. Astera is the leading CXL chip supplier — this is a structural growth driver as AI models scale.

---

## Moat

### First-Mover in CXL Connectivity
Astera was first to market with production CXL retimers and smart cable modules. CXL ecosystem development requires co-design relationships with hyperscalers — Astera has these with Microsoft, Meta, and Google. First-mover advantage compounds as hyperscalers build their data center infrastructure on Astera's chips.

### Hyperscaler Co-Design Lock-in
Astera's chips are validated and certified by hyperscaler customers. Changing connectivity chip suppliers requires re-qualification — long cycle (12–18 months), high switching cost. Once designed into a rack architecture, Astera is sticky for the life of that architecture (3–5 years).

### PCIe Gen 5/6 Signal Integrity Expertise
Signal integrity at PCIe Gen 5 (32 GT/s) and Gen 6 (64 GT/s) speeds requires deep electrical engineering expertise. Astera's team has PhDs in signal processing and mixed-signal design — this is not easily replicated. As PCIe speeds double each generation, the signal integrity problem gets harder and Astera's moat deepens.

### TSMC Manufacturing Access
As a TSMC customer on advanced nodes, Astera benefits from TSMC's process advantages — high yields and fast time-to-market for new process nodes.

---

## Financials

*Data pulled by Saturn agent on 2026-05-22 from Q1 2026 10-Q (SEC) and prior earnings releases.*

**Note:** Astera IPO'd in March 2024; historical data limited to ~2 years of public filings.

### Quarterly Revenue ($M)

| Quarter | Revenue | QoQ % | YoY % |
|---|---|---|---|
| Q1 2024 | $65.3M | — | +269% |
| Q2 2024 | $76.9M | +18% | +619% |
| Q3 2024 | $113.1M | +47% | +206% |
| Q4 2024 | $141.1M | +25% | +179% |
| Q1 2025 | $159.4M | +13% | +144% |
| Q2 2025 | $191.9M | +20% | +149% |
| Q3 2025 | $230.6M | +20% | +104% |
| Q4 2025 | $270.6M | +17% | +92% |
| Q1 2026 | **$308.4M** | **+14%** | **+93%** |
| Q2 2026E | ~$360M | ~+17% | ~+88% |

### Income Statement — Q1 2026 (GAAP, $M)

| Item | Q1 2026 | Q1 2025 |
|---|---|---|
| Revenue | $308.4M | $159.4M |
| Gross Profit | $235.1M (76.3% GM) | — |
| R&D Expense | $125.6M | $64.6M |
| S&M | $21.9M | — |
| G&A | $25.8M | — |
| Operating Income | $61.8M (20.0% margin) | — |
| Net Income | $80.3M | — |
| Diluted EPS (GAAP) | $0.44 | — |
| Diluted EPS (non-GAAP) | $0.61 | $0.33 |
| Diluted Shares | ~182.5M | — |

### Annual Summary

| Year | Revenue | YoY % | Gross Margin | EBIT Margin | Net Income | FCF |
|---|---|---|---|---|---|---|
| FY2024 | $396.3M | +242% | ~73% | ~18% | ~$72M | — |
| FY2025 | $852.5M | +115% | 75.7% | 20.3% | $219.1M | $281.8M |

### Balance Sheet — Q1 2026 (March 31, 2026)

| Item | Value |
|---|---|
| Cash + ST Investments | $1,200M |
| Total Liabilities | $165.3M |
| Long-term Debt | $0 (debt-free) |
| Goodwill (post-$74M acquisition) | $87.7M |
| Est. Book Value of Equity | ~$1,400M |

### TTM (Q2 2025 – Q1 2026)

| Item | TTM Value |
|---|---|
| Revenue | ~$1,001.5M |
| Est. EBIT (GAAP ~20% margin) | ~$200M |
| R&D Expense | ~$411M |
| D&A | ~$15M (annualized from Q1 $3.7M) |
| Est. CapEx | ~$8M (fabless; very light) |

---

## Revenue Segments

**Q1 2026 product mix:** PCIe Gen 6 (Aries) contributed >1/3 of Q1 2026 revenue. Scorpio X-Series AI fabric switches are ramping and are expected to become the largest product line by year-end 2026. Leo (optical interconnects) growing. CXL contribution still small but ramping with Microsoft and Meta pilots.

**Customer concentration:** Amazon (Trainium3), Microsoft, Meta and Google represent a large % of revenue. Amazon Trainium3 is the most visible named design win as of Q1 2026 — Scorpio X switches are the connectivity fabric for Amazon's primary AI accelerator. Concentration risk exists but also signals deep co-design relationships.

---

## Growth Drivers

### 1. AI Cluster Scale-Out
Every GPU added to a cluster requires more connectivity chips. As clusters grow from 10K to 100K+ GPUs, retimer demand grows proportionally. The $725B+ 2026 hyperscaler CapEx translates directly into Astera TAM expansion.

### 2. CXL Memory Pooling Adoption
CXL 2.0 and 3.0 enable memory pooling — critical for models too large for single-GPU HBM. As AI models grow (Gemini, GPT-6, etc.), CXL becomes structurally necessary. Astera is the leading CXL chip supplier. This is a 2026–2028 growth driver on top of the existing retimer business.

### 3. PCIe Gen 6 Upgrade Cycle
Each PCIe generation doubles throughput and requires new retimers. Gen 6 adoption in AI servers (2026–2027) forces a hardware refresh that drives Astera revenue.

### 4. Optical Interconnect (Leo)
As rack-scale AI systems grow beyond what electrical cables can handle, active optical cables (AOC) and co-packaged optics become necessary. Astera's Leo product line addresses this. The XPO MSA optical standard (announced 2026) opens a new market.

---

## Risks

### Customer Concentration
Top 3–5 hyperscalers likely represent >80% of revenue. A single hyperscaler pausing AI infrastructure CapEx or switching to a competitor's connectivity solution has an outsized revenue impact.

### Competitive Threat — Broadcom, Marvell, Texas Instruments
Larger semiconductor companies have retimer products. Broadcom and Marvell compete directly. TI has lower-end retimers. At the high end (PCIe Gen 6, CXL 3.0), Astera has a technology lead — but larger competitors have more resources to close the gap.

### Valuation Risk
Astera IPO'd in 2024 and the stock has re-rated significantly on AI infrastructure enthusiasm. A multiple compression event (even without a fundamental miss) could be painful. The stock is priced for continued execution at a high multiple.

### CXL Adoption Timing
CXL memory pooling has been "next year" for several years. If hyperscaler adoption of CXL-based memory pooling is slower than expected, a key growth driver is delayed.

---

## Catalysts

### Active Catalysts
| Catalyst | Expected Timing | Bull Signal | Bear Signal |
|---|---|---|---|
| CXL 3.0 design wins at hyperscalers | 2026–2027 | Multiple hyperscaler CXL deployments confirmed | Hyperscalers delay CXL adoption |
| PCIe Gen 6 ramp in AI servers | 2026–2027 | NVIDIA/AMD Gen 6 GPU server ramp | Gen 5 longevity longer than expected |
| XPO MSA optical standard adoption | 2026 | Hyperscalers commit to XPO MSA interconnects | Competing standard wins |
| Revenue growth sustaining >100% YoY | Quarterly | Growth maintained above consensus | Growth decelerates sharply |

| Scorpio X 320 Lane shipping — hyperscaler ramp | 2026 H2 | ALAB confirms ramp to becoming largest product line | Q3 underdelivery vs. consensus |
| Computex 2026 showcase | 2026-06-02 | First in-person demo of PCIe 6 scale-up optics draws hyperscaler attention | No-show or negative commentary |
| Q2 2026 earnings | ~Aug 2026 | Revenue >$365M confirms Scorpio X ramp on track | Miss or guide-down |

### Archived Catalysts
*(Move here once played out)*

---

## Monitoring Checklist

**Quarterly (earnings):**
- [ ] Revenue YoY growth — sustaining 100%+ is the bull case; deceleration is the key risk
- [ ] Gross margin — connectivity chips should carry 60%+ GM; watch for pricing pressure
- [ ] Customer concentration — any change in top 3 customer % of revenue
- [ ] CXL product revenue — when does CXL become a material revenue contributor?
- [ ] Management commentary on hyperscaler CapEx spending and design win pipeline

**Leading indicators:**
- [ ] Hyperscaler data center CapEx guidance — direct demand signal for Astera
- [ ] NVIDIA GPU cluster architecture announcements — new architectures require new retimers
- [ ] CXL consortium announcements — ecosystem development pace
- [ ] Broadcom/Marvell retimer competitive updates

---

## Investment View

*(Populate: Valuation, WACC, DCF, Reverse DCF, Scenarios, Decision Log)*

### Decision Log

*(Append-only — no entries yet)*

---

## Recent Updates

### 2026-05-19

**J.P. Morgan TMC Conference — Scorpio X ramp confirmed, stock surges +12–16%:** ALAB management presented at the J.P. Morgan 54th Annual Global Technology, Media and Communications Conference in Boston (May 19). CEO explicitly confirmed Scorpio X-Series 320-lane AI fabric switches are on track to become the largest product line by year-end 2026 — a major product mix upgrade from the legacy P-Series PCIe retimer position. ALAB surged 12.58%–16% on May 19 (touching $255.96 intraday), directly attributable to the conference presentation + simultaneous analyst upgrades from JPMorgan ($280 PT, Overweight), Roth MKM ($275, Buy), Needham ($260), and Stifel ($260). Source: J.P. Morgan conference transcript / Invezz / TradingKey / StocksToTrade, 2026-05-19. *Thesis bearing: Confirms — management's on-record ramp timeline for Scorpio X at a major institutional venue, combined with a wave of new analyst coverage, directly validates the scale-up switch layer of the thesis; the +16% move reflects institutional repricing of the product mix story.*

---

### 2026-05-21

**Q1 2026 record revenue — $308.4M:** Astera Labs reported Q1 2026 revenue of $308.4M with net income of ~$80.3M (net margin >25%), gross margin ~75.7%. The company carries no long-term debt and holds ~$1.18B in cash and short-term investments. This confirms the business is both high-growth and profitable — a rare combination at this stage of the AI infrastructure buildout. Source: StocksToTrade / TimothySykes / InsiderMonkey, 2026-05-20. *Thesis bearing: Confirms — record quarterly revenue with expanding margins validates the thesis that AI cluster scale-out is translating directly into ALAB revenue; the cash-rich, debt-free balance sheet reduces dilution risk.*

**Amazon Trainium3 ramp — Scorpio X switch design win:** RBC Capital reiterated Outperform and raised price target from $225 to $250, citing Amazon's preparation to ramp its Trainium3 AI chips. RBC analyst Srini Pajjuri expects Astera's Scorpio X switches to ramp into Amazon Trainium3 racks in Q3 2026, tied to Amazon's expanded partnership with Anthropic. The AWS AI infrastructure buildout tied to the Amazon-Anthropic deal is a direct demand signal for ALAB's connectivity layer. Source: RBC / InsiderMonkey / TipRanks, 2026-05-20. *Thesis bearing: Confirms — a named Amazon Trainium3 design win (via RBC channel checks) upgrades ALAB from "hyperscaler connectivity supplier" to "named ramp partner in the most watched AI infrastructure program at AWS in 2026." Scorpio X switch ramping in Q3 provides near-term revenue visibility.*

**+57% stock rally (Apr 28 → May 20):** ALAB rose from ~$183 on April 28 to ~$285 on May 20 — approximately +57% in three weeks — driven by the Amazon Trainium3 ramp visibility and broader AI infrastructure enthusiasm from NVDA's blowout earnings. Market cap reached $49.23B on May 21 at $288.06. Source: StockAnalysis, 2026-05-21. *Thesis bearing: Neutral — the thesis is confirmed by the design win; the rapid multiple expansion creates valuation risk if near-term execution disappoints. Not a BUY trigger at current price without DCF validation.*

**Analyst coverage — Barclays and Citi target raises:** Barclays and Citi also raised price targets citing strong product portfolio ramp-up, complementing the RBC move. Source: StocksToTrade, 2026-05-20. *Thesis bearing: Confirms — broad analyst upgrades suggest institutional awareness of the Amazon Trainium3 design win is widening.*

**Hyperscaler capex backdrop — $725B in 2026:** Combined Amazon, Microsoft, Google, and Meta capex for 2026 is tracking $725B (+77% YoY), with Amazon alone at ~$200B. AWS Trainium3 is the primary ALAB growth lever within this — ALAB's Scorpio X switch is the connectivity layer for Amazon's most important AI accelerator. Source: Tom's Hardware / Futurum Group, 2026-05. *Thesis bearing: Confirms — the macro backdrop is the strongest in the portfolio's history; ALAB's Amazon Trainium3 design win positions it directly within the largest single hyperscaler AI spend.*

---

### 2026-05-22

**Analyst price target escalation — RBC raises to $270 (second raise in 3 days), Evercore ISI raises to $297:** RBC Capital raised its price target on ALAB a second time this week — from $250 to $270 (prior raise was $225→$250 on May 20) — maintaining Outperform. Evercore ISI raised to $297 from $215, maintaining Outperform. Both firms cited Amazon Trainium3 ramp visibility and the broader hyperscaler capex acceleration as drivers. Evercore's $297 target is the highest on the Street and implies further upside to the current price. Source: Evercore ISI / RBC Capital / StocksToTrade, 2026-05-22. *Thesis bearing: Confirms — two independent research firms raising PTs rapidly (Evercore +38% in one move) reflects growing institutional conviction that the Amazon Trainium3 design win is not fully priced in; the rapid pace of revision suggests analyst models are still catching up to the demand ramp.*

**Q2 2026 revenue guidance — up to $365M (+18% QoQ):** Reiterated from Q1 2026 earnings (reported May 5): management guided Q2 2026 revenue at up to $365M — an 18% sequential increase from Q1's record $308.4M. Scorpio X-Series scale-up switches are expected to become the largest product line by year-end 2026, surpassing P-Series (PCIe retimers). PCIe Gen 6 contributed >one-third of Q1 revenue. Source: Astera Labs Q1 2026 8-K / Motley Fool earnings transcript, 2026-05-05. *Thesis bearing: Confirms — the sequential growth acceleration driven by Scorpio X ramp into Amazon Trainium3 provides near-term revenue visibility through mid-2026; PCIe Gen 6 > one-third of revenue confirms the upgrade cycle thesis is materializing.*

**New 52-week high $315.73 — stock ~$309.78 in after-hours (+7.5% from $288.06 close):** ALAB set a new 52-week high of $315.73 during May 22 trading, closing near $309.78 — a gain of approximately +7.5% from the prior Session 6 reference price of $288.06. The Benzinga "Why Is Astera Labs Trending Overnight?" headline indicates continued after-hours momentum. Market cap at $309.78 is approximately $53B. **>3% trigger: adding to event_queue for Session 8 deep dive.** Source: Benzinga / StockAnalysis / MarketBeat, 2026-05-22. *Thesis bearing: Neutral — the thesis is confirmed by the Amazon Trainium3 design win and Q2 guide; the rapid price appreciation from ~$183 on April 28 to $309.78 on May 22 (+69% in 25 days) compresses the margin of safety. DCF validation needed before this is a BUY.*

**Session 8 DCF — first valuation run (ALAB dcf_last_run was null):** Saturn agent ran the first ALAB DCF model on 2026-05-22 using TTM financials (Q2–Q4 2025 + Q1 2026). Key inputs: TTM revenue $1,001.5M, TTM GAAP EBIT ~$200M, R&D capitalized from 5-year history, shares 182.5M diluted, price $309.78. See `valuation/outputs/ALAB-dcf.md` for full output. The DCF result is the primary decision input in `decisions/tracker.md` Session 8 update.

**ANET Arista Networks — >3% move today (+3.1%), flagging for event_queue:** Arista Networks rose +3.08% on May 22 to close at $148.59 (from prior close of ~$140.49). Catalyst: Arista named a Gartner Magic Quadrant Leader for Enterprise LAN, Q1 2026 earnings beat + full-year revenue outlook raised, new ruggedized switch products announced. Zacks downgraded to Hold on May 16 citing valuation, but market focused on the fundamental beat and Gartner recognition. NVDA's entry into Ethernet switching noted as a "real competitive overhang" but not yet impacting results. Source: TradingKey / Zacks, 2026-05-22. *Not an ALAB thesis bearing update — noted here for cross-portfolio awareness; ANET >3% move added to event_queue for next rotation.*

### 2026-05-25

**ESUN competitive risk (Oct 2025 retroactive context) — Arista entering scale-up switching in 2027:** Arista Networks unveiled the ESUN (Ethernet for Scale-Up Networks) initiative at the OCP Global Summit on October 13, 2025. ESUN is an open standard for GPU-to-GPU scale-up networking using Ethernet (vs. NVLink/InfiniBand). Founding members: AMD, Arista, ARM, Broadcom, Cisco, Marvell, Meta, Microsoft, Nvidia, OpenAI, Oracle — now grown to 175+ companies. Arista has stated it will enter scale-up switching with ESUN-compatible products beginning 2027, directly competing with ALAB's Scorpio X scale-up switches. ALAB fell ~15% to ~$168 on October 14, 2025 when Arista published its ESUN blog post; the stock has since tripled to $305+ as Amazon Trainium3 design wins for Scorpio X confirmed hyperscaler lock-in (12–18 month re-qualification cycle). Note: Marvell (ESUN founding member) has SerDes/DSP and optical IP embedded in the ESUN stack — MRVL benefits from the standard regardless of who wins the switch layer. Source: OCP / Arista blogs.arista.com / TipRanks / Seeking Alpha "Why ESUN Could Shake Its Growth", 2025-10–2026-05. *Thesis bearing: Challenges (partially discounted) — Arista's 2027 ESUN switch entry is the primary long-term structural risk to ALAB's Scorpio X total addressable market; the October 2025 stress test (−15%) and recovery to ATH suggests the market has partially discounted this risk on the basis of ALAB's confirmed Amazon design wins. Monitor Arista's FY2027 product roadmap announcements for ESUN switch specifics and timeline acceleration.*

### 2026-05-26

**Scorpio X 320 Lane formally confirmed shipping to hyperscalers; Computex 2026 (June 2-5) upcoming showcase:** Astera Labs issued the official press release (GlobeNewswire, May 5, 2026) confirming the 320 Lane Scorpio X-Series Smart Fabric Switch is now shipping to leading hyperscalers, with production ramp in 2H 2026. Key specs: industry's largest open, memory-semantic fabric switch; hardware-accelerated Hypercast and In-Network Compute engines boosting collective operations by up to 2×; engineered to improve token economics for large-scale AI clusters. The target market: merchant scale-up switch silicon projected to reach $20B by 2030. Astera will showcase the 320 Lane at Computex 2026 (Taipei, June 2-5), alongside first industry demos of PCIe 6 scale-up optics — the first major in-person hyperscaler-facing visibility event for the Scorpio X at full ramp. Source: GlobeNewswire / Investing.com / ServeTheHome, 2026-05-05. *Thesis bearing: Confirms — the formal shipping confirmation and $20B TAM quantification anchor Scorpio X as the company's primary revenue driver through 2030; Computex 2026 will be the first institutional-visibility event for the 320 Lane at production scale, and hyperscaler commentary there will be a leading indicator for Q3 2026 design win momentum.*

**Marvell 260-lane PCIe 6.0 Switch + CEO keynote at Computex — direct Scorpio X competition escalates:** In March 2026, Marvell Technology announced an industry-first 260-lane PCIe 6.0 Switch for AI Data Center Scale-up Infrastructure — the first direct named competitor to ALAB's Scorpio X 320-lane product. Marvell CEO Matt Murphy will deliver the Computex 2026 keynote on June 2 entitled "The Future of AI Scaling Depends on Connectivity," where he will discuss Marvell's optical and connectivity strategy built on a three-layer photonic IP stack (Celestial AI $3.25B acquisition + Polariton + legacy SerDes/DSP). ALAB will also be at Computex demoing the 320-lane with PCIe 6 optics — making June 2-5 the first direct head-to-head in-person showcase between the two companies' scale-up switch products at a major institutional audience. MRVL's product has fewer lanes (260 vs. 320) but broader hyperscaler relationships (Google TPU, Amazon Trainium co-design), a complete photonic stack, and balance sheet resources far exceeding ALAB's. Source: StockTitan / NVIDIA GTC Taipei / Computex 2026 keynote schedule / Marvell investor relations, 2026-05-26. *Thesis bearing: Challenges — the ESUN risk (Arista 2027) was already in the entity; the MRVL 260-lane switch is a current, shipping competitive product arriving at the same Computex venue where ALAB will debut PCIe 6 optics. MRVL's photonic IP stack (Celestial AI + Polariton) is more comprehensive than ALAB's Leo product. At SELL/AVOID with IV $111.84 vs. $305 price (MoS -63.3%), this is an additional reason the risk/reward is unfavorable — the moat is narrower than the price implies.*

### 2026-05-28

**ALAB joins NVIDIA NVLink Fusion ecosystem as connectivity partner for hybrid racks — a thesis upgrade:** Astera Labs announced "Astera Labs Expands Collaboration with NVIDIA to Advance NVLink Fusion Ecosystem," making ALAB among the first companies to adopt NVLink Fusion for custom connectivity solutions. The partnership enables "hybrid rack" architectures: non-NVIDIA accelerators (hyperscaler XPUs such as Amazon Trainium and Google TPU) interface with NVIDIA AI factory infrastructure via NVLink Fusion-compatible ALAB connectivity chips. Key technical detail: ALAB's Aries PCIe/CXL retimers have been deployed in volume across NVIDIA Hopper and NVIDIA HGX platforms for multiple generations; the NVLink Fusion collaboration extends this into next-gen heterogeneous racks. Custom solutions sustain "multiple terabytes per second of low-latency data throughput." ALAB becomes the connectivity enabler within the NVIDIA ecosystem rather than an independent competitor at the edge of it. Source: Astera Labs IR / ir.asteralabs.com / stocktitan.net, 2026-05. *Thesis bearing: Confirms (thesis upgrade) — prior framing: ALAB competes with MRVL at the PCIe/CXL switch layer. New framing: ALAB and MRVL are both inside the NVIDIA NVLink Fusion stack playing complementary roles — MRVL (custom XPU co-design + optical scale-up) and ALAB (PCIe/CXL connectivity retimers and switches for hybrid racks). This reduces MRVL vs. ALAB zero-sum framing and elevates both as NVIDIA ecosystem beneficiaries. The moat implication: NVIDIA-certified NVLink Fusion connectivity creates a qualification cycle (12–18 months) that raises the barrier for substitution.*

**10 hyperscaler/AI platform customer engagements; targeting "a couple" of design wins by year-end 2026:** Management disclosed 10 active customer engagements across hyperscalers and AI platform providers for scale-up switch and custom connectivity solutions. Management expects to convert "a couple" into confirmed design wins by year-end 2026, creating revenue opportunities beginning in 2027. This is the first time ALAB has publicly quantified the engagement pipeline size. For context: the confirmed Amazon Trainium3 design win was ALAB's most visible win; the 10-engagement pipeline suggests meaningful diversification beyond Amazon into 3–4 additional hyperscalers. Source: TIKR / TradingView / analyst Q&A at investor conferences, May 2026. *Thesis bearing: Confirms — 10 engagements with conversion expected by year-end upgrades the pipeline from "Amazon-dependent" to "multi-hyperscaler." However, each conversion cycle is 12–18 months to revenue, meaning FY2027 is the earliest material contribution from new wins.*

**New 52-week high $354.53; 51% 6-day rally; $56B market cap:** ALAB reached a new 52-week high of $354.53 on May 28, 2026, closing at $353.86 (+8.8% from May 27 close of $325.33). The move extends a 51% 6-day rally (from roughly May 20) driven by Q1 2026 beat, Scorpio X ramp visibility, NVLink Fusion partnership announcement, and pre-Computex momentum. Market cap reached approximately $56B. This compares to Atreides Management's reported ~$110 entry (~$369M position per 13F). At $353.86, DCF IV $111.84 → MoS **-68.4%** — deeper into SELL/AVOID territory (down from -63.9% at $309.78 DCF-run price on May 22). The market is pricing continued 50%+ YoY growth execution well beyond the conservative DCF scenario. Source: TradingView / Trefis / Tradingkey, 2026-05-28. *Thesis bearing: Neutral (business thesis confirmed; valuation thesis challenged further — market is increasingly ahead of DCF). No change to recommendation: SELL/AVOID.*

**Q2 2026 guidance precision ($355–$365M, non-GAAP EPS $0.68–$0.70):** The Q1 2026 earnings call (May 5, 2026) provided a precise Q2 2026 guide of $355–$365M (vs. the entity's "up to $365M" carrying figure) and non-GAAP EPS $0.68–$0.70 (consensus expected $0.62, implying further beat potential). Q1 actuals confirmed: $308.4M revenue (+93% YoY, +14% QoQ), non-GAAP EPS $0.61 (vs. $0.54 estimate), GAAP gross margin 76.3%, non-GAAP operating margin 36.2%. Scorpio X-Series 320-lane is in initial production volumes with full ramp in 2H 2026. PCIe Gen 6 contributed >1/3 of Q1 revenue. Source: Astera Labs 8-K / Motley Fool earnings transcript, 2026-05-05. *Thesis bearing: Confirms — Q1 beat-and-raise pattern with NVLink Fusion partnership announced concurrently is the combination driving pre-Computex re-rating.*

---

## Cross-links

- [[NVDA]] — primary indirect customer; Blackwell/Vera Rubin GPU clusters drive ALAB demand; ALAB is now an NVIDIA NVLink Fusion ecosystem partner for hybrid-rack connectivity
- [[MRVL]] — overlapping hyperscaler data center exposure; Marvell competes at the custom ASIC level, Astera at the connectivity level; MRVL is also an ESUN founding member; both now inside NVIDIA NVLink Fusion ecosystem
- [[ANET]] — complementary today (Arista handles scale-out, ALAB handles scale-up connectivity); competitive from 2027 as ESUN scale-up switches enter market
- [[TSM]] — manufactures Astera's chips on TSMC advanced nodes
- [[custom-silicon]] — ALAB is now the connectivity layer inside NVIDIA NVLink Fusion ecosystem for custom silicon hybrid racks
