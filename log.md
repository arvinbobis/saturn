# Saturn Wiki Log

Append-only. Each entry records what happened and when.

Format:
- `## [YYYY-MM-DD] scan | daily` — daily agent scan
- `## [YYYY-MM-DD] ingest | [Source Title]` — manual source ingestion
- `## [YYYY-MM-DD] quarterly-review | [YYYY-QX] | [TICKER]` — quarterly review entry
- `## [YYYY-MM-DD] lint` — periodic health check

---

## [2026-05-18] daily-scan

Stocks checked: TSM, MU, ASML, NVDA, MRVL, ANET
Notable: Samsung's 61,000-worker 18-day strike (starting May 21) is the largest planned work stoppage in semiconductor industry history — analysts expect 3–4% DRAM supply disruption and order redirection to Micron and SK Hynix, making this the single most material development for the MU thesis; Marvell hit an all-time high of $182 on confirmed reports of an AI chip co-design agreement with Google (inference TPU + Memory Processing Unit), cementing Marvell's position at the center of the hyperscaler custom silicon wave.
No significant news: ANET — no material developments beyond the May 17 update; stock recovering near $142.

Entity updates:
- TSM: Barclays raised PT to $470 (Overweight); Cathie Wood sold $40.6M; Vera Rubin 2H 2026 ramp extends CoWoS demand
- MU: Samsung 18-day strike starts May 21 (MAJOR) — bullish for MU; Samsung began preemptive HBM4 shipments; analysts flag MU as beneficiary
- ASML: Apple-Intel foundry talks could drive €1.8–4.6B in EUV orders; €80M buyback; High-NA mass production 2027–2028
- NVDA: Earnings May 20 setup — consensus $78.8B revenue, $1.77 EPS; Vera Rubin in full production for 2H 2026; Jensen Huang $1T Blackwell+Rubin order book
- MRVL: Google/Alphabet AI chip co-design (inference TPU + MPU, ~2M units) — stock ATH $182; Polariton silicon photonics acquisition (Apr 22, uncaptured until today)
- ANET: No new material developments

## [2026-05-17] daily-scan

Stocks checked: TSM, MU, ASML, NVDA, MRVL, ANET
Notable: NVDA Q1 FY2027 earnings report lands May 20 — the single most important near-term event for the full portfolio; TSMC April 2026 revenue was NT$410.73B (+17.5% YoY), the second-highest month ever, confirming accelerating AI demand; Micron Q2 gross margin hit 74.9% with HBM sold out through 2026, but Samsung HBM4 reportedly passed NVIDIA qualification tests, introducing competitive pressure on Micron's HBM share.
No significant news: none — all six tickers had material developments.

Entity updates:
- TSM: April revenue (NT$410.73B, +17.5% YoY), Q1 GM 66.2%, $20B Arizona capital injection approved, Vanguard stake sale, $1.5T market forecast, Trump-Xi summit geopolitical context
- MU: Q2 +196% revenue, 74.9% GM, HBM sold out 2026, Samsung HBM4 qualification risk flagged, MU -5.5% on China H200 demand concern
- ASML: Q1 EPS beat ($8.37 vs $7.72), guidance raised, -5.22% post Trump-Xi summit, Tata Electronics India partnership
- NVDA: Q1 FY2027 earnings May 20, TD Cowen PT raised to $275, IREN 5GW AI infrastructure partnership, -4.42% May 15 on China H200 demand news
- MRVL: AMD 13F stake disclosed (+10% stock surge May 13), BofA PT raised to $200, Q1 FY2027 earnings May 27
- ANET: Q1 beat ($2,709M revenue, EPS $0.87 vs $0.79), FY2026 guidance raised to $11.5B, AI fabric to double to $3.5B in 2026, Raymond James upgrade to Outperform

## [2026-05-14] init | Repository seeded

Pages created: CLAUDE.md, index.md, log.md, entities/TSM.md, entities/MU.md, entities/ASML.md, entities/NVDA.md, entities/MRVL.md, entities/ANET.md, concepts/HBM.md, concepts/cowos.md, concepts/dram-cycle.md, concepts/custom-silicon.md, schemas/claude-tsm.md, schemas/claude-micron.md
Key context: Six satellite picks initialized with stub entity pages. Schema files for TSM and MU contain full standing knowledge and quarterly review workflows. Daily scan agent begins 2026-05-15.
