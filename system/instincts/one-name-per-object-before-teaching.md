---
id: one-name-per-object-before-teaching
trigger: Teaching, quizzing, or writing review comments on a technical workstream whose working doc has accumulated across multiple sessions — especially when several source documents (other people's) each carry their own vocabulary for the same objects
behavior: Fix one canonical name per object BEFORE teaching or testing on it. Sweep the working doc for the two collision types — one name covering two objects, and one object carrying several names — and resolve them into a written name-to-object map. Ambiguity in a question Leo asks is Leo's defect, not the learner's wrong answer. If James's answer collides two concepts, check whether Leo's own documents collided them first; usually they did. When source docs disagree on a term, name the collision explicitly and retire the overloaded word rather than picking a winner silently.
confidence: 0.3
evidence_count: 1
created: 2026-08-14
last_updated: 2026-08-14
status: active
---

## Evidence

### 2026-08-14
> "I think all of this terminology is fucking confusing and you're using different terminology for different things. Can you write down where all of this terminology is?"

and, earlier in the same session:

> "Your questions are not very clear to be honest."

Context: Reflex eval teaching session (Lessons 6–10). Leo had been maintaining `eval_critique_and_ic_lane_2026-08-11.md` across four sessions, during which the doc came to use **"case bank"** for two different objects with opposite access rules — Janvi's Evolve fixture store (optimized on) in §12, and the hindsight-recall set (never optimized on) in §E.4. Leo then wrote a quiz question using "case bank" in one sense while asking about holdout wear-out, which James correctly flagged as unclear. Two questions later James answered "the case bank is what allows us to train the LLM judges" — collapsing the anchor into training data, i.e. exactly the contamination his own notes existed to prevent. **The learner's conceptual error was downstream of Leo's terminological drift.** Resolution: `eval_dataset_glossary_2026-08-14.md` — five canonical objects, each pinned by two questions (where labels come from, who may optimize on it), plus three documented collisions ("case bank", "golden set", bare "holdout") with retire-this-word instructions.

Signal: correction

Lesson: a doc that grows over several sessions accrues synonym drift invisibly, because each individual session's usage is locally consistent. The drift only surfaces when someone is tested on it. Sweep for it before teaching, not after — and when a term collides across *other people's* documents (here James's own 7/24 "golden set" vs Chao's "recall gold set"), that collision is itself a finding worth surfacing upward, since it will silently merge two objects in any reader reconciling the two docs. Related: [[one-home-per-fact-in-multisection-docs]], [[credit-provenance-precisely]], [[name-reference-files-by-role-not-instance]].
