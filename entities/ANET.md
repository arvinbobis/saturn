# Arista Networks, Inc. (ANET)

> The dominant vendor for AI data center networking infrastructure —
> every scale-out GPU cluster needs high-speed, low-latency ethernet switching, and Arista builds it.

*Last updated: 2026-05-20 | Wisesheets data as of: not yet pulled*

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

---

## Cross-links

- [[NVDA]] — NVIDIA GPU cluster scale-out drives Arista networking demand; InfiniBand (NVDA) vs. Ethernet (ANET) is the competitive framing
- [[MRVL]] — Marvell supplies networking silicon to Arista; complementary at chip/system level
- [[TSM]] — Arista's networking ASICs manufactured at TSMC
- [[custom-silicon]] — hyperscaler networking ASICs may partially substitute for merchant silicon (Broadcom/Marvell) that Arista uses
