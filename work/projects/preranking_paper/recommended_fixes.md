# Recommended Fixes — "Alignment + Accuracy" Preranking Paper

**Compiled:** 2026-04-25
**Sources:** editor review (RecSys senior PC stance), writing review (clarity/grammar/concision/ACM), deep-search v1 (2025–2026 preranking lit), deep-search v2 (LTR theory + CF-eval + surveys), Pinterest publications scan, bibliography diff
**Audience:** Hedi (lead) + co-author team. Each item has location, concrete action, effort estimate, source tag.

---

## Tier 0 — Ship blockers (cheap, do first)

These are credibility-level fixes that take <1 hour combined and remove the loudest reviewer attacks.

### Fix 1. Reference [23] misattribution
- **Where:** Bibliography page 11, ref [23].
- **Issue:** Currently listed as "Kai Zhang, Haijun Zhao, Rui Huang, Beichuan Zhang, Na Mou, Yanan Niu, Yang Song, Hongning Wang, Kun Gai 2024 SIGIR — Full Stage Learning for Multi-Stage Systems: A Unified Framework." The actual citation is **Kai Zheng et al. WWW 2024** (arXiv:2405.04844). Wrong lead author, wrong venue.
- **Action:** Update to correct author list, venue (WWW), and DOI.
- **Effort:** 5 min.
- **Source:** deep-search v2 / bibliography diff.

### Fix 2. Spearman ρ sign error in §5.1 + §5.4
- **Where:** §5.1 prose around Table 1 ("Spearman ρ −0.86 → −0.87"), §5.4 ablation paragraph.
- **Issue:** Table 1 displays positive Spearman ρ values (0.871, 0.867, 0.862, 0.860). Prose narrates them as negative. Either the convention flipped silently or the prose is wrong.
- **Action:** Audit every Spearman ρ reference in body text; align signs with table.
- **Effort:** 10 min.
- **Source:** writing review.

### Fix 3. Replace "Conference'17" placeholder
- **Where:** Title page header + footer.
- **Issue:** Placeholder text "Conference'17, July 2017, Washington, DC, USA" still in the LaTeX.
- **Action:** Replace with "RecSys '26" header per ACM template.
- **Effort:** 2 min.
- **Source:** writing review (ACM formatting).

---

## Tier 1 — Credibility fixes (citations)

The single highest-leverage block of work. Each item closes a specific reviewer attack vector. Sub-grouped by theme.

### 1.A — Pinterest internal coherence

*Reviewers expect this paper to sit visibly inside Pinterest's published cascade. Five fixes bring Pinterest self-cites from 2 → 8 with one-sentence positioning each.*

#### Fix 4. Cite InteractRank (Pinterest, WWW '25)
- **Where:** §6 Related Work + §2.1 (multi-stage pipeline framing).
- **Issue:** InteractRank is Pinterest's own published preranker on the Search side, using a Unified Pre-Ranking Label. Claiming a novel alignment-vs-accuracy formalism without positioning against Pinterest's existing preranking publication is a credibility risk. Reviewers will find it.
- **Action:** Add to bibliography. In §6, add 1–2 sentences contrasting: this paper's separated alignment+accuracy structure vs. InteractRank's unified label.
- **Effort:** 30 min.
- **Source:** Pinterest publications scan (P0).

#### Fix 5. Cite TransAct (KDD '23) + TransAct V2
- **Where:** §2.1 (describing L₂) + §6.
- **Issue:** TransAct characterizes the L₂ ranker that the alignment metric targets. TransAct V2 dates the L₂ generation present during the Mar–Apr 2026 forward test set. Reviewers expect "what is the L₂ you're aligning to" answered with a citation, not just "the main ranker."
- **Action:** Add both to bibliography. Cite TransAct in §2.1 when introducing L₂; cite V2 when discussing the forward test models.
- **Effort:** 20 min.
- **Source:** Pinterest publications scan (P0 + P1).

#### Fix 6. Cite MTMD (AdKDD '25)
- **Where:** §6 + abstract / §1 framing.
- **Issue:** Pinterest's ad-side LWS workstream. Internal-coherence cite + clean positioning ("organic LWS aligns to L₂; ad LWS unifies tasks").
- **Action:** Add to bibliography; one-sentence positioning in §6.
- **Effort:** 15 min.
- **Source:** Pinterest publications scan (P0).

#### Fix 13a. Cite PinRec (Pinterest L₀ generative retrieval, arXiv:2504.10507, 2025)
- **Where:** §2.1 (multi-stage pipeline) + §6.
- **Issue:** Generative retrieval deployed across Pinterest Homefeed, Search, Related Pins. Complementary to existing [5] retrieval cite — together they characterize the L₀ space the LWS preranker filters from. Without it, reviewers see a thin L₀ characterization.
- **Action:** Add to bibliography. One-sentence reference in §2.1 alongside [5] when describing retrieval.
- **Effort:** 15 min.
- **Source:** Pinterest publications scan (P1).

#### Fix 13b. Cite "Improving Feature Interactions @ Pinterest" (arXiv:2412.01985, 2024)
- **Where:** §4 or §5 (training objective / production constraints framing).
- **Issue:** Industry-constraint precedent — feature-interaction architecture lessons inside Pinterest Homefeed ranking under latency / GPU memory / reproducibility constraints. The preranking paper's training-objective choices live under the same constraints; citing this gives a direct precedent for "we made this design choice for production reasons."
- **Action:** Add to bibliography. One-sentence reference where production constraints are first discussed.
- **Effort:** 15 min.
- **Source:** Pinterest publications scan (P1).

### 1.B — Preranking competition (2025–2026)

*Direct contemporaries that compete on the cascade-decomposition or unimpressed-pool theses. Failing to engage these is the loudest novelty attack.*

#### Fix 7. Cite LCRON (Wang et al., ICML 2025)
- **Where:** §6 + Theorem 3.4 / Corollary A.4 vicinity.
- **Issue:** Closest theoretical competitor on cascade-decomposition. Derives a lower-bound probability that ground-truth items survive the cascade as a unified surrogate, with stage-specific auxiliary losses. This is the #1 novelty risk.
- **Action:** Add to bibliography. Add 2–3 sentences of explicit contrast: LCRON jointly trains all stages (different problem); this paper holds L₀, L₂ fixed and decomposes the L₁ scalar surrogate (different problem). Frame our exclusivity claim as scoped to that fixed-pipeline regime.
- **Effort:** 45 min.
- **Source:** deep-search v1.

#### Fix 9. Cite HCCP (WWW '25 Companion) + HAP (WWW '26)
- **Where:** §6 + §4.1 (motivating unimpressed-pool alignment).
- **Issue:** Both directly compete on the unimpressed-pool alignment thesis. HCCP: multi-level unexposed-sample construction + Margin InfoNCE. HAP: gradient-harmonized contrastive learning for heterogeneous candidate pools. Risk: reviewers say "industry-standard 2025, not novel."
- **Action:** Add both to bibliography. Position contribution as the **theoretical justification** for what HCCP/HAP/RankFlow do empirically — that's the honest framing.
- **Effort:** 30 min.
- **Source:** deep-search v1.

#### Fix 10. Cite Gu et al. RCS (arXiv 2205.01289, 2022)
- **Where:** §6 + §4.1 (overlap@K motivation).
- **Issue:** The team's own internal background doc analyzes Gu et al. as paper [2] but the paper does not cite it. Self-inflicted credibility wound. Theorem 3.3 is the defense — overlap as the first-order surrogate — but the defense only lands if RCS is named and contrasted.
- **Action:** Add to bibliography. Add 1 sentence to §6 contrasting RCS (an offline simulator producing a hit-rate metric) with overlap@K-on-unimpressed (a theory-derived first-order surrogate).
- **Effort:** 20 min.
- **Source:** bibliography diff bonus add.

#### Fix 13c. Cite WORTH CITING preranking work (HA-PFD, GPL, AIF, Scaling Laws)
- **Where:** §6 Related Work (small bundle).
- **Issue:** Each is adjacent-not-central but shows the field is active in 2025-2026. Bundling them as a single 2-sentence pass shows comprehensive coverage without padding.
- **Action:** Add to bibliography (one row each):
  - **HA-PFD** — "Hardness-aware Privileged Features Distillation with Latent Alignment for CVR Prediction" (KDD 2025, ByteDance). `[unverified — third-party source only; verify primary citation before submission]`. Privileged-feature distillation, adjacent to alignment-loss design (§4.2).
  - **Bi et al. 2026** — "Generative Pseudo-Labeling for Pre-Ranking with LLMs" (GPL, arXiv:2602.20995). LLM-generated content-aware pseudo-labels for unexposed items; +3.07% CTR. Adjacent to alignment-on-unimpressed thesis from a label-generation angle.
  - **Kou et al. 2025** — "AIF: Asynchronous Inference Framework for Cost-Effective Pre-Ranking" (arXiv:2511.12934, likely Alibaba). Decouples interaction-independent computation from real-time prediction. Orthogonal (efficiency, not objective) but represents 2025 industrial preranking lit reviewers expect to see.
  - **Wang et al. (Kuaishou)** — "Scaling Laws for Online Advertisement Retrieval" (arXiv:2411.13322). Offline-to-online metric scaling laws. Adjacent to §5.1 calibration.
- **Effort:** 30 min.
- **Source:** deep-search v1 (ii) WORTH CITING.

### 1.C — Calibration / CF-OPE positioning

*The §5 calibration story competes with the off-policy evaluation literature. These two fixes engage that field explicitly so reviewers don't ask "why not IPS / Cascade-DR?"*

#### Fix 8. Cite Wilm & Normann (RecSys 2025)
- **Where:** §6 + §5.1 (calibration setup).
- **Issue:** Same venue, same year, same problem (offline metrics → online impact). Methodology differs (single-online-experiment Pareto-front approximation vs. our positive-LSQ regression on N=71 models with temporal-gap forward test). Must cite + differentiate.
- **Action:** Add to bibliography. Add 1–2 sentences in §5.1 explaining the methodological difference.
- **Effort:** 30 min.
- **Source:** deep-search v1, deep-search v2.

#### Fix 11. Add CF / OPE scope-clarification paragraph in §6
- **Where:** §6 Related Work, new sub-paragraph.
- **Issue:** Counterfactual / off-policy evaluation literature (Joachims IPS, Schnabel, Saito's OPE-for-recsys, doubly-robust estimators) is the most likely surprise reviewer attack on §5.1. The paper does positive-LSQ regression on (offline, online) pairs, which is **not** OPE. But §6 currently doesn't say so. A reviewer with CF-eval background will ask "why not IPS / Cascade-DR?" and there's no answer prepared.
- **Action:** Add a 4–6 sentence paragraph in §6 explicitly: (a) acknowledging the OPE literature; (b) clarifying that this paper's calibration is a learned regression on historical (offline, online) pairs, not an OPE estimator; (c) noting the two approaches are complementary — OPE estimates reward from logs with policy-correction; we estimate offline-to-online lift map from prior experiments. Cite the following:
  - **Joachims, Swaminathan, Schnabel 2017** — "Unbiased Learning-to-Rank with Biased Feedback" (WSDM, arXiv:1608.04468). Canonical IPS-LTR reference.
  - **Schnabel et al. 2016** — "Recommendations as Treatments" (ICML, arXiv:1602.05352). Foundational CF-eval for recsys.
  - **Saito & Joachims** — "Counterfactual Learning and Evaluation for Recommender Systems" (RecSys 2021 / KDD 2022 tutorial). Most-cited tutorial in this neighborhood; signals engagement with the field.
  - **Kiyohara, Saito et al. 2022** — "Doubly Robust OPE for Ranking Policies under the Cascade Behavior Model" (WSDM, arXiv:2202.01562). Cascade-specific OPE — must acknowledge.
  - **Wang, Gao, Jain, Edge, Ahuja 2023** — "How Well do Offline Metrics Predict Online Performance of Product Ranking Models?" (SIGIR, Amazon). Direct prior art on the offline-metric-selection question.
  - **Krauth, Dean, Zhao et al. 2020** — "Do Offline Metrics Predict Online Performance in Recommender Systems?" (arXiv:2011.07931). Sets up the question this paper answers empirically.
  - **Wang, Agarwal, Dudik 2017** — "Optimal and Adaptive Off-policy Evaluation in Contextual Bandits" (ICML, arXiv:1612.01205). Cite if reviewers push on minimax bounds for "why two scalars."
  - **Gilotte 2018** — already in refs as [7]; expand the in-text treatment by ~3 sentences contrasting their counterfactual estimator with this paper's regression approach.
- **Effort:** 1.5 hours (paragraph + 7 citations + Gilotte expansion).
- **Source:** deep-search v2 (B).

### 1.D — Theoretical anchors

*LTR theory is the closest field to what §3 actually does. Engaging it shows the result is novel-but-not-orphaned.*

#### Fix 12. Cite Bias-Variance Decomposition for Ranking (Shivaswamy & Chandrashekar, WSDM 2021)
- **Where:** §6 (or §3 motivation).
- **Issue:** Closest prior "scalar ranking metric splits into two named components" precedent. Different decomposition (bias / variance, not alignment / accuracy) but useful as a positioning anchor — "we are not the first to argue that a single ranking metric splits into two named pieces; our split is differently motivated."
- **Action:** Add to bibliography. One-sentence positioning in §6.
- **Effort:** 15 min.
- **Source:** deep-search v2 (A).

#### Fix 13d. Expand canonical LTR-theory cites (Cao [1], Xia 2008 add, Liu [14])
- **Where:** §3 motivation + §6.
- **Issue:** [1] Cao 2007 ListNet is cited but treated as a one-line listwise reference. [14] Liu 2009 textbook is the canonical LTR survey — cited but underused. **Xia, Liu, Wang, Zhang, Li 2008** — "Listwise Approach to Learning to Rank: Theory and Algorithm" (ICML) — establishes consistency / soundness / continuity / convexity properties of listwise surrogates and is the closest existing analog of "what properties a scalar ranking surrogate must have." Currently NOT cited; add it.
- **Action:** Add Xia 2008 to bibliography. In §3 motivation, position the exclusivity claim as *an analog at the cascade-stage level of Xia et al.'s consistency conditions at the single-stage level.* In §6, expand the 1-line treatment of [1] and [14] to acknowledge the listwise-LTR theoretical lineage explicitly.
- **Effort:** 45 min.
- **Source:** deep-search v2 (A).

#### Fix 13e. Cite Huang et al. 2024 retrieval methods survey (arXiv:2407.21022)
- **Where:** §6.
- **Issue:** "A Comprehensive Survey on Retrieval Methods in Recommender Systems" — accepted ACM TOIS, 41 pages, 100+ papers. Worth a 1-line cite to acknowledge the broader cascade literature is surveyed and to position the preranking-stage focus as a complement.
- **Action:** Add to bibliography. One sentence in §6.
- **Effort:** 10 min.
- **Source:** deep-search v2 (C).

### 1.E — Self-cite hygiene

#### Fix 13. Self-cite [16] — confirm in-text reference
- **Where:** §4.2 (alignment loss design).
- **Issue:** Naikawadi et al. WWW '26 is "Hybrid Pointwise and Pairwise Ranking Loss" — exactly the structural lineage of L_align (BCE + KL + pairwise). Currently in bibliography but verify it is cited in body when introducing the pairwise alignment loss.
- **Action:** Verify or add inline cite in §4.2.
- **Effort:** 10 min.
- **Source:** editor review F12.

---

## Tier 2 — Theoretical defensibility

### Fix 14. Soften the exclusivity claim
- **Where:** Abstract claim (i), §1 "Exclusivity" bullet, §3, §3.2.
- **Issue:** Prop. 3.2 is a two-term *identity* of S_p^E − S_p^0. Identity ≠ exclusivity. The claim "no third independent scalar component is needed" overclaims relative to what is proven. Reviewers holding the team's own 3-role mental model (alignment / accuracy / SSB-reduction-via-penetration-rate) will press.
- **Action:** Recommended phrasing: **"exclusive *relative to a fixed scalar engagement reward*"** rather than absolute exclusivity. State explicitly that Prop. 3.2 establishes an identity, and that exclusivity follows under the smoothness assumption + the fixed-pipeline assumption (L₀, L₂ held constant). Acknowledge in §6 or §7 that joint-stage decompositions (LCRON-style) are out of scope.
- **Effort:** 1.5 hours (abstract + intro + §3 + §6).
- **Source:** editor review F1, deep-search v2 (A).

### Fix 15. Address penetration-rate@K explicitly
- **Where:** §3 or §6.
- **Issue:** The team's internal 3-role doc defines SSB-reduction via penetration-rate@K = (# top-K LWS items that passed L₂) / K. The paper claims SSB-reduction is "absorbed" into alignment-on-unimpressed, but never proves the absorption. Currently the role just disappears.
- **Action:** Add 1 paragraph: define penetration-rate@K, observe that for a fixed L₀ and L₂, items in top-K-LWS-on-unimpressed that "pass L₂" are (approximately) the items in C ∩ X_p^0 — i.e. the same overlap set the alignment metric measures. Argue that under our framing, penetration-rate@K is dominated by overlap@K-on-unimpressed up to threshold normalization.
- **Effort:** 1 hour.
- **Source:** editor review F1, F14.

### Fix 16. State the target-identification result honestly
- **Where:** §3.3, §4.1.
- **Issue:** The paper claims Theorem 3.3 "narrows the choice to overlap differences specifically — not score correlation, NDCG-with-L₂-as-label, Kendall-τ." But the theorem proves overlap is a *valid* first-order surrogate, not a *unique* one. Score correlation under a different smoothness condition could equally satisfy the theorem.
- **Action:** Either (a) prove uniqueness with explicit conditions, or (b) reframe as "a theory-justified surrogate" rather than "the theory-justified surrogate." Option (b) is cheap and honest.
- **Effort:** 30 min for option (b); harder for (a).
- **Source:** editor review F3.

### Fix 17. Empirical bound on the linearity remainder R_p
- **Where:** §3.3, §5 (new ablation), or appendix.
- **Issue:** Assumption 1 (local smoothness) carries the entire linearity argument. Remainder bound |R_p| ≤ C_p(O_p^E − O_p^0)²/p² is never measured empirically. In recsys with heavy-tailed engagement, smoothness can fail at the head of the L₂ ordering — exactly where the paper operates. For p=10 and overlap shift of 5, R_p could be 25% of c_p · Δ_p, breaking linearity by Order-1.
- **Action:** Across the 71 models, compute observed reward lift, the linear-prediction-from-(O_p^E − O_p^0), and report the residual. Show the remainder is small in practice. Even one figure or table cell would close this attack.
- **Effort:** 4–6 hours (data work).
- **Source:** editor review F2.

---

## Tier 3 — Empirical strengthening

### Fix 18. Add at least one external baseline comparison
- **Where:** Table 3 (live A/B) or new offline comparison table.
- **Issue:** RecSys main-track reviewers will not accept "beats our own production." The team's own internal background doc reviews RankFlow [23], COPR, and IntTower at length but the paper compares only against B1 (Pinterest accuracy-only) and B2 (Pinterest heuristic alignment).
- **Action:** Minimum: an offline comparison of M̂ against RankFlow's joint-training metric, or against COPR's rank-bucket alignment, or IntTower-style two-tower distillation. Pick the cheapest to implement; one is enough.
- **Effort:** 8–12 hours (re-implement and run).
- **Source:** editor review F5.

### Fix 19. Bootstrap CIs on Table 1
- **Where:** Table 1.
- **Issue:** N=20 forward-test models. The claimed ranking "Unimp. forecast (0.871) > Unimp. overlap (0.867) > Imp. forecast (0.862) > Imp. overlap (0.860)" is statistically indistinguishable. The 70% vs 80% winner-accuracy gap is 2 models — at N=20, the binomial CI overlaps. Headline finding does not survive review without uncertainty quantification.
- **Action:** Bootstrap 95% CI on each Spearman ρ. Add binomial CI on each winner-accuracy. Update table caption + §5.1 prose to discuss the CIs.
- **Effort:** 2–3 hours.
- **Source:** editor review F6.

### Fix 20. Drop or contextualize T_MSE
- **Where:** Table 3 row 4, §5.4.
- **Issue:** T vs T_MSE = +3.17% save / +5.79% CV is order-of-magnitude larger than T vs T_KL (+1.43% / neutral) and T vs B2 (+0.62% / -0.97%). MSE on raw scores is a known-bad baseline. Including it inflates the ablation story; reviewers will ask "why MSE? Why not COPR rank-bucketing?"
- **Action:** Either drop T_MSE entirely, or add explicit framing: "MSE distillation is a strawman known to underperform; we include it for completeness."
- **Effort:** 30 min.
- **Source:** editor review F4.

### Fix 21. Address content-view regressions honestly
- **Where:** §5.3 + §7 conclusion.
- **Issue:** T vs B1: +1.43% save, **−0.55% CV (p<0.001)**. T vs B2: +0.62% save, **−0.97% CV**. The paper waves these through as "lighter engagement." A senior reviewer will ask: is the framework optimizing save at the cost of content-view? Pareto improvement or trade?
- **Action:** Choose one of: (a) argue CV is not in the serving objective + cite the Pinterest utility weighting that defines this; (b) acknowledge the Pareto trade explicitly + frame as "save-leaning calibration." Conclusion currently silent — must be addressed.
- **Effort:** 1 hour.
- **Source:** editor review F7.

### Fix 22. Add λ-sensitivity ablation (and ρ, K if cheap)
- **Where:** §5.4.
- **Issue:** L = λL_align + (1−λ)L_acc is the central training prescription. No λ sweep. "λ from offline experiments" on page 1 is hand-waved. Similarly, ρ ∈ (0,1) is the central metric parameter; K is the head cutoff for hits@K. Reviewers will demand at least one sensitivity sweep.
- **Action:** Sweep λ ∈ {0.1, 0.3, 0.5, 0.7, 0.9} on the forward test set. Plot M̂ accuracy vs λ. If cheap, add ρ ∈ {0.25, 0.5, 0.75} and K ∈ {10, 50, 100}.
- **Effort:** 4–6 hours.
- **Source:** editor review F8.

### Fix 23. Document A/B test power / multiple-comparison correction
- **Where:** §5.3 or appendix.
- **Issue:** 2% traffic × 2 weeks per arm. p<0.001 quoted but on which metric, corrected for how many comparisons (4 rows × 2 metrics = 8 tests)? Reviewers familiar with experimentation will ask. MDE calculation absent.
- **Action:** Add MDE calculation. State Bonferroni or Benjamini-Hochberg correction explicitly.
- **Effort:** 1 hour.
- **Source:** editor review F9.

### Fix 24. Tone down generalization claim or add a second surface
- **Where:** Abstract last sentence + §1.
- **Issue:** "Although developed for preranking, the decomposition applies to any intermediate filtering stage in a cascade system." Single-platform (Pinterest homefeed) experiments don't support this generalization.
- **Action:** Either (a) tone down to "we validate on Pinterest homefeed; we conjecture..." or (b) include a second surface (Search, Related Pins, Notifications) ablation. (a) is cheap.
- **Effort:** 15 min for (a); 8+ hours for (b).
- **Source:** editor review F10.

---

## Tier 4 — Bibliography hygiene

### Fix 25. Drop or replace [8] He et al. 2014 + [9] Herlocker et al. 2004
- **Where:** Bibliography.
- **Issue:** Both pre-2015 and not load-bearing in the paper. [8] is Facebook's GBDT+LR ad-click work; [9] is a 22-year-old IR-evaluation paper. Likely vestigial padding.
- **Action:** Verify in-text citations; if no body reference, drop. If used as historical context, replace with more recent equivalents.
- **Effort:** 10 min.
- **Source:** bibliography diff.

### Fix 26. Reconsider [2] Wang & Deep 2016 DLRS, [6] Ferraro 2018, [12] Yu Li 2021, [20] Wang 2025 KD survey
- **Where:** Bibliography.
- **Issue:** Each is borderline — vague workshop venues, journal not normally read by RecSys community (MDPI Electronics), or content overshadowed by stronger newer alternatives.
- **Action:** Verify each has a load-bearing in-text citation. If not, replace with stronger alternatives surfaced by the deep-search.
- **Effort:** 20 min.
- **Source:** bibliography diff.

### Fix 27. Verify [18] vs [23] are not duplicate entries
- **Where:** Bibliography.
- **Issue:** [18] Yang Song et al. 2023 and [23] Kai Zhang et al. 2024 share most of the author set (Haijun Zhao, Rui Huang, Beichuan Zhang, Na Mou, Yanan Niu, Hongning Wang, Kun Gai). Plus [23] is misattributed (see Fix 1). Need to verify these are distinct papers.
- **Action:** Cross-check citations. After Fix 1 corrects [23], verify it is genuinely distinct from [18].
- **Effort:** 15 min.
- **Source:** writing review (ACM formatting).

---

## Tier 5 — Writing, notation, ACM polish

### Fix 28. Tighten the abstract's three-bullet structure
- **Where:** Abstract.
- **Issue:** Bullet (iii) "narrowing the large design space" dangles, modifying *target-identifying* but reading as if it modifies "threshold." "**largely** ad-hoc" hedges unnecessarily — the paper's whole point is that the practice *is* ad-hoc.
- **Action:**
  - Replace bullet (iii) with: *"(iii) target-identifying: alignment should track overlap with the main ranker's selections, and accuracy should track conditional engagement above a shared ranker threshold. Together these claims narrow the design space of possible surrogates."*
  - Drop "largely" before "ad-hoc."
- **Effort:** 10 min.
- **Source:** writing review.

### Fix 29. Add headline numbers to the abstract
- **Where:** Abstract.
- **Issue:** Abstract gives no numbers. Reviewers want at least one headline result up front.
- **Action:** Add: "+1.43% save engagement over an accuracy-only baseline and +0.62% over a heuristic alignment+accuracy baseline in two-week A/B tests."
- **Effort:** 10 min.
- **Source:** writing review.

### Fix 30. Define X_p^0 explicitly before §3.3
- **Where:** §3.2.
- **Issue:** `X_p^0` first used in §3.3 / §3.4 without prior definition (definition lives in Appendix A). Readers cannot follow.
- **Action:** Define X_p^0 inline at first use in §3 main text: "let X_p^0 := {e ∈ D : L₂(e) ≥ L₂(s_p^0)} denote the L₂-threshold set for the baseline."
- **Effort:** 15 min.
- **Source:** writing review.

### Fix 31. Disambiguate ρ
- **Where:** §4.1 (ρ ∈ (0,1) overlap fraction) + Table 1 (Spearman ρ).
- **Issue:** Same symbol overloaded for two distinct quantities.
- **Action:** Use a different symbol for one. Suggest `ϕ` for overlap fraction, leaving Spearman ρ untouched (more conventional).
- **Effort:** 30 min (text + tables + figures).
- **Source:** writing review.

### Fix 32. Define Δ_p, d_p, ∂S_p in main text
- **Where:** §3.3, §3.4, Appendix A.
- **Issue:** `Δ_p` used in Theorem A.3 without prior definition (likely := p̂ - p; Appendix A.3 of the captured pages defines it). `d_p` used in Theorem 3.4 without introduction. `∂S_p` in Proposition A.2 may be a typo or undefined.
- **Action:** Add explicit definitions at first use. Audit `∂S_p` for typo.
- **Effort:** 20 min.
- **Source:** writing review.

### Fix 33. Expand acronyms on first use
- **Where:** §1, §4, §6, Table 1.
- **Issue:** KD (knowledge distillation), BCE, KL, MSE, NDCG, MMoE, NE — none expanded on first use in the paper text.
- **Action:** Expand each acronym at its first occurrence: "knowledge distillation (KD)", "binary cross-entropy (BCE)", "Kullback–Leibler (KL) divergence", "mean squared error (MSE)", "normalized discounted cumulative gain (NDCG)", "multi-gate mixture-of-experts (MMoE)", "normalized entropy (NE)" in Table 1 caption.
- **Effort:** 30 min.
- **Source:** writing review.

### Fix 34. Bridge transitions §3.5 → §4.1 and §4.3 → §5.1
- **Where:** End §3.5 / start §4.1; end §4.3 / start §5.1.
- **Issue:** Both transitions abrupt — Theorem 3.4 lands and §4.1 jumps to "Accuracy metric (baseline, unchanged)…"; §4.3 ends with "What theory rules out" and §5 opens with experimental setup.
- **Action:** Add bridging sentences:
  - End of §3.5 → start of §4.1: *"The representation in Theorem 3.4 directly motivates the offline metrics and training losses of Section 4: each summand becomes either an evaluation aggregate or a training proxy."*
  - End of §4.3 → start of §5.1: *"The empirical sections that follow test these predictions in production."*
- **Effort:** 10 min.
- **Source:** writing review.

### Fix 35. Align voice in §4 and conclusion
- **Where:** §4 ("Why X: …" headings); §7 (past-tense passive openings).
- **Issue:** §4 reads slide-deck-like ("Why alignment cannot reuse impressed distribution"). §7 opens "We studied … We preserved …" — past tense + passive. Mismatch with the abstract's confident "We test each prediction."
- **Action:**
  - Convert §4 "Why X: …" headings into declarative section openers or italicized rhetorical leads.
  - Rewrite §7 with present-tense active verbs: "We formalize preranking … We preserve … We add."
- **Effort:** 30 min.
- **Source:** writing review.

### Fix 36. Cut bloat repetition
- **Where:** §2.3 restates the three open questions from §1; §5.4 restates the impressed→unimpressed 70%→80% finding from §5.1.
- **Action:** Compress §2.3 restatement to one-sentence pointer ("We answer the three questions of §1 in Section 3."). In §5.4, replace the restated number with "as quantified in §5.1."
- **Effort:** 10 min.
- **Source:** writing review.

### Fix 37. CCS subcategories
- **Where:** Title page CCS line.
- **Issue:** ACM 2012 CCS path requires explicit hierarchy. Currently flat: "Information systems → Recommender systems; Learning to rank; Theory of computation → Machine learning theory."
- **Action:** Spell out: "Information systems → Information retrieval → Retrieval models and ranking → Learning to rank." Verify in ACM CCS tool before camera-ready.
- **Effort:** 15 min.
- **Source:** writing review (ACM formatting).

### Fix 38. Verify all figure references
- **Where:** §3, §4, §5.
- **Issue:** Figure 4 not referenced in any captured page text. Figure 3 description present but verify in-text "(Fig. 3)" citation.
- **Action:** Search for each `(Fig. N)` reference; add missing ones.
- **Effort:** 10 min.
- **Source:** writing review.

### Fix 39. Author affiliations block
- **Where:** Title page.
- **Issue:** All 13 authors listed as "Pinterest, San Francisco." ACM camera-ready usually wants per-author affiliation block with email.
- **Action:** Hedi to confirm template format; ensure each author has a complete block.
- **Effort:** 15 min.
- **Source:** writing review (ACM formatting).

### Fix 40. Conclusion should restate the exclusivity claim
- **Where:** §7.
- **Issue:** Exclusivity is a Tier-1 abstract claim but conclusion does not restate it. After Fix 14 softens the claim, the new framing should appear in §7 too.
- **Action:** One sentence in §7 stating the (softened) exclusivity result alongside linearity and target-identification.
- **Effort:** 10 min.
- **Source:** writing review.

### Fix 41. Sentence-level prose rewrites (bundled)
- **Where:** Specific spots called out below.
- **Action:** Each rewrite quoted from writing review:
  - **§4.1 alignment-cannot-reuse paragraph:** Replace fragment-style "doesn't recover offline counterpart of Ali_p" with: *"Alignment cannot reuse the impressed distribution. Restricting to impressed items reweights toward seen positions and mixes in exposure effects, so the resulting estimator does not recover the offline counterpart of Ali_p."*
  - **§4.2 pairwise factor explanation:** Replace arrow-notation "Strong teacher preferences → upweighted pairs" with: *"Pairs with strong teacher preference are upweighted; near-tied teacher preferences are downweighted, mirroring the decisive-vs-tied structure at the head of the L₂ ordering."*
  - **§1 intro claim 4:** "Linear is ubiquitous but has little theoretical justification." → "Linear combination is ubiquitous yet unjustified."
  - **§1 first-order linear:** "Serving objective is *(locally) linear* in the alignment and accuracy components. First-order, linear combinations are not just convenient but structurally correct." → "The serving objective is locally linear in alignment and accuracy components, so first-order linear combinations are structurally correct, not merely convenient."
  - **§5.1 opening:** Drop "Goal:" prefix. Declarative: "We quantify how well scalar offline scores predict online experiment winners and lift magnitudes across past and forward-in-time experiments."
  - **§5.2 dual-distribution paragraph:** Three "data" / "distribution" repeats. Rewrite: *"Because the alignment loss runs on the unimpressed candidate pool while the accuracy loss runs on impressed traffic, the trainer ingests two streams via separate paths."*
  - **§6 hedging:** "To their knowledge, prior work does not state…" → "We are not aware of prior work that states an exclusivity claim for the preranking objective or connects overlap surrogates to main-ranker cutoff shifts in this pipeline."
- **Effort:** 30 min total.
- **Source:** writing review.

### Fix 42. Notation bridges + symbol disambiguation (bundled)
- **Where:** Various.
- **Action:**
  - **S_p superscript bridge sentence** (§3.2 first appearance of S_p^0, S_p^E): add *"When comparing two prerankers, we superscript: S_p^0 for baseline, S_p^E for experimental."*
  - **p̂ explanation sentence** (§3.2): one explicit clause noting p̂ is a *random count*, not a fixed index.
  - **λ gloss in abstract**: when λ first appears in the abstract, add a one-clause gloss: "with mixing coefficient λ."
  - **w_p vs w_{ij} disambiguation note** (§4.2): "Note: w_{ij} denotes pair weights, distinct from the position weights w_p of Section 3.1."
- **Effort:** 20 min total.
- **Source:** writing review.

### Fix 43. Voice & arc consistency (bundled)
- **Where:** §5.2, abstract↔conclusion arc.
- **Action:**
  - **§5.2 bullet vs prose voice clash:** §5.2 uses bullet list style ("*Logged scores and subsampling:* …") while §5.1 and §5.3 are prose paragraphs. Pick one style for all of §5 and apply consistently.
  - **Abstract/conclusion verb consistency:** Abstract says "significantly improves offline–online correlation"; conclusion says "improved offline–online agreement." Pick one phrasing — prefer "offline–online correlation" since it matches Table 1's Spearman framing.
  - **Conclusion silent on heuristic baseline:** Abstract claims "outperforms both an accuracy-only preranker and our heuristic alignment+accuracy production model." Conclusion drops the heuristic-baseline mention. Add it back: "outperformed both accuracy-only and heuristic alignment+accuracy production baselines in live A/B tests."
- **Effort:** 30 min total.
- **Source:** writing review.

### Fix 44. ACM details (bundled)
- **Where:** Various.
- **Action:**
  - **Header capitalization audit:** Section titles are mixed — "Theoretical Decomposition" (title case) vs "Offline metric/loss design" (sentence case). ACM standard is title case. Audit + normalize.
  - **Equation (8) reference verification:** Conclusion refers to "per-segment coefficients in (8)." Verify equation (8) exists at that location and is the correct reference.
  - **References [5] and [16] formatting consistency:** Both contain co-authors who are also paper authors (Hedi Xia, James Li). Verify formatting matches third-party-ref style — no "et al." truncation that drops in-house authors.
- **Effort:** 30 min total.
- **Source:** writing review (ACM formatting).

---

## Effort summary

| Tier | Sub-section | Items | Est. effort |
|------|-------------|-------|-------------|
| 0 — Ship blockers | — | 1–3 | <1 hour total |
| 1 — Credibility (citations) | 1.A Pinterest internal coherence | 4, 5, 6, 13a, 13b | ~1.5 hours |
| | 1.B Preranking competition (2025–2026) | 7, 9, 10, 13c | ~2 hours |
| | 1.C Calibration / CF-OPE positioning | 8, 11 | ~2 hours |
| | 1.D Theoretical anchors | 12, 13d, 13e | ~1 hour 10 min |
| | 1.E Self-cite hygiene | 13 | 10 min |
| 2 — Theoretical defensibility | — | 14–17 | ~3.5 hours + 4–6 hours data work |
| 3 — Empirical strengthening | — | 18–24 | ~12–24 hours (Fix 18 dominates) |
| 4 — Bibliography hygiene | — | 25–27 | ~45 min |
| 5 — Writing & ACM polish | — | 28–44 | ~5.5 hours |

**Minimum viable revision (no new experiments):** Tier 0 + Tier 1 (1.A + 1.B + 1.C + 1.D + 1.E) + Tier 2 reframings (Fix 14, 15, 16) + Tier 4 + Tier 5. ~17 hours of focused work, removes the loudest credibility attacks, leaves empirical claims as-is.

**Strong revision (with one new experiment):** above + Fix 17 (remainder bound), Fix 19 (bootstrap CIs), Fix 22 (λ sweep), Fix 21 (CV framing). ~30 hours.

**Full revision (RecSys main-track strength):** all of the above + Fix 18 (external baseline). ~45+ hours.

## Dependencies

- **Fix 1** (ref [23] misattribution) must precede **Fix 27** ([18] vs [23] duplicate check).
- **Fix 14** (soften exclusivity) must precede **Fix 40** (conclusion restatement).
- **Fix 7** (cite LCRON) is the framing anchor for **Fix 14** (exclusivity) — explicit LCRON contrast scopes the exclusivity claim. Do Fix 7 first.
- **Fix 13d** (LTR theory expansion via Cao / Xia 2008 / Liu) supports **Fix 14** (exclusivity reframing) — positions exclusivity as analog of single-stage consistency results.
- **Fix 11** (CF/OPE scope paragraph) is independent of all other fixes; can be drafted in parallel.
- **Fixes within 1.A** (Pinterest cites) can run in parallel.
- **Fixes within 1.B** (preranking competitors) can run in parallel.
- **Fix 19** (bootstrap CIs) depends on access to the per-model offline + online numbers — assume Hedi has these.
- **Fix 41** (sentence-level prose rewrites) should follow Fix 28 (abstract bullet rewrite) since both touch §1 motivation.
- **Fix 43** (voice & arc consistency) is best done last, after Fix 14 + Fix 40 settle the exclusivity framing across abstract / §1 / §7.
