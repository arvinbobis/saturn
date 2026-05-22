# Saturn — Satellite Portfolio Wiki

A compounding knowledge base for seven AI/semiconductor supply chain companies held as satellite positions in a long-term retirement portfolio.

---

## ⚠ Usage Limit Policy

**If you hit the Claude Pro usage limit at ANY point — STOP immediately.**

Do not retry. Do not start a new search. Do not attempt to commit. Close out cleanly (save any in-progress JSON edits if possible) and exit. The session auto-resumes in the next 4-hour window. Burning tokens past the limit costs real money with no benefit.

---

## Portfolio Context

- **System name:** SATURN (SATellite retURN)
- **Goal:** Identify and hold companies that are choke points in the AI/semiconductor supply chain — companies that get paid on the buildout regardless of which application wins at the top of the stack.
- **Satellite picks:** TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
- **Decision frequency:** Every 4 hours (agent-driven). Quarterly manual review by portfolio holder.
- **Investment horizon:** 5–8 years to double (~9–15% CAGR); 10+ year durability required
- **Companion:** This portfolio runs alongside a 70% IUSG core position (passive S&P 900 Growth, ~8% annual return target)
- **Savings rate:** ~PHP 80,000/month (~USD 1,333 at 60 PHP/USD)

---

## Schemas

Each primary entity has a hyperfocused schema file in `/schemas/`. Read the relevant schema before deep work on TSM or MU:

- `/schemas/claude-tsm.md` — TSMC (TSM). Standing knowledge, moat analysis, CoWoS/node roadmap, geopolitical risk framing.
- `/schemas/claude-micron.md` — Micron (MU). DRAM cycle mechanics, HBM thesis, CXMT threat, cycle-normalized financials.

*(ASML, NVDA, MRVL, ANET, ALAB schemas pending — use entity pages and DCF inputs as standing knowledge.)*

---

## 4-Hour Session Structure

Each session runs through these phases in order. Stop immediately at any point if the usage limit is hit.

---

### Phase 1 — Quick Pulse (all 7 tickers, ~5–10 min)

**Run at the start of every session, no exceptions.**

For each of TSM, MU, ASML, NVDA, MRVL, ANET, ALAB:
1. Search for current price and 1-day % change
2. Check for any news in the last 24 hours

**Outcomes from Phase 1:**
- Update the **Price** and **1D%** columns in `dashboard.md` for all 7 tickers
- If any ticker moved >3% in either direction: flag it and add to `state/session.json` event_queue with reason
- If any earnings were released: add to event_queue with `"event": "earnings QN-YYYY"`

**Also check at Phase 1:**
- Hyperscaler CapEx news: Amazon, Microsoft, Google, Meta
- Taiwan Strait developments (affects TSM, ASML)
- TrendForce DRAM pricing update (affects MU)
- TSMC monthly revenue (released ~8th–10th each month at pr.tsmc.com)

---

### Phase 2 — Deep Session (1–2 tickers)

**Session selection logic (in priority order):**

1. **Event-driven:** If `state/session.json` has items in `event_queue`, take the first one.
   - Earnings released → deep earnings analysis session
   - Price move >3% → investigate cause, update thesis bearing
2. **Rotation:** If event_queue is empty, take `next_deep_session` from `state/session.json`.
   - After completing, advance rotation: update `next_deep_session` to the next ticker in `rotation_order`

**What to do in a Deep Session:**

For the selected ticker:
1. Read the entity page (`entities/[TICKER].md`)
2. Read the relevant schema if one exists (TSM, MU)
3. Search for news since the last entity update
4. For each material development, append to `## Recent Updates` in the entity page:

```markdown
### YYYY-MM-DD

**[Topic]:** [What happened]. Source: [outlet, date]. *Thesis bearing: [Confirms / Challenges / Neutral] — [one sentence why]*
```

5. If earnings: update the Financials tables in the entity page
6. If new analyst price target: add to `dashboard.md` Analyst Price Targets section

**Thesis bearing is required on every update.**

---

### Phase 3 — Stories → Numbers + DCF

**Trigger:** Run for the ticker from Phase 2 IF any of these are true:
- Earnings were just processed (new financial data available)
- The last DCF run was >30 days ago (check `state/session.json` dcf_last_run)
- A material thesis-changing event occurred

**Steps:**

1. **Synthesize the story** — read the entity page's Recent Updates section. What is the current narrative? Write it in 2–3 sentences.

2. **Derive assumptions from the story** — open `valuation/inputs/[TICKER].json`. Review the `story_narrative` and `story_*` justification fields. Update them to reflect the current wiki state. The DCF number is only as good as the story backing it.

3. **Search for financial inputs** — search the web for TTM financials:
   - Revenue (TTM or most recent fiscal year)
   - EBIT / Operating Income
   - CapEx and D&A
   - Change in Working Capital
   - Book value of debt and equity
   - Cash and equivalents
   - Shares outstanding
   - Current stock price
   - R&D expense (last 3–5 years for rd_history_usd_m)
   Update the JSON file with these values.

4. **Run the DCF model:**
   ```
   python3 valuation/dcf_model.py [TICKER]
   ```
   Output goes to `valuation/outputs/[TICKER]-dcf.md`

5. **Update `state/session.json`** — set `dcf_last_run.[TICKER]` to today's date.

**If revenue is 0 in the JSON, the model skips gracefully — don't force a run without real data.**

---

### Phase 4 — Update dashboard.md (low-frequency columns)

After Phase 3 (or whenever a new DCF output exists), update the **IV, MoS, Rec, Story, Last DCF** columns in `dashboard.md` for the ticker that was run. Also update the Upcoming Catalysts section if any have resolved.

| Column | Frequency | Source |
|--------|-----------|--------|
| Price | Every session (Phase 1) | Live price search |
| 1D% | Every session (Phase 1) | Live price search |
| IV | On DCF run only | `valuation/outputs/[TICKER]-dcf.md` |
| MoS | On DCF run only | (IV − Price) / Price × 100 |
| Rec | On DCF run only | DCF recommendation() logic |
| Story | On DCF run only | Distilled from story_narrative in JSON |
| Last DCF | On DCF run only | Date from state/session.json dcf_last_run |

**Carry forward** IV/MoS/Rec/Story/Last DCF from prior sessions for tickers not run this session. Never blank out a cell that has data.

Append a session note under `## Session Notes` as a new `### Session N` heading. Include:
- Ticker(s) reviewed in depth and trigger reason
- Most significant news finding
- Whether any recommendation changed

Also append one line to `## Session History`.

---

### Phase 5 — Lint & Link

Quick scan for quality gaps (5 min max):

1. **Missing data audit:** For each ticker, check if any entity page section is empty or says "pending." Flag the most critical gap in the session note.
2. **Broken cross-links:** Scan entity pages for `[[concept]]` links. Verify the concept exists in `/concepts/`. Flag broken links.
3. **Stale catalysts:** Check `dashboard.md` Upcoming Catalysts. Remove any catalysts whose date has passed. Note outcome.
4. **DCF health check:** If any ticker has `current_revenue_usd_m: 0` in its JSON and the last DCF run is null, flag it as "needs financial data" in the session note.

---

### Phase 6 — Commit & Stop

**Only commit if there is material content to save.**

Material = any of: entity page updated, DCF model run, dashboard.md changed, financial data added to JSON, price data updated.

If prices moved <2% and no news found and no DCF run: skip commit.

```
git config user.email "saturn-agent@noreply.com"
git config user.name "Saturn Agent"
git remote set-url origin https://arvinbobis:${GITHUB_PAT}@github.com/arvinbobis/saturn
git add -A
git commit -m "scan: YYYY-MM-DD HH:MM UTC — [ticker] deep session"
git push
```

If git push fails: print the error and stop. Do not retry.

**After commit (or skip): update `state/session.json`:**
- Set `last_run_utc` to current UTC timestamp
- Increment `session_count`
- Update `next_deep_session` if rotation advanced

Then stop. The session is complete.

---

## Entity Page Update Format

Append under `## Recent Updates` with today's date as a sub-heading:

```markdown
### YYYY-MM-DD

**[Topic]:** [What happened]. Source: [outlet, date]. *Thesis bearing: [Confirms / Challenges / Neutral] — [one sentence why]*
```

**Also update structured sections when new data is available:**
- If earnings were reported: update the Financials tables in the entity page
- If HBM market share data is available: update the HBM Market Share table in MU.md
- If a catalyst has played out: move it from Active to Archived Catalysts with the outcome noted
- If a new analyst price target was issued: add it to `dashboard.md` Analyst Price Targets section

**Thesis bearing is required** on every update — always state whether the development Confirms, Challenges, or is Neutral to the investment thesis, and why in one sentence.

---

## Log Format

Append to `log.md` at the end of each session:

```markdown
## [YYYY-MM-DD HH:MM UTC] session-N

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: [TICKER] — [event-driven reason or "rotation"]
Notable: [1–2 sentences on the single most significant finding]
No significant news: [list tickers with nothing notable]
DCF run: [TICKER] — IV $X.XX, MoS +/-X%, Rec: [BUY/WAIT/HOLD/SELL]

Entity updates:
- [TICKER]: [one-line summary of what was updated]
```

---

## Conventions

- **Dates:** YYYY-MM-DD everywhere. Quarterly labels: 2026-Q1, 2026-Q2, etc.
- **Cross-links:** `[[TICKER]]` or `[[concept-name]]` for internal references
- **Currency:** USD throughout (convert EUR/TWD/JPY at prevailing rate, note the rate)
- **Thesis bearing:** every news update must have one — Confirms / Challenges / Neutral + one sentence why
- **Sources:** cite outlet and date inline with every data point
- **Decision Log:** append-only in each entity page. Never edit past entries.
- **Usage limits:** If you hit any API rate limit or usage constraint, stop immediately. Do not retry.
