---
name: leo-validation-and-diagnostics
description: What counts as evidence in the Leo repo, the golden health inventory, and leo_doctor.sh - a read-only 12-check health script. Load this before claiming anything is done/healthy/current, after any structural change or migration (acceptance gates), when starting work on an unfamiliar machine, when docs and reality might disagree, or when you need to measure instead of eyeball (index freshness, instinct integrity, stale paths). Keywords - doctor, health check, validation, acceptance gate, evidence, golden inventory, verify, drift check, is it actually done, measure.
---

# Leo Validation & Diagnostics

## The evidence bar

**Command output beats doc claims.** Two live case studies: `backlog.md` said raw-chunk preservation was "Not started" while 110 files sat on disk (done, silently); CLAUDE.md/AGENTS.md said "five" prompts were flattened while 8 exist. Docs record intent at write-time; the filesystem and git record reality. Before asserting state, run the check. Before asserting a pattern about *James's* behavior (vs. code), the bar is different — ask him first (Karen's blind-spot rule; work-leo is invisible here). See [leo-proof-and-analysis-toolkit] for the analysis recipes behind this.

## The doctor

```
bash .claude/skills/leo-validation-and-diagnostics/scripts/leo_doctor.sh
```

Read-only, portable (derives repo root from its own location), exits 1 only on FAIL. Twelve checks:

| # | Check | Why it matters |
|---|---|---|
| 1 | Exactly 6 non-dot tracked root dirs | The root-dir rule (AGENTS.md, locked 2026-07-11) is the repo's shape contract |
| 2 | GEMINI.md → AGENTS.md symlink | Gemini's entire base context hangs on it |
| 3 | Instinct files == INDEX bullets | A missing INDEX line = an instinct that never fires |
| 4 | 4 hooks wired + executable; hardcode warn | Hooks are the persistence guarantee; hardcodes silently degrade off pc-leo |
| 5 | Stale-path scan on live surfaces | Drift-after-move is the dominant failure class (historical dirs + this library excluded by rule) |
| 6 | Search-index freshness vs newest article | Index never auto-invalidates — silent search quality loss |
| 7 | graph.json present; raw_chunks count | raw_chunks is single-copy + gitignored |
| 8 | Venvs present | Wrong/missing interpreter is the #1 script failure |
| 9 | Google credentials/token | Outbound capability check |
| 10 | Lowercase skill.md shadows | Shadow-bug class (incident `f429fb4`) |
| 11 | Session-log count (INFO) | Documented ~20 trim rule, unenforced by choice |
| 12 | claude CLI on PATH | compile_wiki/graph build dependency |

Expected on a healthy pc-leo as of 2026-07-13: **0 FAIL**, ~5 WARN (all known: pre-compact hardcode, search.md + weekly-review stale paths, index staleness if scout ran recently, raw_chunks single-copy note, 3 lowercase shadows). A *new* WARN is signal — investigate before dismissing.

## Acceptance gates

| After you… | You must… |
|---|---|
| Change KB content (ingest/scout/manual) | `kb_search.py --rebuild` + `kb_lint.py` on the touched domain |
| Move/rename anything | Full repoint checklist ([leo-change-control]) + doctor run + `git diff --name-status` audit for unexpected `D` lines |
| Edit a SKILL.md with a prompts/ twin | Re-sync the flattened prompt (8 exist — prompts/README.md) |
| Retire/migrate a system | Grep every live surface for the retired term (the `7052047` straggler lesson) |
| Finish any session with changes | Commit AND push — then verify push landed |
| Run a long/parallel job | Verify outputs on disk — dirs can exist with zero files inside (2026-07-12 workflow death) |

## Interpreting the measuring tools

- `kb_lint.py`: thin articles = stub-scrape suspects (rescrape class); broken wikilinks + near-dup slugs = wiki hygiene; missing tags on Lenny extractions are a known accepted mass.
- `build_graph.py stats`: compare node/edge/community counts against the 2026-04-08 baseline (6,706 / 8,585 / 593) — any rebuild that shrinks these lost data.
- `kb_search.py --stats`: doc count vs `find kb/*/raw -name '*.md' | wc -l` tells you index coverage.

## When NOT to use this skill

- A check failed and you need the fix → [leo-debugging-playbook]
- The analysis method behind a verdict (git forensics, cost forecasting) → [leo-proof-and-analysis-toolkit]
- Executing the change the gate protects → [leo-change-control]

## Provenance & maintenance

Authored 2026-07-13; doctor test-run same day (13 pass / 5 warn / 0 fail on pc-leo). Re-verify: run the doctor — it IS the re-verification. If repo structure legitimately changes (e.g., a 7th root dir is ratified), update check 1's expected list *and* AGENTS.md §Folder Structure in the same commit.
