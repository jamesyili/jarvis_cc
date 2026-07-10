---
id: resolve-dictation-artifacts-against-context
trigger: James's input reads voice-dictated and a project/person name doesn't match known context ("Allen Utility", "PinRec v2", "Oliver"), especially when the name is headed into a work deliverable
behavior: Resolve garbled names against repo context (projects, people, artifacts) and use the canonical name, but flag the mapping explicitly in the reply ("assuming PinRec v2 = Pin Selection v2 (PSv2)") so James can correct. For names Leo cannot resolve from context (new people), carry them verbatim but surface them in a pre-submit spelling check — dictated names are a known error class.
confidence: 0.5
evidence_count: 1
created: 2026-07-09
last_updated: 2026-07-09
status: active
---

## Evidence

### 2026-07-09 (JJ promo package session)
Three name-shaped dictation artifacts in one session:
- "Allen Utility" → resolved silently to L1 Utility (correct — obvious from context).
- "PinRec v2" → resolved to Pin Selection v2 (PSv2) and flagged in-chat; James did not object (correct).
- "Oliver" → written into the draft as heard; James corrected mid-turn: "Olafur not Oliver." Unresolvable from context (new person), but a spelling-confirm nudge for new dictated names would have caught it — and it echoes the 7/9 peer-feedback session's pre-submit name-spelling checklist item (Andreanne, Jia Chong).
Signal: mixed — two confirmations of the resolve-and-flag move, one correction showing the gap for unknown names.
