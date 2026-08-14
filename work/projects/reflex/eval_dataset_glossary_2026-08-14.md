# Reflex Eval — Dataset Glossary

**Purpose:** there are five distinct datasets in the Reflex eval program and roughly a dozen names floating across three documents. This file fixes one canonical name per object and records every alias in the wild, so a sentence in a review comment can't quietly mean two things.

Written 2026-08-14 because the terminology collided in James's own working session — the strongest available evidence that it will collide in the group's.

---

## The two questions that separate every dataset

Every set below is fully specified by two answers. Nothing else matters for telling them apart.

1. **Where do its labels come from?** A human grading a card, or the world recording an outcome.
2. **Who is allowed to optimize on it?** A specific optimizer, or nobody.

That's it. All five objects are combinations of those two answers.

---

## The five objects

| # | Canonical name | What it is | Labels come from | Who may optimize on it | What it catches | Status today |
|---|---|---|---|---|---|---|
| 1 | **Judge calibration set** | Cards with human labels (binary pass/no-pass + rationale) | Humans grading cards | **Chao's judge GEPA loop** | Judge-human misalignment | ~20 PM-graded cards via Asana forms |
| 2 | **Judge holdout** | Human-labeled cards withheld from judge optimization | Humans grading cards | **Nobody** — judge is scored on it | Judge overfit to the calibration set | **Does not exist** (the §B.6 gap) |
| 3 | **Evolve fixture bank** | The recorded Asana/Presto/MCP snapshots each candidate playbook runs against | n/a — inputs, not labels | **Janvi's playbook GEPA loop** | Nothing; it's the training input | Specified in the TDD |
| 4 | **Lockbox** | Human-labeled cards, frozen, entering *no* optimizer's objective — not judge GEPA, not playbook GEPA, not the Feedback Curator | Humans grading cards | **Nobody** — everything scores on it, nothing tunes on it | The whole stack fooling itself; leakage; overfit | One-pager drafted; posting unconfirmed |
| 5 | **Hindsight set** | World-at-T snapshots + the record of what actually shipped or proved out between T and T+n | **History** — outcomes, not opinions | **Nobody** — read periodically as a drift check | Construct failure: optimizing legibility instead of discovery | v0 scoped; blocked on work-side data |

### The distinction that actually matters: 4 vs 5

Both are frozen. Both are optimized on by nobody. That's why they blur. Here is the difference:

- **Lockbox: humans grade cards.** Same construct as the judge. Answers *"is this number real, or did we leak?"* → **internal validity.**
- **Hindsight set: history grades outcomes.** Different construct entirely. Answers *"is this number measuring the thing I care about?"* → **construct validity.**

A perfect lockbox score with a flat hindsight number means the loop is optimizing card legibility. The lockbox cannot detect that — it is scored by the same judge, so it reports the same construct error with a clean conscience. **This is the reason both must exist.** They are not redundant frozen sets; they catch different failures, and Lesson 6 vs Lesson 7 is exactly this split.

### 1 vs 4 — the other easy confusion

Both are human-graded cards. The difference is permission, not content: the calibration set is *training data for the judge*; the lockbox is *the sealed exam nobody studies from*. If the two are ever drawn from the same pool without an explicit split, the lockbox is already contaminated on day one.

---

## Aliases in the wild — what each source doc calls these

| Object | Appears as | Where |
|---|---|---|
| 1 — Judge calibration set | "graded cards", "human-labeled cards", "the ~20 cards", "Phase 1 labels" | Chao's proposal; session notes |
| 2 — Judge holdout | "held-out split", "leave-one-out CV" | §B.6 of the critique doc |
| 3 — Evolve fixture bank | **"case bank"**, "fixture store", "fixtures", "cases" | Janvi's TDD; §12 of the critique doc |
| 4 — Lockbox | **"ultimate holdout"** (James's notes), **"golden set"** (James, 7/24 meeting), "frozen holdout", "sealed cases" | James's notes; §E.3; the lockbox one-pager |
| 5 — Hindsight set | **"hindsight-recall case bank"**, "the anchor", "outcome anchor" | §E.4, §G of the critique doc |
| — | "recall gold set" — a *sixth*, different thing: past PM roadmaps used as a recall reference. Critiqued in §B.5 and being replaced by object 5 | Chao's proposal |

---

## Three live collisions to defuse

1. **"case bank" means two different objects.** Janvi's TDD uses it for the Evolve fixture bank (object 3, optimized on). The critique doc uses it for the hindsight set (object 5, never optimized on). These have *opposite* access rules. Saying "the case bank" in the working session will be understood as object 3 by everyone who read the TDD. **Fix: retire the phrase entirely.** Use "fixture bank" and "hindsight set."

2. **"golden set" / "gold set" means two different objects, in two live documents.** James's 7/24 on-record comment — *"hold out a golden set if using GEPA"* — means the **lockbox** (object 4). Chao's proposal uses "recall gold set" for the **PM-roadmap recall reference**. Anyone reconciling the meeting notes against the proposal will merge them. **Fix: retire "gold/golden set" from all Reflex eval writing.** It is unrecoverable.

3. **"holdout" is ambiguous between objects 2 and 4.** The judge holdout is a judge-scoped test set; the lockbox is program-scoped. **Fix: never use bare "holdout" — always "judge holdout" or "lockbox."**

---

## Canonical vocabulary (use these, retire the rest)

**Use:** judge calibration set · judge holdout · Evolve fixture bank · lockbox · hindsight set

**Retire:** case bank · gold set · golden set · bare "holdout" · "ultimate holdout" (→ lockbox) · "the anchor" as a standalone noun (→ "the hindsight set," describing it as the anchor)

---

## The one-paragraph version

> Humans grade cards. Some of those grades train the judge (**calibration set**); some are withheld to check the judge didn't just memorize them (**judge holdout**); and some are sealed away from every optimizer in the program so we can tell whether the whole stack is fooling itself (**lockbox**). Separately, the playbook optimizer runs candidates against recorded world-snapshots (**Evolve fixture bank**). And finally, one set is graded not by humans at all but by history — what actually shipped and proved out (**hindsight set**) — because every other number in the program is ultimately somebody's opinion of a card, and only that one can tell us whether we're finding things or just writing well.

---

## Related

- Critique + IC lane: `eval_critique_and_ic_lane_2026-08-11.md` (§E.3 lockbox, §G hindsight set, §B.5 recall gold set, §12 fixture bank)
- Lockbox protocol one-pager: `lockbox_protocol_2026-08-12.md`
- EvalResult v2 straw schema: `evalresult_v2_straw_schema_2026-08-12.md` — `case_source` field is where these distinctions become machine-enforceable
