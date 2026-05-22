# HF Next-Charter Design — Options + Recommendation

**Author:** James Li
**For:** Dylan Wang
**Date:** 2026-05
**Status:** Draft v1 — for your pressure-test

> Per our conversation. Three org-shape options with tradeoffs, my recommendation, scope trims, and the two open variables I want your read on. I lead with the organizing thesis and capability map so the options are evaluable on the substance, not on preference.

---

## Organizing thesis

**Pinterest needs an explicit, cross-surface AI personalization capability** — one team owning the loop from candidate generation → Anticipation → generative recommendations → user-facing explainability, with an AI-leveraged engineering substrate underneath. My team already operates in this space (UPP, Anticipation/RR, RecGPT, Reflex/Pinkerton). The question is the right durable shape.

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
| AI-leveraged engineering substrate | Reflex, Pinkerton, PINvestigator |
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

I own the AI personalization stack end-to-end: CG, Retrieval, Anticipation, LWS, RecGPT, Recsplanations, UPP cross-surface. AI Tooling (Reflex/Pinkerton) becomes a real funded sub-team. Daniel Lu's ML group consolidates if available (desirable, not a dependency). Small surface-engineering wedge for Recsplanations.

- **Pros:** Serves the business AND the AI doubling-down at once. Coherent Pinterest-wide personalization capability. Clean peer story with Dhruvil. Enables Yan to reshape as a coherent presentation-side EM (with Tim consolidating under her). Strong people-growth bench.
- **Cons:** Requires Rajat sign-off on AI net-new headcount. The Recsplanations surface wedge is the political pressure point (small slice from Tim or Yan).
- **Best for:** The right durable shape — see recommendation below.

### Option 3 — AI acceleration as a horizontal program

Reflex/Pinkerton becomes a Pinterest-wide AI engineering substrate (Core-spanning). I own or co-own with Karina/Kaanon. CG team stays largely as-is or modestly expands.

- **Pros:** Highest leverage on the AI bet; Pinterest-wide engineering culture impact; the cleanest "AI-leveraged-leader" pattern across Core.
- **Cons:** Trades the HF presentation-side wedge for cross-org leverage; requires Jeff/Rajat-level sponsorship to land; longer ramp (12-24 mo); relationship density with Faisal/Jia Jing needs to be live, not aspirational, before this is real.
- **Best for:** A 12-24 month play if cross-org AI substrate is the higher-priority Pinterest bet than HF personalization narrative — and if the upward sponsorship architecture is already underwritten.

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

These two interact — if Blending consolidates under Dhruvil, LWS may want to follow (clean late-stage scoring + blending + ranking cluster). If Blending consolidates under me, LWS stays. Want to walk these tradeoffs together — they're the load-bearing seam.

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

Today AI Tooling (Reflex/Pinkerton/PINvestigator) runs on ~0.9 FTE from spare cycles. Initial PRs are already producing 0.1-0.2% SSv2, and the velocity multiplier on other rows is the deeper bet. **Doubling down on AI means funding it as a real sub-team, not borrowing cycles.** Net-new headcount sponsored upward (Option A) is cleanest. Reallocation within the org (Option B) is the fallback.

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

---

## End-to-end Anticipation today (and the gap)

The pivot toward brand-new experiences (Anticipation, Recsplanations, agentic recs) exposes how today's org boundaries don't match where the work actually lives.

**End-to-end Anticipation = user experience × systems stack.**

| User-facing experience | Systems that power it |
|---|---|
| Bundle recommendations / Recsplanations | Client, NGAPI (thin), Unity, Signals + Model |
| Pin recommendations | Client, NGAPI (thin), Unity, Signals + Model |

The systems are the same. The user-facing surface is what changes.

**The gap today.** As we pivot toward brand-new experiences, we need:

1. **Much closer alignment in incentives and outcomes between Signal/Model eng and Client eng** — today these live in different orgs with different metrics; the brand-new experiences require them to ship as one product.
2. **Better understanding of how to leverage ML eng outputs in the app** — the Unity → Client layer doesn't currently absorb ML primitives well; we ship the model, the surface translates poorly.
3. **More knowledge across the org in Unity → Client (full-stack eng)** — coherent end-to-end ownership requires engineers who can move across this seam, not hand it off.

This is the structural argument for Option 2: one team owning Signals + Model + the Unity/Client wedge for Recsplanations is the shape that closes the gap on the experiences we're trying to ship.

---

## Where the trend is going (AI)

The capability-shape decision should be priced against where AI is taking eng orgs over the next 12-24 months. The predictions below are evidence-weighted, not preference.

**What changes with AI:**

1. **Engineers will be expected to have much more range; "pure" client eng deprecates.** AI collapses the cost of cross-domain context-switching. End-to-end engineers do *much* more; specialists in any one layer compound less. *Evidence:* "AI-orchestrated full-stack" is now the dominant senior-IC pattern in 2025-26 industry analyses (Pragmatic Engineer, DORA 2025); Palantir-style Forward-Deployed Engineer postings up ~800% Jan-Sep 2025 across OpenAI, Anthropic, Google.

2. **Reskillers grow much faster; the gap between adopters and non-adopters widens fast.** AI tools are table-stakes — DORA 2025: ~90% of devs use AI assistance; Pragmatic Engineer Feb 2026: 73% use AI coding tools daily, up from 41% a year prior. But the productivity uplift is bimodal: senior + AI-leveraged compounds, others plateau. *Implication for our org:* "AI-leveraged" should be a real performance criterion, not a hobby.

3. **PM-to-eng ratio is inverting; PM becomes the bottleneck.** As AI absorbs more eng execution, the constraint shifts upstream to product judgment and problem definition. *Evidence:* Andrew Ng (July 2025) — *"product management work isn't getting faster at the same speed; this ratio is shifting."* Anthropic now runs closer to 1 PM : 20 eng vs. the classic 1:5. *Implication:* the brand-new experiences will be PM-supply-constrained before they're eng-supply-constrained.

4. **The cost of code trends toward zero; the cost of judgment doesn't.** AI is increasingly writing the code (Pichai + Nadella publicly cite ~25% of new code at Google/Microsoft; Anthropic/OpenAI internal reports 90-100% for some engineers). The differentiated work moves to: taste, architecture, eval design, ranking/blending decisions, when-to-trust-the-model. *Implication:* recsys-native judgment (offline/online gap reasoning, ranking tradeoffs, eval design) is exactly where the org should concentrate senior bandwidth.

5. **AI without a good substrate degrades quality — substrate matters more, not less.** DORA 2025: AI adoption correlates with **bugs/dev +54%, incidents/PR +242%, PR review time +441%, PRs merged with no review +31%**. AI *amplifies* the underlying engineering system. *Implication:* this is the data backing Reflex/Pinkerton as a real org investment, not a hobby — funding the substrate is what makes the AI bet net-positive instead of net-negative.

**What does NOT change with AI:**

1. **Ownership and incentive problems remain human problems.** AI doesn't fix mis-aligned charters, fuzzy metrics, or unowned scope. If anything, AI's velocity multiplier makes ownership gaps fail faster. The cross-surface alignment problem above isn't an AI problem — it's an org-design problem.

2. **Domain expertise and judgment compound from years of experience.** AI accelerates the execution of judgment but doesn't substitute for it. Ranking/blending intuition, the offline-online gap, what "good" looks like on Pinterest specifically — these come from being inside the work for years.

3. **Citizenship and cross-org connection still depend on humans.** ML ↔ Client trust, working relationships across signals/model/surface, the credibility to land a hard ask — these are people-to-people, and AI doesn't shortcut them.

**Net read:** The pivot toward brand-new experiences requires (a) eng range across the stack, (b) a real AI-leveraged substrate, (c) senior judgment concentrated where the model can't go yet, (d) the same human capabilities Pinterest has always needed — ownership, expertise, citizenship — at higher quality, not lower.

This is the org-design backdrop for Option 2.

---

## What energizes me

In response to your direct question — three things, in priority order:

1. **Growing good talent and leaders.** This is where I produce the most durable value. Bowen → me has been the pattern; Daniel Lu (if he comes), Bella, Yuke, J.J. are the live bets.
2. **Solving user problems.** Anticipation, Retentive Recs, Recsplanations — the work I push hardest on is the work that changes what the user actually experiences.
3. **Efficiency.** Reflex/Pinkerton is the most concentrated expression of this — building the substrate that makes the team 2-3x faster is more compelling to me than personally shipping the next feature.

The proposed shape (Option 2) is the one that gives me the most leverage on all three at once.
