# Saturn Wiki Log

Append-only. Each entry records what happened and when.

Format:
- `## [YYYY-MM-DD] scan | daily` — daily agent scan
- `## [YYYY-MM-DD] ingest | [Source Title]` — manual source ingestion
- `## [YYYY-MM-DD] quarterly-review | [YYYY-QX] | [TICKER]` — quarterly review entry
- `## [YYYY-MM-DD] lint` — periodic health check

---

## [2026-05-21 ~01:00 UTC+4h] session-2

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: MU — event-driven (price move +3.88%, Samsung strike Day 1 / preliminary agreement)
Notable: Samsung's 18-day strike was AVERTED via tentative wage deal on May 21, suspending the walkout before material DRAM disruption. Union member vote May 22–27. MU DCF first run: IV $268.33 vs. current $744.68 → MoS -64%, SELL/AVOID under high-uncertainty framework. Stock is priced for 25%+ revenue CAGR from a $58.1B peak-cycle base — an extremely aggressive implied assumption.
Price movers >3% (new): ASML +3.04% (May 21 close, correcting Session 1 early-day reading of -0.52%); ASML two-day gain May 20-21 = +9.5%
No significant news: TSM (flat -0.21%), NVDA (-1.26% continuation of post-earnings sell-the-news), MRVL (-0.36%), ANET (-2.98%), ALAB (-0.20%)
DCF run: MU — IV $268.33, MoS -64.0%, Rec: SELL/AVOID (high uncertainty)

Entity updates:
- MU.md: Added Samsung strike AVERTED update (2026-05-21, thesis bearing: Challenges). Last updated timestamp refreshed.
- MU.json: All financial fields populated from Q2 FY2026 actuals — TTM revenue $58.1B, TTM EBIT ~$28.3B (peak cycle), cash $13.9B, debt $10.1B, shares 1,142M
- dashboard.md: ASML price corrected to $1,597 (+3.04%); HSBC $1,100 MU target added; Samsung union vote catalyst added; price mover flag updated
- tracker.md: MU row populated with IV $268.33 / MoS -64% / SELL/AVOID; Session 2 note appended; ASML price corrected to $1,597
- state/session.json: session_count 1→2; MU removed from event_queue; ASML added to event_queue; dcf_last_run.MU = 2026-05-21; last_run_utc updated

Lint findings:
- 5 of 7 tickers still have current_revenue_usd_m = 0 in DCF inputs: TSM, ASML, MRVL, ANET, ALAB
- Most critical: TSM (next rotation, schema exists) and ASML (in event queue, earnings data available)
- MRVL earnings May 27 will unlock financial data for that ticker
- No broken cross-links found; concepts/HBM.md, concepts/dram-cycle.md all exist from init

## [2026-05-21 21:00 UTC] session-1

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: NVDA — event-driven (Q1 FY2027 earnings released after close May 20)
Notable: NVIDIA Q1 FY2027 beat was historic — $81.6B revenue (+85% YoY), Data Center $75B (+92% YoY), Q2 guide $91B vs. $85–87B consensus; DCF model yields IV $156.27 (MoS -29.2%, SELL/AVOID at high uncertainty); simultaneously hyperscaler capex confirmed at $725B for 2026 (+77% YoY), the single strongest macro confirmation of the portfolio thesis.
Price movers >3%: MU +3.88% (Samsung strike preliminary agreement), MRVL +4.34% (analyst upgrades + NVDA $2B investment), ANET +3.86% (NVDA read-through)
No significant news: TSM (+0.21%), ASML (-0.52%), ALAB (+1.10%) — no material single-session news beyond ongoing trends
DCF run: NVDA — IV $156.27, MoS -29.2%, Rec: SELL/AVOID (high uncertainty)

Entity updates:
- NVDA: Added post-earnings reaction (AH -1.26%), $80B buyback + 25× dividend raise, and DCF result (IV $156.27, MoS -29.2%) to Recent Updates
- dashboard.md: Updated all 7 prices; added ALAB RBC $250 PT; noted April TSMC revenue catalyst resolved
- session.json: session_count 0→1; event_queue populated with MU/MRVL/ANET movers; dcf_last_run NVDA = 2026-05-21
- tracker.md: Session 1 portfolio snapshot populated; NVDA DCF result recorded; session note written

## [2026-05-21] daily-scan

Stocks checked: TSM, MU, ASML, NVDA, MRVL, ANET
Notable: NVIDIA reported Q1 FY2027 after close on May 20 — $81.6B revenue (+85% YoY), Data Center $75B (+92% YoY), non-GAAP EPS $2.39 (beat $1.79 estimate by 34%), and Q2 FY2027 guidance of $91B vs. $85–87B consensus; simultaneously, Samsung's 18-day strike began today (May 21) with ~45,000 workers at the Pyeongtaek and Hwaseong DRAM fabs, making this the largest semiconductor labor stoppage in history and directly benefiting Micron's HBM contracted position.
No significant news: ANET — NVDA results confirm AI networking demand; no new ANET-specific developments beyond ongoing optical standards work.

Entity updates:
- NVDA: Q1 FY2027 actual results: $81.6B revenue, $75B data center, $2.39 EPS, Q2 guide $91B; dividend raised $0.01→$0.25; Jensen Huang: "demand has gone parabolic"
- TSM: Arizona Fab 21 posted $514M profit in inaugural full year; Q1 2026 alone exceeded that figure; NVDA using Fab 21 for Blackwell accelerators
- MU: Samsung strike day 1 confirmed; ~45,000 workers; 3–4% DRAM disruption expected; MU premarket +4%; HBM market share updated to SK Hynix 62% / Micron 21% / Samsung 17%
- ASML: +6.19% on May 20 to $1,549.71; UBS reinstated as Europe's top pick, PT €1,900; High-NA EUV first chips expected in coming months
- MRVL: pre-market above $185; May 27 earnings consensus $2.40B revenue / $0.79 EPS; options pricing 13% move
- ANET: joined EBO MSA (second optical standard track alongside XPO MSA); NVDA demand validates AI networking pipeline

## [2026-05-20] daily-scan

Stocks checked: TSM, MU, ASML, NVDA, MRVL, ANET
Notable: NVDA Q1 FY2027 earnings released after market close tonight (actual results to be captured tomorrow); Micron confirmed shipping initial HBM4 units for NVIDIA's Vera Rubin platform — first HBM4 revenue from Micron and the single most material new thesis datapoint today; Samsung strike confirmed starting May 21 (tomorrow), adding supply-side pressure that further tightens HBM availability through June.
No significant news: TSM — Needham PT raised to $480 (minor); no new fundamental data until ~June 8 monthly revenue report.

Entity updates:
- TSM: Needham PT raised to $480; no May revenue report yet (due ~June 8–10)
- MU: Micron shipping initial HBM4 for Vera Rubin (NEW); Samsung strike begins tomorrow May 21; stock $661–674 range May 19
- ASML: 2026 guidance quantified at €38B (+16% YoY); buy ratings maintained; stock ~$1,463–1,512
- NVDA: Pre-earnings rally to $236 (+4.5%), market cap $5.71T; Q1 FY2027 results pending after close tonight
- MRVL: B. Riley raised PT to $205, Melius to $220, RBC to $200; stock +7.01% today; earnings May 27
- ANET: TD Cowen raised PT to $200; Citi cut to $176; supply chain shortages noted as near-term margin pressure

## [2026-05-19] daily-scan

Stocks checked: TSM, MU, ASML, NVDA, MRVL, ANET
Notable: NVIDIA Q1 FY2027 earnings are tonight (May 20 after close) — the single most anticipated print of the year, with consensus at $79.2B revenue and $1.78 EPS; separately, hyperscaler combined capex for 2026 is now tracking $725B (+77% YoY), more than doubling the $320B+ baseline thesis assumption and representing the strongest macro confirmation of the portfolio thesis to date.
No significant news: ASML — no new developments beyond May 18.

Entity updates:
- TSM: Hyperscaler capex $725B (+77% YoY) captured as macro thesis confirmation; CoWoS 80% CAGR underpinned by these commitments
- MU: Q3 FY2026 guidance $33.5B revenue (+260%) / $18.90 EPS (+1,025%) — highest growth guide in company history; Melius PT raised to $1,100; Micron exiting China data center market (Beijing restrictions — new risk flag)
- ASML: No update
- NVDA: US H200 clearance for 10 Chinese firms (75K units each); Jensen Huang at Trump-Xi summit expecting China breakthrough; pre-earnings consensus $79.2B/$1.78; $725B hyperscaler capex confirmation
- MRVL: NVDA $2B strategic investment (late March, previously uncaptured) added to entity; post-ATH pullback to $168.93 (−4.5%); earnings May 27
- ANET: XPO MSA optical standard announced — 75% rack reduction, 44% floor space savings; extends Arista into AI optical interconnect layer

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
