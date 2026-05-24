# Marvell Technology, Inc. (MRVL)

> The primary co-designer of custom AI ASICs for hyperscalers —
> the company that enables Google, Amazon, Microsoft, and Meta to reduce their NVIDIA dependency.

*Last updated: 2026-05-20 | Wisesheets data as of: not yet pulled*

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
| Q1 FY2027 Earnings (May 27) | 2026-05-27 | 5 days out; consensus $2.40B revenue; options price ~13% move |
| Google inference TPU + MPU program confirmation | May 27 earnings call | Watch for volume timeline and production schedule |
| FY2027 guidance raise | May 27 earnings call | Consensus $11.12B; management expected to raise above this |
| Trainium volume ramp visibility | H2 2026 | AWS deployment scale-out; cited by Wells Fargo as key driver |
| Co-packaged optics revenue (post-Polariton) | 2026-2027 | Integration timeline unclear; watch R&D commentary |

### Archived Catalysts

| Catalyst | Date | Outcome |
|---|---|---|
| NVIDIA $2B strategic investment in MRVL | March 2026 | Confirmed; validates optical + custom silicon thesis |
| AMD 13F stake disclosure | 2026-05-13 | MRVL +10% on day; both NVDA and AMD invested = ecosystem validation |
| NVDA Q1 FY2027 earnings read-through | 2026-05-20 | NVDA +85% YoY revenue confirms AI buildout acceleration; MRVL continued rally |

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

---

## Cross-links

- [[TSM]] — TSMC manufactures Marvell-designed custom ASICs; custom silicon trend = TSMC volume
- [[NVDA]] — Marvell custom silicon partially substitutes for inference GPU workloads; competitive and complementary
- [[ANET]] — data center networking; Marvell and Arista serve overlapping infrastructure layer
- [[custom-silicon]] — the thesis concept; hyperscaler ASIC trend is Marvell's primary growth driver
