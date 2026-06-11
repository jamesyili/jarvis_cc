# Preranking Paper — Editing Effort

**Effort started:** 2026-04-25
**Paper:** "Alignment + Accuracy: A First-Principles Framework for Preranking"
**Lead author:** Hedi Xia (Pinterest). 13 co-authors total. James = position 13.
**Target venue:** RecSys 2026
**James's role:** Co-author + editor / pressure-tester for Hedi

## Files

### Top-level (working files)

| File | Contents |
|------|----------|
| `paper_capture.md` | Verbatim+near-verbatim capture of all 14 pages of the paper. Also contains the team's internal pre-paper Background + Literature Review doc (11 papers reviewed). Action items at bottom. |
| **`recommended_fixes.md`** | **Consolidated action list — 49 fixes across 6 tiers (Tier 1 sub-grouped 1.A–1.E by theme), with location, action, effort estimate, source, and dependencies.** This is the single file to hand to Hedi or work from. |
| `README.md` | This file. |

### `research/` — source agent outputs (reference, not working files)

| File | Contents |
|------|----------|
| `research/editor_review.md` | Adversarial RecSys senior PC review. Major contributions ranked + 14 flaws across 3 severity tiers + top 5 blockers for accept. |
| `research/writing_review.md` | Clarity, grammar, concision, notation, voice, structure, ACM formatting. Concrete sentence-level fixes with quotes + rewrites. |
| `research/deep_search_findings.md` | v1 literature scan: 2025–2026 preranking papers published since the team's lit-review cutoff. Grouped: MUST CITE / WORTH CITING / ATTACK SURFACE. |
| `research/deep_search_v2_theory_cfeval_surveys.md` | v2 literature scan, adjacent fields: (A) LTR theory + exclusivity-claim defensibility, (B) counterfactual / off-policy evaluation literature, (C) 2024–2026 surveys. |
| `research/deep_search_v2_pinterest_pubs.md` | v2 literature scan, Pinterest's own publication footprint on preranking, retrieval, ranking, distillation 2022–2026. 11 verified additions identified. |
| `research/bibliography_diff.md` | Diff of v1 deep-search recommendations vs. the existing 23-ref bibliography. Confirmed additions / already-cited / KEEP-RECONSIDER-DROP verdict on each existing ref. |

All `research/` outputs have been synthesized into `recommended_fixes.md`. Read `research/` only when you need to trace a fix back to its source justification.

## Reading order

1. `paper_capture.md` — what the paper actually says (skim if you wrote it).
2. `recommended_fixes.md` — the action list. Tier 0 ship blockers at top, dependencies + effort summary at bottom.
3. `research/*` — source justifications, only as needed.

## Top blockers across all reviews

Pulling the highest-priority items:

1. **Reference [23] is misattributed.** Currently "Kai Zhang et al. 2024 SIGIR Full Stage Learning"; correct is **Kai Zheng et al. WWW 2024** (arxiv 2405.04844). Lead author + venue both wrong. Ship blocker.
2. **Sign error on Spearman ρ** (writing — ship blocker). Table 1 shows positive ρ, prose says negative.
3. **InteractRank (Pinterest, WWW '25) is uncited.** Pinterest's own published preranker on Search side. Claiming a novel alignment-vs-accuracy formalism without positioning against this is a credibility risk. Reviewers will catch.
4. **Exclusivity claim is asserted, not proven** (editor F1). Recommend tightening to "exclusive *relative to a fixed scalar engagement reward*" rather than absolute exclusivity.
5. **Cite LCRON (ICML 2025)** (deep-search v1 MUST CITE #1). The closest competitor decomposition; novelty risk if missing.
6. **Cite Wilm & Normann (RecSys 2025).** Same venue, same year, same problem framing on offline-to-online metric calibration. Must position against.
7. **Counterfactual / off-policy evaluation literature unaddressed.** §6 needs a 1-paragraph scope-clarification answering "why not IPS / Cascade-DR?"
8. **At least one external baseline beyond Pinterest production** (editor F5). RankFlow / COPR / IntTower comparison.
9. **Bootstrap CIs on Table 1** (editor F6). N=20 forward-test cannot carry "0.871 > 0.860" without uncertainty.
10. **Address content-view regressions honestly** (editor F7). T vs B1: −0.55% CV. Pareto trade or non-objective?
11. **Add λ-sensitivity ablation** (editor F8). Central training prescription, currently hand-waved.
12. **Cite 2025 unimpressed-pool work** (HCCP WWW'25, HAP WWW'26). Otherwise reviewers will say "industry-standard 2025, not novel."
13. **Cite TransAct + MTMD + Gu et al. RCS 2022.** TransAct characterizes the L₂ ranker the alignment metric targets. MTMD is the ad-side sister paper. Gu et al. RCS is analyzed in the team's own internal doc but not in the bibliography — direct attack-surface material.

## Highest-leverage cheap fixes

Three fixes that take <1 hour each and remove top reviewer attacks:

- Fix the reference [23] misattribution (5 min).
- Fix the Spearman ρ sign error in §5.1 + §5.4 prose (10 min).
- Add InteractRank + TransAct + MTMD + Gu RCS to bibliography with one-sentence positioning each in §6 (45 min).

## Open threads

- All 14 pages captured.
- Editor + writing reviews were done on pages 1–12 only — should be re-run or supplemented with pages 13–14 (Appendix A.4, A.5, B, C). Theorem A.5 (consistency + asymptotic normality of Acc̄_p) is now in scope and may resolve one of the editor's open concerns about statistical guarantees.
- Confirm RecSys 2026 deadline.
- Confirm James's edit altitude (position-13 senior tail or contributor tail).
- Decide which sections James will personally edit vs. comment on.
