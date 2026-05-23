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

### 2026-05-23 — MU / ASML

**HBM and server DRAM driving Q2 2026 contract price increases; CSPs securing supply via long-term agreements (TrendForce)** — AI server demand is pulling contract prices up across the entire DRAM stack. DDR5 profitability improving as capacity crowd-out from HBM production continues. The gap between HBM3e pricing and server DDR5 is narrowing toward 1–2x by end of 2026 (from 4–5x prior), reflecting DDR5 catching up rather than HBM falling — a bullish data point for the overall DRAM ASP environment.

---

## Cross-links

- [[MU]] — primary entity affected by cycle; FY2023 trough is the baseline risk scenario
- [[HBM]] — the structural factor that may partially dampen cycle severity
- [[custom-silicon]] — hyperscaler custom silicon demand is relatively cycle-insensitive; dampens server DRAM component of cycle
