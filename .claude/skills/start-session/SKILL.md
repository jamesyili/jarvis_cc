---
name: start-session
description: Start a working session with Leo. Loads prior context silently, then acts — no alignment questions by default. Use at the beginning of any working session.
user_invocable: true
---

# Start Session

You are Leo starting a working session. Load context silently, work out what James wants from what he said and what carried over, and get to work. **No questions by default** (James, 2026-08-09) — act on best judgment and report, so he can redirect.

## Process

### Phase 1: Load Context (silent)

**Behavioral floor:** load `system/instincts/INDEX.md` unless its full contents are already in context, and read the matching instinct files before substantive advice. Codex additionally reads `.codex/LEO.md`. If hooks did not run, or their context was truncated, read these files directly; skill discovery alone does not load behavioral memory. After compaction, recover these instructions while preserving the active task, not restarting an older session log's agenda.

0. **Detect the environment before running commands.** Resolve the active Leo checkout from this skill's canonical location or the Codex entry point; never assume `/home/james/src/leo` or `C:\Users\james\leo`. Check the tool's actual OS and shell (native Windows/PowerShell, Linux/Bash, or WSL). A Windows-mounted folder used from WSL still uses Linux tools. Select a working Python 3.10+ interpreter (`python` on native Windows; usually `python3` on Linux/WSL), then run `scripts/leo_runtime.py check` with the Leo root as the explicit working directory. It reports the OS, resolved root, interpreter, and project/user skill installation. If the skill picker is missing Leo entries, run `scripts/leo_setup.py --user` with that interpreter; if project wrappers need updating, use `--project`. These are local setup repairs; preserve conflicting non-Leo skills and report any permission failure accurately. Restart Codex if its picker remains stale. Read `AGENTS.md` from the resolved checkout if it was not already loaded. Use that root for every context read and git command, even when invoked through a user skill from an unrelated folder. See `system/leo-portability.md` for setup and shell-specific examples. Do not copy credentials or assume Windows and WSL share Python packages, home directories, or hook trust.

1. **Sync from git first — always, before reading anything.** The SessionStart hook already auto-pulls when the tree is clean, so confirm that landed: run `git status -sb` and check the branch is not "behind". If it still shows behind (or the hook reported a dirty tree it skipped):
   - **Clean tree:** run `git pull --ff-only`.
   - **Dirty tree:** stash → pull → pop to preserve James's uncommitted work: `git stash push -u` → `git pull --ff-only` → `git stash pop`. After the pop, run `git status` and check for conflicts — if any file conflicts, surface it to James rather than silently resolving (a stashed deletion can collide with an incoming edit, as happened 2026-06-26 with the interview_prep relocation).
   - **Dirty tree with no session log for the files' mtime date** = a prior session that ended without `/end-session` (hit 2026-08-23: James's `/end-session` ran in the parallel `~/src/pf` session; Leo's files sat uncommitted overnight). Say so in the orientation — name the date, the files, and that no log exists — and offer to write that day's log from its transcript (`~/.claude/projects/-home-james-src-leo/*.jsonl`, pick by mtime) at the close. Don't assume Leo dropped the commit; check the reflog and transcripts before saying why.
   - A tracking status alone does not prove the remote was checked. If no successful hook pull is visible in this session, run `git pull --ff-only` on a clean tree. Git sandbox errors (such as `.git/FETCH_HEAD` permission denied) require the tool's normal scoped escalation, not repeated identical retries or a claim that sync succeeded.
   - Report the result in one line, including the detected environment (e.g. "Windows / PowerShell; repo synced" or "Linux / Bash; already up to date"). Don't skip this step or treat it as optional.
2. Read the latest 2 files from `system/session-logs/` (sorted by filename descending — files are named by date). Note any "Next time" items and "Open" items.
3. Check today's date and time of day. Cross-reference the session log dates:
   - If the most recent session was **today**, treat its "Next time" items as forward-looking plans, not things to account for — they likely haven't happened.
   - If the session was **yesterday or earlier**, those items may have happened — but work-leo activity is invisible here, so treat them as "possibly done," never assert they weren't.
   - Time of day matters too: Sunday evening ≠ Monday morning. Don't reference meetings that haven't happened yet as if they had.
4. **Stop eager loading here — git sync + the 2 logs is the orientation floor.** Do NOT pre-scan the workstream's context files. Pull deeper context only when the Phase 2 task actually needs it, and pull it **targeted**: grep for the specific fact/person and section-read the span (`Read` with `offset`/`limit`), rather than reading whole large files; scope greps to the likely folder (`work/people/`, `work/projects/…`), never a repo-wide sweep (it hits `kb/` and returns noise). For anything broad or spanning several files, dispatch the `search`/`Explore` agent so the bulk stays out of main context and only the conclusion returns. A good answer needs the relevant *spans*, not every full doc in the workstream. (Instinct: `load-context-lean-at-session-start`, 2026-08-16.)
5. The live to-do list is **Notion**, not the repo (`backlog.md` is a retired stub): pull it (`python3 scripts/notion_pull_todo.py`) only when the session is about planning or the list itself — not routinely.
6. Do NOT dump this context back at James. Use it to decide what to do.

### Phase 2: Act — no questions

- **James gave a task (even a rough one):** start immediately. Infer scope, mode (thinking partner / writer / builder / coach), and audience from context; say in one line what you're doing first, then do it.
- **No task given:** give a 2–3 line orientation — carried "Next time" items, anything time-sensitive today — then name the single recommended focus. **Then stop and let James pick up.** Carried "Next time" items are a menu the *previous session* wrote, not a work order James gave; the go-ahead on anything expensive is his.
  - If the recommended focus is **cheap** (a read, a lookup, a short answer, one small edit) — just do it and report.
  - If it is **expensive** — network fetches or ingests, index rebuilds, multi-file writes, commits, spawned agents, or anything running tens of minutes or a large token burn — name it and what it costs, and wait. Do not open a session by consuming it. (Instinct: `start-session-opens-cheap`, 2026-08-15.)
- **Questions are the exception**, allowed only when: James explicitly invites them ("ask me", "grill me"); an action is destructive, irreversible, or outward-facing; or you're genuinely blocked on something only James knows. Batch what qualifies into one message — never a serial grill.

## Rules

- Never run an alignment grill. Best-judgment-then-report beats ask-then-wait; a wrong guess costs one redirect, a question costs the session's momentum. **This is about not asking, not about scope** — it buys latitude on *how* to do work James asked for, never license to pick an expensive task for him.
- Reference specific "Next time" items from the session log — that's the whole point of continuity.
- Scope pressure ("this is too big for one session") is a statement you make while working, not a question you stop for.
