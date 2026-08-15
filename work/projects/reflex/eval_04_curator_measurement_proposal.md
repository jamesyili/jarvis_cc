# Feedback Curator — making it measurable, and three design deltas

**Status:** proposal, 2026-08-15 · **Author:** James Li · **Builds on:** `reflex_feedback_curator_and_skeptic.md` (the Curator design doc) · **Evidence:** SkillOS (Google Cloud AI Research / UIUC / MIT), `kb/hard/raw/arxiv/skillos-learning-skill-curation-for-self-evolving-agents.md`

**Circulation note:** §6 is internal. Everything above it is safe to share with Andrew, Dylan, and Janvi.

---

## 1. What this proposes, in one paragraph

The Curator design already specifies the right *operations* — intake, dedup/conflict resolution, decay handling, ranked retrieval, lineage. What it does not specify is how anyone would know whether the Curator is working. §1.8 names over-curation and under-curation as the failure modes and offers mitigations, but no measurement that would tell us which one we're in. SkillOS is the first paper I've seen that isolates the curator as a component, trains it, and measures it — and its measurements transfer to our design without adopting any of its training machinery. This proposes four metrics, one growth curve we can run against the existing archive this week, and three deltas to the design.

## 2. What the existing design already covers

Worth stating plainly so the deltas below read as additions rather than rediscovery.

| SkillOS component | Already in our design |
|---|---|
| `insert_skill` | §1.3.1 pattern intake |
| `update_skill` | §1.3.2 dedup + conflict resolution (merge / version / replace) |
| `delete_skill` | §1.3.3 decay handling, human-confirmed |
| BM25 retrieval | §1.3.4 ranked pattern lookup |
| — | §1.3.5 **lineage records** — SkillOS has no equivalent |
| — | §1.6 **conflict reports with options and a recommendation** — no equivalent |

Two things we have that the paper doesn't: an audit trail that answers "why does Reflex believe X," and an explicit human resolution step for contradictions. Both are worth keeping even where they cost us something below.

## 3. The gap: the design has operations but no metrics

SkillOS's headline behavioral result is about the *ratio* of operations, not their existence. Early in training the curator almost exclusively inserts; as it improves, `update` rises and `insert` declines, with `delete` staying small but growing. Their conclusion: "the dominant form of adaptation is to revise and consolidate previously acquired skills." An immature curator accretes; a mature one consolidates.

We have no way to say which one ours is. Four metrics fix that, all lifted directly from the paper's Figure 6 (their base → trained values on ALFWorld shown for calibration, not as targets):

| Metric | Definition for us | Their base → trained |
|---|---|---|
| **Pattern coverage** | fraction of `quality_patterns.md` entries retrieved by any card in a window | 53.6% → 72.9% |
| **Usage rate** | fraction of cards where ≥1 pattern was retrieved | 87.9% → 100% |
| **Successful-usage rate** | pass rate among cards that used patterns | 61.2% → 88.6% |
| **Patterns per card** | mean retrieved per card — *lower is better* | 2.24 → **1.95** |

The last one matters most for how we'd read the others: their trained curator did better while retrieving *fewer* patterns. Gains came from precision, not volume. A proposal that grows the patterns file and calls it progress is measuring the wrong thing.

**A second paper found the same shape, which is why I'd treat this as a health metric rather than a curiosity.** EvoHarness-RL (Meta AI/UIUC) trains a policy over externalized harness state and observes *harness annealing*: after RL, external-state calls drop to roughly one per episode, because the policy internalizes routine scaffold use and reserves external access for when expected benefit exceeds step cost. Two independent labs, two different mechanisms, one result — **maturity shows up as reduced and more selective interaction with external state.**

That inverts the natural instinct. If `quality_patterns.md` grows and cards retrieve more patterns over time, that is not the system learning; on this evidence it is the signature of an immature one. Which makes the growth curve in §3.1 a leading indicator rather than a filing concern.

**Coverage is the one to run first.** If it comes back near 50%, half of what the Curator has produced has never been used by anything, and the under-curation failure mode in §1.8 is already live rather than projected.

### 3.1 The growth curve — runnable this week, no labels, no new runs

The design doc records `quality_patterns.md` at **341 lines at cycle 13**. The archive is now at 66 cycles. That gives a baseline and a five-fold interval for free.

Plot lines and entry count per cycle, then sample entries from early, middle, and late cycles and score them pairwise for restatement. Two outcomes, both useful:

- **Monotonic growth with heavy late-stage redundancy** → we are in the accretion regime the design was written to prevent, and the Curator's operation mix is the thing to fix.
- **Flattening, or growth with low redundancy** → the design is holding, and the four metrics become routine reporting rather than a diagnosis.

This is the cheapest real measurement available anywhere in the eval program right now. It needs no human labels, no judge, and no new agent runs.

## 4. Three design deltas

### 4.1 The human gate is also a bias toward accretion

§1.4 and §1.7 are unambiguous: the Curator proposes, humans merge; retirement is never autonomous. That is the right safety property and I don't propose weakening it.

But it has a consequence nobody has written down. An insert is a low-stakes approval — a reviewer glances and accepts. An update means adjudicating a contradiction (§1.6 asks them to pick between merge, version, and replace). A retirement means asserting that something we once believed is now wrong. **The approval cost of the three operations is wildly unequal, and it is cheapest for exactly the operation SkillOS identifies as the immature one.** Whatever mix the Curator proposes, the realized mix will skew toward insert.

| | What it buys | What it costs | Pick it when |
|---|---|---|---|
| Leave as-is | Maximum safety; no stale pattern ever silently disappears | The file accretes regardless of how good the Curator gets; §1.8's under-curation mitigation never actually fires | Reviewer bandwidth is abundant and the file is small |
| **Measure proposed vs. merged separately** | Tells us whether the bottleneck is the Curator or the humans — different fixes | One extra field in the audit trail | **Now — it's nearly free and we currently can't tell these apart** |
| Tiered approval: consolidation is lightweight, retirement stays heavy | Removes the bias where it's cheapest to remove; retirement keeps full protection | Requires agreeing that merging two near-duplicate patterns is lower-risk than retiring one | After the proposed-vs-merged data shows humans are the bottleneck |

Recommendation: take the middle row now, hold the third until we have the data.

### 4.2 Compression, and its real tension with the evidence field

SkillOS carries an explicit compression reward — repository size penalized against the curator's input context — and states its purpose directly: to discourage verbatim trajectory copying and force distillation into reusable skills. Removing it measurably hurt performance.

We have no analogous pressure. And §1.8's mitigation for over-curation — "preserve original reviewer language in the evidence field" — deliberately pushes the other way.

I don't think that mitigation is wrong. Preserving the reviewer's own words is what makes the lineage trail worth having. But the two goals are pulling on the same file, and the resolution is to stop treating a pattern entry as one thing:

- **`Correction:`** is the distilled, reusable part. Compression applies here. It should get shorter and more general as a pattern is reaffirmed across cycles.
- **`Evidence:`** is the verbatim archive. Compression does not apply. It should grow as reaffirmations accumulate.

Measure compression on `Correction:` only. A pattern whose `Correction` field is still growing at its third reaffirmation is being accreted, not consolidated.

This also connects to something already in the critique doc. AI2/UW's explanation for why harness evolution underperformed was that meta-agent edits "memorize fixes rather than distilling strategies" (§15½). SkillOS names the same failure and builds an objective term against it. That's a mechanism-level reconciliation of the two papers, and it argues the negative result may be a result about self-evolution *run without a compression objective* — which is a materially different claim from "self-evolution doesn't work."

### 4.3 Do not point the biggest model at the Curator

SkillOS's most counterintuitive result: using Gemini-2.5-Pro directly as the curator **underperformed their trained 8B curator**, and the gap was worst when paired with a weaker executor. Their reading — "stronger reasoning ability alone does not guarantee effective skill curation, as frontier-generated skills may be misaligned with the executor's capacity or usage patterns."

The default instinct when the Curator underperforms will be to upgrade its model. The evidence says the axis that matters is the match between what the Curator writes and how the executor actually retrieves and uses it — which the coverage and patterns-per-card metrics in §3 measure directly, and model capability does not.

## 5. What this proposal does not do

Explicitly, so it isn't inferred: **no finetuning, no RL, no GRPO.** SkillOS's training recipe is not adoptable here and I am not proposing it. Their entry cost is grouped task streams plus rollout volume; for calibration, GEPA reached better results than GRPO on IFBench with 678 rollouts against GRPO's 24,000, and Evolve's entire budget is 450 invocations. We are two orders of magnitude from the regime where weight optimization is a question worth asking, and the prerequisite is a fitness signal we trust — which is the eval-integrity work, not this.

What transfers is the measurement apparatus and the operation-mix framing. That's it, and it's enough.

## 6. Open questions and what I'd want from whoever owns this

Internal — not for circulation.

1. **Evaluation unit.** Judging a curation decision requires seeing whether it helped a *related* later card. SkillOS's largest single ablation was exactly this: random task sequences cost more than either reward term. Our §1.5 `Evidence:` field already records cycle-and-card lineage — that is the grouping key, and it means the raw material exists. But it also means Curator evaluation needs lineage-linked cycle groups while judge evaluation needs spread across cycles. **These are two different datasets and the 8/14 glossary has an object for neither.** Worth adding before anyone builds either.
2. **Ownership.** §5 of the design doc flagged this for Andrew and Dylan and I don't believe it was resolved. The measurements in §3 are eval-shaped and sit close to my lane; the design deltas in §4 are Curator-shaped and do not. I'd rather hand §4 to whoever owns the component than carry it.
3. **Does the Skeptic change this?** The Skeptic reads patterns via the Curator's retrieval (§2.7), which means it is a second consumer and should appear in the coverage metric. If it isn't counted, coverage will look better than it is.
