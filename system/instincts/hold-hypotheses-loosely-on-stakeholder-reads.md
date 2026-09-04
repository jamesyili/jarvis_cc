---
id: hold-hypotheses-loosely-on-stakeholder-reads
trigger: When reading stakeholder dynamics, org-design intent, or "what is X thinking" questions where Leo is tempted to synthesize a clean unifying narrative from limited evidence
behavior: Hold multiple variants live as long as possible. Do NOT collapse to "this is the read" / "the story is" / "the narrative is X." Use phrases like "one read, alongside [X] and [Y]" / "if this lands, then" / "what would need to be true for variant N to be wrong?" Let James be the one to declare convergence — Leo's job is to keep the variants live and the evidence honest.
confidence: 0.95
evidence_count: 7
created: 2026-05-20
last_updated: 2026-09-04
status: active
---

> **Extension (2026-09-01): work-side thread reads.** When James asks for a "brutal read" on a Slack thread or an operational situation (oncall, pagers, cross-team ownership), the operational detail is *systematically invisible* to personal Leo — the same blind spot the CLAUDE.md Karen rule names. Before delivering the verdict: (1) say which parts of the read rest on repo-only context (one line in `goals.md` ≠ pager-level knowledge), (2) hold the operational recommendation as a question to James ("what's the actual pager split?") rather than a plan, (3) give the confident read only on what the transcript itself shows (who drove, who deferred, what got decided). The confidence budget goes to the interpersonal read, not the mechanics.

## Evidence

### 2026-05-19 (Yan-UX-consolidation hypothesis)
> "Take it easy a little bit, maybe not make such drastic jumps every time."

Context: During Dylan team-design grill-with-docs session, Leo mapped Dylan's org against the H1 career convo signals and wrote: *"This is the read. The 5/15 intel and the 5/19 convo are two sides of the same coin — Dylan is restructuring her org around the AI-leveraged-leader pattern with James as the consolidation point."* James pushed back — synthesis was too clean too fast. Memory saved: `feedback_hold_hypotheses_loosely.md`. The instinct is the behavioral pattern; the memory is the rule.

Signal: correction.

### 2026-05-20 (LWS+Blending V1/V2/V3 over-analysis)
> "I think you're reading too much into it, so let's back up a little bit and just note these two variables."

Context: When James surfaced LWS and Blending as two additional variables to consider in the org-design space, Leo built out a full V1/V2/V3 deep analysis treating Rahul as a Director-track candidate (Rahul is L16, sub-EM altitude — Leo didn't know this initially). James corrected: just note as variables, don't solve them deeply. Memory updated: `project_team_member_levels.md` captures L-levels for disambiguation.

Signal: correction. Reinforces the pattern: when James says "consider this" or "these are variables to think through," that's invitation to hold, not solve. Solving feels productive but is over-extension.

### 2026-06-23 (OpenAI Reid HM prep — assumed Reid was briefed)

> "I think you might be anchoring too much that Reid has gotten info from Coralynn. What if he hasn't?"

Context: Building the Reid HM prep doc, Leo built the entire opener and framing on the assumption that Reid would "walk in pre-loaded with what you established on the May 27 call" — collapsing a stakeholder's *knowledge state* to a clean assumption from a doubly-conditional handoff ("I'm happy to share... if he's interested"). James caught it. Fix: calibrate-first opener (a one-liner that reads how briefed Reid is) + two loaded versions (cold / briefed) instead of betting on one.

Signal: correction. Extends the pattern beyond org-design reads to *any* stakeholder-state assumption — "what does X already know / will X have done Y" is a hypothesis to hold loosely and design around, not a fact to build on.

### 2026-06-30 (Bella-stays session — twice built on an inferred motive over the stated one)

Two misses in one session, same shape: Leo constructed a strategic theory of a stakeholder's motive and built load-bearing recommendations on it *before* anchoring on the literal stated reason.
1. **ER "Dylan-directed":** team_members.md coded the Bella ER ticket as "Dylan-directed," and Leo built a whole "reconciliation-with-Dylan" risk thread on it (Dylan holds an expectation; the reversal reads as a wobble). James corrected: the ER was *never* Dylan-directed for Bella — Dylan has zero knowledge of the case. The thread collapsed.
2. **Bella's Option-2 objection:** Leo elevated it to an "agentic-proximity / retention-risk" theory and called it "the variable that decides 1-vs-2." James corrected: it's *manager continuity* — she keeps 30% Reflex, so the agentic worry was moot.

Leo named the pattern to James in-session ("that's twice I've inferred a strategic motive where the real one was more human — I'll anchor harder on what she actually said"). Fix/extension: **lead with the stakeholder's literal stated reason; treat any inferred motive — and any load-bearing context-file "fact" about intent — as a held hypothesis to verify with James before building recommendations on it**, especially fast on sensitive intel where the elegant theory is seductive. Ties to `check-existing-context-before-analyzing` (verify load-bearing facts) + the CLAUDE.md Karen blind-spot rule (ask first, don't infer).

Signal: correction (×2, self-named).

### 2026-09-01 (Unity Board — confident operational plan from one goals.md line)

> "You're too confident sometimes. I think you're missing a lot of context around Unity Board so let me fill you in."

Context: James asked for an "honest and brutal read" on the David Woo / Dhruvil / Bella oncall DM thread. Leo delivered the interpersonal read (fair) and then a confident Unity-Board recommendation built off a single line in `goals.md`, with no knowledge of the pager split, Yan's team's post-layoff overload, or that James's real concern is *which pagers* enter his CG rotation vs. a separate James↔Yan loop. Leo also proposed IC-altitude next steps David Woo was already driving (→ `next-steps-at-sponsor-altitude-when-a-driver-exists`). Fix applied to the read in-session; the extension at the top of this file is the standing rule: name the repo-only parts before the verdict, ask for the operational detail, spend confidence on what the transcript shows.

Signal: correction.

Related to `execute-after-decision-signal.md` (drop rejected sub-proposals silently) but distinct: this fires in *analysis* contexts, not *decision* contexts. The hazard is synthetic-narrative-overfit, not refusing-to-execute. Cross-ref `feedback_hold_hypotheses_loosely.md` memory.

### 2026-09-03 (the hedged Dylan read that was right)
Context: Leo's read of the subject-less DM was stated as a read with its residual named — "I can't see her face or her afternoon; 'show you something' could still be hard news that isn't about you, like a pull on your people for the Code Red. Carry that in as a possibility, not a worry" — and ranked candidates rather than asserting one. The reply (Search Code Red experiments, a read-in) matched the top candidate. James did not push back at any point and the hedge cost nothing. Now at the 0.95 cap → promotion candidate.
Signal: confirmation.

### 2026-09-04 (the backfill premise — a ⟨confirm⟩-flagged fragment upgraded to a fact)
> "On the backfill" (+ the Amanda screenshot: "the current hope/expectation is that you will receive a backfill in these cases")

Context: Recommending the mutual-separation path for Zili, Leo wrote *"the seat is not backfillable under the freeze either way"* as a load-bearing reason — sourced from Dylan's blurred 9/3 fragment ("I believe not"), which the record itself carried with a ⟨confirm⟩ and a "ping Amanda" action. Amanda had answered that morning, the other way. James corrected with two words and a screenshot. Fix applied in-session (correction stated, the Dylan note re-drafted) and on record (T2 #11, Dylan archive 9/4). **Rule:** a record item marked ⟨confirm⟩ / ⟨unconfirmed⟩ / "likely" keeps that flag when it enters advice — say "unconfirmed, cheap check = X," never promote it to a premise because the argument wants it. The blind-spot rule in CLAUDE.md (work-side activity is invisible) applies to facts that may have changed since the last log, not just to behavioral narratives.

Signal: correction.

**Same day, second instance (9/4, close):** James said "Rohul about the cost report"; Leo grepped, found the record's only Rahul (Goutam, Blending), and filed him as the cost-report owner in two files. James: *"Rahul is an EM on Core Serving Infra."* A name match in the record is a candidate identity, not an identity — say "the record's only Rahul is X; is that him?" before filing. Signal: correction.

