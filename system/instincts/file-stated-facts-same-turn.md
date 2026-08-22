---
id: file-stated-facts-same-turn
trigger: James states an outcome or status fact in conversation (a promo landed, an item resolved, a decision concluded, an event happened) — especially one originating outside this repo's view (work-leo, live meetings, Slack)
behavior: Write the fact to its routed context file in that same turn — not at end-session, not batched. Verbally-reported facts that never land in a file effectively don't exist next session, and worse, the stale record resurfaces them later as live risks or open items James already closed. "I already told you" is the failure signal. Corollary — before flagging anything as an open risk in an analysis or sweep, check whether its record carries a date older than a James statement that could have closed it; prefer "status as of <date> — confirm" over asserting the risk as current.
confidence: 0.5
evidence_count: 2
created: 2026-08-13
last_updated: 2026-08-22
status: active
---

## Evidence

### 2026-08-13
> "JJ got the promo. I already told you."
Context: In the missing-anything sweep, Leo flagged JJ's IC16 case as a live risk ("sits at Jeff's round with Kurchi sniping — a miss makes the cost-line owner a flight risk") when James had already reported the promo landed in an earlier conversation that never got filed. The repo record still said "submitted 7/10, pending." James had to repeat the outcome; the stale record actively misinformed the sweep. Related: work-leo-execution-scope (the two instances don't share state — the file IS the shared state, which is why same-turn filing matters).
Signal: correction

### 2026-08-22
> Five screenshot dumps across one Saturday session (T&S investigation, Dylan CQ grant, Qinglong WG update, David session, UPP L1 thread) — each filed to its routed file within the same turn it arrived; the session log at day's end was assembly, not archaeology.
Context: The debrief-heavy 8/22 session ran the behavior as designed throughout; James never had to repeat a fact, and mid-session dumps (e.g. Matt's promo history) were already on file when later dumps (the motive statement) needed them for context. Practice confirmed by outcome.
Signal: confirmation
