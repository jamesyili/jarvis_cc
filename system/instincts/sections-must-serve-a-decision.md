---
id: sections-must-serve-a-decision
trigger: Drafting or revising a work-facing technical doc for James — design doc, doctrine, strategy memo, anything with an expert audience
behavior: Every section must change what someone does. Before writing a framing, taxonomy, or formalism section, name the downstream recommendation that depends on it; if nothing does, cut it. Specifically — (1) no scene-setting thesis or "why this matters" sections, they read as pompous to an expert audience that already agrees; (2) no definition or taxonomy that isn't consumed later in the doc; (3) no derivation whose result no action uses, however elegant; (4) a "bets" / "recommendations" section must contain real decisions, not restatements of mechanisms already argued above. (5) **price every option you present** — a doc that argues positions without stating what each one costs cannot be used to decide anything, and "surface the tradeoffs" is usually the literal ask; (6) do not invent a category that duplicates one already in the doc. When James asks "does this add anything?", the honest answer is usually no — check whether the doc's own action items depend on it before defending it. **Standing check before delivering any doc: re-read the ask it quotes in its own opening, and confirm the doc does that thing.**
confidence: 0.45
evidence_count: 2
created: 2026-08-14
last_updated: 2026-08-14
status: active
---

## Evidence

### 2026-08-14 (Safe Journeys placement doctrine) — four cuts in one session, all Leo-authored padding

James edited a Leo-drafted technical doctrine across five revisions and cut four Leo-added sections. The pattern is one pattern, not four incidents:

1. **§1.1, the objective-vs-subjective content quality framing** — *"Remove section 1.1. The whole section is unnecessary for this audience."* Leo had written a conceptual distinction for readers (a VP who chairs KDD, a Sr EM who owns the signal stack) who did not need it explained.
2. **§2, a five-line thesis statement** — *"Remove the current section 2. It's too pompous."* It restated the doc's argument before making it.
3. **The entire log-odds severity formulation** — *"kinda confusing to be honest. I'm not sure I understand it and I don't think it adds anything. Does it?"* On honest review: **no bet in the doc depended on it**, the simpler `ρ` (density in a score band) already did the job, and the correct engineering answer for the stated problem (a cheap USR surrogate) was to distill the LLM judge, not to hand-derive an analytic form. Leo had over-invested because it was the most satisfying part to write.
4. **All three "First bets"** — *"Remove the first bets section, these are all terrible."* They were restatements of mechanisms already argued in the body (run SSD diversity, run density control, do the calibration), not decisions with a cost, an owner, or a falsifiable outcome.

**The test that would have caught all four:** does any downstream recommendation change if this section is deleted? For all four, no.

Signal: correction ×4.

### 2026-08-14 (same doc, later) — the doc quoted its own ask and then did not do it

> James: *"go through all of section four and five and provide all the trade-offs of the different options in each subsection because that's one thing that we're missing right now."*

The doctrine's opening paragraph quotes Michael's ask verbatim — *"a tech design that is scalable across surfaces and parts of the stack, **and surface the tradeoffs**"* — and then argued a position in every subsection without pricing a single alternative. Nine tradeoff tables had to be added afterwards. Once written, they contained the most useful content in the document: that OR triggers pay for washout protection in false positives, that probabilistic sampling is indefensible to policy for violative content, that the trajectory head is the least certain item in the doc, and that building on the anticipation substrate couples a safety-critical system to another team's roadmap. **None of that could have been said by a doc that only argued for its own conclusions.**

Same session, same underlying defect as the four cuts above: Leo optimizes for the argument being right rather than for the reader being able to choose. Related smaller instance in the same doc — "regrettable engagement" was added as a third metric when it was the complement of one already present (collateral damage); the useful move was to name the positive quantity, **unregrettable engagement**, as the unit the existing metric is denominated in.

Signal: correction.
