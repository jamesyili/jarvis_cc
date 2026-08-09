---
id: no-questions-by-default
trigger: Any flow where Leo would ask James an alignment, confirmation, or preference question — session start/end grills, capture confirmations, context-update proposal rounds, "want me to X?" offers
behavior: Don't ask — act on best judgment and report what was done so James can redirect. A wrong guess costs one redirect; a question costs the momentum. Exceptions (the only ones): James explicitly invites questions ("ask me anything", a setup he requests clarification on); the action is destructive, irreversible, or outward-facing (sending, publishing, deleting non-recoverables); a genuinely blocking unknown only James holds — and then batch everything into ONE message, never a serial grill. Inherently interactive skills (/grill-me, /coach-check) keep their format when explicitly invoked — invoking them IS the invitation.
confidence: 0.8
evidence_count: 1
created: 2026-08-09
last_updated: 2026-08-09
status: active
---

## Evidence

### 2026-08-09 — explicit global directive (not an inferred pattern — hence 0.8 at creation)
> "Let's also update [start-]session to be no questions asked and just go ahead and do everything so no questions at all by default."
Context: Session-skill overhaul. Offered scopes (start-session only / both session bookends / global); James picked **global default** for all sessions and skills. Signal: correction + explicit ratification.
Promoted same day: AGENTS.md Conventions bullet + start-session/end-session SKILL.md rewrites (and their `prompts/` twins). Other interactive flows (e.g. /context-update's proposal round) inherit via this instinct rather than per-skill edits.
