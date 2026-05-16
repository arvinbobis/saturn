# NVIDIA Corporation (NVDA)

> The dominant AI training hardware company — every major AI model is trained on NVIDIA GPUs.
> In this portfolio, NVDA is tracked as both a holding and the primary demand signal for TSM and MU.

*Last updated: 2026-05-14 | Wisesheets data as of: not yet pulled*

---

## Overview

- **Business model:** Fabless semiconductor company. Designs GPUs and networking hardware; manufacturing outsourced entirely to TSMC. Revenue = hardware (GPUs, networking) + software/services (CUDA ecosystem, NIM, DGX Cloud).
- **Value chain position:** Sits between TSMC (manufacturer) and hyperscalers/enterprises (buyers). NVIDIA's data center revenue is the most direct demand signal for TSMC CoWoS capacity and Micron HBM.
- **Founded:** 1993, Santa Clara, California. HQ in Santa Clara.
- **Listed:** NASDAQ: NVDA
- **Scale:** ~36,000+ employees.
- **Market cap:** *(update)*

### Why NVDA Is in This Portfolio
NVIDIA is the clearest expression of the AI hardware buildout — it captures the largest margin at the system level. The CUDA software moat compounds independently of hardware, making switching costs extraordinarily high. Data center GPU demand is the single most important leading indicator for the rest of the satellite portfolio.

### CUDA Moat
CUDA (Compute Unified Device Architecture) is NVIDIA's GPU programming framework — released 2006, now deeply embedded into every major AI training framework (PyTorch, TensorFlow, JAX). 15+ years of developer tooling, libraries (cuDNN, NCCL, cuBLAS), and institutional knowledge. Re-implementing this ecosystem for a competitor's hardware is a multi-year undertaking even with unlimited resources. AMD ROCm is the closest alternative; it has improved but remains meaningfully behind CUDA in adoption and capability.

---

## Moat

### CUDA Ecosystem Lock-in
*(Populate: developer ecosystem depth, switching cost quantification, enterprise training pipeline lock-in)*

### Blackwell Architecture Performance Lead
*(Populate: H100 → H200 → Blackwell performance step-ups; competitive position vs. AMD MI-series; Google TPU, Amazon Trainium as custom silicon alternatives)*

### Supply Chain Relationships
NVIDIA has priority access to TSMC's most advanced nodes and CoWoS packaging capacity. These relationships took years to build and give NVIDIA structural supply advantages over competitors.

### Networking — InfiniBand and Ethernet
*(Populate: Mellanox acquisition; InfiniBand for GPU clusters; transition to Ethernet with Spectrum-X; Arista as complementary/competitive)*

---

## Financials

*(Pull from Wisesheets — note pull date when populating)*

**Segment note:** NVIDIA reports Data Center, Gaming, Professional Visualization, Automotive, OEM & Other. Data Center is the primary segment for this thesis — track it as % of total revenue.

---

## Revenue Segments

*(Update quarterly — Data Center absolute revenue and YoY growth is the critical number; Gaming secondary; extract Blackwell commentary from earnings)*

---

## Growth Drivers

*(Populate: Hyperscaler AI CapEx growth; Sovereign AI (government GPU buildouts); Enterprise AI adoption; Blackwell ramp; NIM/software revenue growth)*

---

## Risks

*(Populate: Hyperscaler custom silicon risk (Google TPU, Amazon Trainium taking share over time); Export controls to China (historically ~20% of data center revenue); AMD ROCm closing the gap; Valuation multiple compression; Supply constraints)*

---

## Catalysts

### Active Catalysts
*(Populate: Blackwell full ramp; NVLink/NVSwitch GB200 system adoption; Sovereign AI deals; China export waiver decisions)*

### Archived Catalysts
*(Move here once played out)*

---

## Monitoring Checklist

*(Quarterly: Data Center revenue absolute + YoY growth; Blackwell shipment commentary; Gross margin (supply mix signal); China revenue %; Management commentary on hyperscaler demand visibility; AMD competitive update; Leading for TSM/MU: any NVIDIA guidance revision is a 1–2 quarter forward signal)*

---

## Investment View

*(Populate: Valuation, WACC, DCF, Reverse DCF, Scenarios, Decision Log)*

### Decision Log

*(Append-only — no entries yet)*

---

## Cross-links

- [[TSM]] — sole manufacturer; Blackwell on N4/N3 + CoWoS; NVIDIA supply constrained by TSMC CoWoS
- [[MU]] — Blackwell requires HBM3E; Micron is a qualified supplier alongside SK Hynix
- [[ASML]] — upstream; NVDA demand drives TSMC EUV machine orders
- [[MRVL]] — Marvell designs custom ASICs that may partially substitute for NVIDIA GPUs at hyperscalers; complementary and competitive
- [[ANET]] — Arista networking connects NVIDIA GPU clusters; co-dependent
- [[HBM]] — Blackwell HBM3E requirement drives MU and SK Hynix HBM revenue
- [[cowos]] — TSMC CoWoS packages HBM onto Blackwell; was the binding supply constraint
