# Marvell Technology, Inc. (MRVL)

> The primary co-designer of custom AI ASICs for hyperscalers —
> the company that enables Google, Amazon, Microsoft, and Meta to reduce their NVIDIA dependency.

*Last updated: 2026-05-27 | Wisesheets data as of: not yet pulled*

---

## Overview

- **Business model:** Fabless semiconductor company. Designs custom ASICs (co-designed with hyperscaler customers), networking silicon, and storage controllers. Manufacturing outsourced primarily to TSMC.
- **Value chain position:** Sits between hyperscalers (who want custom silicon) and TSMC (who manufactures it). Marvell is the engineering intermediary — the hyperscaler provides the architecture vision, Marvell handles the chip design and TSMC qualification.
- **Founded:** 1997, Hamilton, Bermuda (HQ now in Santa Clara, California).
- **Listed:** NASDAQ: MRVL
- **Scale:** ~5,500+ employees (lean for its revenue scale — fabless model).
- **Market cap:** *(update)*

### Why MRVL Is in This Portfolio
Hyperscalers are building custom ASICs to reduce NVIDIA dependency and optimize inference cost. Google TPU, Amazon Trainium/Inferentia, Microsoft Maia, Meta MTIA — Marvell co-designs several of these. This is the second AI silicon wave: even if NVIDIA maintains training GPU dominance, inference will increasingly run on custom silicon. Marvell participates in that trend while also benefiting from data center networking demand.

### Custom Silicon Economics
Custom ASICs optimize for a specific workload (inference, recommendation models, video processing) at lower per-unit cost than general-purpose GPUs. The tradeoff: 18–24 month design cycle, TSMC qualification, large minimum volume commitment. Only hyperscalers with scale can justify this. Marvell's value is providing the ASIC design expertise hyperscalers don't want to fully build in-house.

---

## Moat

### Hyperscaler Co-design Relationships
Marvell has multi-year co-design agreements with major hyperscalers. These relationships involve deep IP sharing and long qualification cycles — not easily terminated. Once a custom ASIC is in production, the hyperscaler is locked in for the chip's 3–5 year production life. The next generation re-starts the co-design process, re-entrenching the relationship.

### SerDes and Optical DSP IP
Marvell has deep intellectual property in SerDes (serializer/deserializer) and coherent optical DSP — the signal processing that makes high-speed data center interconnects work. This IP is embedded in every major hyperscaler's custom silicon and networking design. Difficult to replicate quickly.

### Networking Silicon
Beyond custom AI ASICs, Marvell sells programmable networking chips (Teralynx, Prestera) for data center switching. This is a growing market as GPU cluster scale-out increases east-west traffic.

---

## Financials

*Last pulled: 2026-05-22. Source: SEC 8-K (Q4 FY2026, filed March 5, 2026), MarketBeat, web search.*

**Segment note:** Marvell reports Data Center, Carrier Infrastructure, Enterprise Networking, Consumer, Automotive/Industrial. Data Center is the primary segment — custom AI ASICs are here and growing rapidly.

### Annual Income Statement (USD millions)

| Metric | FY2024 (Jan 2024) | FY2025 (Jan 2025) | FY2026 (Jan 2026) |
|---|---|---|---|
| Revenue | ~$5,510 | ~$5,773 | **$8,195** |
| YoY Growth | — | +4.8% | **+42.0%** |
| GAAP Operating Income | — | — | **-$720** |
| Non-GAAP Operating Income | — | — | **~$2,868** |
| Non-GAAP Operating Margin | — | — | **35%** |
| GAAP Net Income | — | — | **$2,670** |
| R&D Expense (GAAP) | $1,896 | $1,950 | **$2,075** |
| CapEx | — | — | **$354** |
| D&A (PP&E) | — | — | **~$374** |

### Quarterly Revenue (USD millions)

| Quarter | Revenue | YoY | Notes |
|---|---|---|---|
| Q1 FY2026 (May 2025) | $1,891 | — | Estimated (FY2026 total minus Q2-Q4) |
| Q2 FY2026 (Aug 2025) | $2,010 | +58% | |
| Q3 FY2026 (Nov 2025) | $2,075 | +37% | Record at time |
| Q4 FY2026 (Jan 2026) | $2,219 | +22% | Record at time |
| **Q1 FY2027 (Apr 2026)** | **$2,418** | **+28%** | **Beat guide $2.40B by $18M; new record** |

**Management Guidance (from Q1 FY2027 earnings call, 2026-05-27):**
- Q2 FY2027: $2.7B midpoint (±5%); +35% YoY
- FY2027 full year: >30% YoY, approaching ~$11B (raised from ~$10B prior); Q4 FY2027 exit >$3B
- FY2028 first-time guidance: ~$15B (~40% YoY)

### Balance Sheet (as of January 31, 2026)

| Metric | Value |
|---|---|
| Cash & Equivalents | $2,639M |
| Total Debt | $4,471M (short $500M + long $3,971M) |
| Net Debt | ~$1,832M |
| Total Stockholders' Equity | $14,308M |
| Shares Outstanding | 874M |

---

## Revenue Segments

*Update quarterly — Data Center % of revenue is the primary metric; extract AI ASIC revenue commentary separately from general data center.*

FY2026 summary: Data Center is the dominant segment, driving the +42% YoY total revenue growth. Management confirmed AI custom ASIC volume as the primary driver. Carrier Infrastructure, Consumer, and Automotive/Industrial are all declining or flat — legacy mix headwind. Data Center is expected to be >70% of revenue by Q1 FY2027.

---

## Growth Drivers

1. **Google custom AI ASIC co-design (confirmed):** Google is co-designing two chips with Marvell — an inference-optimized TPU and a Memory Processing Unit (MPU, ~2M units planned). Marvell added as a third design partner alongside Broadcom and MediaTek. Multi-year, high-volume program anchors revenue visibility through FY2028+.
2. **Amazon Trainium/Inferentia ramp (confirmed):** AWS Trainium custom silicon (designed with Marvell) ramping at scale for AI inference. Wells Fargo cited AWS Trainium deployment as the primary basis for its $195 price target raise.
3. **Hyperscaler CapEx acceleration:** Combined Amazon/Google/Microsoft/Meta CapEx for 2026 forecast at $600-700B (+36% YoY), 75% directed at AI infrastructure. Custom silicon follows CapEx with a 2-4 quarter lag.
4. **Optical interconnect (co-packaged optics):** Polariton Technologies acquisition (April 2026) adds plasmonics-based silicon photonics for 3.2T+ data center links. Combined with existing SerDes and DSP IP, Marvell becomes a full-stack optical connectivity supplier.
5. **NVIDIA ecosystem integration:** NVIDIA's $2B strategic investment (March 2026) means Marvell connectivity silicon is embedded in NVIDIA-centric GPU clusters as well as the custom ASIC alternative path.

---

## Risks

1. **Customer concentration:** Top 3 hyperscalers likely >60% of AI revenue. One program delay = quarterly miss. Custom ASIC revenue is lumpy by design.
2. **NVIDIA inference dominance:** If NVIDIA maintains inference GPU efficiency (Blackwell NIM deployment), hyperscaler urgency to build custom silicon decreases.
3. **Broadcom competition:** Broadcom co-designs custom ASICs for Google at ~60% market share (vs. Marvell ~25%, per Counterpoint Research). Marvell must win next-gen program iterations.
4. **Design cycle timing risk:** 18-24 month lag from design win to revenue. Program slippage creates revenue miss without public warning.
5. **Valuation risk:** At $178+, stock trades at >50× GAAP earnings. Highly sensitive to execution miss at earnings.
6. **Insider selling:** $27.9M in insider sales (prior 3 months, as of May 2026) with no insider buying — elevated multiples + insider sales = elevated expectations already priced in.

---

## Catalysts

### Active Catalysts

| Catalyst | Expected Timing | Status |
|---|---|---|
| Computex keynote — CEO Matt Murphy | 2026-06-02 | "The Future of AI Scaling Depends on Connectivity"; post-earnings product showcase; first head-to-head with ALAB Scorpio X |
| Trainium volume ramp visibility | H2 2026 | AWS deployment scale-out; $225B committed backlog; WF forecasts $6B/yr MRVL revenue |
| Co-packaged optics revenue (Celestial AI + Polariton) | FY2028 | Integration of 3 photonic IP layers; first combined-product revenue commentary expected FY2028 |
| XConn PCIe 6 / CXL 3.1 design wins | FY2028 | Revenue ~$100M FY2028; Scorpio X head-to-head ongoing at Computex |

### Archived Catalysts

| Catalyst | Date | Outcome |
|---|---|---|
| NVIDIA $2B strategic investment in MRVL | March 2026 | Confirmed; validates optical + custom silicon thesis |
| AMD 13F stake disclosure | 2026-05-13 | MRVL +10% on day; both NVDA and AMD invested = ecosystem validation |
| NVDA Q1 FY2027 earnings read-through | 2026-05-20 | NVDA +85% YoY revenue confirms AI buildout acceleration; MRVL continued rally |
| Q1 FY2027 Earnings | 2026-05-27 | Revenue $2.418B (+28% YoY, beat guide by $18M); EPS $0.80 (beat $0.79 est.); Q2 guide $2.7B (+35%); FY2027 raised to ~$11B; FY2028 first-time guide ~$15B |

---

## Monitoring Checklist

*(Quarterly: Data Center revenue and YoY growth; Custom AI ASIC revenue (if broken out); Management commentary on hyperscaler customer timing; Gross margin direction; Leading: Hyperscaler CapEx guidance — Marvell custom silicon revenue follows with 2–4 quarter lag from design win to shipment)*

---

## Investment View

*(Populate: Valuation, WACC, DCF, Reverse DCF, Scenarios, Decision Log)*

### Decision Log

*(Append-only — no entries yet)*

---

## Recent Updates

### 2026-05-17

**Q1 FY2027 earnings — May 27:** Marvell reports Q1 FY2027 on May 27. Analysts expect management to raise FY2027 and FY2028 revenue growth guidance driven by AI data center strength. Revenue estimates: FY2027 $11.12B, FY2028 $15.35B. Source: TheStreet / GuruFocus, 2026-05.

**AMD 13F stake disclosure (May 13):** AMD's quarterly 13F filing revealed an ownership stake in Marvell Technology. MRVL shares surged 10% on the disclosure. AMD's investment in a company that designs inference silicon for hyperscalers could signal deeper semiconductor ecosystem collaboration or acquisition interest. Source: GuruFocus, 2026-05-13. *Thesis bearing: Bullish signal — AMD validation of Marvell's custom silicon position.*

**Analyst upgrades:**
- Bank of America raised PT to $200 from $125
- Goldman Sachs raised PT to $125 from $100
Source: TheStreet, 2026-05.

**Stock performance:** Up 135% since March 5, 2026; closed May 13 at ~$177.95. Source: GuruFocus, 2026-05-14.

**Insider selling:** $27.9M in insider sales over the last 3 months, no reported insider buying. Source: GuruFocus, 2026-05. *Caution flag — monitor at earnings; insider selling at elevated multiples is not unusual but worth tracking.*

**Valuation note:** GF Value model estimates 60.6% overvaluation at current price vs. intrinsic value of ~$102. Note this is a model-based estimate; the AI ASIC revenue ramp may not be fully captured in historical-model valuations. Source: GuruFocus, 2026-05. *Assessment: Valuation is stretched on backward-looking metrics; forward revenue ramp ($11B+ FY2027) may justify current price if hyperscaler ASIC volumes accelerate on schedule.*

---

### 2026-05-18

**Google / Alphabet AI chip co-design (inference TPU + Memory Processing Unit):** Reports surfaced that Google is in talks with Marvell to co-design two new AI chips: (1) an inference-optimized TPU that is cheaper and more power-efficient than existing designs, and (2) a Memory Processing Unit (MPU) — a memory-centric processor designed to optimize data movement during AI inference workloads. Planned volume: ~2 million MPUs. Google is adding Marvell as a third design partner alongside Broadcom and MediaTek. No signed contract disclosed. MRVL shares surged to an all-time high of $182 on this news (May 14). Source: The Information / The Next Web / FX Leaders, 2026-04-20 / 2026-05-14. *Thesis bearing: Strongly confirms — adds Google to confirmed Marvell ASIC co-design relationships alongside Amazon. Counterpoint Research forecasts Marvell at ~25% of the custom AI accelerator market by 2027 (Broadcom ~60%). TrendForce projects custom chip sales up 45% in 2026 vs. 16% GPU growth.*

**Polariton Technologies acquisition (April 22, 2026):** Marvell announced the acquisition of Polariton Technologies, a Swiss ETH Zurich spin-out that develops plasmonics-based silicon photonics devices. Polariton's technology enables ultra-high-density, low-power optical links for 3.2T+ data center interconnect (DCI) applications including ZR and ZR+ coherent optics. Financial terms not disclosed. This acquisition deepens Marvell's optical technology stack — SerDes + DSP + now plasmonics — for the co-packaged optics transition that AI data centers are moving toward. Source: Marvell Newsroom / Data Center Dynamics / Photonics Spectra, 2026-04-22. *Thesis bearing: Confirms — extends Marvell's IP moat in optical interconnect at exactly the point where AI cluster bandwidth demands are scaling beyond what electrical interconnects can support.*

**Stock and valuation update:** MRVL hit all-time high of $182 on May 14 on the Alphabet chip report. TD Cowen doubled price target to $180. Up 135%+ since early March 2026. May 27 earnings: analysts expect FY2027 guidance raised ($11.12B est.) and FY2028 guide (~$15.35B). Source: FX Leaders / CoinCentral, 2026-05-14. *Note: Insider selling of $27.9M in last 3 months continues — elevated multiples + insider selling = elevated expectations already priced in; earnings execution is critical.*

---

### 2026-05-19

**NVIDIA $2B strategic investment in Marvell (late March 2026 — previously uncaptured):** NVIDIA invested $2 billion in Marvell in late March 2026 — a strategic stake, not just a supply relationship. This positions Marvell as a critical NVDA ecosystem partner: Marvell co-designs the networking silicon and custom ASICs that connect and complement NVIDIA GPU clusters. Following NVIDIA's investment came AMD's $6.5M equity disclosure (May 18), meaning both of Marvell's major compute-silicon competitors have now taken financial stakes. Source: Motley Fool / TheStreet / Intellectia, 2026-05. *Thesis bearing: Strongly confirms — competing semiconductor giants investing in Marvell signals that its connectivity and custom ASIC IP is considered infrastructure-critical across all major AI accelerator architectures. The ecosystem bet hedges across GPU winners.*

**Post-ATH pullback — MRVL at $168.93 (−4.5% on May 18):** Marvell shares pulled back 4.5% to $168.93 from the ATH of $182 reached on May 14 (Alphabet co-design news). GF Value model flags 63.9% overvaluation vs. intrinsic value ~$103. Source: GuruFocus, 2026-05-18. *Assessment: Pullback from ATH on no new negative news suggests the $182 move was partly spec-driven by the Alphabet leak. The forward revenue trajectory ($11.12B FY2027 estimate, $15.35B FY2028 estimate) is what matters — execution at May 27 earnings is the key test.*

**Q1 FY2027 earnings — May 27 (8 days out):** Marvell reports Q1 FY2027 on May 27, 2026. Analysts expect FY2027 guidance raised alongside strong AI custom silicon commentary. The primary watch items: AI/data center revenue split, Google TPU/MPU design win confirmation, and any capacity allocation visibility for custom ASIC production at TSMC. Source: FX Leaders / CoinCentral, 2026-05-14.

---

### 2026-05-20

**Analyst price target surge — B. Riley $205, Melius $220, RBC $200:** Multiple major sell-side upgrades today ahead of May 27 earnings:
- B. Riley raised PT to $205 from $156, citing faster-than-expected AI spending acceleration and rising hyperscaler capex through 2026–2028
- Melius Research raised PT to $220 from $140 — the highest published street target on MRVL
- RBC Capital raised PT to $200, highlighting sustained optical momentum and NVIDIA's investment in Marvell's optical connectivity business
Source: StocksToTrade / TheStreet, 2026-05-19–20. *Note: Combined with BofA's prior raise to $200, three of the four top-tier banks now have $200+ targets. The consensus has moved ~60–70% above current trading levels in a short period — a sign that the AI ASIC revenue ramp is being priced more aggressively into forward models. Execution at May 27 earnings is critical to sustain this.*

**Stock up 7.01% today — continuing rally:** MRVL shares climbed 7.01% today, adding to gains from the Alphabet co-design news and the broader AI capex confirmation. Stock has gained 135%+ since March 5. Source: StocksToTrade, 2026-05-20. *Valuation note: At $180+ and P/E above 50, MRVL is priced for strong FY2027 and FY2028 execution — the May 27 earnings call needs to confirm the Google co-design timeline and hyperscaler ASIC volumes.*

**Earnings May 27 — 7 days out:** Watch items: (1) AI/Data Center revenue as % of total — expect >70%; (2) Google inference TPU and MPU co-design program confirmation and volume guidance; (3) FY2027 ($11.12B est.) and FY2028 ($15.35B est.) revenue guide; (4) Optical interconnect revenue trajectory following Polariton acquisition. Source: FX Leaders / TheStreet, 2026-05.

### 2026-05-21

**Pre-earnings positioning — MRVL pre-market above $185, 6 days to May 27:** Marvell shares closed May 20 at $176.27 (+4.35%) and pushed above $185 in pre-market trading ahead of the May 27 Q1 FY2027 earnings report. Options markets price a ~13% move on earnings day (Bloomberg data). Consensus: 22 Buys / 4 Holds — Strong Buy. Source: Investing.com / FX Leaders / TipRanks, 2026-05-20–21.

**Q1 FY2027 earnings expectations (May 27):** Wall Street consensus for Q1 FY2027:
- Revenue: $2.40B (+27% YoY)
- EPS: $0.79 (+27.4% YoY)
Marvell is expected to raise FY2027 full-year guidance above $11.12B and FY2028 above $15.35B estimates. The most watched items: (1) confirmation of Google inference TPU + MPU co-design program and volume timeline; (2) Data Center % of total revenue; (3) optical connectivity revenue trajectory post-Polariton acquisition. Source: Investing.com / TipRanks, 2026-05-20–21.

**NVDA Q1 results — positive read-through for MRVL:** NVIDIA's $81.6B Q1 and $91B Q2 guidance confirms the AI ASIC/custom silicon wave is not decelerating. Hyperscaler CapEx at $725B+ underpins the demand for the custom co-design work Marvell delivers. NVDA's strategic $2B investment in Marvell (captured March 2026) is additional confirmation of the custom silicon and optical interconnect thesis. Source: See [[NVDA]] 2026-05-21 entry.

---

### 2026-05-23

**Stifel raises PT from $140 to $210 — expects "beat-and-raise" on May 27:** Stifel maintained Buy and raised its price target 50% to $210, arguing Marvell will exceed the $2.40B Q1 consensus and guide higher. Key drivers: (1) 1.6T optical deployments accelerating — interconnect revenue now expected to grow **50% YoY in FY2027**, up sharply from Stifel's prior 30% estimate; (2) AWS Trainium 3 (Scorpio X) confirmed in active production ramp; (3) XPU-Attach momentum broadening beyond Amazon to additional hyperscaler programs. Source: Investing.com / Seeking Alpha, 2026-05-22. *Thesis bearing: Confirms — the optical interconnect revision from 30% to 50% YoY and Trainium 3 production confirmation are the first hard third-party data points validating the FY2027 revenue ramp story ahead of May 27 earnings.*

**MRVL hits new ATH ~$192 — up 3% on May 22 analyst wave:** Following the Stifel $210 and Citi $215 upgrades, MRVL closed at approximately $192 — a new all-time high. Stock has rallied ~179% from the March 5 low. Trades at >50× GAAP earnings ahead of binary May 27 event. Source: ForeignPolicyJournal / Investing.com, 2026-05-22. *Thesis bearing: Neutral — ATH ahead of earnings increases downside risk on a miss; execution must match the elevated consensus.*

**Pre-earnings analyst scorecard — all confirmed Buy targets above $195:** Melius $220, Citi $215, Stifel $210, B. Riley $205, BofA $200, Oppenheimer $200, RBC $200, Wells Fargo $195. No Buy-rated analyst below $193. Average street target ~$205+. Source: Various, 2026-05-19–22. *Thesis bearing: Confirms — if earnings confirm the ramp, this repricing significantly narrows the gap between consensus view and our DCF IV of $119.91 from Session 3; a post-earnings DCF re-run is warranted.*

**Taiwan Strait: 26 PLA aircraft near Strait, Liaoning carrier in West Pacific (indirect risk via TSMC dependency):** PLA Liaoning carrier group deployed to West Pacific for live-fire drills; 26 PLA military aircraft detected near Taiwan Strait in a 24-hour period. Trump suggested Taiwan arms sales could be used as a "negotiating chip." No supply chain disruption — elevated but within recent norms (below April's 169/month average). Source: AEI, 2026-05-22. *Thesis bearing: Neutral — MRVL's exposure is indirect (TSMC manufactures its ASICs); elevated geopolitical activity, but no imminent supply risk. Monitor alongside TSM.*

---

### 2026-05-22

**Analyst target escalation — Citi $215 (from $118), Oppenheimer $200 (from $170), Wells Fargo $195 (from $135):** Three additional major sell-side upgrades, all anchored on NVDA's $81.6B Q1 FY2027 blowout and AWS Trainium custom silicon momentum. Citi's raise from $118 to $215 is the single largest revision — nearly doubling their target — citing Amazon's Trainium deployment and broadening custom silicon tailwinds. Oppenheimer (Outperform) and Wells Fargo (Overweight) also raised, bringing confirmed institutional targets above $200 to: Melius $220, Citi $215, B. Riley $205, BofA $200, Oppenheimer $200, RBC $200. Source: GuruFocus / 247 Wall St. / Investing.com, 2026-05-20–22. *Thesis bearing: Confirms — the sell-side consensus has repriced MRVL's revenue trajectory following NVDA's demand-signal earnings; $200+ targets imply the custom silicon ramp is being underwritten by multiple independent research shops.*

**FY2026 full-year results confirmed (year ended Jan 31, 2026):** Revenue $8.195B (+42% YoY, record). GAAP operating income: -$720.3M (distorted by acquired intangibles amortization ~$639M and large SBC). Non-GAAP operating margin: 35%. GAAP net income: $2.67B (aided by tax benefit). Cash: $2.64B. Total debt: $4.47B. Shares: 874M. Source: Marvell investor relations / SEC 8-K March 5, 2026. *Thesis bearing: Confirms — record revenue validates the hyperscaler custom silicon ramp; the GAAP/non-GAAP gap is explained by non-cash accounting charges from prior acquisitions, not operating weakness.*

**Pre-earnings positioning — 5 days to May 27 Q1 FY2027 report:** MRVL trading ~$178, with pre-market sessions pushing above $185 ahead of the earnings report. Options markets price ~13% move on earnings day. Wall Street consensus for Q1 FY2027: revenue $2.40B (+27% YoY), EPS $0.79. Full-year FY2027 consensus: $11.12B revenue. Key watch items: (1) AI/Data Center revenue as % of total (expect >70%); (2) Google inference TPU + MPU program timeline and volume; (3) FY2027 and FY2028 guidance raise; (4) optical interconnect contribution post-Polariton. Source: Investing.com / FX Leaders, 2026-05-22. *Thesis bearing: Neutral — pre-earnings positioning is consensus-driven; actual confirmation on May 27 is the signal that matters.*

---

### 2026-05-24

**Pre-earnings final read — MRVL closes at ATH $196.33, 3 trading days to May 27:** MRVL closed at $196.33 on Friday May 22, a new all-time high close (+2.96% on the day), extending the pre-earnings rally to ~183% from the March 5 low. All 8 major analyst targets stand at $195–$220. Options continue pricing a ~13% move on earnings day. Pre-earnings consensus: Q1 FY2027 revenue $2.40B / EPS $0.79–$0.80; FY2027 full-year consensus $11.12B (expected to be raised). Custom ASIC business confirmed scaling from zero to $1.5B in FY2026; management has guided >20% YoY growth in FY2027 and at least doubling in FY2028. Source: Investing.com / MarketBeat / ad-hoc-news.de, 2026-05-22. *Thesis bearing: Neutral — stock at ATH heading into binary event; execution must match elevated consensus. DCF re-run queued for post-May 27 data.*

**Samsung deal reached May 20 — 18-day strike averted, HBM4 production uninterrupted (indirect MRVL context):** Samsung Electronics and its union reached a tentative wage agreement on May 20, 2026, one day before the planned 18-day work stoppage (May 21–June 7) that threatened ~$43B in AI memory production. Terms: 10.5% of profits distributed as employee stock + 1.5% cash, 10-year structure. Ratification vote runs through May 26. HBM4 production at Samsung's Pyeongtaek and Hwaseong fabs continues at normal run rates. Source: Tom's Hardware / abhs.in, 2026-05-20. *Thesis bearing: Neutral for MRVL — Samsung does not supply Marvell-designed ASICs; the impact is indirect (AI buildout supply chain intact). For MU's thesis: removes near-term supply disruption premium; structural HBM sold-out thesis via LTAs is unchanged.*

**Celestial AI acquisition ($3.25B, completed Feb 2, 2026) — retroactive capture, major entity gap:** Marvell completed the acquisition of Celestial AI on February 2, 2026 for $3.25 billion (~$1B cash + ~27M MRVL shares). Celestial AI's core product is Photonic Fabric™ — an optical scale-up interconnect technology delivering >2× power efficiency vs. copper, significantly longer reach, and higher bandwidth for large-scale AI deployments. This acquisition predated and is larger than the Polariton Technologies acquisition (April 2026, plasmonics-based). Combined, Marvell now holds three distinct photonic IP layers: (1) legacy SerDes + coherent optical DSP, (2) Celestial AI Photonic Fabric™ for high-bandwidth scale-up, (3) Polariton plasmonics for ultra-dense short-reach co-packaged optics. No other fabless semiconductor company owns this full optical connectivity stack at this scale. Source: Marvell Newsroom / Seeking Alpha / investor.marvell.com, 2026-02-02. *Thesis bearing: Strongly Confirms — at $3.25B, Celestial AI is Marvell's largest optical acquisition and converts Marvell's connectivity portfolio from "good SerDes IP" into a multi-technology photonic platform. The optical moat is deeper and broader than the entity captured; the Polariton + Celestial combination positions Marvell for the co-packaged optics transition (3.2T+ links) and the scale-out connectivity layer simultaneously.*

**Wolfe Research $210 PT; analyst consensus reaches 32 Buys:** Wolfe Research set a $210 price target on MRVL ahead of May 27 earnings. Combined with the previously captured targets (Melius $220, Citi $215, Stifel $210, B. Riley $205, BofA $200, Oppenheimer $200, RBC $200, Wells Fargo $195), the total analyst consensus stands at 32 Buy/Strong Buy ratings — 47% Strong Buy, 34% Buy, 19% Hold, 0% Sell. This is the broadest unanimous bullish consensus the entity has tracked. Source: QuiverQuant / MSN, 2026-05-23. *Thesis bearing: Confirms — the continued expansion of sell-side coverage at $200+ targets reinforces that the custom ASIC + optical thesis has been adopted across independent research shops, not just early-mover firms.*

**Microsoft Maia AI chip confirmed as Marvell co-design — Azure AI and OpenAI inference target:** Multiple sources confirm Marvell supplies silicon IP and back-end design services for Microsoft's Maia AI accelerators, which target Azure AI inference and OpenAI workloads. Combined with Google TPU/MPU, Amazon Trainium/Inferentia, and reported Meta MTIA involvement, Marvell has active or confirmed co-design relationships with three of the four major hyperscalers (Google, Amazon, Microsoft). CEO Matt Murphy's most recent public comments: "Bookings are accelerating at a record pace" heading into FY2027. Note: Microsoft Maia is reportedly the largest single ASIC program in Marvell's data center revenue at this stage (sources indicate Amazon Trainium or Microsoft Maia is the primary contributor — not yet broken out in IR). Source: HeyGoTrade / Tech-Insider, 2026-05. *Thesis bearing: Confirms — a three-hyperscaler confirmed design win base (Google, Amazon, Microsoft) fundamentally reduces single-customer concentration risk and confirms Marvell as a platform, not a one-bet custom silicon shop.*

---

---

### 2026-05-25

**Final pre-earnings positioning — "Switzerland of interconnect" framing + 50+ design win count confirmed:** Ahead of May 27 Q1 FY2027 earnings, analysts are framing Marvell as the "Switzerland of interconnect" — a stack-neutral platform that benefits regardless of which GPU architecture wins. Third-party research counts 50+ active custom AI processor design wins across hyperscalers and AI-native companies. This framing materially reduces the single-customer concentration risk that has been the primary bear thesis; the entity already captures confirmed co-designs at Google (TPU/MPU), Amazon (Trainium/Inferentia), and Microsoft (Maia). Source: GuruFocus / FX Leaders, 2026-05-22–25. *Thesis bearing: Confirms — 50+ design wins and multi-architecture neutrality convert the concentration risk narrative from a structural concern to a transitional one; if May 27 confirms ongoing hyperscaler pipeline depth, the "Switzerland of interconnect" label will stick.*

**Final watch list for May 27 earnings call (post-close):** (1) Q1 FY2027 revenue vs. $2.40B consensus — Stifel expects a beat; (2) FY2027 full-year guide vs. $11.12B consensus — must raise to sustain ATH; (3) AI/Data Center revenue as % of total — expect >70%; (4) Google TPU/MPU co-design volume timeline and any capacity allocation visibility for TSMC production; (5) Optical interconnect revenue trajectory: Celestial AI Photonic Fabric + Polariton plasmonics first combined-product revenue commentary; (6) Management commentary on design win pipeline breadth (any fourth hyperscaler, i.e., Meta MTIA confirmation). Options pricing ~13% move. DCF re-run queued for session 19 post-earnings. Source: Investing.com / Stifel / Seeking Alpha, 2026-05-22–25. *Thesis bearing: Neutral — this is the event; no additional thesis data until the call closes.*

---

### 2026-05-26

**Amazon $225B Trainium commitment backlog — first quantified forward revenue anchor for MRVL custom ASIC:** Wells Fargo (May 20, 2026) reported that Amazon exited Q1 calendar 2026 with $225 billion in committed Trainium deployments — the first large, specific backlog figure attached to Amazon's AI infrastructure program. Marvell supplies the silicon IP and co-designs the Trainium/Inferentia custom ASICs under multi-year contracts. Wells Fargo forecasts Trainium-related revenue for Marvell at ~$6B in each of 2027 and 2028, with potential to double if per-unit pricing moves higher. The $225B figure also implies gigawatt-scale AI cluster deployments through 2029 — sustained demand for MRVL's optical interconnect and custom XPU products alongside the compute silicon. Source: Wells Fargo analyst note / 247 Wall St. / Investing.com, 2026-05-20. *Thesis bearing: Confirms — this is the first concrete backlog figure quantifying the scale of Amazon's Trainium commitment; $6B in annual MRVL revenue from a single hyperscaler partner alone would justify a substantial re-rating if confirmed on May 27 earnings call.*

**Pre-earnings hold — entity current through May 25; earnings tonight (May 27 post-close):** No new material pre-earnings developments on May 26. MRVL closed at ATH $196.33 on May 22; first trading day May 26 (Memorial Day ended). Consensus Q1 FY2027: $2.40B revenue / $0.80 EPS; options pricing ~13% move. Event queue item held for post-earnings processing — DCF re-run and story_narrative revision queued for next session. Source: MarketBeat / consensus tracking, 2026-05-26. *Thesis bearing: Neutral — earnings event is the signal; no pre-close data to move the thesis.*

---

### 2026-05-27

**XConn Technologies acquisition ($540M, completed Feb 10, 2026) — retroactive capture of major entity gap:** Marvell completed the acquisition of XConn Technologies on February 10, 2026 for approximately $540M (~60% cash, ~40% stock ≈ 2.5M MRVL shares). XConn is a PCIe and CXL switch silicon provider: PCIe 5 + CXL 2.0 switches are in production today; PCIe 6 + CXL 3.1 switches are sampling. The acquisition expands Marvell's switching portfolio and advances its UALink scale-up switching roadmap for multi-rack AI systems. Revenue expected to begin in H2 FY2027, ramping to ~$100M in FY2028. XConn accretive to non-GAAP EPS at that revenue level. Source: Data Center Dynamics / Marvell Newsroom / Wilson Sonsini, 2026-02-10. *Thesis bearing: Confirms — this is the source of the "Marvell 260-lane PCIe 6.0 switch" captured in Session 25 as competing with Astera Labs Scorpio X. XConn completes Marvell's connectivity stack (SerDes → Optical DSP → Photonic Fabric → PCIe/CXL switches), meaning MRVL is now competing across the entire data center connectivity layer — not just ASIC co-design. This materially raises the competitive threat to ALAB.*

**Q1 FY2027 earnings reported post-close May 27 — results surging 13–15% after hours per TIKR/Stocktwits:** Marvell reported Q1 FY2027 results at approximately 1:45 PM PT today. Per TIKR ("Marvell Technology Nasdaq MRVL Stock Surges 15% As AI Demand Drives Quarterly Beat") and Stocktwits ("MRVL Shares Surge 13% On Solid Q1 Guidance, Bolstered By AI Data Center Growth"), the stock surged 13–15% after hours — consistent with a meaningful beat-and-raise. Actual revenue, EPS, and Q2 FY2027 guidance numbers are not yet indexed; specific data to be captured in Session 28. Q1 FY2027 guidance heading in: $2.40B ±5% revenue / $0.79 ±$0.05 non-GAAP EPS. Conference call replay available June 2, 2026 (passcode 13760544). Source: TIKR / Stocktwits / BusinessWire, 2026-05-27. *Thesis bearing: Confirms — a 13–15% after-hours surge on what was expected to be a clean quarter validates the hyperscaler custom ASIC ramp is tracking or beating the FY2027 guidance trajectory. Session 28 must capture specific numbers (Q1 actual vs. $2.40B guide, Q2 guide, data center segment %, FY2027 full-year raise if any).*

**NVIDIA Vera Rubin uses TSMC CoWoS-L + 8-layer HBM4 for first time — TSMC packaging bottleneck now the AI supply chain constraint, not silicon:** Jensen Huang (arrived Taipei May 23) is meeting TSMC Chairman C.C. Wei to secure CoWoS production commitments for Vera Rubin. The constraint is packaging, not silicon — TSMC is scaling CoWoS from ~35,000 WPM (late 2024) to 120,000–140,000 WPM by end 2026 (nearly 4×). TSMC has committed $56B capex toward this expansion. NVIDIA has pre-committed >50% of TSMC's CoWoS capacity through 2027. The Vera Rubin NVL72 includes 36 Vera CPUs + 72 Rubin GPUs on TSMC N3P, CoWoS-L, with 8-layer HBM4 — the first GPU platform to use HBM4. Jensen called it "the largest product launch probably in the history of Taiwan." Source: TechTimes / NVIDIA Blog / FinancialContent, 2026-05-24. *Thesis bearing: Confirms — Marvell's custom ASICs are all manufactured at TSMC using the same CoWoS capacity; the capacity expansion that enables Vera Rubin also unlocks the next generation of custom ASIC designs (Google inference TPU, Trainium successor). TSMC CoWoS bottleneck remains through 2026, confirming the manufacturing choke point thesis across both NVDA and custom silicon programs.*

**Northland downgrades ALAB to Market Perform (no PT) on 2027 hyperscaler spending risk — indirect MRVL read-through:** Northland Capital Markets downgraded Astera Labs from Outperform to Market Perform on May 26, citing: (1) P/E 204 (stretched valuation); (2) hyperscalers could become cash-constrained by CY2027, with datacenter spending potentially declining; and (3) XConn (now Marvell) PCIe 6 switches sampling creates direct competition. ALAB fell ~3.8% on May 27 morning. MRVL's XConn acquisition positions it to capture PCIe/CXL connectivity revenue ALAB currently holds. Source: Northland Capital / Investing.com / Daily Political, 2026-05-26. *Thesis bearing: Neutral — the hyperscaler cash constraint risk for 2027 applies equally to MRVL (custom ASIC revenues follow CapEx). The competitive displacement story is a medium-term (FY2028) event, not near-term.*

---

### 2026-05-27 (Session 28 — Q1 FY2027 Actuals)

**Q1 FY2027 results confirmed: Revenue $2.418B (+28% YoY), non-GAAP EPS $0.80 — beat-and-raise.** Actual numbers now indexed from SEC 8-K filed May 27, 2026. Revenue beat the $2.40B guidance midpoint by $18M and the +27% YoY consensus. Non-GAAP EPS of $0.80 beat the $0.79 estimate. This is a new quarterly revenue record. Source: Marvell Technology 8-K / SEC EDGAR, 2026-05-27. *Thesis bearing: Confirms — first hard earnings confirmation of the FY2027 revenue ramp; management delivered on Q1 within range and is now guiding Q2 and full year materially higher.*

**Q2 FY2027 guidance: $2.7B midpoint (+35% YoY).** The $2.7B Q2 midpoint (±5%) implies $150M above Q1's $2.418B — sequential acceleration consistent with data center segment ramping through the year. +35% YoY growth in Q2 accelerates from Q1's +28%, driven by continued hyperscaler ASIC ramp and expanding optical connectivity shipments. Source: Marvell investor call / 8-K, 2026-05-27. *Thesis bearing: Confirms — sequential acceleration in Q2 guidance is strong signal that the custom ASIC production ramp (Trainium, Google TPU, XPU programs) is expanding, not plateauing.*

**FY2027 guidance raised to ~$11B; FY2028 first-time management guidance: ~$15B (+40% YoY).** Management raised FY2027 revenue outlook to "approach ~$11B" (>30% YoY from $8.195B FY2026), up from the prior ~$10B implied guidance. This means management crossed the $11B threshold that was previously only an analyst consensus estimate. FY2028 guidance of ~$15B is the first formal management long-range guidance — +36% from $11B FY2027. Q4 FY2027 exit rate guided >$3B (quarterly). Data center segment: >$6B in FY2026 (+46% YoY), expected +40% FY2027, +50% FY2028. Custom ASIC: $1.5B FY2026 (doubled YoY), >20% FY2027, at least doubling FY2028 (>$3B). Source: Marvell earnings call / TIKR analyst summary, 2026-05-27. *Thesis bearing: Strongly Confirms — this is the most important single data point in the MRVL entity. First-time management FY2028 guidance of $15B puts a number on what was previously analyst conjecture. Custom ASIC revenue doubling again in FY2028 (to >$3B) confirms the Google+Amazon+Microsoft programs are tracking to volume. The 10-year DCF CAGR assumption of 25% is now supported by management's own 2-year roadmap showing 34-36% YoY growth.*

**Stock price context: AH ~$214.59 (down from AH high ~$220, regular session close ~$208).** Stock traded up ahead of earnings (closed regular session ~$208 after a 10% pre-earnings run) and initially surged to ~$220–222 AH on the beat. Has since settled to $214.59 AH (-3% from AH peak) as the market digested that FY2027 guidance of ~$11B, while raised from mgmt's implicit ~$10B, was broadly in line with analyst consensus ($11.12B). The beat was clean but not dramatically above the elevated buy-side bar. Source: CNBC / Investing.com, 2026-05-27. *Thesis bearing: Neutral — the AH retreat from $220 to $214 suggests the guidance didn't provide a new upside surprise versus what the most optimistic analysts had already modeled. This is consistent with the stock having run 183% since March 5 — much of the good news was pre-discounted.*

---

### 2026-05-28

**Jensen Huang confirmed as special guest at Computex June 2 keynote — "The Future of AI Depends on Connectivity":** NVIDIA CEO Jensen Huang will appear alongside Marvell CEO Matt Murphy at the June 2 Computex keynote (10:30am, Taipei Nangang Exhibition Center Hall 2). The joint presentation will showcase the NVIDIA-Marvell NVLink Fusion partnership — announced March 2026 and backed by a $2B NVIDIA investment — which integrates Marvell's custom XPUs and scale-up networking into NVIDIA's AI factory and AI-RAN ecosystem. The keynote will cover: (1) NVLink Fusion technical integration, enabling Marvell-designed chips to connect natively into NVIDIA infrastructure; (2) joint AI data center interconnect blueprint for hyperscaler deployments; (3) NVIDIA Aerial AI-RAN (5G/6G telecom-to-AI infrastructure transformation). This is the first time NVIDIA's CEO has appeared as a dedicated joint-keynote guest for a fabless competitor/partner — an extraordinary signal of partnership depth. Source: PR Newswire / Marvell.com / BigGo Finance, 2026-05-27–28. *Thesis bearing: Strongly Confirms — Jensen Huang sharing a stage with Matt Murphy positions Marvell as the primary non-NVIDIA silicon architecture inside NVIDIA's ecosystem. NVLink Fusion is a strategic bet that custom ASICs (Google TPU, Amazon Trainium, Microsoft Maia) should connect to NVIDIA infrastructure rather than replace it — and Marvell is the connectivity backbone that makes that happen. This is the clearest validation yet that Marvell is not an NVIDIA competitor but an NVIDIA ecosystem partner.*

### 2026-05-29

**Marvell acquires Polariton Technologies + Alphabet partnership talks — optical AI connectivity thesis advances:** Two material developments emerged alongside the Q1 FY2027 earnings beat. (1) Marvell has acquired Polariton Technologies, a photonics startup focused on optical technology for AI infrastructure data movement — a direct complement to the Inphi optical DSP business Marvell acquired in 2021. The Polariton acquisition adds chip-embedded optical I/O technology that aligns with NVIDIA's $6.5B photonics investment thesis (NVIDIA separately committed $2B to Marvell, partly to accelerate exactly this optical integration inside the NVLink Fusion ecosystem). (2) Marvell is reported to be in active talks with Alphabet for a new custom AI chip program — separate from (but potentially adjacent to) the existing Google TPU supply relationship. If confirmed, an Alphabet custom silicon engagement would add a third major hyperscaler ASIC program alongside Google TPU v6 co-design and Amazon Trainium. Source: SimplyWallSt / company filings, 2026-05-27–30. *Thesis bearing: Confirms — the Polariton acquisition closes the "optical I/O gap" in Marvell's custom silicon stack; combined with NVIDIA's $2B investment specifically validating Marvell's optical connectivity for NVLink Fusion, Marvell is becoming the optical backbone of the AI factory. The Alphabet talks, if confirmed, would make Marvell the only fabless semiconductor company designing custom silicon for three of the four largest hyperscalers — a durable competitive position.*

**Post-earnings analyst upgrades — consensus rapidly re-rating MRVL post-FY2028 $15B guide:** Following the Q1 FY2027 beat and first-ever FY2028 $15B management guidance, analysts raised targets materially: Benchmark initiated Buy with $275 PT (from no prior rating); JPMorgan raised PT to $240 from $135; Oppenheimer raised PT to $250 from $200 (already captured: HSBC initiated Buy $300, Melius $220). The breadth of upgrades confirms NVIDIA's $2B investment + Jensen Huang's June 2 Computex appearance has permanently repositioned Marvell in institutional coverage — from "cyclical custom silicon" to "AI infrastructure partner." Note: Goldman Sachs remains outlier at Neutral/$125 — the only major house below Saturn's own DCF IV of $126.75. Source: Yahoo Finance / Benzinga, 2026-05-27–28. *Thesis bearing: Confirms (institutional view) — rapidly rising consensus PTs reduce the probability of sharp multiple compression; however Saturn IV remains $126.75, and the spread between institutional targets ($240–$300) and IV is the widest of any portfolio position.*

**Post-earnings "sell the news" — stock falls ~9% to ~$201 on May 28 (from ~$221 May 27 close):** Despite the Q1 FY2027 beat ($2.418B revenue, $0.80 EPS) and Q2 FY2027 guidance of $2.7B (+35% YoY, beating the $2.6B consensus), MRVL fell approximately 9% on May 28 to around $201 (intraday range: $191.84–$202.30). The decline reflects profit-taking after the stock had rallied 183% from the March 5 low and ~6% on the earnings day itself. The same "sell the news" pattern was seen post-NVDA's $91B guide and post-MU's UBS upgrade. The FY2028 $15B management guidance and Q2 $2.7B guide remain intact; the sell-off is valuation-driven, not thesis-driven. Source: Stocktwits / GuruFocus / Investing.com, 2026-05-28. *Thesis bearing: Neutral — price action reflects elevated positioning unwinding, not a fundamental deterioration. DCF IV $126.75 at the $201 price implies MoS -37.2% — improved from -42.7% at $221, but still firmly SELL/AVOID. The June 2 Computex keynote with Jensen Huang is the next material event.*

**HSBC upgraded MRVL to Buy with $300 price target (new Buy initiation from prior Hold, May 27–28):** HSBC set a $300 price target on MRVL, citing the NVLink Fusion partnership depth and first-time FY2028 $15B management guidance as the key valuation re-rating triggers. This is the highest new-initiating analyst PT in the table (above Melius $220), and reflects expanding institutional consensus that Marvell's custom silicon + connectivity franchise justifies a 20–25× FY2028 revenue multiple. Source: HSBC research note, 2026-05-27–28. *Thesis bearing: Confirms (institutional view) — however, even HSBC's $300 PT is 136% above Saturn's DCF IV of $126.75, reflecting the market's willingness to pay for growth optionality that the model doesn't credit. The gap between $300 institutional target and $126.75 Saturn IV is the single largest spread across all 7 tickers.*

---

## Cross-links

- [[TSM]] — TSMC manufactures Marvell-designed custom ASICs; custom silicon trend = TSMC volume
- [[NVDA]] — Marvell custom silicon partially substitutes for inference GPU workloads; competitive and complementary
- [[ANET]] — data center networking; Marvell and Arista serve overlapping infrastructure layer
- [[ALAB]] — XConn acquisition makes Marvell a direct PCIe/CXL switch competitor to Astera Labs
- [[custom-silicon]] — the thesis concept; hyperscaler ASIC trend is Marvell's primary growth driver
- [[cowos]] — TSMC CoWoS is the packaging layer for all Marvell-designed custom ASICs
