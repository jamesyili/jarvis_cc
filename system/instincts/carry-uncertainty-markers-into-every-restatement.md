---
id: carry-uncertainty-markers-into-every-restatement
trigger: Restating, migrating, or summarizing content that carries an uncertainty marker (⟨confirm⟩, `?`, TBD, "draft", "inferred", "not yet verified") — OR about to build a load-bearing claim on a field so marked
behavior: The marker travels with the content. Never let a qualifier die in migration — content that was provisional in doc A must read as provisional in doc B, or it silently becomes settled fact and nobody re-examines it. Before asserting anything load-bearing, check whether the source field is marked uncertain; if it is, either verify with James or state it as unconfirmed. Corollary: after changing a person/entity fact, grep the WHOLE doc (and siblings) for that entity before shipping — not just the table being edited.
confidence: 0.6
evidence_count: 1
created: 2026-07-15
last_updated: 2026-07-15
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

### Why this one matters
`⟨confirm⟩`, `?`, and "draft" are the repo's cheapest safety mechanism, and restatement is where they get stripped — because prose wants to read confidently. The cost here was real: a wrong pod in a Dylan-facing proposal and a wrong script for a retention-critical 1:1 with a new M16.

Related: [[check-existing-context-before-analyzing]] (verify load-bearing facts), [[resolve-dictation-artifacts-against-context]] (the "Ray"=Rui Wang artifact surfaced in the same session, same root shape — unverified content carried as fact).
