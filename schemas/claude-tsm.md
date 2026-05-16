# claude-tsm.md
# Schema: TSMC LLM Wiki

A compounding knowledge base for deep research on Taiwan Semiconductor Manufacturing Company (TSM).  
The wiki is a **learning artifact first** — the investment decision is an output, not the organizing principle.  
Built on the llm-wiki pattern. The LLM writes and maintains the wiki; the human curates sources and asks the right questions.

---

## Investment Mandate

- **Goal:** Determine whether TSM can double in 5–8 years (~9–15% CAGR) and remain competitively viable for 10+ years
- **Decision frequency:** Quarterly — review the Monitoring Checklist, update the model, record a buy / hold / sell
- **Core question:** Can TSMC generate significantly more free cash flow in year 8 than it does today, at a price that gives an acceptable entry point?
- **Data source:** Wisesheets — 10 years of annual and quarterly financial data, used to anchor every assumption in historical reality rather than narrative
- **The FCF inflection thesis:** TSMC's CapEx is peaking in the 2024–2026 period. As N3 and N2 capacity fills with AI demand, revenue grows into the fixed cost base and FCF expands materially. The investment thesis is partly a bet on the timing and magnitude of that inflection.

---

## TSMC Standing Knowledge

*This section is permanent context. Every new LLM session should read this before touching any wiki page. It encodes what is known about TSMC so sessions don't start from zero.*

### What TSMC Is

Taiwan Semiconductor Manufacturing Company is the world's first and largest pure-play foundry — they manufacture chips designed by others and never compete with their customers by designing their own chips. Founded in 1987 by Morris Chang (former Texas Instruments executive). The foundry model was Morris Chang's invention; before TSMC, chip companies had to build and operate their own fabs. TSMC's existence enabled the entire fabless industry: NVIDIA, AMD, Apple Silicon, Qualcomm — none of them exist at their current scale without a trusted foundry.

Headquartered in Hsinchu Science Park, Taiwan. Listed on TWSE (2330) and NYSE ADR (TSM). ~65,000+ employees.

**Critical operational fact:** TSMC reports monthly revenue — unusual for a company of this size. This gives much higher frequency signal than quarterly-only reporters and is a key data advantage in the Monitoring Checklist.

### Business Model

Revenue = wafer starts × ASP per wafer, by node. Higher nodes (N3, N2) command 3–5x the ASP of mature nodes (N28, N16). The business has high operating leverage: fixed costs are large, but once fabs are built and filled, incremental revenue flows through at high margins. CapEx intensity is the key variable — TSMC spends 40–50% of revenue on CapEx during investment cycles, which suppresses FCF during buildout phases.

### Revenue Segments — Know These by Name

**By end market (approximate 2024 mix):**
| Segment | ~% Revenue | Key Customers | Trend |
|---|---|---|---|
| HPC / AI | ~51% | NVIDIA, AMD, Apple M-series, Google TPU, Amazon Trainium, Microsoft Maia, Meta MTIA | Fast growing; overtook smartphone as largest segment in 2023 |
| Smartphone | ~38% | Apple iPhone (A-series), Qualcomm Snapdragon, MediaTek | Slow growth; declining mix |
| IoT | ~6% | Various | Moderate |
| Automotive | ~5% | Renesas, NXP, Infineon (via JASM) | Fast growing from small base; 2–3 year lag from design win to revenue |
| DCE (Digital Consumer Electronics) | ~3% | TV/gaming SoCs | Flat |
| Others | ~1% | — | — |

**By node (approximate 2024 mix):**
| Node | ~% Revenue | Notes |
|---|---|---|
| N3 (3nm) | ~15–20% | Ramping; Apple anchor customer; GAA transition upcoming at N2 |
| N5 (5nm) | ~35% | High volume; most current AI GPUs |
| N7 (7nm) | ~17% | Mature but sustained demand |
| N16 and above | ~30%+ | Specialty, automotive, IoT, mature |

**CoWoS — a separate revenue stream:** CoWoS (Chip on Wafer on Substrate) is TSMC's advanced packaging that physically stacks HBM memory alongside compute dies. Every NVIDIA H100, H200, and Blackwell chip requires CoWoS at TSMC. This is incremental revenue on top of wafer revenue. TSMC's CoWoS capacity was the binding constraint on AI chip supply in 2023–2024. Always track CoWoS separately from wafer revenue.

### Node Roadmap

N3 (2022 production) → N2 (2025 ramp) → A16/N16 (1.6nm, 2026+)

N2 introduces GAA (Gate-All-Around) transistor architecture — a fundamental design shift. Apple is the anchor customer for N2 (A19/M5 chips). NVIDIA and AMD follow. Successful N2 ramp further extends TSMC's lead because Samsung's GAA implementation has had significant execution issues.

### Key Customers — Know the Hierarchy

| Customer | ~% Revenue | Strategic Role |
|---|---|---|
| Apple | ~25% | Anchor customer for every new node. Apple funds node development by committing early volume; TSMC gives Apple first access. The relationship is symbiotic and extremely stable. |
| NVIDIA | ~12–15% | AI-driven, fast-growing. Blackwell on N4/N3 + CoWoS. NVIDIA is effectively supply-constrained by TSMC CoWoS capacity. |
| AMD | ~5–8% | EPYC CPUs (winning vs. Intel) + Instinct MI-series AI GPUs. Gaining share = additive TSMC volume. |
| Qualcomm | ~5% | Snapdragon mobile + edge AI. Moved orders from Samsung back to TSMC — durable share gain. |
| Broadcom | ~3–5% | Custom ASICs for Google, Meta. Benefits from hyperscaler custom silicon trend. |
| MediaTek | ~3–5% | High-volume mid-range smartphone SoCs. |

### Geographic Footprint

| Location | Status | Nodes | Notes |
|---|---|---|---|
| Taiwan (Hsinchu, Tainan) | Primary; most advanced | N3, N2, all leading edge | 90%+ of advanced production. Will remain the leading-edge center for the foreseeable future. |
| Arizona, USA (Fab 21) | Phase 1 in production 2024 | N4 (Phase 1), N3 (Phase 2, ~2028) | CHIPS Act grant ~$6.6B. Apple anchor customer. Costs ~50%+ more per wafer than Taiwan equivalent. |
| Japan (JASM) | Fab 1 in production 2024 | N22/N28 (Fab 1), N6/N7 (Fab 2, ~2027) | Sony, Toyota anchor. Automotive supply chain focus. Japanese government subsidy. |
| Germany (ESMC) | Planned ~2027 | N22/N28 specialty/automotive | Bosch, Infineon, NXP as partners. EU Chips Act. |

**Key implication for margins:** Overseas fabs cost structurally more than Taiwan. As overseas capacity grows from ~5% toward 15–20% of output over the investment horizon, gross margin faces structural headwind. TSMC has been transparent about this. It is real and should be modeled explicitly — do not assume Taiwan-equivalent margins for overseas production.

### Competitive Landscape

| Competitor | Status | Threat Level |
|---|---|---|
| Samsung Foundry | Losing leading-edge share; persistent yield/execution issues. Customers (Qualcomm) have moved back to TSMC. | Low–Medium |
| Intel Foundry (IFS) | Announced as major threat in 2021. Reality: Intel in financial distress, 18A delayed, external wins minimal. | Low (5+ year horizon) |
| SMIC (China) | Cut off from EUV by US/Dutch export controls. Capped at ~N7 equivalent. | None for AI chips; only risk if export controls collapse |

**10-year durability of moat:** The competitive moat is not at risk from Samsung or Intel within the investment horizon — both have structural disadvantages that compound rather than close. The moat's 10-year risk is almost entirely geopolitical, not competitive.

### The Geopolitical Fact

Taiwan is a disputed territory. ~90%+ of the world's most advanced chips are made there. Morris Chang has publicly stated TSMC would be "not operable" under CCP control — the value is in the people and knowledge, not just physical assets. This risk cannot be priced by standard DCF. It is binary and asymmetric. The investment model must treat it as a separate probability-weighted scenario, not a standard risk premium adjustment.

---

## Directory Structure

```
tsmc-wiki/
  claude-tsm.md          ← this file (schema, standing knowledge, conventions, workflows)
  index.md               ← catalog of all wiki pages with one-line summaries
  log.md                 ← append-only record of ingests, queries, reviews
  entities/
    TSM.md               ← TSMC (primary entity — the point of this wiki)
    NVDA.md              ← NVIDIA (key customer and supply chain link)
    AMD.md               ← AMD
    MRVL.md              ← Marvell (custom silicon co-design)
    ASML.md              ← ASML (EUV supplier — leading indicator)
  concepts/
    HBM.md               ← High Bandwidth Memory — supply constraint for AI chips
    cowos.md             ← CoWoS advanced packaging — TSMC's AI packaging monopoly
    custom-silicon.md    ← Hyperscaler custom ASIC trend
    node-roadmap.md      ← N3 → N2 → A16 technology progression
    geopolitical-risk.md ← Taiwan Strait risk — scenarios and probability framing
  sources/
    raw/                 ← immutable source documents (earnings transcripts, articles, reports)
    wisesheets/          ← financial data exports (annual, quarterly)
```

**Rules:**
- TSM.md is the primary entity. All other entities exist to serve understanding of TSM.
- Raw sources are never modified — the LLM reads from them, never writes to them
- The LLM owns `entities/`, `concepts/`, `index.md`, and `log.md` entirely
- Concept pages are created when a topic appears across multiple entity pages and deserves its own treatment

---

## TSM.md — Entity Page Schema

*This is the template and guidance for building and maintaining TSM.md specifically. Sections are in fixed order — do not reorder or skip.*

```markdown
# Taiwan Semiconductor Manufacturing Company (TSM)

> The world's pure-play foundry and the single most critical node in the global AI supply chain —
> every advanced AI chip, regardless of who designed it, is manufactured here.

*Last updated: YYYY-MM-DD | Wisesheets data as of: YYYY-MM-DD*

---

## Overview

- **Business model:** Pure-play foundry — manufactures chips designed by others; never competes
  with customers. Revenue = wafer starts × ASP per wafer, by node. Higher nodes = higher ASP.
- **Value chain position:** Sits between chip designers (fabless companies) and end markets.
  The entire fabless industry (NVIDIA, AMD, Apple, Qualcomm) depends on TSMC.
- **Founded:** 1987 by Morris Chang. The foundry model was his invention.
- **Listed:** TWSE: 2330 / NYSE ADR: TSM
- **Scale:** ~65,000+ employees. Hsinchu HQ. Fabs in Taiwan, Arizona, Japan, Germany.
- **Market cap:** $XX (as of YYYY-MM-DD)
- **Unique data cadence:** TSMC reports monthly revenue — track this between quarterly earnings
  as a leading indicator of demand and mix shift.

## Moat

*Assess each dimension: how strong today, and how durable over 10 years?*

### Technology Lead
TSMC is 1–2 full node generations ahead of Samsung and effectively 3+ ahead of Intel Foundry.
N3 in high volume production; N2 ramping 2025. Document the current lead vs. each competitor
and update quarterly as competitive developments emerge.

### Process Design Kit (PDK) Lock-in
Every chip design is optimized against a specific foundry's PDK. Re-qualifying a chip for a
different foundry takes 2–3 years minimum. The entire fabless ecosystem has been co-designed
with TSMC — this is structural lock-in, not just preference.

### Yield Advantage
TSMC's yields on advanced nodes are industry-leading. A few percentage points of yield advantage
translates to enormous cost differences. This is a compounding advantage — years of process
knowledge cannot be acquired quickly. Document yield commentary from earnings calls.

### CoWoS Packaging Monopoly
No competitor has meaningful CoWoS capacity. This is a separate revenue stream and a separate
moat on top of the wafer manufacturing moat. See [[cowos]] for full treatment.

### Scale Economics
Volume across all nodes gives TSMC equipment utilization and process learning rates no
competitor can match. R&D spend (~$6–8B/year) is spread across the highest revenue base
in the industry.

### 10-Year Moat Durability Assessment
The competitive moat is not at risk from Samsung or Intel within 10 years. Samsung's execution
issues compound; Intel is financially distressed. The moat's 10-year risk is almost entirely
geopolitical, not competitive. See [[geopolitical-risk]] for the Taiwan Strait treatment.
The one credible long-term competitive threat: SMIC acquiring EUV access — currently blocked
by US/Dutch export controls. State probability and track.

## Financials

*All figures from Wisesheets. Always note pull date. Trends matter more than snapshots.*

### Income Statement
| Metric | TTM | 1Y ago | 3Y CAGR | 5Y CAGR |
|---|---|---|---|---|
| Revenue (USD) | | | | |
| Gross Margin % | | | | |
| Operating Margin % | | | | |
| Net Margin % | | | | |

### Cash Flow
| Metric | TTM | 1Y ago | 3Y avg |
|---|---|---|---|
| Operating Cash Flow | | | |
| CapEx (absolute) | | | |
| CapEx as % of Revenue | | | |
| Free Cash Flow | | | |
| FCF Margin % | | | |

### Balance Sheet
| Metric | Latest |
|---|---|
| Cash + Equivalents | |
| Total Debt | |
| Net Cash / (Net Debt) | |

### Capital Efficiency
| Metric | Latest | 3Y avg | 5Y avg |
|---|---|---|---|
| ROIC | | | |
| ROE | | | |

**CapEx Cycle Note:** TSMC's CapEx intensity peaks during node investment phases. The FCF
inflection thesis depends on CapEx tapering after the N2/A16 buildout (expected post-2026)
while revenue continues to grow. Track CapEx as % of revenue quarterly — declining ratio
is the signal that FCF expansion is beginning.

## Revenue Segments

*Update every quarter from earnings. Track both end market and node mix — they tell different stories.*

### By End Market
| Segment | Current % | Prev Quarter % | YoY Growth | Outlook |
|---|---|---|---|---|
| HPC / AI | | | | |
| Smartphone | | | | |
| IoT | | | | |
| Automotive | | | | |
| DCE | | | | |
| Others | | | | |

**HPC/AI subsegment note:** Distinguish between GPU compute (NVIDIA/AMD) and custom silicon
(Google TPU, Amazon Trainium, Microsoft Maia, Meta MTIA). Both are growing but for different
reasons and with different risk profiles. If TSMC breaks this out, track it.

**Automotive note:** Long 2–3 year lag from design win to revenue. JASM (Japan) is the
geographic anchor for automotive. Track design win announcements as a 2–3 year leading
indicator of revenue.

### By Node
| Node | Current % | Prev Quarter % | Notes |
|---|---|---|---|
| N3 (3nm) | | | |
| N5 (5nm) | | | |
| N7 (7nm) | | | |
| N16 and above | | | |

**Node mix significance:** Advanced nodes (N3, N5) command 3–5x the ASP of mature nodes.
Mix shift toward advanced nodes is a revenue and margin tailwind even on flat wafer volumes.
Document ASP commentary from earnings calls — TSMC does not publish ASP directly but
management commentary often gives directional signal.

### CoWoS (Advanced Packaging)
- Current capacity: [update from earnings]
- Utilization: [update from earnings]
- Expansion timeline: [update from earnings]
- Revenue contribution: [if disclosed]

Track CoWoS as a separate line because it is additive revenue on top of wafer manufacturing
and has its own supply constraint dynamic. CoWoS lead times are a leading indicator of
AI chip delivery timelines across the industry.

## Growth Drivers

*For each driver: what it is, magnitude, timeline, probability of materializing.*

### 1. AI Silicon Demand
Every major AI chip — NVIDIA Blackwell, AMD Instinct, Google TPU, Amazon Trainium,
Microsoft Maia, Meta MTIA — is manufactured at TSMC. Hyperscaler combined CapEx is
$320B+ in 2025 and growing. A large portion flows through TSMC regardless of which
hyperscaler wins at the application layer. This is a structural multi-year tailwind,
not a one-cycle event.
*Magnitude: Very high. Timeline: Now through 10Y+. Probability: High.*

### 2. Node Migration ASP Uplift
Each new node generation (N5 → N3 → N2 → A16) carries higher ASP. Revenue grows even
on flat wafer starts as customers migrate to newer nodes. N2 ASP expected materially
higher than N3. Document ASP trend by node as data becomes available.
*Magnitude: High. Timeline: Continuous. Probability: Very high.*

### 3. N2 Ramp (2025–2026)
Apple anchor customer (A19/M5). NVIDIA and AMD will follow for next-generation AI chips.
N2 uses GAA transistor architecture — a fundamental design shift that further extends
the lead over Samsung (whose GAA implementation has had significant execution issues).
Successful N2 ramp = TSMC's lead widens, not just holds.
*Magnitude: High. Timeline: 2025–2027. Probability: High (on track as of last update).*

### 4. CoWoS Capacity Expansion
TSMC is aggressively adding CoWoS capacity. Each capacity addition directly enables
more AI chip shipments. CoWoS revenue is incremental to wafer revenue.
*Magnitude: Medium-High. Timeline: 2024–2027. Probability: High.*

### 5. Automotive Secular Growth
EVs require 5–10x more semiconductors than ICE vehicles. ADAS adds further silicon
content per vehicle. JASM (Japan) is positioned for this market. Long qualification
cycles mean today's design wins become 2026–2030 revenue — well within the
investment horizon.
*Magnitude: Medium. Timeline: 2026–2032. Probability: High.*

### 6. Edge AI / On-Device AI
Apple Intelligence, Qualcomm on-device AI, AI PCs — all require more advanced SoCs,
all manufactured at TSMC. This is a smartphone and PC upgrade cycle catalyst separate
from the data center AI story. Could accelerate iPhone upgrade cycles.
*Magnitude: Medium. Timeline: 2025–2028. Probability: Medium-High.*

### 7. Pricing Power
TSMC raised N3 prices significantly and customers paid. The ability to raise ASP on
leading-edge nodes is a function of being the only viable supplier. Track pricing
commentary each earnings cycle. Pricing power is one of the most important levers
in the revenue model — a 5% ASP increase compounds significantly over 5 years.
*Magnitude: High per unit, moderate in aggregate. Timeline: Continuous. Probability: High.*

## Risks

*For each risk: describe it, assess probability (Low/Medium/High), assess magnitude of impact (1–5). Update when new information changes either dimension.*

### Geopolitical — The Dominant Tail Risk

This is a different category from business risk. It is asymmetric, binary, and not captured
by standard valuation multiples. It must be treated with explicit scenario framing.

| Scenario | Description | Probability | Impact | Portfolio Response |
|---|---|---|---|---|
| Economic coercion | Ongoing political pressure, no operational disruption | Ongoing | Valuation multiple compression | Hold; this is priced in |
| Blockade / exercises | Disrupts shipping lanes and supply chain access; no direct strikes | Low–Medium | Weeks–months production disruption | Trim on escalation signals |
| Targeted strikes | Missile strikes on power grid or fab infrastructure | Low | Months of production loss; global semiconductor shock | Hedge; hard to time |
| Full occupation | CCP military takeover | Very Low | TSMC stated it would be inoperable; near-total loss | Existential; cannot be modeled normally |

**Mitigation:** Arizona, Japan, Germany fabs provide geographic diversification — but only for
mature nodes. N2 and N3 production remains Taiwan-centric for years. The diversification is
real but limited relative to the concentration of risk.

**Key signals to watch:** Taiwan Strait military exercises, US arms sales to Taiwan, PRC
diplomatic posture, export control escalation.

### Competitive Risks
- **Samsung:** Real but losing. Persistent execution issues at leading edge. Share loss trend
  is durable barring a sudden Samsung yield improvement. Probability of meaningful recovery: Low.
- **Intel Foundry:** Announced as major threat in 2021; not credible at leading edge.
  Intel in financial distress. Track Intel quarterly — further deterioration is a TSMC tailwind.
- **SMIC:** Capped by EUV export controls. Only a threat if controls collapse. Track
  US-China export control policy as the leading indicator.

### Operational Risks
- **Overseas fab cost structure:** Arizona fabs cost ~50%+ more per wafer than Taiwan.
  As overseas capacity grows toward 15–20% of output, gross margin faces structural headwind.
  This is known and manageable but must be modeled — do not assume flat margins.
- **CoWoS yield complexity:** A yield setback on advanced packaging would bottleneck
  AI chip supply and damage relationships with NVIDIA and other key customers.
- **Seismic risk:** Taiwan is in an earthquake zone. TSMC has contingency plans but
  this is a real physical risk. Note any major seismic events and TSMC's response.
- **Key person:** C.C. Wei is an excellent successor to Morris Chang. Knowledge
  concentration in a small leadership team is worth noting.

### Financial Risks
- **FX:** Earns primarily in USD, reports in TWD. TWD appreciation = revenue headwind.
  TSMC hedges but imperfectly. Track TWD/USD quarterly.
- **CapEx cycle overshoot:** If AI demand disappoints or hyperscaler spending plateaus,
  TSMC will have over-invested. Customers have committed demand (reducing but not
  eliminating this risk). Watch for guidance revisions downward.
- **Customer concentration:** Apple at ~25% is the primary concentration risk. Apple
  insourcing manufacturing is extremely unlikely but worth noting in a 10-year view.

## Customer Profile

*Update when new data is available from earnings or public disclosures.*

| Customer | ~% Revenue | Node | Strategic Role | Risk |
|---|---|---|---|---|
| Apple | ~25% | N3, N2 (upcoming) | Anchor customer for every new node; funds node development by committing early volume | Extremely low churn risk; deeply symbiotic |
| NVIDIA | ~12–15% | N4/N3 + CoWoS | AI GPU demand; supply-constrained by TSMC CoWoS | Revenue grows with AI CapEx spending |
| AMD | ~5–8% | N3/N5 | Server CPU gains vs Intel + AI GPUs | Growing share = additive TSMC volume |
| Qualcomm | ~5% | N3/N5 | Snapdragon + edge AI | Moved back from Samsung; durable |
| Broadcom | ~3–5% | N3/N5 | Custom ASICs for Google, Meta | Benefits from hyperscaler custom silicon trend |
| MediaTek | ~3–5% | N5/N7 | High-volume mid-range smartphone | Volume-dependent on Android cycle |

**Anchor customer dynamic:** For each new node, identify the anchor customer who commits early
volume and funds the development economics. Apple has been this anchor for N5, N3, and N2.
Who is the anchor for A16? Track this — it determines who funds the next node.

**Pricing power indicator:** When TSMC raises prices, do customers accept? Document each
price increase and customer response. Willingness to pay is the ultimate moat test.

## Catalysts

*Time-bound. Archive played-out catalysts with the outcome noted — they become historical record.*

### Active Catalysts
*(Update each quarter — add new ones, archive completed ones)*

| Catalyst | Expected Timing | Bull Signal | Bear Signal |
|---|---|---|---|
| N2 volume ramp | 2025–2026 | On-schedule ramp with Apple anchor confirmed | Yield delays; ramp pushed out |
| Arizona Fab 21 Phase 2 (N3) | ~2028 | Customer commitments secured; cost structure improving | Cost overruns; customer hesitation |
| CHIPS Act grant receipt | [update] | Full grant received; conditions favorable | Conditions restrict customers or technology |
| CoWoS capacity expansion | Ongoing | Lead times shrinking; capacity ahead of demand | NVIDIA still supply-constrained into 2026+ |
| Intel Foundry deterioration | Ongoing | More customers route to TSMC | Intel stabilizes and competes |

### Archived Catalysts
*(Move here once played out, with outcome)*

## Monitoring Checklist

*Run this checklist every quarter before updating the Investment View and Decision Log.*

### Monthly (between earnings)
- [ ] **TSMC monthly revenue release** — absolute revenue, MoM and YoY growth rate.
  Acceleration = demand strengthening. Deceleration = early warning sign.
  *Where: TSMC investor relations site, published around 10th of each month.*

### Quarterly (earnings cycle)
- [ ] **HPC/AI % of revenue** — the mix shift metric. Should be trending up.
  Any reversal is a significant signal.
- [ ] **Gross margin guidance and actuals** — tracks overseas fab cost absorption.
  Watch for the gap between Taiwan economics and overseas economics widening.
- [ ] **CapEx guidance** — up means demand confidence and customer commitments.
  Revision down is the earliest warning of a demand concern.
- [ ] **N3 utilization, N2 ramp progress** — management typically gives directional
  commentary even without precise numbers.
- [ ] **CoWoS capacity and lead time** — stated in wafers or lead time weeks.
  Shrinking lead times = demand normalizing; still extended = still supply-constrained.
- [ ] **ASP trend commentary** — TSMC doesn't publish ASP directly but management
  language around pricing is consistent. Document the language each quarter.
- [ ] **Overseas fab cost commentary** — any update on Arizona, Japan, Germany cost
  per wafer vs. Taiwan. This is the gross margin headwind to track.

### Leading Indicators (from related companies)
- [ ] **NVIDIA earnings** — data center revenue growth and TSMC supply commentary.
  NVIDIA's forward guidance is a 1–2 quarter leading indicator for TSMC HPC segment.
- [ ] **AMD earnings** — MI-series GPU ramp and EPYC server share.
- [ ] **ASML orders and EUV shipments** — 12–18 month leading indicator of TSMC
  fab investment pace. ASML order book predicts TSMC CapEx direction.
- [ ] **Apple iPhone sell-through data** — impacts smartphone segment 1–2 quarters ahead.
- [ ] **Hyperscaler CapEx guidance** — Amazon, Microsoft, Google, Meta. Up = TSMC demand
  visibility for HPC segment. Any reduction is an early warning.

### Geopolitical
- [ ] **Taiwan Strait developments** — military exercises, US arms sales, PRC statements.
  Escalation signals should trigger a review of the geopolitical scenario probability table.
- [ ] **Export control policy changes** — US/Dutch restrictions on SMIC and advanced chip
  equipment. Tightening = TSMC protected; loosening = SMIC threat emerges.
- [ ] **CHIPS Act implementation** — grant receipt, conditions, any policy changes.

## Investment View

*Synthesizes all sections above into a quantified position. Update every quarter.*
*All models anchored in Wisesheets 10Y annual + quarterly data. Always note data pull date.*

### Valuation
| Metric | Current | 1Y ago | 3Y avg | 5Y avg |
|---|---|---|---|---|
| Price (TSM ADR) | | | | |
| Market Cap | | | | |
| EV | | | | |
| Forward P/E | | | | |
| EV/EBITDA | | | | |
| EV/FCF | | | | |
| P/S | | | | |

**What is the market pricing in?** Use the Reverse DCF (below) to answer this explicitly.
TSMC historically traded at 10–15x forward P/E before the AI demand rerating in 2023.
The question each quarter: is the current multiple justified by the growth trajectory,
or is it pricing in a scenario that is too optimistic or too pessimistic?

### WACC
| Input | Value | Notes |
|---|---|---|
| Risk-free rate | | 10Y US Treasury |
| Beta (5Y monthly) | | Pull from Wisesheets |
| Equity risk premium | | Use Damodaran's published ERP |
| Cost of equity | | Rf + (β × ERP) |
| Cost of debt | | Effective rate on outstanding debt |
| Debt / (Debt + Equity) | | Market value weights |
| Tax rate | | Effective tax rate from financials |
| **WACC** | | |

*Revisit WACC annually or when capital structure or rates change materially.*
*Note: TSMC has historically had a strong net cash position — low financial leverage.*

### DCF
*Build from Wisesheets historical data. The model structure:*

**Revenue projection (5 years):**
- Base revenue from Wisesheets actuals
- Growth rate by segment: HPC/AI vs. Smartphone vs. Automotive vs. Other
- Blended growth rate with mix shift assumptions
- ASP uplift from node migration (document assumption)

**Margin projection:**
- Gross margin: start from current; apply overseas fab cost headwind explicitly
- Operating margin: track operating leverage as revenue grows
- Tax rate: TSMC benefits from R&D tax incentives; document rate assumption

**CapEx projection:**
- Use Wisesheets 10Y CapEx history to anchor the cycle
- Identify CapEx peak year and the post-peak taper
- The FCF inflection is the gap between revenue growth and CapEx tapering

**FCF and terminal value:**
- FCF = Operating Cash Flow − CapEx
- Terminal growth rate assumption (document and justify)
- Terminal value = FCF(year 5) × (1 + g) / (WACC − g)
- Discount all cash flows at WACC → intrinsic value

**Sensitivity table:** Run the model across a range of revenue CAGR (e.g., 10%, 15%, 20%, 25%)
and WACC (e.g., 8%, 10%, 12%) to produce an intrinsic value matrix.

### Reverse DCF
*Start from current stock price. Back out the implied assumptions.*

1. Take current market cap and EV
2. Assume a terminal growth rate and WACC
3. Solve for the FCF growth rate implied by current price
4. Compare that implied growth rate against:
   - TSMC's historical revenue CAGR (from Wisesheets)
   - Your own DCF projection
   - Consensus analyst estimates
5. Answer: **Does the market's implied growth rate seem too conservative, about right, or too optimistic given what the Monitoring Checklist and segment analysis tell you?**

This is the core question each quarter. If the implied growth rate is 12% but AI demand
data suggests 20%+, the stock may be underpriced. If it implies 25% and hyperscaler
CapEx guidance is softening, it may be overpriced.

### Scenarios

| Scenario | Key Assumptions | Revenue 5Y CAGR | Gross Margin (exit) | CapEx Peak | FCF Margin (exit) | Intrinsic Value | IRR at Entry |
|---|---|---|---|---|---|---|---|
| Bull | N2 ramps ahead of schedule; AI demand sustained; overseas fab costs managed | | | | | | |
| Base | N2 on schedule; AI demand continues; overseas cost headwind materializes | | | | | | |
| Bear | N2 delayed; AI CapEx plateaus; overseas costs worse than guided | | | | | | |
| Tail | Taiwan Strait conflict (probability-weighted) | N/A | N/A | N/A | N/A | ~0 | N/A |

*Geopolitical tail scenario: assign a probability to the Tail scenario and compute expected
value as: (probability of no conflict × weighted average of Bull/Base/Bear) + (probability
of conflict × ~0). This probability should appear explicitly in the model.*

### Decision Log

*Append-only. Never edit past entries. This is a permanent record.*

```
### [YYYY-QX] Decision: BUY / ADD / HOLD / TRIM / SELL
- TSM price at decision: $XX (ADR)
- Market cap at decision: $XXB
- Key reasoning: [2–3 sentences — what drove this quarter's decision]
- Monitoring Checklist summary: [what the checklist showed this quarter]
- Model update: [what changed in the DCF/scenarios vs. last quarter]
- What changed since last quarter: [new data, revised assumptions, or reaffirmed conviction]
- What would change this view: [the specific, concrete conditions that flip the decision]
```

## Cross-links

### Related Entities
- [[NVDA]] — TSMC's largest AI customer; NVIDIA's data center growth = TSMC HPC segment growth
- [[AMD]] — GPU and CPU customer; server CPU gains are additive TSMC volume
- [[MRVL]] — Custom ASIC co-design for hyperscalers; hyperscaler silicon orders flow through TSMC
- [[ASML]] — Sole supplier of EUV lithography; ASML order book predicts TSMC CapEx direction

### Related Concepts
- [[cowos]] — TSMC's advanced AI chip packaging; a separate revenue stream and moat
- [[HBM]] — Memory that stacks on AI chips via CoWoS; SK Hynix/Micron supply affects TSMC CoWoS utilization
- [[custom-silicon]] — Hyperscaler trend toward proprietary ASICs; adds second AI demand wave on top of NVIDIA/AMD
- [[node-roadmap]] — N3 → N2 → A16 technology progression; the ASP uplift story
- [[geopolitical-risk]] — Taiwan Strait risk; full scenario and probability treatment

### Key Sources
*(Populate as sources are ingested)*
```

---

## Operations

### Ingest
When a new source is added (TSMC earnings transcript, analyst report, article, Wisesheets export):
1. Read the source in full
2. Note: what is new, what contradicts existing wiki content, what strengthens it
3. Update `entities/TSM.md` — the primary target for almost every TSMC source
4. Update any relevant concept pages (`cowos.md`, `geopolitical-risk.md`, etc.)
5. Update related entity pages if the source contains relevant data (e.g., NVIDIA earnings with TSMC commentary)
6. Update `index.md` if new pages were created
7. Append to `log.md`:
   ```
   ## [YYYY-MM-DD] ingest | [Source Title]
   Pages updated: [list]
   Key changes: [1–2 sentences on what moved]
   Contradictions found: [any claims that conflict with existing wiki content]
   ```

**Priority sources to ingest:**
- TSMC quarterly earnings transcripts (primary)
- TSMC monthly revenue releases (high frequency signal)
- NVIDIA, AMD, Apple earnings (customer demand signal)
- ASML earnings and order data (CapEx leading indicator)
- Wisesheets annual and quarterly pulls (financial model anchor)

### Query
When asked a question against the wiki:
1. Read `index.md` to identify relevant pages
2. Read those pages in full
3. Synthesize an answer with citations to specific wiki sections
4. If the answer is a scenario analysis, comparison, or thesis update — file it back into the
   wiki as an update to the relevant section. Explorations compound in the knowledge base.

### Quarterly Review
Run at the start of each quarter, before updating the Decision Log:
1. Pull latest quarterly financials from Wisesheets (note pull date)
2. Run through the full Monitoring Checklist — document what changed for each item
3. Update `TSM.md` Financials with latest actuals
4. Update Revenue Segments with latest mix data
5. Update Catalysts — archive played-out ones with outcome, add new ones
6. Refresh DCF with updated actuals; update Reverse DCF with current price
7. Update Scenarios if assumptions have changed materially
8. Append a new entry to the Decision Log with full reasoning
9. Log the review in `log.md`:
   ```
   ## [YYYY-MM-DD] quarterly-review | [YYYY-QX]
   Monitoring Checklist: [summary of key findings]
   Model changes: [what changed in the DCF/scenarios]
   Decision: BUY / ADD / HOLD / TRIM / SELL
   ```

### Lint
Run periodically or when the wiki feels stale:
- Check for contradictions between TSM.md sections and concept pages
- Flag financial figures that are older than one quarter — mark for Wisesheets refresh
- Identify catalyst entries that have played out but were not archived
- Check that the Decision Log reflects the most recent quarterly review
- Identify any concept mentioned repeatedly in TSM.md that deserves its own concept page
- Surface data gaps: what would a Wisesheets pull or earnings transcript fill?

---

## Conventions

- **Primary ticker:** TSM (ADR) for price and valuation; 2330.TW for TWSE reference
- **Currency:** USD throughout (convert TWD figures at time of Wisesheets pull; note exchange rate used)
- **Cross-links:** use `[[Ticker]]` or `[[concept-name]]` format for all internal references
- **Dates:** YYYY-MM-DD everywhere. Quarterly labels: 2026-Q1, 2026-Q2, etc.
- **Wisesheets data:** always note the pull date when citing any financial figure — data goes stale
- **Decision Log:** append-only. Past entries are a permanent record. Never edit them.
- **Catalysts:** time-bound. Archive with outcome noted rather than deleting — they become history
- **Node naming:** use TSMC's official nomenclature (N3, N5, N2, A16) not Intel's or Samsung's equivalent labels
- **Numbers:** USD millions or billions consistently within a page; state which at the top

---

## index.md Format

```markdown
# TSMC Wiki Index
Last updated: YYYY-MM-DD

## Entities
- [[TSM]] — TSMC. Primary subject. Pure-play foundry, leading-edge silicon, AI supply chain anchor.
- [[NVDA]] — NVIDIA. Largest AI customer. Data center revenue = TSMC HPC segment signal.
- [[AMD]] — AMD. Server CPU and AI GPU customer. Share gains vs Intel = additive TSMC volume.
- [[MRVL]] — Marvell. Custom ASIC co-design for hyperscalers.
- [[ASML]] — ASML. EUV sole supplier. Order book predicts TSMC CapEx direction.

## Concepts
- [[cowos]] — CoWoS advanced packaging. TSMC's AI chip packaging monopoly and separate revenue stream.
- [[HBM]] — High Bandwidth Memory. Supply constraint for AI GPUs; stacked via CoWoS.
- [[custom-silicon]] — Hyperscaler custom ASICs. Second AI demand wave beyond NVIDIA/AMD.
- [[node-roadmap]] — N3 → N2 → A16 progression. The ASP uplift and competitive lead story.
- [[geopolitical-risk]] — Taiwan Strait scenarios. Probability framing and portfolio impact.

## Sources
- [filename] — [one-line description, date ingested]
```

## log.md Format

```markdown
# TSMC Wiki Log

## [YYYY-MM-DD] ingest | [Source Title]
Pages updated: ...
Key changes: ...
Contradictions found: ...

## [YYYY-MM-DD] query | [Question asked]
Pages read: ...
Filed back into wiki: yes / no — [which page]

## [YYYY-MM-DD] quarterly-review | [YYYY-QX]
Monitoring Checklist summary: ...
Model changes: ...
Decision: ...

## [YYYY-MM-DD] lint
Issues found: ...
Actions taken: ...
Data gaps identified: ...
```
