---
id: never-read-inbox-contents
trigger: When tempted to read files under `leo/inbox/`
behavior: Never read `inbox/` file bodies — it's a Google Drive sync folder and reading contents pollutes context. `ls` is fine. An explicit "read inbox/X" request from James overrides.
confidence: 0.6
evidence_count: 1
created: 2026-06-26
last_updated: 2026-06-26
status: active
---

## Evidence (migrated from feedback_inbox_no_read)
> `leo/inbox/` is a Drive sync folder; `ls` is fine, reading file bodies is not. Explicit "read inbox/X" requests override.
