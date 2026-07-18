---
id: resolve-dictation-artifacts-against-context
trigger: James's input reads voice-dictated and a project/person name doesn't match known context ("Allen Utility", "PinRec v2", "Oliver"), especially when the name is headed into a work deliverable
behavior: Resolve garbled names against repo context (projects, people, artifacts) and use the canonical name, but flag the mapping explicitly in the reply ("assuming PinRec v2 = Pin Selection v2 (PSv2)") so James can correct. For names Leo cannot resolve from context (new people), carry them verbatim but surface them in a pre-submit spelling check — dictated names are a known error class.
confidence: 0.8
evidence_count: 3
created: 2026-07-09
last_updated: 2026-07-17
status: active
---

## Evidence

### 2026-07-17 (Dhruvil/reorg session) — a garbled list nearly reversed a load-bearing org premise
Two artifacts in one session, both resolved by the documented move:
- "Drupal" / "Droovl" / "Dhruva" → **Dhruvil**, resolved from context and flagged in the reply ("Reading Drupal/Dhruva as Dhruvil — flag if wrong, everything below hangs on it") before building a whole stakeholder-strategy response on it. James confirmed implicitly by proceeding.
- **"Yan, Daniel, and Rahul are moving under Dhruvil"** — dictated mid-context-dump. Taken at face value, "Daniel" would have **reversed the central premise of the org design work** (Daniel Liu + team → James, established 7/7, reconfirmed the same morning). Leo held the one conflicting name out of the record, cross-checked internal evidence (James's own "my new team already collaborates with his current team around UPP" = the Kim Toy loan = only coherent if Daniel Liu is James's inbound), and asked one disambiguation question. James's answer: "Only Rahul and his team of 4 MLEs → Dhruvil; Daniel and his 7 MLEs → me." The garble was real and the record survived it.

Refinement worth keeping: when a dictated list **conflicts with an established premise**, don't ⟨confirm⟩-tag it into the record (the 7/15 Zihao lesson — provisional tags get promoted to fact). Write only the non-conflicting parts, ask about the conflict, record after. Also: internal evidence elsewhere in the same dictation often adjudicates the garble before James answers — use it to form the hypothesis, but still ask.

### 2026-07-15 (Alim roster session) — the artifact hid for weeks inside a Dylan-facing doc
"**Ray**" — an L14 SWE on L1/Real-Time with his own 1:1, named in the H1 self-review ("I also hired two new engineers, Ryan and Ray"), and load-bearing in `org_design_proposal_2026-07_v2.md` in **10 places** including the no-pager-gap oncall table — turned out to be **Rui Wang**. A preferred-name/dictation artifact that had been carried as a distinct person across every doc.

What worked: Leo **did not infer**. Ray was absent from James's new authoritative table while Rui Wang (same level, same family, same two workstreams, also a recent hire) was new — Leo flagged the fork and asked, rather than assuming a rename. Tenure math actively argued *against* the merge (a 6/29 message implied Ray predated the OOO; Rui joined during it), so a confident guess would have gone the wrong way.

Two traps avoided, both worth carrying:
- **`Rui Liu` (Notif ML, cross-org UPP partner) already existed in the repo** — a different person entirely. Near-match names ≠ variants (cf. `check-existing-context-before-analyzing` heuristic 6).
- **"Ray" in `l1_utility.md` and `paper_capture.md` = the Ray compute framework.** A word-boundary global find-replace would have corrupted both files. Nine targeted edits, not one sed.

Refinement: dictation artifacts don't only appear in *fresh* input — they **calcify into the repo** and get carried as fact. When an authoritative roster/list arrives and a known name is *missing* while a near-identical unknown one appears, that's the artifact surfacing. Ask; don't reconcile silently in either direction.

### 2026-07-09 (JJ promo package session)
Three name-shaped dictation artifacts in one session:
- "Allen Utility" → resolved silently to L1 Utility (correct — obvious from context).
- "PinRec v2" → resolved to Pin Selection v2 (PSv2) and flagged in-chat; James did not object (correct).
- "Oliver" → written into the draft as heard; James corrected mid-turn: "Olafur not Oliver." Unresolvable from context (new person), but a spelling-confirm nudge for new dictated names would have caught it — and it echoes the 7/9 peer-feedback session's pre-submit name-spelling checklist item (Andreanne, Jia Chong).
Signal: mixed — two confirmations of the resolve-and-flag move, one correction showing the gap for unknown names.
