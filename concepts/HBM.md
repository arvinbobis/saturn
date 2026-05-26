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

### 2026-05-24 — MU / Samsung

**Samsung deal reached May 20 — 18-day strike averted; HBM4 production at Pyeongtaek and Hwaseong continues at normal run rates** — The 18-day work stoppage (May 21–June 7) that JPMorgan estimated would cause $14–$20.8B in operating profit losses did not occur. Samsung agreed to 10.5% profit-sharing as stock + 1.5% cash for 10 years. Ratification vote through May 26. Near-term HBM supply disruption risk eliminated; Samsung HBM4 supply for NVIDIA Rubin (and competing AI accelerators) uninterrupted. MU's structural advantage via LTA-contracted supply remains intact — Samsung's deal does not accelerate Samsung's HBM4 yield improvement or qualification timeline. Source: Tom's Hardware / abhs.in, 2026-05-20.

### 2026-05-24 — NVDA

**KeyBanc: Rubin GPU 2026 production cut 25% (2M→1.5M units) due to HBM4 certification delays at SK Hynix and Micron** — HBM4 is now the binding supply constraint for NVIDIA's next-generation Rubin platform. Both primary suppliers are still in qualification, which has back-loaded Rubin availability to late 2H 2026 or early 2027. This establishes HBM4 certification as the next major market-moving milestone: whichever supplier (SK Hynix or Micron) achieves first Rubin design win for HBM4 gains ~12–18 months of monopoly revenue at the highest possible ASP before the second supplier qualifies.

### 2026-05-24 (vote update) — Samsung / MU

**Samsung union vote 82.86% cast as of May 24; result announced May 27 (10am KST) — approval highly likely** — High voter turnout (82.86% of 57,290 eligible members through Sunday), driven by DS semiconductor division employees who benefit most from the 10.5% profit-sharing deal. Industry consensus expects ratification. If approved: Samsung HBM4 production at Pyeongtaek and Hwaseong proceeds with labor stability for the multi-year profit-sharing horizon, removing the last near-term HBM supply disruption risk. No impact on Micron's LTA-contracted capacity or pricing — MU is sold out into 2027 regardless of Samsung's production rate.

### 2026-05-25 — Samsung / MU

**Samsung TSP (Test & Package) division intentional slowdowns threaten HBM4 delivery schedules despite formal strike being averted** — Even though Samsung reached a tentative wage deal on May 20 (10.5% profit-sharing for memory workers), the deal exposed a massive internal bonus disparity: DS memory division workers receive ~$400,000 in performance bonuses while TSP/foundry/non-memory workers received ~$4,000. This disparity is triggering intentional work slowdowns, meeting cancellations, and a "work vacuum" in the TSP packaging division — the exact division responsible for advanced HBM stacking and testing. Tom's Hardware reports that "major AI chip project decisions have come to a complete halt" in the TSP division. Samsung HBM4 delivery risk has NOT been fully eliminated by the strike avoidance; the secondary threat is a protracted internal TSP operational slowdown. If Samsung HBM4 volume is constrained by TSP throughput, SK Hynix and Micron (whose A3 fab runs TSP inline) are direct supply beneficiaries — consistent with MU's HBM4 qualification race for Rubin. Source: Tom's Hardware / Seoul Economic Daily, 2026-05-22–24.

### 2026-05-25 — Samsung / MU

**Samsung DX union court injunction filing adds new procedural uncertainty to May 27 ratification — 87.4% turnout already cast, approval still likely** — Non-semiconductor DX division workers filing injunction at 9am May 26 (Suwon District Court) to halt the ratification vote; their grievance is the 93x bonus disparity ($4,300 DX vs. $400,000+ DS). As of 5:10pm KST May 25, 87.4% of 57,290 eligible voters have already cast ballots — Labor Ministry sides with the DS semiconductor union. Even if injunction succeeds, Samsung TSP packaging division slowdowns (the structural HBM4 supply risk) persist independently of the vote outcome. Micron's LTA-contracted HBM supply through 2027 is unaffected either way. Watch for court ruling May 26 KST morning and final vote result May 27 10am KST.

### 2026-05-26 — MU (UBS upgrade / $1T milestone)

**UBS raises HBM ASP model to +50% YoY; projects EPS >$100 through 2029; MU crosses $1T market cap** — UBS analyst Arcuri raised Micron's PT from $535 to $1,625 (+204%) on May 26, citing revised HBM ASP assumptions (+50% YoY vs prior +35%) and LTAs with NVIDIA through 2029. Stock surged 18% to $894, crossing $1 trillion market cap for the first time. This is the market's explicit endorsement of the "HBM breaks the DRAM commodity cycle" thesis: a $1T valuation is only rational if contracted LTA pricing insulates Micron from the trough that would otherwise reset the stock to $150-200. The UBS EPS >$100 projection through 2029 implies revenue >$160B, consistent with current Q3 FY2026 guidance of $33.5B (single quarter) annualizing to $134B with further growth projected.

### 2026-05-26 — MU

**Micron HBM4 in high-volume production for Vera Rubin; CEO confirms 50–67% demand fill; first 5-year LTA signed** — The HBM supply constraint has reached a structural ceiling: Micron's entire 2026 HBM4 capacity is sold out under binding contracts, CEO Sanjay Mehrotra states they are fulfilling only 50–67% of key customers' medium-term demand, and Micron has signed its first-ever five-year strategic supply agreement — a structural departure from quarterly/annual contracting that validates the "HBM breaks the commodity cycle" thesis. HBM4 (36GB 12H) for Vera Rubin is in high-volume production now. This is peak thesis confirmation for the HBM structural case: the binding 5-year LTA means a customer has accepted long-term pricing certainty in exchange for guaranteed supply — the mirror image of the 2023 spot-price collapse that characterized the commodity cycle. Hyperscalers and cloud providers are paying for supply certainty, not just chip specs.

---

## Cross-links

- [[MU]] — Micron; HBM3E supplier with Blackwell design win; thesis entity
- [[TSM]] — TSMC CoWoS packages HBM alongside compute dies; CoWoS is the packaging chokepoint
- [[NVDA]] — primary HBM customer; Blackwell GPU uses HBM3E
- [[cowos]] — the packaging technology that connects HBM to compute
- [[dram-cycle]] — HBM may dampen but not eliminate DRAM commodity cycles
