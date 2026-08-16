# Seam message — Chao's Stage 2 ≡ Janvi's Evolve Detect adapter

**Drafted 2026-08-12 (§F.2 of the eval working doc). Goal: name the overlap now so two GEPA-on-playbooks pipelines don't exist by October, and get the EvalHub question answered in writing.**

Recommended delivery: one Slack message to Chao + Janvi together (they're each other's reviewers already — this is a seam-naming, not an escalation), with Dafang either included directly or pinged right after for the TL blessing. A live 30-min working session is the likely outcome; the message just sets the frame.

---

## RECOMMENDED — V2 merged message (8/12 PM, folds in James's expectation-setting draft)

Context: James drafted an opener proposing to "disambiguate the terminology"; decision (8/12 evening session) was **no standalone terminology doc** (professor-mode risk, third-doc-beside-two problem) — vocabulary locks via the seam conversation instead. This version leads with specific credit (proves the docs were actually read), makes terminology a symptom of the seam rather than the headline ask, and pre-announces the lockbox note:

> Hi Janvi, Chao — I spent real time in both docs this week. Chao, the judge V1 + calibration sequencing is the right backbone; Janvi, EvalResult-as-the-sole-coupling-point is exactly the contract move I'd have made. Reading them side by side as a reviewer, two things worth settling together, ideally live for 30 min:
>
> 1. We're using the same words for different work in a couple of places — the clearest one: Stage 2 of the Phase-1 plan and Evolve's Detect adapter describe the same GEPA-on-playbooks loop. I'd propose the seam as: Chao owns judge + calibration (the fitness function), Evolve owns the optimization loop, Stage 2 becomes the Detect adapter. Locking the vocabulary and ownership now is much cheaper than two parallel pipelines in October.
> 2. The references already list EvalHub — worth a written build-on-it-or-why-not, before someone with less context asks us.
>
> Separately, I'm dropping a short eval-integrity note on the Detect doc today (holdout/lockbox, judge versioning, blind audits) — it's my 7/24 comments made concrete, and I'd rather it land before the first GEPA run than after. I have a couple of contract-field proposals too, but those are easier sketched live.

## V1 — original main message (to Chao + Janvi, Dafang cc'd or in-channel)

> Chao, Janvi — reading both docs side by side (Detect Eval Proposal + Evolve TDD), I think Stage 2 of the Phase-1 plan and Evolve's Detect adapter are the same work: run the calibrated judge in the detect cycle and use GEPA to improve playbook prompts against it. Same loop, described in two docs with two owners — if both proceed as written we'd have two GEPA-on-playbooks pipelines by fall.
>
> Proposed seam, for reaction: **Chao owns the judge + human calibration** (i.e., the fitness function — Stage 1 exactly as planned), **Janvi's Evolve owns the optimization loop**, and Stage 2 becomes the Evolve Detect adapter rather than a parallel build. Chao's judge plugs in as the eval source Evolve's contract already expects. Nobody loses scope — the judge is the harder and more load-bearing half, and Evolve gets a real first customer.
>
> One more thing worth settling in writing while we're at it: the proposal's own references list **EvalHub** (agent registration, datasets, simulation runs, LLM/code graders). Are we building on it, or is there a reason not to? Either answer is fine — but if we build beside it without a stated why-not, we're inviting the platform-consolidation question later, from people with less context than us. A paragraph in the doc settles it.
>
> Happy to do a 30-min working session this week if that's easier than threading — I have concrete proposals for the contract seam (judge versioning + a couple of EvalResult fields) that I'd rather sketch live.

## Dafang heads-up (if not in the main thread — send just before)

> Dafang — about to suggest to Chao + Janvi that Stage 2 of the judge plan and Evolve's Detect adapter merge into one pipeline (Chao = judge/fitness, Janvi = loop). It's a scope-clarity fix, not a criticism of either doc — both are good, they just grew into the same territory from two directions. Flagging so it lands with your blessing rather than as a surprise.

---

## Watch-fors

- **Attribution:** Evolve's author of record is **Janvi Palan** (Ads folks are reviewers/Build-eval source). Use her name when citing the TDD upward — the repo's earlier "senior Ads MLE" phrasing was wrong and is now corrected.
- **Sequencing:** the lockbox one-pager (`lockbox_protocol_2026-08-12.md`) should hit Chao's doc **before or with** this message — it's the "concrete proposals" the last line references, and it establishes the eval-integrity lane as James's contribution before the seam re-org conversation starts.
- If Chao reads the merge as scope loss: the counter is in the message already (judge = the load-bearing half), and Dafang's blessing is the backstop — that's why the heads-up goes first.
