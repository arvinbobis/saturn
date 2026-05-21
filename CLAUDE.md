# Saturn — Satellite Portfolio Wiki

A compounding knowledge base for seven AI/semiconductor supply chain companies held as satellite positions in a long-term retirement portfolio.

## Portfolio Context

- **Goal:** Identify and hold companies that are choke points in the AI/semiconductor supply chain — companies that get paid on the buildout regardless of which application wins at the top of the stack.
- **Satellite picks:** TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
- **Decision frequency:** Quarterly — review each entity's Monitoring Checklist, update models, record buy / hold / sell
- **Investment horizon:** 5–8 years to double (~9–15% CAGR); 10+ year durability required
- **Companion:** This portfolio runs alongside a 70% IUSG core position (passive S&P 900 Growth, ~8% annual return target)

## Schemas

Each primary entity has a hyperfocused schema file in `/schemas/`. Read the relevant schema before working on TSM or MU:

- `/schemas/claude-tsm.md` — TSMC (TSM). Standing knowledge, moat analysis, CoWoS/node roadmap, geopolitical risk framing.
- `/schemas/claude-micron.md` — Micron (MU). DRAM cycle mechanics, HBM thesis, CXMT threat, cycle-normalized financials.

## Daily Scan — Agent Instructions

When running the daily scan, work through these steps in order:

---

### Step 1 — Update prices/dashboard.md

Search for current prices for all seven tickers: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB.

Update the `prices/dashboard.md` table with:
- Current price
- 1-day % change
- Any notable price moves (>3% in either direction get a note)

Also update the "Upcoming Catalysts" section — remove any catalysts that have passed and add any newly announced events within 30 days.

---

### Step 2 — Scan for news (last 24–48 hours) for each stock

Search for `[TICKER] news`, `[COMPANY] stock news`, and relevant supply chain/industry developments.

For each stock find:
- Major company news or announcements
- Earnings releases or guidance updates
- Analyst rating or price target changes
- Industry developments affecting the thesis

Also check:
- **TSMC monthly revenue** (released ~8th–10th each month at pr.tsmc.com)
- **Samsung HBM quality/qualification updates** (critical for MU thesis)
- **Hyperscaler CapEx news:** Amazon, Microsoft, Google, Meta
- **Taiwan Strait geopolitical developments** (affects TSM and ASML)
- **TrendForce DRAM/NAND pricing** (monthly; critical for MU cycle position)

---

### Step 3 — Update entity pages

For each ticker with material news:

**Entity page update format — append under `## Recent Updates` with today's date as a sub-heading:**

```markdown
### YYYY-MM-DD

**[Topic]:** [What happened]. Source: [outlet, date]. *Thesis bearing: [Confirms / Challenges / Neutral] — [one sentence why]*
```

**Also update structured sections when new data is available:**
- If earnings were reported: update the Financials tables in the entity page (Revenue, Gross Margin, Operating Margin, FCF)
- If HBM market share data is available: update the HBM Market Share table in MU.md
- If a catalyst has played out: move it from Active to Archived Catalysts with the outcome noted
- If a new analyst price target was issued: add it to `prices/dashboard.md` Analyst Targets section

**Thesis bearing is required** for every update — always state whether the development Confirms, Challenges, or is Neutral to the investment thesis, and why in one sentence.

---

### Step 4 — Update log.md

Append one entry per scan:

```markdown
## [YYYY-MM-DD] daily-scan

Stocks checked: TSM, MU, ASML, NVDA, MRVL, ANET, ALAB
Notable: [1–2 sentences on the single most significant finding]
No significant news: [list tickers with nothing notable]

Entity updates:
- [TICKER]: [one-line summary of what was updated]
```

---

### Step 5 — Update index.md

Update the "Last Updated" date for any entity page that was modified today.

---

### Step 6 — Run DCF model (Quarterly — when earnings data is fresh)

**Trigger:** Run after any quarterly earnings report for TSM, MU, ASML, NVDA, MRVL, or ANET.

Steps:
1. Read `valuation/inputs/[TICKER].json`
2. Search for the key financial inputs from the most recent earnings: Revenue, EBIT/Operating Income, CapEx, D&A, shares outstanding, current stock price
3. Update the JSON file with the new data
4. Run: `python3 valuation/dcf_model.py [TICKER]`
5. The model outputs to `valuation/outputs/[TICKER]-dcf.md`
6. Append the DCF summary (Intrinsic Value, Current Price, Margin of Safety) to the entity's Investment View section

**Note:** The DCF model requires Python 3. No external packages needed.

---

### Step 7 — Commit and push

Run exactly in this order:
```
git config user.email "saturn-agent@noreply.com"
git config user.name "Saturn Agent"
git remote set-url origin https://arvinbobis:${GITHUB_PAT}@github.com/arvinbobis/saturn
git add -A
git commit -m "scan: YYYY-MM-DD daily update"
git push
```

**Scope:** Only commit when there is something material to update. If no meaningful news was found for any ticker and prices moved less than 2%, skip the commit.

If git push fails, print the error and stop. Do not retry.

---

## Conventions

- **Dates:** YYYY-MM-DD everywhere. Quarterly labels: 2026-Q1, 2026-Q2, etc.
- **Cross-links:** `[[TICKER]]` or `[[concept-name]]` for internal references
- **Currency:** USD throughout
- **Thesis bearing:** every news update must have one — Confirms / Challenges / Neutral + one sentence why
- **Sources:** cite outlet and date inline with every data point
- **Decision Log:** append-only in each entity page. Never edit past entries.
- **Wisesheets data:** note pull date whenever citing financial figures
- **Usage limits:** If you hit any API rate limit or usage constraint, stop immediately. Do not retry.
