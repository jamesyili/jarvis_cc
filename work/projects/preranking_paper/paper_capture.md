# Preranking Paper — Editing Notes (helping Hedi)

**Status:** In progress — capturing paper content + James's edits/notes
**Started:** 2026-04-25
**Target venue:** RecSys 2026 (per James — title page placeholder says Conference'17 but real submission target is RecSys)
**James's role:** Co-author + editor / pressure-tester for Hedi (lead author)

## Paper metadata

- **Title:** Alignment + Accuracy: A First-Principles Framework for Preranking
- **Informal name:** "Unimpressed LWS paper" (per James)
- **Authors (in order):** Hedi Xia, Dylan Zhou, Yali Bian, Yichu Zhou, Zili Li, Tianyou Wang, Bella Huang, Hongbo Deng, Piyush Maheshwari, Dafang He, Darren Reger, Bowen Deng, James Li — all Pinterest, San Francisco
- **Length:** 14 pages (ACM format)
- **CCS:** Information systems → Recommender systems; Learning to rank; Theory of computation → Machine learning theory
- **Keywords:** recommender systems, preranking, multi-stage ranking, cascade ranking, offline evaluation, knowledge distillation, serving objective

## What James has shared so far

Page coverage: **all 14 pages** captured (from 7 two-page screenshots labeled by the visible page indicator: 1, 3, 6, 7, 10, 11, 13). Each section heading below covers two consecutive pages.

### Pages 1–2 — Title, authors, abstract, Introduction

**Abstract (verbatim):**

> Prerankers in large-scale recommender systems must efficiently select candidates for a downstream ranker while remaining aligned with its serving behavior. In practice, teams combine accuracy metrics with heuristic alignment losses, yet the choice of what these quantities should target—and how they should combine—is largely ad-hoc.
>
> Starting from a formal serving objective in a three-stage pipeline (retrieval, preranking, main ranking), we decompose the preranking objective into *alignment* and *accuracy*. Under mild assumptions, this decomposition is (i) *exclusive*—no third independent scalar component is needed, (ii) *approximately linear*, justifying the ubiquitous practice of linear metric and loss combinations, and (iii) *target-identifying*—alignment should track overlap with the main ranker's selections, and accuracy should track conditional engagement above a shared ranker threshold, narrowing the large design space of possible surrogates.
>
> We test each prediction in a large-scale industrial recommender system. A calibrated linear combination of the two metrics significantly improves offline–online correlation and experiment winner prediction over the accuracy-only metrics previously used in production. The corresponding two-part training objective outperforms both an accuracy-only preranker and our heuristic alignment+accuracy production model in multiple A/B tests. Although developed for preranking, the decomposition applies to any intermediate filtering stage in a cascade system.

**Introduction key claims:**

1. Multi-stage pipelines: retrieval → preranking → main ranking → post-ranking. Preranker filters under tight latency.
2. Two requirements on preranker: (a) accuracy on local engagement labels, (b) alignment with eventual full-ranking behavior. Mismatches → wasted capacity.
3. Industry practice today: combine multiple offline metrics + multiple training losses heuristically. Offline pattern: one accuracy metric (AUC, log loss, NDCG on click) + one or more alignment metrics (score correlation, top-K overlap, replay-based KPI). Training: linear/heuristic combinations + alignment losses (often KD).
4. **Three open questions:**
   - (1) What kinds of quantities are fundamentally needed? Is alignment+accuracy enough, or are practitioners ignoring an independent component?
   - (2) How should these quantities be combined? Linear is ubiquitous but has little theoretical justification.
   - (3) What should alignment and accuracy actually target? Within the large design space, which surrogates are theoretically justified vs merely convenient?
5. **Three theoretical insights** (their answers):
   - **Exclusivity.** Apart from orthogonal considerations like diversity/fairness, no third independent scalar type is needed. Any scalar surrogate respecting their assumptions lies, up to approximation error, in the 2D space spanned by alignment + accuracy.
   - **Linearity.** Serving objective is *(locally) linear* in the alignment and accuracy components. First-order, linear combinations are not just convenient but structurally correct.
   - **Target identification.** Alignment should measure overlap with main ranker; accuracy should measure conditional engagement above a shared ranker threshold. They derive ideal targets and construct practical offline metrics + training losses as approximations.
6. **Two practical contributions:**
   - Two-metric *evaluation scheme* (M_align + M_acc) — calibrate via positive linear regression of online lift on (M_align, M_acc) → single calibrated score.
   - Two-part *training objective* L = λL_align + (1-λ)L_acc reusing existing accuracy branch + adding alignment branch. Mixture λ from offline experiments.

### Pages 3–4 — Background and Problem Setup

**§2.1 Multi-stage recommendation pipeline.** Standard 4-stage view:
1. Candidate retrieval (L₀): nearest-neighbor over corpus.
2. Preranking (L₁): scores each item in D(u), keeps top-k as C(u).
3. Full ranking (L₂): expensive scoring of each e ∈ C(u).
4. Post-ranking arrangement: blending/diversification/business rules.

**§2.2 Simplified mathematical model: L₀, L₁, L₂.** Three-stage abstraction; post-L₂ mixing/rules omitted. Notation:
- L₀ retrieves D (= D(u) at fixed u).
- L₁ assigns score L₁(e) ∈ ℝ to each e ∈ D, keeps top-k by this score → C := {e ∈ D : L₁(e) is among top-k scores}.
- L₂ scores each e ∈ C and induces a total order on C.

Page 3 also begins **§2.3 Current practice: metrics and losses for preranking** — accuracy metrics (pointwise/pairwise on engagement labels: AUC, log loss, NDCG on click/watch labels) and alignment metrics (correlation between L₁ and L₂ scores, top-k overlap, replay-based KPI). Composite-score practice + alignment-loss practice are noted as effective but lacking theoretical foundation. Three open questions restated.

### Pages 5–6 — Theoretical Decomposition (§3.1–§3.5)

**§3.1 Reward decomposition.** Define I(i) = impression probability for position i (monotone profile: I(1) ≥ I(2) ≥ ... ≥ I(k) ≥ 0). Expected user reward R(s₁,...,s_k) = Σᵢ E(s_i)I(i). They rewrite as a *nonnegative linear combination of prefix-average engagements*:

> S_p := (1/p) Σᵢ₌₁ᵖ E(s_i),   p = 1,...,k
> Proposition 3.1: R(s₁,...,s_k) = Σ w_p S_p, where w_p := p(I(p) - I(p+1)) ≥ 0.

The prefix-level view is the basis of the alignment–accuracy machinery.

**§3.2 Alignment–accuracy decomposition.** Compare two prerankers L₁⁰ (baseline) and L₁ᴱ (experimental), same L₂. For each prefix p, let

> S_p⁰ := (1/p) Σᵢ E(s_i⁰),  S_pᴱ := (1/p) Σᵢ E(s_iᴱ)

denote prefix-average engagement of the top-p items of (L₁⁰,L₂)- and (L₁ᴱ,L₂)-induced final lists. Goal: understand S_pᴱ - S_p⁰. Introduce intermediate Š_p (item at position p under baseline full ranking; consider L₂ score threshold L₂(s_p⁰)). Define

> p̂ := |{s_iᴱ : L₂(s_iᴱ) ≥ L₂(s_p⁰)}|   (count among experimental top-p whose L₂ scores beat baseline threshold)
> Š_p := (1/p̂) Σᵢ₌₁^p̂ E(s_iᴱ)

**Proposition 3.2 (Prefix-level alignment–accuracy decomposition):** S_pᴱ - S_p⁰ = (S_pᴱ - Š_p) + (Š_p - S_p⁰)

The first piece (alignment term Ali_p) captures how the preranker shifts the effective main-ranker cutoff; the second piece (accuracy term Acc_p) captures quality differences among items above a common main-ranker threshold.

> Ali_p := S_pᴱ - Š_p,   Acc_p := Š_p - S_p⁰

**§3.3 Alignment is first-order linear in overlap.** Define overlap Op^m := |Cᵐ ∩ X_p^0| (m ∈ {0, E}). By construction, O_p^0 = p and O_pᴱ = p̂, so the cutoff shift equals overlap difference: p̂ - p = O_pᴱ - O_p⁰.

**Theorem 3.3 (Alignment is linear in overlap):** Under local smoothness, Ali_p = c_p (O_pᴱ - O_p⁰) + R_p, with local coefficient c_p and remainder satisfying |R_p| ≤ C_p(O_pᴱ - O_p⁰)²/p². Proof via Taylor expansion (Appendix A).

**§3.4 Accuracy is conditional engagement above a shared threshold.**

> Acc_p = (Σ_{e∈Cᴱ∩X_p⁰} E(e) / |Cᴱ ∩ X_p⁰|) - (Σ_{e∈C⁰∩X_p⁰} E(e) / |C⁰ ∩ X_p⁰|)

To estimate from logs: let X̂_p ⊆ X_p⁰ be a sample of items with high L₂ scores and Ŷ_p ⊆ X̂_p those with positive engagement. For each m ∈ {0, E}, define normalized engagement proxy N_p^m := Σ_{x∈Ŷ_p} P(x ∈ Cᵐ) / Σ_{x∈X̂_p} P(x ∈ Cᵐ). Use N_pᴱ - N_p⁰ as offline proxy for Acc_p.

**§3.5 Alignment–accuracy representation of reward lift.** Sum prefix contributions to global reward lift:

> Rᴱ - R⁰ = Σ w_p (S_pᴱ - S_p⁰) = Σ w_p Ali_p + Σ w_p Acc_p

**Theorem 3.4 (Alignment–accuracy representation of reward lift):**

> Rᴱ - R⁰ = Σ α_p (O_pᴱ - O_p⁰) + Σ β_p (N_pᴱ - N_p⁰) + R
> α_p = w_p c_p, β_p = w_p d_p

i.e., online reward lift = linear combination of alignment proxies (overlap differences) + accuracy proxies (conditional engagement differences) + remainder.

### Pages 7–8 — Offline metric/loss design (§4.1–§4.3) + Experiments (§5)

**Figure 3: Three-way parallel decomposition** across theory / evaluation / training. Same equation shape:
- **Theory (Section 3):** Total = Accuracy + Alignment
- **Evaluation:** Calibrated predictor M̂ = α·M_align + β·M_acc, weights from positive linear regression on online lift. M_align operationalized as **hits@K with overlap-at-fraction-ρ** on impressed traffic; M_acc remains hits@K accuracy on impressed.
- **Training:** Total Loss = L_acc (accuracy on impressed) + L_align (alignment on **unimpressed** candidate pool)

The structural point: **accuracy side reuses the existing production baseline. Alignment side is the novel contribution — and it operates on UNIMPRESSED candidate pool.**

**§4.1 Offline alignment/accuracy metrics:**
- *Accuracy metric (baseline, unchanged):* hits@K on user-impressed data — items the user actually saw.
- *Alignment metric (theory-guided new):* score agreement between L₁ and L₂ on the preranker output pool C(u) — using overlap-at-fraction-ρ. Sample requests, subsample C(u) (~5%), get L₂ scores for each kept item, compute preranker score for each L₁ variant. For ρ ∈ (0,1) (default ½), form set of top-ρ fraction by L₁ on subsample; intersect with set of top-ρ fraction by L₂. Aggregate by mean overlap per request on **unimpressed traffic** so metric does not depend on what items were actually shown.

Why alignment cannot reuse impressed distribution: data distributions are fundamentally different. Restricting to impressed reweights toward seen positions and mixes in exposure effects; doesn't recover offline counterpart of Ali_p. Why overlap, not other surrogates: Theorem 3.3 narrows the choice to overlap differences specifically — not score correlation, NDCG with L₂ scores as labels, Kendall-τ.

**§4.2 Alignment / accuracy training losses:**
- *Accuracy losses (baseline, unchanged):* BCE + pairwise loss on impressed; computed across users, sum L_acc.
- *Alignment losses (new):* on the same unimpressed distribution as the alignment metric, add KL-divergence distillation + weighted pairwise term against the main ranker. L_align = L_align-kl + L_align-pair. KL branch matches preranker softmax distribution to teacher's over candidate set. Pairwise branch: fix a request and let i,j index items from preranker output pool that appear in the same minibatch. Use σ as sigmoid. Use L̃₁ and L̃₂ obtained by batch-normalizing raw preranker logits and transformed main-ranker scores. With nonnegative weights w_{ij}:

> L_align-pair := Σ w_{ij} (-log σ(L̃₁(i) - L̃₁(j))) σ(L̃₂(i) - L̃₂(j))

The factor -log σ(L̃₁(i) - L̃₁(j)) is pairwise logistic pressure. The factor σ(L̃₂(i) - L̃₂(j)) is teacher's smooth probability that i ranks above j. Strong teacher preferences → upweighted pairs; near-tied teacher preferences → downweighted (mirrors the L₂-decisive vs near-tied structure in the head of the L₂ ordering).

**§4.3 Combined offline score and training objective.** Calibrated predictor:
> M̂ := α M_align + β M_acc, α,β ≥ 0 fit by positive linear regression: each historical/toy experiment contributes (M_align, M_acc, Δy), Δy = observed online lift in save engagement.

Multi-K expansion: M̂ = Σₖ α_k M_align^{(k)} + β M_acc, weights ≥ 0. Sparsity regularization implicit: nonneg LSQ produces sparse solutions.

What theory rules out: adding a third metric should not improve prediction beyond α·M_align + β·M_acc. Tested explicitly in §5.4.

Training combines two loss branches via mixing coefficient λ ∈ (0,1):
> L := λ L_align + (1-λ) L_acc

§5 Experiments evaluates: (i) whether learned linear combo of M_align and M_acc predicts online preranker lift better than existing offline baselines; (ii) whether training objective improves live metrics over strong production baselines. L₂ + retrieval held fixed.

**§5.1 Offline metric calibration (M̂ vs. baselines).** Goal: quantify how well scalar offline scores predict online experiment winners and lift magnitudes across many past + future experiments.

Splits: fit (α,β) on training set of 51 models drawn from 4 experiments run between July and December 2025. Freeze (α,β); evaluate on held-out **forward test set** of 20 models from 3 experiments run between March and April 2026 — *temporal gap that tests robustness to distribution shift.*

### Pages 9–10 — Results, A/B tests, ablations, related work

**Table 1: Offline metric calibration on the forward test set** (20 models, 3 experiments, Mar–Apr 2026). Training: 51 models from 4 experiments (Jul–Dec 2025). "Direction incorrect" = negative Spearman correlation.

| Scoring rule | Winner acc. | Spearman ρ |
|---|---|---|
| Unimp. forecast | 80% | 0.871 |
| Unimp. overlap | 80% | 0.867 |
| Imp. forecast | 70% | 0.862 |
| Imp. overlap | 70% | 0.860 |
| NE | 50% | 0.482 |
| PR-AUC | 50% | dir. incorrect |
| ROC-AUC | 45% | dir. incorrect |

Seven scoring rules grouped by (a) whether alignment is computed on theoretically-motivated unimpressed vs impressed, (b) whether accuracy uses forecasted engagement metric or overlap surrogate.

- **Unimp. forecast:** M̂ = αM_align^{unimp} + βM_acc^{forecast}, alignment on unimpressed with forecasted accuracy.
- **Unimp. overlap:** M̂ = αM_align^{unimp} + βM_acc^{overlap}, alignment on unimpressed with overlap-based accuracy.
- **Imp. forecast / Imp. overlap:** alignment on impressed traffic.
- **NE / PR-AUC / ROC-AUC:** accuracy-only baselines.

Key result: switching alignment from impressed → unimpressed raises winner accuracy 70% → 80%, Spearman ρ −0.86 → −0.87 (validates Section 3 prediction that alignment should be measured on the preranker's full candidate pool, not the biased subset that survived to impression). Forecast vs overlap accuracy: nearly identical performance — choice of accuracy surrogate matters far less than choice of data distribution for alignment.

Alignment is **load-bearing.** All four combined metrics (≥ 70% accuracy, ρ ≥ 0.860) dramatically outperform three accuracy-only baselines. NE achieves only chance-level winner prediction (50%) with weak correlation (ρ=0.482); PR-AUC and ROC-AUC predict winner direction *incorrectly* — models that improve online engagement may actually decrease these accuracy scores.

**Figure 5:** offline metric vs online lift for 20 test models. Left: unimp. forecast (M̂); points cluster along positive trend, metric correctly predicts lift vs drop for 80% of models. Right: NE; weak relationship, frequently assigns higher scores to models that hurt online engagement.

**§5.2 Alignment metric and pairwise-loss implementation:**
- *Logged scores and subsampling:* §4.1 metric uses request and within-C(u) subsampling rates stated there (~5% of requests and ~5% of items per kept request unless infrastructure dictates). All L₂ scores are logged from serving path for subsampled items.
- *Batch normalization in the alignment branch:* raw main-ranker scores are nonnegative; before they enter pairwise loss, apply batch normalization to log(raw L₂) so teacher logits are at single scale across minibatches. Raw preranker outputs are already logits; apply batch normalization to raw L₁ without taking log.
- *Pair weights w_{ij}:* hyperparameters. In runs they set w_{ij} = 1/|C(u)|, where |C(u)| = preranker output size for the request from which j contributes — comparable total mass regardless of |C(u)|.
- *Dual-distribution training infrastructure:* alignment and accuracy losses operate on fundamentally different data distributions (unimpressed candidate pool vs impressed traffic), requiring separate data ingestion paths in production. They use a trainer-side union of two independently calculated datasets rather than pre-merged dataset, allowing mixing ratio to be tuned as a hyperparameter. Throughput-mismatch addressed by zeroing out excess batches at the loss stage; details in Appendix B.

**§5.3 Live A/B tests** — homefeed surface, 2 weeks per arm, 2% traffic per arm. Same inference architecture across arms; only training objective differs. Two engagement actions tracked: save (user bookmarks) + content view (user views full content; lighter engagement). All guardrail metrics (weekly active users, hide rate, report rate, others) neutral in every experiment.

**Table 2: Training configurations.**

| Arm | Accuracy | Alignment loss | Align. data |
|---|---|---|---|
| B1 | L_acc | — | — |
| B2 | L_acc | KL | funnel |
| T | L_acc | KL + pairwise | unimp. |
| T_KL | L_acc | KL | unimp. |
| T_MSE | L_acc | MSE | unimp. |

B1, B2 = production baselines; T = proposed model; T_KL, T_MSE = ablations varying alignment loss form while holding unimpressed data fixed.

**Table 3: Live A/B test results** (two weeks, 2% traffic per arm, homefeed).

| # | Comparison | Save | Content view |
|---|---|---|---|
| 1 | T vs. B1 (accuracy-only) | +1.43% | -0.55% |
| 2 | T vs. B2 (heuristic align.) | +0.62% | -0.97% |
| 3 | T vs. T_KL (ablation) | +1.43% | ntrl |
| 4 | T vs. T_MSE (ablation) | +3.17% | +5.79% |

All non-neutral effects p < 0.001; "ntrl" = not statistically significant.

Main: T over B1 = +1.43% save (-0.55% content view); T over B2 = +0.62% save (-0.97% content view) — both directions consistent with theory. Switching alignment from impressed → unimpressed (per Section 4) improves preranker contribution to downstream engagement, even though B2 already performs KL distillation.

Efficient pairwise alignment loss: naive pairwise alignment on batch of B items requires O(B²); with B ≈ 42,000 prohibitively memory-intensive. They exploit the fact valid pairs must share same request (k ≤ 100 items) → use hash-based sorting and block-diagonal scanning to reduce cost to O(B(k + log B)). Appendix C.

**§5.4 Ablations and robustness:**
- *Alignment loss form (rows 3–4):* unimpressed data fixed, vary only alignment loss. KL-only distillation (T_KL) lacks ordering structure: pairwise term adds +1.43% save at no content-view cost. MSE distillation (T_MSE) performs worst (-3.17% save, -5.79% content view) — pointwise score matching wastes capacity on scale calibration irrelevant to the preranker's selection task. Loss form ranking pairwise > KL > MSE consistent with overlap-motivated alignment term in Theorem 3.3.
- *Alignment data distribution:* Table 1 offline comparison: switching from impressed → unimpressed raises winner accuracy 70% → 80%, ρ −0.86 → −0.87. Online comparison (B2 vs T row 2): replacing funnel-log distribution with unimpressed candidate pool lifts save by 0.62%.
- *Linearity, exclusivity, metric sensitivity:* offline calibration dataset (51 training + 20 test models across 7 experiments) too small to compare nonlinear calibrators or test whether a third metric improves prediction beyond the alignment–accuracy pair. Left to future work.

**§6 Related Work:**
- *Multi-stage ranking & preranking:* references (industrial cascades, two-tower → interaction-enhanced designs, computation-aware adaptive allocation). Most published work emphasizes architecture/efficiency; few focus on formalizing how preranking objective relates to downstream serving quality.
- *Offline evaluation & metric combination:* cumulated-gain metrics (NDCG) formalize position-weighted utility behind their prefix-average reward model. Learning weights over multiple offline metrics has been explored in specific products. Offline A/B testing methods can estimate policy value from logs without [continues on page not shown].

### Pages 11–12 — Conclusion, References, Appendix A (Theoretical Details)

**§6 Related Work (continued from page 10):**
- Many teams still treat one metric as the primary objective and the other as a guardrail when tradeoffs appear. We use a *two-dimensional structure* (alignment vs. accuracy) tied directly to a serving objective, which motivates both the choice of metrics and their calibrated combination into a single predictor of online lift.
- *Knowledge distillation and cross-stage training.* KD [10] from teacher ranker to student is standard in recommendation and search [12, 17, 19, 20]. Multi-task and multi-objective formulations like MMoE [15] address the challenge of combining heterogeneous objectives within a single model, typically via shared-bottom or gated architectures. Their alignment losses are instances of the distillation paradigm; the contribution is tying them to a formal alignment term derived from the serving objective and pairing them with an *unchanged* accuracy branch, rather than proposing a new distillation architecture or multi-task gating mechanism.
- *Position bias and impression models.* Reward formulation assumes monotone impression profile I(1) ≥ I(2) ≥ ..., consistent with examination hypotheses in click models [4]. The alignment–accuracy decomposition does not require a specific parametric form for I(·); monotonicity suffices.
- *Learning-to-rank theory.* Listwise LTR [1, 14] often starts from a scalar reward on ordered lists; their prefix-based reward rewrite and alignment–accuracy decomposition specialize that viewpoint to the preranker stage L₁ in a fixed retrieval (L₀) and main-ranker (L₂) pipeline. To their knowledge, prior work does not state an exclusivity-style claim for the preranking objective or connect overlap surrogates to main-ranker cutoff shifts in this pipeline as in Section 3.

**§7 Conclusion:**

> We studied preranking in multi-stage recommenders, where systems must optimize both engagement prediction and agreement with the main ranker. Starting from a formal serving objective, we showed how reward lift decomposes into alignment and accuracy components, justified linear combinations of proxies under mild assumptions, and identified overlap and conditional-engagement quantities as practical targets.
>
> We preserved the production accuracy metric (hits@k on impressed data) and accuracy losses (BCE and pairwise on impressed logs), and added a theory-guided alignment metric (overlap@k on unimpressed main-ranker inputs) and alignment distillation losses, using distinct data distributions where the theory calls for them. A learned linear offline score and a linearly combined training objective improved offline–online agreement and outperformed accuracy-only and heuristic alignment baselines in large-scale experiments.
>
> Future work includes tighter estimators for the accuracy term under impression and selection bias, per-segment coefficients in (8), and extensions to more than two ranking stages or to diversity and fairness constraints treated alongside alignment and accuracy.

**References (23 total).** Notable for citation/positioning purposes:

[1] Cao et al. 2007 Listwise LTR (ICML); [2] Wang & Deep 2016 (DLRS); [3] Covington et al. YouTube 2016 (RecSys); [4] Craswell et al. cascade click model 2008 (WSDM); **[5] Pan, Lin, Chen, Deng, Hedi Xia, Yuke Yan, James Li 2025 — "Synergizing Implicit and Explicit User Interests: A Multi-Embedding Retrieval Framework at Pinterest" (KDD'25)**; [6] Ferraro et al. offline metrics + user behavior 2018 (REVEAL); [7] Gilotte et al. offline A/B testing 2018 (WSDM); [8] He et al. 2014 ad click prediction (ADKDD); [9] Herlocker et al. 2004 evaluating CF (ACM TOIS); [10] Hinton et al. 2015 distillation (NeurIPS workshop); [11] Järvelin & Kekäläinen 2002 cumulated gain NDCG (ACM TOIS); [12] Yu Li et al. 2021 top-aware recommendation distillation (Information Sciences); [13] Zhang et al. 2020 Two-Tower for preranking (CIKM); [14] Liu 2009 LTR foundations; [15] Ma et al. MMoE 2018 (KDD); **[16] Naikawadi, Hedi Xia, Dafang He, Yichu Zhou, Xue Xia, Piyush Maheshwari, Bella Huang, Bowen Deng, James Li, Dhruvil Deven Badani, Yijie Dylan Wang 2026 — "Improving Multi Task Recommendations via Cross User Learning with a Hybrid Pointwise and Pairwise Ranking Loss" (WWW'26 Industry Track)**; [17] Reddi, Merchant, Jain, Haque, Suggala 2021 RankDistil (AISTATS); [18] Yang Song, Haijun Zhao, Rui Huang, Beichuan Zhang, Na Mou, Yanan Niu, Kai Zheng, Hongning Wang, Kun Gai 2023 Rethinking Large-scale Pre-ranking System (arxiv); [19] Tang & Wang 2018 Compact Ranking Models with HP Distillation (KDD); [20] Wang et al. 2025 KD-Based Recommendation Systems Survey (Electronics); [21] Zhe Wang, Liqin Zhao, Biye Jiang, Guorui Zhou, Xiaoqiang Zhu, Kun Gai 2020 — COLD: Towards Next Generation of Pre-Ranking System; [22] Yi, Hong, Zhuyun Cheng, Lukasz Heldt, Aditee Kumthekar, Zhe Zhao, Li Wei, Ed Chi 2019 Sampling-Bias-Corrected Neural Modeling for Large Corpus Item Recommendations (RecSys); [23] Kai Zhang, Haijun Zhao, Rui Huang, Beichuan Zhang, Na Mou, Yanan Niu, Yang Song, Hongning Wang, Kun Gai 2024 Full Stage Learning for Multi-Stage Systems: A Unified Framework (SIGIR).

**Appendix A — Additional Theoretical Details:**
- A.1 Exact alignment identity: Proposition A.2 — Ali_p = ((p̂-p)/p̂)(S_pᴱ - ∂S_p), with convention Ali_p = 0 when p̂ = p. Proof handles cases p̂ > p and p̂ < p separately.
- A.2 Local smoothness assumption: Assumption 1 (continuously differentiable g_p, |g_p'(t)| ≤ M_p in neighborhood of p). Engagement of items as a function of position in main-ranked list is locally smooth around prefix p — engagements vary gradually with rank.
- A.3 First-order approximation of alignment: Theorem A.3 — Under Assumption 1 and small |Δ_p|, Ali_p = c_p Δ_p + R_p, where c_p := (1/p)(S_pᴱ - E(s_p^E)), |R_p| ≤ C_p (Δ_p²/p²). Equivalently, Ali_p = c_p(p̂ - p) + O((p̂-p)²/p²).

### Pages 13–14 — Appendix A.3 cont., A.4, A.5, B, C, Figure 6

**Appendix A.3 (cont.) — Proof sketch of Theorem A.3.**
By the exact identity, `Ali_p = Δ_p / (p + Δ_p) · (S_p^E - ∂S_p)`. From Assumption 1, the boundary average satisfies `∂S_p = E(s_p^E) + O(|Δ_p|)` because it is an average of `g_p(i)` over an interval of length |Δ_p| adjacent to p. A Taylor expansion of g_p and the bounded-derivative condition imply that the difference between ∂S_p and E(s_p^E) is at most O(|Δ_p|). Similarly, `Δ_p / (p + Δ_p) = Δ_p/p + O(Δ_p²/p²)` whenever |Δ_p| ≪ p. Combining: `Ali_p = (Δ_p/p)(S_p^E - E(s_p^E)) + O(Δ_p²/p²)`.

Connecting Δ_p to the overlap quantity of Section 3: recall `X_p^0 := {e ∈ D : L_2(e) ≥ L_2(s_p^0)}` is the baseline L₂-threshold set; `O_p^m := |C^m ∩ X_p^0|` is the overlap between preranked candidates of model m ∈ {0, E} and X_p^0. Since O_p^0 = p and O_p^E = p̂, we get **`Δ_p = O_p^E - O_p^0`**. Substituting into Theorem A.3 yields the overlap-based form of Theorem 3.3.

**Corollary A.4 (Alignment–overlap approximation):** Under Assumption 1, `Ali_p = c_p(O_p^E - O_p^0) + R_p`, with `|R_p| ≤ C_p(O_p^E - O_p^0)² / p²`.

**§A.4 Consistency of the accuracy estimator.**
Population view across requests. Let u_1,...,u_n be i.i.d. requests; for each u_t, let D_t be its candidate set. For each t, define baseline threshold set `X_{p,t}^0 := {e ∈ D_t : L_2(e) ≥ L_2(s_{p,t}^0)}` and corresponding preranked candidates C_t^0 and C_t^E. Let Y_t(e) ∈ [0,1] denote observed engagement label under u_t. Assume `E[Y_t(e) | u_t, e] = μ_t(e)`. Per-request accuracy estimand:

> A_{p,t} := Σ_{e∈C_t^E∩X_{p,t}^0} μ_t(e)/|C_t^E ∩ X_{p,t}^0| - Σ_{e∈C_t^0∩X_{p,t}^0} μ_t(e)/|C_t^0 ∩ X_{p,t}^0|

Population accuracy: `Acc_p := E[A_{p,t}]`. Plugin estimator:

> Acc̄_p = (1/n) Σ_{t=1}^n (Σ_{e∈C_t^E∩X_{p,t}^0} Y_t(e)/|C_t^E ∩ X_{p,t}^0| - Σ_{e∈C_t^0∩X_{p,t}^0} Y_t(e)/|C_t^0 ∩ X_{p,t}^0|)

**Assumption 2 (Sampling assumptions).** Requests u_1,...,u_n i.i.d. For each u_t: (i) E[Y_t(e) | u_t, e] = μ_t(e); (ii) Y_t(e) uniformly bounded; (iii) for m ∈ {0, E}, denominator |C_t^m ∩ X_{p,t}^0| is almost surely nonzero.

**Theorem A.5 (Consistency and asymptotic normality).** Under Assumption 2, `Acc̄_p →^a.s. Acc_p` as n → ∞. If per-request variance Var(A_{p,t}) is finite, `√n(Acc̄_p - Acc_p) →^d N(0, σ_p²)` for some σ_p² ≥ 0.

*Proof sketch.* Define `Z_{p,t} := Σ_{e∈C_t^E∩X_{p,t}^0} Y_t(e)/|C_t^E ∩ X_{p,t}^0| - Σ_{e∈C_t^0∩X_{p,t}^0} Y_t(e)/|C_t^0 ∩ X_{p,t}^0|`. By conditional unbiasedness `E[Z_{p,t} | u_t] = A_{p,t}`, so `E[Z_{p,t}] = Acc_p`. Bounded + i.i.d. → SLLN gives a.s. convergence; finite variance → CLT gives asymptotic normality.

Theorem A.5 justifies using Acc̄_p (and its normalized variant N_p^E - N_p^0 constructed from replay pools) as a statistically valid proxy for the accuracy contribution at prefix p.

**Appendix B — Dual-Distribution Training Infrastructure.**
Training objective (9) requires consuming two data streams per step: impressed examples for L_acc + unimpressed candidate-pool examples for L_align. Use a **trainer-side union** of two independent dataloaders, rather than a workflow-level union merging streams before the trainer. Advantage: mixing ratio controlled by `unimpressed_ratio` hyperparameter at training time (not hard-coded into dataset definition).

*Throughput mismatch.* Each Ray dataloader's loading speed is determined by dataset layout (shard sizes, storage bandwidth), while consumption rate is governed by `unimpressed_ratio`. Rates unlikely to match. Faster dataloader produces excess samples → memory accumulation → eventual OOM failures.

*Handling excess batches.* Strategies considered:
- **Drop at the dataloader.** Idles while discarding → timeouts when it falls too far behind.
- **Drop at inference.** Different GPU workers may discard different numbers of batches → accumulating imbalance causes GPU synchronization failures.
- **Pass through unchanged.** Skewed batches make training loss unstable, prevent convergence.

**Solution: zero out excess batches at the loss stage.** Batch flows through forward pass normally (all GPUs synchronized), but loss contribution multiplied by zero → no gradients propagate. On average, **~40.6% of batches are zeroed out**, so they run roughly 2× as many iterations to compensate. Training cost: ~**16.5 hours and $200/run** vs **9 hours and $110/run** for single-distribution baseline. Most efficient method given available infrastructure — balances iteration speed with stable convergence.

**Appendix C — Efficient Pairwise Alignment Loss.**
Pairwise alignment loss (7) sums over item pairs (i, j) sharing the same request within a minibatch. With B ≈ 42,000, naïve O(B²) enumeration is prohibitively memory-intensive. Scatter-operation alternative avoids memory issue but introduces GPU write collisions, defeating parallelism.

*Key observation.* Each request contributes at most k = 100 items, so number of valid pairs is at most O(Bk), not O(B²). Algorithm:
1. **Hash grouping.** Compute h = user_id ⊕ chunk_id for each item in batch (represents originating request).
2. **Sort by hash.** Sort batch by h in O(B log B). After sorting, same-request items form contiguous blocks along batch index.
3. **Block-diagonal structure.** In B × B pair matrix, same-request items now occupy contiguous blocks along the diagonal, each of size at most k × k.
4. **Chunk the batch.** Partition sorted batch into contiguous chunks of size k (boundary cases handled separately).
5. **Scan near-diagonal region.** For each chunk, compute pairwise losses only within the chunk and with its immediate neighbors (one block above + one below diagonal). Any pair (i, j) with |i - j| ≥ k sharing a hash would require at least |i - j| + 1 > k items with the same hash in sorted order, contradicting the per-request bound — so no valid pair lies outside the near-diagonal band.

**Total cost: O(Bk) for pair computation + O(B log B) for sorting = O(B(k + log B)).** All operations within each chunk are dense tensor computations that parallelize efficiently on GPU, avoiding scatter-based gradient collisions.

**Figure 6:** Block-diagonal structure of valid pairs after hash-based sorting. Cyan squares on diagonal = same-request item blocks (at most k×k). Yellow band (diagonal ± one block) = only region that can contain valid pairs. Grey region = provably empty, need not be scanned.

---

## Background context (internal LWS strategy/literature-review doc)

*This is the team's pre-paper internal doc — synthesizes the project context, role definition for LWS, and detailed literature review of 11 papers. The paper is the formalization output of this work.*

### Background — project framing

Current workstream on Lightweight Scoring (LWS) in HF facing significant challenges impacting development velocity:
1. Inconsistency between offline evaluation and online success — slows engineering velocity.
2. Attempts to enhance online performance by incorporating information-rich features (e.g. user sequences) have not produced expected improvements.
3. Transitioning to model architectures previously successful in pinnability and learned retrieval has not resulted in increased performance in either offline or online metrics.

To address: comprehensive literature review of industry papers on LWS models, focused on evaluating these models, identifying critical improvements, and understanding integration with downstream ranking + re-ranking layers.

**[Update 11/03/2024]** After alignment with stakeholders, three roles for LWS (L1 utility role removed for simplicity):

1. **(Primary) Alignment with LSR**
   - Metric: **Overlap @ K** = (# items in intersection of top K LWS output and top K L2 output) / K
2. **Accuracy w.r.t. engagement outcomes**
   - Metric: AUC or Group AUC for engagement actions
3. **Reducing Sample Selection Bias**
   - Metric: **Penetration rate @ K** = (# items in top K LWS output that passed LSR layer) / K

(Q4 2024 + Q1 2025 plans for HF LWS referenced separately.)

### Major learnings from literature review

**Primary role of LWS.** Reviewed recent (2022+) papers + blogs from large-scale recsys + e-commerce + reputable journals. LWS = lightweight scorer = pre-ranking / first-stage ranking model. Sits between downstream LSR (late-stage ranker) and upstream CGs (candidate generators / retrieval sources / matching stage). Retrieval optimizes for recall; LWS optimizes for *alignment* with downstream layers (system alignment).

**Notation funnel:** CG → post-CG candidates → LWS → LSR candidates → LSR → LSR output → Re-ranking → final ranking. Red parts = funnel components; purple parts = sorted items along funnel. Two important notes:

1. Much of the literature simplifies with single prediction head (e.g. CTR). For multi-objective systems like Pinterest HF, use a utility function for linear combination of objectives (repin, closeup, click, share, etc.). Two utility-application points: (a) along with LSR predictions to generate LSR output, (b) along with LWS predictions to generate LSR candidates.
2. Candidate counts vary by context (eCommerce/Search/Content) and company. Typically: thousands+ post-CG, hundreds (sometimes <100) LSR candidates, tens of LSR output. Funnel: CG → post-CG (~thousands+) → LWS (w/ utility) → LSR candidates (~hundreds) → LSR (w/ utility) → LSR output (~tens) → Re-ranking → final (~tens).

### Common expectations for LWS (synthesis across literature)

- LWS more compute-efficient (latency + flops) than ranking model — scores more candidates. Limits feature sets + architecture. User sequences typically not included in entirety due to cost; care needed to include cost-effectively. Two-tower architecture common to avoid cross-features given network-latency constraints.
- Empirical evidence overwhelmingly: alignment between LWS and ranking model is critical to whole system performance. Intuitive: whole LWS layer not needed if LSR can scale cost-free to all candidates.
- Ideal LWS matches exact LSR ranking — but impractical. Most effective: LWS really good at picking LSR output from post-CG candidates.
- LWS and LSR operate on very different candidate sets → care needed in training data construction.
- LWS labels typically combine via loss function:
  - Direct user interactions (model actual behavior)
  - LSR predictions / derived labels (if LSR calibrated) — for aligning LWS and LSR
  - Whether item was in LSR output (handles non-impressed items)
- Training data typically includes unimpressed items in addition to impressed — corrects for **sample selection bias (SSB)**: LWS makes predictions on a candidate population very different from its training population (post LSR).
- Different ways to handle unimpressed: assume all negative; weight during training; use LSR predictions as label ("p-select"); active learning to pick most informative.
- Offline evaluation data typically a portion of overall training data, time-adjusted (e.g. first 3 weeks training, last week eval).
- Common offline metrics:
  - Group AUC
  - Overlap @ K (top-k LWS ∩ top-k LSR / K)
  - Penetration rate @ K (unexposed items in top K LWS / K — measures SSB mitigation)
  - HitRate@K, NDCG@K, MAP@K — biased due to SSB but useful as guardrails

### Additional notable callouts

- **COLD** and **IntTower** both based on SE (Squeeze and Excitation) module for feature importance. IntTower uses cheaper version that removes ReLU block.
- **Sample Selection Module** from Enhancing Pre-Ranking Performance worth investigating — designed for active learning from early-funnel logs.
- **Contrasting Information Transfer** uses LSR embedding to fine-tune LWS embedding.
- **COPR** and **Ranking Consistency** suggest chunking LSR predictions into buckets and using how well LWS predicts which bucket — ignoring within-bucket ranking.
- **Rankflow** and **IntTower** both suggest joint training of LWS + LSR more optimal for both (especially LWS) than separate training.

### Paper-by-paper summaries

**[1] Contrastive Information Transfer for Pre-Ranking Systems (2022)**
- "The ranking consistency between pre-ranking and ranking stages is a key factor to the whole system's performance." Top-u items retrieved by pre-ranker get re-ranked by ranker → relative orders within top-u don't affect final result.
- Main idea: use LSR final embeddings to update LWS final embedding.
- Label = "p-select" (whether item was in LSR output). Training set = LSR candidates only (nothing from post-CG that didn't make LSR).
- Cross-entropy for first component. For each positive label, sample K negatives randomly from same request; add contrastive loss minimizing distance between LWS final-layer embedding and LSR final-layer embedding (latter fixed during training). L_CKT = contrastive loss.
- Offline metrics: G-AUC, Recall, NDCG@K — aligned with online metrics.
- G-AUC interesting candidate to adopt in offline reports.

**[2] On Ranking Consistency of Pre-ranking Stage (2022)**
- "Items with high LSR scores but low LWS scores are less competitive — won't be selected, hurting effectiveness. Items with low LSR scores but high LWS scores won't be impressed; LSR compute wasted, undermining efficiency."
- "Production system can not log ranking-model predictions on the pre-ranking set due to latency. Propose using an online simulator (no latency constraint, doesn't serve main traffic) — each request sent to both production and simulator; simulator logs prediction score on pre-ranking set."
- **Ranking Consistency Score (RCS)** = average hit rate of LWS simulating LSR's role (use LWS to score LSR candidates, compare with LSR predictions on same candidates). Claim: RCS of LWS consistent with online performance of entire system.
- "Ranking quality" (AUC / Group AUC) and "proxy-calibration" (calibration of LWS w.r.t. LSR predictions as ground truth) both important to RCS.
- Finding: RCS much worse for unimpressed items than impressed (SSB). Fix: (a) use LSR predictions directly as soft label for unimpressed; (b) downsample uniformly given larger scale of unimpressed vs impressed.
- Multi-objective: like p-select, use post-utility ranking of LSR; treat LWS as learning-to-rank model.
- Chunking post-utility LSR ranking helps simplify LWS's task — split ranked list into chunks; ignore intra-chunk ordering.

**[3] Scaling the Instagram Explore recommendations system (Engineering at Meta, 2023)**
- Two-stage: light first-stage ranker (recalls thousands), heavy second-stage ranker (operates on top 100 from stage 1).
- First-stage = Two-Tower NN (cacheability). Architecture similar to retrieval but learning objective different: predict output of second stage with label PSelect = {media in top K from second stage}. View as KD from bigger 2nd-stage to smaller 1st-stage.
- "If we have access to enough historical data in the form of offline + online metrics, we can learn functions that map changes in offline metrics into changes in online metrics. Once we have such functions, we can try different parameter values offline and see how offline metrics translate into potential online changes. To make this offline process more efficient, can use BO techniques. Main advantage of offline tuning vs online BO: requires much less time to set up an experiment (hours vs weeks). However, requires strong correlation between offline and online metrics."

**[4] Powered by AI: Instagram's Explore recommender system (2019)**
- 3-stage instead of usual 2: First pass = distillation model (mimics other 2 stages, minimal features) picks 150 of 500. Second pass = lightweight NN with full dense features → 50. Final pass = deep NN with dense + sparse features → 25.
- Multi-task multi-label (MTML) NN to predict positive (like, save) and negative (SFPLT) actions. Shared MLP captures common signals across actions.

**[5] Rethinking the Role of Pre-ranking in Large-scale E-Commerce Searching System (2017)**
- "Most researchers focused on building a lighter model imitating the ranking via feature selection / network compression / KD. Imitating ranking improves consistency between ranking and pre-ranking. Although these can improve online business metrics short-term, they rarely benefit overall item quality at the pre-ranking stage. In Taobao Search these optimizations only make pre-ranking output a few more high-quality items among thousands."
- Pre-ranking selects items from hundreds of thousands of candidates. Using only exposures during training (as ranking does) → severe SSB. Most items' scores in pre-ranking candidates can be unconvincing — model rarely learns them during training.
- "Ranking re-ranks the order inside pre-ranking outputs and determines final output. As a result, primary goal of pre-ranking should be to return an *optimal unordered set* rather than ordered list."
- "Quality of whole output set drops when imitating ranking and improving its inside AUC without involving more online compute. Why AUC is not consistent with online business metrics."
- Authors empirically validate hitrate@k is not a good offline measure of LWS due to SSB. "Offline hitrate@k can only measure the difference between the offline models' output sets and the online output set rather than their quality."
- Advocate using positive labels not only from LSR but other scenarios to reduce bias.
- Training dataset construction:
  - Impressed items
  - LSR candidates (cast as hard negatives)
  - post-CG candidates (cast as easy negatives)
- Labels:
  - Different engagement outcomes (purchases, clicks) based on all scenarios (e.g. not just HF)
  - Whether or not item is exposed (p-select)
  - Combine these losses linearly with weighting
  - Combine with distillation loss from LSR

**[6] Enhancing Pre-Ranking Performance: Tackling Intermediary Challenges in Multi-Stage Cascading Recommendation Systems (2024)**
- Two primary challenges in pre-ranking: (a) training dataset has feedback derived from ranking-stage outcomes but eval needs larger dataset from recall-stage outcomes → SSB; (b) simpler pre-ranking models perform worse than ranking models → inconsistency in candidate set rankings.
- Existing methods integrate recall results into pre-ranking training and assign negative labels to unfed-back samples [22]; or improve precision through feature interaction / selection [12, 13, 18, 30]; or use ranking models for KD [22, 25].
- Issues with existing: large recall result set → substantial compute costs; assuming all unexposed = negative introduces noise; existing methods fail to consider exposure bias. Ranking models tailored to exposed dataset → performance deteriorates on unexposed → compounds exposure bias. Undiscriminating distillation. Most methods tackle only one challenge; methods that tackle two simultaneously [22] need 3-stage simultaneous optimization which is too complex.
- Training data:
  - Impressed items (SE in their notation)
  - post-CG candidates (SNE)
- Downsample post-CG via **Sample Selection Module (SSM)** — uses impressed items to choose which post-CG to include. Active learning via separate discriminator: random walk on historical interaction graph → likelihood of any user × any item interaction → defines "hardness score" → pick hard examples from post-CG.
- Loss = weighted combination of: BCE on engagement label (pseudo-label for unexposed) + p-select + distillation from LSR scores.
- Offline metrics (3 sets):
  - HitRate@K, NDCG@K, MAP@K — how well LWS helps LSR
  - Penetration rate @ K — SSB mitigation
  - Overlap @ K — alignment with LSR

**[7] IntTower: the Next Generation of Two-Tower Model for Pre-Ranking System (2022)**
- Solves efficiency-accuracy dilemma via Interaction enhanced Two-Tower (IntTower): enhances information interaction between user and item towers while keeping "user-item decoupling architecture" paradigm.
- Components:
  - Light-SE module → identifies feature importance, refined feature representations
  - User and item towers → multi-layer nonlinear transformations
  - **FE-Block** (explicit fine-grained early feature interaction between multi-layer user representations and last-layer item representation)
  - **CIR** (contrastive interaction regularization — implicit interaction between user and item representations)
- "FE-Block is the most important part of IntTower. Removing it leads to huge performance drop — explicit feature interaction modeling between user and item towers is statistically significant for two-tower."
- Data: 8 consecutive days of user behavior records from large-scale ad platform. User features: profile, behavior (list of clicked ads), statistics (count of clicked ads), contextual (time). Ad features: task features (id), statistics (click count). Categorical embeddings via lookup; numerical via AutoDis.

**[8] Achieving A Better Tradeoff in Multi-stage Recommender Systems Through Personalization (2024)**
- Most recsys make global fixed choice on # items ESR passes to LSR. Authors claim optimal # should vary per request.
- Contributions:
  - Personalized policy taking into account request-level features in determining ESR budget. Off-policy evaluation of logged data → estimate marginal improvement in slate quality (taking into account user features), per-cohort.
  - Formal model in which a wide class of quality functions (incl. recall) exhibit DR-submodularity (diminishing returns property). Property linked to extent ESR ranking agrees with LSR ranking. Despite NP-hardness, greedy algorithm has approximation guarantees.
  - Experimental validation on three large-scale production recsys; 8.8% compute savings without measurable engagement impact.
- Notes on existing literature: Gu et al. propose RCS aligned with online metrics; Zhang et al. argue for metric estimating online recall via counterfactual examples; Li et al. show simple score-based thresholding can certifiably achieve good consistency. Common approach for SSB: joint optimization of ESR + LSR.
- ESR designs: two-tower (no user-item interaction features). Trained on user labels (clicks, reshares, watch-time), or on LSR predictions (soft labels), or on p(select), or combination.

**[9] COPR: Consistency-Oriented Pre-Ranking for Online Advertising (2023)**
- "Given a set of candidates, it is not their absolute pCTR scores but their relative ECPM ranks that determine results of each phase. Pre-ranking model not required to output same pCTR scores as ranking model — only needs to output scores yielding same ECPM ranks when multiplied by bids. Score alignment relaxed to *rank alignment* — easier to meet."
- Key idea: chunk LSR output, train LWS to predict which chunk each item should go to (rank alignment, not score alignment).
- Training pairwise: learn whether left item should end in higher chunk than right. Importance weighting based on chunk order (chunks 1-10 more important than 11-20).
- Plug-and-play with any existing model. Didn't explicitly mention if this is sole loss or addition.

**[10] AutoFAS: Automatic Feature and Architecture Selection for Pre-Ranking System (2024)**
- "Co-build pre-ranking and ranking models such that knowledge from ranking automatically guides finding most valuable features and architectures for pre-ranking. Co-train, not separate."
- Search space construction; feature + architecture parameters to search for most valuable features + architectures; latency- and KD-guided reward.
- Data: impression logs, click/not-click labels. 10B+ display/click logs, 20M users, 400M clicks in 9 days. Preprocess by adding non-displayed examples based on sample orders in later ranking model (SSB mitigation). Train: first 7 days; val + test: following 2 days.
- Metrics: AUC + Recall (offline), CTR (online), RT (return time / latency) + CPU consumption (system perf).
- Recall here = Overlap @ K.

**[11] RankFlow: Joint Optimization of Multi-Stage Cascade Ranking Systems as Flows (2022)**
- Most existing works train rankers independently on same impression data → fail two challenges: (a) SSB — inconsistency between training and inference data (rankers see only exposed during training, see large unseen pool at inference; "like forcing a student to take an exam beyond the syllabus"); (b) doesn't exploit interactions between rankers — each unaware of others. Huge potential if rankers could interact without changing architectures or sacrificing inference efficiency.
- Main idea: independently train LWS + LSR on impressed items → joint training phase = self-learning + tutor-learning. During joint training, LWS training data constructed using unimpressed items scored by LSR.
- Self-learning + tutor-learning specifics referenced.

## James's edit notes / questions / pushback

*(populate as we go)*

## Action items / open threads

- [x] All 14 pages captured (2026-04-25).
- [ ] Confirm RecSys 2026 submission deadline (need to know edit window)
- [ ] Confirm James's role on the paper — author position 13 (last) is unusual; senior-author or contributor signal? Affects edit altitude.
- [ ] Identify which sections James wants to focus edits on
- [ ] Reconcile background-doc 3-role framing (Alignment / Accuracy / SSB-reduction) with paper's 2-role framing (Alignment / Accuracy only). Paper drops SSB as separate role and absorbs it into the alignment-on-unimpressed construction. Worth checking: is this drop deliberate / theoretically defensible per Section 3 exclusivity claim, or a simplification that loses something?

## James's edit notes / questions / pushback

*(populate as we go)*

## Action items / open threads

- [ ] Get pages 2, 4, 5, 8, 9, 11, 12, 13, 14 (the rest)
- [ ] Confirm RecSys 2026 submission deadline (need to know edit window)
- [ ] Confirm James's role on the paper — author position 13 (last) is unusual; senior-author or contributor signal? Affects edit altitude.
- [ ] Identify which sections James wants to focus edits on
