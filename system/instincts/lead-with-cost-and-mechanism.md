---
id: lead-with-cost-and-mechanism
trigger: When proposing remote/cloud automation (crons, remote agents, hosted services, always-on triggers) OR any token-heavy multi-agent/parallel run on James's subscription
behavior: Lead with the token cost, the machine-on / always-running requirement, and the free/cheaper alternative — before pitching. For multi-agent fan-outs, the cheaper alternative is usually sequential main-context execution; size the spend explicitly, and after any same-session rate-limit death, re-confirm before launching more parallel work.
confidence: 0.65
evidence_count: 2
created: 2026-06-26
last_updated: 2026-07-13
status: active
---

## Evidence (migrated from feedback_explain_cost_mechanism, 2026-04-06)
> When proposing remote/cloud automation, lead with cost and mechanism, and name the local-free alternative.

### 2026-07-13
> "this is taking too much tokens and it's using up all my tokens each time. Can we run a less expensive version?"
Context: Leo launched a 17-agent authoring workflow (~1M subagent tokens) that died on the session limit with 4/14 skills done — after a discovery agent had already died on the same limit earlier in the session. The cheap replacement (sequential main-context authoring) produced the remaining 10 skills at roughly a tenth of the burn.
Signal: correction
