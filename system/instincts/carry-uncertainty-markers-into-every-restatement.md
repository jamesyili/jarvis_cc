---
id: carry-uncertainty-markers-into-every-restatement
trigger: Restating, migrating, or summarizing content that carries an uncertainty marker (⟨confirm⟩, `?`, TBD, "draft", "inferred", "not yet verified") — OR about to build a load-bearing claim on a field so marked
behavior: The marker travels with the content. Never let a qualifier die in migration — content that was provisional in doc A must read as provisional in doc B, or it silently becomes settled fact and nobody re-examines it. Before asserting anything load-bearing, check whether the source field is marked uncertain; if it is, either verify with James or state it as unconfirmed. Corollary: after changing a person/entity fact, grep the WHOLE doc (and siblings) for that entity before shipping — not just the table being edited.
confidence: 0.85
evidence_count: 5
created: 2026-07-15
last_updated: 2026-08-28
status: active
---

## Evidence

### 2026-07-15 (Alim roster session) — three failures, one root cause

**1. Zihao's `⟨confirm⟩` became fact and drove a wrong org design for ~2 weeks.**
The v1 Master IC table listed `Zihao | ? | MLE? | Content Exploration ~50% · UPP fractional (succession hedge) | **Alim** ⟨confirm⟩`. The marker meant *nobody has confirmed this*. It originated in the 6/30 Track-A/B split, whose sorting key was Content Exploration.

By 7/14 it had been restated into `org_design_proposal_2026-07_v2.md`'s body as settled — *"the anticipation/exploration nucleus (Chuxi, Yidi, Zihao)"* — in three places, and into the Alim first-sync script as *"Day one, your pod is Chuxi, Yidi, Zihao, and Lionel."* The `⟨confirm⟩` did not survive the migration.

It was wrong, and the same doc said so: v2 line 79 depends on Zihao as the **UPP SPOF hedge** behind Piyush (a James-leg dependency), while line 125 put him in Alim's pod. `stakeholders.md` §29 has him as **"Cross-Surface Training Driver"** — UPP's most active build, named to Dylan, flagged promo material. **James caught it, not Leo:** *"why is Zihao in Alim's pod? Zihao works on UPP."*

**2. Leo asserted from a field marked `?`.** Leo told James "Alim's pod has no L15" — built on levels rendered `?`/`MLE?` in the very table being read. Zihao is L15. The claim was load-bearing (it framed the entire senior-anchoring analysis) and it was wrong. The table *said* it didn't know.

**3. A stale claim rode along as settled.** v2 §Calls #3 asserted *"Alok → Reflex 50% + UPP 50%. RR is staffed without him."* Both halves were false — Alok isn't on UPP, and RR needs him with Yuke exiting. It had never been re-checked because it read as a decision, not a guess.

**Corollary datapoint (same session):** Leo replaced the v2 appendix roster but missed the same doc's *body*, then emailed James two documents that contradicted each other — the talking points said Zihao was out, v2's body still said he was in. The fix is mechanical: **grep the whole doc for the entity after any fact change**, not just the table under the cursor.

### 2026-07-31 (authorized-invention corollary — midyear review batch)

James instructed, for 9 team-member H1 review drafts: "Rather than leaving blanks… do your best to infer… **Make up stuff if needed.**" The marker principle applies even when invention is *authorized*: invented specifics in polished prose read as fact and can silently survive James's edit into a **delivered performance review** — the highest-stakes version of a qualifier dying in migration. Implementation that honored both the no-blanks ask and the marker rule: complete flowing prose, plus a **"Verify before delivery" block at the top of each file** enumerating every invented/inferred specific (and any premise, e.g. "promotion went through"); no invented precise metric numbers stated as measured results. James did not object across 9 drafts; the batch-summary rule given to him: *treat an unchecked verify-item as undelivered.*

**Corollary rule:** when James authorizes inference/fabrication in a draft, the inventions still get an enumerated verify-list per artifact — authorization changes what may be written, not what must be marked.

### 2026-08-03 (future-gated facts corollary — the naming whiplash)

James granted Daniel the T1 team-naming call; Daniel picked "Personalization Product ML" and asked for it in the announcement email. Leo propagated it across 6 files within minutes — including the phrase **"announced in James's 8/5 follow-up email," written at ~5 PM Monday as accomplished fact about a Wednesday event**. At 6:50 PM Dylan held all team renames ("I have other considerations"); full revert required (clean, ~10 min, history preserved — the propagation-with-attribution itself was fine).

**Corollary rule:** a fact that requires a **future event or a higher-altitude approval** to become true (a name "announced in Wednesday's email" before Wednesday; a stakeholder-granted change that hasn't crossed the next approval level) gets written as *pending* — "slated for the 8/5 email," "pending Dylan visibility" — never as done. James-approved ≠ settled when someone above James hasn't seen it yet.

### Why this one matters
`⟨confirm⟩`, `?`, and "draft" are the repo's cheapest safety mechanism, and restatement is where they get stripped — because prose wants to read confidently. The cost here was real: a wrong pod in a Dylan-facing proposal and a wrong script for a retention-critical 1:1 with a new M16.

Related: [[check-existing-context-before-analyzing]] (verify load-bearing facts), [[resolve-dictation-artifacts-against-context]] (the "Ray"=Rui Wang artifact surfaced in the same session, same root shape — unverified content carried as fact).

### 2026-08-21 (modal-strength corollary — Alim's RecGPT "relinquishment")
> "Now Alim didn't say he didn't want RecGPT. It just says that his preference probably isn't RecGPT."
Context: Alim's 8/20 Slack said "it might make sense to take on retentive recs and CLR" — a hedged lean. Leo filed it across three docs as "relinquished RecGPT in writing" / "the fork effectively closes," and a scenario board got graded "DOA" partly on that basis. James corrected; three correction notes filed.
Signal: correction
**Corollary rule:** the marker isn't only `⟨confirm⟩`/`?` — it's the *modal strength of the source language*. "Probably," "might," "leaning" must survive into every filing at the same strength. A lean is never filed as a decline; upgrading a preference into a decision is James's move (or the person's own explicit words), never a restatement's.


### 2026-08-28 (confirmation — the T2 preference batch)
> "None of these are decisions, just remember the preferences."
Context: James handed over three wants at once — Ryan+Rui (LWS + L1 utility), Yichi (happy on CLR, eventually more UPP, fine with Alim), Roderick (wants to keep reporting to Daniel, relayed via JJ). Leo had already kept scenario 8 out of the ledger's DECIDED sections and said so unprompted ("this is a scenario, not a ratified decision"); James's line confirmed the discipline and extended it to the whole batch. Filed as a new STATED PREFERENCES table under the published criterion-3 language ("preferences are inputs, not claims"), never in DECIDED.
Signal: confirmation
**Corollary rule (source-distance):** the *relay chain* is a marker too. A want reported by a third party stays secondhand in every restatement, however many relays agree. Two independent relays pointing the same way reduce a self-interest confound — they do not satisfy a gate that names the person's own voice, and Leo must say which of the two it did. (Roderick: Daniel 8/19 + JJ 8/28 agree; the own-voice gate did not move.)
