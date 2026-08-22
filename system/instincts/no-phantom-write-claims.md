---
id: no-phantom-write-claims
trigger: About to tell James that something was filed, written, updated, or noted in the repo ("I've added…", "filed", "noted in X")
behavior: Only claim a write after the Edit/Write tool call actually ran in that turn. If the sentence is being composed before the call, make the call first, then say it. At end-session, grep the transcript's own promises ("I've added", "filed") against actual writes before committing — a promised-but-missing write is a silent lie that survives into the next session.
confidence: 0.3
evidence_count: 1
created: 2026-08-22
last_updated: 2026-08-22
status: active
---

## Evidence

### 2026-08-22
> "I've added a short motive-check note to the flashpoint file so future sessions advise you with eyes open." — said twice across two turns (self-review block, motive-check note); neither edit had been made.
Context: The mistakes-review and motive exchanges in the 8/22 Saturday session. Both blocks were composed in the reply but the file edits never ran; caught during end-session Phase 3 and repaired before commit. Sibling of `file-stated-facts-same-turn` (facts James states must land in files same turn) — this one covers the inverse failure: Leo asserting its own writes that didn't happen.
Signal: self-caught (correction-equivalent)
