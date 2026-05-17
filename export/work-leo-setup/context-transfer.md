# Context Transfer: Leo → work-leo

> One-way payload of context updates from Leo to ship into work-leo. Append-only during Leo sessions; work-leo ingests and merges into its own context files, then this file gets archived.

**Session date:** 2026-04-11

---

## PINvestigator — post-Jeff demo next steps

### Diagnosis

Demoed PINvestigator to Jeff and his directs. ~10-minute slot. Body language was strong — clear "moment of recognition" in the room. But Jeff did not commit verbally to anything concrete after Manu (Sr Director, Data Science) interjected with "your team should follow my team — we're building something similar."

Stress-tested the silence reading against Wes Kao Frameworks + Coaching Patterns notebooks. Both converge:

- **Most likely cause is time + Manu interjection, not value miss.** 10 minutes is below the threshold for an exec to context-switch, absorb a tool, navigate a turf interjection, and commit publicly.
- **Comparison trap to flag:** Reading Jeff's silence as "demo lost steam" relative to Akaasha's earlier ralph-loop demo (which got more Jeff/Phil questions) is the *Status Sensor* firing. Akaasha's was research/exploration → invites curiosity. PINvestigator is a production tool → invites adoption decisions, not out-loud commitments. Different stage, not lower value.
- **Delivery lesson (one-time calibration):** Did not preempt the **MOO (Most Obvious Objection)** — Manu's overlap. Wes Kao framework: when an adjacent team's work is in the room, address it head-on in the opening so you control the frame instead of letting them set it.
- **Load-bearing fact often under-weighted:** Dylan strongly supports PINvestigator. She brokers upward to Jeff. The Status Chase wants Jeff's verbal nod; the operating reality is Dylan already has it.

### Five next steps (committed)

**1. Send Dylan a written follow-up using the OAV framework.** (Originally drafted for Jeff; swapped to Dylan to get her blessing and let her broker upward instead.)

   - **Observe:** "Following up on yesterday's PINvestigator demo. Jeff's directs were engaged; Manu flagged that his team is exploring adjacent work."
   - **Assert:** "I'm proposing a 2-week pilot on the next 3 recsys incidents to capture hard metrics on time-to-resolution and engineering hours saved. In parallel, I'll sync with Kareem (Manu's team) offline to deconflict and find consolidation opportunities. JJ is going to drive the eval harness expansion; I'll own the stakeholder layer and adoption metrics."
   - **Validate:** "Want your blessing to proceed — and if the metrics land where I expect, I'd like your help framing this with Jeff for broader rollout. Sound right?"

   **Why Dylan not Jeff:** Dylan is the manager-broker. She converts adoption into upward narrative more credibly than James can do directly. Asking Jeff for sign-off post-silence reads needy; asking Dylan for partnership reads strategic.

**2. Drive adoption metrics — that's the only signal that matters now.**

   Success = runs + hours saved (already named). Operationalize:
   - Lightweight telemetry on every PINvestigator invocation: timestamp, user, incident type, outcome
   - Target: **20+ runs across 3+ teams in 2 weeks**
   - Weekly summary line for Dylan's 1:1 and Jeff's follow-up thread

**3. Convert Manu's overlap into a Kareem partnership — not a competition.**

   Already in motion (James is engaging Kareem). Accelerate it. Offer PINvestigator to Kareem's team as a co-pilot. The moment Manu's org is *using* the tool, the overlap dissolves and Jeff has nothing to referee. This is also the *Observation-as-Contribution* pattern (Coaching Patterns / Dhruvil pattern): don't advocate for your tool, observe what's working from the practitioner seat.

   Related: Dylan shared a front-end DS tool from Manu's team for "integration possibilities." James's gut: not a front-end fit (PINvestigator is a Claude Code skill). **Reframe back to Dylan as: "Not a front-end fit, but I see an analytics-agent integration path. I'll scope it with Kareem and JJ."** Preserves the Dylan signal AND routes it through the actual technical fit.

**4. Delegate features to JJ aggressively.**

   JJ is contributing to PINvestigator while on PTO — strongest possible signal he wants this. Hand him:
   - Eval harness expansion (build on this week's 8 golden examples — 3 slow drift + 5 cliff incidents — landed this week)
   - New surface integrations
   - Better harnessing strategies

   **James keeps:** Adoption + stakeholder layer (Manu, Kareem, Dhruvil, Dylan, Jeff follow-up).

   **Why partition:** JJ gets a clean promo artifact for end-of-June with James as visible sponsor. James gets velocity without building himself into a corner. If the work merges, JJ's promo case gets muddy ("was this James's or JJ's?").

**5. Stop benchmarking PINvestigator's reception against Akaasha's demo.**

   That comparison is the Roberto-line tournament re-asserting itself. Yesterday's session named this explicitly: Roberto/Akaasha sit in the Kurchi-line dynamic, which is partly a proxy for Dylan-vs-Kurchi director-level positioning. Not a fair comp for James's Pinkerton/PINvestigator track. Different game, different scoreboard.

   *Impact Over Approval audit:* James's scoreboard is **adoption volume**, not exec question count.

### This week's PINvestigator wins (ship to work-leo's session log)

- 8 golden set examples generated (3 slow drift + 5 cliff incidents)
- Eval harness built and code landed
- Demo to Jeff + directs (despite ambiguous Jeff signal, Dylan support is strong)
- Dhruvil onboarded — actively wants to play with the tool
- Manu's team flagged interest (via Kareem partnership lane)

### Stakeholder additions for work-leo's `context/people/stakeholders.md`

- **Manu** — Senior Director, Data Science. New stakeholder. Said publicly "your team should follow my team — we're building something similar" during PINvestigator demo. Read as: legitimate adjacent work + competitive territorial signal. **Operating plan:** route through Kareem (manager under Manu) — turn overlap into partnership, not competition.
- **Kareem** — Manager under Manu. Already in motion as PINvestigator partnership lead. Critical unlock for Manu-org goodwill.
- **Dhruvil** — Active PINvestigator user (asked to play with the tool, James shared). Practitioner ally signal.

---

## Pinkerton — M0 in production + Reflex co-dev escalation

### Wins this week

- **Two PRs landed → Pinkerton M0 is in production.** James personally shipped both while running a full Sr EM job. New mode of work: EM-as-builder.
- **Chuxi committed 20% time going forward.** Excited specifically about the agentic recsys vision at the end of the roadmap. Covers the 2-week Alok PTO gap; James now has a code reviewer + collaborator beyond Alok.
- **Logging is done.** Minor hiccup: field names too long → some logging entries failed. **Daniel knows, fix shipping by Monday 2026-04-13.** Alok wrote a comprehensive verification plan; Daniel will execute.
- **Manual log verification on logs that did make it through → fields are present.** M1 unblocked.
- **Chuxi + James can build Pinkerton M1 in parallel** with the logging fix and full distribution verification. No serial blocker.
- **Dylan is bought into the vision.** Gave James debugging examples from herself **and Rajat** to test against. Dylan is now extending Pinkerton scope upward — wants the logging extended to **BMI (Board More Ideas)** surface. Dhruvil's team has a way forward on the BMI extension.

### Reflex × Pinkerton — the convergence (this is the strategic story)

Andrew Yaroshevsky built a working **Reflex prototype**. Reflex is an autonomous diagnostic agent that reads recsys signals and generates Trello cards proposing investigation hypotheses + opportunities. It's based on something Andrew calls the "**Anticipation vision**" (need clarification — see open questions below).

**What Reflex is already doing:**
- Generated a DS Agent Trello card on CG signal decay (followed CG, holdout-only, pinUIC replacement). After James + Dylan feedback, it reframed from "kill it" to (1) close holdout, (2) validate pinUIC against four failure modes from case studies, (3) updated impact sizing, (4) added "Experiment/holdout status check" to `quality_patterns.md` → DS Agent Phase 2.
- Generated a search relevance card flagging non-English market underperformance: 9.5B daily impressions, CJK 83% CTR gap, I18N MoE at 0% allocation. **Used VLM annotation as part of the analysis** — multimodal hypothesis generation in the loop.
- **Dylan's external validation to Andrew:** "it's great to see it's catching issues, and real ones, very promising."

**The escalation in the last 24 hours:**
- James told Andrew: "I think Reflex can be much more powerful if it can have access to the code directly + expert knowledge of where to look in the code."
- Andrew: "1000%. I was about to add the playbook of looking into the code to look for new hypotheses. We'll just need some expert feedback to provide for RLHF."
- **Andrew committed: "let me land the code in git before Tuesday and we can co-develop."**
- James also offered to point CC (Claude Code) at the HF CG codepaths + share the table of HF CG engagement rates so Reflex can join survey labels (relevance) with engagement results.
- Andrew is biased toward weighting engagement data over relevance going forward.

**The shape this is taking:**
- **Pinkerton** = the structured logging + observability data substrate
- **Reflex** = the autonomous hypothesis-generation agent that consumes signals and proposes diagnoses
- **James** = the expert-in-the-loop providing codepath knowledge + RLHF feedback + the bridge between the two systems
- **Dylan + Rajat** = upstream sponsors providing real debugging cases as test fixtures
- **Andrew** = primary builder of Reflex, ships before Tuesday 2026-04-14

This is the **agentic recsys vision from the Pinkerton roadmap unfolding faster than planned**, via Andrew's parallel build. Pinkerton is no longer a standalone observability play — it's the data layer for a multi-agent diagnostic system.

### Strategic notes from Leo

1. **Andrew's Tuesday code-drop is a real timer.** James needs to be ready to plug in that week. Reflex co-dev is a new commitment competing with: Pinkerton M1, BMI extension to Dhruvil's team, blog post #1, China trip prep, and the day job. Load management is the watchword.
2. **The "expert-in-the-loop / RLHF feedback" role is the highest-leverage seat James can occupy.** It's where his codepath knowledge + recsys judgment compounds. But it requires *consistent* presence — RLHF is not a one-shot input.
3. **Dylan brokered this and is now externally vouching to Andrew.** That's the bypass-lane signal from yesterday's session log materializing. Dylan-as-sponsor is becoming Dylan-as-co-architect.
4. **The "doing this while full-time EM" framing is celebratory, but it's also a tripwire.** This is the over-commitment pattern. Karen would flag this. The PR-shipping-while-managing-17 signal is powerful — but only if it's sustained without burnout or dropped balls elsewhere.
5. **Pinkerton M0 → production = James is shipping at IC velocity while at EM altitude.** That's the rare combo execs notice. Don't let the Andrew/Reflex excitement crowd out documenting and surfacing the M0 win itself.

### The Anticipation Vision (resolved)

- **Authors:** Andrew Yaroshevsky, Dylan Wang, **Mira** (Senior Director of Design — new stakeholder for work-leo's map)
- **Scope:** The vision for **all of 2026 personalization** at Pinterest
- **One-sentence frame:** "Pinterest should not just show you things you want, but anticipate what you might want next and show that to you instead."
- **Predicated on:** effective user interest exploration + knowing the user well enough to anticipate the *next* interest — the one that has not yet shown up in platform activity
- **The technical key:** **James + Anna's Retentive Recommendations project**. The vision authors explicitly recognize Retentive Recs as the architecture that makes Anticipation possible.
- **CTO-level surface area:** Andrew has **pitched the Anticipation Vision to Matt Madrigal (CTO of Pinterest).** Matt has subsequently talked about it **openly at a conference**, naming it as "one of the things he is most excited about for personalization and ML/AI at Pinterest." This means the vision has external CTO endorsement on the public record. The endorsement chain is: Mira (Sr Director, Design) + Dylan (James's manager) + Andrew (Dylan's peer) → authored vision → Andrew pitched to Matt → Matt amplified externally at a conference.

**Strategic implication:** Retentive Recs is no longer a project among James's projects. It is **the technical foundation for Pinterest's 2026 personalization vision**, with explicit recognition from a Sr Director of Design + James's manager + her peer + **CTO-level external amplification at a public conference**. This reframes nearly every other strategic call:

- Dylan's sustained sponsorship is not kindness — it is self-interest. She needs James to ship Retentive Recs for *her* vision to land.
- Andrew's Reflex co-dev invitation is not extra work — Reflex needs the Retentive Recs layer to function, so co-dev is the same strategic work surfaced via a new collaborator.
- Grabbing credit is structurally unnecessary — the architecture *is* the credit. James's name is on the vision via the technical foundation, regardless of doc authorship.
- **Blog post #1 (pretrain-finetune in recsys) and the Retentive Recs blog post are not "blog posts"** — they are the **executive narrative artifacts** for a vision that the CTO is publicly amplifying at conferences. They convert internal structural recognition into external articulation **at a moment when the gap between the vision's external visibility and the architect's external visibility is at its widest**. Karen's urgency on blog post #1 is no longer just a guardrail — it is structural risk management.
- **CTO-level visibility on a vision James is the technical key for is the kind of work that flips Director conversations** — but only if James is visible *inside* the narrative, not just present in the code that enables it.

### James's role decision on Reflex (resolved)

James explicitly chose **not to define a credit/role frame with Andrew before the Tuesday code drop**. Reasoning, as stated:

- Andrew is Dylan's peer; the Andrew/Dylan/James trio is exclusive
- Bringing a transactional credit conversation into a high-trust sponsor relationship would damage it
- Dylan has taken care of James so far; trust-extension is the right move
- Letting the work speak is the Coaching Patterns "Impact Over Approval" frame

**This is the right call given the relationship topology.** The "define your role before the code drop" framework Leo initially proposed applies to transactional relationships, not high-trust sponsor relationships. Trust-driven default is correct here.

### The wave-ride decision + tripwires

James acknowledged the time-crunch concern is real, but is consciously choosing to ride the excitement for now before tightening prioritization. Cost: paying less attention to routine project updates. Justification: team has shipped heavily over the past 2-3 weeks; a 2-week project-update lull is acceptable; team is stepping up more autonomously (which is itself the Director move).

**Tripwires installed (any one triggers a re-decision):**

1. **Team-drop signal** — Someone on James's team drops a ball James was supposed to catch and James doesn't notice for >24 hours. This is the actual test of the autonomy reframe vs. James's prediction of it.
2. **Dylan flag** — Dylan mentions a project gap in the next 1:1 (anything she expected to be moving that isn't).
3. **Pinkerton M1 two-week test** — If it's 2026-04-25 and Pinkerton M1 has not landed a meaningful milestone (not just code-merged but a real progress beat), the wave is crowding out the headline.
4. **Blog post #1 Monday test** — If James walks into Monday 2026-04-13 with blog post #1 still at zero, Karen's tripwire moves from +5 to +6 and Leo escalates to a sharper conversation.

### The 4-way nexus (corrected topology)

After checking James's stakeholders.md, the original "trio" framing was wrong. The actual structure is a **4-way nexus** that is structurally over-determined for trust:

- **Andrew Yaroshevsky** (Sr Director of Product) — author of Reflex two-pager + co-author of Anticipation Vision; pitched to Matt Madrigal (CTO) + Kartik (Chief Architect); invited James to co-own Detect + Diagnose engineering layers. **Anna's direct manager.**
- **Dylan Wang** (James's manager, Sr Director of Engineering, Homefeed Relevance) — co-author of Anticipation Vision; brokers James upward; provides debugging cases from herself + Rajat; expanding Pinkerton scope to BMI surface.
- **Anna** (PM partner for Retentive Recommendations, reports to Andrew) — James's "work bestie" and political amplifier inside Andrew's chain. DISC: Id (chaotic driver, High I + High D). Maximum psychological safety with James; relies on him as "Translator" from product instincts to engineering heuristics. **The bridge that holds the nexus together** — sells James sideways into Andrew's chain while Dylan sponsors upward.
- **James** — technical architect of Retentive Recommendations (the named foundation under Anticipation Vision). Now also Reflex co-developer.

**Why this matters:** there is no weak link. Dylan sponsors James up, Anna sells James sideways, Andrew co-owns the vision, James builds the architecture. The Anticipation Vision authorship reflects this: Andrew + Dylan + Mira (Design SD) wrote it; Anna + James are the operational foundation; the CTO is publicly amplifying the result.

**Mira (Sr Director of Design)** — third Anticipation Vision co-author. Cross-functional Design × Engineering × Product play. James's direct relationship with her is unclear and should be probed (mediated through Dylan/Andrew vs direct?). New stakeholder for work-leo's map.

### CTO-level surface area (corrected framing)

The CTO context is **not new** — Andrew was already pitching Reflex to Matt Madrigal and Kartik per James's existing stakeholders.md. What is new this week:

- **Matt Madrigal is now publicly amplifying the Anticipation Vision at conferences**, naming it as one of the things he is most excited about for Pinterest personalization and ML/AI.
- The Anticipation Vision frame (broader than Reflex) is now the umbrella narrative.
- Retentive Recs is explicitly named as the technical key under that umbrella.

This means James has been **operating inside a CTO-visible vision for weeks**, and the strategic stake on blog post #1 is not "react to a sudden jolt" — it is **steady-state structural risk management**: the gap between the vision's external velocity and James's external articulation widens every week the artifact does not ship.

### Open questions / context Leo still needs from James

1. **James's direct relationship with Mira (Sr Director, Design)?** First-name basis or formal? Has James met her on the Anticipation work directly, or is the connection mediated through Dylan/Andrew? Cross-functional play to track?
2. **What's the M1 scope for Pinkerton given the Reflex convergence?** Does M1 stay as originally planned, or pivot to feed Reflex as a first-class consumer?
3. **BMI extension owner?** Dylan asked for it; Dhruvil's team has a way forward — but who actually builds it? Chuxi? James? A Dhruvil-team engineer?

### Stakeholder updates for `context/people/stakeholders.md`

- **Chuxi** — Now committed 20% to Pinkerton going forward. Excited about agentic recsys vision. Critical Alok-PTO bridge.
- **Daniel** — Strong contractor on James's team. Owns Pinkerton logging fix, shipping Monday 2026-04-13. Will execute Alok's verification plan.
- **Andrew Yaroshevsky** — Reflex co-dev partnership formalized this week. Tuesday code drop. Pinterest-internal builder of Reflex prototype, biased toward engagement data over relevance signals.
- **Dylan Wang (update)** — Now actively brokering the Reflex × Pinkerton convergence, providing debugging cases from herself and Rajat as test fixtures, and externally vouching to Andrew that Reflex is "catching real issues." Has expanded Pinkerton scope to BMI surface. **Dylan has shifted from sponsor to co-architect on this lane.**

---

## Retentive Recommendations — UCAN WAU gain + Engineering Blog editor role + KDD paper

### Headline result (week of 2026-04-07)

**The program-level holdout is showing UCAN-stable WAU gains.** Global WAU gains across all regions are showing but **not yet stable** — do not broadcast globally; let the holdout mature.

This is the holy-grail signal that proves the entire Retentive Recs bet. WAU gains via ranking/CG experiments are historically rare in industry. Achieving this in UCAN justifies every architectural decision in Retentive Recs and converts internal architectural credibility into publicly defensible result-based credibility.

**Narrative rule for ALL artifacts (KDD paper, Engineering Blog, blog posts, interview answers):** Lead with the **UCAN-specific framing** — "holdout-validated WAU gain in our largest market." Specific, defensible, won't get retracted if global wobbles. The geographic qualifier adds rigor; do not generalize to "WAU gain" without qualifier.

### Status by workstream

| Workstream | Status |
|---|---|
| Program-level holdout | ✅ UCAN WAU stable; global WAU not yet stable |
| **Heuristic pUIC** | Live; mostly neutral overall; **positive for LFU (Low Frequency Users)** — retention gains may emerge over time |
| **Model-based serendipity prediction** | Strong offline results; online AB ~1 month out |
| **LLM-based pUIC** | Good qualitative prediction evaluations; no quantitative production data yet |
| **Front-end experiment integration** | Landing |
| **RL Feedback Loop / Geometric Bandit** | Offline eval design done; needs experiment results |

### Three prediction tracks (the spine of Anna's "claim 2")

1. **Heuristics** — fast-to-deploy, live, modest LFU gains. Empirical anchor.
2. **Model-based serendipity prediction** — strong offline results. "This will work at scale" claim.
3. **LLM-based prediction** — good qualitative evaluations. "This is where the field is going" claim.

The "predict next steps" novelty is no longer aspirational — three tracks at three evidence states. James can write Anna's claim 2 section today.

### KDD 2026 paper (July cycle, ADS track)

**James position:** "I'll take any authorship." Not fighting for first author. Sole-author of three sections (Prior Work, Architecture chapter lead, Future Work). **Armando + Anna are load-bearing for the paper** and James is consciously protecting their bandwidth.

| Section | Author |
|---|---|
| Background | Anna Kiyantseva |
| Prior Work | **James Li (sole)** |
| Architecture | **James Li (sole, chapter lead)** |
| → Representation | Armando Ordorica + Jiacong He (departing — likely absorbs into Armando) |
| → Prediction | Armando Ordorica + Yuke Yan (James will delegate sections to support Yuke's career — see Yuke entry in stakeholders.md) |
| → Federation | Armando Ordorica + Olafur Gudmundsson |
| Evaluation | Armando Ordorica |
| Future Work | **James Li (sole)** — "Using cluster-level features as a sequence?" |

**Anna's three novelty claims:** (1) representation inadequate for broad longitudinal movements → Board_create supervision; (2) **no ability to predict next steps — biggest open question, now substantiated by three prediction tracks**; (3) ability to evaluate categorical change vs point-wise change. All three move topline / WAU.

**Armando's framing notes (defense strategy):**
- Piggyback on OmniSage (different inputs; novel construction in new domain)
- Double down on predicting NOT at point-wise change
- Composite rewards + user-level Explore/Exploit + global SID
- Need offline analysis to avoid "throwing shit at the wall" framing
- Feedback Loop has good offline eval design; needs experiment results
- **PinnerSage offline results look really good** — insurance if live experiments don't fully bake by July 31

**Architecture-section defense gap:** James needs a one-paragraph "what's reused, what's novel, why the new construction is non-trivial" defense ready before draft v1. Don't let Armando be the only one who can answer this under reviewer pressure.

**Timeline:**
- End of April 2026 — soft draft + thoughts
- Beginning of May 2026 — next sync
- July 24, 2026 — abstract deadline (KDD ADS July cycle)
- July 31, 2026 — paper deadline
- Oct 4-18, 2026 — author rebuttal period
- Nov 23, 2026 — notification

**Key risk:** If Feedback Loop / Geometric Bandit experiment results don't land in time for July 31, paper slips → KDD slot lost → fall back to next cycle. PinnerSage offline results are the insurance.

**Setup:** Armando is setting up new repo + Cursor environment for the team.

### Pinterest Engineering Blog (high-leverage Director artifact)

**James will be recognized as the program lead in this artifact.** Externally-visible Pinterest Engineering Blog post publicly identifying James as leading Retentive Recommendations.

**Status (2026-04-11):**
- **Draft exists.** Jiacong He wrote a draft.
- **Jiacong is leaving the company** — on the blending team, minimal team retention impact, but the editor role is open.
- **James committed 2026-04-11 to take the editor role.** Reasoning: being recognized as program lead requires *being* the lead on the publication itself. Punting = losing the recognition by default.
- **Anna was hesitant** when James subtly floated her taking the role. Acceptable — Anna + Armando are load-bearing for KDD; Engineering Blog editing should not pull her off KDD.

**Why this is the highest-leverage 5-10 hours of work for the Director conversation:**
- Effort: editing existing draft + corralling cross-team engineers ~5-10 hours over 1-2 weeks (lower than writing from scratch)
- Leverage: externally-visible Pinterest Engineering Blog naming James Li as program lead on a project that just shipped UCAN-stable WAU gains, in a vision the CTO is publicly amplifying at conferences
- Counterfactual: if James doesn't take this, the framing drifts and the recognition does not appear by default

### Five committed next steps (Retentive Recs)

1. **Inherit Jiacong's Engineering Blog draft cleanly before his offboarding.** Critical handoff — losing the draft = losing the artifact. Get the file before he leaves; verify completeness; confirm transfer with him in writing.
2. **Take editor role: corral cross-team engineers for final edits.** James as program lead is the one with the authority to drive this. Cross-team coordination is the hard part. Insert the UCAN WAU headline as the lead.
3. **Lead with UCAN WAU framing in every artifact.** KDD paper abstract, Engineering Blog opener, blog posts, interview answers, internal updates. Specific, defensible, durable. **Do not broadcast global WAU gains until the holdout matures.**
4. **Soft draft of KDD paper sections (Prior Work, Architecture, Future Work) by end of April 2026.** ~2.5 weeks from now. Draft doesn't need to be polished — needs to exist for the early-May team sync.
5. **Delegate KDD Prediction subsections to Yuke as career-aligned investment.** Yuke is busy landing impact AND is a flight risk per stakeholders.md §8. A published-paper credit on his record before the end-of-year promo conversation is high-leverage retention work. Frame the delegation explicitly in those terms when you ask him.

### Anticipation Vision authorship (cross-reference)

The Anticipation Vision authors are **Andrew Yaroshevsky, Dylan Wang, and Mira (Senior Director, Design)**. James + Anna's Retentive Recommendations is the explicitly named technical key under this vision. Andrew has pitched it to **Matt Madrigal (CTO of Pinterest)**, who has subsequently amplified it openly at a conference as one of the things he is most excited about for Pinterest personalization. See the Pinkerton section of this transfer for the full Anticipation × Reflex context.

**Cross-cutting strategic point:** Pinkerton (data substrate) + Reflex (autonomous hypothesis generator) + Retentive Recs (the architecture that makes Anticipation possible) form a single integrated story. James is the technical key under all three. The narrative artifacts (Engineering Blog, KDD paper, blog post #1) convert this internal recognition into externally-defensible credit.

### Stakeholder additions for `context/people/stakeholders.md`

- **Armando Ordorica** — KDD paper operational engine. Owns Representation, Prediction, Federation, Evaluation subsections. Setting up new repo + Cursor for the team. Load-bearing peer; default is *let the work speak*.
- **Olafur Gudmundsson** — KDD paper Federation co-author with Armando. Limited information; light touch.
- **Jiacong He** — **Departing.** On blending team. Wrote the Engineering Blog draft James is inheriting. KDD Representation co-author (likely absorbs into Armando).
- **Yuke Yan (update)** — KDD Prediction co-author. James will delegate sections to support his career as part of retention work (Yuke is a flight risk; published-paper credit is career-aligned).
- **Anna (update)** — Hesitant about taking the Engineering Blog editor role when James floated it. Keep her on KDD Background section; do not pull her off KDD.

### Retentive Recs Feedback Loop update (added 2026-04-11)

**The RL Feedback Loop / Geometric Bandit work is nearing completion and about to start AB.** This materially de-risks the KDD paper timeline. Armando had flagged "feedback loop has good offline eval design, needs experiment results" as a key risk for July 31. With AB launch imminent (next 1-2 weeks), there is realistic runway to have real experiment data before the paper deadline. PinnerSage offline results remain the insurance layer.

**Operational implication:** The "key risk" on the KDD paper dropped from medium-high to low-medium this week. Paper drafting should proceed on the assumption that Feedback Loop AB data *will* be available for the July 31 submission, with PinnerSage as the fallback if AB launch slips.

---

## UPP — Hands-off operating mode + two near-term actions

### Headline

**UPP is running extremely smoothly across 4 of 5 prongs with momentum building — and James has not been involved in any execution work in the past 2 weeks.**

This is the strongest Director-readiness signal in James's entire portfolio. The biggest and highest-stakes project he owns is shipping without him. Operator → architect transition in its cleanest form. Every week UPP runs without James IS the Director case.

When James's portfolio gets audited (by Karen, by Dylan, by himself), UPP is the counter-example to the "James is still in operator mode" concern. Every other lane (Pinkerton M0 PRs, PINvestigator adoption, Reflex co-dev, Retentive Recs Engineering Blog editor role) is pulling James toward hands-on operator mode. UPP is the proof that he already operates at Director altitude on work he has cultivated to maturity. **This framing should be visible in stakeholder conversations about Director readiness.**

### Five-prong status (April 2026)

| Prong | Status | Key signal |
|---|---|---|
| **1. Cross-surface training** | Active, momentum building | Piyush + Zihao + Matthew Lawhorn (Ranking) + Jiaqing (P2P Retrieval). Cross-surface data loading PR landed. Early signs of success. |
| **2. Scaling up Base/HF CLR** | Active, launches in flight | Devin got launch approval for CLR GPU Serving, rolling out. Foundation Model in CLR promising (first few days of data). Devin + ATG landed CLR router simplification with good engagement gains. |
| **3. P2P architectural discussions + socialization** | Active, organizational momentum | Architectural design landed well with P2P Retrieval team + Jinfeng. **Sai (peer Sr EM, she/her) proactively committing more engineers** and asked James to add them to weekly coordination meetings. |
| **4. Notifications** | Active, **handoff approaching but NOT immediate** | Rui (Notif ML) stepping up on finetuning; collaborating with Hongtao (ATG). **v2 of Surface Tower experiment starting.** James needs to check in with Piyush on v1 outcome. Handoff conditional on v2 success. |
| **5. Finetuning HF/BMI specific models** | Not started, deferred | Bandwidth-gated. Fine to do later in Q2. No action required. |

**Adjacent:** UPP Ranking momentum also riding high.

### Operating stance

**Hands-off on execution. Lightweight visibility only.**
- Monday review of team updates is the minimum viable touch point. It's working — James knows every prong from memory.
- **Do not upgrade the touch point** unless a tripwire fires. Upgrading cues the team that James is re-entering the operator seat and they start deferring decisions back to him.
- **Do not re-engage "just because I have time."** If UPP needs James, UPP will signal it. The best thing he can do for UPP right now is protect its autonomy.

### Two near-term actions (next 1-2 weeks)

1. **Slack Sai directly.** She's proactively committing engineers and asked James to be in the loop. A 3-line DM costs nothing and reinforces the partnership. Template:
   > "Hey Sai — thanks for staffing more folks on the cross-surface effort. Added them to the weekly sync. Really appreciate how this is coming together. Let me know if you want a quick 15-min sync sometime to share where I see this heading."

2. **Check in with Piyush on Surface Tower v1.** Questions: What happened with v1? What's the thesis for v2? What does success look like that would unblock the Notif handoff? James needs this before he can give Dylan a clean "handoff imminent" signal.

### Five tripwires (any one fires → re-engage)

1. **Two-week stall on any active prong** (cross-surface training, Base/HF CLR scaling, or P2P architectural work).
2. **Dylan asks about UPP status in a 1:1 and James can't answer** — visibility degradation.
3. **Surface Tower v2 fails or stalls** — Notif handoff is conditional on v2 success.
4. **Prong 5 (HF/BMI fine-tuning) pushes past end of Q2 without anyone claiming it** — "fine for later" has an expiration date.
5. **A launched experiment (CLR GPU Serving, Foundation Model, router simplification) shows neutral/negative results** after initial rollout.

### Stakeholder additions for `context/people/stakeholders.md`

- **Sai** (peer Sr EM, P2P Retrieval, she/her) — Correcting earlier UPP log that listed her as "P2P IC, silent, following Jinfeng's lead." She is a **peer Sr EM**, likes Dylan + James, proactively committing resources. **Intel:** Has complained privately that Huizhong (her manager) is too controlling and too conservative about ML investment. Do not surface this to Huizhong/Jinfeng. The intel suggests Sai may see UPP as a vehicle for ML work Huizhong won't fund internally — incentive alignment with James.
- **Jiaxing Qu** (likely same as "Jiaqing" from verbal update — transliteration variation) — P2P Retrieval engineer, reports to Sai. **Co-author of the UBR (Unified Cross Surface Retrieval) design doc** with Piyush Maheshwari. Active on cross-surface training.
- **Dafang He** — Leading the new Search CLR workstream (UPP Prong 1). Guiding Devin, Sophia, and a UU team member on scoping. Also commenting on UBR design doc.
- **Zihao Chen** — Driving UPP Prong 2 (Cross-surface training / CFM unlock for Retrieval). Cross-surface data loading PR landed; initial model training started and seems to be working. Supported by Piyush + Hongtao + Jaewon.
- **Hongtao Lin** — ATG side, confirmed as **primary Notif FT driver — major Q2 project** per Zhenyu Tan. Already in historical UPP log.
- **Zhenyu Tan** — Notif ML side, likely manager; confirmed Hongtao's Q2 focus. Potential operational counterpart for the Notif handoff.
- **Rui** — Notif ML team IC, stepping up on finetuning work (parallel to Hongtao's ATG-side driving). Healthy handoff signal.
- **Dimitra** — James's Notif-side partner for the operational handoff. James plans to reach out to scope the April/May clean handoff milestone. Historical strategic ally from the March must-win ("UPP can evolve into the next generation of models").
- **Sophia** — IC on the Search CLR workstream under Dafang He.
- **Matthew Lawhorn** — Ranking side of cross-surface training partnership. Already in historical UPP log as "Matt Lawhon." No update needed.
- **Olafur Gudmundsson (upgrade)** — Already logged as KDD Federation co-author. **Upgrade:** he is also an **active reviewer on the UBR design doc** (commented 2026-04-03 asking for use-case outlines). His engagement spans both the KDD paper AND the UPP platform architecture — treat as "active cross-project collaborator," not "light touch KDD co-author."

### UBR (Unified Cross Surface Retrieval) — New technical reference

**Piyush Maheshwari + Jiaxing Qu** authored the UBR design doc (last updated 2026-04-05). Leo captured the full design into `work+self/projects/ubr_design.md` on 2026-04-11 from screenshots James shared. This is the **technical instantiation of UPP Prongs 1-3** and the operational realization of the pretrain-finetune paradigm at Pinterest.

**Key design points worth carrying to work-leo:**
- **Two-tower base model** (query tower + pin tower) with per-surface **Condition Towers** and per-surface **Surface Towers**, shared **User Tower** (conditioned user sequence transformer or context tokens or FM), final DHEN feature cross layer
- **Three progressive Model Adoption approaches** (Embedding Generation Module → User Tower Module → Full Model with feature adaption) representing increasing base-model reuse in surface FT
- **"Reserve dedicated model capacity for relevance"** as an explicit design principle — the operational answer to Kurchi's March must-win concern
- **Alternative ablation: unified transformer backbone** (OneTRANS / RankMixer / FM-as-backbone) replacing explicit feature crossing with attention-based global crossing
- **Fine-tuning uses data from the window after pre-training window** to prevent leakage
- **Per-surface recall@k evaluation metrics** (p2p_recall_k_query_pin_condition, etc.)
- **Loss:** Binary cross-entropy + in-batch negatives + optional relevance loss; open design question on per-surface vs joint IBN
- **AppConfigs proposal:** Combine CLR's flat single-surface config with CFM's two-layer pretrain/finetune pattern into a unified two-layer config

**Full technical detail in `work+self/projects/ubr_design.md`.** When the technical UPP context update James has deferred lands, cross-reference UBR design choices against the final architecture.



  1. RecGPT launched to Homefeed Production after a near-yearlong journey — now the #1 performing CG across all of
  Homefeed. Strong metric gains and deep trust built with ATG along the way. The roadmap ahead is exciting. Kudos to
  Bella and Hanlin for relentless iteration on this.

  2. Retentive Recs / Anticipation delivered across the full stack — from research to production to CTO visibility. The
  team shipped UIC x CLR, Frontier Sampling, and initial pUIC to support the Anticipation Cupcake Q1 sprint, plus built
  a feedback loop that will systematically tie into how Blending explores/exploits user interests and fresh content. The
   holdout is showing positive WAU impact, especially in UCAN. The CTO called out Anticipation as one of the projects
  he's most excited about at Pinterest for AI and Personalization. The team also delivered critical backend components
  on tight timelines to enable user-facing features. Kudos to Yuke, Chuxi, Yidi, Devin, and many Blending, UU, ATG, and
  XFN partners.

  3. UPP delivered one of the most celebrated Leads Reviews in recent memory — [Must Win March '26] UPP for Core. The
  team moved at exceptional speed: 3 LRs on Notifs, 2 on HF, including GPU Serving for CLR which unlocks significant
  scale going forward. The team also held down the fort on GULP debugging and scoped a strong HF/Base CLR roadmap. Kudos
   to Piyush, Sophia, Devin, Charlie, and ATG partners.

  4. LWS and L1 Utility delivered foundational wins in one of the toughest problem spaces we operate in. Unimpressed
  data, GPU serving rollout, Unified User Tower — all impressive feats given LWS's complexity. L1 Utility continued to
  prove its durability with additional wins, and the team made strong progress onboarding Shopping CGs to LWS and L1
  Utility. The team also helped unblock PinSelection V2 rollout — one of Content Quality's biggest wins in years —
  building strong cross-org relationships in the process. Kudos to Yali, Hedi, Zili, JJ, and David.

  5. The team became AI-first — on short notice, without top-down guidance. PINvestigator (agentic investigation tool),
  HF Full Funnel Logging for future AI work, and early foundations for AI-native recommendation workflows. All built
  bottoms-up by the team. Kudos to JJ, Alok, Zihao, and Daniel.

  ---
  Now here are 5 learns, forward-looking, Rajat altitude:

  1. Cross-org sprints (Anticipation Cupcake) force prioritization clarity that normal planning doesn't. The Cupcake
  model — tight scope, shared deadline, cross-team accountability — produced faster alignment than quarterly planning.
  Worth replicating for UPP surface expansion in Q2.
  2. AI-native tooling adoption works bottoms-up, not top-down. PINvestigator spread through organic use (Dylan,
  Dhruvil, Gigi) — not a mandate. The learn: invest in tools that solve an immediate pain point for one user, then let
  pull do the work. Top-down "AI transformation" programs produce slides, not adoption.
  3. GPU Serving was a long-overdue infrastructure unlock — moving earlier would have compounded. The gains from GPU
  Serving for CLR are immediate, but the constraint was sequencing priority against feature work. Infra investments that
   unblock multiple downstream teams should be treated as P0 earlier, even when feature pressure is high.
  4. Trust with partner teams (ATG, Blending, UU) compounds and should be treated as a durable asset. RecGPT, Retentive
  Recs, and UPP all accelerated because of trust built over prior quarters. The learn: protect these relationships
  during reorgs and priority shifts — they're load-bearing.
  5. Full funnel logging and evaluation infrastructure should precede, not follow, new product bets. The team is
  building HF Full Funnel Logging now in anticipation of future AI work. In hindsight, having this earlier would have
  accelerated iteration on RecGPT and pUIC. For Q2 bets (Reflex, Pinkerton M1), instrumentation goes in first.

1. System debuggability is our biggest gap — and we're now investing to close it.

Q1 exposed how much time we lose when we can't trace the full path from retrieval to what a user actually sees on screen. Debugging across the funnel — understanding why a specific user got a specific recommendation — is still too manual, too slow, and too fragmented across teams. We learned this the hard way through incidents and investigations that took days when they should have taken hours. We're closing this gap on two fronts: Full Funnel Logging gives us the instrumentation foundation — end-to-end visibility across the retrieval and ranking stack. And we're building agentic AI tooling (PINvestigator) on top of that foundation to automate the investigation itself — reading logs, building timelines, surfacing root causes. The logging makes debugging possible. The AI makes it fast. In Q2, Full Funnel Logging lands first, and we build the debugging workflows on top. The goal: any engineer on the team can answer "why did this user see this pin?" in minutes, not days.

2. Acting cross-surface: build unified first, diverge only when you must.

UPP's Q1 wins taught us that the feared tradeoffs between surfaces often aren't there — but you won't know unless you try. The team moved fast on cross-surface work (Notifs, HF, GPU Serving) and repeatedly found that a unified approach worked where we expected it to break. When we assumed surfaces would need divergent solutions and branched early, we created unnecessary parallel work. When we pushed toward universal solutions first, we got results that were better for everyone and faster to ship. The Q2 shift: default to building unified and universal. Push the shared architecture (Base CLR, shared User Tower, cross-surface pretraining) as far as it will go before branching into surface-specific solutions. The burden of proof should be on divergence, not on unity.

3. Anticipation Cupcake proved that cross-team sprints expose the highest-leverage integration gaps.

Cupcake was a forcing function — it made teams work closely together under a shared deadline and a tight scope. What it revealed wasn't just product wins (WAU-positive holdout, CTO excitement). It exposed which integration paths — unity integration paths between ML solutions and UX features, backend systems that bridge model outputs to user-facing components — disproportionately accelerate impact for all teams when they work. These aren't feature work. They're connective tissue. Before Cupcake, each team optimized their own layer. During Cupcake, we found the seams between layers where a small investment unblocked multiple teams at once. In Q2, we should identify and invest in these integration accelerators deliberately — not just when a sprint forces us to discover them.


  1. We're making system debuggability a Q2 infrastructure priority — cutting incident resolution from days to minutes.

  Our team loses too much time tracing issues across the retrieval-to-screen pipeline. In Q2, Full Funnel Logging lands first to give us end-to-end visibility, then we build agentic AI debugging (PINvestigator) on top to automate investigation workflows. The goal: any engineer
  answers "why did this user see this pin?" in minutes. This aligns with the broader org push toward AI-native engineering workflows — happy to sync on how this fits with Rajat's infra investment priorities.

  2. Unified-first is now our engineering default for cross-surface work. Burden of proof is on divergence.

  UPP's Q1 results proved that the feared tradeoffs between surfaces often aren't there. We shipped faster and got better results when we pushed toward universal solutions (Base CLR, shared User Tower, cross-surface pretraining) instead of branching early into surface-specific
  work. In Q2, every cross-surface decision starts unified — we only diverge when data forces it. This should accelerate Search and P2P onboarding significantly. If this conflicts with how other orgs are planning their surface-specific roadmaps, I want to know now.

  3. Anticipation Cupcake revealed the integration layers that disproportionately accelerate all teams — we're investing in those deliberately in Q2.

  The sprint exposed specific connective tissue — unity integration paths between ML and UX, backend systems bridging model outputs to user-facing components — where a small investment unblocked multiple teams at once. In Q2, we're identifying and funding these integration
  accelerators as explicit workstreams, not side effects of sprints. I'm partnering with Blending and UU to scope the top three. This maps to the same cross-team velocity Rajat is optimizing for — does this match his Q2 priorities or should I adjust the list?