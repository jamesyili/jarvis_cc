# Reflex ↔ Pinkerton — Interface Design

**Date:** 2026-05-16
**Status:** Design proposal grounded in published agent-system patterns + production MLOps practice
**Companion to:** `reflex_pinkerton_strategy_051626.md` (strategic framing) and `2026-05-11-pinkerton-vlm-visual-signature-brainstorm.md` (V0 sensor primitive)
**Resolves:** Q5 from V0 brainstorm (Pattern A data-API vs Pattern B Q&A agent)

---

## Decision Summary

**MCP-primary, A2A-secondary, Event-stream-tertiary.** Three protocols, three consumer classes, one substrate.

| Consumer | Interface | Pattern | Why |
|---|---|---|---|
| **Reflex agents** (Detect/Build/Simulate/Prove) | MCP server: `pinkerton.sensors.*` | A: Data API | Reasoning lives in the consumer; orchestrator-workers needs sensor primitives, not pre-cooked findings |
| **Human investigators** (EMs, eng, exec demos) | A2A skill: `pinkerton.investigate` (façade over MCP) | B: Q&A Agent | Chat-shaped consumers want findings, not sensor dumps; façade pattern keeps one source of truth |
| **ML systems** (Anticipation eval, dashboards, attribution) | Kafka topics: `pinkerton.sensor_events.*` (defer until needed) | C: Event-driven | Reactive subscription beats polling for high-volume streams; not load-bearing day 1 |

**Pinkerton stays dumb-but-rich. Reasoning lives in the consumer.**

This is the load-bearing decision. Both research streams (Anthropic's published multi-agent results + production MLOps practice) converged on it from different angles. The architectural mistake to avoid: making Pinkerton reason for Reflex.

---

## Two Modes: Single-User + Cohort

Pinkerton exposes every sensor in **two first-class modes**, not one. Both ship as distinct MCP tools that share underlying implementation. Most Reflex Detect queries are cohort-level; most human-investigator queries are single-user. The contract must support both natively or the substrate fails its consumers.

| Mode | Tool family | Use cases | Primary consumer |
|---|---|---|---|
| **Single-user** | `pinkerton.visualize.user_*.v1` | DSAT trace investigation; individual debugging; exec demo on a specific user (e.g., Jeff's profile); RLHF expert labeling | Human investigators, Reflex Build agents validating individual outcomes |
| **Cohort/segment** | `pinkerton.visualize.cohort_*.v1` | Hypothesis formation ("segment X engages with signature Y; Anticipation served signature Z"); cross-market/state comparisons; Anticipation eval at scale; signature-partitioned attribution | Reflex Detect agents (most use cases), Anna K Anticipation eval, surface-team analytics |

**Why two distinct tools, not one tool with a mode flag:**

- **Different input schemas**: `user_id` vs segment specification (filter conditions or explicit user list)
- **Different output schemas**: single signature object vs aggregate signature + cohort metadata (size, sampling rate, sub-distribution markers)
- **Different cache characteristics**: single-user cached by user_id (long TTL, high reuse); cohort cached by segment-spec hash (shorter TTL, depends on cohort volatility)
- **Different cost profiles**: single-user is fast and cheap; cohort can amortize via batching and stratified sampling
- **Different tool descriptions**: agents reason about when to call each based on the task — distinct descriptions are clearer than a parameterized mode

**Under the hood, implementation is shared.** Cohort mode calls single-user mode N times (over a sampled set) then aggregates. Per-user signatures landed in the cache during cohort runs serve future single-user queries at zero marginal cost. The two modes feed each other operationally.

**Aggregation strategies for cohort mode** (configurable per call):
- **Centroid**: average structured fields (when distribution is unimodal)
- **Mode**: most common values per axis (when categorical)
- **Distribution**: full histogram per axis (when the consumer needs to detect multimodality)
- **Exemplars**: top-N representative users + narrative (when the consumer needs to inspect)

Reflex Detect typically wants distribution (to detect bimodal cohorts — "segment X has two distinct visual sub-populations"). Anticipation eval typically wants centroid (for comparison against served distribution). Human investigators typically want exemplars (to see actual users).

---

## Why Pattern A primary for Reflex Detect

Three concrete reasons, all empirically grounded:

### 1. Orchestrator-workers outperforms single-reasoner by 90.2%

Anthropic's published multi-agent research data (June 2025): orchestrator-workers pattern outperforms single-agent on complex research tasks by 90.2%, specifically because **the lead agent and workers own the reasoning** — each subagent gets its own context window to compress sensor data into a finding, in parallel. If you push reasoning into Pinkerton (Pattern B), you collapse this pattern into a flat call chain, lose the parallel context-compression benefit, and double the LLM bill.

### 2. Token economics

Anthropic published: multi-agent systems run ~15× the tokens of single-agent chat. If every Reflex Detect call invokes a Pinkerton reasoning loop, that 15× tax hits on every hypothesis, with reasoning duplicated across both systems. Pattern A keeps Pinkerton at low-marginal-cost sensor compute (cache-friendly, batchable); reasoning cost lives in Reflex where it's actually load-bearing.

### 3. Composability

Reflex Detect's strength is creative recombination: "show me visual signature drift overlaid with cross-surface DSAT for users in segment Y who saw content from cluster Z." Pattern B flattens this to "investigate engagement on segment Y." You lose the combinatorial surface that makes Reflex powerful. The production MLOps analogue (feature stores at YouTube, Pinterest CG, Facebook PYMK) is unambiguous on this: centralized composition in the substrate, primitive lookup at the consumer.

---

## Pinkerton as Feature Store: Tiered Architecture

The production-grade analogue for Pinkerton is **feature store + serving layer**. Three tiers, each addressing a different latency/freshness/cost regime:

```
┌────────────────────────────────────────────────────────────┐
│  TIER 1: Batch Pre-Compute                                  │
│  • Heavy sensors (e.g., VLM-based primitives)               │
│  • Nightly or hourly cadence                                │
│  • Outputs landed in online feature store (Redis/etc.)      │
│  • Reflex queries at microsecond latency                    │
└────────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────────┐
│  TIER 2: Inference Cache                                    │
│  • VLM outputs keyed by (entity_id, version, params)        │
│  • Cache hits = free                                        │
│  • Cache misses = live VLM call with SLA budget             │
│  • Per-pin captions cacheable cross-user (high hit rate)    │
└────────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────────┐
│  TIER 3: Demand-Driven Freshness                            │
│  • Track which primitives Reflex actually queries            │
│  • Over time: pre-compute exactly those, drop the rest      │
│  • "Start with heuristics, earn the right to complexity"    │
└────────────────────────────────────────────────────────────┘
```

V0's per-pin caption caching (50% hit rate target) is Tier 2 in this architecture. Tier 1 batch pre-compute is the natural Phase 1 extension. Tier 3 is a Phase 3 optimization — observe which sensors Reflex actually uses before scaling compute for all of them.

---

## The MCP Server: Concrete Tool Contract

**Transport:** Streamable HTTP (not stdio). Pinkerton is a service, not a local subprocess.

**Authentication:** OAuth2 client credentials flow (service-to-service). Reflex authenticates as Reflex; per-sensor RBAC via scopes.

**Tool naming:** `pinkerton.{category}.{mode}_{action}.v{n}`

Mode is `user` (single-user) or `cohort` (segment-aggregate). Both modes ship per sensor.

Examples from what exists today:
- `pinkerton.visualize.user_signature.v1` / `pinkerton.visualize.cohort_signature.v1` (visual signature; V0 single-user, Phase 1 cohort)
- `pinkerton.trace.user_cross_surface_dsat.v1` (cross-surface DSAT trace; live as Pinkerton Jeff-demo tool — single-user only since cross-surface trace is inherently individual)

Additional sensor primitives follow the same `{category}.{mode}_{action}.v{n}` convention when shipped. The naming convention is the contract; the specific sensors that get built are driven by consumption, not pre-planning.

Version in the name, not in headers. Agents call specific versions explicitly — no implicit upgrades.

### Tool contract example: visual signature

```json
{
  "name": "pinkerton.visualize.user_signature.v1",
  "title": "User Visual Signature",
  "description": "Returns the user's visual signature: dominant visual clusters they engaged with over the lookback window, with confidence scores and narrative description of the aesthetic pattern. Use when forming hypotheses about visual-quality mismatches or aesthetic drift. Returns cached results when available (TTL: 6h). Computed from saves + closeups via VLM per-pin captioning.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "user_id": {"type": "string", "description": "Pinterest user ID"},
      "lookback_days": {"type": "integer", "minimum": 1, "maximum": 90, "default": 30},
      "include_narrative": {"type": "boolean", "default": true},
      "max_staleness_seconds": {"type": "integer", "description": "Override default cache TTL; if cache older than this, force recompute"}
    },
    "required": ["user_id"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "signature_id": {"type": "string", "description": "Stable hash; use for partitioning attribution downstream"},
      "schema_version": {"type": "string", "description": "Sensor output schema version; downstream consumers pin this"},
      "vlm_version": {"type": "string", "description": "Underlying VLM model version"},
      "clusters": {"type": "array", "items": {"type": "object"}},
      "narrative": {"type": "string", "description": "Human-readable aesthetic description"},
      "computed_at": {"type": "string", "format": "date-time"},
      "cache_status": {"enum": ["hit", "miss", "stale_served"]},
      "audit_trail_uri": {"type": "string", "format": "uri", "description": "MCP resource URI for full computation lineage; pull on demand, not in main response"},
      "guardrail_flags": {"type": "array", "items": {"type": "string"}, "description": "Any deterministic anomaly flags from tier-1 guardrails (see Failure Modes)"}
    },
    "required": ["signature_id", "schema_version", "vlm_version", "clusters", "computed_at"]
  }
}
```

Three load-bearing details:

1. **`signature_id`** is the partition key for Reflex Prove attribution. Reflex stamps experiments with the signature_id at exposure time so post-hoc attribution can slice by signature segment. This is the "signature-partitioned attribution" mechanism named in the strategy doc — wired in at the contract level.

2. **`audit_trail_uri`** returns an MCP resource (not a tool result) so the full lineage doesn't pollute the agent's context window. Resources are pulled on demand. This is Anthropic's "lightweight references" anti-pattern fix for context bloat.

3. **`guardrail_flags`** surface deterministic anomaly detection at the response level (see Failure Modes §). If non-empty, Reflex Detect should treat the sensor output as suspect.

### Tool contract example: cohort visual signature

```json
{
  "name": "pinkerton.visualize.cohort_signature.v1",
  "title": "Cohort Visual Signature",
  "description": "Returns the aggregate visual signature for a user cohort defined by segment filters or explicit user list. Sampled and aggregated from per-user signatures. Use when forming hypotheses about segment-level visual mismatches, cross-cohort comparisons, or signature-partitioned eval. Returns aggregate + cohort metadata; per-user signatures landed in cache during the run are reusable by subsequent single-user queries.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "segment_spec": {
        "type": "object",
        "description": "Either filter conditions (market, interest, user_state, etc.) OR explicit user_id list",
        "oneOf": [
          {"properties": {"filters": {"type": "object"}}, "required": ["filters"]},
          {"properties": {"user_ids": {"type": "array", "items": {"type": "string"}}}, "required": ["user_ids"]}
        ]
      },
      "lookback_days": {"type": "integer", "minimum": 1, "maximum": 90, "default": 30},
      "sample_size": {"type": "integer", "default": 500, "description": "Max users to sample within the cohort"},
      "stratify_by": {"type": "array", "items": {"type": "string"}, "description": "Stratification dimensions for sampling (e.g., engagement_tier, market) to avoid selection bias"},
      "aggregation_strategy": {
        "enum": ["centroid", "mode", "distribution", "exemplars"],
        "default": "distribution",
        "description": "centroid: averaged structured fields; mode: most common per axis; distribution: full histogram per axis (recommended for Reflex Detect — detects multimodal cohorts); exemplars: top-N representative users + narrative"
      },
      "max_staleness_seconds": {"type": "integer"}
    },
    "required": ["segment_spec"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "cohort_signature_id": {"type": "string", "description": "Stable hash of (segment_spec + lookback + sample) for attribution partitioning"},
      "cohort_size_total": {"type": "integer", "description": "Total cohort population matching the spec"},
      "cohort_size_sampled": {"type": "integer", "description": "Actual users sampled (may be < sample_size if cohort smaller)"},
      "sampling_rate": {"type": "number"},
      "stratification_realized": {"type": "object", "description": "Achieved stratification distribution (vs requested)"},
      "schema_version": {"type": "string"},
      "vlm_version": {"type": "string"},
      "aggregate": {
        "type": "object",
        "description": "Shape depends on aggregation_strategy",
        "properties": {
          "clusters_distribution": {"type": "array", "description": "Present when strategy=distribution"},
          "clusters_centroid": {"type": "object", "description": "Present when strategy=centroid"},
          "exemplar_users": {"type": "array", "description": "Present when strategy=exemplars"},
          "narrative": {"type": "string", "description": "Human-readable description of the cohort's aggregate aesthetic"}
        }
      },
      "multimodality_detected": {"type": "boolean", "description": "Flagged when distribution suggests cohort has 2+ distinct sub-populations — Reflex Detect should consider re-segmenting"},
      "computed_at": {"type": "string", "format": "date-time"},
      "cache_status": {"enum": ["hit", "miss", "stale_served", "partial_hit"]},
      "audit_trail_uri": {"type": "string", "format": "uri"},
      "per_user_signature_ids": {"type": "array", "items": {"type": "string"}, "description": "References to individual user signatures landed in cache — pullable via user_signature tool with cache_status: hit"},
      "guardrail_flags": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["cohort_signature_id", "cohort_size_sampled", "schema_version", "vlm_version", "aggregate", "computed_at"]
  }
}
```

Four load-bearing details specific to cohort mode:

1. **`stratify_by` + `stratification_realized`** — stratified sampling is the antidote to cohort-mode's #1 failure mode (selection bias; see Failure Modes §). Reflex Detect specifies stratification dimensions; Pinkerton returns what was actually achieved. If `stratification_realized` materially diverges from `stratify_by`, the agent should treat the result as suspect.

2. **`multimodality_detected`** — surfaces when a cohort's signature distribution is bimodal/multimodal. Reflex Detect's correct response is usually to re-segment (the cohort spec is over-aggregating distinct populations). Wired into the contract so the agent can route this automatically rather than rely on humans noticing.

3. **`per_user_signature_ids`** — the cross-mode operational link. Per-user signatures computed during cohort runs are reusable by single-user queries at zero marginal cost. The two modes feed each other; this field makes the linkage explicit.

4. **`cache_status: "partial_hit"`** — added vs single-user enum. Cohort runs frequently hit cache for some users + miss for others; agents need to know the mix to reason about freshness/cost trade-offs.

### Tool description as contract

Per Anthropic's published findings: tool descriptions reduced task completion time by ~40% when rewritten for clarity. Tool description is not documentation — it's part of the API contract. Ship a tool-testing harness that runs description-rewrite quarterly and tracks per-tool error rates from callers.

### Caching surface

`cache_status: "hit" | "miss" | "stale_served"` exposes cache state to the agent. Agent can decide whether to accept stale or pass `max_staleness_seconds` to force recompute. Pinkerton may serve stale on compute failure (graceful degradation) with `stale_served` marker — agent decides whether to trust.

---

## The A2A Skill: `pinkerton.investigate`

For human investigators and high-altitude consumers who want a finding, not a sensor dump.

**Agent Card** at `https://pinkerton.pinterest.internal/.well-known/agent-card.json`:

```json
{
  "name": "pinkerton-investigator",
  "version": "1.0.0",
  "provider": {"organization": "Pinterest"},
  "capabilities": {"streaming": true, "pushNotifications": false},
  "skills": [{
    "id": "investigate",
    "name": "Substrate Investigation",
    "description": "Investigates a hypothesis or open question about user behavior or content quality by composing Pinkerton sensors. Returns a structured finding with evidence trail.",
    "examples": [
      "Why did engagement on the home decor segment drop 8% last week?",
      "Investigate visual-signature drift in users who reported quality issues."
    ]
  }]
}
```

**Critical implementation rule:** `investigate` is a façade. Internally it's an orchestrator-worker pattern that calls the same MCP sensor primitives Reflex uses. One source of truth for sensor compute.

**Task lifecycle:** investigations are long-running (10s–5min). Use streaming transport. Status updates: `WORKING` → emit progressive findings as artifacts → `COMPLETED`.

**Reflex Detect should NOT call `investigate`.** Reflex Detect calls MCP sensors directly and owns its own reasoning. The A2A layer is for chat-shaped consumers (humans, future cross-Pinterest agent ecosystem).

---

## Event Stream: When (Not If)

Kafka topics for ML-system consumers:
- `pinkerton.sensor_events.dsat_anomaly.v1`
- `pinkerton.sensor_events.signature_drift.v1`
- `pinkerton.sensor_events.quality_collapse.v1`

**Defer until concrete subscriber emerges.** MCP supports `resources/subscribe` for change notifications — start with that. Add Kafka when (a) you have an ML-system consumer that needs sub-second latency, or (b) volume forces durable buffering. Don't add Kafka day 1; the operational weight isn't justified.

**Critical constraint:** if/when added, events carry **coarse triggers only** (threshold-crossing alerts) with `signature_id` + `audit_trail_uri` for full lineage. Don't stream narrative traces or rich diagnostics — batch those. Cascading-hallucination risk (see Failure Modes) is amplified by event-driven architectures because there's no human gate.

---

## Versioning + Drift Handling

This is where production MLOps practice diverges most sharply from generic agent-protocol guidance. Three non-negotiable mechanisms:

### 1. Schema registration

Every sensor output has a registered schema. `schema_version` in every response. Downstream consumers (Reflex) pin specific versions. Breaking changes ship as new `v{n}` tool name; old version stays live ≥2 quarters with deprecation annotations.

### 2. Shadow mode for VLM upgrades

Before Reflex consumes an upgraded VLM's outputs:
- New VLM runs in shadow — processes live traffic, logs outputs to data lake, does NOT feed Reflex
- Compare distribution of old vs new VLM outputs offline
- If aligned, promote
- If drifted, investigate before promoting

This is non-negotiable. VLM upgrades change the embedding space — what was "cluster A" under VLM v1 may not correspond to "cluster A" under VLM v2. Every Reflex hypothesis built against v1 is potentially invalidated.

### 3. PSI continuous drift monitoring

After promotion, Population Stability Index continuously compares the distribution of new sensor outputs against the reference baseline. Automated rollback if PSI exceeds threshold. Standard MLOps drift instrument; load-bearing for any substrate-to-agent pipeline.

### 4. Cached hypothesis revalidation

The cross-cut: when VLM upgrades, Reflex's cached hypotheses against signature outputs may become stale even though no Reflex code changed. Upgrade runbook must include explicit cache invalidation + hypothesis revalidation step. This is invisible to API contracts; it lives in the operational protocol.

---

## Failure Modes (Load-Bearing)

The MLOps notebook surfaced three production-real failure modes specific to this architecture, in order of likelihood:

### 1. Silent Failures / Stale-Table Anti-Pattern

**What goes wrong:** Pinkerton's batch pipeline breaks. Quality scores stop updating. Reflex continues its loop against 3-week-old data, detects no gaps (because the data shows the world as it was 3 weeks ago), and the improvement loop silently stalls. **The system appears healthy.**

**Why this is the most common failure mode:** stale data doesn't throw errors. Reflex doesn't know the data is stale unless explicitly told.

**Fix:**
- Data freshness SLAs with automated alerting (every sensor primitive has a named owner + freshness threshold)
- Reflex rejects Pinkerton data older than N hours rather than consuming silently
- `computed_at` field in every response; Reflex Detect checks freshness as a precondition
- Dashboard: per-sensor data-freshness gauge with paging thresholds

### 2. Training-Serving Skew / Alignment Paradox

**What goes wrong:** Reflex's Simulate phase (VLM-as-judge) uses a different prompt structure / temperature / context window than the VLM Pinkerton used in Detect. The two systems disagree on what counts as a gap. Reflex builds fixes for gaps Pinkerton never flagged, and vice versa.

**Why this is structural in your architecture:** Detect and Simulate are independently optimized; nothing forces them to share inference code.

**Fix:**
- Shared inference code and prompt templates across Detect and Simulate
- Treat prompt versioning as seriously as model versioning
- Same VLM version across the pipeline (if Pinkerton is on v2, Simulate is on v2)
- Contract test: random sample of Detect outputs re-evaluated by Simulate VLM; alert on disagreement rate above baseline

### 3. Cascading Hallucinations — Most Dangerous

**What goes wrong:** Pinkerton hallucinates a narrative trace ("user cluster X is seeing DSAT from content quality issue Y"). Reflex treats it as ground truth, writes a PR to fix Y. If Reflex's Simulate VLM is **from the same model family** as Pinkerton's VLM, it's likely to approve the PR — it agrees with the hallucination because they share the same failure mode. The bad PR ships.

**Why this is the most dangerous failure mode specific to this architecture:** the autonomous loop has no human gate. Same-model-family VLMs at Detect and Simulate stages will rubber-stamp each other's hallucinations. Defense-in-depth via more LLM reasoning doesn't help — it shares the underlying failure.

**Fix (tier-1 deterministic guardrails before Reflex Build triggers):**
- **Range checks** on numeric sensor outputs (engagement rates, quality scores) — flag values outside historical bounds
- **Isolation Forests** for multivariate anomaly detection on sensor output vectors
- **Cross-VLM ensemble** at high-stakes decision points: if Pinkerton's primary VLM and a secondary VLM (different family) disagree on a finding above some threshold, escalate to human review
- **PSI on sensor output distributions** — sudden distributional shifts trigger review before propagation
- `guardrail_flags` array in every sensor response (see MCP contract above)
- Reflex Build agents must check `guardrail_flags` and abort/escalate if non-empty

**The architectural principle:** cheap deterministic checks first, expensive LLM reasoning second. Defense-in-depth via different mechanisms, not via more of the same.

### 4. Cohort Selection Bias (Cohort Mode Specific)

**What goes wrong:** Reflex Detect queries `cohort_signature` for "users in segment X." The cohort has 50K users; sampling cap is 500. If the sampler isn't stratified, the 500 sampled may over-represent high-engagement users (more recent activity, easier to fetch features for, faster cache responses). Resulting aggregate signature reflects "engaged subset of segment X" not "segment X." Reflex Detect forms a hypothesis ("segment X engages with style Y") that's actually about a sub-population, and Build agents ship a fix that misses the at-risk users it was supposed to help.

**Why this is structural in cohort mode:** sampling is a load-bearing operation, and the "natural" sampler (whatever's fastest) systematically biases toward easy-to-fetch users.

**Fix:**
- **Stratified sampling is the default**, not an opt-in. `stratify_by` field in the contract forces the agent to specify stratification dimensions; Pinkerton enforces stratification within sampling
- `stratification_realized` in the response surfaces what was actually achieved vs requested
- Reflex Detect treats responses where `stratification_realized` materially diverges from `stratify_by` as suspect (guardrail flag triggers)
- `multimodality_detected` flag forces the agent to consider re-segmenting when the cohort is over-aggregating distinct populations
- Default `stratify_by` for Reflex Detect calls: `[engagement_tier, market]` (the two dimensions most likely to bias)
- Cost discipline: cohort with sample_size=500 and stratification=4-dim is the budget ceiling for synchronous calls; larger goes async

---

## Observability

### OpenTelemetry GenAI semantic conventions

Every MCP tool call emits `execute_tool` span with:
- `gen_ai.tool.name`
- `gen_ai.usage.input_tokens` / `gen_ai.usage.output_tokens`
- `pinkerton.signature_id`
- `pinkerton.cache_status`
- `pinkerton.vlm_version`
- latency

Trace context propagates via JSON-RPC headers from Reflex orchestrator → Pinkerton sensor → underlying ML model. Industry-standard tooling (Datadog, Honeycomb, New Relic) consumes OTel GenAI spans natively.

### Immutable event logging

Every Pinkerton → Reflex handoff logged to immutable data lake with full context: inputs, outputs, model versions, timestamps, cache status, guardrail flags. **Non-negotiable.** When Reflex authors a bad PR on Tuesday, you must be able to reconstruct the exact Pinkerton state Reflex consumed at decision time. Without this, bad decisions are undebuggable.

### Structured logs for joinability

Every sensor call logs `{caller_agent_id, tool_name, signature_id, schema_version, vlm_version, cache_status, latency_ms, guardrail_flags}` to the canonical Reflex experiment log. This enables joining sensor calls to experiment outcomes for post-hoc attribution.

### Feature ownership as a forcing function

Every Pinkerton sensor has a named owner + SLA + freshness monitor. Orphaned sensors are the production hazard MLOps teams flag explicitly — they get stale, break, and nobody notices. The owner is the first call when Reflex produces an anomalous result that traces back to that sensor.

---

## Implementation Sequencing

### Phase 0 — V0 (5/12 → 5/29) — Single-user mode

In progress. The brainstorm doc's Q5 + Q5a resolved here:
- **Pattern A confirmed** for Reflex Detect ↔ Pinkerton (data API)
- **Single-user mode ships first** per Q5a; cohort mode deferred to Phase 1
- Function + thin CLI sufficient for V0; MCP server deferred to Phase 1
- `signature_id` + `audit_trail_uri` + `schema_version` baked into V0 schema so Phase 1 MCP wrapper is a clean lift
- Per-pin caption cache populated during V0 runs — directly enables cohort mode's batching efficiency in Phase 1
- Visual coherence metric (Week 2 eval) is the first signature-partitioned attribution instance

### Phase 1 — China gap → end Q2 (MCP wrapper + cohort mode + substrate hardening)

Focus is on hardening the visual signature into a production-grade substrate primitive across both modes, not on shipping additional sensors. Additional primitives ship when Reflex consumption pulls for them, not on a schedule.

- Wrap V0 function as MCP tool: `pinkerton.visualize.user_signature.v1`
- **Ship cohort mode**: `pinkerton.visualize.cohort_signature.v1` with stratified sampling default
- Schema registration + version-pinning protocol (so future primitives plug in cleanly)
- Tier-1 guardrails: range checks + PSI on signature distributions; cohort-level PSI separate from user-level
- OTel GenAI span emission (with cohort-specific attributes: `cohort_size_sampled`, `sampling_rate`, `stratification_realized`)
- Immutable logging hook

**Why cohort mode is Phase 1, not Phase 2:** Most Reflex Detect hypotheses are cohort-level ("segment X engages with Y"). Without cohort mode, Reflex Detect is forced to either (a) call single-user mode N times then aggregate itself (wasteful, no shared cache benefits), or (b) skip Pinkerton for cohort queries (defeats the substrate). Cohort mode is load-bearing for Reflex Detect's primary use case.

### Phase 2 — Q3 (A2A façade + Reflex Build consumption)

- A2A `pinkerton.investigate` skill (façade over MCP for human investigators)
- Reflex Build agents consume signatures as spec input
- Cross-VLM ensemble at high-stakes decision points
- Cross-surface formalization (shared schema for Pinkerton-Notifs ↔ Pinkerton-HF)
- Shadow mode protocol formalized for VLM upgrades

### Phase 3 — Q4 (Prove stage + event triggers)

- Signature-partitioned attribution in Reflex Prove
- VLM arm auditing + visual guardrail
- Event stream IF concrete subscriber emerges (Anticipation eval, dashboards)
- Hypothesis revalidation runbook formalized

### Phase 4 — 2027 (Production scale)

- Tier 1 batch pre-compute migration for hot sensors
- Tier 3 demand-driven freshness (drop pre-compute for sensors Reflex doesn't query)
- Code-execution-with-MCP pattern if sensor count exceeds 20+ (Anthropic Nov 2025 pattern)

---

## What's Genuinely Uncharted

Both research streams flagged honestly:

1. **The autonomous Build loop is 2025-2026 territory.** No production examples of a system that autonomously writes and validates PRs against substrate diagnostics. The instrumentation and guardrail patterns above apply by analogy from MLOps, but you're in partially uncharted territory on Build → Simulate → Prove loop design specifically. James's own engineering judgment fills the gap.

2. **A2A maturity is thin.** Protocol is real but production interop between independent A2A agents is rare. If Pinkerton's consumers are all Pinterest-internal for the foreseeable future, you could expose `investigate` as another MCP tool on the same server and skip A2A entirely. A2A only earns its keep if (a) external/third-party agents will consume Pinkerton, or (b) vendor-neutral semantics matter for Pinterest's internal agent ecosystem.

3. **Same-model-family ensemble for guardrails.** The cascading-hallucination fix recommends cross-VLM ensembles at high-stakes decisions. But cross-family VLM access at Pinterest is an open question — depends on Piyush's confirmation of which VLMs are accessible. If only one family is accessible, the deterministic guardrails (range checks, PSI, Isolation Forests) carry more weight.

---

## How to Share This

- **Andrew** — primary audience. This is the architectural complement to his Reflex pipeline. Lead with the Pattern A decision (Pinkerton stays dumb-but-rich) and the cascading-hallucination failure mode (it's an architectural risk to his loop, not just Pinkerton's). Frame as: *"Here's the substrate interface contract that lets Reflex's Detect/Build/Simulate/Prove agents reason cleanly without hallucination cascades."*
- **Piyush** — VLM access path discussion (Phase 1 dependency: confirm VLM access, ideally cross-family for ensemble guardrails)
- **Dimitra** — cross-surface schema implications when Pinkerton-Notifs and Pinkerton-HF formalize Phase 2
- **Anna K (Anticipation)** — `cohort_signature` mode is what makes signatures-as-eval scale (per-cohort coherence metric vs Anticipation's served distribution); `signature_id` + `cohort_signature_id` hooks make signature-partitioned attribution and aggregate eval clean partnership patterns
- **Hold from Jeff/Rajat** — too technical for VP altitude. The strategy doc is the right artifact for them; this one is for the technical leads.

---

## Cross-references

- `reflex_pinkerton_strategy_051626.md` — strategic framing (dark factory + sensor substrate)
- `2026-05-11-pinkerton-vlm-visual-signature-brainstorm.md` — V0 spec; Q5 resolved here
- `2026-05-11-vlm-in-reflex-brainstorm.md` — agent-facing sensor catalog
- `reflex_redesign.md` — Reflex target architecture; invariants I-0 → I-3

## Source attribution

- **Web research** (agent-spawned 2026-05-16): MCP spec, A2A spec, Anthropic's "Building Effective Agents" + "Multi-Agent Research System" essays, LangGraph + OpenAI Agents SDK docs, OpenTelemetry GenAI semantic conventions, Confluent + Red Hat on event-driven agent architectures
- **ML & AI System Design notebook consult** (NotebookLM session `1db85aa6`, 2026-05-16): feature store patterns, MLOps versioning, PSI drift monitoring, shadow mode, failure-mode catalog (silent failures, training-serving skew, cascading hallucinations), defense-in-depth guardrails
