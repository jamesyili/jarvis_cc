# HF Next-Charter Design — Options + Recommendation

**Author:** James Li
**For:** Dylan Wang
**Date:** 2026-05
**Status:** Draft v1 — for your pressure-test

> Per our conversation: a few org-shape options and tradeoffs to help pressure-test the business, resourcing, and coordination implications. **These are options, not a pitch** — sharing to reduce coordination tax and make my reasoning visible.

---

## Organizing thesis

**Pinterest needs an explicit, cross-surface AI personalization capability** — one team that owns the loop from candidate generation through Anticipation through generative recommendations through user-facing explainability, with an AI-leveraged engineering substrate underneath. The work my team has been doing (UPP, Anticipation/RR, RecGPT, Reflex/Pinkerton) is naturally converging toward owning that space. The question is the right durable shape.

## Design principles

1. **Optimize for topline (SSv2, WAU/MAU).** Charter altitude should match metric leverage.
2. **Couple ML and AI where they compound.** Reflex/Pinkerton + Anticipation + RecGPT + Recsplanations live together because they reinforce each other.
3. **Keep charters durable; reduce coordination tax.** Clean boundaries beat clever org structures.
4. **Create growth paths under each EM.** Strong-people retention is an org capability, not an HR detail.
5. **Bound scope to actual capacity.** Don't stretch a thin team across too many fronts.

## Capability map (independent of team ownership)

| Capability | Building blocks |
|---|---|
| Production personalization (ML) | CG, Retrieval, Anticipation, LWS, CLR |
| Frontier AI for recs | RecGPT, Recsplanations, agentic generative recs |
| AI-leveraged engineering substrate | Reflex, Pinkerton, Pinvestigator |
| Platform interfaces | UPP cross-surface, UPP foundations, ML foundations |
| Product / E2E partnership | Anticipation surface logic, Recsplanations UX |
| Ranking + blending | HF Ranking, Blending |
| Surface engineering | Frontend, mobile, client |

---

## Three org-shape options

### Option 1 — Two-track within current scope (production + frontier)

Internal restructure only. Production track (CG/Retrieval/LWS) and frontier track (RecGPT/Reflex/Pinkerton/Recsplanations) as sub-teams under me. Minimal external scope change.

- **Pros:** Easy to land; coherent within current scope; no cross-EM negotiation.
- **Cons:** Doesn't operationalize the AI doubling-down. Doesn't enable the Yan/Tim reshape. Smaller Director-altitude story. Underprices the personalization-narrative opportunity.
- **Best for:** A status-quo-plus year if business priorities shift away from AI/personalization investment.

### Option 2 (recommended) — AI personalization as cross-surface capability

I own the AI personalization stack end-to-end: CG, Retrieval, Anticipation, LWS, RecGPT, Recsplanations, UPP cross-surface. AI Tooling (Reflex/Pinkerton) becomes a real funded sub-team. Daniel Lu's ML group consolidates if available. Small surface-engineering wedge for Recsplanations.

- **Pros:** Serves the business AND the AI doubling-down at once. Coherent Pinterest-wide personalization capability. Clean peer story with Dhruvil. Enables Yan to reshape as a coherent presentation-side EM (with Tim consolidating under her). Strong people-growth bench.
- **Cons:** Requires Rajat sign-off on AI net-new headcount. The Recsplanations surface wedge is the political pressure point (small slice from Tim or Yan).
- **Best for:** What I believe is the right durable shape — see below.

### Option 3 — AI acceleration as a horizontal program

Reflex/Pinkerton becomes a Pinterest-wide AI engineering substrate (Core-spanning). I own or co-own with Karina/Kaanon. CG team stays largely as-is or modestly expands.

- **Pros:** Highest leverage on the AI bet; Pinterest-wide engineering culture impact; clearest "AI-leveraged-leader" pattern.
- **Cons:** Requires Jeff/Rajat-level decision; longer timeline (12-24 months); declines the presentation-side door; sponsorship architecture becomes load-bearing immediately.
- **Best for:** A 12-24 month play if cross-org AI substrate is a higher-priority Pinterest bet than HF personalization narrative.

---

## Recommendation: Option 2

Option 2 serves the most signals at once with the least sponsorship cost:

- **Business:** ~2-3% SSv2 deliverable from the personalization stack; WAU/MAU lift via Retentive Recs; cost/velocity gains via AI Tooling.
- **AI doubling-down:** Reflex/Pinkerton as funded sub-team (4-6 engineers) converts the signal into a real bet.
- **Org coherence:** James (AI personalization), Dhruvil (foundations + ranking), Yan (presentation surfaces) — three clean charters, no overlap.
- **People:** growth paths for Daniel Lu (if available), incoming EM, Bella, Yuke, Piyush, J.J. — plus a clean Director-track shape for Dhruvil too.

## Scope trims (what I would stop / delegate / simplify)

| Scope today | Goes to | Rationale |
|---|---|---|
| **UPP foundations** | Dhruvil | Platform infra naturally pairs with ranking/foundations; cleaner Dhruvil charter |
| **ML foundations** (UPP third pillar — training data, etc.) | Dhruvil | His team already has people working there |
| **Responsiveness** (J.J. 50% in-session signals) | Surface side | Closer to surface integration; frees J.J. for AI Tooling promo case |
| **Unity-for-IB** | Yan / IB team | Stays with the surface that consumes it |
| **Dynamic Triggering** | Stop funding | Low-leverage; not worth ongoing investment |
| **Multi-embedding, Content Exploration/MDD, GULP, Growth/LFU** | Other teams | Lower-energy, lower-leverage (already in proposed cuts) |

## Two open variables to weigh together (LWS + Blending)

Two areas where multiple reasonable shapes exist; I'd want your read before locking:

- **LWS** is now a fruit-bearing area thanks to recent GPU serving + architecture unlocks (3 engineers, real upside). It couples tightly with Ranking and Blending downstream. Could stay with me, or could move with the late-stage scoring cluster if that consolidates elsewhere.
- **Blending** (Rahul, L16, ~7 people) is probably understaffed and shouldn't stand alone reporting to you. Natural homes: sub-team under me or sub-team under Dhruvil.

These two interact — if Blending consolidates under Dhruvil, LWS may want to follow (clean late-stage scoring + blending + ranking cluster). If Blending consolidates under me, LWS stays. **Happy to walk through specific tradeoffs.**

## People setup

**Director-track / protected candidates under this shape:**

- **Dhruvil** — doesn't need more scope; needs more people + another EM. Owns Ranking + UPP foundations + ML foundations (+ optionally Blending). Clean peer shape to mine.
- **Tim** — consolidates under Yan as presentation-side TL; coherent growth path on the surface side.
- **Daofeng, Olafur** — strong TLs on the ranking/IC side. Both stay where they are.

**Growth paths under my team:**

- **Daniel Lu** — TL / sub-lead for Anticipation/RR ML cluster if available. (Ideal, not essential — proposal holds without him.)
- **Incoming EM** (hiring pipeline) — owns a sub-charter (AI Tooling or RecGPT/Recsplanations).
- **Bella** — EM-track candidate for the RecGPT + Recsplanations LLM cluster.
- **Yuke** — TL → potential sub-EM for the Retentive Recs cluster.
- **Piyush** — IC16 → staff growth on retrieval; cross-surface UPP impact.
- **J.J.** — IC16 promo Q2; refocused on AI Tooling sub-team.

## Headcount ask

**4-6 dedicated engineers for an AI-Leveraged Engineering sub-team** under my org, with a real charter.

Today AI Tooling (Reflex/Pinkerton/Pinvestigator) runs on ~0.9 FTE from spare cycles. Initial PRs are already producing 0.1-0.2% SSv2, and the velocity multiplier on other rows is the deeper bet. **Doubling down on AI means funding it as a real sub-team, not borrowing cycles.** Net-new headcount sponsored upward (Option A) is cleanest. Reallocation within the org (Option B) is the fallback.

## Success metrics (tied to business outcomes)

- **Topline:** ~2-3% SSv2 from the personalization stack over the next 6 months; +X% WAU/MAU via Retentive Recs.
- **Velocity:** measurable cycle-time reduction across Anticipation, CLR, LWS via Reflex/Pinkerton adoption.
- **Quality:** regression rate on production launches; AI-substrate guardrail effectiveness on cascading-hallucination risks.
- **AI substrate adoption:** % of Core ML teams using Reflex/Pinkerton primitives by EOY.

## Open questions for you

- Is the cross-surface AI personalization framing the right organizing thesis, or is there a different capability frame you'd prefer?
- Can you sponsor the 4-6 AI engineer headcount upward to Rajat, or should we plan against Option B (reallocate within the org)?
- What's the right timeline for the Yan-team reshape and Tim consolidation — early Q3 or later?
- Where am I missing something in the rebalance — particularly Francisco's path and any signals on Dhruvil's preferences?
