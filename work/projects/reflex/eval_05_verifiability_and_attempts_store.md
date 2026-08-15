# Making Reflex's failures verifiable — the partition, and the attempts store

**Mine, pre-circulation · 2026-08-15 · James Li**
**Provoked by:** AutoHarness (`kb/hard/raw/arxiv/autoharness-improving-llm-agents-by-automatically-synthesizing-a-code-harness.md`, Google DeepMind)

This is not a critique of anyone's doc. It's a strategy for the program, and it starts from one observation about why AutoHarness worked.

---

## 1. The idea

AutoHarness let Gemini-2.5-Flash beat Gemini-2.5-Pro — 56.3% vs 38.2% win rate across 16 two-player games, and in the code-as-policy limit case it beat GPT-5.2-High (0.870 vs 0.844) at roughly zero inference cost against ~$640. The motivating statistic was that **78% of Flash's chess losses were illegal moves, not strategic blunders.**

It's tempting to read that as "harness beats model size." The more useful reading is narrower:

> The harness didn't make chess verifiable — chess already was. What the harness did was **take the verifiable part away from the LLM entirely, at 100% accuracy, so the model only ever faced the part that needed judgment.** It didn't solve the hard problem. It shrank it.

That is a move Reflex can make, and it does not require the loop to be verifiable end to end. It requires **partitioning** card failures into the part a program can adjudicate and the part that genuinely needs a judge — and then never spending judgment, human attention, or optimizer budget on the first part again.

**Hallucinated references are Reflex's illegal moves.** A card citing a table, metric, or experiment that does not exist is checkable with a catalog lookup and zero judgment.

---

## 2. The taxonomy — a start, not a finish

Five failure modes, sorted by what it would take to make each a mechanical true/false. The first column is the failure; the last column is the honest cost of mechanizing it.

| # | Failure mode | Verifiable? | By what | What it would take |
|---|---|---|---|---|
| 1 | **Hallucinated reference** — cites a table, metric, component, or experiment that doesn't exist | **Fully, today** | catalog / schema lookup | wiring to the existing catalogs. Cheapest item here. |
| 2 | **Already tried** — a genuine result, but it was attempted before and the outcome was never logged | **Yes, if the log exists** | retrieval against an attempts corpus | **the corpus doesn't exist — see §5** |
| 3 | **Too small** — real, but the magnitude doesn't justify verification effort | **Yes, if the card asserts magnitude** | threshold on declared fields | a card-schema change: cards must state estimated effect and effort |
| 4 | **Not worthwhile given the metrics** — genuine, correctly sized, and still not worth doing | **No** | irreducible judgment about priorities | this is what the judge and the humans are *for* |
| 5 | **Unsupported causal claim** — the finding may be real but the stated mechanism isn't evidenced | **Partially** | check whether cited evidence supports the claim | LLM-assisted; not mechanical, but far more constrained than open-ended scoring |

Modes 1–3 came out of working through this on 8/15; 5 is a carryover from the earlier failure-type sketch. **This taxonomy is a starting hypothesis and should be replaced by one derived from real labeled failures** (§4).

### Two things the table makes visible

**Mode 2 is not a harness problem.** AutoHarness's environment always knew whether a move was legal. Reflex's environment has amnesia. That's an *instrumentation* defect, not an agent defect, and no amount of harness synthesis fixes it. It should be argued for separately — and it's the easiest of these to argue, because "we don't record what happened to things we tried" is indefensible on its face.

**Mode 4 is where the judge earns its keep.** Everything above it is currently consuming judge calls, human review, and optimizer budget that it does not deserve.

---

## 3. What the partition buys

1. **The judgment surface shrinks.** Cards disqualified on mechanical grounds never reach a judge or a human.
2. **The κ measurement gets cleaner.** Some of the human–human disagreement Lesson 11 is about to measure will be on cards that are mechanically disqualifiable. Strip those first and the remaining disagreement is *purer judgment* — which is the number that actually tells you whether you have a judge problem or a criteria problem.
3. **The "why" gets partitioned too.** AutoHarness's refiner reads *error messages from the environment*, not rationales. For verifiable failures the explanation is free and exact — "table `x` not in schema `y`." For judgment failures it's a human rationale, and those carry a measured >90% verbosity bias. **Half the diagnosis can be generated deterministically; only the other half has to be read out of prose.**
4. **`blame()` becomes a lookup table for the mechanized share.** AutoHarness assigns credit from the *error signature*: if `is_legal_action()` returned True but the action was invalid, refine both functions; if it returned False, refine only `propose_action()`. Deterministic, immune to rationale bias. For modes 1–3 the same is available: failure type implies component. Modes 4–5 stay in the noisy path — but over a much smaller share, and you know exactly which share.

---

## 4. Measurement zero — the ratio that gates all of this

**Classify the rejected cards you already have into the taxonomy above, plus "other."** No new labels, no new runs, no judge changes.

The output is one number: **the fraction of Reflex's failures that are mechanically adjudicable.**

- In chess it was 78%, and that's why AutoHarness worked.
- If Reflex's is high, this is the highest-leverage work in the program.
- If it's ~10%, this is a sideshow, the judgment problem dominates, and the effort belongs in rubric design instead.

Nobody has measured this. It is an afternoon of work and it decides whether §5 below is worth building. **Do this before anything else in this document.**

---

## 5. The attempts store

Mode 2 is the only entry in the taxonomy whose fix requires a corpus that doesn't exist. It's also the one with the most upside, because the corpus is useful far beyond failure classification.

**What it is:** a store of things that were tried, what specifically was tried, and what happened — with enough specificity to be looked up rather than merely browsed.

### 5.1 The two sources have opposite biases, and that's the point

| Source | What it contains | Its bias |
|---|---|---|
| **LR (launch request) docs** across surfaces | Engineer-proposed changes, accepted or rejected, most reaching production | **Survivorship toward positives.** People write an LR when they have a result worth launching. This is the record of *what worked*. |
| **The experiment platform (Helium), joined to Reflex** | Every experiment that ran, read out against the metrics matrix, whether or not anyone wrote it up | **The full distribution, including failures.** |

LR docs are the numerator; the experiment platform is the denominator. **The gap between them — experiments that ran and never became an LR doc — is, almost by definition, the negative-results corpus nobody wrote down.** That gap is the highest-value content in the store and it is currently invisible.

This is the third appearance of the same survivorship structure in this program: the recall gold set measures redundancy because PM roadmaps only contain what humans found (§B.5); hindsight recall covers only what was eventually investigated (Lesson 12); and now the written record covers only what worked. The attempts store is the first thing that would actually break the pattern, because the experiment platform holds attempts nobody chose to write about.

### 5.2 The record schema

"Tried X, didn't work" is nearly useless as a lookup. The specificity is the product:

- **Hypothesis** — what was believed, stated in the vocabulary a card would use
- **Intervention** — what was actually built. The diff, config, or model change, not the summary
- **Locus** — surface, stage, model, ranking layer
- **Timeline** — proposed → launched → read-out → decision, with dates
- **Movement** — metric deltas *with intervals and powering*, not "positive/negative." An underpowered null is not a negative result
- **Decision and its reason** — shipped / reverted / inconclusive / abandoned before readout
- **Mechanism of failure, where known** — the field that makes it a lookup rather than an archive. "Didn't work because the effect was real and negative" and "didn't work because the holdout couldn't resolve it" are opposite lookups, and only one of them means don't try again

### 5.3 What it unlocks beyond mode 2

The hindsight set (glossary object 5) measures **recall** — of things that proved out, how many did Detect surface. It is scored against what shipped, so it too is biased toward positives.

An attempts store adds the missing axis: **precision against reality.** Of the things Detect proposed, how many were actually tried, and how many of those failed? Today a Detect card that was pursued and didn't pan out looks like nothing at all. That's a false positive the program currently cannot see.

### 5.4 The hazard that would silently corrupt everything

**Temporal leakage.** The hindsight set works by snapshotting the world at time T and scoring what Detect produces against outcomes from T to T+n. If Detect also reads the attempts store, and the store contains records dated after T, then Detect at time T is reading the answers.

**Rule, non-negotiable if both exist:** the store is time-indexed, and any run anchored at T may only retrieve records with decision dates strictly before T. This is easy to get right at design time and nearly impossible to detect after the fact — the numbers just quietly improve.

### 5.5 It has the Curator's lifecycle problem, and the Curator already solved it

"This was tried and failed in 2024" may be false today; the system changed. Every record needs staleness handling, supersession, and human-confirmed retirement — which is exactly §1.3.2 and §1.3.3 of the Feedback Curator design, plus the lineage record in §1.3.5. **Reuse that design rather than inventing a second one.** The attempts store is a second repository with the same custodian problem.

### 5.6 The join is the work

The honest cost. Experiment records are structured but don't carry the hypothesis. LR docs carry the hypothesis in prose but not in a schema. Tying an experiment to a working code change or a stated hypothesis — the thing that makes a record useful — is a manual or LLM-assisted join, and that's where the effort lives. Any plan that doesn't budget for the join is not a plan.

---

## 6. The filter already exists on paper

The Skeptic (`reflex_feedback_curator_and_skeptic.md` §2) was designed in June with a `### Verified` section and a `### Related prior cards` section in its output format. Those are hallucination-check and already-tried-check. **The two mechanizable modes were already in the design and it's sitting unbuilt.**

This reframes it: the Skeptic isn't a pre-review quality nicety. It's Reflex's `is_legal_action()`, and it belongs *before* the judge, not beside it.

---

## 7. Risks

**Hallucination and novelty look identical from the outside.** Both cite something not in the record. A card asserting a table that doesn't exist is a defect; a card proposing a signal nobody has built yet is the entire point of the program. The check must distinguish **an assertion about the present** from **a proposal about the future** — structurally different claims — and that has to be in the design from day one, not retrofitted. This is Lesson 12's unsupported-region warning arriving from a different direction.

**"Already tried" must annotate, not reject.** This is the sharpest asymmetry in the whole scheme. Mode 1 can *reject* — a nonexistent table is simply wrong. Mode 2 cannot: a prior failure is a reason to look harder, or to check whether the earlier attempt was underpowered, not a veto. If "already tried" becomes a filter, Reflex re-creates the conformity problem it exists to break, and it does so invisibly.

**Over-filtering compounds.** Every mechanical check reduces what reaches a human. That's the benefit and also the exposure: filters are never audited by the people they save work for. Whatever gets built needs a periodic sample of *rejected* cards reviewed by a human — the mirror image of the blind audit on top-scored cards in `eval_02` rule 3.

**Owner.** Routed 8/15 (see `eval_00` §5 item 19): the eval framing goes to **Chao**, as the non-confounded version of his own Phase 3 shipped-experiment metric; the LR/Helium integration is data engineering and sits closer to **Gideon's** logging and infra lane. The taxonomy work in §2 and §4 is eval-shaped and stays with me.

**The seam, which must be named in the ask rather than discovered later.** The attempts store and my hindsight case bank (`eval_00` §7) are the *same join*. The bank ties the cycle archive to the shipped-experiment record with outcome labels; the store ties the experiment platform to LR docs with hypothesis labels. The expensive half — tying experiments to hypotheses — is common to both. Propose it as **one join, two consumers.** Otherwise this reproduces the structural finding in `eval_00` §4 item 1 precisely: two people building one pipeline under two names, found in October.

**And keep the two uses separate.** As an *eval source* — Detect's precision against reality — this is Chao's. As a *retrieval corpus at card-generation time*, so Detect stops re-proposing tried things, it is agent capability: the Skeptic, Andrew's surface. Same corpus, two consumers, different owners. Only the first is eval, and conflating them is how the proposal gets rejected as scope creep.

---

## 8. Sequencing

1. **Classify existing rejected cards** into §2's taxonomy. Produces the ratio. Gates everything below. *(An afternoon, no new data.)*
2. **Build the mode-1 check** — catalog lookup for hallucinated references. Cheapest, fully mechanical, and independently useful whatever the ratio says.
3. **Move it pre-judge**, then re-measure human–human and judge–human κ on what survives. This is the number Lesson 11 actually wants.
4. **Scope the attempts store** — pick one surface, join a quarter of experiment records to LR docs by hand, and measure effort-per-record before proposing anything wider.
5. **Derive the real taxonomy** from step 1's labels and replace §2.
6. **Only then** build the failure-type → component lookup that makes `blame()` deterministic for the mechanized share.

---

## 9. Open questions

1. **What's the actual ratio?** Everything here is conditional on step 1.
2. **Can the experiment platform be joined to Reflex cards at all**, or only to LR docs? If only the latter, the store inherits the positive-result bias and most of its value evaporates.
3. **Who owns the store?** It spans the experiment platform, LR docs, and Reflex, which likely means no one does today.
4. **Does the card schema change?** Mode 3 requires cards to assert estimated magnitude and effort. That's a change to what Detect emits, which is Andrew's surface, not the eval program's.

## Related

- `eval_00_hub.md` — program state and open items · `eval_01_glossary.md` — the attempts store is a candidate object 8
- `eval_02_judge_lockbox_protocol.md` §rule 3 — the blind-audit pattern this borrows for rejected cards
- `eval_03_evolve_feedback_and_contract.md` §3 — the failure-type variant of the `blame()` proposal
- `reflex_feedback_curator_and_skeptic.md` §2 — the Skeptic, i.e. the filter, already designed
