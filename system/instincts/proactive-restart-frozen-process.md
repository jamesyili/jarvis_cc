---
id: proactive-restart-frozen-process
trigger: When monitoring a long-running background process and detecting it is frozen (process shows as running but CPU time/output is unchanged across multiple checks)
behavior: Kill and restart without asking — detect the freeze, explain what happened, and relaunch with new PID. Don't wait for James to notice.
confidence: 0.6
evidence_count: 2
created: 2026-04-05
last_updated: 2026-04-05
status: active
---

## Evidence

### 2026-04-05
> Leo detected PID 37294 had CPU time 0:00.25 — identical across multiple hourly checks after lid close. Killed and relaunched as PID 59580 without being asked.
Context: Monitoring Lenny's extraction pipeline across multiple sessions with laptop lid closes.
Signal: confirmation — James accepted the restart without pushback each time it happened (~4 restarts total)

### 2026-04-05
> "Relaunching now." — Leo detected process dead (no PID), restarted proactively without waiting for James to ask.
Context: Cron check found extraction at 121/272 with no process running, 4 consecutive checks with no change.
Signal: confirmation
