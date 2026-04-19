# Reflex Feedback Curator + Skeptic — Design Doc

Owner: James Li
Co-dev audience: Andrew Yaroshevsky, Dylan Wang
Last updated: 2026-04-18
Status: v0.1 draft — pre-code-read. Work-leo follow-up needed (see §7).

---

## 0. One-paragraph summary

Reflex's Detect stage ships PM Agent + DS Agent, with `quality_patterns.md` as shared institutional memory and human experts in the RLHF loop. That loop compounds well at cycle 13; at cycle 50+ with 7 experts across multiple surfaces, two structural roles are missing. The **Feedback Curator** owns quality-of-memory as an ongoing discipline — versioning, dedup, conflict resolution, decay-handling. The **Skeptic** owns pre-review quality — red-teaming opportunity cards against existing patterns so expert cycles go to novel catches, not re-teaching. Curator manages memory quality; Skeptic manages output quality. Together they close two structural gaps in the compounding loop.

---

## 1. Feedback Curator

### 1.1 Purpose

Custodian of `quality_patterns.md`. Keeps institutional memory high-signal as it grows beyond human-scannable size.

### 1.2 Why now

Reflex is at cycle 13. `quality_patterns.md` is 341 lines and growing per cycle. Projected to cycle 50, 100, that file is either:
- a well-versioned, queryable summary of battle-tested patterns, or
- a graveyard of contradictory, stale, unversioned corrections

The difference is whether someone owns memory-quality as an ongoing discipline. Today nobody does — patterns append-only. This degrades faster once multiple experts contribute across multiple surfaces, because contradictions become more frequent.

### 1.3 Responsibilities

1. **Pattern intake.** When a new expert correction lands (Asana comment or reviewer override), curator proposes a well-formed pattern entry following a standardized structure (see §1.5).
2. **Dedup + conflict resolution.** When a new pattern contradicts an existing one, curator flags the conflict, surfaces both, and proposes merge / version / replace. Human expert resolves; curator encodes the resolution.
3. **Decay handling.** When the underlying system changes (CG deprecated, table renamed, retrieval arch changed), curator identifies which patterns are now stale and flags for expert confirmation before retiring. Patterns are never retired autonomously.
4. **Retrieval support.** Offers ranked pattern lookups for PM, DS, and Skeptic agents — "what patterns apply to this hypothesis category / surface / claim type?"
5. **Audit trail.** Every pattern has a lineage record: who caught it, which cycle, which card, what the original fix was. Enables post-hoc reasoning: "why does Reflex believe X?"

### 1.4 Scope boundaries

- Does NOT generate new patterns autonomously — only shapes human-surfaced corrections.
- Does NOT retire patterns autonomously — only proposes retirement with human confirmation.
- Does NOT evaluate card content — that's Skeptic.
- Does NOT modify agent prompts or playbooks — that's Andrew's domain.

### 1.5 Pattern entry format (proposed)

```
## Pattern P-047: Following CG Holdout Status
Category: holdout-architecture
Surface: HF CG
Trigger: Card cites Following CG (ID 19) engagement data
Correction: Following CG is holdout-only. Low volume ≠ small feature. Do not
  propose engagement optimizations without confirming holdout-lift methodology.
Evidence:
  - cycle 4 card C-0037; reviewer: James Li; 2026-02-11
  - cycle 9 re-affirmation card C-0112; reviewer: James Li; 2026-03-20
Supersedes: —
Superseded by: —
Applies when: card.cg_source == "Following" OR card.claim references Following CG
Status: active
Last reaffirmed: cycle 9
```

### 1.6 Conflict report format

```
## Conflict Report CR-003
Cycle: 14
New pattern proposed: P-047 (Following CG holdout status)
Contradicts existing: P-023 (CG engagement rate interpretation)

Options:
  (a) Merge: P-023 general rule + P-047 as Following-specific exception
  (b) Version: P-023 applies to non-holdout CGs; P-047 to holdout CGs
  (c) Replace: P-023 was overbroad; P-047 supersedes

Curator recommendation: (b) — evidence suggests general rule still holds
outside holdout CGs.

Awaiting: James Li
```

### 1.7 Interaction pattern

- **Triggers on:**
  - New Asana comment on opportunity card (poll or webhook)
  - Reviewer override of a Skeptic flag
  - Scheduled audit every N cycles (default: N=6, matches PM Agent's library audit cadence)
- **Writes to:** `quality_patterns.md` — proposed changes only; human merges
- **Reads from:** `quality_patterns.md`, `context.md`, opportunity cards, Asana comment threads, past conflict reports

### 1.8 Failure modes to avoid

- **Over-curation** — patterns abstracted so far they lose domain specificity. Mitigation: preserve original reviewer language in the evidence field.
- **Under-curation** — memory grows into noise, agents can't effectively use it. Mitigation: scheduled audit cycles + ranked retrieval.
- **Silent pattern retirement** — curator removes a pattern still doing work. Mitigation: retirement always requires human confirmation; never autonomous.
- **Conflict avoidance** — curator merges contradictions into bland uninformative patterns rather than flagging. Mitigation: bias toward flagging; merging only after human decides.

---

## 2. Skeptic

### 2.1 Purpose

Adversarial pre-review agent. Sits between DS Agent's opportunity card and the human expert. Red-teams each card against existing patterns before it reaches us.

### 2.2 Why now

Today every card — regardless of whether it re-makes known mistakes — consumes expert review cycles. As Reflex scales to 7 experts × N surfaces, expert cycles become the binding constraint on the entire system. Skeptic load-sheds the obvious so humans spend cycles on novel catches, not re-teaching the system things it already knew.

Secondary motivation: reviewer fatigue degrades quality. If James reads 30 cards a week, card #29 gets less rigorous treatment. Skeptic absorbs the repetitive checks.

### 2.3 Responsibilities

1. **Pattern-check.** For each opportunity card, run against applicable patterns from `quality_patterns.md` (via Curator's retrieval). Flag violations.
2. **Context-check.** Cross-reference card claims against `context.md`: CG referenced but deprecated? Table named but renamed? Holdout status wrong? Retrieval architecture claim consistent with known codepath?
3. **Evidence-check.** Every quantitative claim must trace to a source (SQL query, table reference). Every qualitative claim (pin example) must have VLM verification. Flag unverified claims.
4. **Internal consistency check.** CG source claim consistent with user-history trace? Retrieval architecture claim consistent with known codepath? Signal-decay claim consistent with signal-source table?
5. **Novelty check.** Card archive lookup — has a similar hypothesis been explored? What was the outcome? Surface prior art so the expert sees context.

### 2.4 Output format

Structured critique **appended** to the card (not replacing any DS Agent content):

```
## Skeptic Review (auto-generated)
Card: C-0214
Cycle: 14
Pass/Fail: FAIL

### Flags
- [HIGH] Card cites INTEREST.prod engagement data. Pattern P-023 retires
  INTEREST.prod (deprecated cycle 7); replaced by Interest CLR.
- [MED] Claim "17% engagement lift in dormant users" has no traced SQL
  source. Schema section 2.3 requires query reference.
- [LOW] Pin example 3 lacks VLM verification per pattern P-019.

### Verified
- Holdout status correctly identified (non-holdout CG).
- CG source (reason_to_choose) matches retrieval codepath.
- Survey × engagement join uses correct table.

### Related prior cards
- C-0142 (cycle 7) proposed a similar INTEREST.prod optimization; retired
  because of the same deprecation.

### Action
Returning to DS Agent for revision. Max 1 more revision round before
escalating to human expert.
```

### 2.5 Pass / Fail semantics

- **PASS** — no flags higher than LOW. Card flows to expert with Skeptic notes appended as supplemental context.
- **FAIL** — one or more HIGH flags. Card returned to DS Agent with critique. DS Agent revises and resubmits. **Max 2 revision rounds** before mandatory escalation to human (prevents infinite loop, caps compute cost).
- **NEEDS-HUMAN** — ambiguous case (novel claim not covered by patterns, or Skeptic self-reports low confidence). Routes to expert with explicit "Skeptic couldn't evaluate" flag.

### 2.6 Scope boundaries

- Does NOT rewrite cards — that's DS Agent.
- Does NOT retire cards — human decision.
- Does NOT block cards from reaching human review after 2 revision rounds.
- Does NOT generate new patterns — flags class-of-issue, curator proposes pattern.
- Does NOT modify `quality_patterns.md` — read-only.

### 2.7 Interaction with Feedback Curator

- Skeptic uses patterns; does not write them.
- When Skeptic catches a violation not covered by an existing pattern, it emits: "consider adding pattern for [class of issue]" — Curator picks up for human review.
- When human expert **overrides** a Skeptic flag (approves a card Skeptic FAILed), that override is itself a signal Curator captures — either the pattern is wrong, or the pattern has an exception.

### 2.8 Failure modes to avoid

- **Over-blocking** — Skeptic becomes a bottleneck, experts never see borderline cases, DS Agent learns to write narrowly to pass Skeptic. Mitigation: hard cap on revision rounds; NEEDS-HUMAN default for ambiguity.
- **Under-catching** — Skeptic misses obvious issues, trust erodes, experts start ignoring its reviews. Mitigation: audit Skeptic against historical cards where we know the right answer.
- **Prompt overload** — Skeptic prompt grows into a mirror of `quality_patterns.md` rather than using it as an external resource. Mitigation: patterns live in file; Skeptic queries them via Curator.
- **False adversarial** — Skeptic adversarial against DS Agent specifically (learns to flag DS style rather than issues). Mitigation: prompt explicitly frames role as quality gate for experts, not adversary to DS.

---

## 3. Handoff sequence

```
PM Agent (playbook cycle) → hypothesis card
    ↓
DS Agent (enrichment) → opportunity card
    ↓
Skeptic → annotated card
    ├─ PASS → proceed to human
    ├─ FAIL (≤ 2 revisions) → back to DS Agent
    └─ NEEDS-HUMAN → proceed to human, flagged
    ↓
Human Expert → review, comment, approve / reject
    ↓
Feedback Curator
    ├─ Shape Asana comments into proposed patterns
    ├─ Detect conflicts with existing patterns
    └─ Propose updates to quality_patterns.md (human-merged)
    ↓
quality_patterns.md updated
    ↓
(feeds back to Skeptic and PM/DS agents next cycle)
```

---

## 4. Shared integration

### 4.1 File placement (proposed)

- `services/reflex/detect/agents/feedback_curator.md`
- `services/reflex/detect/agents/skeptic.md`

Both under existing `services/reflex/detect/CLAUDE.md` conventions. Alternative: new subdir `services/reflex/detect/quality/` for both — cleaner but creates a path precedent. Prefer flat placement; defer subdir decision.

### 4.2 Execution model

- **Skeptic** runs synchronously after DS Agent completes a card. Blocks forward flow until PASS / FAIL / NEEDS-HUMAN decision.
- **Curator** runs asynchronously:
  - Triggered: new Asana comment, Skeptic override, scheduled audit (every N=6 cycles).
  - Does not block any other agent's cycle.

### 4.3 MCP access

- **Skeptic** probably needs:
  - Read access to `quality_patterns.md`, `context.md`, card archive.
  - Optional: Presto MCP to re-run queries and verify claim evidence (high-value, higher-cost). Start without; add if drift observed.
- **Curator** probably needs:
  - Read + proposed-write access to `quality_patterns.md`.
  - Asana MCP for comment ingestion.
  - No Presto access needed.

### 4.4 Cost envelope

Both agents add per-cycle context load. Rough budget to hold:
- Skeptic: ~800 lines prompt + ~200 lines card + retrieved patterns (ranked, capped at top 10 relevant). Per card.
- Curator: ~600 lines prompt + up to 5 incoming comments + relevant slice of `quality_patterns.md`. Per trigger.

Flag for Andrew: we should track marginal cost per card through the pipeline as agent count grows.

---

## 5. Open design questions (flag for Andrew + Dylan)

1. **Does Skeptic FAIL block human review, or only annotate?**
   Current proposal: blocks for up to 2 DS revision rounds, then unblocks. Alternative: always annotate, never block — let DS decide whether to revise. Depends on how much Andrew trusts the gate vs. the expert.

2. **Does Curator propose new patterns autonomously, or only shape approved ones?**
   Current proposal: only shapes. Alternative: Curator proposes patterns as suggestions requiring human confirmation before entering `quality_patterns.md`. Depends on risk tolerance for pattern inflation.

3. **Where do Skeptic's pattern-applicability rules live?**
   Current proposal: per-pattern `applies_when` field in the pattern entry itself (§1.5). Alternative: separate index maintained by Curator. Depends on how expressive `applies_when` can be.

4. **Does Skeptic get its own MCP access (Presto), or rely on DS Agent's traces?**
   Current proposal: rely on DS traces (cheaper). Re-evaluate if evidence-check flags drift from reality.

5. **File placement — flat under `agents/`, or new `quality/` subdir?**
   Current proposal: flat. Aligns with `pm_agent.md` / `ds_agent.md`. Change if we expect more quality-layer agents (e.g., a future Attribution agent closing the Prove→Detect loop).

---

## 6. What this design does NOT cover

Explicit non-goals, to prevent scope creep:

- **Build / Simulate / Prove stages.** Both agents are Detect-scoped. Prove→Detect outcome-learning is a separate structural gap (flagged in strategic_next_steps, not covered here).
- **Multi-surface scaling.** Curator's conflict resolution generalizes, but Skeptic's pattern library today is HF CG. Cross-surface requires context.md per surface; out of scope for v0.1.
- **Automated experimentation.** Skeptic does not gate on experimentability. A card can pass Skeptic and still not be an experiment. Build stage problem.
- **Cost tracking.** Called out in §4.4 but not solved. Reflex lacks a cost model today; not adding one here.

---

## 7. Work-leo TODO (after reading the code)

This design is pre-code-read. Once inside work-leo with Pinterest code access, do these before writing the agent prompts:

### 7.1 Read these files and note deltas to this design
1. `services/reflex/detect/agents/pm_agent.md` (315 lines) — match voice, MCP conventions, Asana GID references, playbook-referencing style.
2. `services/reflex/detect/agents/ds_agent.md` (218 lines) — same.
3. `services/reflex/detect/quality_patterns.md` (341 lines, growing) — categorize existing patterns into the taxonomy in §1.5. Confirm categories cover all real patterns; extend if not. Note which patterns already have `applies_when` logic encoded informally.
4. `services/reflex/detect/schemas/opportunity_card.md` (139 lines) — map Skeptic's checks to specific schema fields. Produce field-level check list.
5. `services/reflex/detect/board_setup.md` (295 lines) — figure out how Skeptic annotations and Curator proposals surface in Asana. New section? New tag? New column?
6. `services/reflex/CLAUDE.md` and `services/reflex/detect/CLAUDE.md` — confirm no conflicts with proposed file placement.
7. `services/reflex/docs/reflex-vision-two-pager.md` and `anticipation-p13n-vision-2026.md` — confirm design aligns with stated vision; flag any drift.

### 7.2 Cross-reference
- `cg_quota_analysis.md` registry → seed Skeptic's context-check rules against the real CG map, including deprecated CGs.
- The `context.md` being drafted for Reflex (`~/reflex-context/context.md`) → Skeptic's context-check engine relies on this.

### 7.3 Decide (flag the decision back to Andrew + Dylan)
- Flat placement vs. `quality/` subdir (§5.5).
- Skeptic MCP access scope (§5.4).
- Whether Curator's proposed patterns go straight into `quality_patterns.md` as a "proposed" section, or live in a separate staging file.

### 7.4 Write the prompts
Following house style:
- `feedback_curator.md` — role, responsibilities, output formats (pattern entry, conflict report), interaction triggers, scope boundaries, failure modes.
- `skeptic.md` — role, responsibilities, output format, pass/fail semantics, scope boundaries, failure modes.

### 7.5 Validate before PR
- Dry-run Skeptic against 2–3 historical cards where we know the right call. Does it catch what James caught? Does it over-flag?
- Dry-run Curator against 2–3 past expert corrections. Does it produce well-formed pattern entries? Does it detect the conflicts we'd expect?

### 7.6 Documentation
- Short README in `services/reflex/detect/agents/` (or `quality/`) explaining the two roles, how they interact with PM / DS / human expert, and the handoff sequence from §3.
- Update `services/reflex/detect/CLAUDE.md` with pointers to the new agents.

### 7.7 PR description scaffold
Lead with the compounding-loop framing (mirrors the pre-share message). Include the handoff diagram (§3). Call out the 5 open design questions (§5) explicitly so reviewers know where to focus.

---

## 8. Success criteria for v0.1

- Skeptic catches ≥ 80% of cases where James would have flagged a deprecated-CG, holdout, or unverified-VLM issue on historical cards. (Measure against cycles 1–13 archive.)
- Curator produces well-formed pattern entries for 100% of James's Asana feedback in cycles 14+. Human merge rate ≥ 50% without major edits.
- Expert review time per card drops by ≥ 30% within 5 cycles of Skeptic activation.
- Zero autonomous pattern retirements or modifications in `quality_patterns.md`.
- Andrew's verdict: this extends the compounding loop rather than complicating it.
