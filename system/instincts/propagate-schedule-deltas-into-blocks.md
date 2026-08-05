---
id: propagate-schedule-deltas-into-blocks
trigger: New intel changes the schedule or structure of a plan held in an operational doc (a meeting added/moved/cancelled, an owner or sequence change) and Leo files it as a banner/blockquote note
behavior: Don't stop at the banner. Restructure the doc's action blocks in the same session — a new meeting gets its own prep block (goals / talking points / questions), a moved meeting's block moves, a cancelled one gets collapsed to reference. A banner records the delta; only a block makes the doc operational for it. If restructuring must wait, say so explicitly ("4-way noted, block not yet built") so the gap is visible rather than silent.
confidence: 0.3
evidence_count: 1
created: 2026-08-04
last_updated: 2026-08-04
status: active
---

## Evidence

### 2026-08-04
> "You forgot about the meeting today between Dylan, myself, Yan, and Daniel."

Context: Dylan's 8/3 comm-plan change (her 11:01 AM Slack) was filed into `announcement_week_timeline_2026-08.md` on 8/3 as a schedule-change blockquote — which explicitly listed the 8/4 comm-plan 4-way. But the doc's meeting-block structure was never updated: Tue still led with the superseded Daniel 45-min, and the 4-way — a same-day meeting with Dylan in the room — had no prep block at all. James caught it the morning of the meeting. The information was IN the doc; the doc just wasn't operational for it.

Signal: correction (explicit "you forgot").

## Pattern

Banners/blockquotes are how debrief-time filing captures deltas fast, and that's fine as capture. The failure mode is treating capture as done: an operational doc's value is its action blocks, and a delta that lives only in a banner silently rots the block layer around it. The check at filing time: "does this delta add, move, or kill any meeting/step that has (or needs) a block?" If yes, touch the blocks now or name the debt out loud.
