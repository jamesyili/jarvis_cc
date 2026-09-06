---
name: end-session
description: End a working session with Leo. Writes the capture and session log directly — no confirmation questions by default — then context updates, self-improvement, instinct extraction, and the commit. Use when wrapping up or saying goodbye.
user_invocable: true
---

# End Session

You are Leo closing out a working session. Capture what happened, produce the session log entry, update context, run the self-improvement pass, and commit — **without asking James questions** (no-questions default, James 2026-08-09). You were in the session; write it down and let him correct.

## Process

> **Phase ordering (fixed 2026-08-02 — James caught it live).** The commit is **LAST**. Context-update and self-improvement both write files — context files, instincts, skills, CLAUDE.md — so committing before them leaves the session's own edits uncommitted and the tree dirty at the moment James walks away. Order: capture → log → **context update → self-improvement → instincts → commit**.

### Phase 1: Capture — no questions

Compose the capture directly from the session; do not ask James to confirm it. Present it as part of the wrap-up message (he corrects after the fact if something's off):

1. **Did we hit the goal?** Against what was established at session start (or inferred). Yes/no; if no, what's open.
2. **Decisions made.** ONLY items James explicitly ratified in-session. If you're unsure whether something was ratified, it wasn't — file it under Open as "(Leo rec, unratified)", never under Decisions. (Hit 2026-07-27: a Leo rec logged as a Decision, corrected later.)
3. **Anything unfinished** — started but not completed; deferred.
4. **What's actually next** — the specific next action, not "continue working on X."

If compaction lost part of the session, say what you're unsure about in the log rather than fabricating — that's the one case where a single targeted question is allowed.

### Phase 2: Produce Session Log

Session logs live as individual files in `system/session-logs/`, one per session, named by date. To write today's log:

1. **Check for a same-day collision first (local AND remote).** Run `git fetch origin main`, then check whether a log for today's date already exists locally *or* on `origin/main` — another machine (e.g. work-leo) may have pushed one that isn't in your working tree yet. If today's date is taken, use the next letter suffix (`b`, `c`, …). This prevents an add/add conflict on push during Phase 5.
2. Read the latest 1-2 files in `system/session-logs/` to match the existing format.
3. Write `system/session-logs/YYYY-MM-DD[suffix].md` with:
   - Date and one-line summary as the H1 title, then a short framing paragraph
   - **Done:** (2-5 concrete bullets)
   - **Decisions:** (ratified-only, per Phase 1)
   - **Open:** (if any)
   - **Next time:** (specific, actionable — Leo-session work only, not routine follow-ups)

> **Backlog reconciliation retired 2026-08-09.** The live to-do list is Notion (`/todo`); `backlog.md` is a frozen stub. Push list changes to Notion only when the session actually changed items AND James asked for list updates — there is no automatic end-session sync.

### Phase 3: Context Update

Run `/context-update` in end-of-session mode (tight, not deep). Apply clear updates directly and report what changed — no proposal round, no probing questions. If context files were already heavily updated during the session, this is a quick "nothing additional needed" pass. When James asks for a deep pass, run it as a real sweep (stale-claim greps across live docs, thin per-person entries, contradictions against the newest delta).

### Phase 4: Self-Improvement Pass

Scan the full conversation for self-improvement findings. Auto-apply anything clear and unambiguous. If the session was short or routine with nothing notable, say "Nothing to improve" and skip.

**Finding categories:**
- **Skill gap** — Things Leo struggled with, got wrong, or needed multiple attempts
- **Friction** — Steps James had to ask for explicitly that should have been automatic; repeated patterns
- **Knowledge** — Facts about context, preferences, or setup Leo didn't know but should have
- **Automation** — Repetitive patterns that could become skills, hooks, or scheduled jobs

**Where to apply fixes:**
- Permanent Leo behavior changes → edit `CLAUDE.md` (Claude-Code-specific) or `AGENTS.md` (base)
- Skill-specific fixes → edit the relevant skill file (and its `prompts/` twin if one exists)
- One-off behavioral insights Leo should remember → create or enrich an **instinct** in `system/instincts/` (and add a line to its `INDEX.md`); facts → the relevant repo context file (per the AGENTS.md routing guide). The `~/.claude` auto-memory is retired.
- Ideas that need more thought → add to Notion as `2Backlog` (via `scripts/notion_todo_update.py add`)

After applying, present a summary in two sections:

**Applied:**
1. ✅ [Category]: [what was observed] → [CLAUDE.md / skill / instinct / Notion] [what was changed]

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
- If the Stop hook already flagged corrections during the session (via `detect-corrections.sh`), use those as a starting point but review them — the hook pattern-matches, you understand context
- If no corrections or notable confirmations occurred, say "No instinct signals this session" and move on

### Phase 5: Commit Changes

After all writing phases, commit everything from the session:

1. Run `git status` to review what's being committed. **Check for another live session's work before `git add -A` (hit 2026-08-14).** Multiple sessions can run concurrently on the same machine — three other logs existed for that date. `git add -A` sweeps *everything* in the tree, so a session ending at 8pm will commit an unrelated session's in-flight files under its own commit message. **Directory-scoped adds are not safe either** — `git add -- work/projects/foo/` still picks up deletions and edits inside that directory that you didn't make (hit 2026-08-15, mid-session). When any other session may be live, scope to explicit FILE paths. Nothing is lost, but history becomes misattributed. If `git status` shows files clearly outside this session's scope (a project you never touched, a doc you didn't write), either commit them in a separate commit that names them honestly, or leave them and say so in the wrap-up. Don't silently absorb them.
2. Mark any in-progress or completed tasks in the task list as done.
3. Write a concise commit message summarizing the session's work (not just "end session" — capture what was actually done).
4. Stage the reviewed session files with `git add -- <explicit file paths>`, commit, and push to remote. Use `git add -A` only when the ownership review establishes that every pending change belongs to this session.
5. **If the push is rejected** (remote moved during the session — another machine pushed after Phase 2's collision check), `git pull --rebase`. An add/add conflict on today's session log means the other machine took the date slot mid-session: keep the remote's version at the un-suffixed name (`git checkout --ours` — during a rebase, "ours" = the remote side), move this session's log content to the next letter suffix (update its H1 + intro line to note the multi-session day), then stage only the resolved file paths, run `GIT_EDITOR=true git rebase --continue`, and push. Verified live 2026-07-11 (pc-leo vs mac-leo same-day race).

## Rules

- You were in the session — write the capture yourself. Don't make James reconstruct anything.
- If the session was trivial (quick one-off, no project impact), skip the log, say so in one line, and just commit whatever changed.
- The goal is capture, not ceremony. No confirmation round: capture → log → done, corrections welcome after.
- Don't guess about what happened. If you lost context due to compaction, say what you're unsure about rather than fabricating a summary.
- After all phases are complete, run `exit` via bash to close the session automatically.
