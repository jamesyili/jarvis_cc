# Deep Search v2 — Pinterest Publication Footprint (preranking / retrieval / ranking / distillation 2022–2026)

**Purpose.** Map Pinterest's own publication footprint that the LWS preranking paper (RecSys 2026 submission) sits inside, so reviewers see internal coherence with prior Pinterest work.

**Method.** Verified each citation via arxiv abstract page or DBLP. Only entries explicitly confirmed at Pinterest are listed; unverified labelled `[unverified]`.

---

## (1) Already cited in the paper's bibliography

Listed so we don't double-recommend.

- **[5] Fan, Lin, Chen, Deng, Xia, Yan, Li (2025).** *Synergizing Implicit and Explicit User Interests: A Multi-Embedding Retrieval Framework at Pinterest.* KDD '25. arxiv 2506.23060. Verified DBLP. Pinterest Homefeed retrieval — the paper's L₀ neighbor.
- **[16] Naikawadi, Xia, He, Zhou, Xia, Maheshwari, Huang, Deng, Li, Badani, Wang (2026).** *Improving Multi-Task Recommendations via Cross User Learning with a Hybrid Pointwise and Pairwise Ranking Loss.* WWW '26 Industry Track. Confirmed via paper-internal author list overlap; arxiv listing not yet surfaced (pre-conference). Same author cluster — Pinterest L₂ ranking.

---

## (2) Recommended additions, in priority order

### P0 — directly relevant; same Homefeed stack the preranking paper sits inside

**A. Xia, Eksombatchai, Pancha, Badani, Wang, Gu, Joshi, Farahpour, Zhang, Zhai (2023). TransAct: Transformer-based Realtime User Action Model for Recommendation at Pinterest. KDD '23.** arxiv 2306.00248; DOI 10.1145/3580305.3599918. Verified arxiv + ACM DL.
*One-liner.* Sequential model that injects realtime user-action sequences into Pinterest's Homefeed Pinnability ranker.
*Why cite.* This is the production L₂ ranker the preranking paper aligns *to*. Without citing TransAct, reviewers can't tell what "main ranker" means in this stack. **Must-cite.**

**B. Khandagale, Juneja, Agarwal, Subramanian, Yang, Wang (2025). InteractRank: Personalized Web-Scale Search Pre-Ranking with Cross Interaction Features. WWW '25 Industry Track.** arxiv 2504.06609. Verified arxiv.
*One-liner.* Two-tower preranker for Pinterest Search with engagement-based query-item cross interactions, optimized via a Unified Pre-Ranking Label.
*Why cite.* This is *Pinterest's published preranker* (Search side) — directly adjacent to the LWS Homefeed preranker. The current paper claims novelty in formalizing the alignment-vs-accuracy decomposition; positioning relative to InteractRank (which uses a single composite label rather than the separated alignment + accuracy structure) is essential. **Must-cite — this is the most awkward omission as currently drafted.**

**C. Yang, Yin, Engle, Zhuang, Leng (2025). MTMD: A Multi-Task Multi-Domain Framework for Unified Ad Lightweight Ranking at Pinterest. AdKDD '25.** arxiv 2510.09857. Verified arxiv.
*One-liner.* Two-tower MoE-based ad LWS unifying multiple domains (Homefeed, Search) and tasks (CTR/CVR/etc.).
*Why cite.* The ad-side counterpart of this paper's organic LWS. Demonstrates Pinterest has two parallel LWS workstreams converging on different design choices; explicitly contrasting "organic LWS aligns to L₂; ad LWS unifies tasks/domains" gives the paper a cleaner relative-positioning story. **Strong cite.**

### P1 — Pinterest production stack that the preranking paper inherits or feeds

**D. Xia, Joshi, Rajesh, Li, Lu, Pancha, Badani, Xu, Eksombatchai (2025). TransAct V2: Lifelong User Action Sequence Modeling on Pinterest Recommendation.** arxiv 2506.02267. Verified arxiv.
*One-liner.* Lifelong (16k+ actions) variant of TransAct deployed in Pinterest Homefeed L₂.
*Why cite.* Current state of the L₂ ranker at the time of the LWS experiments (Mar–Apr 2026 forward test set). Citing both TransAct and TransAct V2 dates the L₂ generation the alignment metric is targeting. **Cite alongside [A].**

**E. Agarwal, Badrinath, Bhasin, Yang, Botta, Xu, Rosenberg (2025). PinRec: Outcome-Conditioned, Multi-Token Generative Retrieval for Industry-Scale Recommendation Systems.** arxiv 2504.10507. Verified arxiv.
*One-liner.* Generative retrieval (L₀) deployed across Pinterest Homefeed, Search, Related Pins.
*Why cite.* Complementary to the existing [5] retrieval cite — together they characterize the L₀ space the LWS preranker filters from. Optional but tightens the L₀ characterization.

**F. Malreddy, Lawhon, Nookala, Mantha, Badani (2024). Improving feature interactions at Pinterest under industry constraints.** arxiv 2412.01985. Verified arxiv.
*One-liner.* Feature-interaction architecture lessons inside Pinterest Homefeed ranking under latency / GPU memory / reproducibility constraints.
*Why cite.* The preranking paper's training-objective choices live under the same industry constraints; citing this gives a direct precedent for "we made this design choice for production reasons." **Useful for §4 / §5 framing.**

### P2 — supporting context (older Pinterest lineage; lighter cite weight)

**G. Pancha, Zhai, Leskovec, Rosenberg (2022). PinnerFormer: Sequence Modeling for User Representation at Pinterest. KDD '22.** arxiv 2205.04507. Verified arxiv.
*One-liner.* Long-term user embedding learned via dense all-action loss; canonical Pinterest user representation.
*Why cite.* Establishes the user-representation lineage that feeds both retrieval and ranking towers. Optional; cite only if §2.1 wants a Pinterest-flavored "what L₂ uses as user features" sentence.

**H. Xu, Zhai, Rosenberg (2022). Rethinking Personalized Ranking at Pinterest: An End-to-End Approach. RecSys '22.** arxiv 2209.08435. Verified arxiv.
*One-liner.* End-to-end Homefeed ranking blueprint integrating PinnerFormer + realtime user actions.
*Why cite.* RecSys '22 — same venue as this submission. Citing it signals continuity of the Pinterest research line at RecSys. **Modest cite-weight, high venue-courtesy value.**

**I. Liu, Li, Sun, Li, Sun, Wang, Wu, Gao, Soares, Li, Liu, Li, Ji, Leng, Deshikachar (2025). Decoupled Entity Representation Learning for Pinterest Ads Ranking. RecSys '25.** arxiv 2509.04337. Verified arxiv + ACM DL.
*One-liner.* Upstream-downstream entity embedding paradigm for Pinterest ads ranking.
*Why cite.* Same venue (RecSys), prior year. Useful as a "Pinterest ads-side analog of upstream-downstream paradigm" comparator. Lower priority unless §6 wants ads-side scope.

**J. Chen et al. (2025). PinFM: Foundation Model for User Activity Sequences at a Billion-scale Visual Discovery Platform. RecSys '25.** arxiv 2507.12704. Verified arxiv + ACM DL.
*One-liner.* 20B-param transformer foundation model for user-activity sequences across Pinterest applications.
*Why cite.* If reviewers ask "how big is the L₂ teacher?", PinFM characterizes the upper-bound capacity Pinterest deploys. Optional context.

**K. Wang et al. (2024). Improving Pinterest Search Relevance Using Large Language Models. CIKM '24.** arxiv 2410.17152. Verified arxiv.
*One-liner.* LLM cross-encoder distilled into a lightweight servable model for Pinterest Search relevance.
*Why cite.* Most directly relevant Pinterest-internal *distillation* precedent — pairs naturally with the §6 KD discussion ([10],[12],[17],[19],[20] in the current paper are all non-Pinterest). Citing this proves Pinterest has a published distillation-into-light-model lineage. **Worth adding to §6 KD discussion.**

### Skipped (verified but lower fit)

- *OmniSearchSage* (Pinterest Search embeddings, WWW '24 Companion) — adjacent surface, not preranking. arxiv 2404.16260.
- *PinSage* (KDD '18) and *MultiBiSage* (2022) — graph retrieval; predates current pipeline framing.
- *ItemSage* (KDD '22) — shopping product embeddings; tangential.

---

## Suggested action

Add **A (TransAct), B (InteractRank), C (MTMD)** at minimum — these are the must-haves for "internal coherence with prior Pinterest work." Then **D (TransAct V2), F (Feature Interactions), K (LLM Search Relevance distillation)** to round out L₂ generation, industry-constraint precedent, and Pinterest distillation lineage. That brings the Pinterest self-cite count from 2 → 8 without padding — every addition has a specific positioning justification.

---

## Verifiable URLs

- TransAct: https://arxiv.org/abs/2306.00248 ; https://dl.acm.org/doi/10.1145/3580305.3599918
- TransAct V2: https://arxiv.org/abs/2506.02267
- InteractRank: https://arxiv.org/abs/2504.06609
- MTMD: https://arxiv.org/abs/2510.09857 ; https://www.adkdd.org/papers/mtmd:-a-multi-task-multi-domain-framework-for-unified-ad-lightweight-ranking-at-pinterest/2025
- PinRec: https://arxiv.org/abs/2504.10507
- Feature Interactions @ Pinterest: https://arxiv.org/abs/2412.01985
- PinnerFormer: https://arxiv.org/abs/2205.04507
- Rethinking Personalized Ranking (RecSys '22): https://arxiv.org/abs/2209.08435
- Decoupled Entity Representation (RecSys '25): https://arxiv.org/abs/2509.04337 ; https://dl.acm.org/doi/10.1145/3705328.3748098
- PinFM (RecSys '25): https://arxiv.org/abs/2507.12704 ; https://dl.acm.org/doi/abs/10.1145/3705328.3748050
- LLM Search Relevance (CIKM '24): https://arxiv.org/abs/2410.17152
- Synergizing Implicit/Explicit (already cited [5]): https://arxiv.org/abs/2506.23060 ; https://dl.acm.org/doi/10.1145/3711896.3737265
- DBLP James Li: https://dblp.org/search?q=james+li+pinterest
- DBLP Hedi Xia: https://dblp.org/search?q=Hedi+Xia+Pinterest
