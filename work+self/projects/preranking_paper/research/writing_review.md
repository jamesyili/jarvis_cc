# Writing Quality Review — Preranking Paper Draft

**Source:** Writing-quality agent run 2026-04-25
**Scope:** Clarity, grammar, concision, notation, voice, structure. Content correctness handled by editor agent (see `editor_review.md`).
**Coverage:** Pages 1–12 reviewed in this pass. Pages 13–14 (Appendix A.4, A.5, B, C, Figure 6) captured after this review — clarity/grammar pass on 13–14 recommended as follow-up. The "Background context" section in `paper_capture.md` is an internal doc and not part of the submission — skipped.

## SENTENCE-LEVEL ISSUES

### Hard-to-parse sentences

**Abstract, third bullet (p.1):**
> "(iii) *target-identifying*—alignment should track overlap with the main ranker's selections, and accuracy should track conditional engagement above a shared ranker threshold, narrowing the large design space of possible surrogates."

The trailing "narrowing the large design space" dangles — modifying *target-identifying* but reading like it modifies "threshold." Rewrite:
> "(iii) *target-identifying*: alignment should track overlap with the main ranker's selections, and accuracy should track conditional engagement above a shared ranker threshold. Together these claims narrow the design space of possible surrogates."

**Page 7, §4.1 alignment-cannot-reuse paragraph:**
> "Why alignment cannot reuse impressed distribution: data distributions are fundamentally different. Restricting to impressed reweights toward seen positions and mixes in exposure effects; doesn't recover offline counterpart of Ali_p."

Fragment ("doesn't recover…") plus telegraphic style. Rewrite:
> "Alignment cannot reuse the impressed distribution. Restricting to impressed items reweights toward seen positions and mixes in exposure effects, so the resulting estimator does not recover the offline counterpart of Ali_p."

**Page 7, §4.2 pairwise factor explanation:**
> "Strong teacher preferences → upweighted pairs; near-tied teacher preferences → downweighted (mirrors the L₂-decisive vs near-tied structure in the head of the L₂ ordering)."

Arrow notation reads like draft notes; "L₂-decisive vs near-tied structure" is jargon-thick. Rewrite:
> "Pairs with strong teacher preference are upweighted; near-tied teacher preferences are downweighted, mirroring the decisive-vs-tied structure at the head of the L₂ ordering."

**Page 10, Table 1 caption / surrounding prose:**
> "Spearman ρ −0.86 → −0.87 (validates Section 3 prediction…)"

The numbers in the table are *positive* (0.871, 0.867); the prose says −0.86 → −0.87. Sign is wrong or the convention flipped. Either way: **ship-blocker**. Fix the sign and audit every Spearman reference (this same error repeats in §5.4 ablation paragraph).

### Wordiness / redundancy

**Abstract (p.1):** "yet the choice of what these quantities should target—and how they should combine—is largely ad-hoc." → "yet *what* these quantities should target and *how* they combine remain ad-hoc."

**Page 1 intro claim 4:** "Linear is ubiquitous but has little theoretical justification." → "Linear combination is ubiquitous yet unjustified."

**Page 7, §5.1:** "Goal: quantify how well scalar offline scores predict online experiment winners and lift magnitudes across many past + future experiments." Drop "Goal:" — declarative is tighter: "We quantify how well scalar offline scores predict online experiment winners and lift magnitudes across past and forward-in-time experiments."

**Page 10, §5.2 dual-distribution paragraph:** "alignment and accuracy losses operate on fundamentally different data distributions (unimpressed candidate pool vs impressed traffic), requiring separate data ingestion paths in production." Three "data" / "distribution" repeats. Rewrite: "Because the alignment loss runs on the unimpressed candidate pool while the accuracy loss runs on impressed traffic, the trainer ingests two streams via separate paths."

### Hedging / under-confident phrasing

**Abstract:** "**largely** ad-hoc" — drop "largely." The whole point of the paper is that it *is* ad-hoc.

**Page 1:** "First-order, linear combinations are not just convenient but structurally correct." Strong line — keep, but the surrounding "Serving objective is *(locally) linear*" softens it with parenthetical hedge. Promote local linearity into a clean clause: "The serving objective is locally linear in alignment and accuracy components, so first-order linear combinations are structurally correct, not merely convenient."

**Page 11 §6:** "To their knowledge, prior work does not state an exclusivity-style claim…" Switch from third person and tighten: "We are not aware of prior work that states an exclusivity claim for the preranking objective or connects overlap surrogates to main-ranker cutoff shifts in this pipeline."

**Page 11 conclusion:** "We studied preranking in multi-stage recommenders, where systems must optimize both engagement prediction and agreement with the main ranker." "Studied" is weak for a conclusion. → "We formalized preranking…"

### Notation introduced-but-not-used or used-before-introduced

- **C(u), D(u)** appear on p.3 (§2.1), but on p.6 §3.2 the paper writes `C^E ∩ X_p^0` — the set `X_p^0` is never defined in the captured pages. **Define X_p^0 explicitly** before §3.3 (likely "top-p items by L₂ from the baseline candidate set").
- **S_p, Š_p, S_p^0, S_p^E** — the bare `S_p` on p.6 §3.1 is defined as a prefix average over `s_i`. Then §3.2 introduces `S_p^0, S_p^E` without explicitly stating that `S_p` from §3.1 is now superscripted by experiment arm. Add a bridging sentence: "When comparing two prerankers, we superscript: `S_p^0` for baseline, `S_p^E` for experimental."
- **p̂** is defined immediately before `Š_p` but the role of `p̂` (a *random count*, not a fixed index) deserves one explicit sentence. Currently it's introduced and then `Š_p := (1/p̂) Σ` uses it as a denominator without comment.
- **Δ_p** appears in Theorem A.3 (p.11 appendix) without prior definition in the captured text. Likely `Δ_p := p̂ - p` — define inline.
- **∂S_p** in Proposition A.2 (p.11) — no prior introduction. Looks like a typo for `S_p^0` or similar. Audit.
- **c_p, d_p, α_p, β_p** — c_p defined in Theorem 3.3, d_p never introduced in captured text but used in Theorem 3.4 (p.6). Define d_p before or alongside c_p.
- **λ** introduced in §4.3 (p.7) as mixing coefficient; abstract on p.1 also uses `λ` — fine, but the abstract should give a one-clause gloss ("with mixing coefficient λ").
- **ρ** is overloaded: ρ ∈ (0,1) as overlap fraction (p.7 §4.1) **and** Spearman ρ in Table 1 (p.10). Disambiguate — use a different symbol for one.
- **w_p** defined cleanly in Proposition 3.1; **w_{ij}** in §4.2 is a separate object. Acceptable but flag in a sentence: "Note: `w_{ij}` denotes pair weights, distinct from the position weights `w_p` of Section 3.1."

### Acronym expansion

- **LWS, LSR, CG** — used heavily in the background doc; **never expanded in the paper text shown**. The paper currently uses "preranking" / "main ranking" / "retrieval" — consistent. But check whether L₀/L₁/L₂ ever appear as "LWS/LSR" in paper body — if so, reconcile.
- **KD** (knowledge distillation) — first used in §1 ("often KD") with no expansion. Expand on first use.
- **BCE, KL, MSE** — never expanded in captured pages. Spell out at first use: "binary cross-entropy (BCE)", "Kullback–Leibler (KL) divergence", "mean squared error (MSE)".
- **NDCG, AUC, PR-AUC, ROC-AUC** — standard enough to leave, but NDCG should expand on first use ("normalized discounted cumulative gain") since the prefix-reward derivation in §3.1 is positioned against NDCG-style position weighting.
- **NE** in Table 1 — never defined. Looks like "normalized entropy." Expand in the table caption.
- **MMoE** (p.11 §6) — expand: "multi-gate mixture-of-experts (MMoE)."
- **MTML, SE, FE-Block, CIR, SSM, BO, SSB** — appear only in the background doc, not in the paper itself. Skip.

### Voice inconsistency

- §3 (p.6) reads as a tight mathematical voice ("Define I(i)…", "By construction…"). §4 (p.7) shifts into a more conversational engineering register ("Why alignment cannot reuse impressed distribution", "Why overlap, not other surrogates"). The §4 "Why X: …" headings read like a slide deck — convert to declarative section openers or italicized rhetorical leads.
- §5.2 (p.10) bullet list style ("*Logged scores and subsampling:* …") clashes with the prose paragraphs of §5.1 and §5.3. Either bullet all of §5 or none.
- Conclusion (p.11) opens "We studied" then shifts to "We preserved … and added" — past tense + passive constructions. Compare to abstract's confident "We test each prediction." Align tense and vigor: "We formalize … We preserve … We add."

## STRUCTURAL ISSUES

### Section transitions

- **§3.5 → §4.1** is abrupt: Theorem 3.4 states `R^E - R^0 = Σ α_p (O_p^E - O_p^0) + Σ β_p (N_p^E - N_p^0) + R`, and §4.1 jumps to "Accuracy metric (baseline, unchanged)…" Add one bridging sentence: "The representation in Theorem 3.4 directly motivates the offline metrics and training losses of Section 4: each summand becomes either an evaluation aggregate or a training proxy."
- **§4.3 → §5.1** also abrupt — the "What theory rules out" callout ends §4.3, then §5 opens with experimental setup. Add: "The empirical sections that follow test these predictions in production."
- **§6 (related work) → §7 (conclusion)** — no captured transition. Likely fine, but check the paragraph end.

### Figures / tables references

- **Figure 3** is described in §4 prose (p.7) — referenced *in text* there? The summary says "Figure 3: Three-way parallel decomposition" but I don't see an in-text "(Fig. 3)" citation. Verify the body cites it.
- **Figure 5** (p.10) is described after Table 1 in the captured prose — ok.
- **Figures 1, 2, 4** are captioned as placeholders in the markdown; verify each is referenced by number in body text. Especially Figure 4: not mentioned anywhere in the captured pages. Likely lives on page 8 or 9 (not captured) — confirm.
- **Tables 1, 2, 3** are all referenced in body text — good.
- "Theorem 3.3 narrows the choice to overlap differences specifically" (p.7 §4.1) — the in-text reference is fine, but Theorem 3.3 in §3 narrows alignment to overlap *differences with a remainder*; §4.1 prose makes it sound like a hard exclusion. Soften or recheck.

### Repetition across sections

Load-bearing repetition (keep):
- The alignment/accuracy decomposition is restated in abstract, §1, §3.2, §3.5, §4 (Fig 3), §7. For a 14-page methods paper, reviewers often skim — these restatements help self-contained reading. Keep.

Bloat repetition (cut):
- "Three open questions" appears in §1 list and is "restated" at end of §2.3 (p.3). Either drop the §2.3 restatement or compress it to a one-sentence pointer ("We answer the three questions of §1 in Section 3").
- "Switching alignment from impressed → unimpressed raises winner accuracy 70% → 80%" appears in §5.1 prose, Figure 5 caption discussion, and §5.4 ablation paragraph (p.10). Once in §5.1 + once in §5.4 with a "as quantified above" pointer is enough.

### Abstract → Introduction → Conclusion arc

Inconsistencies:

1. **Abstract says** "significantly improves offline–online correlation and experiment winner prediction." **Conclusion says** "improved offline–online agreement and outperformed accuracy-only and heuristic alignment baselines." Same claim, different verbs. Pick one phrasing — "offline-online correlation" is more precise and matches Table 1's Spearman framing.

2. **Abstract says** "two-part training objective outperforms both an accuracy-only preranker and our heuristic alignment+accuracy production model in multiple A/B tests." **Conclusion is silent on the heuristic baseline.** Add it back: "outperformed both accuracy-only and heuristic alignment+accuracy production baselines in live A/B tests."

3. **Numbers:** The abstract gives no numbers; the intro gives no numbers; the conclusion gives no numbers. RecSys reviewers want at least one headline result up front. Suggest: add to the abstract — "+1.43% save engagement over an accuracy-only baseline and +0.62% over a heuristic alignment baseline in two-week A/B tests."

4. **Exclusivity claim:** Strong in abstract ("(i) *exclusive*"), strong in §1 ("Apart from orthogonal considerations like diversity/fairness, no third independent scalar type is needed"), but the conclusion does not restate the exclusivity result. Reviewers will notice. Add one sentence.

## ACM / RecSys FORMATTING NOTES

- **Title page:** "Conference'17" placeholder → must be replaced with "RecSys '26" before submission. Standard ACM gotcha.
- **CCS subcategories:** "Information systems → Recommender systems; Learning to rank; Theory of computation → Machine learning theory" — Learning to rank is correctly nested, but the ACM 2012 CCS path requires explicit hierarchy. Spell it out: "Information systems → Information retrieval → Retrieval models and ranking → Learning to rank." Verify in ACM CCS tool before camera-ready.
- **Author affiliations:** All 13 authors listed as "Pinterest, San Francisco." ACM camera-ready usually wants full affiliation block per author with email. Currently flat — confirm Hedi has the per-author block.
- **Theorem/Proposition numbering:** Pages 6 + 11 use Proposition 3.1, 3.2, Theorem 3.3, 3.4, then Proposition A.2, Theorem A.3. **Where is Proposition A.1?** Either A.1 exists in §A.1 (not captured) or the numbering jumped — check.
- **Header capitalization:** Section titles look mixed: "Theoretical Decomposition" vs "Offline metric/loss design" (lowercase 'metric/loss'). ACM standard is title case. Audit.
- **Equation numbering:** The conclusion refers to "per-segment coefficients in (8)" — verify equation 8 exists and is the right reference.
- **Reference [18]** lists "Yang Song, Haijun Zhao, Rui Huang, Beichuan Zhang, Na Mou, Yanan Niu, Kai Zheng, Hongning Wang, Kun Gai 2023" and **Reference [23]** lists "Kai Zhang, Haijun Zhao, Rui Huang, Beichuan Zhang, Na Mou, Yanan Niu, Yang Song, Hongning Wang, Kun Gai 2024" — overlapping author sets across two refs. Verify these are distinct papers, not duplicate entries.
- **Reference [5] and [16]** include co-authors who are also paper authors (Hedi Xia, James Li). Standard practice — fine — but verify the citations are formatted in the same style as third-party refs (no "et al." truncation that drops the in-house authors).
