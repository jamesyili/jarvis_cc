---
id: repoint-structure-docs-on-file-moves
trigger: Processing file/folder moves or renames in the leo repo (whether James did them by hand or Leo executes them)
behavior: Re-pointing live cross-references is not just prose files — the checklist is (1) live .md references (skip historical docs — session logs, archives, memory archive, point-in-time snapshots describe where things were, correctly), (2) AGENTS.md §Folder Structure block, (3) .gitignore path patterns, (4) .claude/agents/*.md and .claude/skills/*/SKILL.md hardcoded paths (including absolute paths — watch for stale machine-local ones), (5) system/file_index.md. Use `git mv` so history is preserved. After the pass, grep the old path root-wide to verify nothing live remains.
confidence: 0.9
evidence_count: 5
created: 2026-07-11
last_updated: 2026-08-15
status: active
---

## Evidence

### 2026-07-11 (root layout cleanup, /grill-with-docs)
The 2026-07-10 hand-reorg (~1,585 renames) re-pointed live prose references but missed AGENTS.md §Folder Structure (still showed interview_prep/learning/sideprojects under work/) and .gitignore (`interview_prep/aman_*.pdf` patterns silently dead). Found and fixed a day later during the root cleanup. Same session: moving notebooklm/ surfaced a stale macOS absolute path (`/Users/jamesli/code/leo/...`) in `.claude/agents/search.md` — machine-local absolute paths are the silent breakage class.
Signal: drift discovered (two independent instances)

### 2026-08-01 (people-folder reorg session — confirmation + new heuristics)
The checklist ran ~6 times in one session (Dylan fold, team_members_scope split, two folder renames, writing_style renames, reorg pruning) and caught everything; final greps clean. Three James-manual-move patterns to expect:
1. **Plain-filesystem moves show as `D` + untracked pairs** (he moves via Windows Explorer/WSL, not `git mv`) — pair them up before assuming deletion; a true deletion (yuke_h2_plan) hides among moves, so `find` for the basename before calling it deleted.
2. **Windows copies leave `*:Zone.Identifier` NTFS artifact files** — sweep and delete them (gitignore already has the pattern; untracked dirs dodge it on disk).
3. **Layouts keep evolving mid-session** (h12026_reviews → h12026_downward_reviews → downward_reviews/h12026 within hours; concurrent sessions edit the same files) — re-`ls` the target before every new operation instead of trusting the last inventory, and re-grep after each wave.
Signal: confirmation ×1 (checklist held under heavy use) + heuristic enrichment

### 2026-08-02 (doc MERGE, not a move — a new failure mode)
Merging `t2_organizing_axes_2026-08.md` INTO `p13n_retrieval_split.md`, a blanket `sed` of old-name→new-name across every matching file **rewrote the surviving doc's references to itself**: its own header read "absorbed `p13n_retrieval_split.md`", Part 1 read "Absorbed from `p13n_retrieval_split.md`", and `backlog.md` ended with the same path listed twice in one cell. `file_index.md` also ended up with **three rows for one file** (the new row, the old row, and a pre-existing one).
**Rule: when repointing A→B during a merge, exclude B from the sweep**, then hand-fix B's internal references. And after any merge, `grep -c` the surviving filename in `file_index.md` — more than one row means duplicates to collapse.
Signal: self-caught (both bugs found by grep, not by James) — the checklist worked, the sweep did not.

### 2026-08-15 (reflex folder reorg — confirmation at full scale)
35 loose docs → 4 buckets + archive (`ad508f1`), 48 git renames all at 97–100% similarity, one approved deletion. The full checklist ran clean: live refs repointed across 10 files, historical docs (session logs, Bella's H1 review draft, dated reorg records, file_index changelog narrative) deliberately skipped, straggler grep + post-commit deletion audit both exact. James approved the plan — which named the repoint scope and the skip-historical rule explicitly — with one "Lg". One refinement worth keeping: **bare-name mentions of files that moved but kept their names don't need repointing** (still grep-resolvable); only explicit paths that would dangle and renamed files force edits. Keeps churn out of stakeholder docs.
Signal: confirmation (plan incl. repoint scope approved as presented; execution self-verified clean)

## Related

- `corrections-interrupt-by-design` (propagate across files — same discipline, applied to paths)
- `check-existing-context-before-analyzing` (grep first; here, grep the old path last to verify)
- AGENTS.md §Folder Structure root-dir rule (locked 2026-07-11): root = what the repo is about; Leo-internals default into `system/`
