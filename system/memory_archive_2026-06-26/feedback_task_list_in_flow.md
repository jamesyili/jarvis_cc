---
name: Task list visibility in flow
description: Don't create TaskCreate lists mid-session when James is in flow; they clutter the display
type: feedback
originSessionId: 044981b7-20dd-4393-bf32-f368bb56ec34
---
Don't create a persistent task list during a session that's already in smooth flow, even when the system reminder nudges toward TaskCreate. The task list stays visible to James and becomes noise rather than signal when he's focused on the work itself, not tracking state.

**Why:** In the 2026-04-18 Charlie CPP session, I created 6 tracked tasks mid-flow after a TaskCreate reminder. James said "remove the to-do list in my face right now" — the list was clutter he had to look at, not value he was using.

**How to apply:**
- Use TaskCreate when James has multiple concurrent workstreams he'll be juggling, wants explicit state visibility, or is stepping away and needs resumable state.
- Don't use TaskCreate when we're in a focused, flowing session on one topic — use inline structure (headers, bullets) in the conversation instead. The session log at end-of-session handles what got done.
- If a system reminder nudges TaskCreate and the session is in flow, follow the reminder's own "ignore if not applicable" clause.
- If I've already created tasks and James signals annoyance (or the list has grown past ~3 visible items), delete them immediately.
