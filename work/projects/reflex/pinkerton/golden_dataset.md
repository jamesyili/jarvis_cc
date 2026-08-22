# Pinkerton — Golden Dataset of 5 Issues for Eval

**Started 2026-08-22** (weekend IC project, decided with Leo; Notion: "[Pinkerton] Golden Dataset of 5 Issues for Eval", This Week). Purpose: 5 curated real investigations with known-good diagnoses → the regression benchmark for the Reflex **Evaluation & Evolution** thread (Janvi/Chao weekly, Shifu eval w/ An; JJ inherits ~Nov). Each case records: the trigger, the evidence trail, the verdict a competent agent must reproduce, and the traps (plausible-but-wrong answers).

Naming: **Pinkerton**, never "Pinsight" (James 8/22). Legacy URLs still carry `pinsight` paths.

---

## Case #1 — T&S "Elon scam pins" DSAT (2026-08-21) ✅ captured

**Trigger:** #user-feedback-xfn thread (started ~Aug 14 by **Becky Stoneman, Dir of Product**): the test account of **Neeti Deshmukh — VP of Trust & Safety, reports into the Chief Legal Officer** — kept receiving "Elon scam" pin recommendations on homefeed despite her having reported similar content. Root pin: AI-gen Elon Musk "Why do you like Elon Musk?" spam pin (sig `d9766702…`), reported from **Search**, 08-13. Andrew asked for same-day help. Worked in a James + Michael Weissinger + Dhruvil 3-person DM: James ran the Pinkerton investigation; **Michael wrote the response, asked the sharpening questions, suggested next steps**; **Dhruvil supplied the utility-weights dashboard** (`analytics…/homefeed-utility`; note repin + p2p impression weights are now *learned* — not visible in that UI) and ran the account lookup. Response posted Fri 8/21; Slack thread: `pinterest.slack.com/archives/C07SP4E8Q5S/p1786716774025239`.

**Key confounder (Michael's question found it):** the account's behavior is adversarial by design — Neeti *searches out* scam content, engages it heavily (closeups etc. — "yes, lots"), and reports some, deliberately probing "spiral" scenarios (Michael's read, from their shared Snap suggestive-content history). So the ranker's "she will engage with this" prediction is a faithful read of test-account usage. James's joke-solution #3 ("use another pinterest account") is a real recommendation shape: probe with a clean account, or the positive-engagement signal swamps everything.

**Method (what Pinkerton did):** full-funnel cross-reference of the 5 flagged homefeed pins against the user's complete 10-day negative-feedback ledger (PIN_HIDE / PIN_FLAG / PROMOTED_PIN_FLAG from `default.safe_event`, 08-04→08-13), checked against all three CG denylist keys (pin id / image signature / through-object board), per the stack doc *Hide & Report Signals Across the Homefeed Stack* (updated 8/21, at `scrimshaw…/reflex/hide_report_homefeed_stack.html`).

**Known-good verdict (what an eval agent must reproduce):**
1. **Not a suppression failure — a relevance problem.** Zero entity overlap: none of the 5 pins, their seed boards, or signatures match anything hidden/reported in the window. The denylists (PIN_ID / PFY / PFY_THROUGH) were *correctly* empty of these pins.
2. **Cross-surface silo:** the one organic report (08-13 spam PIN_FLAG) fired on `SEARCH_PINS`; its negative label/features live in the Search lineage and never reach homefeed retrieval/ranking. 8 of 10 negatives were ad flags, also off-homefeed; report carries no REPORT_WEIGHT in L2 utility → cannot demote at serving time.
3. **Positive/negative asymmetry:** positives (closeup ~0.09–0.10, repin ~0.047, share, at GENERAL weights SHARE 2000 / REPIN ~74–92) flow into the user representation and *generalize*; negatives suppress only the exact entity. One report kills one pin; similar pins survive. Positive interactions on later-reported pins are never scrubbed from training data.
4. **Nothing systematic in ranking/retrieval:** the 5 pins arrived via 5 different sources (MULTI_EMBEDDINGS, INSTANT_PFY, RECGPT ×2, REPIN_BOARD) with no shared rank profile (two p98–p99, rest deep-tail/demoted; the demoted one pulled down by its own HIDE_SCORE ~0.0033, ~75% above peers) → driver is the shared user-interaction signal, not any one CG or stage.

**Traps (plausible-but-wrong):** "denylist leaked" (it didn't); "ranker bug" (heads are working as designed); "report should have suppressed similar pins" (system never claimed to — exact-entity only); **"there's a report head in L2"** — one of James's agents claimed this; Michael's Claude-Code-built P13n ranking doc found none, and he was right (no REPORT_WEIGHT in utility). Live example of agents disagreeing on ground truth — the exact failure mode this eval dataset exists to catch ("my different AI Agents are telling me different things, and now they're arguing with each other" — James, in-thread). Blog-post color for the eval-harness piece.

**Outcome / next steps as posted (James's response, Situation/Findings/Next-Steps form):** (1) cross-surface negative feedback via **UPP** (ongoing — flagged as worth prioritizing in the UPP roadmap), (2) demotion experiments for borderline-quality content with **CQ team** (ongoing), (3) **Safe Journeys** working group follow-up on in-session/sequence-responsive approaches. **Public commitment: timeline follow-up next week.** As of Sat 8/22 am: no response yet from the VP, Dylan, or Andrew (posted late Fri — normal weekend latency, check Mon).

**Artifacts:** Selection View + Analysis View on scrimshaw (`…/pinsight/2026-08-12_2026-08-14_990229174226835247_{overview,analysis}.html`); stack doc above; Slack AI thread-summary credits "investigation led by @James Li" (VP-visible).

---

## Case #2–#5 — candidates (sketch, 8/22)

- **Dylan's irrelevant-pin case** (HF Pinkerton v0's first live case, ~May) — retrieval-side diagnosis.
- **CG sizer / quota-starvation case** (`cg_quota_analysis.md` — two-level budget divergence, e.g. UIC CLR 750 sizer vs 200 ANN cap) — config-vs-model confusion trap.
- **BMI / GULP logging case** (Alok's hookup) — instrumentation-gap diagnosis ⟨pick a concrete instance⟩.
- **A Notifications or Search full-funnel case** once task-1 logging lands ⟨placeholder — aligns dataset with the Q3 roadmap⟩.
- ⟨fifth: ideally a true positive — a real suppression/ranking bug, so the eval set isn't all "working as designed"⟩
