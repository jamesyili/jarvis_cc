# The World Store and the LR Connector — Detect-stage memory, closing the Prove→Detect gap

Status: v1 proposition, 2026-08-20 — grilled against the domain model in-session (decisions ratified by James; see §2). Pre-circulation: for me first, then Andrew + Dylan (Detect homing), Janvi (Evolve contract), Chao (eval consumer).
Builds on: `feedback_curator_and_skeptic.md` (June Curator/Skeptic design) · `eval_05_verifiability_and_attempts_store.md` (attempts store + partition) · `eval_01_glossary.md` candidate object 8 · SkillOS / EvoRec / EvoHarness-RL / YouTube-paper evidence (`eval_06`).

---

## 0. One-paragraph summary

Reflex's environment has amnesia: a change can originate anywhere, nothing records what was tried or what the world currently is, so Detect re-proposes tried things, cites deprecated systems, and can't be measured against reality. This proposes a **connector** that ingests each quarter's launch-review docs per surface (crawl: Reflex → Helix → Glean MCP, orchestrated under Claude Code), looks up the implementing code, and writes two repositories: **Launch Records** (raw, append-only: hypothesis → intervention-as-code → movement → decision, full provenance) and the **World Store** (distilled, canonical current-world facts with supersession). The existing **Feedback Curator becomes the custodian of both** — one curation discipline, two repositories — which finally gives its decay-handling step a signal source. The first consumer is Detect's agents at card-writing time; the Skeptic's context/already-tried checks, the Curator's staleness flags, and Chao's precision-against-reality measurement follow on the same records. It homes in **Detect**, couples to Evolve only through a version-pinning contract, and is the Prove→Detect outcome-learning path the June design explicitly deferred.

---

## 1. The problem, in five concrete defects

1. **Detect can't know what was already tried.** A card proposing something launched (or killed) two quarters ago looks identical to a novel one. The Skeptic's novelty check (§2.3.5 of the June design) has no corpus to check against.
2. **The world model is hand-drafted and stale by construction.** The Skeptic's context-check engine "relies on `context.md`" — a manually maintained file of CG statuses, table names, and architecture facts. Nobody's job keeps it current.
3. **The Curator's decay handling has no trigger.** §1.3.3 says the Curator notices "the underlying system changed" and flags stale patterns — with no mechanism anywhere for how it would notice.
4. **The negative-results corpus is invisible.** LR docs record what worked (survivorship by construction). What ran and failed was never written up. The program's most valuable lookups don't exist as documents.
5. **Detect has no precision-against-reality.** Of the things Detect proposed, how many were tried? How many failed? Today a pursued-and-failed card is indistinguishable from an unread one (`eval_00` item 19).

One build addresses all five, because all five are the same missing thing: **a curated, time-indexed record of what the system is and what happened to attempts to change it.**

## 2. Decisions already ratified (8/20 grill)

These are settled; the rest of the doc builds on them.

| # | Decision | Rationale anchor |
|---|---|---|
| D1 | **Two stores, one Curator.** World knowledge and card-writing patterns are separate repositories; `quality_patterns.md` is untouched. The Curator custodians both with the same §1.3 machinery | facts and lessons age, retrieve, and compress differently; EvoHarness-RL types its stores (Belief ≠ Experience) and the separation is load-bearing in ablation |
| D2 | **Raw layer kept.** Launch Records are append-only, never compressed, never edited — the audit trail and the future attempts-store corpus | EvoRec's Memory/Skill-Evolver split; recoverability of every ingestion mistake |
| D3 | **Glean is the crawl layer, not a competitor.** Access path: Reflex orchestrates **Helix** (internal agent service) via protocol → Helix runs its **Glean MCP** → docs come back. Claude Code is the harness | don't rebuild discovery or permissions; differentiation is downstream of retrieval (§5) |
| D4 | **First consumer = Detect agents at card-writing time** (option c). Post-hoc already-tried annotation is redundant if the writer already knows; precision-against-reality is a fast-follow, not v0 | with one guardrail — the prior-art-engagement rule, §7.1 |
| D5 | **Homes in Detect; is the Prove→Detect bridge; is not Evolve.** Evolve touches it only through the versioned-world contract (§8) | preserves the policy/knowledge boundary; keeps it inside an existing stage's charter under consolidation pressure |

## 3. Canonical names

Fixed here so review comments can't mean two things (`eval_01` candidate object 8 carries the same vocabulary):

- **LR Connector** — the ingestion pipeline (Helix→Glean crawl, extraction, code join).
- **Launch Records** — the raw layer. One record per launch/experiment readout.
- **World Store** — the distilled layer. Current-world facts with supersession.
- Retire from use for this system: "knowledge base" (collides with `quality_patterns.md` institutional-memory language) and "attempts store" as the v0 name — the attempts store is what Launch Records **become** once the experiment-platform join lands (§6, phase 4). Until the failures are in, calling it that overclaims.

---

## 4. Architecture

### 4.1 The pipeline

```
LR docs (per surface, per quarter)          code (diffs/PRs/configs)
        │                                            │
        │  Reflex → Helix → Glean MCP (crawl)        │  repo lookup (join)
        ▼                                            ▼
   EXTRACTION (Claude Code harness, LLM-assisted, human-verified in v0)
        │
        ▼
 LAUNCH RECORDS — raw, append-only, full provenance          ← EvoRec's "Memory"
        │
        │  Curator distills, periodically (not per-event); human merges
        ▼
 WORLD STORE — canonical current facts, compressed, supersession  ← EvoHarness's "Belief"
        │
        ├─→ Detect agents at card-writing time (v0 consumer)
        ├─→ Skeptic: context-check + already-tried check (when built)
        ├─→ Curator: decay flags on quality_patterns.md entries      ← "Experience"
        └─→ Chao: precision-against-reality (fast-follow)
```

### 4.2 Launch Record schema (raw layer)

Extends `eval_05` §5.2; the specificity is the product — "tried X, didn't work" is nearly useless as a lookup.

- `record_id`, `ingested_at`, **`decision_date`** (the temporal index key — every read is filtered on this, §7.2)
- **Hypothesis** — what was believed, stated in the vocabulary a card would use
- **Intervention** — what was actually built: the diff / config / model change (links + extracted summary), not the prose summary. This is the code join, and it's the field no search index can produce
- **Locus** — surface, stage, model, ranking layer
- **Timeline** — proposed → launched → read-out → decision, with dates
- **Movement** — metric deltas with intervals and powering. An underpowered null is not a negative result, and the record must be able to say so
- **Decision + reason** — shipped / reverted / inconclusive / abandoned-before-readout
- **Mechanism of failure, where known** — the field that makes it a lookup instead of an archive ("effect real and negative" and "holdout couldn't resolve it" are opposite lookups; only one means don't retry)
- **Provenance** — LR doc link, PR/diff links, experiment IDs; `source: Literal["lr_doc", "experiment_platform", "manual"]`
- **Card linkage** — if a Detect card motivated this launch: card ID + contamination tag (calibration/lockbox-linked records are excluded from any agent-visible retrieval, same rule family as the Curator's pattern-extraction exclusions)
- `screening_status` — LR prose is untrusted content entering headless runs; screened at intake for instruction-shaped text (same policy as Evolve's fixture intake, `eval_03` §8)

Records are structured data, not markdown prose — the format-as-guard result (Anthropic): structurally inert fields can't be softened by any downstream process the way prose can.

### 4.3 World Store entry schema (distilled layer)

Deliberately mirrors the §1.5 pattern-entry format so the Curator's machinery transfers:

- Fact statement (one canonical sentence) · entity references (tables, CGs, models, surfaces) · `status: current | superseded` · `supersedes` / `superseded_by` · evidence → Launch Record IDs · last reaffirmed · applies-to surface

**Compression applies here and only here** (SkillOS's compression reward, `eval_04` §4.2 split): a fact should get shorter and more general as it's reaffirmed; the raw layer underneath it only grows. A distilled entry still lengthening at its third reaffirmation is being accreted, not curated.

### 4.4 Retrieval

Expose both layers to agents **via MCP** (everything is already MCP-shaped through Helix). Two dividends: Evolve's existing fixture-recording machinery captures store reads automatically, giving snapshot consistency nearly for free (§8); and retrieval becomes a designed interface rather than file-grep — which SkillOS says is where curation succeeds or fails (entries must match how the reading agents actually query; their frontier-model-as-curator underperformed a small trained one on exactly this mismatch).

---

## 5. Why this isn't Glean (the paragraph for the review room)

**Glean tells you which documents mention a thing. This tells you what's true about the system** — what exists, what was tried, what happened — as typed, time-indexed, curated records an agent can check a claim against. Four differences, then two concessions:

1. **Documents vs. typed records.** The query Reflex needs — "has this hypothesis been tried on this surface, what moved, and was the null powered?" — isn't answered by any single document; it's assembled across the LR doc, the code, and the readout. The join is the product, and an indexer doesn't join.
2. **It contains things no document says.** The gap between the experiment platform (everything that ran) and LR docs (what worked) is the negative-results corpus. It doesn't exist as documents; Glean structurally cannot have it; the connector manufactures it (phase 4).
3. **Curation vs. crawling.** Glean's freshness is re-crawl. The World Store has supersession: a Q3 launch replacing X fires decay flags on every pattern citing X. An index never tells you a document is now false.
4. **Eval-grade constraints.** Time-travel reads for hindsight measurement, contamination tags, already-tried-annotates-never-rejects, deterministic existence lookups for the Skeptic. Search has no concept of leakage.

Concessions: Glean **is** the crawl layer (D3) — discovery and permissions are solved problems we inherit through Helix; and v0 extraction is literally retrieval-augmented (search finds the doc, the connector extracts the record). Differentiation is everything downstream of retrieval.

---

## 6. Sequencing — phases with gates

**Phase 0 — verify at work (one session).** Confirm the Helix protocol + Glean MCP can reach LR docs; pull the LR doc inventory per candidate surface; run the slice query from `eval_05` §7.5 — experiment volume by surface/stage where each experiment ties to an identifiable hypothesis. **Slice criteria in order: attribution cleanliness (card→change→experiment is one line — non-negotiable) · already instrumented · historical density · latency; business impact and org convenience are tiebreaks only.** Gate: one surface + one quarter with ≥~15 accessible LR docs and clean attribution.
**Phase 1 — the spike (~1–2 weeks, part-time).** Connector v0: ingest that quarter, extract Launch Records (LLM-assisted, every record human-verified), measure **effort-per-record** — the number that decides whether wider scope is a proposal or a fantasy. Hand-distill the first ~10–20 World Store facts against the known history of that surface. Gate: records answer real queries I can check from memory; effort-per-record supports scaling.
**Phase 2 — first consumer (option c).** Store exposed via MCP; playbook adds retrieval + the prior-art-engagement rule (§7.1); run one cycle store-enabled vs. incumbent on the same surface. Gate: §9's v0 metrics move.
**Phase 3 — Curator formalization.** Distillation as a periodic Curator operation (proposed → human-merged, logged **proposed-vs-merged separately** per `eval_04` §4.1); demonstrate one real decay event end-to-end: LR ingest → supersession → staleness flag on a `quality_patterns.md` entry → human confirmation.
**Phase 4 — hand-offs.** Experiment-platform (Helium) join scoped with the data/infra lane (this is where Launch Records become the attempts store); precision-against-reality delivered to Chao as the non-confounded version of his Phase 3; `world_store_version` lands in the EvalResult v2 PR with Janvi; production ownership decision with Andrew.

Phase 0–1 is me. Phase 4 is deliberately other people (§10).

---

## 7. Design invariants (non-negotiable, stated up front)

**7.1 Prior art annotates — the agent engages it, never silently obeys it.** Generation-time consumption (D4) makes the conformity hazard invisible: the agent can self-censor ideas the store says failed, and nobody sees what was never proposed. Rule: the playbook requires cards touching known prior art to **engage it in the card** — "tried 2026-Q1, flat, but underpowered / world has changed since." Suppression becomes reviewable prose. A prior failure is a reason to look harder or check powering, never a veto — or this system re-creates the conformity problem Reflex exists to break.
**7.2 Temporal indexing from day one.** Every read is anchored: a run anchored at T retrieves only records with `decision_date < T`. Without this, any hindsight measurement (Record of System Launches, glossary object 7) silently corrupts — numbers just quietly improve, undetectably. Design-time trivial, forensically impossible later.
**7.3 Survivorship is named, not hidden.** Until phase 4, this corpus is the numerator (what worked). Every consumer and every metric readout carries that caveat; the Helium join is scoped in the proposal precisely so "phase 1 = LR docs only" reads as staging, not blindness.
**7.4 Contamination fencing.** Records linked to calibration/lockbox cards are tagged and excluded from agent-visible retrieval. The store is a new channel folding information back into the agents; every such channel gets explicitly fed or fenced (standing doctrine, `eval_00` §9).
**7.5 Nobody optimizes on it.** Like objects 4 and 7: read by agents, measured against by evals, tuned on by nothing.

## 8. The Evolve contract (the entire ask to Janvi)

The store is world, and Evolve requires the world pinned. Four rules — one field, one schedule, one boundary, one fence:

1. **`world_store_version` in EvalResult v2 / fixture provenance.** Snapshotted store; an Evolve run pins one version, same discipline as `judge_version` and `fixture_snapshot_id` (third instance of the same principle). I already own this PR; it's one more field.
2. **Ingests land between runs, never mid-run; a store bump = re-baseline.** The incumbent pre-flight canary (`eval_03` §6) now also catches store drift for free.
3. **Mutation boundary: Evolve owns policy, Curator owns knowledge.** Evolve may mutate how a playbook *queries* the store — including improving the §7.1 engagement instruction; that's spec text. It never mutates store content. The Curator never touches playbooks (§1.4 of the June design already says so). SkillOS's frozen-executor/curator split, applied at the seam.
4. **Store content is data, never instructions** — screened at intake (§4.2), same as fixture policy.

Net effect on Evolve is positive: grounded agents mean the judge scores strategy, not hallucination noise.

## 9. Measurement — how we'll know it's working

**v0 (phase 2 gate), one cycle, store-enabled vs. incumbent on the same surface:**
- **Prior-art engagement rate** — fraction of cards touching known prior art that cite and engage it (target: high; the demo moment is the first live card that would have re-proposed a known failure and instead engages it)
- **Reference-error rate** — cards citing deprecated/nonexistent systems, before vs. after (the store is what makes the claim checkable at all)
- **PM verdicts** on the cycle's cards — the human-signal readout
- Effort-per-record from phase 1 — the scaling economics, reported not spun

**Store health (ongoing — SkillOS's four, applied per store):** coverage (fraction of entries ever retrieved — if ~50%, half the store has never helped anything), usage rate per card, successful-usage rate, entries-retrieved-per-card (**down over time is good** — precision, not volume; a growing store with rising retrieval counts is the signature of an immature system, per SkillOS + EvoHarness annealing, two labs, same shape).
**Explicitly not claimed:** business metrics. Funnel/launch counts stay program KPIs (`eval_00` item 10). The eval-grade number this eventually unlocks — Detect's precision against reality — ships to Chao in phase 4, not as a v0 promise.

## 10. Ownership and the org seam

- **Me:** the connector + spike (phases 0–2), the schemas, the invariants, the Evolve contract field. This is the capability-building shape of my Eval & Evolution thread — and it is deliberately a **spike with hand-offs**, not a quarter-scale data project on my plate.
- **Andrew (first-week conversation, not a discovery):** Detect homing; the Curator-custodian formalization (Curator ownership has been flagged for Andrew + Dylan since 8/15, unresolved — this forces the resolution productively); the playbook change is his surface.
- **Janvi:** §8 — one field, one scheduling rule, rides the existing seam conversation (Stage-2 collapse + the `blame()` questions).
- **Chao:** precision-against-reality as the non-confounded version of his own Phase 3 metric — offered, not imposed.
- **Data/infra lane (Gideon):** the Helium join at phase 4 — the expensive half, and the same join as the hindsight case bank (`eval_00` §7). **One join, two consumers, named in the ask** — or two people build one pipeline under two names and find out in October.
- **Dylan narrative:** "built the memory layer that made Detect stop repeating itself and made its output measurable against reality" — capability with a succession shape (custodianship lands in Detect; JJ is a natural inheritor), never "James's knowledge base."

## 11. Risks

| Risk | Mitigation |
|---|---|
| Hallucination vs. novelty look identical (both cite something not in the record) | the check distinguishes assertions about the present (defect) from proposals about the future (the point); in the design from day one |
| Conformity via generation-time suppression | §7.1 — engagement is mandatory and visible |
| Extraction quality (LLM misreads an LR doc; a wrong record poisons downstream) | v0 = human-verified per record; raw layer append-only so any error is correctable by supersession, never silent edit |
| Effort-per-record too high to scale | phase 1 measures it before anything wider is proposed; the gate is explicit |
| Filters/knowledge never audited by the people they save work for | periodic human sample of what the store influenced — mirror image of the blind audit on judge-top-scored cards (`eval_02` rule 3) |
| Scope-creep rejection ("this is a data platform pitch") | phased gates, spike-first, hand-offs named, Glean/Helix reused, business metrics unclaimed |
| Cross-surface transfer assumed cheap | it isn't (AutoHarness: per-game harnesses; transfer unsolved at DeepMind). What transfers is the playbook — slice selection, schema, verification — not the artifact. Slice two is budgeted as real work |

## 12. Open questions (phase 0 answers most)

1. Helix protocol mechanics — auth, rate, what the Glean MCP exposes for LR docs; whether code repos are reachable through the same path or need a second lookup.
2. Can the experiment platform be joined to Reflex cards at all, or only to LR docs? (If only LR docs, the phase-4 attempts store inherits positive bias and loses most of its value — worth knowing early.)
3. Which surface wins the §7.5 slice query.
4. Current state of `~/reflex-context/context.md` — how much hand-drafted content the World Store inherits vs. replaces.
5. Card schema: does prior-art engagement need a dedicated card section (Andrew's surface)?

## 13. Evidence base — what each source contributed

| Source | Contribution to this design |
|---|---|
| **SkillOS** (Google Cloud AI/UIUC/MIT) | curator = operations policy, judged by consumption; compression on distilled only; the four health metrics; don't fix curation by upgrading the model — match writer to reader |
| **EvoRec** (Alibaba, production +1.85% revenue) | raw Memory / periodic distillation split (D2); the funding citation that methodology-from-past-experiments pays |
| **EvoHarness-RL** (Meta AI/UIUC) | typed stores (Belief ≠ Experience → D1); maturity = fewer, more selective reads |
| **YouTube self-evolving recsys** (Google, production) | the Slow Loop — outcomes feeding discovery — is the missing half of a two-loop system; this is Reflex's |
| **AutoHarness** (DeepMind) | take the verifiable part away from judgment; deterministic lookups need authoritative records; per-slice builds, transfer is unsolved |
| **AI2/UW counterweight** | matched comparisons before crediting anything; "memorize fixes vs. distill strategies" is the failure compression pressure exists to prevent |
| **Anthropic harness post** | format-as-guard: structured records over prose (§4.2) |
| **June Curator/Skeptic design (mine)** | the custodian machinery reused wholesale (§1.3, §1.5, §1.6); decay handling finally gets its trigger; the Skeptic checks this store makes buildable |
| **eval_05 (mine)** | record schema, survivorship structure, temporal leakage rule, annotate-never-reject, slice criteria, one-join-two-consumers |

Beyond the literature in one place, worth saying out loud: **none of these papers handle cross-store decay** — a world that deprecates its own knowledge. SkillOS has no deprecation concept; EvoHarness resets Belief per task. The supersession→staleness-flag link (§4.3 + phase 3) is past the published state of the art, and it exists because the June design already had lineage and decay waiting for a signal.

## 14. Related

`eval_00_hub.md` (state; items 19, §7 — the same join) · `eval_01_glossary.md` (candidate object 8 — canonical vocabulary) · `eval_05` (the strategy this executes the corpus half of) · `feedback_curator_and_skeptic.md` (the custodian machinery + the Skeptic consumers) · `eval_03` §6/§8 (canary, fixture intake policy) · `eval_06` (paper details)
