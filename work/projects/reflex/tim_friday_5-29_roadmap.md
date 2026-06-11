# Reflex Roadmap — Talking Points for Tim (Fri 5/29)

**Use:** scoping doc for James / talking-points scaffold for Friday. Not a handoff doc.
**Frame for Tim:** "Detect is mature and compounding. The next 1-2 quarters expand Build, stand up Simulate, layer in agent-to-agent and model integration — all on limited engineering resources, with shared ownership across teams. There's also a foundation layer underneath all four that's currently un-staffed; I want to walk you through it so you can help land funding."

---

## Resource picture (open with this)

| Workstream | Anchor owner | Status |
|---|---|---|
| Build agent expansion | JJ | Has an engineer |
| Simulate | ATG primary + Bella support | Partnership ask, not committed yet |
| Agent-to-agent integration | TBD | Open |
| Model integration | Ranking team partners + James | Synergy play, not staffed |
| **Foundation (RLHF + Prove-loop + Velocity)** | **None** | **Load-bearing and un-funded** |

This is the picture Andrew said he wanted Tim to help with — funded-for-my-team is the ask underneath.

---

## Workstream 1 — Build agent expansion (JJ)

**What:** Today's implementation agents are narrow (config write-back, experiment setup). Goal: capable enough to take materially more of the post-approval workload off engineers.

- **1 month:** allowlist expanded to 1-2 more engineering teams (engineer-adoption-driven, not top-down); one new capability shipped (variant generation or bounded refactor).
- **2 months:** end-to-end implementation for one well-defined opportunity-card class; cost-per-card metric live.
- **For Tim:** which engineering teams should we court for opt-in, and what's the political shape of that ask?

## Workstream 2 — Simulate (ATG + Bella)

**What:** offline canary that pre-screens opportunity cards before they consume online A/B budget. Anchors on user-level visual + interest primitives we've already built (user.md + VLM work). Andrew loves this direction and wants ATG collaboration.

- **1 month:** VLM-as-feed-judge prototype against N approved opportunities; partnership memo with ATG signed off by Andrew; Bella scoped in.
- **2 months:** cohort-mode simulation operating; track which cards simulation rejected vs. how they performed online (validation eval).
- **For Tim:** ATG partnership shape — joint headcount, joint roadmap, or vendor-style. Andrew has already opened the door.

## Workstream 3 — Agent-to-agent integration (TBD)

**What:** Reflex agents consume from / publish to other Pinterest agent systems. Analytics agent is the natural starter; other A2A protocol work likely.

- **1 month:** scope decided (analytics agent vs alternative); one integration spiked.
- **2 months:** one integration in production with one measurable benefit (cycle-time reduction or quality lift).
- **For Tim:** this is the most open of the four — strong PM moment to define charter.

## Workstream 4 — Model integration (ranking team + James)

**What:** hooks so ranking-team model improvements flow into / out of Reflex. Some ranking folks are already exploring adjacent direction — partnership rather than new build.

- **1 month:** working group formed with ranking-team contacts; one integration scoped.
- **2 months:** one model improvement in flight via Reflex.
- **For Tim:** map of which ranking folks are working on what; help arbitrate scope so we don't duplicate.

---

## Foundation layer — load-bearing, currently un-staffed

Three pieces sit underneath all four workstreams. Each is what makes "Reflex compounds" true rather than aspirational. Pulling these forward is the cleanest funding ask.

- **Expert labeling + RLHF infrastructure.** The system that turns Andrew / Dylan / Anna / Matt / your-team-judgments into structured, attributable patterns that improve subsequent cards. Without it, every expert minute evaporates into Asana prose. Curator + Skeptic gates already exist in design; the surrounding structured-log and pattern-provenance layer doesn't.
- **Prove → Detect loop (Outcome Learner).** Closes the loop from shipped A/B outcomes back to which patterns survived contact with reality. Without it, "Reflex is getting better" is an unverifiable claim.
- **Velocity / observability.** End-to-end idea-to-launch cycle time, decomposed by stage. The headline metric — single number that proves the dark factory is throughput-positive. Without it, no defensible answer to "is Reflex working?"

**Ask:** at least one engineer (or split FTE) on the foundation layer for the next quarter. This is what "make sure Reflex is funded for my team" cashes out to operationally.

---

## What I'd want Tim to walk away with on Friday

1. There are five things, not four. The fifth is the one I most need his help to land.
2. Each workstream has a named anchor owner — except foundation, deliberately.
3. The ask to Andrew is concrete and is about platform durability, not surface land-grab.
4. Tim is the PM the platform needed; the role is real and scoped.

---

## Open variables (hold these for Friday, don't pre-decide)

- Tim's level / start date / preferred working style — unknown going in.
- Whether to surface Pinkerton-by-name (default: capability-led, same move that worked with Andrew).
- The Dylan funding-ask circle-back still needs to land separately — Tim convo doesn't replace it.
- Whether James's OOO timing (~6/4) constrains what Tim can credibly start before then.
- Cost-tracking and detect/CLAUDE.md cleanup — Detect-internal items that Tim doesn't need on day 1, but should be aware are in flight.

---

## Things I'd want flagged that aren't in the four workstreams you sketched

- **Detect maintenance burden.** Who keeps the Cycle-N+1 loop running while we expand outward? JJ's bandwidth presumably splits; surface that as a known risk.
- **Engineer-adoption motion for Build.** The allowlist expansion is a relationship game across HF CG, Notifs, Search, etc. Tim could own that as PM cross-org work.
- **Recsplanations dimension.** If magical-dimensions / Recsplanations lands in the team-design proposal with Dylan, it intersects Reflex on the substrate side (user.md / interest clusters). Worth noting; not for the Tim opening convo.
- **Implementation-agent blast radius / trust ladder.** Already in the redesign doc; political shape is non-trivial; Tim should be aware before any expansion conversation.
