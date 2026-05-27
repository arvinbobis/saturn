# Custom Silicon — Hyperscaler ASICs

> The trend of major hyperscalers designing their own AI chips rather than buying NVIDIA GPUs — creating the second AI silicon wave that flows through Marvell and TSMC.

*Last updated: 2026-05-14*

---

## What Custom Silicon Is

Custom ASICs (Application-Specific Integrated Circuits) designed by hyperscalers for their specific AI workloads — training large models, running inference at scale, processing recommendation system queries. Unlike NVIDIA's general-purpose GPUs, custom ASICs are optimized for one company's specific models and infrastructure, yielding better performance-per-watt and lower cost-per-inference at scale.

## Why Hyperscalers Build Custom Silicon

1. **Cost at scale:** At 100,000+ chips, even a 20% cost improvement per chip is billions of dollars annually
2. **Performance optimization:** A chip designed for the exact model architecture and data types runs more efficiently than a general-purpose GPU
3. **Supply independence:** Reduces dependency on NVIDIA's supply chain, pricing, and roadmap
4. **Competitive differentiation:** A faster inference chip means cheaper AI products for customers

## Major Custom Silicon Programs

| Company | Chip | Type | Co-designer | Foundry | Status |
|---|---|---|---|---|---|
| Google | TPU v5/v6 | Training + Inference | Marvell (partially) | TSMC | Volume production |
| Amazon | Trainium2 | Training | Annapurna/Marvell | TSMC | Ramp |
| Amazon | Inferentia | Inference | Annapurna | TSMC | Volume |
| Microsoft | Maia 200 | Training | Marvell | TSMC | Ramping |
| Meta | MTIA (Meta Training and Inference ASIC) | Inference | Internal | TSMC | Production |
| Apple | Neural Engine (A/M series) | On-device inference | Internal | TSMC | Mature |

## Portfolio Implications

**TSMC (TSM):** All custom silicon is manufactured at TSMC. The custom silicon trend creates a *second* AI silicon demand wave on top of NVIDIA/AMD GPU demand. Even if NVIDIA loses some hyperscaler share to custom ASICs, total TSMC wafer demand may grow — because custom ASICs plus NVIDIA GPUs together use more wafers than NVIDIA alone.

**Marvell (MRVL):** Marvell is the primary co-design partner for several hyperscaler programs (Google, Amazon, Microsoft). Marvell provides the ASIC design engineering that hyperscalers don't want to build fully in-house. As more hyperscalers launch custom silicon programs, Marvell's pipeline grows.

**NVIDIA (NVDA):** Custom silicon is a competitive threat — but primarily at inference, not training. NVIDIA still dominates training because CUDA is deeply embedded. The threat is real but slower-moving than headlines suggest.

## Timeline Dynamics

Custom ASIC design cycles: 18–24 months from design kickoff to first silicon; 6–12 more months to production qualification. Revenue from a design win flows 2–4 years after the win announcement. This means Marvell's current design wins are the 2026–2028 revenue, not next quarter.

## Key Questions to Track

- How many hyperscalers have active Marvell co-design relationships? Any new wins announced?
- Is custom silicon taking inference share from NVIDIA faster than expected?
- Does NVIDIA respond with inference-optimized products (NIM, Spectrum-X, etc.) that blunt custom silicon adoption?

## Dated Intelligence Log

### 2026-05-24 — MRVL

**Custom ASIC revenue scaled from zero to $1.5B in FY2026; management guiding >20% YoY growth in FY2027 and at least doubling in FY2028** — pre-earnings consensus data confirms the custom silicon ramp is now a material revenue line at Marvell, not a future promise. At >$2B projected by FY2029 from NIC and CXL use cases alone, custom silicon is transitioning from a growth driver to Marvell's defining revenue segment. The 3-year trajectory ($0 → $1.5B → $1.8B → $3B+) is the fastest-scaling silicon franchise in the current AI supply chain wave. Amazon Trainium3 (Scorpio X) confirmed in active production ramp; XPU-Attach broadening beyond Amazon. Source: ad-hoc-news.de / Quiverquant, 2026-05-22.

### 2026-05-23 — MRVL

**Stifel: optical interconnect revenue growth revised from 30% to 50% YoY for FY2027; AWS Trainium 3 confirmed in production; XPU-Attach broadening** — Stifel's pre-earnings channel check (PT raised $140→$210) produced the first third-party confirmation that Trainium 3 is actively ramping and that interconnect growth is accelerating. XPU-Attach — Marvell connectivity silicon bundled into hyperscaler custom ASIC deployments — is expanding to programs beyond Amazon, suggesting the custom silicon supply chain attach rate is increasing faster than prior models assumed. If confirmed at May 27 earnings, this 50% interconnect growth guide would meaningfully revise the FY2027 revenue story.

### 2026-05-22 — MRVL / ALAB

**NVDA invested $2B strategically in Marvell; Amazon Trainium3 (Scorpio X) ramp visible through Astera Labs** — NVDA's $2B stake validates Marvell as the central co-design partner for the custom ASIC wave, not a peripheral player. The Amazon Trainium3 ramp is evidenced by ALAB's revenue growth (+93% YoY Q1 2026) from PCIe connectivity into the Scorpio X cluster. The three-company stack — MRVL (ASIC design) + ALAB (connectivity) + TSM (foundry) — confirms the custom silicon supply chain is scaled and investable. Jensen Huang on Dwarkesh (April 15, 2026) confirmed NVIDIA views custom ASICs as complementary at inference, not competitive at training.

### 2026-05-24 — MRVL

**Marvell's Celestial AI acquisition ($3.25B, Feb 2, 2026) confirms optical interconnect is now inseparable from the custom ASIC thesis** — Custom ASICs designed for inference at hyperscale require optical scale-up interconnects (not just copper) to link chips at 3.2T+ bandwidth. Celestial AI's Photonic Fabric™ + Polariton's plasmonics (April 2026) give Marvell end-to-end optical IP that complements its ASIC design wins. This means Marvell is not just the custom silicon co-designer but the optical connectivity layer that custom silicon clusters require — effectively expanding the per-cluster attach value. The optical moat (Celestial AI + Polariton + legacy SerDes/DSP) is now the second structural choke point in Marvell's business model alongside the ASIC co-design franchise. Confirmed hyperscaler design base now spans Google, Amazon, and Microsoft.

### 2026-05-27 — MRVL

**XConn Technologies ($540M acquisition, completed Feb 10, 2026) extends Marvell from ASIC co-designer to full connectivity stack including PCIe/CXL switches — direct ALAB competition** — XConn's PCIe 5 + CXL 2.0 switches are in production; PCIe 6 + CXL 3.1 switches are sampling (the latter directly competes with Astera Labs Scorpio X 320-lane PCIe 6 switch). XConn will contribute ~$100M in revenue in FY2028, beginning H2 FY2027. Combined with Celestial AI (Photonic Fabric optical scale-up), Polariton (plasmonics for co-packaged optics), and legacy SerDes/DSP IP, Marvell's connectivity offering now spans the entire data center fabric layer. The custom silicon thesis has expanded: Marvell is not just co-designing the compute chips, it is also supplying the switches, optical links, and DSP silicon that connect those chips. This raises the per-cluster attach value materially — every AI cluster needs both the custom ASIC AND the interconnect, and Marvell now provides both. Source: Data Center Dynamics / Marvell Newsroom, 2026-02-10.

### 2026-05-26 — MRVL

**Amazon $225B Trainium commitment backlog (exiting Q1 2026 calendar) is the largest single-customer quantification of custom silicon demand to date** — Wells Fargo's May 20 channel check revealed Amazon had $225B in committed Trainium deployments exiting Q1 2026. At Marvell's estimated revenue share per cluster, this underpins Wells Fargo's $6B annual Trainium-related revenue forecast for FY2027 and FY2028. The $225B figure reframes the custom silicon thesis from "emerging" to "committed infrastructure program at scale." This is not CapEx guidance; it is committed deployment — meaning the silicon co-design work (Marvell), manufacturing (TSMC), and connectivity (Astera Labs) are already contracted downstream. Custom silicon is no longer a thesis about what hyperscalers might do; it is now quantifiably underwritten.

---

## Cross-links

- [[MRVL]] — primary beneficiary; co-designs hyperscaler custom ASICs
- [[TSM]] — manufactures all custom silicon; additive demand on top of NVIDIA/AMD wafers
- [[NVDA]] — threatened at inference; maintains training dominance via CUDA
- [[ANET]] — custom silicon clusters still need networking infrastructure; Arista benefits
