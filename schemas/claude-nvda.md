# NVIDIA — Hyperfocused Schema

## Investment Mandate

NVIDIA is the demand signal for the entire AI build-out. Every data point about NVIDIA revenue — quarterly earnings, guidance, product roadmap — propagates forward to TSMC (CoWoS capacity), Micron (HBM demand), Marvell (custom ASIC competition framing), and Arista (GPU cluster networking). NVIDIA is the portfolio's leading indicator, not just a portfolio position.

**Core thesis:** CUDA ecosystem creates 10+ years of software switching costs. The AI training and inference market is growing faster than any competing silicon can absorb. NVIDIA gets paid on every AI workload that runs on GPU.

---

## Standing Knowledge

### The CUDA Moat

- CUDA has been the standard GPU programming framework for 15+ years. The entire AI software stack (PyTorch, TensorFlow, JAX) is optimized for CUDA. Migrating to AMD ROCm or Intel OneAPI requires significant re-engineering — most teams won't.
- This software moat is what makes NVIDIA's position durable beyond individual GPU generations.

### Product Roadmap

- **Hopper (H100/H200):** AI training workhorse. Still dominant in deployed fleet.
- **Blackwell (B100/B200/GB200):** Current generation. Q1 FY2027 revenue dominated by Blackwell ramp. CoWoS packaging at TSMC. HBM3E from Micron (primary) and SK Hynix.
- **Vera Rubin:** Next generation. Full production 2H 2026. Jensen Huang has described a $1T Blackwell+Rubin order book.
- **NIM / DGX Cloud:** Software/inference platform — recurring revenue layer on top of hardware.

### Key Financials (from agent sessions)

- Q1 FY2027 (Feb–Apr 2026): Revenue $81.62B (+85% YoY) — record
- Data Center Q1 FY2027: $75.2B (+92% YoY)
- Q2 FY2027 guidance: $91B (consensus was $85–87B; beat guidance meaningfully)
- Non-GAAP EPS Q1: $2.39 (beat $1.79 estimate by 34%)
- FY year ends January. FY2027 = Feb 2026 – Jan 2027.
- Shares outstanding: ~24.5B (post-split adjusted)

### Hyperscaler Dependency

NVIDIA's data center revenue (~92% of total) is almost entirely hyperscaler CapEx. The $725B combined hyperscaler CapEx in 2026 is the demand floor. If hyperscaler CapEx decelerates, NVIDIA revenue decelerates disproportionately (GPU clusters are the highest-ASP item in the CapEx stack).

### Custom ASIC Risk

Google (TPU), Amazon (Trainium/Inferentia), Microsoft (Maia), Meta (MTIA) are all developing custom AI chips to reduce NVIDIA dependence, primarily for inference. Marvell co-designs many of these. Near-term (2024–2026) NVIDIA is gaining share even as custom ASICs ramp because the AI market is growing faster than any substitution. Monitor when custom ASIC inference volumes cross a meaningful threshold (~10–15% of hyperscaler inference workloads).

---

## Monitoring Checklist

**Every session:**
- [ ] Stock price move and news — NVDA is the portfolio's leading indicator; any major move reflects AI sentiment
- [ ] Hyperscaler CapEx news (Amazon, Microsoft, Google, Meta) — direct demand signal
- [ ] Custom ASIC competitive news (AMD MI series, Google TPU, Amazon Trainium)

**Quarterly (earnings — FY ends January):**
- [ ] Data Center revenue vs. prior quarter and YoY
- [ ] Q2/Q3 guidance vs. consensus — the most important single number for the portfolio
- [ ] Gross margin trend (high margins = pricing power intact)
- [ ] Blackwell/Vera Rubin supply chain commentary (TSMC CoWoS capacity)
- [ ] HBM supplier mix (Micron vs. SK Hynix share)

**Thesis-bearing triggers:**
- Hyperscaler reduces GPU orders → major Challenges signal
- Custom ASIC announced for training (not just inference) → Challenges thesis
- New GPU architecture announced ahead of schedule → Confirms
- NVDA enters new market with GPU compute (automotive, robotics) → Confirms

---

## DCF Notes

- **Uncertainty: High** — extraordinary growth embeds future expectations; CapEx deceleration or custom ASIC substitution reprices significantly
- **R&D amortization: 5 years** — GPU architecture IP (Blackwell, Rubin) has 2-year competitive lead; CUDA software amortizes longer
- **Fabless:** All manufacturing at TSMC; very high Sales-to-Capital ratio (~3x)
- **Tax rate:** ~13% (R&D credits and international structure)
- **Last DCF:** 2026-05-21 | IV $156.27 | MoS -28.4% | SELL/AVOID at $218.13
- **DCF sensitivity:** At 30% CAGR, IV ≈ $210; at 15% CAGR, IV ≈ $110. Price embeds >25% CAGR for 10 years.
