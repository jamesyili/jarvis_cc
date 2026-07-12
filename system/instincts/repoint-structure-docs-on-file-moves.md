---
id: repoint-structure-docs-on-file-moves
trigger: Processing file/folder moves or renames in the leo repo (whether James did them by hand or Leo executes them)
behavior: Re-pointing live cross-references is not just prose files — the checklist is (1) live .md references (skip historical docs — session logs, archives, memory archive, point-in-time snapshots describe where things were, correctly), (2) AGENTS.md §Folder Structure block, (3) .gitignore path patterns, (4) .claude/agents/*.md and .claude/skills/*/SKILL.md hardcoded paths (including absolute paths — watch for stale machine-local ones), (5) system/file_index.md. Use `git mv` so history is preserved. After the pass, grep the old path root-wide to verify nothing live remains.
confidence: 0.7
evidence_count: 2
created: 2026-07-11
last_updated: 2026-07-11
status: active
---

## Evidence

### 2026-07-11 (root layout cleanup, /grill-with-docs)
The 2026-07-10 hand-reorg (~1,585 renames) re-pointed live prose references but missed AGENTS.md §Folder Structure (still showed interview_prep/learning/sideprojects under work/) and .gitignore (`interview_prep/aman_*.pdf` patterns silently dead). Found and fixed a day later during the root cleanup. Same session: moving notebooklm/ surfaced a stale macOS absolute path (`/Users/jamesli/code/leo/...`) in `.claude/agents/search.md` — machine-local absolute paths are the silent breakage class.
Signal: drift discovered (two independent instances)

## Related

- `corrections-interrupt-by-design` (propagate across files — same discipline, applied to paths)
- `check-existing-context-before-analyzing` (grep first; here, grep the old path last to verify)
- AGENTS.md §Folder Structure root-dir rule (locked 2026-07-11): root = what the repo is about; Leo-internals default into `system/`
