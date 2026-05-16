# claude-micron.md
# Schema: Micron Technology LLM Wiki

A compounding knowledge base for deep research on Micron Technology, Inc. (MU).  
The wiki is a **learning artifact first** — the investment decision is an output, not the organizing principle.  
Built on the llm-wiki pattern. The LLM writes and maintains the wiki; the human curates sources and asks the right questions.

---

## Investment Mandate

- **Goal:** Determine whether MU can double in 5–8 years (~9–15% CAGR) and whether HBM has structurally changed the earnings profile enough to justify holding through commodity troughs
- **Decision frequency:** Quarterly — review the Monitoring Checklist, update the model, record a buy / hold / sell
- **Core question:** Has HBM created a permanently higher floor for Micron's earnings through the cycle, or is this a peak-of-cycle story that will revert to commodity economics?
- **Data source:** Wisesheets — 10 years of annual and quarterly financial data, anchoring every assumption in historical cycle reality rather than the current upswing narrative
- **The HBM inflection thesis:** AI training chips require HBM stacked directly on the compute die. HBM pricing is contracted (not spot), supply is constrained by capacity conversion lead times of 12–18 months, and Micron won the NVIDIA Blackwell HBM3E design certification — its first time at the front of an HBM cycle. If HBM becomes a structural portion of Micron's revenue mix, the brutal troughs of 2023 (–$5.8B operating income) may not recur at that magnitude. The thesis is a bet on that structural shift.

---

## Micron Standing Knowledge

*This section is permanent context. Every new LLM session should read this before touching any wiki page. It encodes what is known about Micron so sessions don't start from zero.*

### What Micron Is

Micron Technology is one of only three companies in the world that manufactures DRAM at scale (alongside SK Hynix and Samsung). It is also one of a small number of NAND manufacturers. Founded in 1978 in Boise, Idaho — still headquartered there. Listed on NASDAQ as MU.

Micron is not a fabless company — it designs and manufactures its own memory chips, operating fabs in Idaho, Virginia, Japan (via Elpida acquisition), Singapore, and Taiwan. This is capital-intensive and creates operating leverage: fixed fab costs are large, so revenue swings translate directly into exaggerated margin swings. This is the source of both Micron's opportunity (peak margins are extraordinary) and its risk (trough losses are severe).

**The DRAM oligopoly:** DRAM is manufactured by only three companies at meaningful scale — Samsung (~40% share), SK Hynix (~30%), Micron (~25%). Unlike most commodities, consolidation has been extreme. DRAM manufacturers learned from the 2008–2012 era of irrational capacity additions that destroyed the industry. Discipline has generally improved, but the cycle has not been eliminated.

### Business Model

Revenue = bit shipments × ASP per bit, by product type. ASP is the critical variable — it can swing 50–70% through a cycle while bit shipment volumes are relatively stable. This means gross margin tracks ASP almost directly: 40–50% gross margin at cycle peaks, negative gross margin at cycle troughs. CapEx is lumpy and must be maintained even through downturns to hold process technology competitiveness.

**The commodity cycle mechanism:** When demand is strong, all three DRAM makers add capacity. Capacity additions take 18–24 months to come online. By the time new supply arrives, the demand cycle may have turned. Oversupply drives ASP down. Losses mount. CapEx gets cut. Supply tightens again. Repeat. The cycle has compressed in recent years from 3–4 years to 2–3 years, but it persists.

**HBM is different:** HBM capacity requires converting existing DRAM capacity — it cannot be built in parallel at full scale. Converting to HBM means sacrificing standard DRAM bit output. This capacity trade-off creates a structural constraint on HBM supply that dampens oversupply risk. Additionally, HBM is allocated to customers under long-term supply agreements rather than sold on the spot market — removing the ASP volatility that defines commodity DRAM.

### Revenue Segments — Know These by Name

**By business unit (approximate FY2024 mix):**
| Business Unit | ~% Revenue | Key Products | Trend |
|---|---|---|---|
| Compute and Networking (CNBU) | ~45–50% | Server DRAM, HBM3E | Fast growing; HBM is the primary driver |
| Storage (SBU) | ~25–30% | NAND SSDs (enterprise, client), QLC NAND | Cyclical; enterprise SSD outperforms client |
| Mobile (MBU) | ~15–20% | Mobile DRAM, mobile NAND | Recovering; tied to smartphone upgrade cycle |
| Embedded (EBU) | ~10% | Automotive DRAM/NAND, industrial, IoT | Steady growth; automotive fastest |

**By product type:**
| Product | ~% Revenue | ASP Characteristics | Key Customers |
|---|---|---|---|
| DRAM (standard) | ~60–65% | Highly cyclical; spot + contract | Cloud hyperscalers, PC OEMs, mobile OEMs |
| NAND | ~25–30% | Highly cyclical; enterprise vs. client diverges | Enterprise storage, hyperscalers, OEMs |
| HBM | Growing; ~5–10% FY2024, targeting higher | Contracted; 5–8x standard DRAM ASP | NVIDIA (Blackwell), AMD (MI350), others |

**HBM revenue note:** HBM earns 5–8x the ASP per bit of standard DRAM. Even a small HBM mix shift has an outsized effect on blended revenue and gross margin. Track HBM as a separate line — CNBU revenue is not equivalent to HBM revenue. Management has been explicit about HBM revenue in recent earnings; document the exact figures each quarter.

### Memory Cycle Context — Know the History

| Cycle | Peak | Trough | Notes |
|---|---|---|---|
| 2018–2019 | ~47% gross margin (2018) | ~25% gross margin (2019) | Trade war; oversupply |
| 2020–2021 | Recovery | COVID demand surge sustained | Unusual; pandemic drove data center demand |
| 2021–2023 | Peak 2022 | –$5.8B operating income FY2023 | Most severe trough in recent history |
| 2024–present | Recovery underway | — | HBM accelerating recovery; standard DRAM still pressured |

**FY2023 context:** Micron reported a $5.8B operating loss — not a narrow miss, but a catastrophic trough. Revenue fell from ~$30B to ~$15B in two fiscal years. The company cut CapEx aggressively and idled some wafer starts. This is the baseline for understanding what the downside looks like without HBM as a structural offset.

### HBM — The Investment Thesis Centerpiece

**What HBM is:** High Bandwidth Memory is a stack of DRAM dies connected by through-silicon vias (TSVs) and a logic die at the base. The stack is then placed directly alongside the compute die (GPU, TPU) via TSMC's CoWoS packaging. The result: dramatically higher memory bandwidth at lower power consumption than standard DRAM. Every NVIDIA H100, H200, and Blackwell GPU requires HBM.

**HBM supply chain:**
| Supplier | Market Share | Status | Notes |
|---|---|---|---|
| SK Hynix | ~50% | Dominant; first mover | HBM3E supplier to NVIDIA. HBM4 development underway. |
| Samsung | ~25–30% | Struggling | Quality/yield issues with HBM3E have delayed certification. Has not been the primary NVIDIA supplier. |
| Micron | ~20–25% | Gaining | Won NVIDIA Blackwell HBM3E design certification. First time Micron has been at the forefront of an HBM cycle. |

**Why HBM is structurally different from standard DRAM:**
1. Contracted pricing — HBM is allocated under long-term supply agreements; not sold on spot market
2. Supply constrained by capacity conversion — HBM production uses the same fab capacity as standard DRAM; converting to HBM reduces standard DRAM output, creating a natural supply ceiling
3. High product qualification barrier — NVIDIA, AMD, and Google must qualify each supplier's HBM. Qualification takes 12–18 months; switching is not trivial. Micron's Blackwell certification is durable until the next-generation HBM spec change.
4. Demand visibility — hyperscaler GPU orders provide 12–18 months of HBM demand signal

**The structural question:** Is HBM large enough as a revenue % to prevent the next FY2023-style trough? Or does standard DRAM still dominate revenue enough that a DRAM cycle crash swamps HBM's premium pricing?

### Key Competitors

| Competitor | DRAM Share | HBM Share | Key Risk |
|---|---|---|---|
| SK Hynix | ~30% | ~50% | First-mover HBM advantage is durable through HBM4 cycle. TSMC CoWoS relationship well-established. |
| Samsung | ~40% | ~25–30% | HBM quality issues are a near-term problem. But Samsung has massive resources and will not concede HBM permanently. The risk: Samsung fixes its yield issues and intensifies HBM competition. |
| CXMT (China) | <5% but growing | 0% | Ramping mature-node DRAM capacity aggressively. Cannot do HBM or leading-edge DRAM yet. Primary threat: crashes standard DDR4/DDR5 commodity pricing while HBM remains tight. |

**CXMT threat deserves explicit treatment:** CXMT (ChangXin Memory Technologies) is ramping domestic DRAM capacity with Chinese government support, targeting commodity segments: DDR4, DDR5. They cannot do HBM and cannot reach leading-edge nodes. Their output going to market suppresses standard DRAM pricing, hurting Micron's non-HBM DRAM revenue. This is the most credible near-term competitive risk.

### Geopolitical Exposure

Micron's geopolitical risk profile is different from TSMC's:
- **China revenue:** ~10–15% of Micron revenue from China customers. China banned Micron products from critical infrastructure in May 2023 — directly costing revenue.
- **Export controls:** US export controls restrict Micron from selling advanced DRAM and NAND to certain Chinese end-users. This limits participation in China's domestic AI buildout.
- **Taiwan concentration:** Micron operates fabs in Taiwan (Taichung) for DRAM. Some exposure to Taiwan Strait risk, though less concentrated than TSMC.
- **CHIPS Act beneficiary:** Micron is building a new fab in New York (Clay, NY) with CHIPS Act support (~$6.1B grant). Idaho fab expansion also underway. US-based production capacity is growing.

---

## Directory Structure

```
micron-wiki/
  claude-micron.md          ← this file (schema, standing knowledge, conventions, workflows)
  index.md                  ← catalog of all wiki pages with one-line summaries
  log.md                    ← append-only record of ingests, queries, reviews
  entities/
    MU.md                   ← Micron Technology (primary entity)
    HXSL.md                 ← SK Hynix (HBM competitor — most relevant comp)
    NVDA.md                 ← NVIDIA (primary HBM customer; Blackwell design win)
    AMD.md                  ← AMD (HBM customer for MI-series)
  concepts/
    HBM.md                  ← High Bandwidth Memory — the structural thesis
    dram-cycle.md           ← DRAM commodity cycle mechanics and history
    nand-market.md          ← NAND competitive landscape (Kioxia, WD, Samsung, SK Hynix)
    cxmt-threat.md          ← CXMT China DRAM ramp — standard DRAM pricing risk
    chips-act.md            ← US CHIPS Act — Micron fab investment and grants
  sources/
    raw/                    ← immutable source documents (earnings transcripts, articles, reports)
    wisesheets/             ← financial data exports (annual, quarterly)
```

**Rules:**
- MU.md is the primary entity. All other entities exist to serve understanding of MU.
- Raw sources are never modified — the LLM reads from them, never writes to them
- The LLM owns `entities/`, `concepts/`, `index.md`, and `log.md` entirely
- Concept pages are created when a topic appears across multiple entity pages and deserves its own treatment

---

## MU.md — Entity Page Schema

*This is the template and guidance for building and maintaining MU.md specifically. Sections are in fixed order — do not reorder or skip.*

```markdown
# Micron Technology, Inc. (MU)

> The only US-headquartered manufacturer of DRAM and NAND at scale —
> and the company whose investment thesis turns on whether HBM has broken the commodity cycle.

*Last updated: YYYY-MM-DD | Wisesheets data as of: YYYY-MM-DD*

---

## Overview

- **Business model:** Integrated device manufacturer (IDM) — designs and manufactures its own
  memory and storage chips. Revenue = bit shipments × ASP per bit. Gross margin tracks ASP
  almost directly; the cycle is amplified by operating leverage on fixed fab costs.
- **Value chain position:** Sits between fab inputs (equipment: ASML, Applied Materials, Lam)
  and end markets (AI data centers, PC OEMs, mobile OEMs, automotive/industrial).
- **Founded:** 1978, Boise, Idaho. HQ still in Boise.
- **Listed:** NASDAQ: MU
- **Scale:** ~40,000+ employees. Fabs in Idaho, Virginia, Japan, Singapore, Taiwan.
- **Market cap:** $XX (as of YYYY-MM-DD)
- **Fiscal year:** September year-end (FY2025 = Oct 2024 – Sep 2025)

## Moat

*Assess each dimension: how strong today, and how durable over 10 years?*

### DRAM Oligopoly Position
Three companies manufacture DRAM at meaningful scale: Samsung (~40%), SK Hynix (~30%),
Micron (~25%). This extreme consolidation is the primary structural defense against commodity
cycle collapse — irrational capacity additions have been punished too severely and too recently.
Micron is the only US manufacturer. Assess oligopoly discipline each quarter: are players
cutting or adding capacity during downturns?

### HBM Design Wins
Winning NVIDIA Blackwell HBM3E certification is not trivial — it took Micron years of
process development. Qualification cycles for next-generation HBM (HBM4) will similarly
take 12–18 months per customer. First-mover certification advantages compound.
Document each HBM design win and its expected revenue duration.

### Process Technology
Micron competes at 1-alpha and 1-beta DRAM nodes, the leading edge of DRAM manufacturing.
Leading-edge nodes provide cost-per-bit advantage over competitors still on older nodes.
Assess Micron's node position vs. SK Hynix and Samsung each quarter — any gap widening
or closing is a gross margin signal.

### US Manufacturing Advantage
CHIPS Act investments (Idaho expansion, New York fab) will produce US-made DRAM and NAND.
Defense and critical infrastructure customers have a preference or requirement for
US-sourced memory — this is a structural, government-supported moat unavailable to
SK Hynix and Samsung.

### Scale and Learning Curve
Bit production volume drives process learning. Micron's position as the #3 DRAM producer
by share limits this advantage vs. Samsung and SK Hynix, but at $25B+ revenue scale,
learning curve effects are still material. Track bit output growth each quarter.

### 10-Year Moat Durability Assessment
The DRAM oligopoly is durable. The primary 10-year moat risk is CXMT (China) reaching
leading-edge DRAM capability — currently constrained by equipment export controls (ASML
EUV, advanced DUV). If controls hold, CXMT remains capped at DDR4/DDR5 commodity segments.
HBM moat durability: each HBM generation resets the qualification race — Micron's current
Blackwell position does not guarantee HBM4 leadership. Track Samsung's HBM yield recovery
as the primary HBM competitive threat.

## Financials

*All figures from Wisesheets. Always note pull date. Trends matter more than snapshots.*
*Micron's fiscal year ends in September — FY2024 = Oct 2023 – Sep 2024.*

### Income Statement
| Metric | TTM | 1Y ago | 3Y CAGR | 5Y CAGR |
|---|---|---|---|---|
| Revenue (USD) | | | | |
| Gross Margin % | | | | |
| Operating Margin % | | | | |
| Net Margin % | | | | |

**Cycle context note:** Always view Micron financials relative to cycle position.
A single-year snapshot is nearly meaningless — gross margin of 40% looks different
depending on whether you're at a peak, mid-cycle, or trough recovery.
Pull 10Y data from Wisesheets and annotate cycle phases explicitly.

### Cash Flow
| Metric | TTM | 1Y ago | 3Y avg |
|---|---|---|---|
| Operating Cash Flow | | | |
| CapEx (absolute) | | | |
| CapEx as % of Revenue | | | |
| Free Cash Flow | | | |
| FCF Margin % | | | |

**FCF note:** Micron's FCF is highly negative at cycle troughs (heavy CapEx + low margins)
and strongly positive at peaks. Evaluate FCF through-cycle average, not point-in-time.
Also track CapEx pattern vs. cycle: does management cut CapEx at troughs (rational
discipline) or keep spending (concerning)?

### Balance Sheet
| Metric | Latest |
|---|---|
| Cash + Equivalents | |
| Total Debt | |
| Net Cash / (Net Debt) | |

**Balance sheet matters for Micron:** Unlike TSMC, Micron carries meaningful debt.
At cycle troughs, net debt position determines whether the company can withstand
losses without distress. FY2023 trough was survived with debt but no distress — assess
whether the balance sheet can absorb the next trough at the current debt level.

### Capital Efficiency
| Metric | Latest | 3Y avg | 5Y avg | Cycle Peak | Cycle Trough |
|---|---|---|---|---|---|
| ROIC | | | | | |
| ROE | | | | | |
| Gross Margin | | | | | |

**ROIC through-cycle is the key metric:** If Micron generates ROIC > WACC on average
across a full cycle (peak and trough), it is creating value. If trough ROIC destroys
more value than peak creates, the long-term holder is not being rewarded.
Use Wisesheets 10Y data to compute cycle-average ROIC.

## Revenue Segments

*Update every quarter from earnings. Track all four business units.*

### By Business Unit
| Segment | Current Revenue | Current % | QoQ Change | YoY Change | Outlook |
|---|---|---|---|---|---|
| CNBU (Compute & Networking) | | | | | |
| SBU (Storage) | | | | | |
| MBU (Mobile) | | | | | |
| EBU (Embedded) | | | | | |

**CNBU note:** Contains both HBM and standard server DRAM. Management has been
disclosing HBM revenue explicitly — always extract it separately. CNBU ex-HBM
gives you the standard DRAM server picture; HBM tells you the structural story.

### HBM Detail (within CNBU)
- HBM revenue (if disclosed): $[X]B in [quarter]
- HBM ASP vs. standard DRAM: management commentary
- HBM bit output: management guidance on YoY growth
- Design wins: NVIDIA Blackwell (confirmed), AMD MI-series (confirm status), others
- HBM generation roadmap: HBM3E (current), HBM4 (next — qualification status)

### By Product
| Product | ~% Revenue | ASP Direction | Volume Direction | Notes |
|---|---|---|---|---|
| DRAM (total) | | | | |
| — of which HBM | | | | |
| NAND | | | | |

### End Market Mix
Track where bits are going: data center, PC, mobile, automotive, industrial.
Data center growth is the HBM demand driver. PC and mobile signal the standard
DRAM cycle. Automotive is the structural growth story (EV silicon content).

## Growth Drivers

*For each driver: what it is, magnitude, timeline, probability of materializing.*

### 1. HBM Demand from AI Training
Every next-generation AI GPU requires more HBM — Blackwell H200 uses 141GB HBM3E,
vs. H100's 80GB. Each GPU generation increases HBM content per chip. Combined with
accelerating GPU shipment volumes, total HBM bit demand is growing faster than any
other memory market. Micron's Blackwell design win means this demand flows directly
to MU revenue.
*Magnitude: Very high. Timeline: Now through 5Y+. Probability: High.*

### 2. HBM ASP Premium
HBM earns 5–8x the ASP per bit of standard DRAM. As HBM grows as a % of Micron's
DRAM bit output, blended DRAM ASP rises even if standard DRAM pricing is flat or
declining. Track this mix-shift-driven ASP uplift each quarter.
*Magnitude: High per unit. Timeline: Continuous as HBM mix grows. Probability: High.*

### 3. Data Center DRAM Recovery
Server DRAM (DDR5, LPDDR5X) for standard AI inference servers, hyperscaler compute,
and enterprise IT represents a separate large demand pool from HBM. DDR5 adoption
is accelerating. Data center DRAM pricing has been recovering since H2 2024.
*Magnitude: Medium-High. Timeline: 2025–2027. Probability: High.*

### 4. NAND Enterprise Recovery
Enterprise SSD demand from hyperscalers (all-flash storage for AI workloads) is
recovering. Micron's 232-layer and 276-layer NAND is competitive. Enterprise NAND
earns a premium over client NAND — track enterprise vs. client mix shift.
*Magnitude: Medium. Timeline: 2025–2027. Probability: Medium-High.*

### 5. Automotive Memory Growth
EV and ADAS systems require 3–10x more memory per vehicle than ICE equivalents.
Embedded DRAM and NAND for automotive applications has long qualification cycles
(2–3 years) but once qualified, revenue is sticky. Automotive mix in EBU is growing.
*Magnitude: Medium. Timeline: 2026–2032. Probability: High.*

### 6. CHIPS Act Capacity Expansion
The New York fab (potentially $100B total investment over a decade) and Idaho
expansion funded partly by CHIPS Act create incremental US production capacity.
This capacity positions Micron as the preferred domestic supplier for
US government, defense, and critical infrastructure customers — a captive market.
*Magnitude: Medium. Timeline: 2026–2030+. Probability: High (construction ongoing).*

### 7. CXMT Stalls or Gets Export-Controlled
If US/EU export controls tighten further and restrict CXMT's equipment access,
CXMT's progress toward leading-edge DRAM slows. This removes the primary standard
DRAM price pressure risk. Track export control policy as a tail upside catalyst.
*Magnitude: High if it happens. Timeline: Uncertain. Probability: Medium.*

## Risks

*For each risk: describe it, assess probability (Low/Medium/High), assess magnitude (1–5).*

### The Commodity Cycle — Structural Risk #1

DRAM has been one of the most destructive investments in semiconductor history
for buy-and-hold investors who don't manage through cycles. The question this
investment thesis hinges on is whether HBM structurally changes the earnings floor.

**Bear case on HBM thesis:** HBM is still ~10–15% of DRAM bit output. Standard DRAM
is still ~85–90% of bits. If a standard DRAM oversupply cycle hits (say 2026–2027
as new capacity comes online), the majority of Micron's revenue gets hit hard —
HBM premium revenue cannot fully offset standard DRAM collapse. FY2023 happens
again, only modestly less severe.

**Bull case on HBM thesis:** The capacity conversion trade-off means adding HBM
capacity means removing standard DRAM capacity — so a DRAM oversupply while
simultaneously ramping HBM is structurally harder. Industry discipline plus
the capacity conversion constraint prevents the magnitude of FY2023 from recurring.

*Probability that cycle severity is similar to FY2023: Medium. Magnitude: 5.*
*Track: industry capacity additions, ASP trend for standard DRAM each quarter.*

### CXMT and Chinese DRAM Expansion

CXMT is targeting commodity DRAM (DDR4, DDR5) with heavy state subsidies.
Their output hitting the market suppresses standard DRAM pricing. They cannot
reach HBM or leading-edge DRAM currently — but their commodity output still
matters because it competes with Micron's non-HBM DRAM revenue (~85% of bits).

*Probability: High (already happening). Magnitude: 3–4 on standard DRAM ASP.*
*Track: CXMT production reports via TrendForce, DRAMeXchange.*

### Samsung HBM Recovery

Samsung is the largest DRAM maker by share and is highly motivated to fix its
HBM quality issues. If Samsung's HBM3E or HBM4 achieves NVIDIA qualification,
Micron faces a three-way HBM competition vs. the current two-way (Hynix + Micron).
This would pressure HBM ASP and potentially Micron's allocation share.

*Probability of Samsung HBM recovery: Medium (well-resourced but has failed twice).
Magnitude: 3 (erodes one pillar of the thesis but doesn't destroy it).*
*Track: Samsung earnings commentary on HBM yield; NVIDIA supply chain reports.*

### AI CapEx Plateau

If hyperscaler AI spending plateaus or declines, HBM demand growth slows.
Unlike standard DRAM (which has broad demand: PC, mobile, enterprise), HBM
demand is concentrated in a narrow set of buyers (NVIDIA, AMD, Google, Microsoft).
Demand concentration means a single demand shift is high-impact.

*Probability of AI CapEx plateau in 2–3 years: Medium. Magnitude: 4 on HBM.*
*Track: Hyperscaler quarterly CapEx guidance (Amazon, Microsoft, Google, Meta).*

### Export Control Impact on China Revenue

~10–15% of Micron revenue historically from China. China's May 2023 ban of Micron
from critical infrastructure reduced this. Further tightening of US export controls
could reduce Chinese customers' ability to purchase advanced Micron products.
This is a direct revenue loss with no near-term offset.

*Probability of further China revenue reduction: Medium. Magnitude: 2–3.*
*Track: US-China export control policy; China customer revenue disclosure quarterly.*

### Balance Sheet at Cycle Trough

If a severe trough occurs while Micron is mid-CapEx-cycle (Idaho expansion, NY fab),
the company could face FCF deeply negative with high debt service. This was
manageable in FY2023 but could be more severe with higher CapEx commitments.

*Probability: Low–Medium (CHIPS Act grant timing helps). Magnitude: 3.*
*Track: Net debt position quarterly; CapEx commitments vs. operating cash flow.*

## Competitor Comparison

*Update when earnings data is available for SK Hynix and Samsung.*

| Metric | Micron (MU) | SK Hynix (HXSL) | Samsung Memory |
|---|---|---|---|
| DRAM market share | ~25% | ~30% | ~40% |
| HBM market share | ~20–25% | ~50% | ~25–30% (quality issues) |
| HBM generation | HBM3E (Blackwell win) | HBM3E (lead) | HBM3E (struggling) |
| Gross margin (latest) | | | |
| CapEx intensity | | | |
| Geographic risk | Idaho/Virginia primary | Korea primary | Korea primary |
| CHIPS Act beneficiary | Yes ($6.1B grant) | No | No |

**Key comp: SK Hynix is the most relevant peer.** It is ahead on HBM, has similar
DRAM market position, and its commentary on HBM supply/demand is the best market
signal available. Read SK Hynix earnings the week they report — it gives HBM demand
context before Micron's earnings. HXSL trades on Korean exchange (000660.KS).

## Catalysts

*Time-bound. Archive played-out catalysts with the outcome noted.*

### Active Catalysts
| Catalyst | Expected Timing | Bull Signal | Bear Signal |
|---|---|---|---|
| HBM4 qualification (NVIDIA, AMD) | 2025–2026 | Micron qualifies for HBM4 alongside Hynix | Samsung qualifies; three-way competition |
| New York fab groundbreaking / progress | 2025–2026 | On schedule; CHIPS Act grant received | Delays; cost overruns |
| DRAM ASP stabilization | 2025 | Standard DRAM pricing inflects positive | Continued pricing pressure from CXMT |
| Samsung HBM yield recovery | Uncertain | No recovery (Micron/Hynix duopoly holds) | Samsung certified by NVIDIA for Blackwell |
| Hyperscaler HBM purchase commitments | Quarterly | Long-term agreements announced | Spot buying behavior; no commitment |

### Archived Catalysts
*(Move here once played out, with outcome)*

## Monitoring Checklist

*Run this checklist every quarter before updating the Investment View and Decision Log.*

### Monthly (between earnings)
- [ ] **DRAM spot and contract price (DRAMeXchange / TrendForce)** — standard DDR5
  contract price direction. Increasing = tailwind; decreasing = headwind for non-HBM DRAM.
  *Where: TrendForce monthly DRAM price report, published ~10th of each month.*
- [ ] **NAND spot price** — enterprise vs. client. Enterprise premium is the signal.
- [ ] **NVIDIA data center GPU shipment estimates** — proxy for HBM demand 1–2 quarters ahead.

### Quarterly (earnings cycle)
- [ ] **HBM revenue (absolute and % of CNBU)** — is HBM growing as a revenue % fast enough
  to meaningfully offset standard DRAM cycle exposure?
- [ ] **Gross margin (actual vs. guidance)** — the primary cycle position indicator.
  Compare to 10Y historical range from Wisesheets.
- [ ] **CapEx guidance** — direction signals management confidence in demand outlook.
  Cuts during a downturn = discipline; aggressive increases = either confidence or cycle over-extension.
- [ ] **DRAM/NAND ASP commentary** — management directional language on pricing by product.
  Extract exact language; compare to prior quarter.
- [ ] **Bit shipment growth guidance** — volume vs. price is the decomposition that matters.
- [ ] **HBM design win updates** — any new customer qualifications; HBM4 progress.
- [ ] **China revenue %** — monitor for export control impact.
- [ ] **CHIPS Act grant/milestone status** — any updates on Idaho or NY fab progress.

### Leading Indicators (from related companies)
- [ ] **SK Hynix earnings** — the most direct HBM peer. Their HBM ASP/demand commentary
  directly signals the market Micron operates in. Read before Micron earnings each quarter.
- [ ] **NVIDIA data center revenue and GPU shipments** — HBM pull-through demand.
  NVIDIA Blackwell shipments are the primary HBM revenue driver for 2025–2026.
- [ ] **Hyperscaler CapEx guidance** — Amazon, Microsoft, Google, Meta.
  AI CapEx growth = HBM demand growth. Any guidance cut is an early HBM demand warning.
- [ ] **ASML DUV/EUV shipments to non-US entities** — a leading indicator of
  whether CXMT can access leading-edge lithography. Blocked = CXMT stays at commodity DRAM.
- [ ] **TrendForce DRAM supply/demand report (quarterly)** — industry-wide bit supply growth
  vs. demand growth. Oversupply > 5% is a pricing warning.

### Geopolitical
- [ ] **US-China export control changes** — specific restrictions on DRAM/NAND to China.
- [ ] **CXMT capacity announcements** — any reports of CXMT capacity expansion pace.
- [ ] **CHIPS Act implementation** — grant milestones, conditions, any policy changes.

## Investment View

*Synthesizes all sections above into a quantified position. Update every quarter.*
*All models anchored in Wisesheets 10Y annual + quarterly data. Always note data pull date.*

### Valuation
| Metric | Current | 1Y ago | Cycle Peak | Cycle Trough |
|---|---|---|---|---|
| Price (MU) | | | | |
| Market Cap | | | | |
| EV | | | | |
| Forward P/E | | | | |
| EV/EBITDA | | | | |
| EV/Sales | | | | |
| Price / Book | | | | |

**Cycle-adjusted valuation:** Micron's P/E is meaningless at cycle extremes (infinite at
trough losses, misleadingly low at peak earnings). EV/Sales and EV/EBITDA through-cycle
are more reliable. Pull 10Y from Wisesheets. The question: at what point in the cycle
does the current price imply you're buying?

### WACC
| Input | Value | Notes |
|---|---|---|
| Risk-free rate | | 10Y US Treasury |
| Beta (5Y monthly) | | Memory stocks carry higher beta than market; pull from Wisesheets |
| Equity risk premium | | Use Damodaran's published ERP |
| Cost of equity | | Rf + (β × ERP) |
| Cost of debt | | Effective rate on outstanding debt |
| Debt / (Debt + Equity) | | Market value weights |
| Tax rate | | Effective tax rate from financials |
| **WACC** | | |

*Micron's beta will be higher than TSMC's — memory stock volatility reflects cycle exposure.*

### DCF

**The challenge with Micron DCF:** Standard 5-year DCF models don't handle cyclical businesses
well — they project from current earnings, which may be peak or trough. The right approach:

**Step 1: Establish cycle-normalized earnings.**
Pull 10Y revenue and gross margin from Wisesheets. Compute average gross margin through
a full cycle. That's the normalized margin — not current peak, not trough.

**Step 2: Project cycle-normalized revenue.**
- HBM bit growth (driven by AI GPU shipments) × HBM ASP
- Standard DRAM bit growth (PC + mobile + server ex-HBM) × normalized standard DRAM ASP
- NAND revenue (enterprise + client) × normalized NAND ASP
- Sum to total normalized revenue; apply HBM mix-shift uplift to blended ASP over 5 years

**Step 3: Apply normalized margins.**
- Gross margin: use cycle-normalized base, then add HBM ASP uplift (structural improvement)
- Operating margin: apply historical operating leverage ratio
- CapEx: model through-cycle average, noting the CHIPS Act expansion years

**Step 4: FCF and terminal value.**
- FCF = Operating CF − CapEx (use through-cycle average CapEx, not single-year)
- Terminal growth rate (document assumption — memory bit demand grows ~20–30%/year but
  ASP deflation partially offsets; normalized revenue CAGR is the better anchor)
- Terminal value = FCF(year 5) × (1 + g) / (WACC − g)
- Discount at WACC → intrinsic value

**Sensitivity table:** Run across revenue CAGR (8%, 12%, 16%, 20%) and WACC (9%, 11%, 13%)
to produce intrinsic value matrix. Flag which cell corresponds to the current price.

### Reverse DCF

*Start from current stock price. Back out the implied assumptions.*

1. Take current market cap and EV
2. Assume terminal growth rate and WACC
3. Solve for implied FCF / revenue CAGR
4. Ask: is the implied growth rate above or below cycle-normalized reality?
5. Compare against SK Hynix valuation on same metrics — if Micron trades at a large
   discount to Hynix without obvious reason, investigate why. Discount or premium?
6. **The key question each quarter:** Is the market pricing Micron as a commodity
   cyclical (discount to normalized earnings), or as an HBM-driven structural grower
   (premium to cycle)? The answer tells you what the market believes and whether you agree.

### Scenarios

| Scenario | Key Assumptions | Revenue 5Y CAGR | Gross Margin (exit) | FCF Margin (exit) | Intrinsic Value | IRR at Entry |
|---|---|---|---|---|---|---|
| Bull | HBM becomes 30%+ of DRAM revenue; standard DRAM cycle mild; Samsung fails to recover HBM | | | | | |
| Base | HBM reaches 20% of DRAM revenue; normal cycle hits once over 5Y; Samsung partially recovers | | | | | |
| Bear | Standard DRAM oversupply 2026–2027; HBM < 15% of revenue; Samsung recovers; CXMT pressure | | | | | |
| Tail | Severe DRAM crash worse than FY2023 + AI CapEx plateau simultaneously | | | | | |

*Bear case test: Does Micron survive with balance sheet intact if FY2023 repeats with
higher CapEx commitments? At what price is the Bear scenario fully priced in?*

### Decision Log

*Append-only. Never edit past entries. This is a permanent record.*

```
### [YYYY-QX] Decision: BUY / ADD / HOLD / TRIM / SELL
- MU price at decision: $XX
- Market cap at decision: $XXB
- Cycle position assessment: [early-cycle / mid-cycle / peak / early-trough / trough]
- HBM revenue % (current): [X%]
- Key reasoning: [2–3 sentences — what drove this quarter's decision]
- Monitoring Checklist summary: [what the checklist showed this quarter]
- Model update: [what changed in the DCF/scenarios vs. last quarter]
- What changed since last quarter: [new data, revised assumptions, or reaffirmed conviction]
- What would change this view: [the specific, concrete conditions that flip the decision]
```

## Cross-links

### Related Entities
- [[HXSL]] — SK Hynix. HBM market leader. Most direct peer; read their earnings first.
- [[NVDA]] — NVIDIA. Primary HBM customer; Blackwell design win. Data center GPU growth = HBM demand.
- [[AMD]] — AMD. HBM customer for MI-series AI GPUs. Growing HBM allocation.

### Related Concepts
- [[HBM]] — High Bandwidth Memory. The structural thesis. Supply dynamics, ASP premium, design win economics.
- [[dram-cycle]] — DRAM commodity cycle. Full historical record. Why troughs happen, how long they last.
- [[nand-market]] — NAND competitive landscape. Less central to thesis but 25–30% of revenue.
- [[cxmt-threat]] — CXMT China DRAM expansion. The standard DRAM price pressure risk.
- [[chips-act]] — US CHIPS Act. Micron fab investment, grant structure, US manufacturing moat.

### Key Sources
*(Populate as sources are ingested)*
```

---

## Operations

### Ingest
When a new source is added (Micron earnings transcript, SK Hynix earnings, TrendForce report,
NVIDIA earnings, Wisesheets export):
1. Read the source in full
2. Note: what is new, what contradicts existing wiki content, what changes cycle assessment
3. Update `entities/MU.md` — primary target for almost every Micron source
4. Update relevant concept pages (`HBM.md`, `dram-cycle.md`, `cxmt-threat.md`)
5. Update related entity pages if the source contains relevant data (e.g., SK Hynix earnings
   with HBM pricing commentary affects both HXSL.md and HBM.md)
6. Update `index.md` if new pages were created
7. Append to `log.md`:
   ```
   ## [YYYY-MM-DD] ingest | [Source Title]
   Pages updated: [list]
   Key changes: [1–2 sentences on what moved]
   Cycle position change: [any change to cycle assessment]
   Contradictions found: [any claims that conflict with existing wiki content]
   ```

**Priority sources to ingest:**
- Micron quarterly earnings transcripts and 10-Q/10-K (primary)
- SK Hynix quarterly earnings — read before Micron earnings; best peer signal
- TrendForce monthly DRAM and NAND price reports (monthly cadence)
- NVIDIA earnings — Blackwell shipment commentary = HBM demand signal
- Wisesheets annual and quarterly pulls (financial model and cycle tracking)

### Query
When asked a question against the wiki:
1. Read `index.md` to identify relevant pages
2. Read those pages in full
3. Synthesize an answer with citations to specific wiki sections
4. If the answer involves cycle position assessment or HBM thesis update — file it back into
   the wiki. The cycle position assessment is the most time-sensitive update to maintain.

### Quarterly Review
Run at the start of each quarter, before updating the Decision Log:
1. Pull latest quarterly financials from Wisesheets (note pull date)
2. Run through the full Monitoring Checklist — document what changed for each item
3. Update MU.md Financials with latest actuals; annotate cycle position
4. Update Revenue Segments with latest business unit and HBM detail
5. Update Catalysts — archive played-out ones with outcome, add new ones
6. Refresh DCF (cycle-normalized model); update Reverse DCF with current price
7. Update Scenarios if HBM mix or cycle position has changed materially
8. Append a new entry to the Decision Log with full reasoning
9. Log the review in `log.md`:
   ```
   ## [YYYY-MM-DD] quarterly-review | [YYYY-QX]
   Cycle position: [early-cycle / mid-cycle / peak / trough]
   HBM revenue %: [X%]
   Monitoring Checklist: [summary of key findings]
   Model changes: [what changed in the DCF/scenarios]
   Decision: BUY / ADD / HOLD / TRIM / SELL
   ```

### Lint
Run periodically or when the wiki feels stale:
- Check that cycle position assessment in MU.md matches current financial data
- Flag DRAM/NAND pricing figures older than one month — mark for TrendForce refresh
- Verify HBM revenue figure reflects the most recent earnings, not a prior quarter
- Check that the Decision Log reflects the most recent quarterly review
- Identify whether the Samsung HBM recovery risk is correctly calibrated to current data
- Surface gaps: what would the next TrendForce report or Wisesheets pull answer?

---

## Conventions

- **Primary ticker:** MU (NASDAQ). SK Hynix: 000660.KS (Korean exchange).
- **Currency:** USD throughout (Micron reports in USD)
- **Fiscal year:** September end. FY2025 = Oct 2024 – Sep 2025. Always specify fiscal quarter vs. calendar quarter.
- **Cross-links:** use `[[Ticker]]` or `[[concept-name]]` format for all internal references
- **Dates:** YYYY-MM-DD everywhere. Quarterly labels: 2026-Q1, 2026-Q2, etc.
- **Cycle position:** Always annotate financial data with cycle phase. "Gross margin 47% (cycle peak)" is meaningful; "Gross margin 47%" is not.
- **Wisesheets data:** always note the pull date when citing any financial figure
- **Decision Log:** append-only. Past entries are a permanent record. Never edit them.
- **TrendForce data:** note the specific month of the price report; DRAM pricing is monthly and directionally volatile
- **Numbers:** USD millions or billions consistently within a page; state which at the top

---

## index.md Format

```markdown
# Micron Wiki Index
Last updated: YYYY-MM-DD

## Entities
- [[MU]] — Micron Technology. Primary subject. DRAM/NAND IDM; HBM thesis; US-only manufacturer at scale.
- [[HXSL]] — SK Hynix. HBM market leader. Most relevant peer; read their earnings before Micron's.
- [[NVDA]] — NVIDIA. Primary HBM customer. Data center GPU shipments = HBM demand signal.
- [[AMD]] — AMD. HBM customer (MI-series). Growing allocation.

## Concepts
- [[HBM]] — High Bandwidth Memory. The structural thesis. ASP premium, supply dynamics, design win economics.
- [[dram-cycle]] — DRAM commodity cycle. Historical record of cycle mechanics and timing.
- [[nand-market]] — NAND competitive landscape and pricing dynamics.
- [[cxmt-threat]] — CXMT China DRAM expansion. Standard DRAM pricing risk.
- [[chips-act]] — US CHIPS Act. Micron fab investment, grants, US manufacturing moat.

## Sources
- [filename] — [one-line description, date ingested]
```

## log.md Format

```markdown
# Micron Wiki Log

## [YYYY-MM-DD] ingest | [Source Title]
Pages updated: ...
Key changes: ...
Cycle position change: ...
Contradictions found: ...

## [YYYY-MM-DD] query | [Question asked]
Pages read: ...
Filed back into wiki: yes / no — [which page]

## [YYYY-MM-DD] quarterly-review | [YYYY-QX]
Cycle position: ...
HBM revenue %: ...
Monitoring Checklist summary: ...
Model changes: ...
Decision: ...

## [YYYY-MM-DD] lint
Issues found: ...
Actions taken: ...
Data gaps identified: ...
```
