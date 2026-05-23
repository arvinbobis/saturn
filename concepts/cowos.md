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

---

## Cross-links

- [[TSM]] — TSMC; sole meaningful CoWoS capacity; separate revenue stream on top of wafer revenue
- [[HBM]] — HBM requires CoWoS to connect to the compute die; HBM demand = CoWoS demand
- [[NVDA]] — Blackwell requires CoWoS; NVIDIA was supply-constrained by TSMC CoWoS in 2023–2024
- [[MU]] — Micron HBM3E goes into CoWoS packaging at TSMC
