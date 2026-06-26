---
name: update-in-place-not-companion-docs
description: "When new substance lands that belongs in an existing artifact, update the original in-place. Don't create parallel companion docs that James has to read alongside."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 09d278d5-9bb1-4891-abd5-d381591324b9
---

When new substance lands that belongs in an existing artifact, **update the original in-place**. Don't create a parallel companion doc and tell James to read both.

**Why:** Surfaced 2026-05-22 during OpenAI May 27 prep. New material (FP/FN framing, Snap Discover war story, anti-patterns from failed Anthropic loop) was generated and saved to a separate `openai_integrity_substance_v1.md` instead of being woven into the existing `openai_call_prep_2026-05-27.md`. James caught it: *"Did you update my talking points / questions for the recruiter based on the previous stuff?"* That's a process miss — James shouldn't have to ask whether updates happened, and shouldn't have to read parallel docs to get current state.

**How to apply:**

- **Default: in-place update.** If new material has a natural home in an existing artifact, integrate it there. Mark the section as updated if version-history matters.
- **Companion doc only when:** (a) James explicitly asks for separation, (b) the new material is a fundamentally different format (e.g., a checklist vs. a narrative), or (c) the existing doc would lose coherence with the additions.
- **When unsure: ask once.** "This belongs in [existing doc] — update in place, or create separate?" Cheaper than creating two parallel docs.
- **End-of-session check:** if a session generated 2+ docs on the same topic, ask before wrapping whether to consolidate.

Pairs with [[write-artifacts-to-files]] (write substantive material proactively) and [[email-md-files-by-default]] (email new artifacts) — but those rules don't override "update in-place when there's an existing home."
