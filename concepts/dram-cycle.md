# DRAM Commodity Cycle

> The boom-bust cycle in DRAM pricing driven by capacity additions lagging demand signals by 18–24 months.

*Last updated: 2026-05-14*

---

## Cycle Mechanics

1. Demand strengthens → DRAM pricing rises → margins improve
2. All three DRAM makers (Samsung, SK Hynix, Micron) announce capacity expansions
3. New capacity takes 18–24 months to come online
4. When capacity arrives, demand has often moderated → oversupply
5. ASP falls sharply; gross margins collapse; losses mount
6. CapEx gets cut; some wafer starts idled → supply tightens
7. Demand recovers → cycle repeats

The cycle has historically run 2–4 years peak-to-peak. It has not been eliminated, though industry consolidation to three meaningful players has somewhat dampened magnitude.

## Historical Cycle Reference

| Period | Phase | Micron Gross Margin | Notes |
|---|---|---|---|
| 2017–2018 | Peak | ~58% (FY2018) | Data center buildout; crypto mining demand |
| 2019 | Trough | ~28% | Trade war; inventory correction |
| 2020–2021 | Recovery → Mid-cycle | ~30–35% | COVID accelerated data center demand |
| 2022 | Peak | ~47% | Pandemic demand overshoot |
| 2023 | Severe trough | Negative | PC and mobile demand collapsed post-COVID; $5.8B Micron operating loss |
| 2024+ | Recovery | Recovering | HBM ramp accelerating recovery; standard DRAM still pressured |

## Why FY2023 Was Unusually Severe

- COVID created a demand pull-forward in PC, mobile, and some server DRAM
- When demand normalized in 2022, inventory at OEMs was bloated
- Customers stopped buying while working through inventory
- DRAM price fell 50–70%; Micron's revenue halved from ~$30B to ~$15B in two years
- All three DRAM makers posted losses simultaneously

## HBM and Cycle Dampening

The central question for the Micron thesis: does HBM meaningfully dampen future cycle severity?

**Arguments for dampening:**
- HBM capacity conversion reduces standard DRAM bit output — less oversupply potential
- HBM is contracted (not spot) — contracted revenue is cycle-insensitive
- HBM demand (AI GPUs) is structurally growing and uncorrelated with PC/mobile cycles

**Arguments against dampening:**
- HBM is still ~10–15% of total DRAM bit output — standard DRAM dominates
- A severe standard DRAM oversupply can still dwarf HBM premium revenue
- If AI CapEx plateaus, HBM demand could also slow, removing the dampening mechanism

## CXMT (China) Wildcard

CXMT is ramping commodity DRAM (DDR4, DDR5) capacity with state subsidies. Their output adds supply to the commodity DRAM market without facing the discipline constraints that Samsung, SK Hynix, and Micron have learned. This could steepen the downside of the next standard DRAM cycle.

Track: TrendForce monthly reports on CXMT capacity additions and market share.

## Key Metrics to Monitor

- TrendForce monthly DRAM contract and spot price (DDR5 is the leading indicator)
- TrendForce quarterly DRAM supply/demand balance — bit supply growth vs. bit demand growth
- Any indication of inventory build at major DRAM customers (hyperscalers, PC OEMs)

## Dated Intelligence Log

### 2026-05-22 — MU

**TrendForce: DRAM contract prices +90–95% QoQ in Q1 2026 (record); +58–63% expected in Q2 2026** — Memory makers are reallocating capacity to HBM and server DDR5, driving across-the-board price increases. This is the acute shortage phase of the current cycle, the mirror image of the 2023 trough. Risk to watch: capacity additions from 2024–2025 expansions begin coming online in 2027, which could tighten the supply-demand balance if AI CapEx growth moderates even modestly.

### 2026-05-24 — MU

**TrendForce: Mobile DRAM +93–98% QoQ in Q2 2026; NAND flash +70–75% QoQ** — The memory price surge has extended beyond server DDR5 and HBM into mobile DRAM, which is rising even faster (+93–98% vs. +58–63% for server DDR5). Supplier capacity reallocation to AI/server applications is squeezing mobile DRAM inventory as well — suppliers prefer the higher-ASP AI segments. NAND flash price acceleration (+70–75% in Q2 vs. +60% in Q1) confirms the supply-demand dislocation is system-wide across all memory types. Final Q2 LTA negotiations concluding in May. No meaningful capacity expansion expected until late 2027. Implication: the supply constraint is broad-based, reducing the risk that AI-driven DRAM demand is a narrow niche; it validates MU's full product portfolio (HBM + server DDR5 + mobile) as pricing beneficiaries simultaneously.

### 2026-05-23 — MU / ASML

**HBM and server DRAM driving Q2 2026 contract price increases; CSPs securing supply via long-term agreements (TrendForce)** — AI server demand is pulling contract prices up across the entire DRAM stack. DDR5 profitability improving as capacity crowd-out from HBM production continues. The gap between HBM3e pricing and server DDR5 is narrowing toward 1–2x by end of 2026 (from 4–5x prior), reflecting DDR5 catching up rather than HBM falling — a bullish data point for the overall DRAM ASP environment.

### 2026-05-26 — MU (Session 26 / Mizuho structural call)

**Mizuho: memory market 30-50% structurally undersupplied through 2026-2027; no capacity relief until late 2027** — Mizuho's estimate of 30-50% undersupply is the most explicit sell-side confirmation to date that this is not a transient inventory cycle but a structural shortage. The mechanism: HBM capacity buildout is consuming wafer starts that previously served standard DRAM, reducing spot-market DRAM supply precisely as AI-driven demand accelerates. This is structurally distinct from prior cycles (2017-2018, 2020-2022) where demand was driven by PC/mobile upgrades subject to consumer discretionary cutoffs. AI inference CapEx is capex-committed and relatively price-inelastic, reducing the probability of demand destruction that has historically triggered cycle reversals. Counter-risk: if UBS's $1,625 PT attracts massive capacity investment that comes online 2028-2030, the structural undersupply could become structural oversupply — the cycle resets at a higher floor, not eliminates.

### 2026-05-26 — MU

**Micron CEO: filling only 50–67% of customer demand; first 5-year LTA signed — cycle-dampening thesis advancing** — CEO Sanjay Mehrotra confirmed Micron is fulfilling only 50–67% of key customers' medium-term memory demand — a supply-constrained posture not seen in prior cycles, where memory IDMs were supply-long and fighting for shelf space at declining ASPs. The first-ever 5-year strategic customer agreement represents the supply-demand regime change this thesis predicted: customers paying for supply certainty rather than waiting for spot-price collapses. Together with 2026 HBM4 capacity fully committed and HBM3E pricing at sustained premium levels, the structural factors preventing a 2023-magnitude trough (5×–8× HBM ASP premium, LTA contracts, capacity permanently redirected to AI) are all in place. The Harvard Willy Shih warning ("this too will pass") is the bear case — the counter is that AI DRAM demand is qualitatively different from consumer/mobile demand because it is capex-committed, opaque to spot markets, and growing faster than capacity expansion.

---

## Cross-links

- [[MU]] — primary entity affected by cycle; FY2023 trough is the baseline risk scenario
- [[HBM]] — the structural factor that may partially dampen cycle severity
- [[custom-silicon]] — hyperscaler custom silicon demand is relatively cycle-insensitive; dampens server DRAM component of cycle
