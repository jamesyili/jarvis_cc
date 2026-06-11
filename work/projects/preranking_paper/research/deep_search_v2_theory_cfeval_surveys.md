# Deep Search v2 — Theory, CF-Eval, Surveys

**Created:** 2026-04-25
**Scope:** Adjacent-literature defensibility check for "Alignment + Accuracy: A First-Principles Framework for Preranking" (RecSys 2026 target).
**Method:** WebSearch + arxiv abstract verification. Each entry tagged `[verified]` (arxiv abstract / openreview / DOI page directly fetched or returned in search) or `[unverified]` (secondary-source mention only).

---

## (A) Exclusivity-claim defensibility

The paper claims: under mild assumptions, no third independent scalar is needed beyond alignment + accuracy for the preranker objective. This is a strong sufficiency-style claim. Searched listwise LTR theory, click-model decomposition, multi-objective ranking, and recent cascade end-to-end work for any prior result of the same shape.

### MUST CITE

- **Cao, Qin, Liu, Tsai, Li 2007 — "Learning to Rank: From Pairwise Approach to Listwise Approach" (ICML).** [verified]
  Foundational listwise framing. Defines a scalar listwise loss over the full predicted ordering and uses permutation/top-1 probability decompositions. Already in refs as [1].
- **Xia, Liu, Wang, Zhang, Li 2008 — "Listwise Approach to Learning to Rank: Theory and Algorithm" (ICML).** [verified]
  Establishes consistency / soundness / continuity / convexity properties of listwise surrogates. Closest existing analog of "what properties a scalar ranking surrogate must have"; the exclusivity claim should be positioned as an *analog at the cascade-stage level* of Xia et al.'s consistency conditions at the single-stage level. **Already cited as [14]; expand the 1-line treatment.**
- **Liu 2009 — "Learning to Rank for Information Retrieval" (Foundations and Trends in IR, 3(3): 225–331).** [verified]
  The textbook. Survey of pointwise/pairwise/listwise. Cite as the canonical reference for prior-art on scalar ranking-loss decompositions. **Already in refs as [14] (likely conflated with Xia 2008 — check the BibTeX).**
- **Craswell, Zoeter, Taylor, Ramsey 2008 — "An Experimental Comparison of Click Position-Bias Models" (WSDM).** [verified]
  Already in refs as [4]. Examination hypothesis grounds the monotone I(·) profile in §3.1. Reference is correctly placed; nothing more needed unless reviewers push on whether the impression-profile assumption is restrictive.

### WORTH CITING

- **Shivaswamy & Chandrashekar 2021 — "Bias-Variance Decomposition for Ranking" (WSDM, Netflix).** [verified, DOI 10.1145/3437963.3441772]
  Decomposes ranking error into bias and variance components. *Different decomposition* than alignment+accuracy, but it's the most prominent prior "scalar ranking metric splits into two named components" result. Precedent that decomposition results are accepted in this venue. Use for positioning ("decomposition results are an established mode in this literature; ours specializes to the cascade-preranker setting").
- **Wang, Agarwal, Dudik 2017 — "Optimal and Adaptive Off-policy Evaluation in Contextual Bandits" (ICML, arxiv 1612.01205).** [verified]
  Establishes minimax MSE lower bounds matched by IPS and DR; introduces SWITCH. Use as the canonical bias-variance lower-bound reference if reviewers ask "why two scalars and not three" — Wang/Agarwal/Dudik don't claim sufficiency at any number, so the exclusivity claim is genuinely orthogonal to their result. Also lets you frame your claim as constructive (you exhibit two) rather than minimax.
- **Chuklin, Markov, de Rijke 2015 — "Click Models for Web Search" (Morgan & Claypool monograph).** [verified — standard reference]
  Catalog of PBM, DCM, UBM, CCM, DBN. If a reviewer challenges the "monotone I(·)" assumption, this is the reference for the space of plausible profiles and what each model adds beyond examination.

### ATTACK SURFACE

1. **The exclusivity claim is the riskiest single sentence in the paper.** No prior work in the searched literature states a sufficiency result of this form for the preranker stage. That cuts both ways: genuinely novel framing, but also no precedent for reviewers to anchor on, so the burden of proof falls fully on §3 + Appendix A. Two specific failure modes:
   - **Diversity / fairness as the canonical "third scalar" counterexample.** Paper hedges with "apart from orthogonal considerations like diversity / fairness." A skeptical reviewer will read this as conceding the exclusivity claim is false in general and only true under a restricted reward model. Recommend tightening §1 to "exclusive *relative to a fixed scalar engagement reward*" rather than absolute exclusivity.
   - **The "scalar surrogate respecting their assumptions" qualifier.** Assumption 1 (locally-smooth g_p) does most of the work. Anyone who proposes a non-smooth third metric (e.g., a long-tail recall measure that isn't differentiable in cutoff) is technically outside the theorem. Reviewer might frame this as "the theorem only rules out smooth third components."
2. **No prior cascade-stage exclusivity result exists** (verified via search). This means novelty is real, but it also means there is no incumbent framing to point to that has been peer-reviewed and accepted. Strengthens the case for a longer related-work pass through Xia 2008 + Shivaswamy 2021 as the closest analogs.
3. **Risk that listwise-LTR theorists (a small but vocal community) read §3 as an under-developed re-derivation of known consistency results restricted to cascade structure.** Mitigation: explicitly position §3 as *operationalizing* Xia 2008 / Liu 2009 in the cascade setting, not re-proving from scratch.

---

## (B) Counterfactual / off-policy evaluation literature

The paper's §5 calibration approach — positive linear regression of online lift on offline metrics across 71 historical+forward-test models — competes directly with off-policy / counterfactual offline evaluation, but §6 Related Work mentions "offline A/B testing" only briefly via [7] Gilotte. This is the largest unaddressed adjacent literature.

### MUST CITE

- **Joachims, Swaminathan, Schnabel 2017 — "Unbiased Learning-to-Rank with Biased Feedback" (WSDM, arxiv 1608.04468).** [verified]
  IPS-weighted Ranking SVM; canonical reference for unbiased LTR via counterfactual inference. The paper's calibration claim ("learn weights of M_align + M_acc that predict online lift") is doing something fundamentally different from IPS — it's a regression on observed online lift, not an unbiased value estimate from logged data — and §6 needs to say so explicitly. Otherwise reviewers will ask "why didn't you just use IPS?"
- **Schnabel, Swaminathan, Singh, Chandak, Joachims 2016 — "Recommendations as Treatments: Debiasing Learning and Evaluation" (ICML, arxiv 1602.05352).** [verified]
  Casts recommendation as causal-inference treatment effect; propensity-weighted MF. Foundational counterfactual-eval reference for recommender systems. Same role: cite to acknowledge the literature, then differentiate.
- **Gilotte, Calauzènes, Nedelec, Abraham, Dollé 2018 — "Offline A/B Testing for Recommender Systems" (WSDM, arxiv 1801.07030).** [verified, already ref [7]]
  Capped/normalised IS counterfactual estimator benchmarked against online A/B at Criteo. **Already cited; should be expanded** — this is the most direct prior "calibrate offline against online" paper from industry. Worth ~3 sentences in §6 contrasting their counterfactual estimator approach with this paper's regression-on-online-lift approach.
- **Saito & Joachims 2021/2022 — "Counterfactual Learning and Evaluation for Recommender Systems" (RecSys 2021 tutorial; KDD 2022 tutorial).** [verified]
  Most cited recent tutorial / position piece on OPE for recsys. If submitting to RecSys 2026, reviewers will know this tutorial. Cite as the canonical entry point to OPE-for-recsys to acknowledge the literature exists, and explain why your calibration framing is complementary, not competitive.

### WORTH CITING

- **Wilm & Normann 2025 — "Identifying Offline Metrics that Predict Online Impact: A Pragmatic Strategy for Real-World Recommender Systems" (RecSys 2025, arxiv 2507.09566).** [verified — abstract page fetched]
  This is **the closest contemporary peer.** OTTO e-commerce; defines a novel offline metric "order density" and validates against online CTR / conversion / units-sold. Same problem framing as your §5: which offline metrics align with online impact. **Strongly recommend citing and differentiating** — they don't do positive linear regression across N=71 models, they validate alignment in a single online experiment. Your contribution is the *calibration via regression* + *temporal-gap forward test* methodology.
- **Wang, Gao, Jain, Edge, Ahuja 2023 — "How Well do Offline Metrics Predict Online Performance of Product Ranking Models?" (SIGIR, Amazon).** [verified, DOI 10.1145/3539618.3591865]
  Evaluates 36 offline-metric variants against business-metric ranker preferences. Direct prior art for "pick the right offline metric." Cite to establish the question is live in industry.
- **Krauth, Dean, Zhao, Guo, Curmei, Recht, Jordan 2020 — "Do Offline Metrics Predict Online Performance in Recommender Systems?" (arxiv 2011.07931).** [verified]
  Sarah Dean is a coauthor (matches your prompt's "Dean"). Simulation-based study across 11 recommenders × 6 environments. Sets up the question this paper answers empirically.
- **Castells & Moffat 2022 — "Offline Recommender System Evaluation: Challenges and New Directions" (AI Magazine 43(2), DOI 10.1002/aaai.12051).** [verified]
  Position paper enumerating offline-eval pitfalls. Useful one-line cite to legitimize §5 as engaging with a known open problem.
- **Kiyohara, Saito et al. 2022 — "Doubly Robust Off-Policy Evaluation for Ranking Policies under the Cascade Behavior Model" (WSDM, arxiv 2202.01562; Best Paper Runner-Up).** [verified]
  Cascade-DR estimator. Genuinely cascade-specific OPE. Important to acknowledge: there is OPE work that takes the cascade structure seriously, and it's recent and visible.
- **Kiyohara, Uehara, Narita, Shimizu, Yamamoto, Saito 2023 — "Off-Policy Evaluation of Ranking Policies under Diverse User Behavior" (KDD, arxiv 2306.15098).** [verified]
- **Shimizu, Tanaka, Kishimoto, Kiyohara, Nomura, Saito 2024 — "Effective Off-Policy Evaluation and Learning in Contextual Combinatorial Bandits" (RecSys, DOI 10.1145/3640457.3688099).** [verified]
  These two together establish the OPE-for-ranking subfield is active at top venues 2022–2024.

### ATTACK SURFACE

1. **The biggest defensibility gap is the unaddressed competition with OPE.** A careful reviewer will read §5 and ask: "You have logged data, you have a baseline policy, you have a target policy, you want to estimate target-policy value. Why not IPS / DR / Cascade-DR?" The answer — which the paper should make explicit — is: (a) you're not estimating policy value, you're regressing online lift on already-observed offline metrics; (b) you have N=71 model-experiment pairs which is a regression dataset, not a logging-policy dataset; (c) IPS-style estimators address a *different* problem (single-policy value estimation from biased logs). This needs to be in §6 or a 1-paragraph "scope" callout in §5.
2. **The "positive linear regression" methodology is empirically defensible (71 models, train/forward-test split, temporal gap) but theoretically thin in the paper.** No coverage of standard concerns: confidence intervals on (α, β), regularization, multiple-comparisons over the metric panel in Table 1, robustness to outlier experiments. A counterfactual-eval reviewer will note that OPE estimators come with concentration / consistency guarantees (your Theorem A.5 only handles the accuracy estimator, not the calibration). Risk: reviewers could decide the empirical contribution is solid but the theoretical contribution is "linearity + decomposition" with calibration being just methodology. Pre-empt by adding a 1-paragraph note on calibration uncertainty.
3. **Wilm & Normann 2025 is the most likely "you didn't cite us" reviewer comment.** Same venue (RecSys), same year, same problem framing. Must cite.
4. **Saito's tutorial visibility.** RecSys 2026 reviewers will skew toward recognizing Saito as the OPE-for-recsys voice. Citing the tutorial signals you've engaged with the field even though the paper is doing regression-not-OPE.

---

## (C) 2024–2026 surveys / position papers on preranking, cascade ranking, multi-stage ranking

Searched for surveys that the paper would need to position against.

### MUST CITE

- **Zheng, Zhao, Huang, Zhang, Mou, Niu, Song, Wang, Gai 2024 — "Full Stage Learning to Rank: A Unified Framework for Multi-Stage Systems" (WWW, arxiv 2405.04844).** [verified]
  **This is the closest direct competitor and you already cite it as [23] (attributed there to "Zhang et al. 2024 SIGIR" — the BibTeX is wrong; actual venue is WWW 2024 and lead author is Zheng).** Proposes Generalized Probability Ranking Principle (GPRP), addresses selection bias across all four stages with a unified framework. Your §3 exclusivity result is *narrower scope* (preranker only) but *deeper structure* (decomposition + linearity + target identification). Position explicitly: GPRP gives a multi-stage principle; this paper gives a stage-local 2-axis sufficient set with operational metrics. **Fix the citation in [23] before submission.**
- **Wang, Zhang, Wang, Yang, Li, Yang, Wen, Jiang, Gai 2025 — "Learning Cascade Ranking as One Network" (LCRON, ICML 2025, arxiv 2503.09492).** [verified]
  ICML 2025 acceptance. End-to-end cascade training via surrogate loss derived from the lower-bound probability ground-truth items survive the cascade. **Direct theoretical competitor.** They propose a *training* objective that targets end-to-end alignment; you propose an *evaluation + training* decomposition that separates alignment from accuracy at the stage level. Both target the same north-star (online lift) via different theoretical machinery. Must cite, and can position favorably: LCRON requires joint training of all stages; your method preserves the modular accuracy branch and only retrains preranker.

### WORTH CITING

- **Huang, Chen, Lin, Qin, Feng, Zhang, Yu 2024/2025 — "A Comprehensive Survey on Retrieval Methods in Recommender Systems" (arxiv 2407.21022, accepted ACM TOIS).** [verified]
  Retrieval-stage focused (not preranker), 41 pages, 100+ papers. Worth a 1-line cite to acknowledge the broader cascade literature has been surveyed. Note: explicitly *does not* cover the ranking stage in depth.
- **Zhou, Zhao, Huang et al. — "A Survey of Real-World Recommender Systems: Challenges, Constraints, and Industrial Perspectives" (arxiv 2509.06002, 2025).** [verified — abstract page fetched]
  Industry-focused survey. Useful framing reference; does not appear to deeply cover preranker theory specifically.
- **Generative Recommendation surveys (multiple, 2025).** [verified — multiple arxiv hits]
  The field is shifting toward generative / unified architectures (preprints.org 202512.0203, 202512.0741; TechRxiv). Worth a 1-sentence acknowledgment in §6 that the cascade architecture this paper targets is being challenged by generative alternatives, with note that the alignment+accuracy decomposition is architecture-agnostic at the stage-filter level.

### ATTACK SURFACE

1. **There is no single "preranking survey" that frames the field.** This is good for your novelty story (you can say "no formal first-principles framework exists") and bad for your positioning story (no obvious target to position against). The two SIGIR/WWW/ICML works above (Zheng 2024, Wang 2025) are *the* incumbent framings to engage with; if §6 doesn't engage them substantively, reviewers will read the related-work section as thin.
2. **The reference [23] BibTeX error is concrete and fixable.** "Zhang et al. 2024 SIGIR" should be "Zheng et al. 2024 WWW." Lead-author misattribution is the sort of thing area chairs notice.
3. **LCRON is dated March 2025 → ICML 2025 → June 2025 v3.** It is plausibly the single most-likely-to-be-known-to-reviewers paper in this neighborhood for a RecSys 2026 submission. Risk of "you missed the obvious comparison." Mitigation: a clear 2-sentence framing of how a stage-local decomposition relates to end-to-end cascade training.
4. **Generative-recommendation framing risk.** A bold reviewer could write "this work optimizes a stage in an architecture the field is moving away from." Pre-empt with a 1-line note that the alignment+accuracy decomposition characterizes any *intermediate filtering stage*, including filtering layers in generative pipelines.

---

## Verifiable URLs

- https://arxiv.org/abs/1602.05352 — Schnabel et al. 2016, Recommendations as Treatments
- https://arxiv.org/abs/1608.04468 — Joachims et al. 2017, Unbiased LTR with Biased Feedback
- https://arxiv.org/abs/1612.01205 — Wang/Agarwal/Dudik 2017, Optimal and Adaptive OPE
- https://arxiv.org/abs/1801.07030 — Gilotte et al. 2018, Offline A/B Testing for Recommender Systems
- https://arxiv.org/abs/2011.07931 — Krauth/Dean et al. 2020, Do Offline Metrics Predict Online Performance
- https://arxiv.org/abs/2202.01562 — Kiyohara/Saito 2022, Cascade DR
- https://arxiv.org/abs/2306.15098 — Kiyohara/Saito 2023, OPE under Diverse User Behavior
- https://arxiv.org/abs/2310.08039 — Song et al. 2023, Rethinking Large-scale Pre-ranking (Entire-chain)
- https://arxiv.org/abs/2407.21022 — Huang et al. 2024, Retrieval Methods Survey
- https://arxiv.org/abs/2405.04844 — Zheng et al. 2024 WWW, Full Stage Learning to Rank (GPRP)
- https://arxiv.org/abs/2503.09492 — Wang et al. 2025 ICML, LCRON
- https://arxiv.org/abs/2507.09566 — Wilm & Normann 2025 RecSys, Identifying Offline Metrics
- https://arxiv.org/abs/2509.06002 — 2025, Real-World Recommender Systems Survey
- https://dl.acm.org/doi/10.1145/3437963.3441772 — Shivaswamy & Chandrashekar 2021 WSDM, Bias-Variance Decomposition for Ranking
- https://dl.acm.org/doi/10.1145/3539618.3591865 — Wang et al. 2023 SIGIR, How Well Do Offline Metrics Predict
- https://dl.acm.org/doi/10.1145/3640457.3688099 — Shimizu/Saito et al. 2024 RecSys, OPE Combinatorial Bandits
- https://dl.acm.org/doi/10.1145/1341531.1341545 — Craswell et al. 2008 WSDM, Click Position-Bias Models
- https://dl.acm.org/doi/10.1145/1390156.1390306 — Xia et al. 2008 ICML, Listwise LTR Theory and Algorithm
- https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2007-40.pdf — Cao et al. 2007 ICML, Listwise (ListNet)
- https://onlinelibrary.wiley.com/doi/10.1002/aaai.12051 — Castells & Moffat 2022, Offline RS Eval AI Magazine
- https://www.nowpublishers.com/article/Details/INR-016 — Liu 2009, LTR Foundations and Trends
- https://usaito.github.io/files/RecSys2021_Tutorial.pdf — Saito & Joachims RecSys 2021 tutorial
