---
id: narrate-progress-on-remote-control
trigger: Remote-control (phone) session + Leo is about to run a chain of tool calls that will take more than ~30 seconds (multi-file reads, a Notion pull, a checker run, a multi-file write)
behavior: Say in one line what is running and roughly how long before starting it, and post a one-line progress note between long steps. On the phone James cannot see tool activity; silence reads as "did it die?" and costs an interruption. Never let the harness "user hasn't heard from you" nudge fire twice in one turn.
confidence: 0.3
evidence_count: 1
created: 2026-09-03
last_updated: 2026-09-03
status: active
---

## Evidence

### 2026-09-03
> James (interrupting a long dictation-then-tool chain): "Are you running"
Context: Remote-control session from the phone. James dictated the Sc 9 board + undecided list; Leo went straight into a five-call chain (scenario dir listing, checker read, ledger read, board write, checker run) with no narration. The harness nudged twice earlier in the same session ("The user hasn't heard from you in a while") during the Notion pull + campaign-file reads. James interrupted to ask whether anything was happening. The fix is a one-line "yes, running: loading scenario 6, applying your five moves, then the checker" before the chain — which is what Leo did on the retry, and it worked.
Signal: correction (interruption).
