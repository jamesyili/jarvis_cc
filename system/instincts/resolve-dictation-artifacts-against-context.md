---
id: resolve-dictation-artifacts-against-context
trigger: James's input reads voice-dictated and a project/person name doesn't match known context ("Allen Utility", "PinRec v2", "Oliver"), especially when the name is headed into a work deliverable
behavior: Resolve garbled names against repo context (projects, people, artifacts) and use the canonical name, but flag the mapping explicitly in the reply ("assuming PinRec v2 = Pin Selection v2 (PSv2)") so James can correct. For names Leo cannot resolve from context (new people), carry them verbatim but surface them in a pre-submit spelling check — dictated names are a known error class.
confidence: 0.95
evidence_count: 9
created: 2026-07-09
last_updated: 2026-08-15
status: active
---

## Evidence

### 2026-08-14 (Safe Journeys session) — search by ROLE, not just by name spelling

> James: *"Qinglong not Xing Xong. Sr EM on content quality reporting into Faisal. **Teen** safety not team safety."*

Two garbles in one session opening, handled differently:
- **"team safety" → teen safety.** Leo flagged it proactively and unprompted ("I'm reading that as *teen* safety given 'headlines' and 'up to the CTO'"). Correct, and the flag was the right shape. ✅
- **"Xing Long" → Qinglong (Zeng).** Leo **failed** here. It grepped for the literal string `xing long`, found nothing, and then wrote *"Xing Long is not in the repo at all"* — building a whole "gap to fill" framing on a name that didn't exist. **Qinglong Zeng was already on file** from the 2026-07-27 GenAI WG entry, tagged *"CQ team — new contact,"* which matched James's description exactly (Content Quality, senior, Faisal's org).

**The lesson:** a name-string grep returning nothing is not evidence the person is unknown. When a dictated name fails to resolve, **search by ROLE** — team, level, reporting line, the function James described — because that is what the repo actually indexes well. Phonetic distance here was small (Xing-Long / Qing-long) and the role match was exact; either check alone would have caught it.

Signal: correction.

### 2026-08-10b (evening session) — the garble WAS a real, higher-stakes person; resolution flipped the advice
> "This came from Kurchi's feedback that Alok isn't really ramping up well into the space"
Dictation produced "Kurchi" — a real name in the repo (**Sr. Director SSJ, Roberto's boss, structurally adversarial on UPP**) — but the complaint shape (daily collaborator, "slowing her down," Alok's ~20-day RR ramp) fit **Chuxi**, whose 1:1 was the same day. The two readings demanded *different advice* (intra-pod re-scope under Alim vs. immediate pull-off-the-SSJ-surface political move). Leo checked the stakeholder file, flagged the fork explicitly, wrote the filed entry with the ⚠️ dictation-check open, covered both branches in the advice, and asked the one question. James: "It was Chuxi." Extends the 7/15 lesson: a near-match garble can land on a *real* different person, making it more dangerous, not less — the wrong reading was fully coherent and would have produced confident wrong strategy. Signal: confirmation (capped).

### 2026-08-10 (Fan session) — person-name garbles in an emotional conversation, flag-the-tangle confirmed
> "Her manager, Gary, I understand. Fish, I'm putting in quotes."
Dictation produced "Gary" and "Fish" for two people load-bearing to the read (the hated boss vs. the sponsor she's staying for). No prior record of Fan's reporting chain existed to resolve against, so Leo carried the names, built the read on the parts that didn't depend on the fork, and flagged the contradiction explicitly in-reply ("she 'hates her boss' but is 'staying for Fish' — if those are the same person, that contradiction *is* the whole story; the dictation didn't let me tell"). James corrected cleanly next turn: manager **Giri** (the friction), skip **Vish** (the sponsor) — two people, contradiction dissolved. Confirms the carry-verbatim-and-surface move for unresolvable names; the flag did the work. Facts filed to `family.md` same session. Signal: confirmation.

### 2026-08-09 (todo/session-overhaul session) — two artifacts in one dictated line, resolve-and-flag confirmed
> "start working on **leafguests** … looking at **Ashifu**"
Resolved against the Notion [Reflex] Next steps subs and backlog #11: "leafguests" → **Reflex**, "Ashifu" → **Shifu** (also "authentic AI systems evals" → *agentic*). Flagged the mapping in-reply per the documented move; James's next message ("a new reflex item") confirmed the resolution. Signal: confirmation.

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

### 2026-08-13
> (James, after Leo's flagged resolutions:) "Oliver = Olafur"
Context: Heavy dictation session — resolved Kurchi→Chuxi, Sy→Sai, biology→Balaji, David→Dylan against repo context with mappings flagged inline; James confirmed the one Leo couldn't resolve (Oliver→Olafur Gudmundsson) and corrected nothing else. Two names carried verbatim + surfaced as unresolved ("Rope Urkel", "Yichin") per the behavior. The full loop worked end-to-end.
Signal: confirmation

### 2026-08-15
> Session-long decode chain, all confirmed by non-correction: "Elim"→Alim · "WriteGBT"→RecGPT · "janitor retrieval"→GenRet/Generative Retrieval · "flat weight scoring"→LWS/lightweight scoring · "Zli"→Zili · "Lim"→Alim · "Neema"→Nima. "DR approved" (Zili PIP) unresolvable → carried with a ⟨dictated⟩ flag into the record.
Context: Phone/dictation session on T2 scenario boards. Stating each mapping inline ("decoding: janitor retrieval = GenRet") let James confirm silently and never broke flow. Signal: confirmation.
