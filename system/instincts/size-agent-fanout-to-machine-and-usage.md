---
id: size-agent-fanout-to-machine-and-usage
trigger: About to launch a multi-agent workflow or fan-out (Workflow tool, parallel Agent calls), especially in a remote/cloud session or late in a heavy day
behavior: Before launching, check two ceilings and size to the smaller one. (1) Machine — concurrency is min(16, CPUs−2); `nproc` on the remote box is 4, so only 2 agents run at a time and a "parallel" 31-agent design is a 2-wide queue (~2 hours). (2) Usage — the subscription session limit; a subagent-heavy session burns it fast (this one: ~1M subagent tokens in 20 minutes before the wall). Prefer few agents with large context over many small ones; cut verification breadth (top-1 per lane, one combined lens) before cutting mappers; make every phase's output land in the repo as it completes so a mid-run kill loses nothing. Tell James the wall-clock and the usage cost in one line before launching, even when ultracode is on — ultracode says thoroughness is the goal, not that the box or the plan can pay for it.
confidence: 0.4
evidence_count: 2
created: 2026-09-05
last_updated: 2026-09-06
status: active
---

## Evidence

### 2026-09-05
> James: "You're going to hit usage limits soon."
Context: Leo launched a 4-mapper → 6-lane → 20-refuter → 1-memo workflow (31 agents) on a 4-CPU remote container. Only 2 ran at once; three mappers finished (~12 min each), then the session limit hit: 8 agents failed, the who-leads deliverable never ran. Leo had estimated ~2 hours when James asked "how much longer" — the right answer was to trim at that moment, not to describe the trade and wait. The three finished maps were recoverable from `journal.jsonl` and were saved to the repo at close; the lane/verify/synthesis phases had produced nothing.
Signal: correction (implicit — the usage warning arrived after Leo's own estimate showed the design didn't fit the box).

### 2026-09-06
> (No complaint.) Leo pre-announced "about five agents total and 30 to 40 minutes" at session open, ran 1 seams agent + a 6-agent refute workflow (2 at a time, ~20 min), saved each phase's output to the repo as it landed. James's only feedback was on the *reporting* register, not on cost or time.
Signal: confirmation.

## Related

- `start-session-opens-cheap` (bounds work James didn't ask for; this bounds work he did ask for to what the machine and the plan can finish)
- `leo-debugging-playbook` skill (session-limit death mid-run is a known failure mode; save intermediate outputs to the repo, not only to the transcript)
