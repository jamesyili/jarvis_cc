# Pinkerton

LLM-powered deep analysis tool for Homefeed recommendation systems — user understanding, request debugging, and aggregate insight generation. **Pinkerton is the data substrate for the Anticipation Vision via Reflex co-development with Andrew Yaroshevsky.**

Last Updated: 2026-05-14

## Sibling artifacts

- `pinkerton-agentic-vision.md` — forward vision, Reflex mapping, Phase 4 simulation bet
- `pinkerton-m1-spec.md` — M1 build spec
- `pinkerton-paper-summaries.md` — agentic recsys literature notes
- `strategic_next_steps_april.md` — Wes Kao / Shreyas / Ethan Evans / Coaching Patterns playbook, 8 scenarios + 22 aggressive moves + sequencing
- `bluf_memo_v0.md` — 2-page Pinkerton + Reflex memo for Dylan / Darren / Jeff (v0, FILL placeholders remain)
- `../context_instructions.md` — paste-ready prompt for work-leo to generate the Reflex agent's grounding `context.md`
- `jeff_demo_deck_2026-05-14.md` — Pinkerton joint cross-surface DSAT deck for Jeff (5–8 min, 7 slides, James opens then hands off)

---

## Headline (week of 2026-05-12)

- **Pinkerton — joint cross-surface DSAT diagnostic with Dimitra (Notifs) + Chuxi (HF).** Named 2026-05-14 (Dimitra owns naming). Pinkerton joins the HF Pinkerton v0 (used live on Dylan's irrelevant-pin case) with Dimitra's Notif v0 (used live in #notifications-feedback). Going to Jeff for a 5–8 min demo with a 1-FTE ask. James presents Slide 1 only (~45 sec opener); Dimitra carries Slides 2/3/4/6/7; Chuxi carries Slide 5 (HF demo). Deliberate Director-altitude move: James as convener, Chuxi gets VP-altitude exposure on the HF demo. Deck at `jeff_demo_deck_2026-05-14.md`. Open: Slide 6 diagram cleanup, dry run with Dimitra + Chuxi, pre-align 1-FTE ask with Dylan + Dimitra's manager before Jeff hears it, Chuxi prep 1:1.

## Headline (week of 2026-04-14)

- **Pinkerton demoed to Rajat (VP) on 2026-04-16.** Meeting with Dylan + Andrew Y present; Rajat asked about AI agents for debugging, James demoed Pinkerton. Rajat DM'd immediately after for the doc, then endorsed the fix-loop trajectory in Slack ("great! yea that would be a good one to prototype. and hook up e2e"). Rajat is now a VP-level stakeholder on Pinkerton and (adjacently) Reflex.
- **Andrew frame-capture residue.** In the Rajat meeting, both James and Andrew raised hands; James's turn came, demoed Pinkerton, which displaced Andrew's planned Reflex big-picture pitch. Andrew deferred with "I'll talk about the big picture later." James chose contribution-as-signal over verbal repair (ran CG context through Reflex with DS + PM bots, looped Andrew + Dylan on results). Political residue: Andrew's Reflex-framing with Rajat not yet reclaimed.
- **Dylan opened Reflex Build-stage scoping in 3-person DM on 2026-04-16.** Unprompted. Proposed sequencing: easy wins first (CG deprecation, utility tuning) → advanced (features-to-model, parameter searching). Asked about auto-PR once hypothesis lands. Same pattern as her RLHF self-insert yesterday: moving from sponsor to operational participant. Green-light to increase Reflex Build scope while respecting pacing commitment (Slack tempo, not substance).

## Headline (week of 2026-04-07)

- **M0 in production.** Two PRs landed this week. James personally shipped both while running a full Sr EM job (17 directs). New mode of work: EM-as-builder.
- **Logging done.** Daniel shipped it. Minor hiccup: field names too long → some logging entries failed. Daniel has the fix; ships Monday 2026-04-13. Alok wrote a comprehensive verification plan; Daniel will execute.
- **Manual log verification on logs that did make it through → fields are present.** M1 unblocked.
- **Chuxi committed 20% time going forward.** Excited specifically about the agentic recsys vision at the end of the roadmap. Covers the 2-week Alok PTO gap; James now has a code reviewer + collaborator beyond Alok.
- **Dylan extending Pinkerton scope to BMI (Board More Ideas) surface.** Dhruvil's team has a way forward. Owner TBD.
- **Reflex co-development formalized with Andrew.** Tuesday code drop. See "Reflex × Anticipation Vision" section below.

---

## What It Does

Pinkerton equips Homefeed (and eventually other surfaces) with automated, deep analysis of recommendation systems using LLMs/VLMs. Three capability layers:

1. **HF Request Debugger (M1)** — Given an employee ID + timestamp, fetch and diagnose a full Homefeed request across all 14 funnel stages. "What happened to this candidate at every step?"
2. **User Understanding Summary (M2)** — Given a user ID, generate a rich interest/intent profile using VLM analysis of engagement history. Evaluates how well the system understands the user.
3. **Scale Analysis (M3)** — Run Pinkerton at scale (hundreds of thousands of queries) to surface systematic patterns: relevance gaps by segment, content supply gaps, training data staleness, cross-surface quality differences.

## Strategic Context

### Reflex × Anticipation Vision (the umbrella story, updated 2026-04-11)

Pinkerton is no longer a standalone observability play. It is the **structured data substrate for Pinterest's 2026 personalization vision**, via co-development with Andrew Yaroshevsky's Reflex.

**The Anticipation Vision:**
- **Authors:** Andrew Yaroshevsky (Sr Director, Product), Dylan Wang (James's manager, Sr Director, Engineering), **Mira (Sr Director, Design)**
- **Scope:** The vision for **all of 2026 personalization** at Pinterest
- **One-sentence frame:** "Pinterest should not just show you things you want, but anticipate what you might want next and show that to you instead."
- **Predicated on:** effective user interest exploration + knowing the user well enough to anticipate the *next* interest — the one that has not yet shown up in platform activity
- **The technical key:** **Retentive Recommendations (James + Anna)**. The vision authors explicitly recognize Retentive Recs as the architecture that makes Anticipation possible.
- **CTO-level surface area:** Andrew has pitched the Anticipation Vision to **Matt Madrigal (CTO of Pinterest)**. Matt has subsequently talked about it **openly at a conference**, naming it as one of the things he is most excited about for personalization and ML/AI at Pinterest. Endorsement chain: Mira + Dylan + Andrew → authored vision → Andrew pitched to Matt → Matt amplified externally.

**Reflex (Andrew's prototype, escalation this week):**
- Andrew built a working Reflex prototype. Reflex is an autonomous diagnostic agent that reads recsys signals and generates Trello cards proposing investigation hypotheses + opportunities. Already in production across two cards:
  - **DS Agent CG signal decay card.** Reframed after James + Dylan feedback from "kill it" to (1) close holdout, (2) validate pinUIC against four failure modes from case studies, (3) updated impact sizing, (4) added "Experiment/holdout status check" to `quality_patterns.md` → DS Agent Phase 2.
  - **Search relevance card.** Flagged non-English market underperformance: 9.5B daily impressions, CJK 83% CTR gap, I18N MoE at 0% allocation. **Used VLM annotation as part of the analysis** — multimodal hypothesis generation in the loop.
- **Dylan's external validation to Andrew:** "it's great to see it's catching issues, and real ones, very promising."
- **Andrew committed: "let me land the code in git before Tuesday and we can co-develop."** James offered to point CC (Claude Code) at the HF CG codepaths + share the table of HF CG engagement rates so Reflex can join survey labels (relevance) with engagement results. Andrew is biased toward weighting engagement data over relevance going forward.

**The shape this is taking:**
- **Pinkerton** = the structured logging + observability data substrate
- **Reflex** = the autonomous hypothesis-generation agent that consumes signals and proposes diagnoses
- **James** = the expert-in-the-loop providing codepath knowledge + RLHF feedback + the bridge between the two systems
- **Dylan + Rajat** = upstream sponsors providing real debugging cases as test fixtures (Dylan has been giving James debugging examples from herself **and Rajat** to test against)
- **Andrew** = primary builder of Reflex; ships before Tuesday 2026-04-14
- **Anna** (PM partner for Retentive Recs, Andrew's report) = political amplifier inside Andrew's chain — the bridge that holds the 4-way nexus together

The Reflex pipeline (updated mapping):
1. **Detect** where experience is failing → PINvestigator + Pinkerton M3 + Reflex autonomous scan
2. **Diagnose** likely causes → Pinkerton M1 + M2 + Reflex hypothesis generation
3. Design interventions → (future)
4. Verify → (future)
5. Experiment → (future)
6. Explain results → Pinkerton + PINvestigator reporting
7. Roll out → (future)

### The 4-way nexus (relationship topology)

Trust on this lane is structurally over-determined. There is no weak link:

- **Andrew Yaroshevsky** authored Reflex two-pager + co-author of Anticipation Vision; pitched to Matt Madrigal (CTO) + Kartik (Chief Architect); Anna's direct manager.
- **Dylan Wang** (James's manager) co-author of Anticipation Vision; brokers James upward; provides real debugging cases.
- **Anna** (PM partner for Retentive Recs, reports to Andrew) — James's "work bestie" and political amplifier inside Andrew's chain.
- **James** technical architect of Retentive Recommendations + now Reflex co-developer.

Dylan sponsors James up, Anna sells James sideways into Andrew's chain, Andrew co-owns the vision, James builds the architecture. The Anticipation Vision authorship reflects this: Andrew + Dylan + Mira wrote it; Anna + James are the operational foundation; the CTO is publicly amplifying the result.

**Credit framing decision (2026-04-11):** James explicitly chose **not** to define a credit/role frame with Andrew before the Tuesday code drop. Reasoning: bringing a transactional credit conversation into a high-trust sponsor relationship would damage it. Default is *let the work speak* (Coaching Patterns "Impact Over Approval" + Dhruvil pattern of Observation-as-Contribution). The architecture is the credit.

### Roberto / Search Dynamic (deprioritized)

Roberto (Sr. EM, Search) built a similar funnel debugging tool on Search logs using Claude Code. Jeff highlighted it to the entire org earlier in Q1. Original framing: ship Pinkerton M1 for parity. **This framing is now obsolete** — Pinkerton has moved past parity into the Reflex × Anticipation Vision co-development lane, which Roberto is not in. Roberto sits in the Kurchi-line dynamic; James's lane is the Dylan/Andrew/Mira/Anna nexus. Different game. Connect with Roberto as peers if natural; do not chase parity comparisons.

## Data Substrate

### Full Funnel Logging (14 stages)
James's team built comprehensive request tracing for HF. Alok completing by April 4, 2026.

| Stage | What's Logged |
|-------|--------------|
| AT_REQUEST_ENTRY | User context, request params |
| AFTER_SIZER_CALCULATION | Sizer values |
| AFTER_RESOURCE_FETCHING | Signal values |
| AFTER_CANDIDATE_GENERATION | Candidates + metadata |
| AFTER_PRERANKING_FILTERING | Surviving candidates + LWS signals |
| AFTER_LWS | Per-head LWS scores |
| AFTER_L1_UTILITY | L1 utility scores |
| AFTER_RANKING_BATCHING | Batch size/metadata + ranking signals |
| AFTER_RANKING | Per-head ranking scores |
| AFTER_POST_RANKING_FILTERING | Candidates + filter attribution |
| AFTER_PRESORTING | Utility scores + SSD signals |
| AFTER_SSD | SSD scores + metadata |
| FINAL_CHUNK | Final candidate set returned |

**Gap:** More Ideas surface not included in logging. Extension needed if relevance fire continues.

## Q2 2026 Milestones

### M0: Foundational Pinkerton skill + structured logging (✅ shipped this week)
- **Status:** **In production as of week of 2026-04-07.** Two PRs landed (James personally shipped both).
- **Logging:** Done by Daniel. Field-name-too-long hiccup → Daniel fix shipping Monday 2026-04-13. Alok wrote the verification plan; Daniel will execute. Manual verification on logs that did make it through confirms fields are present.
- **M1 unblocked.** Chuxi + James can build M1 in parallel with the logging fix and full distribution verification.

### M1: HF Request Debugger (Active — building 2026-04-13 onward)
- **What:** Employee ID + timestamp → full funnel trace + LLM-powered diagnosis
- **Owner:** James + Chuxi (parallel), Alok extends after PTO return
- **Open question:** Does M1 stay scoped as originally planned, or pivot to feed Reflex as a first-class consumer? Decide after Andrew's Tuesday code drop reveals what Reflex needs from Pinkerton.

### M2: User Understanding Summary (Target: late Q2)
- **What:** User ID → VLM-powered interest/intent profile from engagement history
- **Why it matters:**
  - Evaluates UIC model for Retentive Recs (Goal 1 tie-in)
  - Tests VLM capabilities for understanding user history
  - Differentiated — no one else building this
- **Owner:** James architects, handoff TBD

### M3: Scale Analysis (Target: late Q2 / stretch)
- **What:** Run Pinkerton hundreds of thousands of times, aggregate for systematic insights
- **Use cases:**
  - Systematic relevance gaps by user segment
  - Content supply gaps for high-intent users
  - Training data staleness signals
  - Cross-surface quality comparison
  - UIC validation at scale (does the model see what the LLM sees?)
- **Owner:** TBD
- **Constraint:** Cost management for LLM calls at scale

## Origin

Summer 2025 hackathon prototype. Original team included Alok (motivated, still invested). Vision: LLM-powered understanding of users and recommendations — going beyond internal data to incorporate "world knowledge" for richer insights.

Original Pinkerton vision included:
- Helix-powered user understanding using LLMs for semantic/world knowledge
- User journey mapping (enticed → activated → stabilized → retired)
- Future external data integration (e.g., Gmail with consent)
- Smart efficiency via representative sampling for LLM analysis

## Staffing

| Person | Role | Notes |
|--------|------|-------|
| James | Architect / M0 builder / M1 co-builder / Reflex co-dev | Personally shipped 2 PRs to land M0 in production this week. EM-as-builder mode. Exit criteria TBD after M1 ships. |
| **Chuxi** | **20% Pinkerton commit going forward (new 2026-04-11)** | **Commits 20% time to Pinkerton.** Excited about agentic recsys vision. Critical Alok-PTO bridge — covers 2 weeks. Code reviewer + collaborator beyond Alok. |
| **Daniel** | **Logging owner (new 2026-04-11)** | **Strong contractor on James's team.** Owns Pinkerton logging implementation. Field-name fix shipping Monday 2026-04-13. Will execute Alok's verification plan. |
| Alok | Logging spec → DT → extends Pinkerton later | Original hackathon team. Out 2 weeks (PTO). Wrote comprehensive verification plan before going out. |
| Darren's eval DS | Eval framework | Via partnership with Darren's infra team. |
| Darren's team (TBD — 2026-04-09 commit) | Additional contributors | Darren read the Pinkerton proposal overnight 2026-04-08, loved it. Expect confirmation on/after Darren's Director promo 2026-04-16. |

## Partnerships

| Partner | What they bring | Play |
|---------|----------------|------|
| **Darren Regers** (Sr. EM → Director, Infra — promo official 2026-04-16) | Eval DS, **actively staffing Pinkerton contributors from his team as of 2026-04-09**, Director-track sponsor for James | **Deepened 2026-04-09.** Read + loves proposal. Searching his team for contributors ("Dylan" on his team OR Analytics Agent folks). Give milestones, get DS + contributors committed. Send congrats on promo day 4/16. |
| **Brian Lee** (Activation/Growth) | Weekly AI forum, front-end tooling | Use forum for visibility/demos. Don't force engineering collab. |
| **Kent** (Core Serving Infra) | System log debugging | Pass. Different domain, manager may leave. |
| **Roberto** (Sr. EM, Search) | Search equivalent tool, Jeff's attention | Wait until M1 ships, then peer-to-peer shared platform conversation. |

## Positioning

### With Dylan (Friday 1:1)
"Andrew shared his Reflex vision and invited me to co-own the sensing layer — Detect and Diagnose. It maps directly to PINvestigator and Pinkerton, and ties into Retentive Recs through UIC evaluation. Darren's team is contributing eval support. I'd love your take — any landmines? And I want to keep you in the loop given your AI interest."

### With Jeff
PINvestigator demo first (next bi-weekly). Pinkerton M1 demo next. Each builds the story incrementally.

### With Andrew
Name added to Reflex doc. Co-owning Detect + Diagnose layers. Wait for his CTO pitch outcome, then align on next steps with Kartik.

## Success Criteria (End of Q2)
- Pinkerton M1 shipped and used for real HF debugging
- Pinkerton M2 working prototype tied to UIC eval
- Darren's eval DS actively contributing
- Andrew has pitched CTO on Reflex; James named on Detect + Diagnose
- Dylan sees AI work as strategic, not a side project

## Open Items

- **BMI (Board More Ideas) extension owner.** Dylan asked for the logging extension to BMI. Dhruvil's team has a way forward — but who actually builds it? Chuxi? James? A Dhruvil-team engineer? Needs an owner before it becomes invisible WIP.
- **M1 scope under Reflex convergence.** Decide after Andrew's Tuesday code drop whether M1 stays as originally planned or pivots to feed Reflex as a first-class consumer.
- **James's direct relationship with Mira (Sr Director, Design)?** Mira co-authored the Anticipation Vision but James's direct line to her is unclear. Mediated through Dylan/Andrew? Worth a direct touchpoint?
- **Handoff criteria for Pinkerton** — when does James stop being TL? (Resolve after M1 ships)
- **Alok's milestone doc** — compare with James's milestones and align when Alok returns from PTO
- **Roberto parity work** — deprioritized; do not chase

## Wave-ride decision + tripwires (2026-04-11)

James acknowledged the time-crunch concern is real but consciously chose to **ride the excitement** for now before tightening prioritization. Cost: paying less attention to routine project updates. Justification: team has shipped heavily over the past 2-3 weeks; a 2-week project-update lull is acceptable; team is stepping up more autonomously (which is itself the Director move — operator → architect).

**Tripwires (any one fires → re-decide):**

1. **Team-drop signal:** Someone on James's team drops a ball James was supposed to catch and James doesn't notice for >24 hours. The actual test of the autonomy reframe vs James's prediction of it.
2. **Dylan flag:** Dylan mentions a project gap in the next 1:1 (anything she expected to be moving that isn't).
3. **Pinkerton M1 two-week test:** If it's 2026-04-25 and Pinkerton M1 has not landed a meaningful milestone, the wave is crowding out the headline.
4. **Blog post #1 Monday test:** If James walks into Monday 2026-04-13 with blog post #1 still at zero, Karen's tripwire moves from +5 to +6 and Leo escalates.

## 2026-08-01 — Status: folding into Reflex (deliberate)

James (8/1): Pinkerton work has stalled — and that's acceptable, because the plan is now to **fold it into Reflex** and concentrate attention there. One narrative, one funding story; Pinkerton's DSAT/deep-analysis substance becomes Detect/Prove content inside Reflex rather than a separately defended program. This file stays as the historical record; forward state lives in the Reflex program docs.
