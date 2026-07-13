---
name: leo-proof-and-analysis-toolkit
description: First-principles analysis recipes for the Leo repo, each with a worked example from real history - git forensics, token-cost forecasting from measured priors, staleness proof by mtime, drift audit by retired-term grep, backlog-vs-reality reconciliation, instinct-evidence auditing, and the adversarial-refutation bar for claims about James. Load this when you need to PROVE something rather than assert it - what actually happened in git, what a planned LLM sweep will cost, whether a doc claim matches reality, whether a migration left stragglers, or whether evidence supports a behavioral pattern. Keywords - prove it, forensics, git history, token cost estimate, forecast, mtime, staleness, retired term, straggler, reconcile, evidence audit, refute.
---

# Leo Proof & Analysis Toolkit

"Prove it" here means: command output over doc claims, git evidence over memory, measured cost over vibes. Sibling [leo-validation-and-diagnostics] holds the standing checks; these are the on-demand methods.

## Recipe 1 — Git forensics: what actually happened

**Commands:** `git log --oneline --all` (arc); `git log --grep='Session 2026-'` (narrated history — session-log commits tell the story); `git show --stat <sha>`; `git log --follow <path>` (survives renames); `git log --diff-filter=D --name-status` (what ever got deleted); after bulk moves: `git show <sha> --name-status | awk '{print $1}' | sort | uniq -c` (audit for unexpected `D`).

**Worked example:** the memory round-trip — `git show --stat 2468264` (instincts deleted, 2026-04-04) then the 2026-06-26 twelve-commit reversal (`4dc8020`→`7052047`). And the reorg drop: `git show 4b29b5c --name-status` shows 1,572 R + 13 M + 0 D — the dropped file was restored in-commit, so `git log --follow work/people/daniel_liu_team_2026-07.md` shows a round-trip no-op. Full stories → [leo-failure-archaeology].

## Recipe 2 — Token-cost forecasting from the measured prior

The repo's one hard datapoint (`kb/.kb/graph/GRAPH_REPORT.md`): graphify Phase 1 = **1,992,800 input / 415,600 output tokens for 2,688 files (~9.8M words)** ≈ ~740 input tokens/file for extraction-class work.

**Method:** count target files → multiply by the prior → compare against the session budget → decide (run / chunk / defer / ask James). State the expected number BEFORE running — hypothesis-predicts-numbers is the house discipline.

**Cost of skipping this:** the 13 lost chunks (Phase 1 died on the limit), and the 2026-07-12 authoring workflow — 17 agents, >1M tokens, zero returns. Design long runs to checkpoint and resume.

## Recipe 3 — Staleness proof by mtime-vs-claim

```
stat -c '%y' <artifact>
find <source-tree> -name '*.md' -newer <artifact> | wc -l
```
**Worked example:** `find kb/hard/raw kb/soft/raw -name '*.md' -newer kb/.kb/search_index.json | wc -l` — proves "search is current" true/false without opening a file. (2026-04-05 index vs ~280 later soft articles was the original catch.)

## Recipe 4 — Drift audit by retired-term grep

After any migration/rename, grep **live surfaces only** (`.claude/ prompts/ AGENTS.md CLAUDE.md` — historical dirs are exempt by rule) for the retired vocabulary:

```
grep -rn -e 'Pinsight' -e 'AIContext/' -e '/Users/jamesli' .claude prompts AGENTS.md CLAUDE.md
```
**Worked examples:** Pinsight → zero live hits (clean rebrand, `a5559d4`); `AIContext/` → still in weekly-review (caught drift); the `7052047` straggler — end-session still said "save to auto-memory" weeks after retirement. Lesson: the grep IS the migration's last step, not an afterthought.

## Recipe 5 — Backlog-vs-reality reconciliation

For any Build row you're about to act on, verify the claimed state with a filesystem/git check first. **Worked examples:** "Preserve raw chunks — Not started" vs `ls kb/.kb/graph/raw_chunks/ | wc -l` → 110 (done, silently, and the /tmp original is gone — the backlog's fear had already materialized AND been mitigated); "compile_wiki.py:82/:249" line refs still exact → proves zero drift, i.e., Phase 2 truly untouched.

## Recipe 6 — Instinct-evidence audit

Before trusting or promoting an instinct: read its frontmatter — `confidence` (start 0.3, +0.15/correction, +0.1/confirmation, cap 0.95, promotion gate ≥0.8 per end-session Phase 4b), `evidence_count`, and the dated Evidence entries with `Signal:` types. An instinct with confidence 0.9 and one evidence entry is mis-scored — the trail must support the number. Lifecycle rules → [leo-research-methodology].

## Recipe 7 — The adversarial-refutation bar (claims about James, not code)

Before asserting an accumulation/avoidance/not-done pattern about James: **repo absence ≠ event absence.** work-leo activity and live conversations are systematically invisible here (Karen's blind-spot rule, CLAUDE.md §Karen; instincts `work-leo-execution-scope`, `notes-absence-is-not-event-absence`). Protocol: state the hypothesis, list what evidence WOULD refute it, ask James, then conclude. One mechanism must explain all observations — including the negatives.

## When NOT to use this skill

- Standing health checks → [leo-validation-and-diagnostics] (run the doctor)
- The incidents these recipes reference → [leo-failure-archaeology]
- Deciding build/defer/retire from the analysis → [leo-research-methodology]

## Provenance & maintenance

Authored 2026-07-13; worked-example outputs verified 2026-07-11/12. Re-verify: each recipe is itself a runnable command — run it. The cost prior (Recipe 2) updates whenever a new large LLM sweep completes; record new datapoints in GRAPH_REPORT-style reports and update the prior here.
