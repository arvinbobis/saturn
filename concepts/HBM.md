# High Bandwidth Memory (HBM)

> Stacked DRAM dies connected via through-silicon vias, placed directly alongside AI compute dies via CoWoS packaging. Required for every major AI training GPU.

*Last updated: 2026-05-14*

---

## What HBM Is

HBM is a stack of DRAM dies (typically 8–12 dies) connected vertically via through-silicon vias (TSVs), with a logic die at the base. The stack is then placed alongside a compute die (GPU, TPU) using TSMC's CoWoS advanced packaging. The result: memory bandwidth of 3–5 TB/s vs. ~100 GB/s for standard GDDR6 — at lower power consumption. AI training requires constant all-to-all parameter exchange across GPU memory; HBM is the only memory technology that can keep GPUs fed at the required bandwidth.

## HBM Generations

| Generation | Bandwidth | Capacity | Primary Use | Status |
|---|---|---|---|---|
| HBM2e | ~460 GB/s | 16–32GB | A100 (NVIDIA) | Mature |
| HBM3 | ~819 GB/s | 24–48GB | H100 | Volume |
| HBM3e | ~1.2 TB/s | 80–141GB | H200, Blackwell | Current ramp |
| HBM4 | ~1.8–2.4 TB/s | 128GB+ | Next-gen (2026+) | Development |

**Blackwell HBM3E:** NVIDIA's Blackwell B200 uses 192GB HBM3E (6 stacks × 32GB). Each generation of GPU increases HBM content significantly — both in capacity and bandwidth requirement.

## Supply Chain

| Supplier | Market Share | HBM3E Status | Notes |
|---|---|---|---|
| SK Hynix | ~50% | Primary NVIDIA supplier | First to market; Blackwell anchor |
| Micron | ~20–25% | NVIDIA certified for Blackwell | First HBM front-of-cycle position for Micron |
| Samsung | ~25–30% | Quality/yield issues | Has not been primary NVIDIA HBM3E supplier |

## Why HBM Is Strategically Different from Standard DRAM

1. **Contracted pricing** — allocated under long-term supply agreements, not spot market. ASP is 5–8x standard DRAM per bit.
2. **Capacity conversion constraint** — converting standard DRAM fab capacity to HBM reduces standard DRAM output. Adding HBM supply is a zero-sum trade with standard DRAM, limiting oversupply risk.
3. **Qualification barrier** — NVIDIA, AMD, and Google must qualify each supplier's HBM. Qualification takes 12–18 months. Switching is not trivial once a supplier is qualified.
4. **Demand concentration** — a small number of buyers (NVIDIA, AMD, Google, Amazon) represent nearly all HBM demand. High demand visibility; also high concentration risk.

## CoWoS Intersection

HBM cannot connect to a GPU without advanced packaging. TSMC's CoWoS is the packaging method — it creates the interposer substrate that HBM stacks sit on alongside the compute die. This means:
- Every HBM unit sold to NVIDIA must go through TSMC CoWoS packaging
- TSMC CoWoS capacity has been the binding constraint on AI chip supply (2023–2024)
- HBM demand and CoWoS demand are directly correlated

## Key Questions to Track

- Is HBM revenue growing fast enough as a % of Micron's total revenue to materially dampen cycle downturns?
- When does Samsung fix its HBM3E yield issues and intensify competition?
- What is Micron's position in HBM4 (qualification status, design wins)?
- Is HBM4 a format change that resets the qualification race?

## Dated Intelligence Log

### 2026-05-22 — MU

**HBM4 in volume production for Nvidia Vera Rubin; 2026 HBM sold out across all three suppliers** — Micron CEO confirmed supply crunch so severe the company can supply only 50–67% of key customers' requirements. All three memory makers have fully contracted 2026 HBM capacity; customers are now signing 3–5 year LTAs for 2027. This marks the structural shift from spot to contracted HBM pricing — the single most important development for the cycle-resistance thesis.

### 2026-05-23 — ASML / MU

**ASML targets 60+ EUV shipments in 2026; >51% going to memory (HBM/storage); Bloomberg Intelligence forecasts HBM market at $130B by 2033** — SK Hynix plans 20 Low-NA EUV units over two years, all dedicated to HBM production. At $130B by 2033 (up from ~$30B today), HBM is moving from GPU component to a major semiconductor category that drives its own equipment cycle — with both Micron (supply) and ASML (tooling) as direct beneficiaries.

### 2026-05-23 — MU

**HBM sold-out window extended from 2026 into 2027; multi-year LTAs now standard** — all three HBM makers' capacity is now committed through 2027, with customers unable to secure full requirements from any single supplier. The shift from spot/quarterly to 3–5 year LTAs is the structural inflection that eliminates ASP volatility for the contracted window — the single most important distinction between HBM and commodity DRAM that the thesis rests on.

### 2026-05-24 — NVDA

**KeyBanc: Rubin GPU 2026 production cut 25% (2M→1.5M units) due to HBM4 certification delays at SK Hynix and Micron** — HBM4 is now the binding supply constraint for NVIDIA's next-generation Rubin platform. Both primary suppliers are still in qualification, which has back-loaded Rubin availability to late 2H 2026 or early 2027. This establishes HBM4 certification as the next major market-moving milestone: whichever supplier (SK Hynix or Micron) achieves first Rubin design win for HBM4 gains ~12–18 months of monopoly revenue at the highest possible ASP before the second supplier qualifies.

---

## Cross-links

- [[MU]] — Micron; HBM3E supplier with Blackwell design win; thesis entity
- [[TSM]] — TSMC CoWoS packages HBM alongside compute dies; CoWoS is the packaging chokepoint
- [[NVDA]] — primary HBM customer; Blackwell GPU uses HBM3E
- [[cowos]] — the packaging technology that connects HBM to compute
- [[dram-cycle]] — HBM may dampen but not eliminate DRAM commodity cycles
