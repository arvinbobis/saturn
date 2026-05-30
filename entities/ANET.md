# Arista Networks, Inc. (ANET)

> The dominant vendor for AI data center networking infrastructure —
> every scale-out GPU cluster needs high-speed, low-latency ethernet switching, and Arista builds it.

*Last updated: 2026-05-22 | Wisesheets data as of: not yet pulled; TTM financials from SEC filings*

---

## Overview

- **Business model:** Sells cloud networking hardware (ethernet switches, routers) and EOS software (Arista's cloud-grade OS). Revenue mix: ~75% products (hardware), ~25% services (support contracts, software subscriptions — high margin, recurring).
- **Value chain position:** Sits between chip suppliers (Broadcom StrataXGS, Marvell silicon) and hyperscaler/enterprise data center operators. Arista is the network fabric that connects thousands of NVIDIA GPUs in a training cluster.
- **Founded:** 2004, Santa Clara, California. HQ in Santa Clara.
- **Listed:** NYSE: ANET
- **Scale:** ~4,300+ employees.
- **Market cap:** *(update)*

### Why ANET Is in This Portfolio
AI GPU clusters require massive east-west bandwidth between GPUs during training. A 10,000-GPU Blackwell cluster needs a non-blocking, low-latency network fabric — Arista's spine-leaf architecture with 400G/800G ethernet is the standard answer. As GPU cluster size grows (100K+ GPU clusters are being announced), network spend scales roughly proportionally. Arista participates in AI infrastructure spend without taking GPU design or manufacturing risk.

### The AI Networking Tailwind
Training a large model on a GPU cluster requires near-constant all-to-all communication — gradient synchronization, parameter server traffic, checkpoint writing. Network latency and bandwidth directly impact GPU utilization. As cluster sizes grow and models get larger, network infrastructure spend grows with it. Arista's 800G ethernet switches and its Ultra Ethernet Consortium (UEC) membership position it for the next generation of AI networking.

---

## Moat

### EOS Software — Cloud-Grade Network OS
Arista's EOS (Extensible Operating System) is a single-image, modular network OS that runs identically across the entire product line. It enables programmability, automation, and rapid bug fixes without system downtime. Enterprise and hyperscaler customers build their automation tooling on EOS — switching vendors means rebuilding that tooling. Cisco's IOS/NX-OS is the primary alternative; EOS is meaningfully better for cloud-scale operations.

### Hyperscaler Relationships
Arista's largest customers are Microsoft, Meta, and a handful of other hyperscalers. These are multi-year, multi-billion-dollar relationships. Microsoft alone represented ~30% of revenue at peak. Hyperscalers co-develop features with Arista, creating co-invested relationships that are durable.

### 400G/800G Leadership
Arista has been early to each ethernet speed generation. 400G is now mainstream in AI clusters; 800G is ramping. Arista's portfolio is ahead of Cisco at each transition. First-mover adoption at hyperscalers creates the installed base and management familiarity that compounds into future orders.

---

## Financials

*(Pull from Wisesheets — note pull date when populating)*

**Note:** Arista is unusually profitable for a hardware company — operating margins ~35–40%. This reflects software content in revenue and lean operations.

---

## Revenue Segments

*(Update quarterly — By customer type: Cloud Titans (hyperscalers), Enterprise, Service Provider; By product: switching hardware, EOS software, support services)*

**Customer concentration note:** Microsoft and Meta together can be >50% of revenue. Track any customer concentration changes quarterly — a hyperscaler pause in networking CapEx hits Arista immediately.

---

## Growth Drivers

*(Populate: GPU cluster scale-out driving 800G ethernet demand; Campus/enterprise AI networking upgrade cycle; Ultra Ethernet Consortium (UEC) adoption; International hyperscaler expansion; Software/subscription revenue mix growing)*

---

## Risks

*(Populate: Customer concentration (Microsoft, Meta together >50%); Cisco competitive pressure; InfiniBand vs. Ethernet competition for GPU clusters (NVIDIA prefers InfiniBand — Arista is an Ethernet play); Lumpy hyperscaler CapEx cycles — Arista networking orders follow GPU orders with ~1 quarter lag; Valuation is premium)*

---

## Catalysts

### Active Catalysts
*(Populate: 800G ramp; Ultra Ethernet Consortium standard finalization; Enterprise AI networking upgrade cycle; Any new hyperscaler customer announcement)*

### Archived Catalysts
*(Move here once played out)*

---

## Monitoring Checklist

*(Quarterly: Revenue YoY growth; Cloud Titans % of revenue; Product vs. services revenue mix; Gross margin (hardware pricing environment); Management commentary on AI networking order pipeline; Leading: Hyperscaler GPU cluster announcements — networking orders follow ~1 quarter later; Competitive: Cisco wins or loses in AI networking; InfiniBand vs. Ethernet adoption at hyperscalers)*

---

## Investment View

*(Populate: Valuation, WACC, DCF, Reverse DCF, Scenarios, Decision Log)*

### Decision Log

*(Append-only — no entries yet)*

---

## Recent Updates

### 2026-05-17

**Q1 2026 earnings (reported May 5):** Revenue $2,709M; EPS $0.87 vs. $0.79 expected (beat). Net income $1,022.9M. Q2 guidance: ~$2.8B. Full-year 2026 guidance raised to ~$11.5B. Source: FX Leaders / Simply Wall St / public.com, 2026-05-05. *Thesis bearing: Strongly confirms — beat and raised on AI networking demand.*

**AI fabric sales to more than double:** Management commentary cited AI fabric (7800 AI spine and Universal AI Fabric) sales expected to more than double in 2026 to ~$3.5B. Supply constraints (wafers, silicon, memory) are pressuring margins slightly but not demand. Source: FX Leaders, 2026-05-13. *Thesis bearing: Confirms the Ethernet-for-AI-clusters thesis; scale-out GPU networking is exactly the growth driver modeled.*

**Analyst upgrades:**
- Raymond James upgraded ANET to Outperform from Market Perform (May 15), citing new application growth and AI infrastructure market share gains
- Morgan Stanley raised PT to $180 from $165 (Overweight maintained)
Source: GuruFocus / Search results, 2026-05-15.

**AI Optical Group membership:** Arista joined the AI Optical Group, a consortium advancing optical networking standards for AI infrastructure. Positions Arista ahead of the co-packaged optics transition. Source: Yahoo Finance, 2026-05.

**Stock price and valuation gap:** ANET at $142.54 on May 13, approximately 25% below average analyst target of ~$182–$183. Source: FX Leaders, 2026-05-13. *Note: Stock is down ~17.9% at some point in recent history (prior pullback) and recovering with analyst upgrades.*

---

### 2026-05-19

**XPO MSA standard announced — AI data center optical interconnect:** Arista announced the XPO (eXternal Pluggable Optics) Multi-Source Agreement (MSA), a new optical packaging standard designed to reduce AI data center networking rack space by up to 75% and floor space by up to 44% vs. traditional pluggable optics. The XPO MSA uses high-density liquid-cooled optics enabling shorter cable runs and lower-power AI scale-up interconnect. This is part of Arista's positioning for the co-packaged optics transition in next-generation AI clusters. Source: Yahoo Finance / SEC Form 8-K / AI Optical Group, 2026-05. *Thesis bearing: Confirms — Arista is not just a switching vendor; it is actively shaping next-gen AI interconnect standards, which entrenches it in the AI data center build-out through the next hardware generation. The rack and floor space efficiency claims address hyperscaler power density constraints, the #1 infrastructure bottleneck.*

**AI Optical Group (already noted May 17) — additional context:** Arista's XPO MSA is the specific product initiative that accompanies its AI Optical Group membership announced May 17. The two items are related: joining the consortium advances the standards that the XPO MSA implements. *Combined reading: Arista is making a structured push into the optical layer of AI networking — moving up the stack from switching to interconnect architecture.*

---

### 2026-05-20

**Analyst PT divergence — TD Cowen to $200, Citi cut to $176:** Sell-side views are diverging post-Q1 earnings:
- TD Cowen raised PT to $200 from $170 (Outperform) — most bullish on AI fabric doubling to $3.5B in 2026
- Citi lowered PT to $176 from $186 — noting supply chain shortages are constraining near-term shipments and pressuring margins
- Consensus from 17 analysts remains Buy at $181.41 average target
Source: FX Leaders / public.com, 2026-05-14. *Assessment: The Citi cut highlights the real near-term risk — silicon and memory supply shortages are constraining ANET's ability to ship even when demand is strong. This is a timing/margin risk, not a demand risk. Long-term thesis intact.*

**Post-earnings stock recovery context:** ANET shares dropped ~13% after hours following May 5 earnings despite the beat, as the full-year guidance of $11.5B came in below some elevated buy-side expectations. Stock had recovered to ~$142.54 by May 13 (per prior scan entry). The consensus target of $181.41 implies ~27% upside from current levels. Source: FX Leaders / Quiver Quant, 2026-05. *Note: In Arista's case, the post-earnings gap lower on guidance that still beat consensus is characteristic of crowded positioning — not a change in underlying AI networking demand trajectory.*

### 2026-05-21

**EBO (Expanded Beam Optical) MSA — new AI optical interconnect standard:** Arista joined an industry standards group for next-generation Expanded Beam Optical (EBO) connectivity for AI infrastructure and is participating in a Multi-Source Agreement (MSA) targeting open, interoperable specifications for high-performance optical interconnects. This is distinct from the XPO (eXternal Pluggable Optics) MSA announced May 19 — Arista is now participating in two parallel optical interconnect standard tracks. Source: Search results / stockanalysis.com, 2026-05-21. *Thesis bearing: Confirms — Arista's simultaneous engagement in both the XPO and EBO standard-setting processes positions it to win regardless of which optical packaging approach prevails in AI data centers. The company is not a bystander but an active architect of the next interconnect generation.*

**NVDA Q1 results — AI networking demand validation:** NVIDIA's $75B data center quarter and $91B Q2 guide represent a direct increase in GPU cluster scale-out demand. Every incremental large GPU cluster requires the spine-leaf ethernet fabric that Arista builds — the networking order pipeline should follow the GPU shipment cadence with roughly a 1-quarter lag. Supply chain constraints (silicon and memory shortages noted by Citi) remain the primary near-term margin risk, not demand. Source: See [[NVDA]] 2026-05-21 entry.

---

### 2026-05-22

**Q1 2026 GAAP operating margin expanded to 42.7% — confirms operating leverage thesis:** GAAP income from operations in Q1 2026 was $1,157.8M on $2,709M revenue (42.7% margin), up sharply from FY2025 full-year average of 32.7% ($2,944.6M on $9,006M). Non-GAAP operating income reached $1,294M (47.8% margin). Q1 2026 operating cash flow was $1,693.5M — nearly 40% of FY2025's full-year OCF of $4.4B in a single quarter. Balance sheet: $2,789.5M cash + $9,563.7M marketable securities = $12,353M total cash/investments; zero debt; equity $13,487.1M. Source: SEC Form 10-Q (anet-20260331), 2026-05-05. *Thesis bearing: Confirms — the margin expansion from 32.7% (FY2025 average) to 42.7% (Q1 2026) demonstrates accelerating operating leverage on EOS software and services revenue; the 40% long-run EBIT margin modeled in the DCF is already being achieved and exceeded.*

**Hyperscaler CapEx $725B in 2026 (+77% YoY) — direct demand signal for AI networking:** Combined CapEx guidance from the Big Four (Microsoft $190B, Amazon ~$200B, Meta raised to $125–145B, Alphabet ~$175–185B) totals ~$725B in 2026, of which ~75% ($450–540B) is AI-related infrastructure. Meta raised its full-year 2026 capex from $115–135B to $125–145B, citing higher component costs and additional data center builds. Microsoft's $190B 2026 CapEx figure was well above the $152B analyst consensus. Approximately 60%+ of hyperscaler spend goes to power/cooling; the remainder directly funds hardware including networking. Source: Tom's Hardware / Yahoo Finance / Futurum Group, 2026-05-22. *Thesis bearing: Strongly confirms — this is the demand source that underpins ANET's $3.5B AI fabric target in 2026 and the FY2026 $11.5B revenue guidance. At $725B combined CapEx, hyperscalers are deploying GPU clusters at a scale that requires proportionally more 800G ethernet switching, and ANET is the primary supplier.*

**NVDA profit-taking (-1.77% today) — not a demand signal:** NVIDIA declined -1.77% on May 22 on post-earnings profit-taking after the historic Q1 FY2027 beat ($81.6B revenue, Q2 guide $91B). For ANET, this is immaterial — NVDA's $91B Q2 guide confirms GPU cluster scale-out continues at full speed. Networking orders follow GPU shipments with a ~1-quarter lag, so the Q2 FY2027 GPU shipment surge translates into ANET networking orders in Q3–Q4 2026. Consensus analyst target for ANET remains $181–188 (17 analysts Buy, average $181.41; 29 analysts show $187.98). High target: Rosenblatt $210 (May 6), TD Cowen $200 (May 19), Barclays $195 (May 7). Source: Market data / MarketBeat, 2026-05-22. *Thesis bearing: Neutral — NVDA price action is irrelevant to ANET's order pipeline; the underlying demand signal from NVDA's Q2 guide is unchanged and strongly confirmatory.*

---

### 2026-05-24

**Evercore ISI $200 PT reaffirmed (Outperform, May 23):** Evercore ISI reaffirmed its Outperform rating and $200 price target on Arista Networks, citing AI fabric revenue trajectory and data center networking leadership. At $154, ANET trades ~23% below the Evercore target, which aligns with TD Cowen ($200) and Rosenblatt ($210) as the higher end of the analyst range. Source: Market data, 2026-05-23. *Thesis bearing: Neutral — no new thesis signal; analyst confirmation reinforces the valuation gap. SELL/AVOID unchanged at MoS -17.6%.*

**AMD $10B+ Taiwan ecosystem investment — Venice CPUs on TSMC 2nm commencing H2 2026:** AMD announced more than $10B in investments across Taiwan's semiconductor ecosystem (May 21), including EPYC "Venice" server CPUs now in production on TSMC's 2nm process — the first high-performance compute product on 2nm. AMD's Helios AI rack platform (rack-scale AI infrastructure) targets H2 2026 deployment. Source: Focus Taiwan / EE Times, 2026-05-21. *Thesis bearing: Confirms — AMD's 2nm production ramp at TSMC confirms AI cluster compute demand is multi-vendor (NVDA GPU + AMD CPU at scale simultaneously). Every AI cluster deploying both NVDA GPU and AMD Venice CPU requires Arista's spine-leaf ethernet networking fabric. Expands total addressable cluster size beyond NVDA-only deployments.*

**No material new ANET-specific developments since May 23 — entity current:** All active thesis tracks captured in prior entries: (1) XPO + EBO MSA standards participation (optical interconnect positioning); (2) Q1 2026 beat-and-raise ($2.71B revenue, $11.5B FY guidance, $3.5B AI fabric); (3) supply "constrained for next couple of years" but demand "best I have ever seen" (CEO Ullal). Next material event: Q2 2026 earnings (est. August 2026). Key monitor: any greenfield AI fabric decision at a major hyperscaler selecting NVDA Spectrum-X over Arista EOS on a net-new cluster — the only thesis-breaking event; none observed.

---

### 2026-05-23

**Post-earnings momentum continues, stock +3.66% to $154.03:** ANET rose a second consecutive session to $154.03 with no specific new catalyst identified — the move reflects continued re-rating as the market digests the Q1 beat and $3.5B AI fabric target confirmed in the May 5 earnings call. At $154.03, the live MoS is approximately -17.6% vs. the DCF IV of $126.94 (last run May 22 at $148.59); the SELL/AVOID recommendation is unchanged. The stock has gained +9.7% in two sessions ($140.49 → $154.03). Source: Market data, 2026-05-23. *Thesis bearing: Neutral — price appreciation compresses the margin of safety further but does not alter the underlying AI networking demand trajectory.*

**NVDA Spectrum-X competitive update — integrative response confirmed:** NVIDIA's Spectrum-X platform has grown from zero to ~11.6% of the DC ethernet switch market, with Oracle and Meta deployments confirmed. However, Arista's strategic response is integrative: co-developing with NVIDIA BlueField-3 SmartNICs to build holistic networking stacks, turning potential competition into a partnership. This "integrate, don't fight" posture is the correct response given Arista's EOS embedding at existing hyperscaler deployments. Key monitor: any greenfield AI fabric decision at a major hyperscaler that selects Spectrum-X over Arista EOS on a net-new cluster. Source: NextPlatform / ainvest / SDxCentral, 2026. *Thesis bearing: Neutral — NVDA entry into ethernet switching is a real long-term risk but the installed-base EOS moat is intact; no evidence of hyperscaler EOS rip-and-replace yet.*

---

### 2026-05-26

**Supply chain commitment escalation — $8.9B non-cancellable purchase commitments, 52-week lead times confirmed:** Q1 2026 10-Q (SEC, March 31, 2026) discloses Arista's non-cancellable purchase commitments jumped from $6.8B at Q4-end to $8.9B (+31% QoQ) — of which $7.6B are due within 12 months and $1.3B extend beyond one year. Co-President Kenneth Duda confirmed in the May 5 earnings call that 52-week chip lead times are now the standard, with reservation requirements extending beyond one year. Management characterizes supply constraints as a "one- to two-year phenomenon," and Arista is absorbing higher procurement costs rather than fully passing them through ("eating a lot of the costs and giving our customers the benefit"). The commitment jump reflects deliberate management decision to lock in supply despite elevated cost, not financial distress. Source: SEC 10-Q (ANET-20260331) / Q1 2026 earnings transcript (Motley Fool / NetworkWorld), 2026-05-05. *Thesis bearing: Neutral — the $8.9B commitment escalation signals management's conviction that demand will persist through 2027–2028, making the multi-year lock-in economically rational; the margin headwind (Citi flagged in May 20 entry) is real but time-bounded, and the commitment itself is a forward demand signal, not weakness.*

**JPMorgan Technology Conference (late May) — SVP confirms demand exceeds supply; actual shipment growth ~54% YoY:** At the JPMorgan Global Technology, Media and Communications Conference, SVP Investor Relations Roderick Hall stated: "We already are in a situation where we can't ship as much product as we have demand for, and that's been the case for quite a while." The bottleneck is industry-wide — advanced semiconductor nodes, memory, and optical components — tied to the AI infrastructure build-out, not Arista execution problems. Q1 recognized revenue of $2.709B plus the deferred revenue balance implies actual shipment growth of approximately 54% YoY (management's framing), versus the headline 35.1% revenue growth figure — the gap is deferred billings, not demand shortfall. Q2 guidance: ~$2.8B revenue at 62–63% gross margin. Tariff exposure noted: supply chain touches Mexico (USMCA exemption), Malaysia, Vietnam (watch-and-wait on tariff status). Source: Investing.com / TIKR.com transcript, late May 2026. *Thesis bearing: Confirms — the 54% actual shipment growth figure is materially more bullish than the headline revenue number; supply is the constraint, not demand. The demand thesis is intact.*

**Stock price decline from $154.03 → $137.53 (-10.7% over May 22–26); MoS crosses from SELL/AVOID to HOLD:** Following the Q1 earnings-driven initial drop (May 5–6: -12 to -17%) and subsequent recovery to $154.03 (May 22–23), continued "margin anxiety" selling drove ANET to $137.53 on May 26 (down ~2.99% on the day; -10.7% vs. May 22 close). At $137.53, the live MoS = (IV $126.94 − $137.53) / $137.53 = **-7.7%**, crossing into the HOLD zone for low-uncertainty names (threshold: HOLD = -10% to +5%). The fundamental thesis is unchanged — supply constraints are demand-driven, management sees "best demand I have ever seen" — but the valuation gap has compressed. Source: Market data / Seeking Alpha "Buy the margin anxiety selloff", 2026-05-26. *Thesis bearing: Neutral — price-only move; underlying business trajectory unchanged. Updated Rec: HOLD at $137.53 (was SELL/AVOID at $154).*

---

### 2026-05-28 (Session 30 supplementary)

**ANET joins Expanded Beam Optical (EBO) MSA for AI datacenter interconnects (May 12 retroactive capture):** Arista joined a new multi-source agreement (MSA) coalition for expanded beam optical (EBO) technology on May 12, 2026. The EBO MSA includes 3M (lead coordinator), AMD, Amphenol, Arista, Cisco, Meta, Molex, Oracle, TE Connectivity, and others. EBO uses beam collimation optics to eliminate the polished end-face requirement of traditional MPO/MTP fiber connectors, addressing contamination and misalignment in ultra-high-density AI datacenter racks. This is Arista's second optical MSA of 2026 (separate from the XPO MSA for 12.8T liquid-cooled modules, launched at OFC March 2026). Source: 3M press release / Convergedigest / SDxCentral, 2026-05-12. *Thesis bearing: Confirms — EBO participation positions Arista at the forefront of two competing next-generation AI datacenter optical standards (XPO for bandwidth density, EBO for reliability in dense deployments). Arista's role in standards-setting reduces the risk of being bypassed by a competing vendor's proprietary optical system; ANET is building ecosystem lock-in one MSA at a time.*

**Price recovery to ~$158 (May 26-28); Rec reverts to SELL/AVOID:** ANET recovered from the May 22-26 decline ($154 → $137.53) and has returned to ~$158 by May 27-28. At $158, MoS = (IV $126.94 − $158) / $158 = -19.7%, which crosses back above the SELL/AVOID threshold (-10% for low-uncertainty names). The Rec reverts to SELL/AVOID from HOLD (HOLD was only valid near $137.53 on May 26). Source: Market data, 2026-05-27. *Thesis bearing: Neutral — price-only move; business fundamentals and AI networking demand trajectory unchanged.*

---

### 2026-05-29

**ANET May 28 confirmed close ~$154.50 (-2.2% from May 27's $158.01); MoS corrects to -17.8%:** Arista pulled back ~$3.50 on May 28 as margin headwind sentiment continued (supply chain cost absorption flagged by Citi in May). No specific negative catalyst; continuation of the "margin anxiety" narrative from the May 5 earnings-driven selloff. At $154.50, MoS = (IV $126.94 − $154.50) / $154.50 = -17.8% — tighter than the -19.7% at $158 but still SELL/AVOID. Source: Market data / Motley Fool, 2026-05-28. *Thesis bearing: Neutral — price-only move; Q1 2026 revenue $2.709B (+35.1% YoY), full-year $11.5B guide, and $3.5B AI fabric target are unchanged. Actual shipment growth 54% YoY per JPMorgan conference.*

**Arista named Leader in 2026 Gartner Magic Quadrant for Enterprise Wired and Wireless LAN:** Arista received the 2026 Gartner Magic Quadrant Leader designation for enterprise networking — a recognition that reinforces EOS software platform stickiness in enterprise (complementary to the hyperscaler AI fabric thesis). The MQ designation increases the switching cost at the enterprise level and supports the long-term ANET moat beyond hyperscaler AI networking. Source: StockTitan, 2026-05. *Thesis bearing: Confirms — incremental moat expansion; Gartner Leader status compounds EOS lock-in across enterprise and hyperscaler segments.*

---

### 2026-05-30

**ANET May 29 close $155.27 (+0.79%) — AI networking demand unchanged; 2026 AI revenue guidance $3.25–3.5B:** ANET closed at $155.27 on May 29 (+0.79% from $154.06). No new specific catalyst; mild recovery from "margin anxiety" selling. AI networking revenue guidance for 2026 stands at $3.25–3.5B (raised from $2.75B at Q1 earnings May 5), representing 83%+ growth in AI revenue year-over-year. Actual shipment growth of 54% YoY (per JPMorgan conference) confirms demand outpaces headline revenue recognition. At $155.27, live MoS = -18.2% vs. DCF IV $126.94 — SELL/AVOID. Source: Market data / Q1 2026 earnings, 2026-05-29. *Thesis bearing: Neutral — AI networking demand trajectory and the $3.25–3.5B 2026 guide are unchanged.*

---

## Cross-links

- [[NVDA]] — NVIDIA GPU cluster scale-out drives Arista networking demand; InfiniBand (NVDA) vs. Ethernet (ANET) is the competitive framing
- [[MRVL]] — Marvell supplies networking silicon to Arista; complementary at chip/system level
- [[TSM]] — Arista's networking ASICs manufactured at TSMC
- [[custom-silicon]] — hyperscaler networking ASICs may partially substitute for merchant silicon (Broadcom/Marvell) that Arista uses
