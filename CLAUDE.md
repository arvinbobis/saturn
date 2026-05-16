# Saturn — Satellite Portfolio Wiki

A compounding knowledge base for six AI/semiconductor supply chain companies held as satellite positions in a long-term retirement portfolio.

## Portfolio Context

- **Goal:** Identify and hold companies that are choke points in the AI/semiconductor supply chain — companies that get paid on the buildout regardless of which application wins at the top of the stack.
- **Satellite picks:** TSM, MU, ASML, NVDA, MRVL, ANET
- **Decision frequency:** Quarterly — review each entity's Monitoring Checklist, update models, record buy / hold / sell
- **Investment horizon:** 5–8 years to double (~9–15% CAGR); 10+ year durability required
- **Companion:** This portfolio runs alongside a 70% IUSG core position (passive S&P 900 Growth, ~8% annual return target)

## Schemas

Each entity has a hyperfocused schema file in `/schemas/`. Read the relevant schema before working on any entity:

- `/schemas/claude-tsm.md` — TSMC (TSM). Standing knowledge, moat analysis, CoWoS/node roadmap, geopolitical risk framing.
- `/schemas/claude-micron.md` — Micron (MU). DRAM cycle mechanics, HBM thesis, CXMT threat, cycle-normalized financials.

Additional schemas will be added as the wiki grows (ASML, NVDA, MRVL, ANET).

## Daily Scan — Agent Instructions

When running the daily scan, for each of the six tickers (TSM, MU, ASML, NVDA, MRVL, ANET):

1. **Search for news from the past 24 hours** — earnings, revenue reports, analyst upgrades/downgrades, product announcements, supply chain developments, geopolitical events
2. **Assess relevance** — is this noise or signal? Only material developments worth tracking
3. **Update the relevant entity page** in `/entities/` — add to the appropriate section (Catalysts, Risks, Financials commentary, or a new dated note at the bottom)
4. **Update `/log.md`** — append one entry per ticker that had a meaningful update
5. **Update `/index.md`** — update "Last updated" date for any page that changed
6. **Commit and push** — one commit per daily scan with message: `scan: YYYY-MM-DD daily update`

**Scope:** Only commit changes when there is something material to report. Do not commit empty or boilerplate updates.

## Conventions

- **Dates:** YYYY-MM-DD everywhere. Quarterly labels: 2026-Q1, 2026-Q2, etc.
- **Cross-links:** `[[TICKER]]` or `[[concept-name]]` for internal references
- **Currency:** USD throughout
- **Sources:** when citing a news item or data point, note the source and date inline
- **Decision Log:** append-only in each entity page. Never edit past entries.
- **Wisesheets data:** note pull date whenever citing financial figures
