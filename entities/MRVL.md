# Marvell Technology, Inc. (MRVL)

> The primary co-designer of custom AI ASICs for hyperscalers —
> the company that enables Google, Amazon, Microsoft, and Meta to reduce their NVIDIA dependency.

*Last updated: 2026-05-17 | Wisesheets data as of: not yet pulled*

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

*(Pull from Wisesheets — note pull date when populating)*

**Segment note:** Marvell reports Data Center, Carrier Infrastructure, Enterprise Networking, Consumer, Automotive/Industrial. Data Center is the primary segment — custom AI ASICs are here and growing rapidly.

---

## Revenue Segments

*(Update quarterly — Data Center % of revenue is the primary metric; extract AI ASIC revenue commentary separately from general data center)*

---

## Growth Drivers

*(Populate: Hyperscaler custom ASIC ramp (Google, Amazon confirmed; others rumored); Inference silicon growth as AI moves from training to deployment; Co-packaged optics opportunity; 5G carrier infrastructure recovery)*

---

## Risks

*(Populate: Customer concentration (hyperscaler co-design revenue is lumpy — one customer delay = quarterly miss); NVIDIA maintaining inference dominance longer than expected, reducing hyperscaler custom silicon urgency; Broadcom as competitor in custom ASIC co-design; Design cycle timing risk — 18-24 month lag between win and revenue)*

---

## Catalysts

### Active Catalysts
*(Populate: Google TPU ramp at TSMC (Marvell co-designed); Amazon Trainium volume; Microsoft Maia revenue contribution; New hyperscaler co-design win announcement)*

### Archived Catalysts
*(Move here once played out)*

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

## Cross-links

- [[TSM]] — TSMC manufactures Marvell-designed custom ASICs; custom silicon trend = TSMC volume
- [[NVDA]] — Marvell custom silicon partially substitutes for inference GPU workloads; competitive and complementary
- [[ANET]] — data center networking; Marvell and Arista serve overlapping infrastructure layer
- [[custom-silicon]] — the thesis concept; hyperscaler ASIC trend is Marvell's primary growth driver
