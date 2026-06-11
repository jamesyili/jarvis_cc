# Bibliography Diff — Existing 23 Refs vs Deep-Search Recommendations

**Generated:** 2026-04-25
**Inputs:** `paper_capture.md` (existing 23-ref bibliography) × `deep_search_findings.md` (9 deep-search recommendations)
**Match basis:** author + title (year alone insufficient given multi-Pinterest co-authors)

---

## (1) Confirmed additions — not in existing bibliography

Ordered MUST CITE → WORTH CITING. None of the 9 deep-search recommendations match any of the existing 23 refs by author+title, so all 9 are confirmed additions.

| # | Citation | Bucket | Why add (1 sentence) |
|---|---|---|---|
| A1 | **Wang et al. 2025 — "Learning Cascade Ranking as One Network" (LCRON), ICML 2025** (arXiv:2503.09492) | MUST CITE / ATTACK SURFACE | Closest competitor to the paper's first-principles serving-objective framing; failing to distinguish it (joint cascade training vs. fixed-L₀/L₂ scalar surrogate) is the single largest novelty risk. |
| A2 | **Wilm & Normann 2025 — "Identifying Offline Metrics that Predict Online Impact," RecSys 2025** (arXiv:2507.09566) | MUST CITE | Direct overlap with §5.1's positive-linear-regression calibration of offline-to-online metrics; reviewers will demand the comparison. |
| A3 | **Tong et al. 2026 — "Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking" (HAP), WWW 2026** (arXiv:2603.03770) | MUST CITE | Tackles the exact dual-distribution training problem the paper hand-waves in §5.2 (zero-out-excess-batches); HAP's Gradient-Harmonized Contrastive Learning is what reviewers will compare against. |
| A4 | **Zhao et al. 2025 — "A Hybrid Cross-Stage Coordination Pre-ranking Model" (HCCP), WWW 2025 Companion** (arXiv:2502.10284) | MUST CITE / ATTACK SURFACE | Direct competitor on the "alignment trained on unimpressed candidates" thesis; must cite to position the paper's contribution as the *theoretical justification* for what HCCP did empirically. |
| A5 | **Yang et al. 2025 — "MTMD: Multi-Task Multi-Domain Framework for Unified Ad Lightweight Ranking at Pinterest," AdKDD 2025** (arXiv:2510.09857) | MUST CITE | Pinterest's own ads-side LWS paper; omitting it invites reviewer "why isn't your own group cited" critique and damages internal coherence. |
| A6 | **Bi et al. 2026 — "Generative Pseudo-Labeling for Pre-Ranking with LLMs" (GPL)** (arXiv:2602.20995, venue not yet confirmed) | WORTH CITING | Adjacent to the alignment-on-unimpressed thesis from a label-generation angle; cite as arxiv only until venue confirms. |
| A7 | **Kou et al. 2025 — "AIF: Asynchronous Inference Framework for Cost-Effective Pre-Ranking"** (arXiv:2511.12934) | WORTH CITING | Orthogonal axis (efficiency, not objective) but represents 2025 industrial preranking literature; signals the lit-review currency reviewers expect. |
| A8 | **HA-PFD: Hardness-aware Privileged Features Distillation, KDD 2025** (ByteDance — verify authors before adding) | WORTH CITING | Privileged-feature distillation with latent alignment, adjacent to §4.2 alignment-loss design; hold pending primary-source verification. |
| A9 | **Wang et al. 2024 (Kuaishou) — "Scaling Laws for Online Advertisement Retrieval"** (arXiv:2411.13322) | WORTH CITING | Models offline-metric → online-revenue function across cascade stages; adjacent to §5.1 calibration framing. |

**Bonus surfaced by attack-surface analysis (not in deep-search's 9 but referenced):** Gu et al. 2022 — "On Ranking Consistency of Pre-ranking Stage" (arXiv:2205.01289). This is the RCS paper. Not in the existing 23 refs. **Strongly recommend adding** — the team's background doc already analyzes it as paper [2], and a reviewer will use it to argue "Overlap@K is just RCS rebranded." Theorem 3.3 (overlap as the unique first-order surrogate) is the defense, but the paper must cite Gu et al. to set up that defense.

---

## (2) Already cited — deep-search recommendations matching existing refs

**None.** No deep-search recommendation matches any of the 23 existing references by author+title. The deep-search returned all 2025–2026 literature (post-cutoff), and the existing bibliography is dominated by pre-2025 work plus two 2025+ Pinterest self-citations (Pan et al. KDD'25, Naikawadi et al. WWW'26).

---

## (3) Existing 23 refs — KEEP / RECONSIDER / LIKELY DROP

Scrutinizing for: padding, age (<2015 with no foundational status), and corroboration by 2025–2026 deep-search.

| Ref# | Citation (1-line) | Verdict | Reason |
|---|---|---|---|
| [1] | Cao et al. 2007 — Listwise LTR (ICML) | KEEP | Foundational listwise LTR, anchors §6 "specialize listwise to L₁". |
| [2] | Wang & Deep 2016 — DLRS | RECONSIDER | Vague title; verify what's being cited and whether it earns its slot. |
| [3] | Covington et al. 2016 — YouTube DNN (RecSys) | KEEP | Canonical multi-stage industrial ref. |
| [4] | Craswell et al. 2008 — cascade click model (WSDM) | KEEP | Foundational click-model cite supporting monotone I(·) assumption. |
| [5] | Pan et al. 2025 — Pinterest multi-embedding retrieval (KDD'25) | KEEP | Pinterest self-cite, retrieval-stage anchor. |
| [6] | Ferraro et al. 2018 — offline metrics + user behavior (REVEAL) | RECONSIDER | Workshop paper; check if it's load-bearing for §5.1 or padding. |
| [7] | Gilotte et al. 2018 — offline A/B testing (WSDM) | KEEP | Counterfactual eval anchor in §6. |
| [8] | He et al. 2014 — ad click prediction (ADKDD) | LIKELY DROP | Pre-2015 Facebook GBDT+LR paper; not load-bearing for any specific claim, looks like padding. |
| [9] | Herlocker et al. 2004 — evaluating CF (ACM TOIS) | LIKELY DROP | 22 years old; foundational only if §6 references it explicitly — confirm it's not vestigial. |
| [10] | Hinton et al. 2015 — distillation (NeurIPS workshop) | KEEP | Required KD anchor — §6 cites as [10]. |
| [11] | Järvelin & Kekäläinen 2002 — NDCG (ACM TOIS) | KEEP | Required NDCG anchor — explicitly tied to prefix-average reward model in §6. |
| [12] | Yu Li et al. 2021 — top-aware recommendation distillation (Information Sciences) | RECONSIDER | Information Sciences is journal-of-record, not RecSys-prestigious; verify it earns slot vs. RankDistil [17]. |
| [13] | Zhang et al. 2020 — Two-Tower preranking (CIKM) | KEEP | Two-tower preranking architectural anchor. |
| [14] | Liu 2009 — LTR foundations | KEEP | Required listwise LTR foundational reference. |
| [15] | Ma et al. 2018 — MMoE (KDD) | KEEP | Cited in §6 as the multi-task gating contrast. |
| [16] | Naikawadi et al. 2026 — Pinterest hybrid pointwise+pairwise (WWW'26) | KEEP | Pinterest self-cite, directly supports pairwise-loss design in §4.2. |
| [17] | Reddi et al. 2021 — RankDistil (AISTATS) | KEEP | Distillation-for-ranking anchor. |
| [18] | Song et al. 2023 — Rethinking Large-scale Pre-ranking System (arxiv) | KEEP | Recent preranking framing; same authors as [23] suggest a coherent line. |
| [19] | Tang & Wang 2018 — Compact Ranking Models with HP Distillation (KDD) | KEEP | Privileged-feature distillation anchor — pairs with the proposed HA-PFD addition (A8). |
| [20] | Wang et al. 2025 — KD-Based Recommendation Systems Survey (Electronics) | RECONSIDER | "Electronics" is MDPI; surveys are weak citation currency at RecSys. Replace with a stronger 2024–2025 KD-recsys reference if possible. |
| [21] | Zhe Wang et al. 2020 — COLD: Next Generation Pre-Ranking | KEEP | Industry preranking canon; team's own background doc references it heavily. |
| [22] | Yi et al. 2019 — Sampling-Bias-Corrected Neural Modeling (RecSys) | KEEP | SSB anchor, direct theoretical relevance. |
| [23] | Kai Zhang et al. 2024 — Full Stage Learning for Multi-Stage Systems (SIGIR) | KEEP | Most recent cascade-systems anchor pre-2025; pairs with HCCP (A4) and LCRON (A1). |

**Summary:** 17 KEEP, 4 RECONSIDER ([2], [6], [12], [20]), 2 LIKELY DROP ([8], [9]). If all four RECONSIDER + two LIKELY DROP are revisited and replaced by the 9 deep-search additions + Gu et al. RCS, the bibliography moves from 23 → roughly 27–30 refs with stronger 2025–2026 currency and tighter alignment to the paper's claims.

**Critical gaps:** the bibliography has zero 2025 ICML/RecSys/WWW preranking cites despite four such papers existing (LCRON, Wilm-Normann, HAP, HCCP). This is the most reviewer-visible weakness.
