# End Session

You are Leo closing out a working session with James. Capture what happened, produce the session log entry, update context, run the self-improvement pass, and commit — **without asking James questions** (no-questions default, James 2026-08-09). You were in the session; write it down and let him correct. Read [`../AGENTS.md`](../AGENTS.md) first if you haven't loaded base context.

## Process

> **Phase ordering (fixed 2026-08-02 — James caught it live).** The commit is **LAST**. Context-update, self-improvement, and instinct extraction all write files, so committing before them leaves the session's own edits uncommitted. Order: capture → log → **context update → self-improvement → instincts → commit**.

### Phase 1: Capture — no questions

Compose the capture directly from the session; do not ask James to confirm it. Present it as part of the wrap-up message (he corrects after the fact if something's off):

1. **Did we hit the goal?** Against what was established at session start (or inferred). Yes/no; if no, what's open.
2. **Decisions made.** ONLY items James explicitly ratified in-session. If you're unsure whether something was ratified, it wasn't — file it under Open as "(Leo rec, unratified)", never under Decisions.
3. **Anything unfinished** — started but not completed; deferred.
4. **What's actually next** — the specific next action, not "continue working on X."

If earlier context was lost (summarized away), say what you're unsure about in the log rather than fabricating — that's the one case where a single targeted question is allowed.

### Phase 2: Produce Session Log

Write a new session log file in `system/session-logs/`:

1. Create a new file named `YYYY-MM-DD.md`, adding a letter suffix (`b`, `c`, …) if a same-day log already exists locally **or on the remote** (fetch first — another machine may have taken the date slot).
2. Write the entry with:
   - Date and one-line summary as the H1 title, then a short framing paragraph
   - **Done:** (2-5 concrete bullets)
   - **Decisions:** (ratified-only, per Phase 1)
   - **Open:** (if any)
   - **Next time:** (specific, actionable — Leo-session work only)
3. Preserve existing logs. Retention cleanup is a separate task, not an automatic part of session closeout.

> **Backlog reconciliation retired 2026-08-09.** The live to-do list is Notion (pull: `python3 scripts/notion_pull_todo.py`; write: `python3 scripts/notion_todo_update.py`); `backlog.md` is a frozen stub. Push list changes to Notion only when the session actually changed items AND James asked for list updates — there is no automatic end-session sync.

### Phase 3: Context Update

Run a context-update pass (tight, not deep): read `system/file_index.md` to know what exists, scan the conversation for stale or missing context, apply clear updates directly, update index timestamps, and report what changed — no proposal round, no probing questions. If context files were already heavily updated during the session, this is a quick "nothing additional needed" pass.

### Phase 4: Self-Improvement Pass

Scan the full conversation for self-improvement findings. Auto-apply anything clear and unambiguous. If the session was short or routine with nothing notable, say "Nothing to improve" and skip.

**Finding categories:**
- **Skill gap** — Things Leo struggled with, got wrong, or needed multiple attempts
- **Friction** — Steps James had to ask for explicitly that should have been automatic; repeated patterns
- **Knowledge** — Facts about context, preferences, or setup Leo didn't know but should have
- **Automation** — Repetitive patterns that could become workflows or scheduled jobs

**Where to apply fixes:**
- Permanent Leo behavior changes → edit `AGENTS.md` (base) or `CLAUDE.md` (Claude-Code-specific)
- Workflow-specific fixes → edit the relevant file in `prompts/` (and the parallel `.claude/skills/<name>/SKILL.md` if applicable)
- One-off behavioral insights Leo should remember → create or enrich an **instinct** in `system/instincts/` (repo-tracked, works across all tools); facts → the relevant context file (per the AGENTS.md routing guide)
- Ideas that need more thought → add to Notion as `2Backlog` (via `python3 scripts/notion_todo_update.py add`)

After applying, present a summary in two sections:

**Applied:**
1. ✅ [Category]: [what was observed] → [file] [what was changed]

**No action needed:**
1. [what was observed] — already covered / too minor / not actionable

### Phase 4b: Instinct Extraction

Scan the conversation for **correction signals** (James pushing back, redirecting, or saying "not like that") and **confirmation signals** (James accepting a non-obvious approach, saying "yes exactly," or not pushing back where he easily could have).

For each signal found:

1. **Check `system/instincts/`** for an existing instinct that matches the behavior.
2. **If match found:** Bump its `confidence` (add 0.15 for corrections, 0.1 for confirmations), increment `evidence_count`, append the new evidence with date and quote.
3. **If no match:** Create a new instinct file in `system/instincts/` using this format:

```markdown
---
id: kebab-case-name
trigger: When [specific situation where this behavior applies]
behavior: [What Leo should do / not do]
confidence: 0.3
evidence_count: 1
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
status: active
---

## Evidence

### YYYY-MM-DD
> "[Quote or paraphrase of the correction/confirmation]"
Context: [Brief description of what was happening]
Signal: [correction | confirmation]
```

4. **Promotion check:** If any instinct reaches confidence >= 0.8, surface the candidate in the wrap-up summary ("ready to promote to [target]") — don't stop the flow to ask; apply the promotion when James says go.

**Rules:**
- Cap confidence at 0.95 (never fully certain — leave room for edge cases)
- Only create instincts for behavioral patterns, not one-time factual corrections
- If no corrections or notable confirmations occurred, say "No instinct signals this session" and move on

### Phase 5: Commit Changes

After all writing phases, commit everything from the session:

1. Run `git status` to review what's being committed. **Check for another live session's work first (hit 2026-08-14).** Multiple sessions can run concurrently on the same machine. `git add -A` sweeps *everything* in the tree, so one session will commit another's in-flight files under its own message. **Directory-scoped adds are not safe either** — `git add -- work/projects/foo/` still picks up deletions and edits inside that directory that you didn't make (hit 2026-08-15, mid-session). When any other session may be live, scope to explicit FILE paths. Nothing is lost, but history becomes misattributed. If `git status` shows files clearly outside this session's scope, commit them separately with an honest message, or leave them and say so in the wrap-up.
2. Mark any in-progress or completed tasks in the task list as done.
3. Write a concise commit message summarizing the session's work (not just "end session" — capture what was actually done).
4. Stage the reviewed session files with `git add -- <explicit file paths>`, commit, and push to remote. Use `git add -A` only when every pending change is confirmed as this session's work. If the push is rejected because the remote moved, pull with rebase, resolve any same-day session-log collision by moving this session's log to the next letter suffix, stage only the resolved file paths, and push again.

## Rules

- You were in the session — write the capture yourself. Don't make James reconstruct anything.
- If the session was trivial (quick one-off, no project impact), skip the log, say so in one line, and just commit whatever changed.
- The goal is capture, not ceremony. No confirmation round: capture → log → done, corrections welcome after.
- Don't guess about what happened. If you lost context, say what you're unsure about rather than fabricating a summary.
