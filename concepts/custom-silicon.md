# Custom Silicon — Hyperscaler ASICs

> The trend of major hyperscalers designing their own AI chips rather than buying NVIDIA GPUs — creating the second AI silicon wave that flows through Marvell and TSMC.

*Last updated: 2026-05-14*

---

## What Custom Silicon Is

Custom ASICs (Application-Specific Integrated Circuits) designed by hyperscalers for their specific AI workloads — training large models, running inference at scale, processing recommendation system queries. Unlike NVIDIA's general-purpose GPUs, custom ASICs are optimized for one company's specific models and infrastructure, yielding better performance-per-watt and lower cost-per-inference at scale.

## Why Hyperscalers Build Custom Silicon

1. **Cost at scale:** At 100,000+ chips, even a 20% cost improvement per chip is billions of dollars annually
2. **Performance optimization:** A chip designed for the exact model architecture and data types runs more efficiently than a general-purpose GPU
3. **Supply independence:** Reduces dependency on NVIDIA's supply chain, pricing, and roadmap
4. **Competitive differentiation:** A faster inference chip means cheaper AI products for customers

## Major Custom Silicon Programs

| Company | Chip | Type | Co-designer | Foundry | Status |
|---|---|---|---|---|---|
| Google | TPU v5/v6 | Training + Inference | Marvell (partially) | TSMC | Volume production |
| Amazon | Trainium2 | Training | Annapurna/Marvell | TSMC | Ramp |
| Amazon | Inferentia | Inference | Annapurna | TSMC | Volume |
| Microsoft | Maia 200 | Training | Marvell | TSMC | Ramping |
| Meta | MTIA (Meta Training and Inference ASIC) | Inference | Internal | TSMC | Production |
| Apple | Neural Engine (A/M series) | On-device inference | Internal | TSMC | Mature |

## Portfolio Implications

**TSMC (TSM):** All custom silicon is manufactured at TSMC. The custom silicon trend creates a *second* AI silicon demand wave on top of NVIDIA/AMD GPU demand. Even if NVIDIA loses some hyperscaler share to custom ASICs, total TSMC wafer demand may grow — because custom ASICs plus NVIDIA GPUs together use more wafers than NVIDIA alone.

**Marvell (MRVL):** Marvell is the primary co-design partner for several hyperscaler programs (Google, Amazon, Microsoft). Marvell provides the ASIC design engineering that hyperscalers don't want to build fully in-house. As more hyperscalers launch custom silicon programs, Marvell's pipeline grows.

**NVIDIA (NVDA):** Custom silicon is a competitive threat — but primarily at inference, not training. NVIDIA still dominates training because CUDA is deeply embedded. The threat is real but slower-moving than headlines suggest.

## Timeline Dynamics

Custom ASIC design cycles: 18–24 months from design kickoff to first silicon; 6–12 more months to production qualification. Revenue from a design win flows 2–4 years after the win announcement. This means Marvell's current design wins are the 2026–2028 revenue, not next quarter.

## Key Questions to Track

- How many hyperscalers have active Marvell co-design relationships? Any new wins announced?
- Is custom silicon taking inference share from NVIDIA faster than expected?
- Does NVIDIA respond with inference-optimized products (NIM, Spectrum-X, etc.) that blunt custom silicon adoption?

## Dated Intelligence Log

### 2026-05-24 — MRVL

**Custom ASIC revenue scaled from zero to $1.5B in FY2026; management guiding >20% YoY growth in FY2027 and at least doubling in FY2028** — pre-earnings consensus data confirms the custom silicon ramp is now a material revenue line at Marvell, not a future promise. At >$2B projected by FY2029 from NIC and CXL use cases alone, custom silicon is transitioning from a growth driver to Marvell's defining revenue segment. The 3-year trajectory ($0 → $1.5B → $1.8B → $3B+) is the fastest-scaling silicon franchise in the current AI supply chain wave. Amazon Trainium3 (Scorpio X) confirmed in active production ramp; XPU-Attach broadening beyond Amazon. Source: ad-hoc-news.de / Quiverquant, 2026-05-22.

### 2026-05-23 — MRVL

**Stifel: optical interconnect revenue growth revised from 30% to 50% YoY for FY2027; AWS Trainium 3 confirmed in production; XPU-Attach broadening** — Stifel's pre-earnings channel check (PT raised $140→$210) produced the first third-party confirmation that Trainium 3 is actively ramping and that interconnect growth is accelerating. XPU-Attach — Marvell connectivity silicon bundled into hyperscaler custom ASIC deployments — is expanding to programs beyond Amazon, suggesting the custom silicon supply chain attach rate is increasing faster than prior models assumed. If confirmed at May 27 earnings, this 50% interconnect growth guide would meaningfully revise the FY2027 revenue story.

### 2026-05-22 — MRVL / ALAB

**NVDA invested $2B strategically in Marvell; Amazon Trainium3 (Scorpio X) ramp visible through Astera Labs** — NVDA's $2B stake validates Marvell as the central co-design partner for the custom ASIC wave, not a peripheral player. The Amazon Trainium3 ramp is evidenced by ALAB's revenue growth (+93% YoY Q1 2026) from PCIe connectivity into the Scorpio X cluster. The three-company stack — MRVL (ASIC design) + ALAB (connectivity) + TSM (foundry) — confirms the custom silicon supply chain is scaled and investable. Jensen Huang on Dwarkesh (April 15, 2026) confirmed NVIDIA views custom ASICs as complementary at inference, not competitive at training.

### 2026-05-24 — MRVL

**Marvell's Celestial AI acquisition ($3.25B, Feb 2, 2026) confirms optical interconnect is now inseparable from the custom ASIC thesis** — Custom ASICs designed for inference at hyperscale require optical scale-up interconnects (not just copper) to link chips at 3.2T+ bandwidth. Celestial AI's Photonic Fabric™ + Polariton's plasmonics (April 2026) give Marvell end-to-end optical IP that complements its ASIC design wins. This means Marvell is not just the custom silicon co-designer but the optical connectivity layer that custom silicon clusters require — effectively expanding the per-cluster attach value. The optical moat (Celestial AI + Polariton + legacy SerDes/DSP) is now the second structural choke point in Marvell's business model alongside the ASIC co-design franchise. Confirmed hyperscaler design base now spans Google, Amazon, and Microsoft.

### 2026-05-27 — MRVL

**XConn Technologies ($540M acquisition, completed Feb 10, 2026) extends Marvell from ASIC co-designer to full connectivity stack including PCIe/CXL switches — direct ALAB competition** — XConn's PCIe 5 + CXL 2.0 switches are in production; PCIe 6 + CXL 3.1 switches are sampling (the latter directly competes with Astera Labs Scorpio X 320-lane PCIe 6 switch). XConn will contribute ~$100M in revenue in FY2028, beginning H2 FY2027. Combined with Celestial AI (Photonic Fabric optical scale-up), Polariton (plasmonics for co-packaged optics), and legacy SerDes/DSP IP, Marvell's connectivity offering now spans the entire data center fabric layer. The custom silicon thesis has expanded: Marvell is not just co-designing the compute chips, it is also supplying the switches, optical links, and DSP silicon that connect those chips. This raises the per-cluster attach value materially — every AI cluster needs both the custom ASIC AND the interconnect, and Marvell now provides both. Source: Data Center Dynamics / Marvell Newsroom, 2026-02-10.

### 2026-05-26 — MRVL

**Amazon $225B Trainium commitment backlog (exiting Q1 2026 calendar) is the largest single-customer quantification of custom silicon demand to date** — Wells Fargo's May 20 channel check revealed Amazon had $225B in committed Trainium deployments exiting Q1 2026. At Marvell's estimated revenue share per cluster, this underpins Wells Fargo's $6B annual Trainium-related revenue forecast for FY2027 and FY2028. The $225B figure reframes the custom silicon thesis from "emerging" to "committed infrastructure program at scale." This is not CapEx guidance; it is committed deployment — meaning the silicon co-design work (Marvell), manufacturing (TSMC), and connectivity (Astera Labs) are already contracted downstream. Custom silicon is no longer a thesis about what hyperscalers might do; it is now quantifiably underwritten.

### 2026-05-27 — MRVL

**Q1 FY2027 actuals confirm custom ASIC ramp on track: $2.418B (+28% YoY); FY2028 management guidance $15B is the first formal multi-year revenue commitment from any custom silicon co-designer** — Marvell's Q1 FY2027 result ($2.418B revenue, $0.80 non-GAAP EPS) beat estimates and management raised FY2027 to ~$11B (from ~$10B) and gave first-time FY2028 guidance of ~$15B (~40% YoY). Custom ASIC revenue alone guided to at least 2× in FY2028 (>$3B from $1.5B FY2026). Data center segment expected +50% YoY in FY2028. This is the first time a co-designer has given management-endorsed multi-year revenue guidance anchored to custom silicon programs — converting the custom silicon thesis from analyst-modeled to management-underwritten. The $15B FY2028 target implies Marvell's custom ASIC + connectivity business is on track to exceed $6B by FY2028, validating the hyperscaler co-design franchise thesis across 3 confirmed programs (Google, Amazon, Microsoft). Source: Marvell 8-K / earnings call, 2026-05-27.

### 2026-05-28 — MRVL / NVDA

**NVLink Fusion changes the thesis frame: custom silicon is no longer a substitute for NVIDIA — it integrates into NVIDIA** — The June 2 Computex keynote (Jensen Huang + Matt Murphy, joint) revealing NVLink Fusion details marks a paradigm shift in the custom silicon thesis. Prior framing: hyperscaler custom ASICs (Trainium, TPU, Maia) are an alternative to buying NVIDIA GPUs — a substitution risk for NVDA. New framing: custom ASICs designed by Marvell connect natively into NVIDIA AI factory infrastructure via NVLink Fusion — making NVIDIA the connective layer, not the displaced vendor. NVIDIA's $2B investment in Marvell and CEO's joint keynote appearance signals that NVIDIA views Marvell-backed custom silicon as an ecosystem expansion, not a threat. For the portfolio: this is net positive for both MRVL (validated as NVIDIA ecosystem partner) and NVDA (extends CUDA/NVLink connective standard to heterogeneous silicon). The custom silicon threat to NVDA is now more nuanced — inference diversification is real, but training and scale-up connectivity remains NVIDIA-anchored. Source: PR Newswire / Marvell.com, 2026-05-28.

### 2026-05-28 — ALAB

**Astera Labs joins NVIDIA NVLink Fusion ecosystem as connectivity layer for hybrid racks — custom silicon clusters now require ALAB as much as MRVL** — With the NVLink Fusion partnership, ALAB is no longer a peripheral connectivity supplier sitting outside the AI factory ecosystem. ALAB's PCIe/CXL retimers and Scorpio X switches enable non-NVIDIA XPUs (Amazon Trainium, Google TPU, Microsoft Maia) to interconnect with NVIDIA AI factory infrastructure at multi-TB/s throughput. This means every custom silicon cluster built on NVLink Fusion requires both MRVL (custom XPU co-design + optical scale-up) and ALAB (PCIe/CXL retimers and switches). The supply chain attach expands: instead of one company capturing the custom silicon connectivity, two satellite positions (MRVL + ALAB) each serve a distinct layer of the same cluster. Combined with 10 active hyperscaler engagements and the confirmed Amazon Trainium3 Scorpio X design win, ALAB is now structurally embedded in the custom silicon infrastructure wave, not merely an adjacency to it.

### 2026-06-02 — MRVL

**Computex keynote confirmed NVLink Fusion live integration; Google assembles 4-partner chip supply chain at 35M unit scale by 2028** — Two major concept-level developments on June 2: (1) The Jensen Huang / Matt Murphy Computex keynote publicly demonstrated Marvell's NVLink Fusion integration — converting the March $2B NVIDIA investment into a live technical reference for hyperscale deployments. Every new custom AI silicon cluster adopting NVIDIA as the connective fabric now has a live Marvell blueprint. (2) The Next Web reports Google has formalized a four-partner chip supply chain: Broadcom (Sunfish training TPU), MediaTek (Zebrafish inference, 20-30% cheaper), Marvell (in talks: MPU + inference TPU), Intel (Xeon). Google projects 4.3M TPU shipments in 2026 → 35M by 2028 — an 8× ramp. At 35M units, even a minority Marvell program would represent billions of dollars in custom ASIC revenue. This is the clearest single data point confirming that custom silicon is not a niche trend but a volume production reality scaling at GPU-comparable rates. Source: Marvell.com / The Next Web, 2026-06-02.

### 2026-06-02 — MRVL

**FY2028 guidance corrected to $16.5B — faster than model implies in years 1–2** — Marvell's actual Q1 FY2027 earnings call guidance for FY2028 was $16.5B (not $15B as initially recorded). This means management is guiding ~50% YoY growth in FY2028, well above the Saturn DCF model's 25% 10-year CAGR. The model is conservative vs. management trajectory for years 1–3; the 25% long-run average reflects expected deceleration in years 4–10 as the custom ASIC market matures. Custom ASIC revenue: $1.5B annual run rate in FY2026, must double to $3B+ in FY2028 per management. Source: Sherwood News / TIKR / Seeking Alpha, confirmed 2026-06-02.

### 2026-06-02 — MRVL

**Jensen Huang calls MRVL "the next trillion-dollar company" — institutional validation raises floor price for custom silicon connectivity franchise** — MRVL surged +32.52% (biggest single-day gain ever) as Jensen Huang publicly endorsed Marvell at Computex, citing connectivity chips as essential infrastructure for AI data centers coordinating across thousands of chips. While not a DCF-relevant fundamental change, the CEO of the world's most valuable semiconductor company publicly anointing a co-design partner as "the next trillion-dollar company" creates durable institutional floor-price awareness. At $290.79, MRVL market cap is ~$253B — still ~4× below a $1T valuation. For the custom silicon concept: this validates that the co-design + connectivity layer is seen by NVIDIA itself as a parallel trillion-dollar infrastructure stack, not a zero-sum threat. Source: CNBC, 2026-06-02.

### 2026-06-04 — AVGO / TSM

**Broadcom Q2 FY2026: AI semiconductor revenue $10.8B (+143% YoY); Q3 guided $16.0B (+200% YoY) — custom silicon is now a multi-$10B-per-quarter reality at hyperscale** — Broadcom's June 3 earnings are the single most important third-party validation of the hyperscaler custom silicon thesis yet. Broadcom's AI semiconductor segment (Google Sunfish/Trillium TPUs, Meta MTIA custom ASICs) reached $10.8B in Q2 FY2026, growing 143% YoY, guided to $16.0B in Q3 (+200% YoY). At $16B per quarter annualizing to $64B, Broadcom's AI chip revenue now approaches NVIDIA's full data center run rate — confirming that custom ASICs are a parallel AI compute stack of comparable scale, not a niche phenomenon. For MRVL: Broadcom reached this scale in ~3 years from product commercialization; MRVL is on a similar trajectory 18–24 months behind (current ~$3B AI revenue/year, guided to $16.5B in FY2028). For TSMC: all Broadcom AI chips are manufactured at TSMC, adding $64B+ annualized to the validated AI demand floor beyond NVIDIA. Source: StockTitan / Broadcom SEC 8-K, 2026-06-03.

### 2026-06-05 — AVGO (thesis recalibration)

**Broadcom Q3 AI guidance miss ($16B vs $16.4–17.2B analyst est.) triggered a semiconductor selloff on June 4 but did NOT lower the custom silicon floor** — The market reaction (-14% AVGO, -7.7% MU, -5.6% MRVL, -4.8% ANET) reflects analyst expectations having run ahead of even Broadcom's own bullish case. The key data points: (1) Broadcom guided $16B for Q3, which is a +48% sequential increase from Q2's $10.8B — an extraordinary absolute figure; (2) Broadcom maintained its $100B AI chip sales target for calendar 2027 — no cut; (3) KeyBanc raised PT to $575 despite the selloff. The selloff is a valuation-regime reset (market expected $17.2B but got $16B), not a thesis cut. For the custom silicon concept: the AVGO guidance miss sets a more calibrated expectation ceiling — MRVL's $16.5B FY2028 target (full year) compares to AVGO's $16B single quarter — highlighting the scale gap MRVL must close. This gap is achievable on a 2–3 year ramp but not yet priced conservatively. The custom silicon thesis is intact; the risk is execution against very high embedded expectations. Source: Bloomberg / CNBC / 24/7 Wall St., 2026-06-04.

### 2026-06-03 — ALAB

**ALAB Computex: UALink support + CXL KV Cache second hyperscaler win + NVLink Fusion custom design win — connectivity layer now fully stack-agnostic** — Three material custom silicon disclosures from ALAB at Computex June 3: (1) Intelligent Connectivity Platform now formally integrates UALink™ alongside NVLink Fusion, PCIe, CXL, and Ethernet — ALAB becomes the only AI fabric provider certified for both NVIDIA (NVLink Fusion) and AMD/non-NVIDIA (UALink) ecosystems; (2) second custom CXL KV Cache design win with a new hyperscaler (unnamed), chips shipping 2027 — first CXL custom silicon win beyond Amazon, directly validating the 2027+ CXL memory pooling thesis; (3) NVLink Fusion custom silicon design win with NVIDIA + a hyperscaler, targeting hybrid rack deployments. Combined with the Amazon Trainium3 Scorpio X win, ALAB now has at least three separate custom silicon programs in progress across hyperscalers — ahead of management's year-end guidance of "a couple." UALink support is the single most important strategic disclosure: it confirms ALAB is not a captive NVIDIA ecosystem vendor but a neutral AI connectivity infrastructure company that gets paid regardless of which GPU architecture wins. Source: Astera Labs IR, 2026-06-03.

### 2026-06-06 — AVGO / Google

**Broadcom's Alphabet TPU share: 95% (2026) → 80% (2027) → 65% (2028) — Google's multi-vendor strategy quantified:** Reporting around the June 4-5 semiconductor selloff surfaced a key datapoint: Broadcom's revenue share for Alphabet's (Google) tensor processing units is expected to decline from ~95% in 2026 to 80% in 2027 and 65% in 2028, as MediaTek gains share with the Zebrafish inference chip (~20-30% cost advantage). For the custom silicon concept: (1) this confirms the June 2 finding (Marvell in talks for Google MPU + inference TPU) is being driven by real supplier diversification economics, not optionality; (2) Google is executing a deliberate multi-vendor strategy — Broadcom (Sunfish training TPU), MediaTek (Zebrafish inference), Marvell (MPU/inference TPU talks), Intel (Xeon infra) — consistent with hyperscaler incentives to commoditize silicon; (3) total Google TPU volume is simultaneously growing (35M units by 2028 per The Next Web, vs. 4.3M in 2026), so even a declining Broadcom share represents higher absolute unit volume; and (4) this is not AI demand destruction — it is supplier diversification on a growing pie. For MRVL: Marvell gaining share from Broadcom in Google's TPU supply chain is the single most important near-term revenue swing factor in the custom silicon portfolio. Source: TradingKey / Bloomberg / The Next Web, 2026-06-04 to 2026-06-05.

### 2026-06-09 — MRVL / QCOM

**Qualcomm enters data center custom ASIC market via ByteDance deal — fourth major chipmaker joins custom silicon space:** Qualcomm signed its "largest AI infrastructure deal to date" to supply custom ASICs to ByteDance for AI data center use, adding a fourth serious competitor to the custom silicon space alongside Broadcom (~60% market share), Marvell (~25%), and MediaTek. The deal validates that custom data center ASIC demand is large enough to attract new entrants from adjacent markets (Qualcomm was previously focused on smartphones/edge). ByteDance's selection of Qualcomm is NOT a defection from Marvell (no known prior Marvell-ByteDance relationship). For the custom silicon concept: (1) Qualcomm's entry increases competitive pressure on MRVL for future hyperscaler program wins, potentially capping MRVL's market share ceiling below the ~25–30% current estimate; (2) simultaneously, a fourth well-capitalized chipmaker entering the space further validates that custom ASIC demand is massive and multi-vendor; (3) MRVL's confirmed programs (Google, Amazon, Microsoft) are unaffected by this announcement. Source: 24/7 Wall St. / AI Weekly, 2026-06-09.

---

## Cross-links

- [[MRVL]] — primary co-design beneficiary; MRVL designs custom ASICs and provides optical scale-up interconnect
- [[ALAB]] — PCIe/CXL connectivity layer for hybrid racks in NVIDIA NVLink Fusion ecosystem; enables non-NVIDIA XPUs to interface with NVIDIA AI factory
- [[TSM]] — manufactures all custom silicon; additive demand on top of NVIDIA/AMD wafers
- [[NVDA]] — threatened at inference; maintains training dominance via CUDA; NVLink Fusion makes custom silicon NVIDIA-compatible rather than NVIDIA-competing
- [[ANET]] — custom silicon clusters still need networking infrastructure; Arista benefits
