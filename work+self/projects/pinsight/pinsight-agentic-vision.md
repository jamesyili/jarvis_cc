# Pinsight → Agentic Recommendation: Research-Grounded Vision

> Synthesis of five agentic-recsys papers against Pinsight's current roadmap. Forward-looking, not a committed plan. Draft for grilling / iteration.

**Inputs:**
- `[AdobeMar2025]AgenticRecommenderSurvey.pdf` — taxonomy of LLM-based agentic recsys (LLM-ARS), four-level RS evolution, four core modules.
- `[GoogleApr2026]MAVR.pdf` — multi-agent video recommender patterns, direct analog for Pinterest's visual surface.
- `[TsinghuaNov2024]MACRec.pdf` — concrete multi-agent collaboration framework (Manager / Reflector / Analyst / Searcher / Task Interpreter).
- `[AmherstFeb2024]CooperativeAgents.pdf` — cognitive architecture for cooperative agents (perception / memory / communication / planning / execution).
- `[RUFeb2024]UserBehaviorSimulation.pdf` — RecAgent, LLM agents as simulated users for offline eval.

**Anchor docs:** `work+self/projects/pinsight.md`, `work+self/projects/pinsight-m1-spec.md`.

---

## 1. Main Ideas to Adopt

### 1.1 Decompose the single "debugger LLM" into a multi-agent crew (MACRec + MAVR pipeline pattern)

M1 today is a single LLM + Presto MCP walking through six phases. That works for debugging 3-5 pins per request, but it will not scale to M2 user understanding or M3 aggregate analysis, and it produces shallow diagnoses because one model is doing perception, analysis, and synthesis in one pass.

Adopt MACRec's role decomposition, adapted to our domain:

| Pinsight role | MACRec analog | Responsibility |
|---|---|---|
| **Manager** | Manager | Owns Thought / Action / Observation loop; assigns subtasks; produces final report. |
| **Funnel Analyst** | Item Analyst | Deep knowledge of the 14 HF stages; writes and interprets Presto queries over `bi.core_daily_homefeed_backend_funnel_candidate_evaluation`; compares selected pins against the population. |
| **User Analyst** | User Analyst | Builds a structured interest / intent profile from engagement history — this **is** Pinsight M2 as a reusable service. |
| **Content Analyst** | (new — VLM) | VLM-powered pin perception: what the pin actually depicts, style, quality signals. Closes the MAVR "item perception" loop. |
| **Searcher** | Searcher | Pulls Pinterest-internal knowledge: wiki, TL doc corpus, Kibana dashboards, prior Pinsight sessions. |
| **Reflector** | Reflector | Critiques the Manager's draft diagnosis. Learn-Act-Critic loop (RAH). Catches hallucinated signals, checks logical coherence. |
| **Task Interpreter** | Task Interpreter | Translates loose natural-language asks ("why am I seeing so many video pins today?") into structured investigation tasks. |

**Why adopt:** MACRec is the cleanest, simplest multi-agent recipe in the literature. The roles map 1:1 to debugging work we're already doing manually. Manager + Analyst + Reflector composed over ReAct loops is battle-tested (same pattern as Claude Code itself).

**What to skip:** We do **not** need MACRec's "diverse application" abstraction (rating prediction / sequential rec / etc.). Pinsight is diagnostic. Keep the crew focused.

### 1.2 Cognitive memory across sessions, not just in-session tracing (Cooperative Agents + RecAgent)

M1 already has a SQLite trace DB — that's episodic memory for free. Extend to the three memory types used in CoELA / RecAgent:

- **Semantic memory** — long-lived facts about the HF system: stage semantics, signal definitions, CG source catalog, known failure modes, team ownership. Today these live scattered across wikis, runbooks, and TL memory. Make Pinsight own a structured knowledge base it can read.
- **Episodic memory** — per-session traces (already in M1 spec). Queryable across sessions. "Have we seen this diagnosis pattern before?" is a killer feature once the DB has history.
- **Procedural memory** — reusable playbooks: "debugging CG dropout," "investigating SSD over-aggression," "diagnosing content type imbalance." Each playbook is a SKILL.md-style prompt the Manager can invoke.

**Why adopt:** Without this, every session starts from zero and every agent rediscovers the same basics. With this, each Pinsight run compounds the team's knowledge. This is the Karen synthesis-over-collection move applied to diagnostic work.

### 1.3 VLM pin perception as a reusable cache, not a one-shot call (MAVR IP Agent)

MAVR's Item Perception Agent compresses raw video into semantic summaries so downstream agents can reason without blowing context windows. Do the same for pins, **once**, and cache:

- For each pin touched in any Pinsight session, generate a semantic summary (what is depicted, style, genre, likely creator intent, quality markers).
- Cache in a structured store keyed by pin_id.
- Content Analyst reads from cache; on miss, produces and writes.

This cache is reusable across M1 (per-pin diagnosis), M2 (user understanding — "what does the user's engagement history actually show?"), M3 (aggregate content supply analysis), and eventually any agentic augmentation layer.

**Why adopt:** One upfront investment, N downstream uses. Pinterest's visual-first nature makes this higher-leverage than for text-only recsys. Closes the "modality gap" MAVR explicitly names as the justification for multi-agent decomposition on video.

### 1.4 User simulation as offline verification (RecAgent / Agent4Rec + Reflex "Verify" stage)

This is the most speculative adoption — and also the biggest strategic unlock.

RecAgent shows you can take structured user profiles (age, traits, interests, history) and drive LLM agents through a recsys sandbox to generate believable behavior. Agent4Rec scales this to 1,000 simulated users and reproduces known phenomena (filter bubbles). The simulator is **agnostic to the recommender algorithm** — you can swap in any model and measure behavioral outcomes.

For Pinterest, this unlocks Reflex's "Verify" stage without live A/B:

1. Pinsight M2 already produces user profiles.
2. Build a sandbox that replays frozen HF candidates and lets simulated-user agents take actions (click, save, skip, long-dwell).
3. Validate the sim: does aggregate simulated behavior match held-out real aggregate?
4. Once validated, use the sim to test hypothesized changes offline: "if we reweight SSD by X, does simulated long-term engagement improve for segment Y?"

**Why adopt:** This is the piece that turns Pinsight from a diagnostic tool into a **design feedback loop**. It's also the piece that maps Pinsight onto Reflex's full pipeline (Detect → Diagnose → Design → **Verify** → Experiment → Explain).

**Why cautious:** Simulator fidelity is the central risk. RecAgent and Agent4Rec both acknowledge the sim-to-real gap. Do not build this until M2 profiles are validated against real behavior. Do not replace A/B. It is a **pre-A/B screen**, not a replacement.

### 1.5 Learn-Act-Critic loop + reflection (MACRec Reflector, RAH)

Small, cheap addition with outsized quality impact: every diagnosis the Manager produces goes through a Reflector pass before the human sees it. The Reflector asks:

- Is the claimed causal story actually supported by the retrieved data?
- Are there alternative explanations the Manager missed?
- Does the diagnosis contradict anything in semantic memory (known stage behavior)?
- Are any hallucinated signals (scores that were never fetched, stages that don't exist)?

**Why adopt:** One of the most consistent findings across MACRec, RAH, CoELA, and the Adobe survey is that a Critic / Reflector loop improves output quality more than better prompts alone. It is also cheap — single LLM call per session.

### 1.6 Human-in-the-loop control (TKGPT + RAH + CoELA user study)

Keep the human in the loop everywhere for the foreseeable future. Pinsight M1 already does this in Phase 2 (human picks pins to analyze). Extend the principle:

- Diagnosis stage: Reflector surfaces alternative hypotheses; human picks which to pursue.
- Aggregate analysis (M3): human defines the segmentation question; agents execute.
- Simulation (future): human scopes the counterfactual; agents run it.
- Augmentation (future-future): human-selected eligible segments only, A/B bounded.

**Why adopt:** All five papers converge on this. Agent autonomy is a research aspiration; in a production recommender, trust is the bottleneck, not capability.

### 1.7 Ideas to explicitly **not** adopt (yet)

- **Full autonomous recommender agent** (Agent4Rec, InteRecAgent as recommender): risk-to-reward is wrong for Pinterest. Our production recsys is mature; LLM-ARS can augment explore, not replace exploit.
- **MAVR Hierarchical Orchestration with central coordinator** over the full pipeline: single-point-of-failure risk, coordinator becomes a bottleneck. Use Pipeline at the top level, Hierarchical only inside the diagnosis step.
- **Agent-based candidate generation** as the primary CG: mature deep models (CLR) dominate here. LLM reasoning is better used for reranking / augmentation / cold-start, not primary retrieval.
- **CoELA's costly-communication optimization** literally: our agents run in one process, not distributed. The principle (be deliberate about what to surface) is worth keeping; the specific formalism is overkill.

---

## 2. Essential Building Blocks

Ordered roughly by how load-bearing they are for the rest of the stack. Each is a discrete artifact we'd need to build.

### 2.1 Trace store (episodic memory) — **exists in M1 spec**

SQLite DB with `sessions`, `phases`, `queries`, `pin_analyses`, `diagnosis` tables (already designed in `pinsight-m1-spec.md`). Extensions needed:

- Add `embeddings` column to `diagnosis` for similarity search over past sessions.
- Add `playbook_used` column to `phases` to track which procedural memory entry was invoked.
- Migration path to Postgres once >1000 sessions accumulated.

### 2.2 Funnel query library — **partial, currently ad-hoc in SKILL.md**

Extract the 8-10 canonical Presto queries (final chunk pull, CG distribution, score percentiles, per-head median, drop-reason breakdown, etc.) into a parameterized library. Each query:

- Is testable in isolation (unit test against a snapshot).
- Has a docstring explaining what funnel question it answers.
- Is invoked by name by the Funnel Analyst agent, not freestyled every session.

### 2.3 Agent prompt library

Per-role SKILL.md files: `manager.md`, `funnel_analyst.md`, `user_analyst.md`, `content_analyst.md`, `searcher.md`, `reflector.md`, `task_interpreter.md`. Each contains:

- Role description
- Available tools (which subset of MCP + which library functions)
- Input/output contract
- Failure modes and recovery
- Anti-hallucination rules specific to the role

### 2.4 Semantic memory store

Structured markdown (or JSON) files under `pinsight/knowledge/` containing:

- HF funnel stage reference (stage name → what it does → common drop reasons → what signals matter).
- CG source catalog (source name → what it retrieves → when it dominates → known failure modes).
- Signal definitions (LWS heads, ranking heads, SSD, presorting — what each means).
- Team ownership map (who owns which stage, for escalation).

The Manager and all Analysts can read this. It's rebuilt manually for now; later, a scout-style skill can keep it in sync with internal wikis.

### 2.5 Procedural memory / playbooks

One markdown per canonical investigation type:

- `playbook_cg_dropout.md` — candidate disappeared mid-funnel
- `playbook_ssd_overaggressive.md` — SSD demoting good pins
- `playbook_content_type_imbalance.md` — feed over-indexed on one type
- `playbook_cold_start.md` — new-ish user getting low-quality recs
- `playbook_cross_user_comparison.md` — same pin performing differently across users

Each playbook is a prompt template the Manager can invoke. Lets us bank expertise as we discover it.

### 2.6 VLM pin perception cache (**new infrastructure**)

A service that, given a pin_id, returns a structured semantic summary:

```json
{
  "pin_id": 12345,
  "subject": "vegan chocolate cake",
  "visual_style": "overhead flat lay, moody lighting",
  "quality_markers": ["professional photography", "clean styling"],
  "likely_intent": "recipe share or food blog CTA",
  "content_type": "image",
  "generated_at": "2026-04-05T...",
  "model": "claude-sonnet-4-6"
}
```

- Backed by a Hive / Iceberg table or a local cache for early prototyping.
- Populated lazily on first touch by the Content Analyst.
- Reusable across M1, M2, M3, and (later) agentic augmentation.
- Estimated cost: batch VLM call at ~$0.003-0.01 per pin; pre-populate hot corpus (~10M pins).

### 2.7 User profile module (this **is** Pinsight M2)

A structured, reusable profile per user:

```json
{
  "user_id": 12345,
  "core_interests": [...],
  "style_signals": [...],
  "intent_modes": ["shopping", "inspiration"],
  "temporal_patterns": {...},
  "session_types": [...],
  "recent_pivots": [...]
}
```

- Generated from engagement history by VLM + LLM reasoning over (pin_image × engagement_action) pairs.
- Caching and freshness same story as 2.6.
- Downstream consumers: M1+ diagnosis (rich user context), M3 aggregate (segment definition), simulation harness (seed for simulated users), UIC eval for Retentive Recs.

### 2.8 Reflector agent

Cheap reflection pass over the Manager's draft diagnosis. Checks:

- Every numeric claim traces back to a logged query result.
- Every mentioned stage exists in the funnel.
- Claimed causal direction is consistent with funnel order.
- Conclusion is bounded by the evidence actually fetched.

### 2.9 Report templates

Structured markdown output with standard sections: request context, per-pin traces, Funnel Analyst summary, Content Analyst summary, User Analyst summary, Manager diagnosis, Reflector notes, open questions, suggested follow-up queries. Consistency matters when reports are read by different stakeholders.

### 2.10 Eval harness (**biggest unknown, gates Phase 4**)

Two components:

1. **Replay environment** — a frozen snapshot of an HF session (candidates at each stage) that can be fed to a simulated user agent for repeated evaluation.
2. **Behavioral fidelity metric** — a KL-divergence-style comparison of simulated user behavior vs. held-out real user behavior on the same candidates.

This is where the Adobe survey, Agent4Rec, and MAVR all converge on the same unsolved problem. We should **not** pretend we've solved it; we should build the scaffolding and measure how far off we are.

---

## 3. Sequencing — Debugging First, Agentic Later

The through-line: **each phase produces a demoable artifact, each phase reuses infrastructure from the prior phase, and no phase depends on unvalidated assumptions about LLM capabilities we haven't tested**. Every phase is a real shippable thing, not a stepping stone to the next.

> **Sequencing note (2026-04-05):** Earlier draft inserted a "multi-agent decomposition" phase between M1 and M2. Dropped after grill — ships single-agent M1 then single-agent M2, lets the multi-agent refactor fall out naturally when M3's cost profile forces it. Do not refactor M1 for aesthetics; refactor only when scale demands it.

### Phase 0 — M1 single-agent debugger (in-flight)

**What:** The current `pinsight-m1-spec.md` build. Single LLM + Presto MCP + six phases. Human picks pins. Markdown report + SQLite trace.

**Why this is the right start:**
- Parity with Roberto's Search debugger.
- ~10 hours to build (already scoped).
- Generates the first real episodic memory.
- Forces us to solve the boring-but-load-bearing data access story first.
- Zero agent-orchestration risk.

**Exit criteria:** M1 demoable to Jeff. SQLite has ≥10 real debug sessions. James has handed off to Alok or extended it himself.

### Phase 1 — Pinsight M2 as the User Profiling Module (late Q2 / early Q3)

**What:** The current roadmap M2, reframed as a **reusable User Profiling Module** (building block 2.7) rather than a standalone report generator. First deliverable is still a markdown report ("here's what we know about this user"), but the underlying profile structure is designed for reuse.

**Architecture:** Still single-agent at this phase. One prompt, one LLM, one VLM for pin perception. Do not introduce multi-agent orchestration yet.

**What this unlocks:**
- M1 can optionally consume profiles for richer user context (non-blocking enhancement).
- UIC eval for Retentive Recs ships on top of the profile module (Goal 1 tie-in).
- Profile structure is the seed for later simulation (Phase 4).

**Concurrently:** start populating the VLM pin perception cache (2.6) — this is shared infra with M2 and cannot be built later.

**Exit criteria:** Profile module produces structured output for any employee user in <30s. UIC eval partially leveraging the module. Pin perception cache has ≥100K pins.

### Phase 2 — Multi-agent refactor, driven by M3 scale pressure (Q3)

**What:** Refactor M1 and M2 into a MACRec-lite crew. Manager + Funnel Analyst + User Analyst + Content Analyst + Reflector. Funnel query library (2.2) replaces ad-hoc SQL. Semantic memory (2.4) gets its first entries. Reflector runs on Manager's drafts.

**Why now and not sooner:** The multi-agent refactor is not justified by quality improvements on individual debug sessions — it is justified by the cost / latency / composability demands of running the same logic across thousands of requests. M3 is the forcing function. Refactoring earlier would be building infrastructure for its own sake.

**What triggers the refactor:**
- M3 scale analysis requires decomposing the work (perception / query / reasoning / reflection) for parallel execution and per-stage cost control.
- We are re-implementing the same user context and pin perception in both M1 and M2 and it's getting painful.
- We have ≥20 real debug sessions showing the same hallucination patterns that a Reflector would catch.

**Exit criteria:** M1 and M2 both run on the refactored crew with quality at least matching single-agent versions. Semantic memory has 20+ entries. One shared trace / memory substrate across both. Ready to scale to M3.

### Phase 3 — M3 Scale Analysis as the "Detect" layer (Q3)

**What:** Run M1+ at scale across many users and requests. Aggregate patterns into systematic insight surfaces:

- Relevance gaps by segment
- Content supply gaps for high-intent users
- Training data staleness indicators
- Cross-surface quality deltas
- UIC validation at scale

**Reusing:** Funnel query library, agent crew, semantic memory, pin perception cache, profile module. Nothing new is load-bearing.

**What's new:** Batch orchestration layer. Cost management (this is where LLM spend becomes real — pre-compute pin perceptions, batch profile generations, sample users rather than process all).

**Reflex mapping:** This **is** the Detect stage. M1+ + M2 together **are** the Diagnose stage.

**Exit criteria:** M3 produces at least one insight leading to a tracked intervention. Cost per aggregate analysis run <$100 at the sample size that gives statistical power.

### Phase 4 — Offline simulation harness (post-Q2, strictly gated)

**What:** Build the RecAgent-lite sandbox (building block 2.10). Simulated users driven by M2 profiles interact with frozen HF candidate replays.

**Strategic decision (2026-04-05):** Committed. Fork A from the grill — we go big. Rationale: Andrew invited co-ownership of Detect + Diagnose in Reflex; if the Reflex conversation evolves toward Design / Verify, Pinsight needs infrastructure in place for the answer to be "yes, we can become that." Dropping this phase forecloses that conversation before it happens.

**Hard gate (must pass before any build starts):** M2 profiles must pass a held-out prediction test. Given a profile generated from user X's engagement history up to time T, does the profile predict X's aggregate behavior from T to T+30 days better than a baseline that ignores the profile? If yes, simulator has a fighting chance at fidelity. If no, Phase 4 defers indefinitely and Pinsight stays diagnostic.

**Timing:** Earliest start is Q3 2026, and only if the gate passes. Likely post-Q2 entirely given M1 and M2 need to ship first and M2 profiles need enough runway to be validatable.

**What it unlocks:**
- Reflex "Verify" stage — test hypothesized changes before A/B.
- Faster iteration on ranking / SSD / CG changes for segments where A/B is slow.
- A sandbox for studying emergent phenomena (filter bubbles, over-exploitation) without touching prod.

**What to be honest about:** The literature does not yet have a reliable answer on sim-to-real. We should build this with realistic expectations — it is a **screening tool**, not a replacement for A/B. Measure the fidelity gap explicitly and surface it to every downstream consumer.

**Exit criteria:** Sandbox runs end-to-end for ≥1 realistic scenario. Behavioral fidelity metric reported against held-out real data. One successful "screened in / screened out" decision made before launching an A/B.

### Phase 5 — LLM augmentation pilot (Q4+, gated on Phase 4 validation)

**What:** First production LLM augmentation. **Not** replacing the recsys. Pipeline pattern:

```
Production candidates (CLR etc.) → Content Analyst (VLM summaries from cache) →
Reasoning Agent (rank/rerank with user profile + world knowledge) → Subset served in bounded A/B
```

**Targeting:** Long-tail segments or cold-start users where classic recsys struggles. This is where LLM world knowledge has the biggest relative lift and the smallest risk to the core engagement surface.

**What this is testing:** Can LLM reasoning recover candidate quality on segments where engagement signals are sparse? If yes, this becomes Reflex's "Design" stage (proposing interventions).

**What it's explicitly not:**
- Not a new candidate generator.
- Not LLM-as-ranker for the full feed.
- Not autonomous — every segment, every ranking change goes through experimentation.

### Phase 6 — Hybrid RL-LLM (speculative, likely beyond 2026)

**What:** Follow MAVR's hybrid direction. LLM plans high-level goals or reward-shaping functions; downstream RL policy executes fine-grained decisions. Pinsight's diagnostic + simulation infrastructure becomes the training/eval substrate.

**Why this is last and fuzzy:**
- The literature doesn't have production examples yet.
- Requires all prior phases to be stable.
- The capability we'd need (reliable LLM reward-shaping) is still an active research question.

**How to leave room for it now:** Keep Phase 1-5 infrastructure decoupled enough that RL can be plugged in as a new consumer of user profiles, pin perceptions, and the simulation harness. Do not over-design for it.

---

## 4. Open Questions / Things to Grill

1. ~~**Phase 1 vs Phase 2 order:** Should we deepen M1 (multi-agent decomposition) before shipping M2?~~ **Resolved 2026-04-05:** No. M1 single-agent → M2 single-agent → multi-agent refactor when M3 forces it.

2. ~~**Is the simulation harness worth the bet?**~~ **Resolved 2026-04-05 (Fork A):** Yes, committed, with held-out prediction gate on M2 profiles. See Phase 4.

3. **Staffing:** Deliberately deferred. James stays hands-on architect + builder through Phase 1-2 at least. Staffing conversation revisited once the project is more visibly successful — probably after M2 ships and delivers measurable UIC eval value for Retentive Recs.

4. **What's the smallest credible agentic augmentation experiment?** Phase 5 is described in broad strokes. What's the actual MVP — 1 cold-start segment, 1 ranking feature, 1 week A/B? Worth scoping concretely before anything earlier phases commit to it.

5. **Cost / scalability:** The Adobe survey, MAVR, and Agent4Rec all name cost as the #1 blocker. We have not modeled total LLM spend across phases. Need a rough cost-per-phase estimate before committing to Phase 3+.

6. **How much does this conflict with James's stated goal of synthesis-over-collection?** Karen's pattern — "hears feedback, builds infrastructure for the pivot instead of doing the pivot" — applies here. Is this vision doc the same trap? The counter-argument: Pinsight M1 ships regardless, and this doc just sequences what comes after. But worth naming the risk.

---

## 5. What This Doc Is Not

- Not a committed roadmap — staffing, dependencies, and cost estimates are missing.
- Not a design doc for any specific phase — those get written when the phase is scoped.
- Not an endorsement of specific papers' claims — sim-to-real gap, LLM-as-judge reliability, and incentive alignment in multi-agent RL are all unresolved in the literature, and this doc inherits those uncertainties.
- Not a replacement for the M1 spec — `pinsight-m1-spec.md` is what actually ships next.

Use as input to the Andrew / Reflex conversation, and as a forcing function for the Phase 1 scope decision.
