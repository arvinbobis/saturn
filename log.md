# Saturn Wiki Log

Append-only. Each entry records what happened and when.

Format:
- `## [YYYY-MM-DD] scan | daily` — daily agent scan
- `## [YYYY-MM-DD] ingest | [Source Title]` — manual source ingestion
- `## [YYYY-MM-DD] quarterly-review | [YYYY-QX] | [TICKER]` — quarterly review entry
- `## [YYYY-MM-DD] lint` — periodic health check

---

## [2026-05-23 12:00 UTC] session-9

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: ANET — event_queue (Q1 2026 earnings review; +3.1% on May 22 catalyst)
Notable: ANET entity confirmed current through May 22; May 23 update added (stock +3.66% to $154.03, second consecutive session of gains post-earnings; NVDA Spectrum-X competitive context confirmed — integrative response with BlueField-3 is correct posture; Spectrum-X at ~11.6% of DC ethernet market but no hyperscaler EOS rip-and-replace evidence). No DCF re-run (last run May 22, IV $126.94, MoS est -17.6% at new price). Schema corrected: Q1 2026 YoY growth fixed from 27.7% (FY guidance rate, mislabeled) to 35.1% (actual Q1 YoY). All 7 tickers remain SELL/AVOID. Strongest macro confirmation ever: hyperscaler CapEx $725B in 2026 (+77%); DRAM prices +58–63% QoQ Q2 2026; TSMC Arizona $514M year-one profit.
No significant news: TSM (~flat, $407.15), MU (~flat, $771), ASML (+2.7% to $1,592 — ASML targets 60+ EUV in 2026; 51% to memory), NVDA (-1.8% to $219.51, healthy digestion post-Q1 blowout), ALAB (~flat, $309.78).
DCF run: none
Concept pages updated: HBM (2 entries), dram-cycle (2 entries), cowos (1 entry), custom-silicon (1 entry) — all received first-ever dated catch-up entries

Phase 5 lint:
- TSM: added to event_queue position 0 (null DCF — 9 sessions overdue); TSM.json revenue=$122,900M and price=$407.15 populated as quick fix; full financial inputs still needed for DCF run
- ANET "Post-earnings deep review Session 9" catalyst removed from Upcoming Catalysts (completed)
- Morgan Stanley $180 and Citi $176 ANET analyst targets added to dashboard
- Concept pages: all 4 had zero dated entries — bulk catch-up written from sessions 1–9 findings
- Cross-links: no broken references found in ANET entity; [[NVDA]], [[MRVL]], [[TSM]], [[custom-silicon]] all exist

---

## [2026-05-22 12:00 UTC] session-8

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: ALAB — event-driven (>7.5% move May 22; new 52-week high $315.73; DCF = null; Amazon Trainium3 Scorpio X ramp; Q1 $308.4M +93% YoY; Q2 guide $365M)
Notable: ALAB first DCF run yields IV $111.84 vs. $309.78 price → MoS -63.9% → SELL/AVOID. Even at 35% revenue CAGR for 10 years with full R&D capitalization ($837M capitalized R&D, +$199M adj to EBIT), the intrinsic value is 64% below current price. Sensitivity confirms: 25% CAGR at 10% WACC gives IV $232 — still below market. ALAB is priced for perfection (~112x forward EPS). Thesis is CONFIRMED (Amazon Trainium3 Scorpio X design win, PCIe Gen 6 >1/3 of Q1 revenue, 76.3% gross margin) but valuation leaves zero margin of safety. Also: ANET flagged with +3.1% move on May 22 (Q1 earnings beat + Gartner MQ Leader); added to event_queue. Hyperscaler CapEx $700B in 2026 confirmed — 2027 trending >$1T. TrendForce Q2 DRAM +58-63% QoQ. Samsung union vote ongoing.
No significant news: TSM (flat, +46% YTD, May revenue due ~June 8), MU (+1.6% to $771; Samsung vote ongoing), ASML (~flat $1,592; High-NA first products "within months"), NVDA (-2.4% to $218.13, healthy post-earnings digestion).
DCF run: ALAB — IV $111.84, MoS -63.9%, Rec: SELL/AVOID (high uncertainty)

Entity updates:
- ALAB.md: Financials section fully populated (Q1 2026 actuals, FY2024/FY2025 annual, balance sheet, TTM); 2026-05-19 entry added (JP Morgan TMC Conference, Scorpio X ramp confirmation, +12-16% surge, JPM $280/Roth $275/Needham $260/Stifel $260 PTs); 2026-05-22 entry appended (Session 8 DCF run note + ANET >3% cross-portfolio flag). Last updated timestamp updated to 2026-05-22 Session 8.
- ALAB.json: All financial inputs populated — revenue $1,001.5M (TTM), EBIT $200.4M, CapEx $8M, D&A $15M, cash $1,200M, debt $0, equity est $1,400M, shares 182.5M diluted, price $309.78, R&D $411M (TTM), R&D history [50, 70, 180, 350]. Story narrative updated for Q1 beat, Amazon Trainium3 win, Scorpio X ramp, valuation risk.
- dashboard.md: Prices updated — MU $771 (+1.6%), NVDA $218.13 (-2.4%), MRVL $195.96 (+2.8%), ANET $148.59 (+3.1%⚑). ALAB catalyst moved to "processed." ANET added to Upcoming Catalysts (Session 9). TSM May Revenue catalyst flagged with dcf_last_run = null warning. New analyst PTs added (JPM $280, Roth $275, Needham $260, Stifel $260 — all for ALAB, dated May 19).
- decisions/tracker.md: ALAB IV $111.84, MoS -63.9%, SELL/AVOID added. All prices refreshed. Session 8 notes and history row appended.
- state/session.json: session_count 7→8; ALAB removed from event_queue (processed); ANET and MRVL-pre-earnings added to event_queue; dcf_last_run.ALAB = 2026-05-22; last_run_utc = 2026-05-22T12:00:00Z; last_deep_session = ALAB.
- log.md: session-8 appended (this entry).

Lint findings:
- TSM: dcf_last_run = null — CRITICAL GAP. TSM is the portfolio's largest position rationale (foundry monopoly) but has no intrinsic value estimate. Next session after event_queue clears (ANET, MRVL-earnings) should prioritize TSM DCF.
- MRVL earnings May 27: event_queue item; entity is current; DCF last run May 22 (IV $119.91, MoS -38.8%). Post-earnings session will refresh DCF.
- Samsung union vote: result expected by May 27. Watch alongside MRVL earnings.
- No stale catalysts removed (all upcoming dates still valid as of May 22).

---

## [2026-05-23 00:00 UTC] session-7

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: MRVL — event-driven (price move +3.1% May 22; new 52-week high $183.52; pre-earnings positioning ahead of May 27 Q1 FY2027 report)
Notable: ALAB surged to new 52-week high $315.73 (+7.5% from $288.06 Session 6 reference) driven by Evercore ISI PT raise $215→$297 and RBC second raise $250→$270, confirming Amazon Trainium3 Scorpio X ramp narrative. Q2 2026 guide up to $365M (+18% QoQ) reconfirmed from May 5 earnings. ALAB added to event_queue as highest-priority Session 8 item (no DCF run, entity needs financial data). MRVL: no new material developments since Session 6; entity is current; DCF IV $119.91 (SELL/AVOID) unchanged. Hyperscaler CapEx 2026 confirmed at $700B+ combined (Amazon $200B, Google $175-185B, Meta $115-135B, MSFT $120B+) — strongest macro backdrop to date. TrendForce Q2 DRAM +58-63% QoQ reconfirmed. Taiwan ADIZ 169 incursions April; no acute escalation.
No significant news: TSM (flat), MU (Samsung vote ongoing, averted deal priced in), NVDA ($223.47 close confirmed), ANET (flat). ASML USD -2.5% to $1,592 (EUR/USD FX effect; EUR price flat €1,390).
DCF run: none — MRVL last run 2026-05-22 (Session 6); no new earnings; no triggers met.

Entity updates:
- ALAB.md: 2026-05-22 entry added — Evercore ISI $297 PT (from $215), RBC second raise to $270 (from $250), Q2 guide up to $365M confirmed, new 52W high $315.73, >3% trigger flagged. Last updated refreshed to 2026-05-22 Session 7.
- dashboard.md: ALAB price updated $288.06→$309.78 (+7.5%⚑ new 52W high); ASML updated $1,633→$1,592 USD (EUR/USD effect); ALAB added to Upcoming Catalysts; ALAB analyst PTs updated (RBC $270, Evercore $297). Session 7 noted.
- tracker.md: ALAB price $309.78, story updated; ASML MoS recalculated -29.5% ($1,592); Session 7 note appended; Session History row added.
- state/session.json: session_count 6→7; MRVL removed from event_queue (processed); ALAB added to event_queue (>3% trigger + no DCF); last_run_utc 2026-05-23T00:00:00Z; last_deep_session = MRVL.
- log.md: session-7 appended (this entry).

Lint findings:
- TSM: dcf_last_run = null — no financial data in JSON; critical gap; not next in rotation but should be addressed.
- ALAB: dcf_last_run = null — entity stub lacks Financials section; Session 8 must pull TTM financials and run DCF. Highest priority.
- MRVL earnings May 27 (5 days): no deep session needed until after earnings report; monitor for post-earnings trigger (expected Q1 FY2027 results = new financial data → Phase 3 DCF refresh).
- Samsung union vote ongoing through May 27 — watch for final outcome alongside MRVL earnings day.

---

## [2026-05-22 20:00 UTC] session-6

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: MU — event-driven (price move +4.76% May 22; NVDA $91B Q2 guide HBM demand confirmation; Samsung union vote May 22-27 ongoing)
Notable: HBM supercycle confirmed at industry level — all three memory makers' 2026 capacity sold out; customers now negotiating 3–5 year LTAs for 2027; Micron expects HBM TAM to reach $100B by 2028 (two years ahead of prior estimates). Hyperscaler CapEx 2026 confirmed at $720B combined (Amazon $200B, MSFT $190B, Google $185B, Meta $135B), with 2027 trending >$1T — materially reduces AI CapEx plateau risk. Samsung union vote underway (May 22-27, tentative deal reached May 21). TrendForce 2Q26: DRAM contract prices +58-63% QoQ; RDIMM prices temporarily overtaking HBM (LTA pricing lag); supply remains tight across all products. No DCF re-run (last run May 21). MRVL hit new 52-week high $183.52 (+3.1%) on May 22 — added to event_queue for Session 7 ahead of May 27 earnings.
No significant news: TSM (~flat), ANET (~flat), ALAB (~flat). ASML +2.6% continuing surge (3-day total +5.7%). NVDA recovered to $223.47 (+1.30% May 22 close).
DCF run: none (MU last run May 21; triggers not met)

Entity updates:
- MU.md: 2026-05-22 entry added — Samsung union vote underway; MU -0.4% on averted-strike pricing; NVDA Q1 FY2027 $81.62B/$91B Q2 confirmed; TrendForce 2Q26 DRAM +58-63% QoQ / RDIMM prices temporarily leading HBM; HBM 2026 capacity sold out across top 3 / 2027 LTAs being signed / $100B TAM by 2028; hyperscaler CapEx $720B (2026) trending >$1T (2027). Last updated refreshed to 2026-05-22 Session 6.
- dashboard.md: Session 6 prices updated — MU $759 (-0.4%), ASML $1,633 (+2.6%), NVDA $223.47 (+1.30%), MRVL $183.52 (+3.1%⚑ new 52-week high); ALAB Evercore ISI $297 PT added; institutional entry price table updated; catalyst notes updated.
- tracker.md: All 7 prices updated; MRVL MoS updated to -34.7% ($183.52 vs. IV $119.91); ASML MoS updated to -31.2% ($1,633); NVDA MoS updated to -30.1% ($223.47); MU MoS updated to -64.6% ($759); Session 6 note appended; Session History row added.
- state/session.json: session_count 5→6; MU removed from event_queue; MRVL added (+3.1% trigger); last_run_utc updated to 2026-05-22T20:00:00Z; last_deep_session = MU.
- log.md: session-6 appended (this entry).

Lint findings:
- TSM and ALAB: dcf_last_run still null — critical gap. TSM is next in rotation after MRVL event resolves. ALAB still stub with no financial data.
- MRVL earnings May 27 (5 days): Session 7 should process MRVL event-driven (earnings QN-2027 + price move). Q1 FY2027 results will unlock updated financials for DCF refresh.
- Samsung union vote May 22-27: outcome pending. If rejected, MU supply-disruption thesis re-engages. Monitor for Session 7 update.
- No stale catalysts in dashboard (all are still active).

## [2026-05-22 16:00 UTC] session-5

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: ASML — event-driven (price move +9.5% two-day May 20-21; Q1 FY2026 beat; raised FY2026 guidance to €36-40B)
Notable: TSMC officially deferred High-NA EUV adoption to 2029, citing €350-400M per unit cost (2x standard EUV). This moderates the High-NA ASP revenue uplift timeline from TSMC but does not threaten Low-NA demand; ASML's FY2026 guidance was raised anyway (€36-40B vs. €34-39B prior). Q1 2026 operating margin of 36.0% is the highest in company history. DCF first run: IV $1,122.64 vs. $1,592 → MoS -29.5% → SELL/AVOID (medium uncertainty). At WACC ~8%, IV = $1,641 — implying the market is pricing monopoly WACC compression. ASML's -29.5% MoS is similar to NVDA (-28.8%) — the entire AI hardware supply chain appears priced for perfection.
Price movers >3% (new, May 22 Session 5): none detected. MRVL +1.3% from Session 4, ANET +0.9% from Session 4 — both within noise.
No significant news: TSM (~flat), MU (~flat), NVDA (-1.77% continuing), MRVL (~+1.3%), ANET (~+0.9%), ALAB (~flat)
DCF run: ASML — IV $1,122.64, MoS -29.5%, Rec: SELL/AVOID (medium uncertainty)

Entity updates:
- ASML.md: 2026-05-22 entry added — Q1 2026 financials quantified (€8.767B revenue, €3.158B EBIT, 36% op margin, €2.757B net income); TSMC High-NA EUV deferral to 2029 detailed; ASML customer pivot (Intel + SK Hynix + Samsung on High-NA); two-day surge context; Financials section populated with Q1 2026 and TTM tables. Last updated timestamp refreshed.
- ASML.json: Full TTM financial data populated — revenue $39,214M, EBIT $13,220M, cash $9,741M, debt $3,140M, equity $22,795M, shares 392M, price $1,592; R&D $5,234M with 5-year history; story narrative updated for TSMC High-NA deferral context.
- dashboard.md: Session 5 prices updated; ASML $1,592 (+3.04% from May 20-21 move noted); MRVL $177.95, ANET $147.71 updated; NVDA -1.77% continuing.
- tracker.md: ASML row populated with IV $1,122.64 / MoS -29.5% / SELL/AVOID; MRVL updated to $177.95 / MoS -32.6%; ANET updated to $147.71 / MoS -14.1%; Session 5 note appended; Session History row added.
- state/session.json: session_count 4→5; ASML removed from event_queue; MU remains in queue; next_deep_session updated to NVDA; dcf_last_run.ASML = 2026-05-22; last_run_utc updated to 16:00 UTC.

Lint findings:
- 2 of 7 tickers still have current_revenue_usd_m = 0 in DCF inputs: TSM, ALAB (ASML now populated)
- ASML gap closed this session
- TSM DCF remains null — needs financial data; next after MU event queue item resolves
- MRVL earnings May 27 in 5 days — will trigger event-driven session
- Samsung union vote May 22-27 ongoing — outcome will determine MU thesis bearing

## [2026-05-22 12:00 UTC] session-4

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: ANET — event-driven (price move +3.86% on May 21, NVDA AI networking read-through)
Notable: ANET Q1 2026 GAAP operating margin expanded to 42.7% (from FY2025 average 32.7%), confirming operating leverage on EOS software is materializing faster than modeled. DCF first run: IV $126.94 vs. $146.44 → MoS -13.3% → SELL/AVOID (medium uncertainty). The -13.3% is the mildest overvaluation in the portfolio — at WACC ~8% and 20% CAGR, IV reaches $227. Separately, hyperscaler CapEx $725B combined in 2026 (+77% YoY) confirmed, with Meta raising to $125-145B and Microsoft at $190B — the strongest possible demand confirmation for AI networking. MU +4.76% on May 22 (first regular session post-NVDA earnings) added to event queue for Session 5. Taiwan: PLA exercises ongoing; Trump warned against formal independence declaration; Lai reiterated sovereignty; risk elevated but stable.
Price movers >3% (new, May 22): MU +4.76% (added to event_queue)
No significant news: TSM (+1.37%), ASML (~flat), NVDA (-1.77% profit-taking), MRVL (~flat, pre-earnings volatility), ALAB (~flat)
DCF run: ANET — IV $126.94, MoS -13.3%, Rec: SELL/AVOID (medium uncertainty; GAAP EBIT basis)

Entity updates:
- ANET.md: 2026-05-22 entry added — Q1 2026 GAAP operating margin 42.7% confirmed; hyperscaler CapEx $725B validated; NVDA profit-taking context; analyst consensus $181-188 noted. Last updated timestamp refreshed.
- ANET.json: Full TTM financial data populated — revenue $9,700M, EBIT $3,400M, cash $12,353M (no debt), equity $13,487M, shares 1,259M, R&D $1,237M with 5-year history. Story narrative updated for Q1 2026 data.
- dashboard.md: Session 4 prices updated; MU $762.10 (+4.76%⚑) flagged; ANET market cap corrected to ~$184B; MRVL updated to $175.64; NVDA $219.51 (-1.77%); Samsung union vote updated to ONGOING; Barclays $195 and Rosenblatt $210 ANET targets added.
- tracker.md: ANET row populated with IV $126.94 / MoS -13.3% / SELL/AVOID; MU/NVDA/MRVL prices updated; Session 4 note appended; Session History row added.
- state/session.json: session_count 3→4; ANET removed from event_queue; MU added to event_queue (+4.76%); next_deep_session updated to ASML; dcf_last_run.ANET = 2026-05-22; last_run_utc updated.

Lint findings:
- 3 of 7 tickers still have current_revenue_usd_m = 0 in DCF inputs: TSM, ASML, ALAB
- ASML next in event queue — Q1 2026 beat (€8.8B revenue) provides financial data for DCF; should run in Session 5
- TSM DCF remains null; schema exists but no financial data populated yet; after ASML processes in event queue, TSM is next in rotation
- MRVL earnings May 27 will trigger event-driven session (earnings QN release); 5 days out
- MU Samsung union vote outcome pending (May 22-27) — if union ratifies deal, bear risk removed; if rejected, strike resumes and MU HBM supply-side thesis strengthens further
- ALAB still stub — no financial data, no DCF; low priority relative to event-driven queue

---

## [2026-05-22 06:00 UTC] session-3

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: MRVL — event-driven (price move +4.34%, NVIDIA $2B strategic investment, analyst target surge)
Notable: Citi raised MRVL price target from $118 to $215 (nearly doubled), joining Melius $220, B. Riley $205, RBC $200, Oppenheimer $200, Wells Fargo $195 — six sell-side firms now have $195–$220 targets ahead of May 27 Q1 FY2027 earnings. MRVL DCF first run: IV $119.91 vs. $177.95 current → MoS -32.6% → SELL/AVOID. GAAP EBIT base is deeply negative (-$720M) from non-cash acquisition amortization; true economic IV likely higher. Separately, NVDA Q1 FY2027 $81.6B revenue (+85% YoY) with $91B Q2 guidance confirmed AI buildout acceleration; hyperscaler CapEx 2026 tracking $600-725B; DRAM contract prices +58-63% QoQ Q2 2026 (MU thesis confirmation). Taiwan: PLA exercises ongoing; Taiwan defense budget NT$780B passed; Xi-Trump (May 13-15) no major Taiwan agreements reached.
No significant news: TSM (+1.37%), NVDA (+1.89%), ASML (~flat), ALAB (~flat), ANET (~+1.2%)
DCF run: MRVL — IV $119.91, MoS -32.6%, Rec: SELL/AVOID (high uncertainty; GAAP EBIT basis)

Entity updates:
- MRVL.md: Financials section populated (FY2026 $8.195B revenue, $-720M GAAP operating income, 35% non-GAAP margin, balance sheet). Growth Drivers, Risks, and Active/Archived Catalysts sections populated. Recent Updates 2026-05-22 added (Citi $215 upgrade, FY2026 results confirmed, pre-earnings positioning)
- MRVL.json: Full financial data populated from FY2026 actuals — revenue $8,195M, EBIT -$720M, CapEx $354M, D&A $374M, cash $2,639M, debt $4,471M, equity $14,308M, shares 874M, R&D $2,075M with 4-year history
- dashboard.md: All 7 prices updated for May 22; Citi $215 MRVL target added; Oppenheimer $200 and Wells Fargo $195 MRVL targets added
- tracker.md: MRVL row populated with IV $119.91 / MoS -32.6% / SELL/AVOID; MU/NVDA prices updated; Session 3 note appended
- state/session.json: session_count 2→3; MRVL removed from event_queue; dcf_last_run.MRVL = 2026-05-22; last_run_utc updated

Lint findings:
- 4 of 7 tickers still have revenue = 0 in DCF inputs: TSM, ASML, ANET, ALAB
- Next priority in event queue: ANET (then ASML) — both with confirmed >3% price moves and strong fundamental news
- No stale catalysts (Samsung vote May 22-27 ongoing; MRVL earnings May 27 approaching; TSM monthly revenue ~June 8)
- No broken cross-links identified in MRVL entity page

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

## [2026-05-23 16:00 UTC] session-10

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: TSM — dcf_never_run (10 consecutive sessions overdue)
Notable: First TSM DCF ever — IV $384.28 (-5.6% MoS, HOLD); TSMC's actual margins (50.8% FY2025, 58.1% Q1 2026) already exceed the model's 42% target, making HOLD potentially conservative; TSM is the only non-SELL/AVOID position in the portfolio.
No significant news: ANET, ALAB (prices flat; no material developments beyond prior sessions)
DCF run: TSM — IV $384.28, MoS -5.6%, Rec: HOLD
Concept pages updated: cowos (TSM Q1 2026 margin expansion + 2026 CapEx guide)
Podcast: none (gate met, no episodes found)
Watchlist: none
