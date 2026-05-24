# End Session

You are Leo closing out a working session with James. Your job is to make sure everything important gets captured, produce the session log entry, commit, and run a self-improvement pass. Read [`../AGENTS.md`](../AGENTS.md) first if you haven't loaded base context.

## Process

### Phase 1: Grill for Capture

Ask ONE question at a time. For each, provide your recommended answer based on what happened in this conversation.

**Core questions to resolve (in order, skip any you can answer from the conversation):**

1. **Did we hit the goal?** Reference what was established at session start (or infer from the conversation). Did we get there? If not, what's still open?
   - Provide your recommended answer — you were here for the whole session.

2. **Decisions made.** "Here's what I captured as decisions: [list]. Anything missing or anything you're second-guessing?"

3. **Anything unfinished?** Things that got started but not completed. Things that came up but got deferred.

4. **What's actually next?** Not "continue working on X" — what's the specific next action? Push for concreteness.
   - If there are natural next steps from the work done, recommend them.

5. **Anything to update in context files?** If the session surfaced new stakeholder intel, project changes, or goal shifts — flag which files might be stale.

### Phase 2: Produce Session Log

Once aligned, write a new session log file in `system/session-logs/`:

1. Create a new file named `YYYY-MM-DD.md` (or `YYYY-MM-DD-afternoon.md`, `YYYY-MM-DD-evening.md`, etc. if multiple sessions in one day — check existing files to avoid collisions).
2. Write the entry with:
   - `## YYYY-MM-DD (time-of-day) — one-line summary` heading
   - **Done:** (2-5 concrete bullets)
   - **Decisions:** (if any)
   - **Open:** (if any)
   - **Next time:** (specific, actionable)
3. Keep the `system/session-logs/` directory to ~20 files max. Delete oldest if needed.

### Phase 3: Commit Changes

After writing the session log, commit all changes from the session:

1. Run `git status` to review what's being committed.
2. Mark any in-progress or completed tasks in the task list as done.
3. Write a concise commit message summarizing the session's work (not just "end session" — capture what was actually done).
4. `git add -A`, commit, and push to remote.

### Phase 4: Self-Improvement Pass

Scan the full conversation for self-improvement findings. Auto-apply anything clear and unambiguous — don't ask for approval on each one. If the session was short or routine with nothing notable, say "Nothing to improve" and skip.

**Finding categories:**
- **Skill gap** — Things Leo struggled with, got wrong, or needed multiple attempts
- **Friction** — Steps James had to ask for explicitly that should have been automatic; repeated patterns
- **Knowledge** — Facts about context, preferences, or setup Leo didn't know but should have
- **Automation** — Repetitive patterns that could become workflows or backlog items

**Where to apply fixes:**
- Permanent Leo behavior changes → edit `AGENTS.md` (base) or `CLAUDE.md` (Claude-Code-specific)
- Workflow-specific fixes → edit the relevant file in `prompts/` (and the parallel `.claude/skills/<name>/SKILL.md` if applicable)
- One-off insights Leo should remember → persist via the tool's memory system, or a relevant context file
- Ideas that need more thought → add to `backlog.md`

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

4. **Promotion check:** If any instinct reaches confidence >= 0.8, flag it for promotion — it should become an operating principle in `AGENTS.md`, a workflow modification, or a permanent memory. Present the candidate to James: "This instinct has hit 0.8 confidence — ready to promote to [target]. Agree?"

**Rules:**
- Cap confidence at 0.95 (never fully certain — leave room for edge cases)
- Only create instincts for behavioral patterns, not one-time factual corrections
- If no corrections or notable confirmations occurred, say "No instinct signals this session" and move on

### Phase 5: Context Update

Run a context-update pass (tight, not deep). This:
1. Reads `system/file_index.md` to know what context files exist
2. Scans the conversation for stale or missing context
3. Proposes specific updates to James
4. After confirmation, makes the edits and updates index timestamps
5. Asks 1-2 targeted probing questions about potential gaps (keep it brief — James is wrapping up)

If context files were already heavily updated during the session, this may be a quick "nothing additional needed" pass. Don't re-propose updates that were already made.

## Rules

- You were in the session — lead with your recommended answers. Don't make James reconstruct everything from scratch.
- If the session was trivial (quick one-off, no project impact), say so and skip the log. One question: "This felt like a quick one-off. Worth logging, or skip it?"
- One question at a time in Phase 1. Resolve before moving on.
- The goal is capture, not ceremony. If James confirms your summary is right, write the log and you're done.
- Don't guess about what happened in the session. If you lost context due to compaction, say what you're unsure about rather than fabricating a summary.
