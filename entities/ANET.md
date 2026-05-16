# Arista Networks, Inc. (ANET)

> The dominant vendor for AI data center networking infrastructure —
> every scale-out GPU cluster needs high-speed, low-latency ethernet switching, and Arista builds it.

*Last updated: 2026-05-14 | Wisesheets data as of: not yet pulled*

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

## Cross-links

- [[NVDA]] — NVIDIA GPU cluster scale-out drives Arista networking demand; InfiniBand (NVDA) vs. Ethernet (ANET) is the competitive framing
- [[MRVL]] — Marvell supplies networking silicon to Arista; complementary at chip/system level
- [[TSM]] — Arista's networking ASICs manufactured at TSMC
- [[custom-silicon]] — hyperscaler networking ASICs may partially substitute for merchant silicon (Broadcom/Marvell) that Arista uses
