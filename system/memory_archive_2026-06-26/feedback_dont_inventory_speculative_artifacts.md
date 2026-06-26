---
name: dont-inventory-speculative-artifacts
description: "When building strategy/roadmap docs, don't inventory speculative future artifacts as if they were planned. List only what exists; name the extension pattern; let consumption drive what ships next."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 94a5fadd-febe-4fcf-905b-60ebb2efe473
---

When drafting strategy or roadmap docs, don't extrapolate one real artifact into a catalog of speculative siblings and present the catalog as a "components to build" list. James will (correctly) call it out as too granular — and won't know what half the items mean because I invented them.

**Why:** 2026-05-16 — wrote `reflex_pinkerton_strategy_051626.md` extrapolating one real sensor (visual user signature, V0 in flight) into an 11-item "user-side sensors" + "content-side sensors" inventory: topic signature, engagement-mode signature, temporal signature, negative-space signature, cross-surface signature, etc. James flagged: "feels too granular at the moment with all of these signatures. I don't even know what that means." He was right — I'd promoted ideas-from-brainstorm-docs to roadmap items without consumption pulling on them. This violates the production-MLOps "start with heuristics, earn the right to complexity" principle that came back from the same session's notebook consult.

**How to apply:**
- Strategy docs should name what exists (real artifacts, in flight or shipped) and the architectural pattern that extends, NOT inventory speculative future items as if planned
- A 35-component "build inventory" with most items marked "future" is the smell — collapse to "what exists today + how the substrate extends"
- Phrase the extensibility honestly: *"next primitive ships when consumption justifies it, not on a pre-planned catalog"*
- When tempted to list 10 future things to demonstrate vision/ambition: ship 1, observe consumption, upgrade what's load-bearing, drop what isn't
- This is distinct from interface design docs (where concrete contract examples ARE appropriate) — strategy docs frame; interface docs spec
- The trigger for promoting an idea from "brainstorm artifact" to "roadmap item" is a specific consumer pulling for it, not architectural symmetry

Related: [[project_pinkerton_reflex_substrate]], [[feedback_engagement_over_structure_in_thinking_partner]]
