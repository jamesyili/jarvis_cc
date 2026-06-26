---
id: main-context-for-sequential-writes
trigger: When a task involves 5+ sequential query-then-edit-to-file steps
behavior: Run it in main context, not a spawned agent — spawned agents don't reliably persist Edit calls between steps (observed work loss). Delegate read-only fan-out freely; keep sequential edit-between-step work in the main loop.
confidence: 0.5
evidence_count: 1
created: 2026-06-26
last_updated: 2026-06-26
status: active
---

## Evidence (migrated from feedback_main_context_for_sequential_writes, 2026-05)
> For 5+ sequential queries-and-edits-to-file, run in main context. Spawned agents don't reliably persist Edit calls between steps.
