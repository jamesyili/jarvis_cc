# Teen-Aware Pinterest Experience — Faisal Farooq

> **Source of record.** Pasted verbatim by James 2026-08-14. Author: **Faisal Farooq** (VP Eng, T&S/Signals — stakeholders §14). Explicitly *not* a PRD/TDD/alignment doc — a living problem-statement doc. "We will not try to perfect this document, rather, bias will be towards action."

## Purpose

Starting point + living document. Core role: ensure that at any point in time we remain aligned on a crisp shared **definition of the problem statement**. Rapid iteration grounded in **AI-native software development and experimentation**; the doc is "connective tissue" — current understanding, open questions, single source of truth.

## Problem Statement

Create a teen-aware experience on Pinterest, **starting with Homefeed**. Teen users — especially new ones — are vulnerable to a **feed quality spiral**: a small amount of interaction with borderline content compounds over time, progressively polluting the feed into an unsafe state.

**Scope = the borderline-to-violative spiral.** While borderline content like profanity and gross can also lead to a low-quality feed, and solving for all low quality *may be the north star*, the initial focus is **harm-adjacent borderline content** — adult-adjacent = racy, self-harm-adjacent = depressive, etc. I.e. content that is sensitive either **in larger volumes** or **borderline content which if interacted with leads to the feedback loop** resulting in harmful and policy-violating content (Adult Content, Self Harm, Violence, Child Sexualization).

## Why This Matters

- Teens are a vulnerable population; **new teens especially** — limited engagement history to anchor recommendations to safe content.
- "Our discovery systems are optimized for clicks and repins. When borderline content earns engagement, the reward cycle reinforces it, spiraling the feed toward increasingly unsafe territory."
- **T&S signals are imperfect**, especially for needle-in-haystack areas like Self Harm. Precision/recall tradeoffs. "Relying solely on last-mile filtering against imperfect signals is a losing proposition — anything that leaks through gets amplified by the reward loop."
- Distinct from and complementary to the **short-term contextualized treatment changes CQ is already making for teens** (e.g., more aggressive thresholds).

## Metric of Success (TBD)

Traditional safety metrics insufficient:
- **Prevalence** — measures average exposure, not the compounding personalization risk.
- **User reach** — doesn't capture how bad an *individual* teen's feed can get once the spiral starts.

Better candidates:
- **Density:** what fraction of an individual teen's feed is borderline or violative (e.g. >33% of feed becoming borderline/violative).
- **Feed quality:** potentially an **LLM-judge-based** evaluation scoring holistic teen-appropriateness of a feed sample.

## Ideas to Explore

> "Faisal's initial scratchpad ideas. Not mutually exclusive. Add to this list, quickly discuss pros and cons, then rapidly move to prototype."

**1. Safety-Aware Homefeed (Modeling Approach).** Today safety lives *outside* the ranker — candidates scored for engagement, ranked, then filtered by T&S at the end. "The model itself has no incentive to prefer safe content; it just gets told 'no' after the fact on a subset of items." Proposal: safety as a first-class term in the **teen ranking utility**.
- Multi-objective ranking for teens: `U = engagement − λ · safety_risk`, λ tuned for teen surfaces.
- **Negative reward shaping:** penalize the model during training when it ranks borderline content highly for teen users, even if it drives engagement.
- **Counterfactual training data:** construct teen examples where borderline content was engaged with, train the model not to propagate that signal forward.
- **Decoupled engagement signals for teens:** a click/repin from a teen on borderline content shouldn't carry the same training weight as an adult click on benign content.
- *Why:* attacks the spiral at the root — the reward loop — "even imperfect safety signals become useful as a **gradient** (push away from risk) rather than a **gate** (binary keep/drop)."
- Refs: `[WIP] Beyond Blanket Filtering: A Full-Funnel Framework for Content Quality Signals`; Quality Signal Registry; Safety Signal Registry.

**2. Curated Teen-Safe Content Pool (Inversion Approach).** Today's default is *allowlist-by-exception*: all content eligible unless a filter removes it. Fragile because filters are imperfect and the long tail is enormous. Proposal: flip to **denylist-by-exception** — a curated corpus of teen-safe content across categories teens care about (fashion, beauty, gaming, sports, study/aesthetic, food, DIY, fandoms), restricting the teen Homefeed candidate set to this pool.
- Curation at scale: high-precision classifiers + creator-level reputation + board-level quality + human review for ambiguous cases; tiered rather than purely manual.
- **Category coverage guarantees** — pool broad/fresh enough that teen experience isn't narrow or stale (**the main risk**).
- **Graduated trust:** content/creators earn their way in over time.
- Fallback handling when the pool is thin for an interest.
- *Why:* "worst-case feed quality is bounded by the quality of the **pool**, not by the **recall of our filters**." Trade-off = breadth and freshness.

**3. Engagement Signal Hygiene for Teens.** Treat teen engagement as inherently lower-trust input.
- Discount/discard teen engagement on borderline content from collaborative filtering, embedding training, Pin2Pin/related-pins graphs.
- **Quarantine signals from new teen accounts** until a baseline of healthy engagement is established.
- **Asymmetric treatment:** positive engagement on clearly-safe content propagates normally; engagement on borderline content propagates weakly or not at all.
- Prevents one teen's spiral from polluting recommendations for other teens.

**4. Cold-Start Protection for New Teens.** Highest-risk cohort.
- Start new teens in a high-confidence safe state (the curated pool from Idea 2) regardless of long-term strategy.
- Gradually expand the candidate set only after healthy engagement patterns.
- Use **explicit interest declaration** (onboarding picker) more heavily for teens, reducing reliance on early implicit signals.
- Ref: `What We Know About...New Users [Research Summary]`.

**5. Spiral Detection and Intervention.** Detect when an individual teen's feed trends toward unsafe density and intervene.
- Track per-user borderline density over a rolling window.
- On threshold cross: **feed reset** — fall back to safer candidate sources, diversify aggressively, or re-seed from declared interests.
- "A safety net that works regardless of what the ranker is doing."

**5a. FOR SEEKERS: spiral detection + user-facing intervention.** When intent signals a trend toward unsafe content (continuous searches for weight loss, diet, etc.), use a **banner or half-sheet** with support and reflection on the topic, then paths away (slides 14–15 of `Teens VSC UXR Report_December 2025`). "Enables the teen to get a nudge away from the content, is not judgmental, but also helps them critically reflect on the topic and spiral, and gives them agency."

**6. Diversity / Exploration Constraints.** The spiral is partly a **concentration problem** — feed collapses onto a narrow set of risky topics.
- **Topic diversity floors** for teens (no more than X% of feed from any one cluster).
- **Mandatory exploration slots** seeded from safe, broadly-appealing content, independent of personalization.
- Bounds how "deep" the personalization rabbit hole can go.

**7. LLM-in-the-Loop Feed Auditing.**
- **Pre-serve auditing:** LLM judge evaluates a sampled teen feed slate *before serving*, rejects/reshuffles if the holistic gestalt is unsafe even when no individual Pin trips a filter.
- **Offline auditing at scale:** continuously sample teen feeds, score them, use scores both as metric and as **training signal back into the ranker**.
- "LLM judges can catch aggregate feed quality issues that per-item classifiers miss."

## Out of Scope (for now)

- Short-term contextualized threshold changes for teens being driven by Content Quality.
- Solving for overall quality of feed.

## Open Questions / Next Steps

- Add more potential ideas to explore.
- **Align on the success metric** (density vs LLM-judged feed quality vs composite).
- **Prioritize ideas by impact and effort**; identify which are complementary vs mutually exclusive.
- Identify a **small set of bets to prototype**.
- **Will the Teen experience last as long as someone is a teen, or graduate** (e.g. 28d, or at some engagement milestone)?
