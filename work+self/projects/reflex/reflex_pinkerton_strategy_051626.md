# Reflex + Pinkerton — Strategy

**Date:** 2026-05-16
**Status:** Strategic framing doc — propagable to Andrew, Dimitra, Anna K, Dylan, and (selectively) Jeff/Rajat
**Source synthesis:** `pinkerton/jeff_demo_deck_2026-05-14.md` + `2026-05-11-pinkerton-vlm-visual-signature-brainstorm.md` + `2026-05-11-vlm-in-reflex-brainstorm.md`

---

## Thesis: Reflex is the recsys dark factory. Pinkerton is the sensor substrate that makes it run.

A **dark factory** in manufacturing is a lights-out facility that runs autonomously — machines execute, sense, adjust, and only escalate exceptions to humans. The economics are transformative: throughput goes up by 10×, marginal cost of iteration approaches zero, and humans move from running the line to designing the line and handling exceptions.

**Reflex is the recsys dark factory.** Detect → Build → Simulate → Prove is the autonomous loop. Humans define invariants, calibrate via RLHF, and handle exceptions; the loop runs the rest.

But a dark factory cannot run without sensors. Temperature, position, defect detection, throughput counters — without these, the machines are blind, and any "autonomy" is just unsupervised flailing. Pinterest's recsys today has the equivalent blindness: opaque embeddings, dashboards built for humans, no programmatic interpretable layer. Agents reasoning over this substrate have nothing to ground on.

**Pinkerton is the sensor and instrumentation substrate of the recsys dark factory.** It's not "a DSAT tool." It's not "VLM signatures." It is *the interpretability layer that any AI-driven recsys evolution structurally requires*. Visual signatures, content-quality scores, cross-surface DSAT traces, feed coherence metrics — these are the sensor primitives. Reflex's agents are the consumer.

This framing has three immediate implications:

1. **Reflex and Pinkerton are coequal architecture, not project + tool.** Reflex needs Pinkerton to be more than a hypothesis generator on aggregate metrics. Pinkerton needs Reflex to be more than a debugging tool. Together they are a complete autonomous recsys-improvement platform.

2. **Pinkerton's two consumer surfaces are unified, not separate.** The Jeff-demo Pinkerton (human-facing DSAT diagnosis) and the VLM-in-Reflex sensor catalog (agent-facing detection/simulation) are *the same substrate accessed by different consumers*. A unified substrate with multiple API surfaces (CLI, function call, MCP tool, async dispatch) — not two products.

3. **The FTE ask should anchor on substrate, not tool.** The Jeff-demo's 1-FTE ask is structurally about operationalizing Pinkerton as shared org infra. Framing it as "DSAT diagnostic" undersells; framing it as "the interpretability substrate Pinterest's AI-driven recsys evolution requires" overshoots for that audience. Land it as: *"shared cross-surface diagnostic substrate that already serves both human investigators and Reflex agents — needs an owner to operationalize."*

---

## Architecture

```
                    REFLEX  (Recsys Dark Factory)
        ┌──────────────────────────────────────────────────────────┐
        │                                                            │
        │   ┌─────────┐    ┌────────┐    ┌──────────┐    ┌────────┐│
        │   │ DETECT  │───►│ BUILD  │───►│ SIMULATE │───►│ PROVE  ││
        │   │ agents  │    │ agents │    │ (VLM     │    │ (arm   ││
        │   │         │    │        │    │  judge)  │    │  audit)││
        │   └────┬────┘    └────┬───┘    └─────┬────┘    └────┬───┘│
        │        │              │              │              │     │
        │        │              │ Curator + Skeptic gates    │     │
        │        │              │ Velocity dashboard          │     │
        │        │              │ RLHF feedback loop          │     │
        │        │              │ Invariants I-0 → I-3        │     │
        │        │              │                             │     │
        └────────┼──────────────┼──────────────┼──────────────┼─────┘
                 │              │              │              │
                 ▼ query        ▼ spec         ▼ ground truth ▼ attribute
        ┌──────────────────────────────────────────────────────────┐
        │           PINKERTON  (Sensor + Instrumentation Substrate) │
        │                                                            │
        │   What exists today:                                       │
        │   • Visual user signature (V0 in flight, ships 5/29)      │
        │   • Cross-surface DSAT trace (Pinkerton Jeff demo tool)   │
        │                                                            │
        │   Substrate pattern (extends to additional primitives      │
        │   when consumption justifies — not pre-planned catalog):   │
        │   • Structured-data + narrative-description hybrid output  │
        │   • Cached, with audit trail / lineage                     │
        │   • Two modes: single-user + cohort (stratified sampling)  │
        │   • Three API surfaces: function, CLI, MCP tool            │
        │   • Versioned schema; drift-monitored                      │
        └──────────────────────────────────────────────────────────┘
              ▲                                          ▲
              │ humans query                             │ external systems query
              │ (DSAT investigation, RLHF labels,       │ (Anticipation eval, surface
              │  exception handling, exec demos)         │  dashboards, AB attribution)
              │                                          │
        ┌─────────────┐                          ┌──────────────────┐
        │ ENGINEERS    │                          │ ANTICIPATION     │
        │ EMs / PMs    │                          │ SURFACE TEAMS    │
        │ VPs (Jeff,   │                          │ AB ANALYTICS     │
        │   Rajat)     │                          │                  │
        └─────────────┘                          └──────────────────┘

  * = currently live or in V0 build
```

The substrate has **three consumer classes**:
- **Reflex agents** (Detect/Build/Simulate/Prove) — programmatic query for autonomous reasoning
- **Humans** (engineers, EMs, PMs, VPs) — interactive query for investigation and decision-making
- **External systems** (Anticipation eval, surface dashboards, AB analytics) — structured-data consumption

All three consume the same primitives. The substrate's value compounds with each new consumer; each new sensor primitive serves all three.

---

## What exists today + what extends

### What's actually built or in flight

**Pinkerton (substrate side):**
- **Visual user signature** — V0 in 3-week build (5/12 → 5/29). Per-pin VLM captioning → per-user aggregate; structured + narrative hybrid; cached. First sensor primitive; defines the pattern.
- **Cross-surface DSAT trace** — Live as the Pinkerton Jeff-demo tool. Walks an individual user's experience across surfaces (Notifs + HF v0; Dimitra-Chuxi joint).
- **14-stage HF funnel trace** — Live; per-request stage-by-stage diagnosis (the technical depth signal in Slide 5 of the Jeff deck).

**Reflex (consumer side):**
- **Detect / Build / Simulate / Prove pipeline** — Detect + early Build live; Curator + Skeptic quality gate live; Simulate stage proposed (VLM-as-feed-judge per VLM-in-Reflex brainstorm); Prove stage partial.
- **RLHF feedback loop + velocity dashboard** — in flight per `reflex_redesign.md` invariants I-0 → I-3.
- **Implementation agents** — Live (Asana card → PR write-back).

**Cross-org integration:**
- **HF + Notifs surfaces** integrated via Pinkerton v0 (James + Chuxi on HF; Dimitra on Notifs).
- **Search + P2P** future; no current commitment.

### How the substrate extends

The visual signature defines the *pattern* — structured-data + narrative-description hybrid, per-pin → aggregate, cached, two-mode (single-user + cohort). Future sensor primitives plug into the same shape. **The next primitive ships when Reflex consumption justifies it**, not on a pre-planned catalog. Candidate extensions from the VLM-in-Reflex brainstorm sit as ideas, not commitments — promoted to actual primitives only when a Reflex use case is pulling for them.

This is the "start with heuristics, earn the right to complexity" principle from production MLOps: ship one primitive, observe what consumers actually query, upgrade compute for what's load-bearing, drop what isn't. Avoid the inventory-driven trap of building 10 sensors before any consumer is pulling on them.

---

## Sequencing

### Phase 0 — Now → 5/29 (V0 ships)

- **Visual signature V0** lands as Pinkerton's first agent-facing sensor primitive
- **Pinkerton Jeff demo** executes (substrate gets exec sponsorship via human-facing artifact)
- **1-FTE ask** lands as the operating-substrate seed
- Eval (Week 2): visual coherence metric vs Anticipation top-K — first eval-partnership signal to Anna K

**Exit criteria:** V0 signature operational on 20 users; Jeff demo shipped; FTE routing pre-aligned with Dylan + Dimitra's manager.

### Phase 1 — China gap → end Q2 (substrate framing + MCP wrapper + cohort mode)

- **Substrate framing doc** (this doc, shareable form) circulated to Andrew, Anna, Dimitra; selectively to Jeff/Rajat as Pinkerton-as-substrate
- **Wrap V0 function as MCP tool**; lock the schema/vocabulary pattern so future primitives plug in cleanly
- **Ship cohort mode** for the visual signature (single-user → cohort is the load-bearing extension Reflex Detect needs for hypothesis formation; see interface design doc)
- **VLM-as-feed-judge prototype** in Simulate stage (highest-leverage Reflex addition per VLM-in-Reflex brainstorm)

**Exit criteria:** One sensor in both modes (single-user + cohort) operating through MCP; substrate API pattern documented; Simulate-stage prototype exists.

### Phase 2 — Q3 (cross-surface + agent consumption)

- **Cross-surface formalization** with Dimitra: shared schema for Pinkerton-Notifs ↔ Pinkerton-HF
- **Build agents consume signatures** as spec input (first signature-aware variant generation)
- **Simulate stage matures**: VLM-as-feed-judge becomes default pre-flight for Build outputs
- **Anticipation eval partnership** formalized with Anna K via signature-as-eval pattern (cohort mode is what makes this scale)
- **Additional sensor primitives ship only as Reflex consumption pulls for them** — not on a pre-planned schedule

**Exit criteria:** Two surfaces sharing substrate; signature-aware Build variants in flight; Simulate filtering Build output.

### Phase 3 — Q4 (prove-stage closure)

- **Signature-partitioned attribution** post-launch: "experiment lifted signature-X cohort by Y%, hurt signature-Z cohort by W%"
- **VLM arm auditing** + **visual guardrail** continuous monitor
- **Post-ship visual monitoring** for shipped experiments

**Exit criteria:** Reflex closes loops with signature-partitioned causal attribution; visual guardrail running continuously.

### Phase 4 — 2027 (dark factory at scale)

- Reflex closes loops without human-in-the-loop for low-stakes / high-confidence changes
- Humans operate at invariant-design, RLHF-curation, and exception-handling layer only
- Pinkerton substrate serves multiple surfaces and consumer classes; sensor primitives have grown to match observed consumption (not pre-planned to a target count)
- Director-altitude bet visibly compounded into platform reality