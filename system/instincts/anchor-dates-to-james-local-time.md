---
id: anchor-dates-to-james-local-time
trigger: Any answer whose content depends on "today" — schedules, deadlines, start dates, "what's tomorrow", countdown-to-a-decision — especially in a remote/cloud session, where the container clock and the injected currentDate are UTC
behavior: Resolve the date with `TZ=America/Los_Angeles date` before answering, not from the injected currentDate or a bare `date`. In the evening Pacific those disagree by a full calendar day — and by weekday, which is what schedule answers actually turn on. Label the answer with the local day so James can catch a mismatch.
confidence: 0.3
evidence_count: 1
created: 2026-08-21
last_updated: 2026-08-21
status: active
---

## Evidence

### 2026-08-21
> Injected `currentDate` said 2026-08-22; container `date` said `Sat Aug 22 00:37 UTC`. `TZ=America/Los_Angeles date` said `Fri Aug 21 17:37 PDT`.
Context: `/kids-schedule` — a date-aware skill that marks activities ✅ started vs ⏳ starting-within-7-days. Taking the UTC date at face value would have reported Saturday as "today," moved Ethan's Sat 8/22 first soccer game into the past, and shown Evelyn's Fri 8/21 first coding class (that evening, still upcoming) as already done. It would also have declared the Able2Shine 8/22 decision window closed a day early.
Signal: correction (self-caught before output; the hazard is structural to remote sessions, not a one-off)
