# CoWoS — Chip on Wafer on Substrate

> TSMC's advanced packaging that places HBM stacks alongside compute dies on a silicon interposer — the physical layer that makes AI chips possible.

*Last updated: 2026-05-14*

---

## What CoWoS Is

CoWoS (Chip on Wafer on Substrate) is TSMC's 2.5D advanced packaging technology. It places multiple dies — a compute die (GPU, TPU) and HBM memory stacks — on a silicon interposer, connecting them with thousands of short, dense interconnects rather than through a PCB. The result: dramatically higher bandwidth between compute and memory, at lower latency and power than traditional package-on-board approaches.

**Why this matters for AI chips:** AI training requires constant, high-bandwidth data movement between GPU compute and memory. CoWoS is the only packaging approach that can deliver the bandwidth HBM requires at the scale of a Blackwell GPU.

## CoWoS Revenue

CoWoS is additive revenue on top of wafer manufacturing. TSMC bills separately for:
1. Wafer manufacturing (the GPU or HBM die itself)
2. CoWoS packaging (the interposer and assembly)

This means every NVIDIA Blackwell GPU generates two revenue streams at TSMC: the wafer and the packaging. CoWoS revenue is tracked separately in TSMC's earnings commentary (not broken out as a line item but referenced directionally).

## Supply Constraint History

In 2023–2024, TSMC CoWoS capacity was the binding constraint on AI chip supply — not the compute die itself. NVIDIA had the GPU dies, but couldn't package them fast enough. This caused:
- AI chip lead times of 52+ weeks
- NVIDIA unable to fulfill hyperscaler orders on schedule
- TSMC's CoWoS utilization at 100%+ (with waitlists)

TSMC responded with aggressive CoWoS capacity expansion in 2024–2025. Track whether lead times have normalized or remain extended.

## Products That Require CoWoS

- NVIDIA H100, H200, Blackwell (B100, B200, GB200)
- AMD MI300X, MI350 (uses similar 2.5D packaging)
- Google TPU v5/v6
- Amazon Trainium2
- Any chip that uses HBM memory

## Key Metrics to Track

- CoWoS capacity (wafers/month) — TSMC reports directionally; absolute numbers occasionally from supply chain sources
- Lead time for CoWoS-packaged chips — when normalized, supply constraint lifted; when extended, still a bottleneck
- Revenue contribution — disclosed directionally in earnings commentary

## Dated Intelligence Log

### 2026-05-22 — TSM

**TSMC Arizona first fab posts $514M profit in year one; board approved $20B additional capital injection** — Demonstrates TSMC's advanced packaging economics (including CoWoS) are replicating successfully outside Taiwan. Q1 2026 TSMC net income NT$572B (+58.3% YoY), with 66.2% gross margin — driven by a combination of N3/N2 wafer revenue and CoWoS packaging revenue on Blackwell and HBM GPU production. The $20B Arizona capital injection signals TSMC's confidence in U.S.-based advanced packaging demand through at least 2030.

### 2026-05-23 — TSM

**Q1 2026 operating margin 58.1% (up from 50.8% FY2025 avg); 2026 CapEx guided $52-56B for CoWoS and N2 capacity** — The operating margin expansion from 50.8% to 58.1% reflects rising AI-HPC revenue mix (now >75% of revenue from North America) and CoWoS pricing power. The 2026 CapEx guide ($52-56B vs. $41B in FY2025) confirms CoWoS remains an active bottleneck requiring continued capital investment. NVIDIA's Vera Rubin and next-gen HBM4 integration will require TSMC CoWoS for the entire roadmap through at least 2028.

### 2026-05-27 — TSM / NVDA

**TSMC targeting 4x CoWoS capacity expansion: ~35,000 WPM (late 2024) → 120,000–140,000 WPM by end 2026; NVIDIA pre-committed >50% through 2027** — Jensen Huang flew to Taipei on May 23 specifically to secure production commitments from TSMC Chairman C.C. Wei for Vera Rubin. The bottleneck is packaging (CoWoS), not silicon fabrication. TSMC has committed $56B capex to expand CoWoS for the Rubin era. NVIDIA's Vera Rubin NVL72 is the first GPU platform to use CoWoS-L (the latest long-reach variant) alongside 8-layer HBM4 on TSMC N3P (3nm) — every one of these chips requires TSMC CoWoS packaging. Jensen declared Vera Rubin "the largest product launch probably in the history of Taiwan." The CoWoS constraint is now a KNOWN, QUANTIFIED bottleneck: TSMC is executing the largest advanced packaging capacity ramp in semiconductor history, and supply remains tighter than demand through 2026. Source: TechTimes / NVIDIA Blog / FinancialContent, 2026-05-24. — This confirms CoWoS is the single point of constraint for the entire Blackwell→Rubin transition; every custom ASIC (Marvell, Google TPU, Amazon Trainium) and every NVIDIA GPU requires CoWoS capacity. The 4x expansion is bullish for TSMC revenue per wafer and confirms TSMC's structural pricing power in advanced packaging through 2028.

### 2026-05-28 — NVDA / TSM

**Jensen Huang-C.C. Wei dinner confirms NVIDIA holds ~60% of all TSMC CoWoS capacity (~595K wafers in 2026); $150B annual Taiwan investment announced** — NVIDIA has committed to ~60% of TSMC's global CoWoS capacity for 2026, specifically ~510,000 CoWoS-L wafers for Blackwell/Rubin NVL72 production. Jensen Huang's private dinner with TSMC Chairman C.C. Wei (and 8 TSMC SVPs) was focused on securing capacity commitments for Vera Rubin before the June 1 Computex announcement. Jensen simultaneously announced $150B/year in total Taiwan investment (wafers, CoWoS, supply chain). CoWoS-L remains the most advanced variant — Vera Rubin is the first GPU to require it alongside HBM4. With TSMC targeting 120-140K WPM by end-2026 (from 35K WPM), and NVIDIA pre-committed to >50% of that capacity, the remaining ~60K WPM must absorb ALL other AI chip demand (AMD, custom ASICs, HPC). — CoWoS is the quantified chokepoint; NVIDIA's dominance of that chokepoint is both a structural moat and a supply constraint on competitors' ramp trajectories.

### 2026-05-28 — NVDA (Session 31)

**Oracle commits to "hundreds of thousands" of Vera CPUs for 2H 2026; Vera Rubin NVL72 (36 Vera CPUs + 72 Rubin GPUs per rack) adds CPU-side CoWoS demand on top of GPU** — Each Vera Rubin NVL72 rack requires CoWoS-L packaging for both the 72 Rubin GPU dies AND the 36 Vera CPU dies. Oracle's public pre-commitment of "hundreds of thousands" of Vera CPUs before the June 1 Computex launch is the first hyperscaler commitment translating to CoWoS demand beyond just GPU packaging. If Oracle deploys 200K+ Vera Rubin NVL72 racks (using hundreds of thousands of Vera CPUs), the CoWoS-L wafer requirement is proportionally larger than GPU-only deployments. This expands the CoWoS addressable demand per rack vs. prior Blackwell-only deployments — reinforcing TSMC's 4× capacity expansion thesis (35K → 130K WPM by end-2026).

### 2026-05-29 — TSM

**TSMC CoWoS yield at 98% as capacity scales toward 127,000 WPM by end-2026 (Digitimes May 14–15)** — Mature production yield means the 4× expansion from 35K WPM (late 2024) delivers near-4× usable output with minimal defect discount; bottleneck release is now a capacity-addition story, not a yield-improvement story; at 98% yield, TSMC CoWoS revenue is predictable per wafer of installed capacity.

### 2026-05-30 — NVDA

**Jensen Huang explicitly confirms NVIDIA will double Vera Rubin production capacity in 2026 (MGX Showcase, Taipei, May 29)** — CEO-level public confirmation of "doubling capacity" in 2026 for Vera Rubin aligns with the 35K→127K WPM trajectory for TSMC CoWoS-L; implies that from the ~63K WPM current run-rate, TSMC must add another ~64K WPM by year-end to satisfy NVIDIA's commitment alone; at NVIDIA's >50% capacity lock-in, all remaining AI chip demand (AMD, custom ASICs, HPC) must share the other ~63K WPM — CoWoS remains the binding supply constraint for the entire AI chip ecosystem through 2026.

---

## Cross-links

- [[TSM]] — TSMC; sole meaningful CoWoS capacity; separate revenue stream on top of wafer revenue
- [[HBM]] — HBM requires CoWoS to connect to the compute die; HBM demand = CoWoS demand
- [[NVDA]] — Blackwell requires CoWoS; NVIDIA was supply-constrained by TSMC CoWoS in 2023–2024
- [[MU]] — Micron HBM3E goes into CoWoS packaging at TSMC
