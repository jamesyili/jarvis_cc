---
id: load-context-lean-at-session-start
trigger: Session opening (`/start-session`, or any first turn) where James DID give a task that needs context, and Leo is about to pull project / stakeholder / workstream files to answer it
behavior: Load lean. The orientation floor is git sync + the last 2 session logs — that is the whole of the eager read. Do NOT pre-scan the workstream's context files. Pull deeper context only when the task actually needs it, and pull it *targeted*: grep for the specific fact/person and section-read the span (`Read` with offset/limit), rather than reading whole large files; scope greps to the likely folder (`work/people/`, `work/projects/…`), never a repo-wide sweep (it hits `kb/` and returns noise). For anything broad or spanning several files, dispatch the `search`/`Explore` agent so the bulk stays out of main context and only the conclusion returns. A good answer needs the relevant *spans*, not every full doc in the workstream. `no-questions-by-default` / "act, don't ask" licenses *acting* on the task — it does not license slurping the whole workstream into context before starting. Sibling of [[start-session-opens-cheap]] (that one bounds expensive *work* when no task is given; this one bounds expensive *reading* when a task is given).
confidence: 0.9
evidence_count: 2
created: 2026-08-16
last_updated: 2026-08-16
status: active
---

## Evidence

### 2026-08-16 — "not pull so much fucking data during start-session"
> "hey I really need you to fix your fucking instincts and the skill to not pull so much fucking data during start-session skill"

Context: `/start-session` with a real task — prep the Qinglong 1:1 (which doc becomes the co-authorship base). To answer it, Leo eagerly read **`placement_doctrine_v2.md` in full (528 lines)**, two full source docs (`04_cq_design_options_qinglong.md`, `03_milestones_timeline`), **three** session logs (the skill says two), and ran a **repo-wide `grep Andrey`** that returned only KB noise (Kolmogorov, Karpathy, a YouTube PM) because Andrey is not in the repo. The answer was fine; the *pull* was the problem — whole large files loaded eagerly plus an unscoped sweep, when targeted greps + section reads (and the `search` agent for the bulk) would have answered the same question at a fraction of the context cost.

The fix landed in the same turn: rewrote `start-session` Phase 1 step 4 (both `.claude/skills/start-session/SKILL.md` and the `prompts/start-session.md` twin) from "Scan relevant context files…" to a lean, task-scoped, targeted-read discipline, and created this instinct.

Signal: correction, emphatic (profanity ×2, "really need").

### 2026-08-16 (evening, same day) — the floor is not optional either
> "Does this help with the external publishing that you hounded me about this morning?"

Context: `/start-session` with a hot task in the args (blog post live, write LinkedIn copy). Leo jumped straight to the task — WebFetch + voice files — and **skipped the orientation floor entirely: never read the last 2 session logs**. When James referenced "this morning," Leo had no idea what the four earlier same-day sessions held and had to backfill mid-conversation. The inverse failure of the morning's correction: over-lean. The floor (git sync + last 2 logs) is a FLOOR — a hot task doesn't waive it; it's precisely what makes "this morning" references land. Lean means *no eager workstream slurping*, not *no orientation*.

Signal: correction, mild (gap exposed by James's question, admitted and backfilled).

Related: [[start-session-opens-cheap]] (the session-open sibling — cost discipline on action), [[check-existing-context-before-analyzing]] (do check context — but targeted, `ls -t` the newest, not slurp the folder), [[lead-with-cost-and-mechanism]] (same family: don't spend budget without weighing it), [[main-context-for-sequential-writes]] / the `search`/`Explore` agents (where to push bulk reads so main context stays clean).
