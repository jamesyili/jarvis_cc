# What the memory literature says about the Curator and the Skeptic — twelve papers against the design as built

**Status:** working synthesis, 2026-08-28 · **Author:** James Li · **For:** me first; then Andrew (Detect / Skeptic / DS Agent), whoever owns the Curator (Andrew + Dylan, still unresolved), Janvi (one Evolve item), Chao (the measurements) · **Ground truth:** `feedback_curator_skeptic_deepdive_0828.md` (the prompts and schemas as of 8/28) · **Evidence:** `eval_06` entries 3, 5, 7 (SkillOS, EvoHarness-RL, EvoRec) and 9–12 (Recuris, WikiSkill, Scroll, Perplexity Brain); full text in `kb/hard/raw/`

**Circulation note:** §1–§5 are safe to share. §6 (ownership) and §7 (what I'd do first) are mine.

---

## 0. If you read one thing

Reflex's memory layer has a **write side** and a **read side**. The write side is the Curator: capture every expert comment verbatim with provenance, classify it, relate it to what's already known (Strengthen / Contradict / Narrow / Orthogonal), refuse to merge contradictions silently, refuse to retire silently, split auto-apply from proposal by blast radius. Against the twelve papers, that side is **ahead of the literature** — WikiSkill's wiki is never pruned and its `replace` silently overwrites; Recuris's store went 51 added / 2 revised / 0 deprecated with 17 near-duplicates admitted; Brain doesn't describe conflict handling at all.

The read side is where the store enters an agent's context, keyed on what, and whether the agent doing the work carries any state of its own. **Every large number in the new set is on the read side, and Reflex has barely built it:**

| Paper | Measurement | Number |
|---|---|---|
| Recuris (Table 2) | verified per-goal working state, no skills | **+23.9†** over base |
| Recuris (Table 2) | skills, no working state | +2.0, CI includes zero |
| Recuris (Table 2) | same ten skills, all in context, model decides what applies | **65.6 vs 83.6** state-keyed — and below the 82.0 of *no skills at all*, at +46% tokens per success |
| Scroll (Table 3) | tool results compacted into summaries, 128K → 256K | **−21.4** |
| Scroll (Table 3) | tool results bound to variables, same backbone | −2.6 |
| WikiSkill (Table 3) | executor walled off from the wiki vs given access | **63.7 vs 60.9** |
| EvoHarness-RL | removing the Progress store | "disproportionately degrades long-horizon tasks with dependent subgoals" |

Mapped onto Reflex: the DS Agent runs a long-horizon investigation (hypothesis → surface → Presto pull → cross-verify → decide) with **no working-state ledger**; the Skeptic reads `registry.yaml` + `dead_ends.yaml` + `quality_patterns.md` + audit logs and **decides for itself what applies** — the model-controlled row; and the verdict log localizes failures to the card, never to the memory component that failed, which is the condition under which Recuris measures attribution at **13%**.

So the leverage is not in the Curator's next feature. It is in giving the investigation a state ledger, keying the Skeptic's retrieval, and making the logs say *which component* was wrong. All three are prompt-and-schema changes, all three are measurable on logs that already exist, and none of them weaken the human gate.

---

## 1. Where the design is already ahead (calibration, not flattery)

Stated first so §2 reads as additions rather than a rewrite.

| Design property (deep-dive) | Nearest paper | Gap in the paper |
|---|---|---|
| Conflict Report — Merge / Version / Replace, routed to the original reviewer, never silent | WikiSkill `update_patterns` with `replace` | `replace` silently overwrites; no conflict concept |
| Never silently retire; retirement always human | Recuris, WikiSkill | 51/2/0 add/revise/deprecate; "no automated mechanism to prune the wiki" listed as a limitation |
| `rationale_verbatim` + `source_ref` + `confirmed_by` with dates | Brain (per-entry provenance), WikiSkill (per-iteration evidence pointers) | equivalent — this is the one place the papers match |
| `no_durable_learning` close — allowed to conclude nothing was learned | Recuris Meta-Agent attributing a cluster to "the harness itself" and proposing no patch | equivalent |
| Blast-radius split: strengthen autonomously, create / retire / broaden with a human | none | no paper distinguishes operations by risk |
| Verdict log on PASS as well as FAIL; validated writer refuses malformed records | Recuris structured trace | Recuris logs mechanism events (which skill was invoked, which goal committed); the verdict log doesn't — see §2.3 |
| `revision_round ≤ 2` enforced in the schema | — | — |

Two of the papers also soften a claim I've been carrying. `eval_04` says, from SkillOS, that untrained curators append and trained ones consolidate. WikiSkill's *untrained* maintainer went edit-dominant (7.0–18.4 edits vs 6.3–8.9 creates per run) from a prompt rule — "do NOT create duplicate patterns, update existing ones" — plus full-wiki context before every edit. The Curator has both. So the accretion risk in `eval_04` §4.1 is real but it comes from the *approval-cost asymmetry*, not from the Curator's own operation mix. The proposed-vs-merged measurement stays the right first move.

---

## 2. Five findings

Each one: the evidence, what it maps to in the design as built, the change, and the measurement that would confirm or kill it — on existing logs where possible.

### 2.1 The investigation has no Progress ledger, and that is the largest number in the set

**Evidence.** Recuris isolates it cleanly: a per-goal working memory (`content / status / evidence / blocker`) where a goal is `done` only when a checker reads the tool receipt — not the model's claim — is worth +23.9 on τ²-Retail with *no skills at all*. Skills without it are worth +2.0. The mechanism is specific: read-action recall is 88–98% at every horizon, so length never breaks retrieval; it breaks *execution* — the base agent ends 42% of write-requiring episodes having issued no write, versus 16% with the ledger. EvoHarness-RL's ablation says the same from the other direction: removing Progress hurts most on long-horizon tasks with dependent subgoals. Scroll gives the cheapest form — a per-step headline (task, verified state, next action, status) bound to an address.

**In Reflex.** Hub open item 14 asked whether Detect maintains anything like Belief or Progress. On the deep-dive: `quality_patterns.md` + `analytical_checks/` + `dead_ends.yaml` are Experience; `context.md` is a hand-maintained Belief (a summary, not provenance-carrying — Scroll's ablation says summaries go to near zero on exact values, which is the wrong-column and topline-guess class of dead end); and **Progress is absent.** `cycle_log.jsonl`'s `phases_attempted / completed / failed` is a post-hoc phase ledger the Curator writes for the auditor; the DS Agent never reads it back mid-investigation. The Skeptic's Check 3 (evidence present?) is a checker — but it runs *after* the card is written, on the card's claim.

The analogue of Recuris's "omitted write" is a card that claims a VLM check, a chart, or a query it never ran. Check 3 catches that after the fact. A ledger catches it before the card exists.

**Change.** Give the DS Agent a per-investigation ledger of `(goal, status ∈ {pending, done, blocked}, evidence, blocker)` where `done` requires a receipt — a query result, a VLM output, a dashboard link — not a sentence. Check 3 becomes the checker that reads receipts instead of prose. Structured, not markdown, for the format-as-guard reason (`eval_06` #2). This is the Progress half of the BPE mapping; the World Store (`eval_07`) is the Belief half; the two together complete the harness-state picture EvoHarness-RL types.

**Measurement, on existing logs.** The fraction of `fail_reasons` in `verdict_log.jsonl` that are *claimed-but-not-executed evidence* — a check the card asserts and cannot show. If that fraction is large, the ledger's expected value is the Recuris number; if small, this is a nice-to-have. One afternoon, no new runs.

### 2.2 The Skeptic reads the whole store and decides what applies — the regime measured as worse than nothing

**Evidence.** Recuris's model-controlled row: byte-identical skills, all in context every turn, the model decides when to use them — 65.6% at 147k tokens per success, versus 83.6% at 101k when a working-state predicate decides which skill enters context, and versus 82.0% with *no skills*. "What the model-controlled regime lacks is a signal for *when* a skill applies." WikiSkill's ablation is the same shape from the executor side: the inference agent given wiki access did worse (60.9 vs 63.7), hypothesis being that it solved from the wiki instead of the skill and the traces stopped showing what was missing.

**In Reflex.** The Skeptic prompt tells it to read the registry, the dead ends, `quality_patterns.md`, and the Curator's audit logs, and then judge — "if your review has zero Check 6 findings, ask whether you read the Cycle Learnings." That is model-decided invocation over a wholesale read. The pieces of a keyed read already exist: `registry.yaml` entries carry `mandatory_when` and `applies_to` (proto-trigger predicates); Check 3's card-type classification is a retrieval key nobody uses for retrieval; cards name tables, surfaces, and a layer.

**Change.** Key Check 6 retrieval on `(card_type, layer targeted, tables named, surfaces)` against `applies_to` / `mandatory_when` / entity references, and **log what was retrieved** per verdict. The Skeptic still reads whatever it retrieves in full; what changes is that the store's own metadata decides the candidate set rather than the model scanning everything. Also: if the DS Agent reads `dead_ends.yaml` directly while authoring (a code check — the deep-dive doesn't say), log which patterns it consulted per card, so Evolve can tell "the playbook knew this" from "the wiki rescued it." Don't cut the DS Agent off; Detect needs the table-name landmines.

**What this does not license.** Trimming the Curator's Phase 0 read-everything. That is a different loop — the cross-task Meta-Agent read, and Recuris's Meta-Agent also reads every failed trace. Phase 0 has its own failure mode, though, and Scroll names it: under a context budget, "read everything" degrades silently into head-and-tail sampling (Appendix D.4 — session coverage complete, mid-session evidence skipped). Phase 0 should be a *program* over `expert_judgments.jsonl` — group by `claim_targeted`, expert, category, with the counts printed — not a load of Asana prose. Cheap check: does a Phase 0 synthesis cite only early and late comments?

**Measurement.** Skeptic precision (`human_agreed` on FAILs) and false-negative rate (humans rejecting PASSed cards) under wholesale read vs keyed read, on `verdict_log.jsonl`. Prerequisite: check the `human_agreed` backfill rate first — if it's mostly `null`, the log can't score anything yet and that's the finding.

### 2.3 The verdict log localizes to the card, never to the component

**Evidence.** Recuris Table 4: attributing a failure to the responsible memory component from the outcome alone is 13.0% (below the 33% constant-answer floor); from the raw trajectory 37.0%; from a structured trace that logs mechanism events 64.8%. Invocation faults — the pattern existed but wasn't pulled in — are *invisible* without mechanism events: 0% from either non-trace condition. And two Meta-Agents sharing no code converged on the same repairs from the same trace (−1.45 paired, p=0.72): what the loop learns is set by the evidence pool, not the intelligence reading it.

**In Reflex.** When a human overrides a FAIL or rejects a PASS, `verdict_log.jsonl` records that the card was wrong. Nothing says *which* of these failed: the pattern was absent (Curator should insert); present but not retrieved (retrieval); retrieved and misapplied (pattern content or check prompt); or the card's evidence state was wrong (the §2.1 ledger). That is outcome-only attribution, and a human reading Asana comments won't beat 13% either. `eval_04` §3 asked for a Curator attribution metric and had none.

**Change.** Three fields on `SkepticVerdict`, all cheap: `card_type` (the classification Check 3 already makes — it sets every downstream severity, and Scroll D.3 shows outcomes fixed by framing before any retrieval ran; without it a wrong-axis review is indistinguishable from a right-axis miss); `patterns_applicable` beside the existing `patterns_cited` (the keyed-retrieval candidate set from §2.2); and `disconfirm_queries: list[str]` — Scroll D.2: successful trajectories issue a disconfirming, address-bounded query before submitting, failed ones never do; "ask whether you read the Cycle Learnings" is that rule as prose. With those three, the human-override backfill can derive `component_blamed` mechanically: absent → insert; applicable-not-cited → retrieval; cited-and-wrong → content. **That turns the Curator's insert / update / retire choice into an evidence-driven decision** instead of a judgment call per comment.

**Measurement.** After one cycle with the fields: the distribution of `component_blamed`. If it's mostly "absent," the Curator's insert bias is correct. If it's mostly "applicable-not-cited," the store is fine and §2.2 is the whole problem.

### 2.4 Evolve has no rejection ledger; the gate needs an A/A run before it needs anything else

**Evidence.** WikiSkill's mechanism for not re-proposing failures is `skill-impact.md`: a **harness-written** append after every validation run — target, unified diff, validation score, accepted/rejected — that the proposer *must* read, with rejected proposals' full content. Their case study shows a rejected abstract skill informing an accepted concrete one one iteration later. On the gate: Recuris's 12-case dev slice at K=4 gave intervals over 30 points wide, rejected all 18 candidates (every dev CI contained zero), and one of those later cleared an 86-task held-out by +11.92†; the A/A re-run of a byte-identical package spans ±7 points. Their read: the gate discards noise, not gains — and a correctly sized gate rejects most candidates in-round.

**In Reflex.** `quality/proposed/` and the Curator's audit logs cover Curator proposals. Nothing covers Evolve's playbook edits — a rejected mutation leaves no trace the next proposer reads. And the paired-bootstrap gate in `eval_03` §2 has a sizing problem I under-called: Evolve's 450-invocation budget buys roughly the dev slice that couldn't resolve a +12-point effect.

**Change.** For Janvi, as an `eval_03` addendum: (a) a harness-written ledger of every playbook edit proposed — target, diff, fitness under pinned `judge_version` + `fixture_snapshot_id`, accepted/rejected, with the proposer required to read it; this is EvalResult v2's provenance written out as a file the loop reads back, one programmatic append. (b) Run the A/A first — the incumbent against itself, twice, on the fixture — and report the interval; that is paper #2's "pre-flight the incumbent" with a number attached. (c) Reserve a pre-registered held-out fixture (~80+ cases) with anchor cases the incumbent already passes as the regression term, and expect most candidates to be rejected in-round.

### 2.5 What the store should look like — six small properties, all from the papers, none in tension with the design

- **Raw layer first, derived view second, and the consumer can expand the address.** Scroll's thesis is that the derived view must never be the *sole* representation — its 30–55 point lead on contradiction resolution comes from materializing both sides in order with provenance. `expert_judgments.jsonl` is the event log; `dead_ends.yaml` and the registry are the derived view; the order is already right. The gap is the consumer: a Skeptic flag citing "Dylan Wang, Cycle 49/57" is a headline, and the Skeptic reads audit logs but not judgment records. Let it expand the address.
- **One-line index entries stating problem + root cause + fix.** WikiSkill's prompt calls the index "the MOST IMPORTANT part of the wiki" because it decides whether a page gets read. `de_topline_guess_without_constituent_numbers`'s label carries only the problem. Give each dead end and check a `summary` line in that form; it's what keyed retrieval (§2.2) will match on.
- **Back-pointers from routed rules to the learning that motivated them.** WikiSkill's `PURPOSE.md` maps each skill to its wiki patterns. The Curator routes to `playbook_rule` and `agent_prompt_rule` with no `motivated_by: [learning_record ids]` — so when a contradiction later supersedes a learning record, the rules it spawned aren't findable.
- **Tag entries by kind: domain fact vs model workaround.** WikiSkill Table 2: a small model's skills encoding low-level workarounds dropped Gemini-Flash from 50.5 to 18.1; domain procedures transferred and sometimes beat self-evolved ones. Recuris transferred a memory evolved on a mid-size model to Opus 5 for +15.6†. `dead_ends.yaml` mixes both — `search_feedview_country_case` is a fact about Pinterest's tables; a formatting quirk of the current Claude is not. One field, and the next model bump has a retirement list instead of a mystery regression.
- **Scoped negatives.** Brain encodes corrections as "avoid this route *in this context*"; `applies_to` already does this. It argues against any dead end or check without a context clause.
- **Two write cadences.** Brain updates pages incrementally per session and consolidates overnight; WikiSkill runs one maintainer call per iteration over ≤8 stratified traces; SkillOS's trained curator and EvoHarness-RL's annealed policy both end up touching memory *less*. The Curator's per-comment trigger plus a full Phase 0 re-read is the expensive version of the same idea. A scheduled consolidation pass with cheap incremental capture between passes is what four systems converge on. Related: WikiSkill harvests *success* patterns from passing traces to prevent regressions; Reflex's capture is correction-skewed — `approve` and `asana_action` judgments carry no words — so "what did approved cards do that failed ones didn't" is an absent Curator category.

---

## 3. The "growing patterns file = immature system" position, revisited

It survives, and Recuris says *why* it holds for Reflex and not for them. Their store went 51 / 2 / 0 with 17 near-duplicates and still gained — "redundant rather than fragile" — because invocation was gated and bloat never reached the context; ablating skills moved held-out by −2.3 to +1.7, intervals including zero. Reflex's wholesale read (§2.2) means every accreted line reaches the Skeptic. So the position is conditional: **a growing file is the signature of an immature system when the consumer reads it wholesale.** Fix the read side and growth becomes cheap; leave it and `eval_04`'s growth curve stays a leading indicator.

Add to `eval_04` §3.1: the create:edit ratio per cycle as the free companion metric, with WikiSkill Table 4 (edits exceed creates for every model, 0.8–2.8×) as the reference range for an untrained maintainer with full-store context.

---

## 4. What none of this licenses

- **No RL, no finetuning.** Unchanged from `eval_04` §5 and `eval_00`'s sequencing argument. Recuris's whole gain is prompt-time evolution with a frozen model; Scroll is one system prompt; WikiSkill is prompt-time. The literature keeps saying structure first.
- **Not dropping the human gate.** WikiSkill's unpruned wiki is its own listed debt; Recuris's 0-deprecate store worked only under gated invocation. Neither is evidence against the never-silent-retire rule.
- **Not cutting the DS Agent off from `dead_ends.yaml`.** WikiSkill's ablation is about what *traces* reveal to an optimizer, not about card quality; the fix is logging consultation, not removing access.
- **Not Brain's numbers.** +25% on repeated tasks, self-reported, unbaselined. Cite Brain's design choices only.
- **Not learning between retries within a task.** Recuris at matched budget: +2.3, p=0.774; the headline +26.4 was the retry budget. Same shape as the AI2/UW result — the 2-round `revision_round` cap is a retry budget, and the DS↔Skeptic loop should be evaluated as one.
- **Not anything about discovery quality.** Every number here is scored against ground truth — legal moves, exact values, task success. The verifiable-signal position (`eval_00` §9) stands: none of this runs without a critic you trust, and Reflex's critic is still uncalibrated. These changes are cheap *because* they're structural and measurable on logs; they are not a substitute for the eval-integrity layer.

---

## 5. Sources, one line each

| # | Paper | The number this doc leans on |
|---|---|---|
| 3 | SkillOS | coverage 53.6 → 72.9%; patterns-per-example 2.24 → 1.95; frontier-as-curator underperformed a trained 8B |
| 5 | EvoHarness-RL | BPE; Progress ablation degrades dependent-subgoal tasks; annealing to ~1 call/episode |
| 7 | EvoRec | Skill Evolver → +1.85% revenue: curation is a first-class component |
| 9 | Recuris | WM-only +23.9† vs EM-only +2.0; model-controlled 65.6 vs 83.6; attribution 13.0 → 64.8%; 12-case dev ±30 points; A/A ±7 |
| 10 | WikiSkill | proposer-reads-wiki 48.7 → 63.7; executor-walled-off 63.7 vs 60.9; harness-written rejection ledger; edits > creates untrained; negative transfer 50.5 → 18.1 |
| 11 | Scroll | compaction −21.4 vs binding −2.6 (Table 3, controlled); lossy summarization 19.9; headlines as Progress; D.2 / D.3 / D.4 failure annotations |
| 12 | Brain | per-entity pages, per-entry provenance, scoped corrections, two write cadences — and silence on curation |

---

## 6. Ownership (internal)

- §2.1 (ledger in the DS Agent), §2.2 (keyed Skeptic retrieval), §2.3 (schema fields) — **Detect, Andrew.** Prompt and Pydantic changes; no new infrastructure.
- §2.5 store properties — **whoever owns the Curator.** This is the first time the Curator-ownership conversation has concrete, small asks attached instead of "someone should own this." Use it that way.
- §2.4 — **Janvi**, as an `eval_03` addendum. One file, one A/A run, one held-out reservation.
- The measurements in §2.1–§2.3 — **me**, eval lane. All on `verdict_log.jsonl` and `expert_judgments.jsonl`; the first thing to check is the `human_agreed` backfill rate, because everything downstream depends on it.

## 7. What I'd do first (internal)

1. **Backfill rate.** What fraction of `verdict_log.jsonl` rows have `human_agreed` non-null. If low, that's the finding and the fix is process, not schema.
2. **Claimed-but-not-executed share** of `fail_reasons` (§2.1 measurement). Decides whether the ledger is the first build or the third.
3. **Schema PR** — `card_type`, `patterns_applicable`, `disconfirm_queries` on `SkepticVerdict`; `summary`, `kind`, `motivated_by` on registry and dead-end entries; `consulted_patterns` on the DS Agent's card output. Small, load-bearing, same class as EvalResult v2.
4. **Keyed retrieval** for Check 6, logged (§2.2), then the precision comparison.
5. **The Evolve ledger + A/A** to Janvi (§2.4).
6. **Progress ledger prototype** in the DS Agent prompt for one card type; measure (2) before and after.
7. **Phase 0 as a program** and a scheduled consolidation cadence — the Curator-owner conversation.

Items 1–2 are an afternoon each on existing files. Item 3 is a day. Nothing here needs a new run, a label, or a judge call.
