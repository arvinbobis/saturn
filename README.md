# Saturn — AI Supply Chain Satellite Portfolio Wiki

A compounding knowledge base for six companies that are structural choke points in the AI/semiconductor supply chain.

## Portfolio Thesis

Hyperscalers (Amazon, Microsoft, Google, Meta) are spending **$725B+ in 2026 CapEx**, the majority directed at AI infrastructure. The companies that sit at unavoidable bottlenecks in this supply chain — foundry, memory, lithography, custom silicon, networking — get paid on the buildout regardless of which AI application wins at the top of the stack.

This wiki tracks six satellite picks held alongside a 70% IUSG core position (S&P 900 Growth, ~8% annual return). The satellite portfolio targets 15%+ CAGR over 15–20 years through deep, compounding research on each position.

## The Six Picks

| Ticker | Company | Why It's Here |
|---|---|---|
| **TSM** | Taiwan Semiconductor | Pure-play foundry; sole manufacturer of every leading-edge AI chip; CoWoS packaging monopoly |
| **MU** | Micron Technology | Only US DRAM manufacturer; HBM3E design win for NVIDIA Blackwell; thesis on HBM breaking the commodity cycle |
| **ASML** | ASML Holding | Sole supplier of EUV lithography — no EUV, no leading-edge chips; upstream of the entire supply chain |
| **NVDA** | NVIDIA | Dominant AI training GPU; CUDA ecosystem moat; $1T+ combined Blackwell/Vera Rubin order book |
| **MRVL** | Marvell Technology | Custom ASIC co-design for hyperscalers (Google TPU, Amazon Trainium, Microsoft Maia) |
| **ANET** | Arista Networks | AI data center networking; 400G/800G ethernet for GPU clusters |
| **ALAB** | Astera Labs | High-speed connectivity chips (PCIe/CXL retimers) for AI GPU clusters; top Atreides holding |

## Wiki Structure

```
saturn/
  README.md                   ← this file
  CLAUDE.md                   ← agent instructions
  index.md                    ← master catalog of all pages
  log.md                      ← append-only daily scan log
  entities/                   ← one file per company
  concepts/                   ← HBM, CoWoS, DRAM cycle, custom silicon
  institutional/
    tracker.md                ← smart money positions and entry prices
  prices/
    dashboard.md              ← daily price snapshot
  valuation/
    dcf_model.py              ← Damodaran FCFF model (Python)
    inputs/                   ← per-ticker DCF input JSON files
    outputs/                  ← per-ticker DCF results markdown
  schemas/                    ← hyperfocused research schemas (TSM, MU)
  sources/raw/                ← drop source documents here for ingestion
```

## How It Works

A remote Claude agent runs daily at 9am Manila time, scanning for news on all seven tickers, updating entity pages, and pushing commits. The log.md captures every scan. The institutional/ and prices/ directories give a point-in-time view of smart money positioning and current valuations.

Quarterly: pull 10Y financials from Wisesheets, run the DCF model, update the Investment View and Decision Log sections in each entity page.

## Key Links

- [Daily log](log.md) — what the agent found each day
- [Institutional tracker](institutional/tracker.md) — where smart money entered
- [Price dashboard](prices/dashboard.md) — current prices vs. institutional entries
- [Index](index.md) — full catalog of all wiki pages
