# Pinkerton VLM Visual Signature — Brainstorm

**Date:** 2026-05-11
**Status:** V0 plan, three-week scope (5/12–5/29 pre-China)
**Companion to:** `2026-05-11-vlm-in-reflex-brainstorm.md` (content-side VLM work). This doc is the user-side counterpart.

---

## Thesis

Pinterest's user-side representations encode visual style **implicitly** inside opaque multimodal embeddings. Making that signal **explicit, interpretable, and queryable** — via VLM-derived visual signatures — unlocks three things vectors cannot:

1. **Interpretability** — readable user-state introspection in Pinkerton
2. **Auditability** — quantifiable evaluation of whether anticipation predictions match visual style or only topic
3. **Compositionality** — visual context as evidence in Reflex Detect hypotheses

---

## The Primitive

**Visual user signature** = a VLM-generated interpretable description of a user's visual engagement aesthetic, derived from VLM processing of their recent engaged pins.

Schema (structured + narrative hybrid):

```yaml
visual_signature:
  narrative: "3-sentence human-readable description"
  structured:
    color_palette: ["muted-warm", "low-saturation"]
    composition: ["close-up", "hand-and-object", "centered"]
    mood: ["naturalistic", "calm", "domestic"]
    content_type: ["lifestyle", "diy", "food"]
    style_tags: ["photographic", "not-illustrated", "golden-hour"]
  derived_from:
    pin_count: 50
    engagement_types: ["save", "closeup"]
    time_window: "last_30_days"
    cache_hit_rate: 0.47
  per_pin_captions: [...]   # full audit trail
```

- `structured` fields = feature surface for downstream models
- `narrative` = what humans + Reflex Detect agents consume
- `derived_from` = reproducibility metadata
- `per_pin_captions` = audit trail (trace any signature element back to source pins)

Narrative example:

> *"This user engages with muted warm-toned photographic lifestyle imagery. Compositions are hand-and-object close-ups, not wide shots. Style is naturalistic — not illustrated, not high-contrast product photography. Recurring elements: textured surfaces (linen, wood), low-saturation greens, golden-hour lighting."*

---

## Why a Primitive — Not Just Better Embeddings

Pinterest has rich multimodal pin embeddings. They encode visual style — but inseparably from topic, in an opaque vector. A retrieval model trained on them learns *something* about visual matching, but you can't read it, intervene on it, or reason over it.

VLM unlocks three things the embedding can't:

1. **Interpretability.** A description ("warm-toned photographic lifestyle") is human-readable; a 512-dim vector is not. Matters for debugging, stakeholder communication, selective intervention.
2. **Compositionality.** You can mix-and-match: *"find users whose visual signature is style A but topic distribution is topic B."* Vectors don't separate cleanly.
3. **Auditability.** When anticipation over-predicts on a topic, you can ask: *"did it actually match this user's visual style, or did it just hit the topic?"* That's a quantifiable failure mode VLM exposes.

---

## Design Decisions (locked 2026-05-11)

Four decisions made today that shape Week 1 build:

### A. Engagement signal selection — saves + closeups

Different engagement signals capture different things:

- Clicks → attention (what catches eye)
- Closeups → consumption (what holds attention)
- Saves → aspiration (what user wants in their world)
- Long-dwell impressions → ambient preference
- Hides / negatives → anti-signature

**V0 uses saves + closeups.** Both are intent-strong, both visually-driven (vs scroll-based passive clicks). Combine into one signature; don't split yet.

**Defer to V2:** negative signal (hides, long-dwell-no-click as anti-style). Interesting but doubles eval complexity.

### B. Pin count + temporal window — N=50, last 30 days

- **N = 50 pins per user**, stratified 25 saves + 25 closeups
- **Window = last 30 days** (shorter → noisy; longer → drift)

Both tunable in Week 2 once we see what stabilizes signatures.

### C. Synthesis approach — per-pin → aggregate

Three options considered:

| Option | Pros | Cons |
|---|---|---|
| **A. Per-pin → aggregate** ⭐ | Interpretable provenance. Per-pin captions cacheable + reusable. Avoids context-window limits. | N VLM calls per user. |
| B. Multi-pin batch | 1 call. Cheap. VLM finds patterns directly. | Context limits. Over-generalization bias. Can't trace why. |
| C. Hybrid (cluster-then-synthesize) | Granular + cross-pin patterns. | Two-stage complexity. |

**Locked: A (per-pin → aggregate).** Three reasons:

1. **Interpretability is the whole point.** Per-pin captions = audit trail. When Week 2 eval says "anticipation missed visual style for user X," we trace exactly which pins drove which signature elements.
2. **Cacheability is structurally valuable.** Per-pin captions are reusable Pinkerton artifacts — once VLM-captioned, that caption is good for any user who engaged with that pin. Hot pins captioned once, reused thousands of times.
3. **Cost is overstated.** If VLM ~$0.01/pin, cold per-user = ~$0.50. With 50% cache hit rate after warmup, marginal ~$0.25. V0 on 20 users: <$10 total. At scale, cache economics dominate.

### D. Signature schema — structured + narrative hybrid

See schema in "The Primitive" section above.

**Key design choice:** structured taxonomies (color_palette, composition, mood) need controlled vocabulary or they're useless for aggregation across users. Free-text VLM outputs vary ("muted-warm" vs "warm muted" vs "earth tones, dim").

**Vocabulary approach: bottom-up.** Let VLM generate freely in Week 1; cluster outputs in Week 1.5; emerge taxonomy from data. Add a Week 1.5 step: cluster structured outputs from 20-user sample, normalize taxonomy, re-run with controlled vocabulary. Adds 1-2 days but gives a defensible taxonomy fit to Pinterest's actual visual diversity.

---

## Three-Week V0 (5/12–5/29)

### Week 1 (5/12–5/16) — Build Pinkerton VLM-Introspection

| Day | Work |
|---|---|
| **5/12 (Mon)** | VLM access path confirmation (Piyush thread). Resolve open Q1. |
| **5/13–14 (Tue–Wed)** | Build per-pin VLM captioning. Schema design (structured + narrative). Pin selection: saves + closeups, last 30d, N=50. Cache layer for cross-user reuse. |
| **5/15 (Thu)** | Run on 20 sampled users across engagement tiers. Inspect outputs. Identify taxonomy emergence patterns. |
| **5/16 (Fri)** | Week 1.5: cluster outputs, normalize taxonomy, lock controlled vocabulary. Re-run pipeline with normalized schema. |

**Output by end of Week 1:** 20 stable signatures + per-pin caption cache + locked taxonomy spec. `pinkerton visualize <user_id>` operational.

### Week 2 (5/19–5/23) — Eval Against Anticipation Predictions

- For sampled users, pull anticipation's top-K predictions
- Score each predicted pin against the user's signature across structured axes
- Compute visual-coherence metric per user
- Compare across segments (engagement tier, market, interest cluster)

**Visual-coherence metric (refined 5/11):** For each user, for each predicted top-K pin from anticipation, compute taxonomy-axis match against signature. If user signature has `composition=[close-up, hand-and-object]` and top-10 anticipation predictions have 3 close-ups + 0 hand-and-object → axis score = 3/10. Aggregate across structured axes (color, composition, mood, content_type, style_tags) → single per-user coherence score. Quantifiable, comparable across users, falsifiable.

**Hypothesis under test:** anticipation overfits topic, underfits visual style.

- If true: visual signature has measurable lift as a retrieval/ranking signal
- If false: this is a learning exercise that surfaces what embeddings already capture (still valuable, but stops the production-bound thread)

### Week 3 (5/26–5/29) — Wire Pinkerton as a Reflex Tool

- Expose visual-signature as a callable tool for Reflex Detect agents
- Detect agent investigating a relevance/quality gap can dispatch: *"Pinkerton, what's the visual signature of segment X users?"*
- Receive interpretable visual context to feed into hypothesis cards
- Demo: one opportunity card that uses visual signature as evidence ("segment X users engage with style A; recently-served pins are style B; visual mismatch hypothesis")

**Output by 5/29:** Reflex Detect agents have a visual-context tool, with one concrete hypothesis card demonstrating it.

---

## What This Is NOT (Scope Discipline)

- **Not UPP integration.** UPP is foundation pretraining for user representations — separate axis. Visual signature as a downstream feature does not belong inside UPP's training task. Different conversation, different timeline.
- **Not embedding replacement.** Embeddings stay where they are. VLM signature is a complementary interpretable layer.
- **Not VLM-as-feed-judge.** That's the content-side work in the companion brainstorm. This is user-side.
- **Not a temporal-dynamics solution.** Signature drift over time is real but out-of-scope for V0.
- **Not a cold-start solution.** No engagement history = no signature. Standard problem; defer.
- **Not UIC integration.** Pinkerton↔Reflex coupling here uses visual signature only. UIC tie-in is later scope.

---

## Open Technical Questions

| # | Question | Status |
|---|---|---|
| 1 | VLM access path: can Pinkerton pass pin images (via signature → URL) to a VLM and get text back? | **RESOLVED 5/12:** VLM access confirmed. Implementation details pending from Piyush. |
| 2 | Does multimodal embedding already encode this signal sufficiently? | OPEN. Eval in Week 2 tests directly. |
| 3 | Synthesis prompt shape: per-pin → aggregate, multi-pin batch, or hybrid? | **RESOLVED 5/11:** per-pin → aggregate. See Design Decision C. |
| 4 | Visual-coherence metric in Week 2? | **RESOLVED 5/11:** taxonomy-axis match aggregation. See Week 2 section. |
| 5 | Reflex tool API surface for Week 3? Inline call, MCP tool, async dispatch? | **REFRAMED 5/12.** Deeper fork: Pattern A (data API — `visualize(user_id) → signature`, Reflex Detect does the reasoning) vs Pattern B (question-answering agent — `investigate(hypothesis, segment) → finding`, Pinkerton does the reasoning). Leo recommended A for V0 (B requires Pinkerton agent reasoning loop = out of scope; A keeps clean separation; MCP tool description becomes the agent-comms contract). Plus sub-question Q5a — granularity: single-user vs segment-aware. Leo recommended both, ship single-user first. **All open — pick up next session.** |
| 6 | What is `pinkerton visualize` under the hood — CLI command, function in existing Pinkerton tooling, or agent that orchestrates VLM calls? | **RESOLVED 5/12:** Function + thin CLI for V0. Agent wrapper deferred. Reframed three "options" as layers (core engine / CLI wrapper / agent wrapper) — the agentic part of V0 is the synthesis-step LLM call *inside* the function, not a multi-step orchestrator. Agent-to-agent comms acknowledged as the deeper layering question; a stable function/module is the better thing to wrap an agent around later than building the agent first. |
| 7 | Fallback plan if VLM-access-path doesn't work this week — what's the alternative path that keeps Week 1 from blowing up? | **CLOSED 5/12:** Moot — VLM access confirmed. No tripwire needed. |

---

## Altitude Notes

- **Week 1 is hands-on build** — primary IC contribution; in James's deep zone (Pinkerton + VLM + recsys)
- **Weeks 2–3 are evaluation + integration** — handoff-shaped for follow-on work post-China
- **Three weeks total**, all in James's existing scope (Pinkerton + Reflex), no external team blocker
- **Compounds beyond V0:** if the eval (Week 2) confirms the hypothesis, this primitive is the foundation for downstream work that Anna K (Retentive Recs PM) and the Anticipation team can pick up — visual signature as a feature for retrieval/ranking models is a much larger conversation enabled by this V0

---

## Pick up next session (post-5/12)

Q5 is the live thread. Two sub-questions to resolve:

1. **Q5 Pattern A vs B (data API vs question-answering agent).** Leo recommended A for V0. Confirm or push back. If A: scope the MCP tool description as the agent-comms contract (description = how Reflex Detect agents will reason about *when* to call this).
2. **Q5a — granularity.** Single-user (`pinkerton.visualize(user_id)`) or segment-aware (`pinkerton.visualize_segment(spec)`)? Leo recommended both, ship single-user first.

Then the Week 1.5 prereqs:

- **Taxonomy axis sketch.** Color, composition, mood, content_type, style_tags — what's reasonable dimensionality per axis (3–8 buckets each? More?). Sets the target for Week 1.5 bottom-up clustering to converge toward.
- **Filing decision: 8 harness engineering observations** (captured in 5/11 conversation but not filed) — sibling brainstorm or absorbed into `reflex-codebase-guide.md` as a "design gaps" appendix.

## Resolved 5/12

- **Q1 — VLM access confirmed.** Details pending from Piyush.
- **Q6 — `pinkerton visualize` = function + thin CLI for V0.** Agent wrapper deferred. See Q6 status above for layering rationale.
- **Q7 — fallback plan moot.** VLM access confirmed.

---

## Cross-references

- `2026-05-11-vlm-in-reflex-brainstorm.md` — content-side VLM work (feed quality, relevance gap detection, etc.)
- `reflex-codebase-guide.md` — Detect stage architecture (where Reflex tool integration lands)
- `work+self/projects/pinkerton/` — Pinkerton current state (M0 shipped, M1 in flight)
