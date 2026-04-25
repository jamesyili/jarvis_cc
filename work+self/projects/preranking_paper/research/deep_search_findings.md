# 2025–2026 Preranking Literature — Findings for "Alignment + Accuracy" Paper

**Source:** Deep-search agent run 2026-04-25
**Purpose:** Identify literature published since the team's 2024 lit-review cutoff that should be cited, contrasted, or defended against in the RecSys 2026 submission

## (i) MUST CITE — clearly relevant, almost certainly missing

**Wang, Zhang, Wang, Yang, Li, Yang, Wen, Jiang, Gai. "Learning Cascade Ranking as One Network" (LCRON). ICML 2025** (arXiv:2503.09492). Kuaishou. *Verified — ICML 2025 poster, deployed Jan 2025 on Kwai ad platform Matching + Pre-ranking stages.* Derives a **lower-bound probability that ground-truth items survive the cascade** as a unified surrogate, with stage-specific auxiliary losses driving the bound down. **This is the closest competitor to the team's "serving objective decomposition" framing** — same first-principles instinct, different decomposition (survival probability product, not alignment+accuracy). Failing to cite/distinguish this is the single biggest novelty risk.

**Wilm & Normann. "Identifying Offline Metrics that Predict Online Impact: A Pragmatic Strategy for Real-World Recommender Systems." RecSys 2025** (arXiv:2507.09566). OTTO. *Verified RecSys 2025.* Methodology for identifying offline metrics that align with online impact in session-based recsys, validated on large-scale e-commerce A/B tests. **Direct overlap with §5.1 (offline-to-online calibration via positive linear regression)**; reviewers will demand a comparison.

**Tong, Chen, Zhang, Wang, Pi, Li, Liu. "Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking" (HAP). WWW 2026** (arXiv:2603.03770). ByteDance/Toutiao. *Verified WWW'26.* Tackles gradient conflicts when training preranker on heterogeneous candidate pool (impressed + unimpressed + multi-source); proposes Gradient-Harmonized Contrastive Learning + Difficulty-Aware Model Routing. **Directly addresses the dual-distribution training problem the team flags in §5.2 ("throughput mismatch addressed by zeroing out excess batches")** — HAP offers a more principled approach reviewers will compare against.

**Zhao, Qi, Xu, Ma, Zhao, Mei, Xu, Hu. "A Hybrid Cross-Stage Coordination Pre-ranking Model for Online Recommendation Systems" (HCCP). WWW 2025 Companion** (arXiv:2502.10284). JD.com. *Verified WWW'25 Companion.* Multi-level unexposed-sample construction + Margin InfoNCE for preranking; reports +14.9% UCVR / +1.3% UCTR. **Direct competitor on the "alignment trained on unimpressed candidates" thesis.** Should be cited and contrasted.

**Yang, Yin, Engle, Zhuang, Leng. "MTMD: A Multi-Task Multi-Domain Framework for Unified Ad Lightweight Ranking at Pinterest." AdKDD 2025** (arXiv:2510.09857). *Verified AdKDD 2025.* Pinterest's own LWS paper from the ads side (cascaded ad recsys). **Same Pinterest, adjacent stage — citing it shows internal coherence and avoids reviewer "why isn't your own group cited" critique.**

## (ii) WORTH CITING — relevant adjacent

**Bi et al. "Generative Pseudo-Labeling for Pre-Ranking with LLMs" (GPL)** (arXiv:2602.20995, Feb 2026). *Verified arxiv; venue not yet confirmed.* LLM-generated content-aware pseudo-labels for unexposed items; +3.07% CTR in production. Adjacent to the team's "alignment on unimpressed pool" thesis from a label-generation angle.

**Kou, Sheng, Han, Zhao, Cheng, Zhu, Xu, Zheng. "AIF: Asynchronous Inference Framework for Cost-Effective Pre-Ranking"** (arXiv:2511.12934, Nov 2025). Likely Alibaba/Taobao. *Venue not confirmed (arxiv only).* Decouples interaction-independent computation from real-time prediction. Orthogonal (efficiency, not objective) but represents 2025 industrial preranking literature reviewers expect to see.

**"HA-PFD: Hardness-aware Privileged Features Distillation with Latent Alignment for CVR Prediction." KDD 2025**, ByteDance. *Verified KDD'25 via guyulongcs awesome-papers repo, primary source not directly fetched — confirm authors before citing.* Privileged-feature distillation with latent alignment, adjacent to the alignment-loss design choices in §4.2.

**Wang et al. (Kuaishou). "Scaling Laws for Online Advertisement Retrieval"** (arXiv:2411.13322). *Arxiv only.* Models the function from offline metrics to online revenue across cascade stages — adjacent to §5.1 calibration.

## (iii) ATTACK SURFACE — reviewer ammo for "not novel"

**LCRON (above) is the primary attack vector.** A reviewer could write: *"The authors claim a first-principles serving-objective decomposition for preranking, but Wang et al. (ICML 2025) already derived a lower-bound surrogate for ground-truth survival across the cascade and proved end-to-end optimality. The proposed alignment+accuracy split is one of several valid decompositions, not the unique first-principles one."* Counter requires explicit theoretical contrast: their exclusivity claim (§3) is about scalar surrogates of L₁ given fixed L₀, L₂ — LCRON jointly trains all stages, which is a different problem.

**On Ranking Consistency of Pre-ranking Stage (Gu et al., arXiv:2205.01289).** Pre-cutoff but the paper already cites adjacent work; a reviewer may push: *"Overlap@K is just RCS rebranded."* The team's Theorem 3.3 (overlap as the *unique* first-order surrogate) is the defense, but it has to be stated more sharply than current §6.

**HCCP (above)** could be used to argue the unimpressed-pool alignment idea is industry-standard 2025, not novel. Mitigation: position the contribution as the **theoretical justification** for what HCCP/RankFlow/[23] do empirically.

## Confidence notes

- ICML 2025, RecSys 2025, AdKDD 2025, WWW'25 Companion, WWW'26: **venue confirmed via official sources/arxiv landing pages.**
- HA-PFD KDD'25 surfaced via a third-party awesome-list repo only — verify primary citation before adding.
- GPL and AIF: arxiv-only; **don't cite as conference papers** without confirming.
- Did not surface a published 2025–2026 paper proposing an alignment+accuracy *exclusivity* claim in this exact form — the team's specific decomposition appears genuinely novel; the risk is positioning, not preemption.

## Sources

- [LCRON arxiv](https://arxiv.org/abs/2503.09492)
- [LCRON OpenReview ICML 2025](https://openreview.net/forum?id=fvmnx3OxTI)
- [Wilm & Normann RecSys 2025](https://arxiv.org/abs/2507.09566)
- [HAP WWW 2026](https://arxiv.org/html/2603.03770v1)
- [HCCP WWW 2025 Companion](https://arxiv.org/html/2502.10284)
- [MTMD AdKDD 2025](https://arxiv.org/abs/2510.09857)
- [GPL arxiv](https://arxiv.org/abs/2602.20995)
- [AIF arxiv](https://arxiv.org/pdf/2511.12934)
- [HA-PFD KDD 2025 (third-party listing)](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising)
- [Scaling Laws for Online Ad Retrieval](https://arxiv.org/pdf/2411.13322)
- [RecSys 2025 accepted contributions](https://recsys.acm.org/recsys25/accepted-contributions/)
