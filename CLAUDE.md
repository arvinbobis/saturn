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

Each entity has a hyperfocused schema in `/schemas/`. **Always read the schema before a deep session on that ticker.**

- `/schemas/claude-tsm.md` — TSMC. CoWoS, node roadmap, geopolitical risk framing.
- `/schemas/claude-micron.md` — Micron. DRAM cycle mechanics, HBM thesis, CXMT threat.
- `/schemas/claude-asml.md` — ASML. EUV monopoly, High NA timeline, China risk, TSMC as leading indicator.
- `/schemas/claude-nvda.md` — NVIDIA. CUDA moat, Blackwell/Rubin roadmap, hyperscaler dependency.
- `/schemas/claude-mrvl.md` — Marvell. Custom ASIC programs (Google TPU, Amazon Trainium), GAAP vs non-GAAP.
- `/schemas/claude-anet.md` — Arista. EOS switching costs, port speed upgrade cycle, NVDA competitive overhang.
- `/schemas/claude-alab.md` — Astera Labs. Aries/Leo products, CXL memory pooling thesis, Atreides conviction.

---

## 4-Hour Session Structure

Each session runs through these phases in order. Stop immediately at any point if the usage limit is hit.

---

### Phase 1 — Quick Pulse (all 7 tickers, every session)

**Run at the start of every session, no exceptions.**

For each of TSM, MU, ASML, NVDA, MRVL, ANET, ALAB:
1. Search for current price and 1-day % change
2. Check for any news in the last 24 hours

**Also check:**
- Hyperscaler CapEx news: Amazon, Microsoft, Google, Meta
- Taiwan Strait developments (affects TSM, ASML)
- TrendForce DRAM pricing update (affects MU)
- TSMC monthly revenue (released ~8th–10th each month at pr.tsmc.com)

**Update `dashboard.md`:** Edit the **Price** and **1D%** columns for all 7 rows in the Portfolio Snapshot table.

**Event queue management — run in this order:**

1. **Null DCF check:** For each ticker where `dcf_last_run` is null in `state/session.json`, if that ticker is not already in `event_queue`, INSERT it at position 0:
   ```json
   {"ticker": "[TICKER]", "event": "dcf_never_run — first DCF needed", "detected": "[today]"}
   ```
   This ensures no ticker is permanently deferred by event volume. TSM must not remain null indefinitely.

2. **Price move check:** If any ticker moved >3%: add to event_queue with reason.

3. **Earnings check:** If any earnings were released: add to event_queue with `"event": "earnings QN-YYYY"`.

---

### Phase 2 — Deep Session (1–2 tickers)

**Session selection logic:**

- FIRST: if `event_queue` is non-empty, take the first item
- ELSE: use `next_deep_session` from `state/session.json` (rotation: TSM → MU → ASML → NVDA → MRVL → ANET → ALAB → TSM)

**For the selected ticker:**

1. Read the entity page (`entities/[TICKER].md`)
2. **Read the schema** (`schemas/claude-[ticker].md`) — every ticker now has one
3. Search for news since the last entity update date
4. For each material development, append to `entities/[TICKER].md` under `## Recent Updates`:

```markdown
### YYYY-MM-DD

**[Topic]:** [What happened]. Source: [outlet, date]. *Thesis bearing: [Confirms / Challenges / Neutral] — [one sentence why]*
```

5. If earnings reported: update the Financials tables in the entity page
6. If new analyst price target: add to `dashboard.md` Analyst Price Targets section

**Thesis bearing is required on every update.**

**Concept page propagation — after each entity update:**

For each material update added, check if it relates to any of these concepts and update the relevant file:

| If update touches... | Update this concept page |
|---|---|
| HBM, high bandwidth memory, memory stacking, HBM ASP | `concepts/HBM.md` |
| CoWoS, advanced packaging, TSMC packaging | `concepts/cowos.md` |
| Custom silicon, hyperscaler ASICs, co-design, TPU, Trainium | `concepts/custom-silicon.md` |
| DRAM pricing, DRAM cycle, memory trough/peak, TrendForce | `concepts/dram-cycle.md` |

Append to the concept page:

```markdown
### YYYY-MM-DD — [TICKER]

**[Key fact or data point]** — [one sentence on why this matters for the concept's standing knowledge]
```

This is how the wiki compounds across entities, not just within them.

**After deep session:** Advance rotation in `state/session.json`:
- Update `next_deep_session` to the next ticker in rotation order
- Remove processed event from `event_queue` if applicable
- Set `last_deep_session` to the ticker just completed

---

### Phase 3 — Stories → Numbers + DCF

**Run for the Phase 2 ticker IF any of these apply:**
- Earnings just processed (new financial data available)
- `dcf_last_run` for this ticker is null or >30 days ago
- A material thesis-changing event occurred

**Steps:**

1. **Synthesize the story** — read the entity page's Recent Updates. What is the current narrative? 2–3 sentences.

2. **Update assumptions** — open `valuation/inputs/[TICKER].json`. Update `story_narrative` and all `story_*` justification fields to reflect current wiki state. The DCF number is only as good as the story backing it.

3. **Search for financial inputs** — search the web for TTM (trailing twelve months) financials:
   - Revenue, EBIT / Operating Income, CapEx, D&A
   - Change in Working Capital
   - Book value of debt and equity
   - Cash and equivalents, shares outstanding
   - Current stock price
   - R&D expense (current year + 3–5 years of history for `rd_history_usd_m`)

   Update the JSON file with these values.

4. **Run the model:**
   ```
   python3 valuation/dcf_model.py [TICKER]
   ```
   Output goes to `valuation/outputs/[TICKER]-dcf.md`

5. **Update `state/session.json`:** set `dcf_last_run.[TICKER]` to today's date.

**If revenue is 0 in the JSON after your search (data unavailable), skip the DCF run and note the gap.**

---

### Phase 4 — Update dashboard.md (low-frequency columns)

After Phase 3, edit `dashboard.md` Portfolio Snapshot table — update these columns for the ticker that had a DCF run:

| Column | Frequency | Source |
|--------|-----------|--------|
| Price | Every session (Phase 1) | Live price search |
| 1D% | Every session (Phase 1) | Live price search |
| IV | On DCF run only | `valuation/outputs/[TICKER]-dcf.md` |
| MoS | On DCF run only | (IV − Price) / Price × 100 |
| Rec | On DCF run only | DCF recommendation() output |
| Story | On DCF run only | Distilled from `story_narrative` in JSON |
| Last DCF | On DCF run only | Today's date |

**Carry forward** IV/MoS/Rec/Story/Last DCF from prior sessions for tickers not run this session. Never blank a cell that has data.

Append a new `### Session N` note under `## Session Notes` with:
- Ticker(s) reviewed and trigger reason
- Most significant news finding
- Whether any recommendation changed
- Any concept pages updated

Append one line to `## Session History` table.

Update `dashboard.md` header: Last updated date and Session #.

---

### Phase 5 — Lint & Remediate

**This phase fixes problems, not just flags them.** 5–10 minutes max.

**1. Null DCF remediation:**
Check `state/session.json` dcf_last_run. For any ticker where it is null:
- Verify the ticker is already in event_queue (the Phase 1 null check should have added it)
- If not, add it now

**2. Zero-revenue remediation:**
For any ticker where `valuation/inputs/[TICKER].json` has `current_revenue_usd_m: 0`:
- Search the web for that ticker's most recent annual revenue figure
- If found in under 2 searches: populate the JSON and add a note. This is a quick fix, not a full DCF session.
- If not found: note the gap and ensure the ticker is in event_queue for a full financial data session

**3. Stale catalyst cleanup:**
Check `dashboard.md` Upcoming Catalysts. For any catalyst whose date has passed:
- Remove the row
- Add a one-line outcome note to the session notes (e.g., "MRVL May 27 earnings: revenue $X.XB, guide $Y.YB, stock moved Z%")

**4. Concept page staleness check:**
For each concept page (`HBM.md`, `cowos.md`, `dram-cycle.md`, `custom-silicon.md`):
- Check the last dated entry
- If >14 days since last update AND material developments have occurred in related entity pages: add a catch-up entry from memory of this session's Phase 1/2 findings

**5. Cross-link audit:**
Scan entity pages for `[[concept]]` or `[[TICKER]]` references. Verify the target file exists. Flag broken links in the session note — do not silently ignore them.

---

### Phase 6 — Commit & Stop

**Only commit if there is material content to save.**

Material = entity page updated, DCF run, dashboard.md changed, JSON populated, concept page updated.

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

**Update `state/session.json`:**
- Set `last_run_utc` to current UTC timestamp
- Increment `session_count`
- Update `next_deep_session` if rotation advanced

**Append to `log.md`:**

```markdown
## [YYYY-MM-DD HH:MM UTC] session-N

Tickers scanned: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Deep session: [TICKER] — [event-driven reason or "rotation"]
Notable: [1–2 sentences on the single most significant finding]
No significant news: [list tickers]
DCF run: [TICKER or "none"] — IV $X.XX, MoS +/-X%, Rec: [BUY/WAIT/HOLD/SELL]
Concept pages updated: [list or "none"]
```

Then stop. The session is complete.

---

## Entity Page Update Format

Append under `## Recent Updates` with today's date as a sub-heading:

```markdown
### YYYY-MM-DD

**[Topic]:** [What happened]. Source: [outlet, date]. *Thesis bearing: [Confirms / Challenges / Neutral] — [one sentence why]*
```

**Also update structured sections when new data is available:**
- Earnings reported → update Financials tables
- HBM market share data → update HBM Market Share table in MU.md
- Catalyst played out → move from Active to Archived with outcome
- New analyst price target → add to `dashboard.md` Analyst Price Targets section

**Thesis bearing is required on every update.**

---

## Conventions

- **Dates:** YYYY-MM-DD everywhere. Quarterly labels: 2026-Q1, 2026-Q2, etc.
- **Cross-links:** `[[TICKER]]` or `[[concept-name]]` for internal references
- **Currency:** USD throughout (convert EUR/TWD/JPY at prevailing rate, note the rate)
- **Thesis bearing:** every news update must have one — Confirms / Challenges / Neutral + one sentence why
- **Sources:** cite outlet and date inline with every data point
- **Decision Log:** append-only in each entity page. Never edit past entries.
- **Usage limits:** If you hit any API rate limit or usage constraint, stop immediately. Do not retry.
