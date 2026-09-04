# stakeholders.md  
Last Updated: 2026-04-18  
---  
  
# Stakeholders & Dynamics  
  
## Purpose  
This file captures the *state I don’t want to repeat* about key stakeholders: trust, incentives, communication preferences, historical interactions, risks, and my operating plan.  
  
## Leo operating technique — theory-of-mind reads

When James asks what a stakeholder is thinking ("what is Dylan thinking about me?", "how is Rajat reading this?", "what's Andrew's real view?"), default to **multi-variant synthesis**, not a single best guess:

1. **Split by dimension** if the question is compound (what she thinks about me *and* what she thinks about the ask = two dimension lists).
2. **3-5 named variants per dimension.** Each variant: sharp label, 2-4 sentences of the read, one evidence line grounding it in the record.
3. **Weight the variants** most-to-least likely given available data. Be honest about why.
4. **Close with "what to do with the uncertainty"** — prep moves robust across variants so James's action doesn't depend on which read is correct.

Why this works for James: prevents his status sensor from locking onto the anxious variant as truth; forces honest theory-of-mind over flattering or catastrophic mono-reads; converts uncertainty into action. Confirmed load-bearing 2026-04-21 during Dylan career-conversation prep.

Don't hedge variants into mush. Don't skip evidence. Don't end without the robust-prep synthesis.

## Quick map (current)  

### Inner Circle (high trust, high leverage)
- **Dylan (Sr. Director, Homefeed Relevance)** — primary evaluator + scope allocator + AI guide relationship. Peak trust.
- **Anna (PM partner for Retentive Recommendations)** — co-owns product narrative; inner circle ally.
- **Dhruvil (Peer Sr EM, Homefeed Ranking)** — peer coalition partner; emotional/strategic ally.
- **Darren Regers (Director, Infrastructure — promo official 2026-04-16)** — primary AI partnership; eval DS + actively staffing Pinkerton contributors from his team; Director-track sponsor for James.

### Senior Sponsors (VP+)
- **Rajat C (VP, Engineering)** — skip-level; system architect + org designer; active UPP sponsor. Reports to Jeff.
- **Jeff Harrell (VP, Engineering - Core)** — Rajat’s manager; engineering culture sponsor; loves demos + AI.
- **Kartik Paramasivam (Chief Architect)** — CTO direct report; publicly supports James’s work; Dylan hints his support matters for promo.
- **Faisal Farooq (VP, Engineering — T&S/Signals)** — UPP supporter; very technical (KDD chair); owns content/user understanding.

### Peer Managers (under Dylan — verified Slack 2026-05-23)
- **Yan Li (Sr. Manager, L17, P13N-Experiences, he/him)** — peer-EM; composite team with 2 sub-EMs (Daniel Liu L16 ML + Edward Zhuang L15 backend SWE) plus Android/iOS; partner not friction (per 4/3 consensus); IB redeployment intel high-fragility. **5/23 preferred shape:** Yan absorbs Unity + PWT + latency + Tim reports under him.
- **Tim Leung (Manager II, L16, Presentation)** — **owns BOTH ngAPI backend AND Android/iOS client** (corrected from "Frontend only" 5/23); reports directly to Dylan currently (anomalous for L16 — should report through L17 peer-EM); James mentors him; great collaboration via Yu Zhao + JJ.
- **Francisco Navarrete (Sr. Manager, L17, Platform/Labeling)** — exiting to Kurchi; team in Mexico; good mutual respect.
- **Rahul Goutam (Manager II, L16, Blending)** — friendly peer; James was his onboarding buddy; co-sponsors Retentive Recommendations via his best engineer Adreanne; RLHF meeting attendee. (Surname corrected 5/23: Goutam not Goldam.)

### Sub-EMs under Yan (verified Slack 2026-05-23, full profiles in §16)
- **Daniel Liu (Manager II, L16, ML — 8 directs)** — NOT under ATG; under Yan. Team works WITH James's team AND with ATG on UIC/pUIC. Candidate for consolidation into James's CG scope in 5/23 preferred shape. Name correction: was previously written as "Daniel Lu" in Leo files (transcription artifact); real name is Daniel Liu. **2026-07-07: consolidation LANDED — Daniel + team + scope reorg under James (Dylan aligned w/ Rajat + HR, approved; downward comms mid-July).** Full profile + roster + inherited scope: `reorg_july2026/daniel_liu_team_2026-07.md`.
- **Edward Zhuang (Manager I, L15, backend SWE — 7 directs)** — likely stays under Yan to support PWT/latency/Unity vertical.

### IC reports to Dylan (Sr. Staff line, verified Slack 2026-05-23)
- **Olafur Gudmundsson** — Sr. Staff ML Engineer; direct to Dylan. KDD paper Federation co-author + active UBR reviewer (see §25).
- **Dafang He** — Sr. Staff ML Engineer; direct to Dylan. Search CLR lead + strong TL across P13N stages (see §28). **9/1: his Reflex engagement is now Dylan's conversation** — she told James she "can tell when Dafang's heart is in a project vs. not," will talk with him after his PTO about how he feels about Reflex overall, and owned part of the cause (she pushed him to launch L3). James: don't reopen, don't pre-empt her; plan Reflex Build/Simulate as JJ/Tim's until she reports back (`../projects/reflex/program_state.md` 9/1).

### Cross-Org (Growth / Search)
- **Shipeng Yu (Sr. Director, Growth)** — close to Dylan; now UPP supporter after initial friction; Brian Lee + Tingting are trust anchors.
- **Kurchi (Sr. Director, SSJ)** — primary political counterweight to UPP; relationship warming but structurally adversarial. **8/19 ⚠️ SECRET (Dylan, closed-laptop):** Dylan is considering **stopping the UPP×SSJ collaboration ~end of Q3 (9/30)** — SSJ ranking-side churn, "tons of escalations" — refocusing UPP on Ads + Growth. Do not act visibly; no new SSJ-UPP commitments; land what's in flight ("let's land and escalate where needed" — Dylan). Full entry: `dylan_wang_archive.md` 8/19; consequences: `../projects/upp/upp_retrieval_em.md` 8/19.
- **Jinfeng (IC18, P2P ML Lead)** — Kurchi’s champion; co-design counterpart. **2026-06-14: leaving the company.** As Kurchi's key technical lieutenant on P2P, his departure is a variable to watch — it may shift the P2P-blocking dynamics (Kurchi has been actively blocking P2P). Reassess the P2P path on return.

### Strategic Partners
- **Andrew Yaroshevsky (Sr. Director, Product)** — Reflex sponsor; invited James to co-own Detect + Diagnose.
- **Brian Lee (EM, Activation/Growth)** — AI forum host; long-term ally.
- **Roberto Konow (Sr. EM, Search, under Kurchi)** — was parity benchmark → **7/29: Shifu↔Reflex partnership opened.** Dylan intro'd him to the Reflex POCs (Dafang/Tim Chu/James) after his Shifu demo (Shifu = SSJ agent platform, GH `pinternal-dev/ssj-agent-platform`); first meeting readout (Tim Chu): systems complementary — Shifu strong on build, Reflex on discovery — and **"search is asking shifu to integrate itself within reflex"**; Roberto scheduling a Shifu deep-dive for Dafang/James/Ananth Pushpendran/JJ Hu/Janvi Palan. Also replied warmly 7/28 (~2 mo late) to James's 5/18 Alim reference ask — "the very first EM I managed… I am really happy!" (filed → team_members Alim entry as counter-evidence). Posture: warm reciprocal, credit Shifu's build progress, **don't amplify the who-integrates-into-whom hierarchy** (Kurchi pattern-matches James's moves as VP-backed encroachment); 1:1-cadence DM queued (James's saved draft: UPP/Prelevance/Shifu-Reflex).
- **Matt Chun (PM, UPP — reports to Andrew)** — strong trust via shared UPP political battles vs. Notif/SSJ; Bowen-era continuity; RLHF meeting attendee.
- **Karthik Subbian (Distinguished Engineer, ML — joined Core 8/29 from M10N; reporting line TBC)** — ⚠️ distinct from Kartik Paramasivam (Chief Architect). Dylan asked him to focus on **UPP** and pointed him at James (8/28 DM). First sync Fri 8/28 (James + Piyush): Piyush fielded his deep technical questions impressively — Karthik's own words, "not easy to explain ML concepts in words," he did a great job; James delivered organized links + the UPPV2-to-Jeff heads-up. Weekend follow-up (Sat 12:14 AM): why is Pixie/random-walk still in the CG mix vs. embedding-based; how does CG %imp add to 100% given overlap. **Read:** his ramp doubles as assessment — first-weeks impressions flow to Dylan and likely Rajat; "isn't this old school" is a test of whether the org has reasons or inertia. **Play (set 8/30):** James owns history/strategy/context layer; Piyush is the staged technical expert on every deep dive (builds the firsthand record for Piyush's EOY promo letter); give Karthik surface area — UPPV2 pre-read input before Jeff, the genuinely-open UPP problems. **Guard:** everything said to him reaches Dylan — UPP narrative must match the structure 1:1; future-plans talk stays on the public track (no hint of the 8/19 SSJ-wind-down secret).
  - **8/31 (Mon, his first full day in Core): full-DE-velocity ramp — pinged 9:56 AM → 6:40 PM.** James executed the Monday plan (Pixie history/consolidation answer 9:56 AM, per the 8/30 play; Piyush carried %imp/overlap mechanics). Karthik's day: sampled-softmax Q(i|x)-vs-ANN-runtime alignment question, GULP-vs-transact, rc/rcs plot readings — and **a real find: the CG overlap report reads 0% for every CG because `after_candidate_generation` logging returns 0 rows** (Piyush's online memory <5%; Karthik traced it to the logging stage within ~2 hrs; `after_blending_capping` works). Rigor-test passed against our own instrumentation — **acknowledge + credit + fix/explain the logging gap; his impressions flow to Dylan/Rajat.** Also: he self-created a **James+Dhruvil+Karthik group DM** (4:48 PM) for "retrieval and ranking questions in one place" (watch: stay active so retrieval isn't mapped around James, given Dhruvil's upstream-relocation pattern); SSJ pitched him `ssj-agent-platform` and he asked "do you have a similar one for hf?" — **James offered Reflex 5:03 PM** (a DE adopting Reflex = beyond-P13N receipt for the Dylan structure story). **Intake structure (Leo rec 8/31, unratified):** one structured 60–90 min onboarding session this week (James+Piyush: funnel map, CG history, measurement trust, open problems, 15-min Reflex walkthrough) + the standing biweekly as the batching container ("batch non-urgent for the biweekly, ping if blocking"); no public channel (question stream = exclusive intelligence; team anxiety; guard surface); JJ per-thread only when squarely blending/L1 (protects his load + Piyush's promo-letter record); consolidated replies at James's cadence, not Karthik's (he pings Sat 12:14 AM / weeknight 6:40 PM). James owes: consolidated reply Tue AM (y-axis question open + overlap-gap acknowledgment).
  - **9/1:** Tue-AM reply sent (honest "I don't know if the table/query is right" + routed him into a thread with the logging owners, Karthik attached; no extra FaceTime offered — the Piyush onboarding session is the container). **He's excited about Reflex and playing with it** (per James) — the DE-adopts-Reflex receipt is real. Not yet told to Dylan (ran out of time in the 9/1 structure 1:1) → **say it offhand in the next 1:1 as a receipt, not a report**: her DE, pointed at UPP, picked up Reflex on his own.
  - **9/2 — ⟨Leo inference, unconfirmed⟩ Karthik is most plausibly the "unnamed DE" of the 8/21 succession intel** (DE · joined Core under Rajat's org · Dylan pointed him at UPP and at James · timing: her DE news 8/21 → he lands 8/29). The record never linked them. **And Jaewon Yang was promoted to Distinguished MLE on 9/1** (§51) — UPP now has two DEs; the "replacing Jaewon" reading is weakened. Ask Dylan the UPP TL shape rather than assume. See `../projects/upp/l1_flashpoint_2026-08.md` 9/2.
  - **9/1 eve → 9/2: "vibing hard with Reflex" (James) — the adoption receipt is now verbatim, and engineering-grade.** Group DM (Karthik + Piyush + James), screenshots filed 9/2. **9/1 7:15 PM**, with a screenshot of the Reflex board: *"is the idea behind reflex that humans come up with hypothesis and defined opportunities and agents can explore the end-to-end pipeline? … for example, if i want to explore are all cg's uniquely producing value to the pinners for hf and search, should i add it to hypothesis and let the agent do the work??"* **7:26 PM:** *"read through readme. let me play with it and tell you 🙂."* **9/2 9:51 AM:** he had cloned the repo and run the full pytest suite with a coding agent — *"there is 1 test that failed… not sure if its just for me or its a known bug"* → his agent traced it to the documented known failure (README:336) **and found the dedup-key mismatch is a production-path bug, not test-only** (`sync_state_to_s3.py:703` vs `infra/jsonl_merge.py`) → *"looks like its a known bug, i will leave it alone then."* **11:50 AM:** *"how frequently do these reflex agents run? if i comment on a card, or add a card when can i expect an output? also can i monitor them?"* **James's replies:** 9/1 9:02 PM the canonical pitch (validate via KB + PM/DS agents → build the change → start and analyze the A/B; operationalizing by task type; CG quota tuning + Blending tuning "pretty far") + an open offer to chat this week (👍); 9/2 10:09 *"we've been iterating on the Eval component. I'll share with the team and we'll get on it"*; 11:51 *"right now it's adhoc, we're working on bringing it onto its own stand alone service in ~2 weeks so it can run at least daily."* **Read:** a DE who reads the README, runs the tests, diagnoses a real bug and asks about cadence + observability is a *user*, not a spectator — the strongest beyond-P13N receipt Reflex has (`../projects/reflex/program_state.md` 9/2). **Two promises now attached to his name:** the daily-run standalone service in ~2 weeks (≈ 9/16 — D-4, Tim's, 9/10 tripwire) and the dedup-key fix (Eval — James's own named thread). **Tell Dylan as a receipt, not a report:** her DE, pointed at UPP, is filing Reflex bugs on day 3.
  - **9/2 (James, evening):** the chat offer went untaken — *"which is fine. We offered so he knows."* He is instead **engaging with Alok on the CG-overlap logging thread James opened 9/1** (the 8/31 find — `after_candidate_generation` returning 0 rows) — the routing-into-a-thread-with-the-owners move worked; Alok is now the one a DE is working with on data. **The dedup-key fix: James does it himself** (*"just a simple PR"*) **and may add Karthik as reviewer** — turns a bug report into a codebase touchpoint and a visible close of the loop; his review comments become the next receipt. **9/3 evening: landed** — James wrote the fix, Tim signed off, merged the same week ⟨confirm Karthik was tagged/told⟩.

### Under Rajat (non-Dylan)
- **Kaanon MacFarlane (Director, Eng)** — re-orged out of Dylan’s org; now working on AI initiative with Karina for Rajat. Frontend/backend, no ML.
- **Karina Sobhani (Director, Eng)** — team shrunk to 15; working on AI initiative with Kaanon. Minimal interaction with James.

  
---  
  
Based on this breakthrough with Dhruvil and the successful containment for Dylan, here are the updated sections for stakeholders.md.

The key shifts are:

Dhruvil: Moved from "Functional Ally" to "Emotional/Strategic Ally" (the highest tier). You successfully leveraged his S/C profile by offering safety ("us vs. the problem") and control (letting him own the final decision).

Dylan: Updated "Political Calibration" from a risk to a proven capability. You demonstrated you can clean up your own messes without her intervention, which is a massive trust accelerator for her.

Markdown
# 1) Dylan — Manager / Director (Homefeed Relevance)

> **Related files (Dylan two-file system, consolidated 2026-08-01):**
> - [dylan_archive.md](dylan_archive.md) — the single deep Dylan file. Part I = 1:1 & touchpoint log, newest first (`prep` reads, `debrief` writes) · Part II = deep 9-month forensic archive (read once per strategic question) · Part III = point-in-time artifacts, verbatim.
>
> **What this section is:** compressed live profile in the same shape as 23 other stakeholders. Cross-stakeholder triangulation. Update on arc-shift events; keep compressed (depth lives in archive).

## Role in my 6–12 month goals
- **Primary gatekeeper for scope, ratings, and sponsorship.**
- Assigns and endorses **director-shaped, ambiguous problem spaces**.
- Sets the **bar for executive narrative quality** upward (accuracy, calm, trustworthiness).
- Key amplifier (or limiter) of my visibility with VP / skip-level leadership.

## DiSC Profile (Most Likely)
- **Primary:** C (Conscientious)
- **Secondary:** D (Dominant)
- **Low:** I (Influence), S (Steadiness)

### Implications
- Optimizes for **correctness, rigor, and risk containment** over speed or charisma.
- Interprets **calm precision as competence**; interprets emotional charge as risk.
- Values leaders who **reduce her cognitive load** via structure, pre-alignment, and ownership clarity.
- Prefers **decisions with tradeoffs surfaced**, not exploratory brainstorming.
- Trust is cumulative and fragile to surprises.

> **Operational takeaway:** Lead with structure, evidence, and optionality. Let decisiveness emerge from rigor, not energy.

## Current trust state
- **Overall trust level: Very High (Peak Trust — Exceeds + Active Sponsorship)**
  - **Evidence:** strong onboarding rating; entrusted with ambiguous investigations; relies on me for accurate exec-facing communication; has shared sensitive context selectively. **March 2026:** Exceeds rating, $1.2M equity grant, IC17 sacrifice for EM backfill, explicit confidence statement, co-solving DaFang situation. Full sponsorship confirmed.
  - **Confidence:** Very High.

### Trust dimensions
- **Execution correctness:** High
  (rigor, closure, accuracy discipline)
- **Operational reliability:** High
  (oncall, triage, process stabilization)
- **Strategic judgment:** Medium–High
  (strongest when framed crisply with explicit tradeoffs)
- **Political / communication calibration:** **High (Confirmed via Bowen transition handling and UPP escalation management)**
  (Consistently demonstrates ability to repair misalignment laterally without escalation; showed maturity in handling "Matthew" calibration dynamics and Bowen departure framing).

## What Dylan optimizes for
- **Business outcomes + risk management**
  - Zero tolerance for late surprises.
- **Legible narratives to skip-level / VP**
  - Clear “so what,” explicit confidence bounds, calm tone.
- **Cross-org alignment**
  - Pre-aligned plans > escalations.
- **Scalable leadership**
  - TL / EM ownership that reduces her coordination burden.

## Communication preferences

### Known / observed
- Strong preference for **accuracy and trustworthiness** in exec-facing statements.
- Responds best to **crisp framing**:
  - *Problem → options → recommendation → risks → explicit ask.*
- Expects **pre-alignment** before broader forums.

### Channel hierarchy (4/25 update)
- **1:1** — strategic, agenda-driven items. Default for career, roadmap, team.
- **Slack DM** — tactical real-time re-anchoring (4/15, 4/21 patterns). Faster than 1:1, lower-friction than email.
- **Personal cell phone** — sensitive-issue channel established 4/25 (Rajat shield conversation). Use sparingly; signal value depreciates with frequency. Default reverse: after high-stakes stakeholder events, decide whether cell-channel debrief is warranted vs standard DM.
- **Email / threaded** — almost never. Dylan operates in DM-not-thread mode (managerial pattern).

### Uncertain / to validate
- Ideal cadence for strategic updates (weekly vs biweekly).
- Tolerance for speculative forecasting vs strictly evidence-backed claims.
- Preference for **written 1-pagers vs verbal ideation** early in problem formation.

> **Working default:** short written pre-reads + explicit asks; reserve meetings for decisions and tradeoffs.

## Dylan’s leadership style (best current model)
- **High standards; low tolerance for hand-wavy claims.**
- Trust accrues through **correctness × calm × consistency**.
- Rewards leaders who **simplify complexity** and own outcomes end-to-end.
- Will step in decisively when ambiguity creates emotional or operational risk.

**Confidence in model:** Medium–High (based on repeated interaction patterns).

## High-signal history
- **Onboarding:** Strong rating recognizing team building, roadmap clarity, and operational excellence.
  *(Confidence: High)*
- **Matthew Calibration Incident (Jan 2026):** Initially missed pre-alignment with Dhruvil; self-corrected immediately by repairing the relationship laterally. Dylan validated the feedback ("thanks for flagging") and the recovery ("great to hear").
  *(Confidence: High — proved you can clean up your own messes).*
- **Trust evolution:** Initial perceived coolness reframed; deliberate work on influence without attachment, brevity, and composure has increased trust.
  *(Confidence: Medium–High)*
- **Bowen Departure & Perf Review (March 2026):** Managed Bowen's departure to OpenAI with clean framing ("management gap, not technical crisis"). Dylan's reaction casual — she already viewed Bowen as self-prioritizing. Received Exceeds rating and $1.2M equity grant. Dylan expressed full confidence and offered IC17 sacrifice for backfill. Co-solved DaFang situation together.
  *(Confidence: Very High — trust at peak)*
- **PINvestigator Breakthrough (April 1, 2026):** Dylan personally ran PINvestigator for ~5 hours, called the investigation doc "great," proactively suggested sharing with Karim Wahba/PADS, asked to see custom skills next 1:1. **Register shift: sponsor → AI guide.** AI/IC drift concern dissolved.
  *(Confidence: Very High)*
- **PM Tone Feedback (April 3, 2026):** Two newer PMs (Akshanta, Lily Li) told Dylan James's tone could be better. Yellow flag delivered softly as a favor. Same D:88% root cause as Feb "eggshells" but lower severity. Repair landed (Akshanta DM + cordial 1:1).
  *(Confidence: High)*
- **Operational Embedding (April 15-21):** Dylan self-inserted into RLHF expert team for Reflex (Sr. Director as IC), proposed critic-agent architecture (4/17), put Dafang onto Reflex "to learn." Issued two pacing DMs in one week (4/15, 4/21) — care-based real-time re-anchoring via DM, not 1:1. **Register: operational co-participant on flagship initiatives.**
  *(Confidence: Very High)*
- **Career Conversation Accepted (April 21, 2026):** Dylan accepted as "quarterly regular, happy to have one, this is regular." Pre-seed plan obsolete. On-call ask landed instantly. Burnout-watch flagged twice in one week — sustainability is the path ceiling. Public AI differentiation private, with calibration-room ceiling ("everyone is excited by different things").
  *(Confidence: Very High)*
- **Retention Philosophy + Moral Filter (April 23, 2026 Slack):** *"If ppl really want to go and try the new areas, I don't want to be in the middle of it... I'm happy for him."* Won't fight leavers; engage-via-interesting-work then release. Moral hierarchy: Anthropic/OpenAI respectable; Meta/Snap disappointing. Reddit unknown. Warm peer-level register confirmed.
  *(Confidence: High — verbatim quotes captured)*
- **Peer-Moral Alignment on Krishna (April 24, 2026 Slack):** Unprompted *"poor guy. he did everything he could. yeah it's very sad"* on Krishna's reorg. Values-shared territory — Dylan morally distancing from Kurchi's playbook in plain language. Direct counter-evidence to "Pinterest will Kurchi me" rationalization. Rarest stakeholder signal.
  *(Confidence: Very High — verbatim quotes)*
- **Shielding the team from Rajat (April 25, 2026, off-channel cell phone):** Dylan called from her **personal cell phone** to flag Rajat's recurring engineer-names ad-hoc-ask pattern. Said it's not the first time. Positioned herself as **POC for UIC / Retentive Recs** to absorb the political overhead and keep the team focused on substrate. Established cell phone as the sensitive-issue channel between us going forward. **Register shift: operational co-participant → political-shield co-owner.** This is Operational Embedding (Lesson 7) made literal — Dylan running the political layer so I run the build layer. Sponsorship escalation, not demotion.
  *(Confidence: Very High — direct conversation)*
- **Action-sponsor framing clarified (May 5, 2026 1:1):** Compression-day 1:1 (new topline-growth mandate from her chain landed that morning) made Dylan's primary sponsor affordance visible across a single meeting: Sophia HC escalated to Rajat ✓, Reflex resources via Chuck + Faisal ask ✓, EM hire pinged-recruiting ✓, repeated *"what can I do"* as offer-of-escalation ✓. Strategic-reframing asks (AI-enablement / Anticipation Foundations seed with deferral wrapper) got silence. Cross-framework convergence with Ethan customGPT independent confirmation: *"Dylan is your action sponsor. She will: forward, resource, unblock, re-scope, protect against burnout."* **Operating implication — "Dylan ask portfolio" pattern:** 2 asks per 1:1 max — 1 forwarding (artifact attached) + 1 resourcing/unblock (binary). Strategic-reframing / decision-inside-her-team / big-picture-vision asks go to Rajat, Andrew Y, coach, or peer EM. Distinct from leadership-style observations (high-standards / correctness × calm × consistency) — this is about *what she does for me as sponsor*, not who she is as leader. See auto-memory `project_dylan_action_sponsor.md`.
  *(Confidence: Very High — single-meeting saturation across 4 distinct asks + cross-framework convergence with Ethan)*
- **Value-driven scope decisions (May 7, 2026 DM thread on Francisco labeling team):** Kurchi pushed to move Francisco's labeling team to Krishna. Dylan's reaction made her decision filter explicit: *"well it's fine, I don't feel this worth my energy anyway. I will just give to her and let her have fun"* + *"I am just cleaning up debt. yeah. what's the point us owning it. you never hear anything about it in anticipation"* + *"business wise it makes sense. Kaanon should have done it long time ago"* + *"I haven't discussed with Francisco and team. I'm sure this wouldn't be great."* **The filter, in her words: anticipation-relevance + business sense. She gives up scope when no anticipation/business value, fights for what does (Sophia backfill same week). She'll prioritize business sense over peer-EM preferences. NOT territorial — value-driven. Pacing default: "I will figure out in a bit" / "I will ask Kurchi next week" — she takes time to process.** Implication for Yan's-team-stable-split read (per Anna intel): Dylan keeps the current shape because she sees value, not because she's defending territory. To shift, surface anticipation/SSv2-relevant value-case observations as input-not-demand. She's already invited it: *"if other things change for SSv2, let me know."*
  *(Confidence: Very High — verbatim quotes, multi-message thread)*
- **Director timing reframe + manager-staying clarification (May 9, 2026 corrections):** Two corrections James locked in during 5/9 coaching session:
  - **Realistic Director target is mid-2027 (July) or end-2027 (December).** 2026 calibration cycles (July, EOY) are NOT career-meaningful for him — not close to consideration. Stale references to "ready and advocated for late summer/early fall 2026" / "promo by EOY 2026" / "90-day inevitability goal by end Aug 2026" (in `ethan-james-situations.md` Q17) are superseded.
  - **Dylan is NOT transitioning to a new role on June 12.** She remains James's manager. The 6/13 → ~7/6 window is OOO only (3 weeks PTO + 1 week India). Her commitments — *"I'll get you and Dhruvil to Director next, set up org for high performers like you two"* + *"wait for org to settle"* — remain HERS to execute, not handed-off-to-successor. The Director arc with Dylan is a multi-quarter relationship, not a 5-week pre-transition sprint.
  - Operating implication: Don't fight Dylan's decisions, don't push timing, don't over-apply hand-forcing. Trust the commitment, work in alignment with her stated frame, surface value-case observations as input-not-demand on the long arc. Path A (capability axis: Anticipation Foundations, RR cross-surface) is the operational frame; Path B (consolidation push) is closed for the foreseeable.
  *(Confidence: Very High — direct corrections from James, captured in memory `project_director_timing_reframe.md` + `project_dylan_staying_not_transitioning.md`)*
- **Pre-OOO Slack download — Bill Reflex review + Michael close + JJ promo + cupcake catch (June 3, 2026):** Four signals packed into a single ~100-minute Slack exchange the afternoon before James's OOO trip:
  - **Bill product review on Reflex landed well.** *"we just had a great product review with Bill on reflex btw, all due to the hard work from you and team"* + *"with Bill review the audience is extremly tight"*. Reflex crossed CEO-altitude airtime via Dylan's channel. Dylan credited James + team explicitly. (Bill = Bill Ready. Note: Reflex, not Anticipation — separate from the Jeff/Vicky must-win below.)
  - **Michael close (recruiting win, "keep to yourself, low key now, not sharing").** Senior hire Michael accepted; James cultivated him on LinkedIn for ~4 years; Dylan flagged James's contribution as a pre-trip gift. *"keep to yourself, we closed Michael"* + *"maybe Andrew told you, but yeah don't share"*. James's reaction *"oh wow, he didn't even tell me"* is just a flicker — closes go quiet at the end. **Confidentiality discipline: do not surface to Michael himself or to peers (incl. Dhruvil) until announced.**
  - **JJ promo conversation parked post-OOO.** Dylan asked *"no promo on your end right?"* — expected a no, got JJ. Her response: *"okay this is going to be very tough"* + *"let's discuss once you are back"* + *"budget extremly tight, keep to yourself"*. James committed *"makes sense. I would like to try, for retention reasons."* Dylan: *"sure"* with thank-you react. Read: Dylan takes case seriously, won't pre-litigate over Slack, wants real airtime post-return. Retention framing is the right lever with Dylan specifically (echoes her *"high performers like you two"* Director-commitment line). **Post-OOO action: prep the JJ retention/case conversation with Dylan, do NOT draft over the 7-day OOO window — will re-pattern wrong.**
  - **Cupcake metric catch + Dylan thank-you.** TPM put wrong holdout numbers (Q1 p13n instead of Anticipation holdout) in the Jeff + Vicky **Anticipation must-win** presentation; James didn't catch in real-time during the meeting (fast-rolling, no prep buffer); Vicky propagated the numbers to ATG post-meeting; correction required. TPM had asked Anna + James for sign-off with only a **2-hour window**, James was in back-to-backs. James proactively flagged the swap to Dylan post-hoc; Dylan: *"right I'm trying to get that straight / thanks for helping, no worry"*. **Process gap worth fixing post-OOO: private DM to TPM asking for ≥24-hour review buffer on must-win artifacts going to Vicky/Jeff/Bill altitude.** The correction is in motion (Dylan handling) — protects James from over-claim overhang (relevance holdout likely overstated Anticipation delta).
  - **Cross-thread read:** Dylan is using the pre-OOO window to download high-trust intel and bank a sponsorship signal before James goes silent for 7 days. Three "tight" signals in one conversation (Bill audience tight + budget extremely tight + promo very tough) = budget-pressured calibration cycle is hardening. Reflex investment is winning sponsorship while IC promo budget tightens — likely zero-sum somewhere upstream. The Bill review win is real and is James's; bank it without over-rotating.
  *(Confidence: Very High — verbatim Slack quotes captured. Confidentiality flags: Michael close + JJ budget/promo both marked keep-to-yourself.)*
- **Reorg timing read (2026-06-30 — inferred; no committed date exists anywhere):** The broader reorg is Dylan's own instrument for James's Director growth path (Innovation-James / Core-Dhruvil split, her design intent since **Feb 3**). It is a **distinct event from the Director promo** (promo = ~2027, sequenced after Dhruvil). **Best-guess timing: fall 2026 (Q3/Q4), Dylan-intended but genuinely unscheduled**, gated on the org "settling" + Alim landing (mid-July). Enabling signals cluster H2-2026 ("making my way through it" + stakeholders pre-warned, 5/18 career convo; March "By Q3, new-EM-onboarded, scalable org" metric; Dhruvil packet staging) **vs.** restraining signals (6/1 "very early / no forced clock"; 6/17 "unknown timeline"). Three nested events: (1) Alim two-track split = now/mid-July = her own "By Q3" target; (2) broader reorg/charter-lock = fall 2026; (3) promo = 2027. **Implication:** Dylan is unlikely to tell James to "hold off on Alim" (it's her Q3 metric) — more likely "go ahead" while keeping charter/scope fluid. The reorg is James's **vehicle**, not a hazard. Full analysis + 1:1 talk-track: `alim_reorg_proposal_2026-06-30.md`. **⟨SUPERSEDED by 7/7 entry below — reorg is approved and moving NOW, not fall.⟩**
- **REORG APPROVED — landed in the 7/7 re-entry 1:1 (2026-07-07, direct from Dylan):** Dylan has **already aligned with Rajat and HR; the reorg is approved.** **Downward conversations start mid-July.** First concrete act: **Daniel Liu (EM) + his 8-person team + their scope (Exploration module ML/plumbing, Intelligent Boards, Recommend-a-Board, Unity Board) reorg under James** — the fall-2026 prior is dead; the scope expansion arrived a quarter early. Dylan framed the team as "relatively underutilized" (she'd lent them to other personalization efforts) and the inheritance as James's opportunity to correct that. **She wants a structure proposal from James** (Alim-vs-Daniel allocation the open question) and **offered time to observe before deciding** — no forced clock on internal structure. Also from the 1:1: stepped-up-in-absence list (Piyush, Devin, Yali, JJ) landed well; Bella disclosure received with "thanks for the visibility, let's see how it goes" (no forced action); Yuke TL→IC endorsed with *"this is exactly the type of transparency I'm looking for"* — **file that phrase: transparency is the currency Dylan trades in.** Her open question back: who TLs the pUIC/RR space. Intel + roster: `reorg_july2026/daniel_liu_team_2026-07.md`.
- **REORG UPDATE — timeline decoupled + org shape clarified (2026-07-14 conversation; full detail `dylan_archive.md` Part I 7/14):** **Two decoupled reorgs** — *Dylan's* happens first; *James's internal* reorg runs on **his own clock** (she explicitly gave more time to observe/think/propose). **Initial state = minimal reporting changes**: only Alim onboarding, taking a subset of *James's own* reports — NOT moving Daniel's reports to Alim ("too drastic"); **Daniel's team stays intact under Daniel** initially. **Headcount: only Dhruvil + James** this cycle. **Dhruvil gets the blending team** (Rahul + ~5–6 eng) as blending manager. **Comms:** other EMs told **~1–2 days before** the announcement; timing/messaging **finalized this week after calibrations**; decision audience = Dylan + James + Dhruvil. **Political backing:** Dylan pre-sold to **HR, Andrew, Rajat** — all happy; explicitly **James's path to the next level** (setting him up for success). **Org-shape clarity: James + Dhruvil = the two ML Senior EMs (M17 → Director = M18)**; Dylan building **two ML director pillars** (Innovation/Retrieval = James, Core/Ranking = Dhruvil). **Tim promoted M16→M17** (management, not IC) but **stays under Dylan** (James expected Tim→Yan — not so); **Tim + Yan = non-ML** (frontend/backend SWE EMs — orthogonal to James's ladder; James is *already* M17). Dylan's guidance: **"don't want too many changes."** **Boards intel:** Recommend-a-Board **hasn't driven metrics in ~6 months**, but a recent **notification collab → "wow" improvements** — Dylan shared the launch review + asked James to get into the nitty-gritty (= graded test + the boards-metric-unlock thesis). Daniel's team **underutilized** (Dylan's word, echoed by the team itself). **What Dylan's already aligned with** (from James's early skeleton): CLR+UPP not handed to Alim/Daniel right away (too much context); LWS split from CLR as Daniel's onboarding ramp; James spending more time on Reflex. Structure proposal now `work/people/reorg_july2026/org_design_proposal_2026-07_v2.md`.
  *(Confidence: Moderate — inference from clustered signals; no committed date.)*

- **REORG STATUS (2026-07-17):** **Still unannounced.** From Dylan's 1:1 with James this week: she will tell **James + Dhruvil the messaging timing "this week"** (hasn't yet as of Fri 7/17 morning — likely busy); **Yan gets only ~1 day's notice, by design** (he's the org losing the team). **Moves confirmed (James direct, 7/17, resolving a dictation garble that briefly read as "Yan, Daniel, Rahul → Dhruvil"):** **Rahul Goutam + his 4 MLEs → Dhruvil** (consistent with the 7/14 blending intel); **Daniel Liu + his team of 7 MLEs → James, out of Yan's org** — the 7/7 inheritance premise intact (roster file counts 8 incl. Rita the intern, ~2 months left). James + Dhruvil discussed the reorg laterally in their ~7/16–17 1:1, both gracious; **interim agreement: minimal changes, let ICs keep existing collaboration patterns** (full entry: Dhruvil chapter 7/17).

- **Post-vacation re-entry mood pattern (2026-07-01 — per Anna, RR PM partner / peer ally, §2):** Dylan reliably comes back from vacation in a *"why am I doing all this shit / what's the point of all this"* mood — Anna says Dylan describes her return **exactly** the way James describes his own (James is in the same not-hungry state post-China). **Operating implication for re-entry 1:1s:** the first 1:1 back is a *reconnection* meeting, not a content-delivery one — emotional > intellectual. Lead with genuine vacation catch-up; keep strategic asks light (one time-sensitive land max); read her energy before probing timelines. The un-gripped / operate-from-enough register is what Dylan rewards anyway (burnout-watch ×2; CD-profile distrusts gushing) — so meeting her in the shared mood is both the human move and the credible one. **Caution:** meet her *feeling*, don't co-sign her *conclusion* ("it's all pointless") — that could read as flight risk. Applied in the 7/7 re-entry prep (`dylan_archive.md` Appendix III-A).
  - **Source = Anna** (inner-circle peer ally, §2; an already-established Dylan/org intel channel — cf. the "Yan's-team-stable-split read (per Anna intel)" above). On promo she told James *"you'll get promoted, just a matter of time — that simple"* (they laughed about it, James having said he doesn't really want it anymore). A promo-confidence read from someone with real access to Dylan's thinking — lowers the case for James gripping the title.

## Dylan’s likely current narrative about me
- **Positive core (April 2026):**
  “James is the AI-native operator on my team — he's the differentiator other directs aren't matching. He's running Reflex with Andrew, Pinkerton is winning organic adoption, the team is stable, and he handles his own messes. AI work has graduated from suspicious-IC-drift to actively load-bearing. Career conversation accepted as quarterly-regular; he's serving the org's needs by leading where the puck is going.”
- **Watch-out:**
  “Sustainability is the ceiling — flagged burnout twice in one week (4/15, 4/21). Path he wants compounds with intensity; if he can't decouple AI multiplier output from personal pace, the path caps itself. Public ranking against peers (Dhruvil/Yan) won't happen — private differentiation is real but won't translate into calibration-room weapon.”
- **Confidence:** Very High.

## Risks with Dylan (and mitigations)

- **Risk:** Surprise or misalignment in exec forums
  - **Mitigation:** short pre-read; explicitly ask *“anything you’d like framed differently?”*

- **Risk:** Over-explaining live → loss of executive confidence
  - **Mitigation:** default to 3–5 bullets; offer *“can go deeper if useful.”*

- **Risk:** Emotional reactivity to perceived disapproval
  - **Mitigation:** pre-meeting reset; use calm optionality language (*“two viable paths…”*).

- **Risk:** Becoming the integration bottleneck (signals lack of scaling)
  - **Mitigation:** name owners explicitly; highlight TL / EM-driven outcomes.

## What increases Dylan’s trust fastest
- Deliver 1–2 **exec-legible wins** with clear mechanism and proof plan (e.g., Retentive Recs).
- Demonstrate **leader scaling**: Bowen / TLs owning artifacts and XFN relationships.
- Surface **risks early with mitigation plans** (no late surprises).
- Maintain **accuracy discipline**: clearly separate facts, hypotheses, and open questions.

## What could damage trust
- Confident claims without evidence.
- Escalations without visible pre-alignment.
- Taking on too much personally and degrading quality or calm.

## Operating plan (how I work with Dylan)

> **Standing 1:1 theme from 2026-08-28 (James):** wean the org off its dependence on him — every 1:1 carries one concrete instance of someone else driving (Alim / JJ / Tim / Daniel) and what James did to make room; never narrated, never "I'll lean in more." Detail + per-1:1 rule: `dylan_wang_archive.md` Part I 8/28.
- **Default artifact:** 6-bullet update
  - *So what / Progress / Risks / Decision needed / Ask / Next milestone*
- **Cadence (proposed):**
  - Biweekly strategic sync
  - Weekly lightweight async update (only if needed)

> **Meta-goal:** consistently reduce Dylan’s cognitive load while increasing her confidence that I can scale impact without adding noise.

## 2026-07-22 — coaching point: "learn how to motivate people"

Dylan explicitly named **motivating people** as something she wants James to grow into, and taught it live via a worked example: to motivate **Jeff**, she anchored on **Matt Madrigal's ads priorities** (Jeff's boss cares about ads → ads collaboration is Jeff's incentive), and framed the SSJ-on-UPP friction as a preview risk — *"if it's this hard to get leaders to work together under Jeff in Core, how does it work when we go to ads?"* It worked: Jeff immediately pointed **Andrena (Dir, TPM — §48)** at the ads-collaboration area. **Takeaway to internalize:** motivation = find the other party's real incentive (often their boss's priority) and connect your ask to it. James applied it in the same conversation — offered the UPP-retrieval-in-P2P launch candidate as the ads-collaboration proof point; Dylan endorsed using it "to push things forward." Full context: §5 Jeff 2026-07-22 update.

---  
  
# 2) Anna — Political Sponsor & Strategic Amplifier (Retentive Recommendations)  

**Updated 2026-04-29: Bespoke IRL career-talk on calendar for Thursday 2026-04-30.** Channel still operating at maximum peer register. Apr 27 DM exchange: James shared vulnerable peer line — *"i've been heads-down building so much ai stuff and i look up and i have a sense that i'm maybe just distracting myself from actual career progress 😆"* — and Anna reciprocated with mutual-pivot rather than advice-giving (*"what career stuff???? my level progression in DOS2???"*). She's processing her own progression questions in parallel; tomorrow's bespoke is peer-symmetric, not asymmetric. Co-conspiring on Bo Zhao intel asks routine (*"I'll tell him the question comes from you 🙃"*). **Arc worth holding:** tomorrow's IRL conversation lands ~72 hrs after the Apr 27 "distracting myself" admission and ~24 hrs after Apr 29 CTO demo confirmation — Anna gets to see the answer to the worry she heard Sunday. Don't over-prep; the texture that makes the channel valuable dies under structured agendas.
  
## DISC Analysis: High I (Influence) / High D (Dominance)  
* **Profile:** **The "Chaotic Driver" (Id or Di).**  
* **High I (The Enthusiast):** Highly expressive ("SCREAMING," "OMFG"), prone to boredom in "corporate" settings (uses the Cat Grocery video to cope), and motivates through excitement and camaraderie. She builds deep, emotional alliances rather than transactional ones.  
* **High D (The Driver):** Results-oriented and impatient. She "hates words" and "planning to plan." She wants the "fixed slot" (the win) and will aggressively cut through ambiguity to get it.  
* **Low S (Steadiness):** Restless. Rapidly pivots and prefers high-velocity change over stability.  
* **Adaptive C (Conscientiousness):** generally intolerant of "process" details, *but* surprisingly hungry for "mechanism" details (e.g., CLIP clustering) if it explains *why* her product intuition will work.  
  
## Role in my 6–12 month goals  
- **Primary Political Amplifier:** She is the lens through which **Dylan** (your manager) views your success. Her endorsement is the single biggest factor in your "Trusted" status with Dylan.  
- **"Invisible Authoring" Partner:** She takes your technical strategy and sells it to Andrew (her Sr. Director) and the CTO, rooms you may not be in yet.  
- **The "Real" Product Owner:** She cuts through the "Listen/Explore" corporate fluff to define what actually ships (e.g., the "fixed slot").  
  
## Current trust state  
- **Trust level (overall): EXTREMELY HIGH / "Inner Circle."**  
  - **Evidence:** "Nap time" 1:1s; sharing vulnerable personal photos (the "puking bride"); explicit political collusion (covering for Albert, "managerial diplomacy"); shared cynicism regarding "planning" meetings.  
  - **Confidence:** Very High. You are her "safe harbor" in engineering—the person she vents to and plots with.  
  
- **Trust dimensions**  
  - **Psychological Safety:** Maximum. You can say "I want to leave," and she shares memes. No corporate mask exists between you.  
  - **Technical Credibility:** High. You are her "Translator." She admits she doesn't know "import statements" and relies on you to turn her product instincts into engineering heuristics.  
  - **Political Alliance:** High. You operate as a united front against external thrash (Search, Growth, "planning" meetings).  
  
## What Anna likely optimizes for  
- **"Vibe" & Momentum:** She needs to feel *excited* about the work. If it’s boring/abstract, she checks out.  
- **The "Fixed Slot" (Concrete Wins):** She wants tangible estate on the screen that she can point to as her legacy.  
- **Simplicity:** She is allergic to "words" and complex abstractions. She wants the heuristic (e.g., "CLIP distance") that solves the user problem.  
- **Influence:** She is optimizing for her rising scope under Andrew; she needs you to deliver the "how" so she can sell the "what" to execs.  
  
## Communication preferences  
- **Do:**  
  - **Use "Insider" Language:** Memes, "sksksk," and shared jokes build the bond. Don't be too formal in 1:1s.  
  - **Translate Product to Eng:** Give her the specific heuristic (e.g., "Use PinCLIP distance to denoise") so she feels smart and armed for her meetings with Andrew.  
  - **Validate her Cynicism (carefully):** Acknowledge when a process is "stupid" (e.g., "planning to plan") so she knows you see reality, then pivot to execution.  
- **Don't:**  
  - **Force "Process" Conversations:** Do not drag her into "planning to plan" meetings without a clear exit strategy.  
  - **Use "Corporate Fluff":** Avoid abstract pillars like "Listen/Explore" unless you are mocking them or concretizing them immediately.  
  
> **Working default:** "Nap Time" syncs for real talk + High-level "hype" summaries for her to forward to Andrew/Dylan.  
  
## Anna’s likely current narrative about me  
- "James is my work bestie and the only EM who actually gets it. He cuts through the BS, translates my crazy ideas into real engineering, and handles the politics perfectly. I trust him with my life (and my headcount)."  
  
## Risks with Anna (and mitigation)  
- **[Risk] The "Cynicism Bubble" (Echo Chamber):**  
  - **Context:** You both bond over hating "dumb" corporate things (Search/Growth requests).  
  - **Mitigation:** Ensure your private venting doesn't turn into public obstructionism. Sometimes you have to "play the game" for Dylan/Jeff's sake, even if Anna thinks it's stupid.  
- **[Risk] Professional Brand Leakage:**  
  - **Context:** The "nap time" / "who hurt you" vibe is fun, but dangerous if overheard by Jeff or rigid stakeholders.  
  - **Mitigation:** Keep the "work bestie" vibe strictly in DMs/1:1s. In larger forums (especially with Andrew/Dylan), pivot to "Sharp Strategic Partner" mode so she looks professional by association.  
- **[Risk] Over-reliance on "Vibe" vs. Docs:**  
  - **Mitigation:** She hates writing docs. You must be the one to document the "decisions made in memes" so there is a paper trail for the team.  
  
## What increases Anna’s trust fastest  
- **"Invisible Support":** Prepping your team (Jiacong) to answer Andrew's questions perfectly so *she* looks like a great leader.  
- **Emotional Validation:** Reacting to her memes/videos. Acknowledging her suffering in bad meetings.  
- **Concrete "Toys":** Giving her early data or prototypes (like the labeled clusters) that she can "play" with and get hyped about.  
  
## Operating plan (how I work with Anna)  
- **Default Artifact:** The "Heuristic Translation." (e.g., "Here is the exact engineering logic that proves your product intuition is correct").  
- **Cadence:** Keep the "Nap Time" 1:1s. They are essential for emotional regulation and backchannel alignment.  
- **Escalation:** **None.** You resolve things directly. If you need Dylan, you ask Anna to influence her *for* you.  
  
### Pros / Cons of my current approach with Anna  
- **Pros:** Unbeatable speed and alignment. You have a "super-delegate" who sells your work to leadership (Dylan/Andrew) effectively. High retention/morale for both of you.  
- **Cons:** Risk of becoming a "clique" that alienates other partners (like Growth or Search). Risk of validating biases rather than challenging them (e.g., assuming Search team is "clueless" without checking).  
  
---  
  
# 3) Dhruvil — Peer Sr Engineering Manager (Homefeed Ranking)

## Communication style (filed 8/22 at James's request — "I hate it, but I might benefit from learning some of it")

Observed pattern from the 8/21–22 exchange (and consistent with prior behavior):
- **Deliberate ambiguity with deniability:** no names, no specifics — "I am not taking individual or team names, and I think you get it." The reader constructs the meaning; nothing quotable exists if it's forwarded.
- **Repetition of one load-bearing fact without stating its implication** (the DE succession, emphasized repeatedly) — lets the listener draw the radioactive conclusion himself, so Dhruvil never said it.
- **Timing control:** the scheduled Saturday-morning send; the "sorry I was in a rush" reframe arriving after the live chat had time to settle.
- **Authority self-deprecation while steering:** "not my call, just my 2c, just an opinion" — wrapped around a fully-formed position (the relay-race doctrine) that in fact shapes the decision.
- **Pre-alignment before approach:** James's read — likely synced with Dylan before flagging; his "spontaneous" concerns arrive with ducks already in rows.
- **Softening wrappers** ("I'm fairly confident things will be fine," "sorry if I wasn't clear") that lower the receiver's defenses while the payload lands.

**When to borrow it (James's own use):** cross-org or lateral topics too radioactive for a record — convey the fact, withhold the conclusion, let the receiver own it; the "not my call" wrapper when opining outside his lane; scheduled timing for messages that need to land cold. **When not to:** with directs and close partners, James's directness is the asset — hint-mode there reads as manipulation. Countermeasure when on the receiving end: don't decode alone — name the ambiguity back privately ("help me make sure I got this right") or triangulate (as done here), and never act on a hinted conclusion as if it were stated.

## 2026-08-21/22 — The "trickier next week" flag: UPP L1 / Matt / Jaewon / DE succession

Dhruvil pinged James Fri ("might need to flag something about one of p13n's cross-team partners… trickier next week"), then sent a Saturday-morning scheduled clarification: the big risk is **damage to the P13N↔ATG relationship + unhealthy competition** around the L1 CFM/RecGPT question — "we both in particular have a critical role to play," names withheld ("I think you get it"). In the live chat he framed **Jaewon as possibly feeling threatened** and repeatedly emphasized the confidential **DE-replacing-Jaewon-as-UPP-TL** fact (from Dylan; Rajat→Chuck already). He also ran the clean de-escalation on his own report: extracted Matt's softened position (don't de-pri LWS/FM work; fine trying RecGPT L1) and named the real design question as **relay-race vs. race** (sequencing/merge governance). Full chronology + reads: `../projects/upp/l1_flashpoint_2026-08.md`. Working posture: joint smoothers — Dhruvil handles Matt (his report), James handles Yali/Hedi/team framing + the Jaewon channel; keep the confidential layers (DE, promo history, DM screenshot) out of every room.

## 2026-08-07 — Kim skip-level HELD (early): the dossier validated live, point by point

The her-voice-first design ran 8/7 and the 8/5 dossier held up almost line for line (full record: `reorg_july2026/daniel_liu_team_2026-07.md` 8/7 update). Never cite Dhruvil — this entry tracks dossier-vs-reality only:

- **Change fatigue / flawed-setup history: confirmed.** Her own words: "a lot of things in curation were very flawed" — anchored to a live **promo wound** (denied last year for "not enough ML work" while she was the only MLE and de-facto PM; "a fair reason… not really though. The setup was flawed").
- **Preferred-work-likely-not-curation: directionally confirmed.** She self-identifies as a **systems engineer**, chose the deep-modeling bucket to fight imposter syndrome head-on, and is now questioning whether that's what brings her joy. Blend proposal (model depth in service of product/user, exploration-shaped) appealed.
- **"Your assurance more than Daniel's": stronger than predicted.** Unprompted: James getting to her core in one 1:1 *"says a lot about Daniel as a manager. Maybe it's just that we are not clicking."* Manager-fit friction on record (n=1, ambiguous phrasing — don't over-read).
- **The vacuum:** solo across teams not her own, no feedback loop, can't map owners/reviewers/approvers; Devin's vacation landed mid-ramp.
- **Wind-down path now concrete and Kim-endorsed:** her own clean cut = ship the unified data pipeline; notifs side has a fallback. She wants to wrap cleanly, "not leave anyone hanging." Dhruvil's release promise + her cut-point = the loan wind-down is now fully sequenced in principle.
- **Cadence claimed: weekly 45-min James↔Kim 1:1s from next week**, working clock = "get somewhere in the next two weeks" (her ~2-week vacation starts end of August).

**Promise-watch note:** James's "big plans for her to drive an important area" line to Dhruvil is now backed by a real cadence — deliver the area conversation inside the two-week window or the promise starts aging.

Announcement out 9am; Dhruvil spent the afternoon talking his own moving reports through it ("range of reactions: this is great / scary before we talked but now great / still not great"). Warm, generous, full alliance-mode — +1'd James's ICs-first instinct, volunteered between-us intel unprompted.

**The Kim dossier (⚠️ 1:1-ONLY — never cite Dhruvil onward; he's her long-time mentor):**
- His instant reaction to "Daniel told me she seems worried": *"Whaaat. This is great for her haha."*
- **"Between us, Kim didn't like working with Yan."**
- She complained to him a lot that **curation is "too 0 or 1"**; felt the Curation EMs *"were getting dragged into too many risky efforts by Curation PM with not much product vision."*
- The worry he'd bet on: *"yet another change, what happens to my career planning etc"* — **their EM and PM leads left "not on great terms not so long ago… the fatigue might be there."**
- **"I'd be surprised if her preferred work is on curation stack based on all she told me, keeping aside the fear of change."**
- His advice: *"I think you talking to her will help 100%. Right now they might need your assurance more than Daniel's is my guess."* The driving uncertainty: *"what their projects / charter / focus will be and reporting will be."*

**His strategic reads:** *"TBH Daniel's team should be thrilled"* (no disrespect to Yan or Curation-as-stack) · **culture may need to shift "more IC driven rather than EM/PM driven — the former is exactly how CG team works today, so it would be a good way to assimilate the cultures too"** · **"Getting Daniel fully on board may be the key."**

**James on record to Dhruvil (promise-watch):** *"really thinking big plans for her to drive an important area for the team"* · Kim on CLR = fast ramp, deep + independent, organized, articulate · *"both deep IC or TL paths may be viable for her"* · *"ICs' opinions are very important — probably even more important than EM tbh"* (Dhruvil +1'd). Dhruvil is her mentor — assume warmth relays; don't arrive at the skip-level pitching a pre-picked area before asking what she wants.

**Embedded datapoint:** Daniel told James 8/5 (channel not yet filed) that Kim "seems worried" — the prompt for James's question.

**Synthesis:** Daniel's "worried" and Dhruvil's "great for her" are both true — fear-of-change on top of a latent preference match. Worry axis = career planning under repeat change; preference likely = retrieval-side work (she's solo on UPP now and complained about curation). Skip-level job: surface HER preference directly, reassure the career axis, seed — not pitch — the important-area line. Her stated preference then feeds the allocation resolution (Yan wants-her-continuing × Dylan wind-down ask): **her voice first, then settle.**

**Relationship note:** the alliance at full function — mentor-grade shading on a shared person, zero territorialism about the loan. The wind-down conversation now has a warm path — **and a pre-agreed one: Dhruvil has promised to release Kim from the loan if it helps her career (James, 8/5).** The wind-down (Dylan's ask) is thus unblocked in principle, conditional on the move actually serving her — which routes back through her stated preference (skip-level first).

## 2026-06-05 — Promo trajectory read + sequencing implication

UPP deck to CEO/CTO this month with Matthew + foundations IC from Dhruvil's team presenting ranking + foundations slides. That public-altitude visibility staging is *exactly* the shape of a promo packet being built. Honest weighted read (limited intel):

**2026-07-09 confirmation:** the packet is real — **Matthew Lawhon nominated IC15 → IC16 this cycle.** James submitted strong support ("Ready now"): CFM-to-fruition as headline, "influence through restraint" maturation since the Jan calibration history. Draft + prior familiarity-gap letter: `work/people/peer_feedback/h12026/promo_assessments/matthew_lawhon_promo.md`.

| Read | Weight |
|---|---|
| Dhruvil promotes end-of-2026 (H2 cycle) | ~45% |
| Mid-2027 (H1 cycle) | ~35% |
| Held / not this cycle | ~15% |
| Other | ~5% |

**Sequencing implication for James:** Director slots aren't infinite per cycle per skip-level. If Dhruvil goes end-of-2026, James's earliest realistic window is mid/late-2027 — **sequenced, not parallel**. Consistent with 5/9 timing correction (Director target mid/end-2027). Not a slowdown — the realistic shape of Dylan's promo-bandwidth allocation across ML EM peers.

**Frame to hold:** Dylan's support of Dhruvil's runway ≠ knock against support for James. Different verticals (Foundations+Ranking ↔ AI+Anticipation+Reflex), different cycles, both going well. Not zero-sum. See `dylan_archive.md` Appendix III-C (team-design chapter) 2026-06-05 entry for full read.

## Role in my 6–12 month goals
- **High-leverage peer relationship:** tight alignment between **Candidate Generation ↔ Ranking** materially improves quality, velocity, and credibility of Homefeed outcomes.
- **Coalition partner** for platformization and cross-org bets (e.g., personalization platformization, shared infra/interfaces).
- **Executive mirror:** working effectively with Dhruvil is a forcing function for “quiet authority” — calm, precise, low-drama leadership under ambiguity.

## Current trust state
- **Trust level (overall): High (Solidified via 'Crisis' Resolution).**
  - **Evidence:** relationship evolved from rivalry → functional ally → **emotional ally**.
  - **Recent Pivot:** Successfully navigated a high-stakes disagreement (Matthew promo) by building deep empathy ("us vs. the situation") and restoring trust through vulnerability.
  - **Confidence:** Very High.

### Trust dimensions
- **Technical respect:** High
- **Execution predictability:** High
- **Strategic alignment:** High (reinforced by shared "hand-in-hand" stance on difficult personnel decisions).
- **Political alignment:** High (moved from "competing for scope" to "protecting each other's flank").

## DISC profile (inferred)
**Primary:** **High S (Steadiness)**
**Secondary:** **High C (Conscientiousness)**
**Tertiary:** **Reactive D (Dominance under threat)**
**Low:** **I (Influence)**

### What this means behaviorally
- **High S:** seeks stability, harmony, and clear ownership; struggles when responsibility shifts midstream.
- **High C:** dives into details when uncertain; asks many questions to regain control and avoid being wrong.
- **Reactive D:** when sidelined or exposed, may grab process control.
- **Low I:** limited sensitivity to relational or political cues.

> **Implication for me:** Dhruvil craves **Safety** and **Partnership**. When I frame problems as "Me + Dhruvil vs. The Issue," his defenses drop and he collaborates deeply.

## What Dhruvil likely optimizes for
- **Quality and correctness** in ranking outcomes; strong bias toward protecting metrics and UX integrity.
- **Stable interfaces** between CG and Ranking to minimize operational churn.
- **Low-drama execution:** prefers calm, measured, evidence-backed decisions.
- **Predictable ownership:** clarity on “who owns what” matters more than speed.
- **Safety in leadership:** Values having a peer who validates the difficulty of management challenges (e.g., "Matthew case").

## Communication preferences
### Known / observed
- Responds best to **structured, calm, option-oriented** updates.
- Values **explicit ownership boundaries** and written clarity.
- **New Insight:** responds powerfully to **vulnerability and alliance framing** ("We are in this together").
- Appreciates when you give him **autonomy** on decisions impacting his team (e.g., promo decision) rather than dictating.

### Uncertain / to validate
- Preference for async memos vs live debate when disagreeing.
- Tolerance for speculative ideation vs proof-first posture.

> **Working default:** short pre-align → written clarity → explicit ask.
> **Crisis default:** Face-to-face empathy sync; frame as "coalition vs. problem."

## Key history (high-signal)
- **Rivalry → ally transition:** early comparison dynamics reframed into curiosity and collaboration.
  *(Confidence: Medium–High)*
- **Matthew Calibration (Jan 2026):** A watershed moment. Initial friction (lack of pre-alignment) was converted into deep trust via a 1-hour empathy sync. Dhruvil admitted vulnerability (difficulty of management); James framed it as a joint battle. Result: "Hand-in-hand" alliance.
  *(Confidence: High)*
- **Cross-team investigations:** you’ve led multi-team debugging with Dhruvil as a partner.
  *(Confidence: High)*

## Dhruvil’s likely current narrative about me
> “James is a trusted partner. He respects my autonomy (letting me decide on promo) but backs me up on the hard stuff. We can face difficult political/personnel situations together without fighting each other.”

- **Confidence:** High.

## Risks with Dhruvil (and mitigation)
- **[Risk] Silent misalignment** between Ranking and Retrieval goals/metrics
  - **Mitigation:** align on KPIs, guardrails, and owner early; document decisions.
- **[Risk] Ownership insecurity** leading to process grabs (meetings, deep dives)
  - **Mitigation:** proactively frame changes as *protecting his bandwidth*, not sidelining.
- **[Risk] Blindsiding him with feedback** (triggers High S/C insecurity)
  - **Mitigation:** **Always pre-wire** sensitive feedback 1:1 before group settings. (Lesson learned & applied).

## What increases Dhruvil’s trust fastest
- **Alliance framing:** "Me + You vs. Problem."
- **Respecting autonomy:** Giving him the final call on his direct reports (e.g., promo/rating combo) while offering strategic advice.
- **Vulnerability:** Acknowledging the difficulty of the job.
- Early pre-alignment, especially when Dylan’s guidance is evolving.

## What could damage trust
- **Surprise feedback in public forums** (The "Matthew" mistake — never repeat).
- Publicly signaling reduced ownership without protective framing.
- Overconfident or speculative claims without guardrails.

## Operating plan (how I work with Dhruvil)
- **Default artifact:** 5-bullet pre-align note before cross-cutting work.
- **Crisis Protocol:** Immediate 1:1 sync; apologize for process/timing (not content); re-establish "us vs. them" frame.
- **Cadence:** biweekly peer sync or lightweight async check-ins during active initiatives.
- **Escalation threshold:** if a tradeoff threatens a KPI or launch timeline, align within **48–72 hours**.

## Pros / Cons of my current approach with Dhruvil
### Pros
- Strong technical alignment and shared rigor.
- **Deep emotional safety** established through crisis resolution.
- Clear path to unified front for platformization.

### Cons
- Risk of moving too fast when stakes feel personal (must remember to slow down and pre-wire).
- Requires time investment (long syncs) to maintain the emotional bank account.

## 2026-07-17: Silo-then-demand M.O. documented + the SGI 1:1 that resolved it (for now)

**The pattern (James's accumulated observation, receiving end, repeated):** Dhruvil's teams build infra/cost-savings plays (Galaxy feature store, pipeline merging, training-data consolidation) in silo, present at exec altitude first, then arrive at customer teams with pre-blessed asks — "leadership thinks this is important," "we've already presented to the execs," "fund it, give me people." Erodes trust regardless of business merit. **Cross-org confirmation 7/17:** same friction inside Kurchi's SSJ org (see §27 Sai + §47 Tie), which Kurchi is converting into UPP concerns (see Kurchi chapter 7/17 entry).

**The 1:1 (~7/16–17) — curiosity instead of feedback, and it worked:**
- Live case: **SGI ("Scorpion Galaxy Integration" per dictation — verify expansion)** — pre-blessed cost-savings ask landing on James's team. James's own read: **right tactical direction**; target = finish within H2; **low time pressure** (defuses the aggressive-urgency part of the pattern for this case).
- James had been about to deliver pattern-level feedback ("jumped the gun" — his words); held it, asked questions to understand instead → **arrived at a solid joint plan for what's next.** Register: **"us vs. the problem," not "him vs. me"** — the alliance frame this profile documents as his fastest trust-builder, confirmed in the wild again.
- **SSJ friction intel deliberately NOT raised** — held for possibly-later; felt no need in the moment. Source hygiene held: Sai/Tie never surfaced.
- **Reorg discussed laterally, both gracious.** Interim operating agreement: **minimal changes; let the ICs keep deciding collaboration patterns** — parts of Dhruvil's new team already collaborate closely with James's team on Retentive Recs, and parts of James's new (inbound) team already collaborate closely with Dhruvil's current team around UPP.
- **Dhruvil has been Kim (Toy)'s mentor for quite some time** (his own disclosure) — a lever for the eventual deliberate transition of her loaned time (`reorg_july2026/daniel_liu_team_2026-07.md` roster) and for her development; use at some point.

**Held in pocket (unspoken):** the operating-protocol ask (customer-team co-design *before* exec presentations; co-owned savings numbers, framed as UPP governance). The SGI conversation went well enough that the pattern-level conversation rides on a future incident, if one comes.
  
---  
  
# 4) Rajat C — Skip-Level VP (Discovery / Personalization)  
  
## Role in my 6–12 month goals  
- **Primary shaper of org design and platform direction** (reorg, consolidation, ownership boundaries).  
- Sets the **bar for what “good” looks like** in personalization, discovery, and ML systems.  
- Long-term **sponsor or limiter** for director-level scope expansion.  
- Implicit evaluator of whether I am:  
  - a *strong functional EM*, or  
  - a *system-level leader who can own a platform pillar*.  
  
> **Key insight:** Rajat is not optimizing for local wins. He is optimizing for **org leverage, platform coherence, and velocity at scale**.  
  
---  
  
## Background signal (what he’s really optimized for)  
- **Founding Alexa leader**; ran Discovery, Personalization, Search, Routines, Agentic Automations.  
- Has lived through:  
  - horizontal platformization,  
  - painful infra / cost tradeoffs,  
  - cross-surface alignment failures,  
  - and reorgs driven by system bottlenecks.  
- Deeply fluent in **Amazon-native concepts**:  
  - *single-threaded ownership*  
  - *mechanism > narrative*  
  - *cost vs value*  
  - *platforms as force multipliers*  
  
> **Translation:** He will respect leaders who diagnose *structural problems* and propose *clean ownership models*, not those who optimize locally or complain.  
  
---  
  
## Likely DiSC Profile (Most Likely)  
- **Primary:** D (Dominant)  
- **Secondary:** C (Conscientious)  
- **Low:** I (Influence), S (Steadiness)  
  
### Implications  
- Values **clarity, decisiveness, and structural fixes** over consensus-building.  
- Has low patience for:  
  - vague pain points,  
  - laundry lists,  
  - or “everyone owns a piece” models.  
- Responds best to:  
  - crisp system diagrams,  
  - explicit ownership proposals,  
  - and tradeoff-aware recommendations.  
- Emotionally neutral; not driven by rapport-building.  
  
> **Operational takeaway:** Be *direct, structured, and solution-oriented*. Don’t over-index on warmth or narrative flourish.  
  
---  
  
## Current trust state
- **Overall trust level:** High (Active Sponsorship)
  - **Evidence:** Rajat championed Option 1 for UPP, called Dylan directly to force alignment, ran hour meeting with Kurchi. Actively protecting UPP thesis. James's team is now central to Rajat's highest priority. Earlier signals: asked explicitly for pain points, infra costs, outages, “what should we stop/start” — system diagnosis mode confirmed. **March 2026:** Gave James Exceeds rating and strong comp. Sent direct message: “I want you to keep pushing and looking forward to partnering on a lot of projects this year.” This is explicit encouragement of James's aggressive operating style from the VP level. **April 2026:** "keep up the good work and keep pushing - lots of exciting and impactful work ahead of us to deliver together" — sustained encouragement mandate.
  - **Confidence:** Very High.

### Early signals validated → matured into active sponsorship
- Pulls James into follow-ups on platform questions — **Yes, actively championing UPP**
- Asks James to “own” or draft something — **Yes, UPP architecture**
- References James's framing in broader discussions — **Yes, explicit alignment calls**
- **Directly encouraging James to maintain intensity** — “keep pushing” is not generic praise; it's a mandate.

### 2026-04-16: New engagement surface — Pinkerton / Reflex fix-loop
- James demoed Pinkerton to Rajat in meeting (Dylan + Andrew Y also present). Rajat DM'd immediately after asking for the monitoring-agent doc, then opened a thread on AI agents for debugging.
- **Rajat endorsed the fix-loop trajectory:** "great! yea that would be a good one to prototype. and hook up e2e" after James described VLM-hooked agents + Andrew Y's survey-response partnership auto-triggering investigation.
- **Implication:** Rajat is now a VP-level stakeholder on Pinkerton and (adjacently) Reflex. Mental anchor is Pinkerton-as-primary-mechanism after James took the demo moment in front of Andrew (who was about to set the Reflex big picture). Political residue: Andrew's Reflex-framing with Rajat is displaced until he reclaims it.
- **Calibration going forward:** sustain the D/C profile rules — direct, structured, solution-oriented; no warmth decoration. Rajat's "hook up e2e" is a mandate to show end-to-end detect → diagnose → fix wiring, not a suggestion.

### 2026-04-25: Dylan stepped in as POC for UIC / RR (engineer-names pattern context)
- **Background (off-channel intel from Dylan):** Rajat has a recurring pattern of pulling engineer names off the team for ad-hoc / "random asks." Dylan said it's not the first time. She has positioned herself as **POC for UIC / Retentive Recs** to absorb that flow and shield the team. Full arc-shift writeup in `dylan_archive.md` 2026-04-25 entry.
- **Why this matters for Rajat-facing posture:** the shield is a structural fact running invisibly. James continues to engage Rajat as the substantive program owner — Rajat is still an active sponsor, the encouragement mandate is still live, and the "hook up e2e" directive is still the primary delivery target. The shield is for friction-flow, not for the relationship itself.
- **What changes operationally:** if Rajat floats coordination, headcount, or anything cross-team during a meeting, the natural answer is "let me sync with Dylan and circle back" — same as for any senior EM. Not defensive, just hierarchy hygiene. Naming workstream owners with their workstream is fine and normal. Volunteering unsolicited engineer rosters is what changes — but that's baseline operating cleanliness, not a Rajat-specific paranoia move.
- **What does NOT change:** James does not acknowledge the shield to Rajat. Does not self-position as political POC for UIC / RR (Dylan owns that channel by design — self-positioning would undermine it). Does not perform around the shield in the OH; just delivers the substance.
- **Strategic read:** Dylan-as-POC is sponsorship escalation. James = builder + technical lead. Dylan = political POC + shield. This is how Director-track operators actually work — having a senior absorb political overhead is what *enables* structural compounding. (Connects to: Operational Embedding lesson, journals_and_growth.md Lesson 7.)

### 2026-06-03: Rajat non-push on CST/CFM block (UPP architecture being unwound from above)
- **Event:** CST (Cross Surface Training) + CFM had massive ranking-side wins. **Kurchi personally blocked the launch**, citing a new relevance metric regression + "executives flagging user perception gaps for P2P relevance." **Rajat did not decide unilaterally to launch in the meeting** — chose not to spend capital pushing back on Kurchi.
- **Read:** Reinforces the existing **"Rajat = complementary sponsor, not primary advancement vehicle"** frame (memory: `project_rajat_complementary_sponsor.md`). Rajat doesn't go to the mat on others' relevance/quality concerns — even when wins are clear. He optimizes for org leverage and platform coherence, not for any single launch fight.
- **Implication for UPP:** The 5/13 architecture James stabilized (UPP = "shared infra surfaces co-own") required co-owners to actually co-own and required Rajat-level air cover for cross-surface launches. With Kurchi now actively blocking AND Rajat not spending capital to push, the co-ownership frame is being unwound from above. Sai's "parallel tracks, handed-a-command" reframe is the downstream cascade (see §27 6/3 entry + §6 6/3 entry).
- **Operating implication:** Don't ask Rajat to fight Kurchi for UPP launches. That's not what he does and it would burn the encouragement mandate without changing outcomes. Run the play in James's own code (P2P FT on Hongtao + Zhihao) and use Dylan as the escalation channel.

### Key dynamic: Rajat vs. Kurchi
- Rajat wants **quarterly milestones** and faster UPP execution. Kurchi pushes back — successfully moved Search from monthly milestones to H2.
- This means Kurchi has **leverage beyond Rajat's chain** (likely directly with Jeff or through tenure/institutional relationships). Rajat cannot unilaterally override her on execution pace.
- James is positioned as Rajat's instrument for UPP velocity, which Kurchi recognizes. This is both an asset (VP backing) and a liability (perceived as battering ram).  
  
---  
  
## What Rajat optimizes for  
- **System velocity**  
  - How fast can the org ship *after* this reorg?  
- **Clear ownership**  
  - Single-threaded owners for backend / ML-heavy efforts (Explore Page, personalization platform).  
- **Cost-aware scalability**  
  - Infra spend tied explicitly to product value.  
- **Cross-surface coherence**  
  - HF, Explore, Search, Notifications behaving like *one discovery system*.  
- **Leadership leverage**  
  - Fewer integrators; more autonomous, high-judgment owners.  
  
---  
  
## Communication preferences  
  
### Known / inferred  
- Prefers **structured overviews**:  
  - architecture → bottlenecks → proposed consolidation.  
- Wants **pain points paired with fixes**.  
- Appreciates explicit:  
  - *“This should live under X”*  
  - *“This needs Y headcount”*  
  - *“This is slowing us down because Z”*  
  
### Avoid  
- Emotional language.  
- Over-contextualizing history.  
- Soft phrasing (“might,” “could,” “we feel”).  
  
> **Working default:** crisp written artifacts + decisive spoken summaries.  
  
---  
  
## Rajat’s likely current narrative about me (early hypothesis)  
- “James seems to understand the personalization and retrieval stack deeply.”  
- “He’s thinking in terms of platforms and ownership, not just feature delivery.”  
- “Potential candidate to anchor a backend/ML consolidation — needs to prove leverage and scale.”  
  
**Confidence:** Medium–Low (early days; narrative still forming).  
  
---  
  
## How I should deliberately position myself with Rajat  
  
### What to emphasize  
- **Single-threaded ownership thinking**  
  - Especially for Explore Page backend + ML.  
- **Platform gaps**  
  - Unified personalization signals, retrieval infra, cost transparency.  
- **Org design implications**  
  - Why certain things *must* be centralized under Relevance backend.  
- **Leader scaling**  
  - Bowen / TLs owning pieces; I own the system.  
  
### What to de-emphasize  
- Local heroics.  
- Tactical firefighting.  
- Over-indexing on interpersonal nuance.  
  
---  
  
## Risks with Rajat (and mitigations)  
  
- **Risk:** Being seen as “another strong EM with opinions”  
  - **Mitigation:** Always pair pain points with *clean ownership proposals*.  
  
- **Risk:** Coming off as defensive or territorial  
  - **Mitigation:** Frame consolidation as *org efficiency*, not personal scope.  
  
- **Risk:** Over-sharing complexity  
  - **Mitigation:** Default to 3–4 structural issues max; go deep only when asked.  
  
---  
  
## What will increase Rajat’s trust fastest  
- A **small number of high-quality, system-level insights** that explain:  
  - why things are slow,  
  - who should own what,  
  - and what to stop doing.  
- Demonstrating that **frontend vs backend mismatch** (e.g., Explore Page) is an org design problem — and proposing the fix.  
- Showing you can **carry director-level ambiguity without drama**.  
  
---  
  
## What could damage trust  
- Vague or people-focused complaints.  
- Long lists without prioritization.  
- Framing problems without clear accountability models.  
  
---  
  
## Operating plan (how I work with Rajat)  
- **Default artifact:** system map + 3 pain points + ownership proposal.  
- **In meetings:** speak early, concisely, and then stop.  
- **Follow-ups:** written summaries with explicit “recommended path.”  
  
> **Meta-goal:** be seen as a *force multiplier* who reduces org entropy and makes the reorg obvious — not someone lobbying for scope.  

# 5) Jeff H — Skip-Level Sponsor (VP of Core, Rajat's manager)

**2026-08-21 — He's hosting the CE Managers Offsite (Asilomar, 9/15–17), his org and his travel budget.** Org fact established same day: **CE = Content Engineering**; **SSJ reports into Rajat, who reports into Jeff**, so Kurchi's org is inside this one. Faisal, Shipeng and Bo Zhao also report to Jeff. Format is deliberately summer camp — arts and crafts, campfires, alcohol, one carved-out business block on Wed 9/16. **This is his native terrain and it rewards exactly what the profile says: connection and vibes, not artifacts.** The operational takeaway holds inverted here — at camp the currency is being good company, and working the room with an agenda is the failure mode. Plan of record: `../career/ce_managers_offsite_2026-09.md`.

## Role in my 6–12 month goals
- **The "Scope Expander":** Actively pushing you to be "more ambitious" and look beyond Homefeed. He is the bridge to **Goal #4 (Expand Internal Network)**.
- **Sponsor of "Modernization":** He views your work (AI/Agentic workflows) as the template for the future of Core engineering.
- **Cultural Validator:** Offers high-level air cover for "vibe" and experimentation, which balances Dylan's focus on risk/rigor.

## DiSC Profile (Inferred)
- **Primary:** **I (Influence)**
- **Secondary:** **D (Dominance)**
- **Low:** C (Conscientiousness) — *relative to Dylan*

### Implications
- **High I:** Values connection, "vibes," and storytelling. The fact that you bonded over skiing/kids was a major trust accelerator. He wants to feel *excited* about the work.
- **High D:** Results-oriented but flexible on the "how." He didn't ask for a spec; he asked for a *forum* (action).
- **"Cool" Factor:** He is attracted to "cool work" and novelty. He wants to be associated with the cutting edge.

> **Operational takeaway:** Don't bring him problems; bring him **prototypes and energy**. He wants to be inspired, not managed.

## Current trust state
- **Overall trust level: High (Accelerating after 5/7 OH)**
  - **Evidence:** Immediate sponsorship of the AI forum ("Now you're on the hook for this"); the invitation to partner with Amanda; the relaxed office hours dynamic. **5/7 OH: Jeff offered TWICE unprompted to come talk to my team — *"It would be a highlight of my week."* Commissioned a predicted UIC demo on his own profile (sent his user ID live).**
  - **Confidence:** High.

### Trust dimensions
- **Cultural Fit:** Very High (Shared interests, relaxed communication style).
- **Vision Alignment:** Very High (He sees AI-first cross-functional transformation as the agenda; we are executing on it cross-functionally per his read).
- **Execution:** Proven (Reflex EPD demo 5/4 + UCAN WAU result + cross-org adoption pattern + predicted UIC mid-arc).

## VP mental-model state (5/7 update)
- **Pre-OH ~0-10%** (RR not in his picture; PINvestigator + general AI-in-HF only).
- **Post-OH ~55-65%** (Anticipation thesis + James-as-cross-functional-lead-alongside-Andrew/Dylan installed; UIC translated back in his own "persona perspective" framing; predicted UIC demo committed).
- **Gap to 75% target:** Pin polysemy moat (Beat 2) + Notif CLR adoption proof (Beat 3) + Engineering Blog post 4/17 + KDD 2026 paper — **all durable verifiable artifacts NOT yet introduced.** These are the Beat 2-3 install moves left for next touchpoint.
- **Engineered moments left:** (1) predicted UIC demo on his profile (3-day SLA), (2) team visit (lock date in 48h), (3) post-predicted-UIC follow-up.

## What Jeff H optimizes for
- **Engineering Culture & Modernization:** He wants Core to evolve. He is looking for "spark plugs" who can infect the broader org with new ways of working (e.g., Cursor, Vibe Coding).
- **Cross-Pollination:** Breaking silos between Homefeed and Core.
- **Ambition:** Explicitly told you to aim higher. He values leaders who try to change the system, not just their component.

## Communication preferences

### Known / observed
- **Casual & Human:** Responds well to "light reminiscing" and non-work bonding (skiing, family).
- **"Show, Don't Tell":** The "vibe coding" demo (or description of it) worked instantly. He prefers demos/results over decks.
- **Asymmetric Asks:** He is comfortable giving loose mandates ("Why don't we do something together?") and expects you to fill in the operational details with his EA (Amanda).

> **Working default:** Treat him like a VC sponsor. Pitch the vision + the win, then handle the logistics with his staff.

## Jeff’s likely current narrative about me
- **Positive core (post-5/7 OH):**
  "James is one of the people executing the AI-first cross-functional shift I keep pushing for. He's working it cross-functionally with Andrew + Dylan. His team's anticipation work is producing real WAU gains and is the substrate underneath what I saw at EPD. He's also leaning in on adoption — actively bringing his stragglers along the way I've been describing. I want to come talk to his team."
- **Watch-out:**
  "Can he scale this energy to the broader org without getting bogged down? Is the substrate story (Pinkerton underneath Reflex) holding under more orgs adopting it?"

## Jeff's verbatim language to file (5/7)
- **"Persona perspective"** → Jeff's own framing for predicted UIC. Use this verbatim in calibration / next touchpoint. He'll repeat his own words.
- **"Spec-driven product development"** → his complaint about a 16-page PRD; wants one-page strategy + spec-checked-into-code. Adjacent to UPP charter framing.
- **"Pinterest is investing in everyone's future"** (Jeff amplified Faisal's framing) → AI adoption framing he loves. Adopt this verbatim when discussing team adoption.
- **"Came up with the anticipation? Yeah. I was there."** → claims co-witnessing of original anticipation moment. Reinforces ownership chain that includes James.
- **"Pockets of the team being really good at adoption... others need to be pointed in the right direction... give them the time and space and tooling"** → Jeff's adoption-stragglers model. Mirrors PayPal infra-shift wave pattern.

## Risks with Jeff (and mitigations)

- **Risk: Bypassing the Chain (The "Dylan Gap")**
  - **Context:** Jeff is high-energy/informal. He might greenlight things that Dylan hasn't vetted.
  - **Mitigation:** Always "cc" Dylan or pre-wire her: *"Jeff and I chatted about X; I’m going to run a pilot per his suggestion."*

- **Risk: "Flash over Substance"**
  - **Context:** He likes the "cool" factor. If the Feb 2 pilot is all flash and no engineering utility, trust will evaporate.
  - **Mitigation:** Ensure the "How I AI" session is grounded in *hard engineering workflows* (architecture, debugging), not just "magic tricks."

- **Risk: Scope Creep without Resources**
  - **Context:** "Let's do a forum for Core" is a big ask with zero headcount attached.
  - **Mitigation:** Frame it as "scaling what we already do" (pilots, recordings) rather than a net-new program that eats your management bandwidth.

## Operating plan (how I work with Jeff)
- **The "Pilot" Strategy:** Never commit to a massive program upfront. Commit to a "v1" or "trial run" (like the Feb 2 session) to validate value.
- **Artifacts:** Send him **recordings and 1-pagers** of cool things. He will forward these to other execs.
- **Cadence:** Quarterly "Vision/Ambition" check-ins (Office Hours are perfect). Keep tactical updates for Dylan.

> **Meta-goal:** Position myself as his **"primary source of ground truth"** for how AI is actually changing the engineering workflow on the ground.

## 2026-07-22 update — Jeff's three priorities (via Dylan) + EM review + culture-change mandate

Dylan brought James + Dhruvil **three priorities she's carrying from Jeff**; a quick EM review with Jeff laid out his challenges directly.

**The three priorities:**
1. **See More / See Less (SM/SL).** A **Bill Ready (CEO)** focus area → must be staffed. James's response already in motion: Yali drives retrieval side + Raymond Hsu; talking-points meeting with Andrew/Lily/Michael/Dylan on 7/23 (see `reorg_july2026/reorg_followups.md` #1).
2. **AI / GPU usage down.** Dylan emphasized. **James has an operational plan — handled** (tracked in `work/projects/cost_investigation_2026.md`); no action needed from Leo, just logged as important.
3. **Cost tracking.** The org sits under Jeff's Core org **~$5M/yr over budget**; James's own dig found **>$1.8M/yr over under Dylan alone.** James is **driving the budget investigation for Dylan starting 7/23** — ICs + team leads being looped; Dhruvil pre-warned, will lend someone. Full workstream: `work/projects/cost_investigation_2026.md`.

**Culture-change mandate (the big one).** Jeff wants the org **working differently** — he repeatedly cited **AI pods: cross-org virtual teams that move fast and deliver with little process.** He wants teams to **build bottoms-up without heavy leadership alignment**, because *alignment is what's slowing things down.* Delivered in the meeting and reinforced in Dylan's follow-up 1:1. **Strategic note:** this is near-identical to the pod-autonomy / own-a-problem-move-without-permission theme in James's org-design docs (currently an undercurrent) — Jeff's mandate makes naming it explicitly a *read-the-room* move, not overreach.

**Motivation / political read (from Dylan's follow-up):** the culture push likely traces to Dylan telling Jeff about the **difficulty working with SSJ on UPP** (SSJ's blocking → "partial/tenth-full UPP" framing — controlling a subset of UPP projects while keeping their eng resources; even Jaewon is fed up, pushing "substance over packaging" — see `upp_retrieval_em.md`). Dylan's lever to *motivate Jeff*: **Matt Madrigal's (CTO, Jeff's boss) priorities center on ads** → collaboration-with-ads is Jeff's incentive. Her framing: *"if it's this hard to get leaders to work together under Jeff in Core, how does it work when we go to ads?"* Jeff responded immediately by having **Andrena (Director, TPM — new §48)** lean into the ads-collaboration area. **James's move:** surfaced the upcoming **UPP-retrieval-in-P2P launch candidate** to Dylan as the proof point → Dylan: *"that's great, let's use it as an opportunity to push things forward."*

---

## 2026-09-02 — EM sync: the freeze goes public, EM offsite + travel cancelled; "free to paid," "Code Red in Ads," "strategic growth efforts"; James's two-beat question landed

James live in the room (remote session, Leo as live read + question design). Jeff announced the **hiring freeze** (the one Dylan pre-disclosed 9/1 under "don't tell anyone" — now public; James heard it fresh in the room and did not reference her), **cancellation of the EM offsite and of travel** (→ the CE Managers Offsite 9/15–17, `../career/ce_managers_offsite_2026-09.md` ⟨confirm it's that one⟩; Dylan's EM/leads offsite falls with it per James ⟨unconfirmed⟩). He opened for questions and discussion, then talked **"free to paid," "Code Red in Ads," and "strategic growth efforts."**

**James asked (verbatim, two beats):** *"If the Code Red is in Ads, what's the front door for Core teams to plug in? Do we find our own counterparts in Ads, or is there a named interface so we don't all show up separately? And for the teams that don't get tapped, what are the two or three things you want to make sure still move at full speed?"* → James, after: **"Both parts of the question landed super positively."** Jeff's answers not captured — debrief next session (front door = Andrena? a named interface? what did he name to protect?).

**Why it was the right question (for reuse):** beat one is Dylan's own July lever (*"if it's this hard to get leaders to work together under Jeff in Core, how does it work when we go to ads?"* — which Jeff answered then by pointing Andrena at ads collaboration) asked back to him in his own forum: it asks for the *system*, doesn't volunteer the team. Beat two covers the org's capacity, not James's seat, with a number in it so "everything" can't be the answer — whatever he didn't name is what James is licensed to slow. Framed toward *prioritize/protect*, not *stop* (James's reframe): positive framing gives him a runway to lead in a room absorbing bad news. **Deliberately not asked:** REQ-2/Richard (James: fine to lose the HC); Zili / perf-exit backfills (Dylan's channel); the infra-cost-tool ownership gap (Dylan first — `../projects/cost_investigation_2026.md` 9/2); and the ambitious *"should Core platforms serve Ads directly rather than Ads building parallel stacks"* line — his "aim higher" taste, but a public UPP-into-Ads claim while Dylan's "closed door, proceed with caution" on ads-side AI collaboration stands (9/1: watch, don't re-ask).

**Verbatim language to file:** "free to paid" · "Code Red in Ads" · "strategic growth efforts". Use his words back — he repeats his own.

# 6) Kurchi — Peer Senior Director (SSJ: Search, Shopping, Journey)

**⚠️ 2026-08-21 — She is attending the CE Managers Offsite (Asilomar, 9/15–17), same two nights as James.** Two live and opposed facts in one room: (a) James holds Dylan's closed-laptop disclosure that the UPP×SSJ collaboration may stop ~9/30 — no disclosure, no visible posture change, no new SSJ-UPP commitments; (b) **her 8/7 back-channel invitation is still unused** and both her stated gates looked cleared as of 8/13, while the P2P launch must land before ~9/30 or exits the Exceeds case. Play: 30 seconds, register-matched to her C-profile — *the off-topic tail numbers moved, can I send you the writeup* — earning the right to send receipts, not pitching at a campfire. Landing P2P is precisely what Dylan sanctioned ("let's land, and let's escalate where needed"). Tripwire: camp intimacy plus alcohol manufactures commitments beyond the landing. Full tripwire list: `../career/ce_managers_offsite_2026-09.md` §3.

## Role in my 6–12 month goals
- **Primary political counterweight to UPP expansion.** She controls the surfaces (Search, P2P) that UPP must expand to for the platform thesis to hold.
- **Gatekeeper for IC access.** Her org's engineers (Jinfeng, Krishna, Huizhong's reports) are the ones who must engage for cross-surface scoping and co-design.
- **The relationship that determines whether UPP succeeds through collaboration or attrition.** If Kurchi actively cooperates, Q2 cross-surface goals are achievable. If she slow-plays, progress stalls regardless of Jeff/Rajat support.

### 2026-08-07 — Post-launch-review posture: conditional invitation, not block (group DM w/ Piyush, Jiaxing, Zhenjie)

- After the UPP P2P launch review, Kurchi restated the bar plainly and **invited the ship**: relevance "down to neutralish to −0.3 ish range"; her stated worry is narrow — "the complete off-topic ones (cat for nails, monkey for cartoon, bedroom for outdoor pool etc)." Then: **"Feel free to back channel and bring it to me once those very off topic pins are taken care of."**
- Read: the posture arc has moved active-block (6/3) → ownership-wrestle in process clothing (7/17–7/27) → **conditional invitation with a named, finite bar and a personal back-channel offer** — the strongest cooperation signal on record from her. Consistent with her C-profile: she committed to evidence-conditioned support, which for her is real commitment.
- Same thread: **Zhenjie Zhang confirmed P10 WAU is blocking** ("key P2P OKR… does look blockering") and asked Piyush to size better-P10 sampling — the second gate now has a cooperative owner rather than an adversarial one. Piyush's metric-definition clarifier (b2.5_precision@4 vs b1.5_precision@8) still open.

### 2026-08-13 — Her stated bar now arguably met; back-channel pending

- James's 8/13 status: **P10 WAU negative → neutral** (Zhenjie's gate condition no longer holds) and **the relevance regression is not stat-sig** (James: "Kurchi just made a big deal out of it"). Both 8/7 gates look cleared **on her own stated metric bar**; the off-topic-tail half of her worry (the part she emotionally weighted) has no evidence status captured yet.
- Plan (Leo rec, unratified): use her own invited back-channel WITH tail-cleanup receipts before any Jeff escalation — her invitation is the cheapest channel on record; escalate via Dylan→Jeff only if the stated bar moves, which would then be a clean case ("the written bar was met; it moved"). Full state: `work/projects/upp/upp_retrieval_em.md` 8/13 entry.

### 2026-08-20 — Feedback collection on Huizhong, routed through Dylan; James's read: building an out

- Kurchi asked Dylan for feedback on **Huizhong**; Dylan fanned the ask out to James ("fact driven and candid… I will synthesize and share"). James's read (hypothesis): with the UPP-SSJ churn escalating toward Dylan's ~9/30 wind-down consideration, Kurchi is assembling a **Huizhong-shaped explanation** — "using Huizhong as an out" — rather than owning org-level inconsistency. In-pattern with her documented candor-when-it-positions ("promotion not warranted" to Dylan) and her lieutenant-loyalty structure (Jinfeng IC18).
- Precedent James cites: Ravi/notifications (Dylan + Shupeng → Ravi out). Full entry + James's submission strategy: `dylan_wang_archive.md` 8/20.
- Operational: James's submission kept limited-vantage, first-hand, system-attributed — honest with Dylan without arming the case.

## DiSC Profile (Inferred)
- **Primary:** **C (Conscientious)** — leads with "I need data," "show me the evidence," reasonable-sounding process demands
- **Secondary:** **D (Dominant)** — fiercely turf-protective, will push back on Rajat directly, doesn't fold under VP pressure
- **Low:** I (Influence), S (Steadiness)

### Implications
- Uses **reasonableness as a weapon** — "I need data before committing" sounds fair and *is* fair, but it also maintains optionality and keeps her influence over architecture decisions alive.
- When caught without her delegates' prep, goes **reactive and defensive** (observed in Jeff's "what would it take for Search?" question).
- Most effective **behind the scenes** — pre-wiring, coalition-building, controlling narrative before the room meets. James has not seen her in this mode directly, which is a visibility gap.
- Delegates technical details to lieutenants (Jinfeng, Krishna) and fights the political air war herself.

> **Operational takeaway:** Don't try to out-politic her. Make yourself *safe* — credit her org's work, name her people positively, demonstrate that UPP gives SSJ more, not less.

## Background & Political Context
- **Political veteran.** Has survived and thrived under multiple VPs of Discovery at Pinterest. This is rare and signals deep institutional relationships — likely directly with Jeff or other senior leaders beyond Rajat's chain.
- **Not deeply technical**, but extremely sharp politically. Knows how to read rooms, build coalitions, and time her moves.
- Recently had **Huizhong's P2P org rolled under her**. Told Dylan she doesn't believe Huizhong's promotion from Sr. EM to Director was warranted — signals willingness to be candid with peers when it serves her positioning.
- **Promoted Jinfeng to IC18** despite his reputation for weak technical output. This is a loyalty signal — she rewards political alignment and org defense, not just technical contribution. Jinfeng is her champion in technical debates.

## Org structure (under Kurchi)
| Person | Role | Notes |
|--------|------|-------|
| Krishna | Sr. EM, Text Search Relevance | Long-standing report. Past collaboration with Dhruvil built trust. |
| Huizhong | Director, P2P Backend/ML → Closeup & Multimodal Relevance (org note 8/1) | Recently rolled under Kurchi. Kurchi skeptical of her promotion. Making IC access difficult (early UPP; unblocked after Rajat's decision). **8/20: subject of a Kurchi-originated feedback collection via Dylan** — James's read: scapegoat-in-progress for the UPP-SSJ churn. James likes her personally; Sai's private read on her (§27, protected) is the only negative on file and stays out of anything chain-readable. |
| Jinfeng | IC18, P2P ML Lead | Kurchi's lieutenant. Fights technical battles on her behalf. Pushed for P2P LR as base model. Now co-designing UPP CLR after Dylan/Rajat forced alignment. |

## Current trust state (with James)
- **Overall trust level: Neutral / Wary → Slightly Warming**
  - **Evidence:** Limited direct interaction. She's seen James in calibration rooms (his case succeeded, signaling leadership backing). ML Day coordination built light goodwill. But structurally, James is the execution engine behind the thing threatening her org's technical identity.
  - **New signal (March 30, ELT):** Gave thumbs up during ELT Dynamic Triggering presentation — specifically on RP cost savings ($680K, majority of shipped impact) and cross-surface results. First positive public signal from Kurchi on work James presented. Context: James prominently credited Sai (SSJ/RP) during the presentation.
  - **New signal (March 30, MW):** Came in silent as a bloc with Huizhong, Jinfeng, Sai — coordinated watching brief. First thumbs up was on "business objectives unchanged by UPP." Hearted Jeff's "not a foregone conclusion" comment. Raised semantic relevance and credited Jinfeng. Asked a real technical question (base vs. finetuning features). Seemed to support Jaewon's MoE design. Thumbed up Dylan's relevance measurement point. **Jeff called her out directly (jokingly): "Kurchi don't think you're getting out of things here."** Assessment: positioning around relevance, not blocking. More constructive than silence alone suggests.
  - **Confidence:** Medium. James has a visibility gap on how she operates when effective.

### Trust dimensions
- **Competence recognition:** Medium-High. She's seen the calibration results and knows Jeff/Rajat back him.
- **Political threat assessment:** High. James is Dylan's most effective operator and Rajat's instrument for UPP velocity. The Option 1 escalation went over her head and forced her hand — she'll remember that.
- **Personal rapport:** Low. One intro 1:1 (no follow-up), ML Day goodwill (thin), bar raiser stint (minimal engagement).

### How she likely sees James
> "James is Dylan's guy — competent, aggressive, gets things done. He's the one who triggered the Rajat escalation that forced Option 1. I respect the impact but he's not my ally. He's the battering ram for the platform that could subsume my org's technical identity."

## What Kurchi optimizes for
- **Turf protection through ownership, not obstruction.** She won't fight UPP directly (Jeff/Rajat too strong), but she wants her org to *drive* the technical strategy, not adopt someone else's.
- **Origination over adoption.** Jinfeng's "rebuild using P2P LR codebase" play was Kurchi's strategy in architecture form: if the base model is built on SSJ's code, the innovation flows *from* SSJ outward.
- **Relevance as her differentiator.** This is SSJ's one technical area where they lead and personalization hasn't solved it. She'll keep this front and center to maintain architectural influence.
- **Her people's careers.** Protecting and promoting her reports (Jinfeng IC18) builds deep loyalty and ensures her org fights for her interests in technical forums.
- **Maintaining optionality.** "I need data" buys time, preserves her influence over design decisions, and looks reasonable to leadership. She won't commit until she has to.

## Communication preferences

### Known / observed
- Delegates details; don't expect her to go deep on architecture. Her lieutenants handle that.
- Responds defensively when challenged without prep time.
- Uses process-oriented language ("let's review both approaches," "I need data") that is simultaneously reasonable and strategic.
- Receptive to **credit and recognition** of her org's contributions (ML Day positive signal).

### Uncertain / to validate
- How she operates in 1:1 vs. group settings (James has mostly group signal).
- Whether she responds to direct alliance-building or views it as manipulation.
- Her tolerance for James engaging her ICs directly vs. going through her.

> **Working default:** Credit her org publicly. Go through her (or Dylan↔Kurchi channel) for political asks. Engage her ICs only on clearly scoped technical work.

## Relationship dynamics

### Kurchi ↔ Dylan
- **Tenuous.** Adversarial undertone. Dylan is visibly nervous about this political battle.
- Kurchi sees Dylan's org (personalization) as the vanguard of rec systems — a threat to SSJ's relevance and independence.
- They are peer directors under Rajat, but the power balance favors Dylan on the UPP thesis because Jeff and Rajat are backing it.

### Kurchi ↔ Rajat
- She can **push back on Rajat and make it stick** (pushed Search from monthly milestones to H2). This suggests leverage beyond the Rajat chain — likely direct with Jeff or through tenure/institutional relationships.
- Rajat has forced her hand on Option 1 ("disagree and commit"), but she retains meaningful influence on execution pace and design direction.

### Kurchi ↔ Dhruvil
- **Positive.** Past collaboration between Dhruvil's ranking team and Krishna's search relevance team built real trust. She favors Dhruvil among the personalization EMs.

### James ↔ Krishna (Kurchi's most trusted lieutenant)
- **Strong.** James has a good direct relationship with Krishna — Krishna is reasonable, enjoys talking to James, and is Kurchi's most trusted report. This is a significant trust channel into Kurchi's org, potentially even more direct than the Dhruvil bridge. How to leverage this strategically is TBD but the rapport is real.

### Kurchi ↔ Jeff
- Likely has a **direct or long-standing relationship** that gives her air cover Rajat can't override. She's outlasted multiple VPs — she knows how to maintain executive sponsors.

## Risks with Kurchi (and mitigations)

- **Risk: Being seen as Rajat's battering ram**
  - **Context:** Rajat explicitly told James "keep pushing." Kurchi will pattern-match every aggressive move as VP-backed encroachment.
  - **Mitigation:** Let Dylan and Rajat fight the political air war. James should be the *practitioner*, not the *advocate*. Credit SSJ's work. Name Jinfeng positively. Make co-design feel genuine.

- **Risk: Slow-play through "reasonableness"**
  - **Context:** "I need data" and "let's review both approaches" are simultaneously fair *and* strategic delay tactics. Hard to counter without looking unreasonable yourself.
  - **Mitigation:** Don't fight it. Produce the data. Make the evidence so clear that delaying becomes harder to justify. Notif results (+156k WAU shipped, +130k in-flight) are the strongest counter.

- **Risk: Jinfeng re-litigating through architecture**
  - **Context:** Krystal warned "let's see if we don't re-litigate next week." Jinfeng could steer co-design toward P2P LR with CLR elements rather than CLR with P2P elements.
  - **Mitigation:** Jaewon is co-leading the design and is technically credible with both sides. Ensure the co-design artifact is CLR-based with P2P extensions, not the reverse. Flag to Dylan if the architecture drifts.

- **Risk: Alienating her by cutting her out**
  - **Context:** The Option 1 escalation worked but went over her head. Repeating that pattern will harden resistance.
  - **Mitigation:** Involve, don't bypass. The co-design framing gives Jinfeng real ownership. Extend this posture — make SSJ feel like co-authors, not adopters.

## What increases Kurchi's trust in James
- **Crediting her org's work publicly** — especially relevance contributions and Jinfeng's co-design role.
- **Producing data, not promises.** She asked for evidence; delivering it earns respect even if the results favor UPP.
- **Not escalating over her head again** unless absolutely necessary. The Rajat play worked once; doing it repeatedly will make her an active enemy rather than a cautious skeptic.
- **Leveraging the Krishna relationship.** James has strong direct rapport with Krishna, Kurchi's most trusted lieutenant. This is the highest-fidelity trust channel into Kurchi's org — more direct than the Dhruvil bridge.
- **Building rapport through Krishna/Dhruvil bridge.** The Dhruvil↔Krishna relationship is an additional organic trust channel. Use both.

## What could damage trust
- Escalating to Rajat without giving her a chance to engage first.
- Overclaiming on timeline or results — she will fact-check.
- Framing co-design as "SSJ adopting UPP" rather than genuine joint work.
- Undermining Jinfeng's reputation (even if justified) — he's her promoted champion.

## Operating plan (how I work with Kurchi)
- **Default posture:** Practitioner, not politician. Be the person with shipped results and operational answers, not the person advocating for a platform.
- **In shared rooms:** Credit SSJ contributions. Name Jinfeng and Krishna positively. Let Dylan/Rajat make the structural arguments.
- **Direct engagement:** Look for natural opportunities to build rapport (similar to ML Day). Don't force a political alliance — she'll see through it.
- **Through Dhruvil:** The Krishna↔Dhruvil trust channel is the one organic bridge. Use it for soft alignment where appropriate.
- **Escalation threshold:** Only escalate to Dylan/Rajat if Kurchi's team is *actively blocking* scoped work, not if they're moving slowly. Slow-play requires patience and evidence, not escalation.

> **Meta-goal:** Shift from "Rajat's battering ram" to "the practitioner who made SSJ's surfaces better." That's the only narrative that converts Kurchi from skeptic to neutral — and neutral is a win.

## 2026-07-17: Converting Dhruvil-M.O. friction into UPP concerns

- **Intel (1-hop, direct):** Sai + Tie (P2P Ranking EM, §47) told James that Dhruvil's teams' silo→exec→demand rollout pattern (Galaxy/SGI-class infra plays; full pattern in Dhruvil chapter 7/17 entry) is frustrating SSJ teams too — and **Kurchi is "raising a lot of concerns about UPP" citing this feedback from her teams.**
- **Read (hold): the concerns are an instrument, not new substance.** Kurchi was already wrestling for ownership under UPP (7/13 posture shift, next entry down). Her teams' legitimate friction supplies respectable ammunition. Fixing the rollout pattern strips the evidence but will NOT dissolve the ownership play — don't conflate the two.
- **Counter-moves:** (1) Dhruvil side — the operating-protocol idea (customer-team co-design before exec presentations, co-owned savings numbers) held in pocket after the SGI 1:1 went well (Dhruvil chapter 7/17). (2) Dylan side — pre-frame the causal story at the next 1:1, folded into the already-queued seam-drawing playbook item (7/13): when UPP concerns arrive from Kurchi's direction, Dylan should already know the friction source is a fixable rollout pattern. Context, not complaint — Dhruvil is her report too. **Still pending as of 7/17.**
- **Source hygiene:** Sai/Tie never named to anyone; James's own observations carry the story.
- **Same-day second data point — calibration comparative framing (reported by James 7/17):** In the recent calibration round, **JJ's IC16 case passed Rajat's round; Rajat is bringing it to Jeff's round.** Kurchi's pushback in the room: her Search retrieval teams have only one IC16 — "why should [James's org] have a third with JJ?" **Dylan had to chime in that James's team owns a lot more than retrieval.** Third Kurchi-pressure chapter in the seam playbook (ownership wrestle 7/13 + friction conversion 7/17 + calibration comparisons 7/17). **Countermeasure shipped same day:** org renamed **P13N Retrieval & Anticipation ML** in `reorg_july2026/org_design_proposal_2026-07_v2.md` (commit `5d42072`) so the name blunts retrieval-to-retrieval comparisons in rooms James isn't in; Dylan ask drafted, pending send before announcement messaging locks. Watch-for: the same density argument may recur at **Jeff's round** — JJ defense there = the Foundations & Efficiency leg (L1 Utility, $1.67M), a talking point the name deliberately doesn't carry.

## 2026-07-13: SSJ narrative shift — intent modeling as part of UPP
- **Kurchi's org framing is now "intent modeling":** they want intent + relevance modeled **as part of UPP**. Big narrative shift — in March the play was a competing base model (P2P LR); now their stated ambition presupposes UPP as the vehicle.
- **Read:** relevance-as-differentiator has evolved into intent+relevance-as-pillar-within-the-platform. This is the co-option opening: publicly hand SSJ ownership of the intent/relevance modeling pillar inside UPP (origination-over-adoption satisfied), which raises her cost of blocking the platform her own narrative rides on.
- Source: James, pre-ELT prep session. P2P v0 results context in `work/projects/upp/upp_retrieval_em.md` 7/13 entry.
- **Same session: Jinfeng departed Pinterest; new P2P TL = Zheng Jie (Sr Staff, more collaborative — see §7).** Kurchi's lieutenant structure changed: her technical-debate champion is gone, which may soften the bloc dynamic observed at the March MW.

### Post-ELT observation (same day, James debrief)
- **Visibly much more engaged under the UPP framing than at last contact — now wrestling for ownership and control for her teams UNDER UPP.** Posture arc: slow-play (4/23) → active block (6/3) → **competing for territory inside the platform (7/13)**. The co-option is working: her stake in UPP is now worth fighting for, which is the win condition — cost of blocking rises with her ownership share.
- **Still sending subtle jabs: "it's not clear if the downstream will be faster yet."** Read: contesting the platform's central velocity/economics claim while engaged — positioning herself as judge of the Search-onboarding test. Classic reasonable-sounding optionality play.
- **Counter to the jab is data, not debate:** make time-to-onboard a published, falsifiable metric (Notif ~4mo → P2P → Search target). Meets her own "can't decide without data" standard; her skepticism then gets answered by a dashboard, not an argument.
- **New game = seam-drawing, not blocking-defense.** The fight moves to who-owns-what within UPP: intent/relevance pillar, Search onboarding ownership, possibly governance/process control (watch for a steering-group proposal from her side — decide the desired governance shape in advance so James proposes rather than reacts). Repeat the Yan April-3 pattern: negotiate the seam early and explicitly — base model + cross-surface training + retrieval architecture stay James's; intent/relevance modeling objectives + SSJ surface fine-tunes are SSJ-owned within the platform. The cross-org operational model doc (`work/projects/upp/cross_org_operational_model/`) is the ready-made vehicle.
- Dylan should hear this posture read before her next Kurchi touchpoint — she carries that political channel.

## 2026-06-03: Active block escalation — CST/CFM launch + Sai bandwidth pressure
- **The 4/23 "too hard to move, just hope she doesn't block" stance has failed.** Kurchi is now **actively blocking**, not slow-playing.
- **Event 1 — CST/CFM launch block:** Cross Surface Training + CFM had massive ranking-side wins. Kurchi personally blocked the launch in the meeting, citing **a new relevance metric regression** + **"executives flagging user perception gaps for P2P for relevance."** The "executives flagging" framing is a high-altitude shield — hard to argue with without surfacing the executive source. Rajat did NOT decide unilaterally to override (see §4 6/3 entry).
- **Event 2 — Sai pressure cascade (peer EM observation):** Kurchi is pressuring Sai on "metrics in the holdout" → limits Sai's bandwidth on UPP cross-surface work. Sai is reframing collaboration as **parallel tracks**, not true co-ownership. Sai said it sounded like she was **"handed a command, not debatable"** (see §27 6/3 entry). The architecture James stabilized 5/13 (UPP = "shared infra co-own") is being unwound from above through Kurchi → Rajat-non-push → Sai.
- **The analytical hinge for post-OOO:** is "executives flagging user perception gaps for P2P relevance" **substantive or pretextual**? If substantive, P2P FT work needs to address head-on or it'll get blocked the same way CST/CFM did. If pretextual, Kurchi is using executive-flag framing as cover and the political game is upstream. James probably knows which; flag for clear-eyed post-OOO read.
- **Operating implication:**
  - The "practitioner who made SSJ's surfaces better" meta-goal is now insufficient — the meta-goal worked when Kurchi was slow-playing; now that she's actively blocking, surface-level credit-sharing won't move her.
  - Run P2P FT on James's own code (Hongtao + maybe Zhihao). Do NOT ask Jiaqing or Suki to train variants — would put them between Sai/Kurchi marching orders and a James-side ask, no-win for them.
  - Escalation channel = Dylan (Piyush is messaging her this week + asking for time next week). Not Rajat (see §4 6/3 entry).
  - Hold the "ask the team" frame: if James's team lands a good offline gain on P2P FT, can Sai's team help run it online? — cleanest collaboration test that doesn't force political exposure for Sai's side.
  - Confidentiality on Kurchi-side intel (executive-flag framing, Sai's "handed a command" framing): trust perimeter is Dylan only.

---

# 7) Jinfeng — IC18, P2P ML Lead (Kurchi's org) — **DEPARTED Pinterest (noted 2026-07-13)**

> **2026-07-13 update (James, pre-ELT prep):** Jinfeng has left Pinterest. **New P2P TL: Zheng Jie — Senior Staff engineer, notably more amenable and collaborative than Jinfeng.** Profile below retained as historical context (the Option 2 play, misrepresentation incident, P2P LR legacy dynamics). Implications: (a) credit lines in exec rooms should name **Zheng Jie + Jiaxing**, not Jinfeng; (b) Kurchi lost her technical-debate champion — watch who inherits that role (Zheng Jie's collaborative posture may mean the champion seat stays empty); (c) the P2P-LR-legacy-protection motive largely left with him — v1 co-design friction should drop.

## Role in my 6–12 month goals
- **Co-design counterpart for UPP retrieval expansion to P2P.** Named POC alongside Jaewon for the unified base retriever design.
- **Kurchi's champion in technical debates.** His positions in architecture discussions reflect Kurchi's strategic interests, not just his own technical judgment.
- **The person who determines whether co-design is genuine or performative.** If Jinfeng invests real effort in the UPP CLR design, the platform thesis advances. If he sandbaGs or steers toward P2P LR, the co-design stalls.

## Profile
- **IC18** — promoted by Kurchi. Has a reputation for **weak technical output** but **strong political skills**. The promotion signals Kurchi rewards loyalty and org defense over raw technical contribution.
- **Built P2P Learned Retrieval (P2P LR)** — this is his technical identity. Any architecture decision that sidelines P2P LR threatens his legacy and IC18 justification.
- **His delegate Jiaxing Qu** is the day-to-day P2P co-design counterpart. Jiaxing is still confused about UPP's scope — initially thought UPP = replacing P2P.

## Political Behavior (Observed)

### The Option 2 Play
Jinfeng's initial proposal: rebuild a new base model using the **P2P LR codebase**, then drive adoption across surfaces including Homefeed. This was Kurchi's strategy manifested in architecture — if the base model is built on SSJ's code, innovation flows *from* SSJ outward, and Jinfeng owns the technical direction.

### The Misrepresentation Incident
After Dylan/Rajat/Kurchi aligned on Option 1 (CLR-based), Jinfeng told the Slack channel he'd agreed with Dylan/Kurchi to start with P2P LR as the backbone — **directly contradicting Dylan's actual directive.** His proposed sequencing was designed to produce underwhelming CLR results (low investment) while directing real engineering into P2P LR. This was Option 2 relabeled as a roadmap.

- Jaewon called it out diplomatically: "Shouldn't we also try re-designing today's CLR base model?"
- James escalated to Dylan, who confirmed: "That's not what I agreed."
- Resolution: Kurchi proposed design review → Wednesday meeting → co-design with CLR as base

### Pattern
Jinfeng operates through **positioning and narrative control**, not direct obstruction. He'll comply with the letter of a decision while steering implementation toward his preferred outcome. Watch for architecture drift in the co-design — Krystal warned: "Let's see if we don't re-litigate next week."

### 2026-05-13 — OneTrans surfaces; pattern continuation in Jiaxing's lane
P2P approved a new retrieval architecture (OneTrans — unified transformer tokenization) on 5/12 driven by **Jiaxing Qu (Jinfeng's delegate, reports to Sai)**. OneTrans had been in development since early Q1 in parallel with UPP v0 co-design, not disclosed to UPP. Architecturally it sidelines UPP's feature-cross layer — structurally adjacent to Jinfeng's original "P2P LR as base model" Option 2 play, now expressed as a P2P-internal scaling backbone that arrives faster than UPP v0. Sai owned the disclosure gap at the EM layer (see §27 2026-05-13). Jinfeng's specific role/awareness in the OneTrans parallel track is unclear — but the pattern (P2P building its own scaling backbone in parallel; UPP becoming the catch-up effort) tracks his prior strategic posture. Worth holding lightly; the joint sync technical resolution (Plan 3 prioritized = UPP v0 ships in original form) recovers ground without forcing the question.

## What Jinfeng Optimizes For
- **Ownership of technical direction.** His IC18 case rests on P2P LR being the foundational retrieval model. UPP CLR threatens that narrative.
- **Kurchi's approval.** She promoted him; he fights her battles in technical forums.
- **Face-saving.** The co-design gives him a role (named POC). Any framing that makes him feel like an adopter rather than a co-author will trigger resistance.

## How James Should Interact with Jinfeng
- **Name him positively in front of leadership.** "Jinfeng's team is co-owning the relevance piece" — reinforces co-ownership and makes it harder for him to frame this as P13N imposing on SSJ.
- **Don't undermine his reputation** even if justified. He's Kurchi's promoted champion — attacking him attacks her judgment.
- **Let Jaewon be the technical counterbalance.** Jaewon has credibility with both sides and can challenge architecture drift without the political baggage James carries.
- **Watch the co-design artifact closely.** The key question: is it CLR extended with P2P elements, or P2P LR with CLR elements? The former is aligned; the latter is re-litigation in disguise.

> **Meta-goal:** Make Jinfeng feel like a co-author who chose to build on CLR, not a defeated opponent who was forced to comply.

---

# 8) Key Team Members — Retention & Development Intel (March 2026)

## Piyush (IC16 MLE, UPP Technical Lead)
- **Status:** Most performant IC. Full trust with James. Holds core retrieval architecture context.
- **Retention:** Strong. Invested in UPP. Previously applied for EM role (went to Bowen). James does NOT want Piyush as EM — value is as technical IC lead.
- **Growth path:** IC17. Dylan sacrificed an IC17 role for EM backfill, but Piyush's IC17 case needs building.
- **Risk:** Low flight risk currently. Watch for frustration if EM backfill takes too long and management burden falls on him.

### Coaching focus (2026-05-29, surfaced in David session)
- **Behavioral patterns to address:** not giving direction to people; doesn't stay in touch with team / support what they're doing.
- **Root causes (James's read):** lack of organization + desire to do things himself.
- **Coaching framework (David, 5/29):** connect outcome ↔ behavior; tiny tweaks, not overhauls; set 4-week reasonable goals; define what success looks like; identify a reasonable first step; success breeds success.
- **Anti-pattern to avoid:** directive prescription. Frame is co-coaching, not telling-him-what-to-do.
- **Cross-ref:** `work/coaching.md` 2026-05-29 entry.

## Bella (IC16, RecGPT TL)
- **Status (2026-06-30): STAYING.** Told James directly she is *not* leaving, despite recsys offers in hand (incl. Meta). She turned them down because they're **lateral recsys with ~2x hours**; Pinterest is her preferred *holding pattern* — a lower-workload job that leaves her 20–30% time to reskill into AI (taking Stanford CS337). Reversal from the April/May flight-risk posture, but a *conditional* one.
- **Named leave-trigger:** an interview/offer from a **top-tier AI lab (OpenAI/Anthropic specifically)** — nothing else moves her. Committed to telling James if it comes. She also said the current stack "cannot satisfy what I'm seeking" — so there's a clock on this regardless.
- **Her asks for staying:** **promotion** + freedom to work on **agentic systems + generative retrieval** + time to learn.
- **James's operating stance (unchanged): keep, don't promote near-term, don't manage out.** She's doing good work / still valuable / directs + executes when asked — but she is a **capped directed contributor, not an independent leader** (confirmed: she **declined to TL Retentive Recs** when asked directly). Retention currency = **interesting work (agentic/generative) + autonomy + time, NOT title.** **(2026-06-30: James deliberately kept the promo possibility OPEN — did not give an honest-bar answer, does not owe it now; instead pivoted to a good conversation about Bella reporting to Alim, which she received well.)** Keep the honest promo-bar answer in reserve; deliver it before it hardens into a year-end-calibration expectation he can't meet.
- **Key issues (still valid):** doesn't create ideas, resists James's architecture suggestions, lacks decisiveness and communication skills. Dylan has lost trust over Group MP refusal — **but Dylan does NOT know about the ER consult or the staying reversal** (see team_members_scope.md 6/30 correction).
- **Comp commitment:** James said he'd try for a bump by end of April (never actioned). With the promo now on the table as her ask, the honest-bar conversation supersedes this.
- **ER thread:** the 6/14 ER consult (perf decline, filed to protect a now-moot backfill req) should close as **resolved / retaining**. Only the ER PoC knows; Bella does not.
- **Open (this session):** does Bella route to **Alim's Track A** (RecGPT is Track A's identity) or **stay on James's Track B** (where the agentic/Reflex work she wants lives)? Parallels the Yuke "don't hand a complicated senior to a new EM" call.
- **2026-06-30 — Bella's Option-2 objection + resolution.** Bella is **against Option 2** (RR + Generative Retrieval under Alim). Objection = **manager continuity** (doesn't want to switch to a new manager), NOT scope — she keeps **30% Reflex under Alim**, so the agentic-proximity worry is moot. Direction chosen: **Option 2 as primary** (she's the Staff anchor); handle her objection via **Dylan sign-off first, then a warm high-touch handoff** (James stays visible in her growth; 30% Reflex keeps a live thread to him). Watch-for: ensure "don't want to switch managers" isn't a quiet read on Alim — probe gently before handoff. See `alim_reorg_proposal_2026-06-30.md`.

## Yuke (IC15, Retentive Recs TL — updated 2026-04-11)
- **Status:** Flight risk. Bowen reported Yuke asking interview questions about market pay. Unhappy about promo deferral.
- **Retention anchor:** Green card process is primary.
- **Promo:** Not ready by mid-year. Needs p(UIC) successfully built and landed. End of year is right window. Frame as strategy, not deferral.
- **Key dynamic:** Doesn't get along with Devin. James designing Chuxi bridge arrangement to hedge against Yuke's departure.
- **NEW (2026-04-11): KDD 2026 paper Prediction co-author.** Yuke is busy landing impact, but James will delegate Architecture/Prediction subsections of the KDD paper to him to support his career. Frame: this is a published-paper credit on his record before the end-of-year promo conversation. Career-aligned investment.

## Devin (CLR TL)
- **Status:** Wants strong collaborators. Ryan (April) and Yichi (July) incoming.
- **Risk:** Watch in 2-3 week gap before Ryan arrives post-Bowen announcement.
- **Key dynamic:** Wants to work with Chuxi but must be kept respectful of Yuke's technical leadership.

## JJ (Real-Time / Pinvestigator)
- **Status:** Promo to IC16 targeted end of June.
- **Risk:** Failure + Bowen departure + AI market = potent combination for JJ to look. Start packet April. Address ML depth gap.
- **Essentially solo on Real-Time.** No coverage if he leaves post-promo.

## Chuxi (Retentive Recs + Pinkerton, updated 2026-04-11)
- **Status:** Primary IC for Retentive Recs. Promo vehicle is p(UIC) under Yuke.
- **Strategic role:** Bridge between Yuke (retentive recs) and Devin (CLR). Insurance against Yuke departure.
- **NEW: 20% Pinkerton commit going forward (2026-04-11).** Excited specifically about the agentic recsys vision at the end of the Pinkerton roadmap. Critical Alok-PTO bridge — covers 2 weeks. James now has a code reviewer + collaborator on Pinkerton beyond Alok.
- **Development:** Make sure she's in architectural decision rooms, not just execution.

## Daniel ⟨surname NOT Liu — corrected 2026-07-07⟩ (contractor on James's team — added 2026-04-11)

*(Name correction 2026-07-07: this contractor was mis-recorded as "Daniel Liu." He is a different Daniel; surname unknown/pending. Do NOT conflate with Daniel Liu the EM — ex-Yan sub-EM, now reorging under James, see `reorg_july2026/daniel_liu_team_2026-07.md`.)*
- **Role:** Strong contractor on James's team. Now Pinkerton logging owner.
- **Current state:** Shipped Pinkerton logging this week. Field-name-too-long hiccup → fix shipping Monday 2026-04-13. Will execute Alok's verification plan during Alok's PTO.
- **Why he matters:** Reliable execution layer on Pinkerton infrastructure. Frees James to focus on Reflex co-dev + adoption layer.

## Alok
- **Risk:** If PhP deprioritized after CTO presentation. Keep 20% bandwidth, have alternative scope ready.
- **Pinkerton connection:** Original hackathon team member. Motivated to work on Pinkerton. Completing HF full funnel logging by April 4, 2026. After logging done, shifts to DT (~50%), then picks up Pinkerton extension work as DT scoping stabilizes.

---

# 9) Andrew Yaroshevsky — Sr. Director of Product

**Updated 2026-08-27: SCOPE EXPANSION — ATG PM team now reports to Andrew (org-change announcement, screenshot from James).** Verbatim: *"ATG: ATG PM team will report to Andrew Y. Andrew's leadership of Personalization and UX Frameworks, including work such as UPP and Anticipation Cupcake, makes this a natural fit. This change will strengthen collaboration across Core Product, ATG, and Ads, while supporting a longer-term vision for ATG with Chuck."* Same announcement: *AI Compliance and Wellbeing (Adi Narayan) reports directly to the announcer* ⟨announcer = the Core Product product head; name not in the excerpt⟩. **Reads:** (1) **UPP and Anticipation Cupcake are the named credentials** for the expansion — James's team's work is the stated justification for his sponsor's bigger remit; the cleanest sponsor-utility evidence on file. (2) Andrew is now the **single product owner across the P13N ↔ ATG seam** James has been working by hand (Zelun's pUIC time, GenRet/RecGPT, Simulate's ATG staffing, "ATG relations w/ Dhruvil") — the product case for UPP-as-one-platform now has one owner instead of two. (3) "Core Product, ATG, and Ads" is the exact triangle of James's H2 Reflex success definition (≥1 team outside P13N — Ads — building and launching) and the Jiajing→Dinesh Ads×UPP thread. (4) **Bandwidth risk:** a bigger Andrew is a thinner Andrew — the 5/27 FTE-PM-on-Reflex commitment and his EM-alignment attention are the things to watch diluting. (5) **"Longer-term vision for ATG with Chuck"** (Chuck Rosenberg, VP Eng, CTO-direct, outside Jeff's chain) hints ATG engineering may consolidate under a different VP than James's — the models James depends on (pUIC, GenRet) would then sit in another eng chain with Andrew as the product bridge; watch, don't act. Related: §41 Jiajing (ATG eng side), §31 Zhenyu (ATG Sr. EM). **8/27 evening: James sent the congratulations note same day** (content not captured).

**Updated 2026-07-09: Mid-year peer feedback received — top-tier endorsement + one growth area (XFN patience), third delivery of the Feb/April tone signal.** Andrew's H1 cycle peer feedback about James arrived 7/9 (verbatim text + craft study: `self/writing_style/aspirational_writing_style.md`). **Positive:** "one of the strongest ML leaders at Pinterest"; "supportive of his continued growth here and beyond"; Anticipation Cupcake = thought leadership, velocity, ownership, product sense, judgment; crucial-conversations courage explicitly framed as a senior-leader quality; Reflex ladder "rough idea → real, innovative success → reached Bill Ready → showed a new way we can build and improve Pinterest" (CEO name deliberately in the written record); pivot: technical depth "obvious," what impressed him more this half = **product sense and judgment**; archetype: "the kind of 'builder' we will need more of in the AI future." Third senior stakeholder independently authoring the same director-shaped frame (Dylan: AI-native differentiator; Rajat: AI-first cross-functional executor). **Constructive:** more patience/appreciation for XFN partners with different profiles ("may not grok ML systems or the recsys stack... but bring strength in other disciplines"); unlock framing ("the next level of leverage"), pattern-level, no incidents named — and the paragraph itself models the appreciation it asks for. **Read (James confirmed fair, "felt seen"):** anchor case = Lily Li office-hours incident — she reports up Andrew's PM chain (§21) — with Akshanta corroboration (§20); same pair as Dylan's April 3 yellow flag. Ongoing texture = the PM apprentice on the Feedback tool, an area Andrew is *personally keen on*. **Arc:** Feb eggshells (red alert, Dylan: "limiting ceiling" to Director) → April 3 PM-tone (yellow flag, favor) → July mid-year (pattern-level, wrapped in praise). Severity falling = repair working; but the signal is now institutionalized in a written cycle artifact across two chains — Andrew's "next level of leverage" is Dylan's "limiting ceiling" in sponsor dialect. **H2 response = behavioral, on stages Andrew sees:** (1) apprentice → independence via standing container + possible XFN self-serve framework (aligns with Reflex's confirmed "XFN acceleration" goal axis, §36); (2) Lily → structural repair, no gestures (§21 plan); (3) Tim collaboration already healthy = the positive exhibit (§36). Short, light thank-you to Andrew planned — no promises, register-matched. Related: **Michael (PM Director, §38) starts Mon 7/13** — ML-fluent PM leadership over the non-recsys PM population; the org is fixing the eng↔PM interface from both sides.

**Updated 2026-05-27 (afternoon): Hallway convo — user.md landed, Andrew assigning FTE PM to Reflex, three pre-OOO asks of James.** James ran into Andrew in the hallway and surfaced the user.md work directly. Andrew is **happy with user.md** (capability landed; no DM needed). Andrew is **assigning a full-time PM to Reflex** — major escalation, PM-level investment from his side. When James asked what he could do to set Reflex up for success during his OOO (6/4–end-of-trip), Andrew gave three clean asks: **(1) Connect with the PM. (2) Make sure Reflex is funded for James's team. (3) Andrew takes it from there.** Clean delegation. Pre-OOO punch list is now narrow and concrete. The Pinkerton-as-callable-agent architectural conversation does NOT need to happen pre-OOO — it can ripen organically through the PM as a future forwarding agent. The Andrew Build-expansion thread + agent-to-agent infra coordination (per 5/26 meetings) sits under the new PM's purview going forward.

**Funding ask (#2) is time-sensitive AND lands directly into the Dylan team-design artifact thread.** Dylan's 5/26 1:1 was about James's team scope — "Reflex as a funded line item in my team" is now an explicit Andrew ask that wasn't surfaced at the 5/26 1:1. Worth circling back to Dylan before OOO with this new intel as part of the headcount/funding conversation.

**Updated 2026-05-27 (morning): Build-agent expansion push + JJ landed + Pinkerton not yet in Andrew's model.** Andrew is pushing hard on Build-agent scope expansion across recent Reflex meetings — *"remove the validators, let's go big, run it wildly."* He is also corralling infra folks for agent-to-agent comms. Dylan had a side conversation with Andrew about James's personal bandwidth; James responded by bringing JJ into Reflex, and Andrew now recognizes JJ as doing real work on it. **Andrew did NOT have a working mental model of Pinkerton** as of this morning — was present at the 4/16 Rajat-meeting demo but it was Rajat-focused and brief, and the "Pinkerton" name itself only landed 2026-05-16. Hallway convo (afternoon) introduced user.md capability successfully without invoking the Pinkerton brand. Going forward: lead with capability, introduce Pinkerton name as the substrate-pattern *over* the capability, not as a known thing. James's preferred framing: Pinkerton as a separate callable agent that Reflex consumes (Pattern A, MCP-primary — per `reflex_pinkerton_strategy_051626.md`), NOT subsumed into Reflex. Two reasons: Dimitra co-lead standing, and substrate-with-multiple-consumers pattern (PYC reranker + CV/ATG collab + Reflex Detect). See `project_pinkerton_reflex_substrate.md` memory for current state. **Working hypothesis for Andrew framing:** Build-expansion *requires* rich grounding (or wild Build agents generate garbage) → Pinkerton-as-callable-agent is what makes the unconstrained Build vision tractable. Federation enables Andrew's vision; subsumption would compete with it. Frame as architectural decision driven by Build's needs, not as org-design protection of Pinkerton.

**Updated 2026-04-17: Frame-capture residue not escalating.** Andrew replied positively in the 3-person DM (James + Dylan + Andrew) on James's PR and forward motion — no surface reference to the 4/16 Rajat-meeting moment where James took Andrew's Reflex-setup turn to demo Pinkerton. Read this as "not escalating," not "resolved." Declined-DM call from 2026-04-16 (contribution-as-signal over verbal repair) is validated so far. Caveat: unacknowledged frame-capture in high-trust circles compounds quietly; keep watching for downstream signals. Separate open thread: Andrew's Reflex-frame with **Rajat** is still displaced — Rajat's mental anchor from the meeting is Pinkerton-as-primary, and Andrew's "I'll talk about big picture later" hasn't been cashed yet.

**Updated 2026-04-11: Major escalation this week.** Reflex co-development formalized; Anticipation Vision context now CTO-amplified; Andrew committed to landing Reflex code in git before Tuesday 2026-04-14 for explicit co-development with James.

## Role in my 6–12 month goals
- **Anticipation Vision co-author.** Andrew + Dylan + Mira (Sr Director, Design) co-authored the Anticipation Vision — Pinterest's vision for ALL of 2026 personalization. One-sentence frame: "Pinterest should not just show you things you want, but anticipate what you might want next and show that to you instead." James + Anna's Retentive Recommendations is the named technical key under this vision.
- **CTO pitch landed.** Andrew pitched the Anticipation Vision to **Matt Madrigal (CTO)**. Matt has subsequently talked about it **openly at a conference**, naming it as one of the things he is most excited about for personalization and ML/AI at Pinterest. CTO-level external surface area on the public record.
- **Reflex co-developer.** Andrew built a working Reflex prototype (autonomous diagnostic agent generating Trello cards for investigation hypotheses). Two cards already in production (CG signal decay + non-English search relevance with VLM annotation). Dylan validated to Andrew externally: "it's great to see it's catching issues, and real ones, very promising." **Andrew committed Tuesday code drop + explicit co-development with James.**
- **Strategic amplifier for AI investments.** With Andrew championing the product vision and James building the sensing layer + Reflex co-dev, the AI work is no longer a side project — it's a platform play with Sr. Director product sponsorship + CTO-level visibility.
- **Anna's manager.** James already has Inner Circle trust with Anna. The 4-way nexus (Andrew + Dylan + Anna + James) is structurally over-determined for trust — no weak link.

## Current relationship
- **Status:** **High and accelerating.** Co-development formalized in 3-way Slack DM with Dylan this week. Andrew is actively pulling James in deeper (Tuesday code drop + RLHF expert-feedback role).
- **Trust level:** **High** (co-development + Dylan brokering + Anna bridging + Andrew pitched James's engineering work into the CTO pitch).
- **What Andrew wants:** James's expert codepath knowledge (HF CG codepaths, engagement rate tables) to feed Reflex's hypothesis generation. Andrew is biased toward weighting engagement data over relevance signals going forward. Wants RLHF expert feedback in the loop.

## What Andrew optimizes for
- **Vision + momentum.** He wrote a two-pager, not a PRD. He wants believers and builders, not process owners.
- **Product narrative.** Reflex is framed as "the industrial revolution for recommendations" — Andrew thinks in big product narratives.
- **Cross-team leverage.** Reflex touches all surfaces (HF, Search, P2P, Growth). Andrew wants this to be an org-wide shift, not a team project.
- **Engagement data over relevance signals.** Currently nudging Reflex toward engagement data weighting and away from pure relevance scoring.

## Operating plan
- **Be ready for Tuesday 2026-04-14 code drop.** Andrew lands Reflex code in git; James plugs in for co-development.
- **Default is let-the-work-speak.** Do NOT bring transactional credit/role conversations into this relationship. The trust topology with Dylan + Andrew + Anna does not need credit framing — the architecture is the credit. (See `feedback_credit_in_trust_relationships.md` memory.)
- **High-leverage seat to occupy:** expert-in-the-loop providing codepath knowledge + RLHF feedback. Compounding position. Requires *consistent* presence, not one-shot inputs.
- **Let Andrew own the CTO pitch.** Already done. James owns the engineering proof points (PINvestigator, Pinkerton) + Reflex co-dev.
- **Don't over-coordinate.** Andrew is a vision seller. James is a builder. Keep the interface lightweight.
- **Comms calibration — substance high, logistics deferential** (Sr. Director, not a peer; cross-level + trust-over-determined). Don't pin his calendar ("pick Wed or Thu, I'll book it" is too peer-flat) — offer flexibility ("happy to flex around your calendar, send a time"). Always come with substance (named codepath area, specific scenarios, prepped artifacts) — the expert-in-loop role is the whole reason he invited James. Thank-yous are fine when he goes out of his way, but thank-you *without* technical substance = zero signal to Dylan that James is driving. Nudges carry content ("ready to pull as soon as you push — got X queued"), not passive emojis (brick/thumbs-up read as "waiting"). (Migrated from auto-memory 2026-06-26.)
- **Watch:** Mira (Sr Director, Design) is the third Anticipation Vision co-author. ~~James's direct line to her is unclear.~~ **Updated 2026-04-28: direct line activated, Mira-initiated** (UIC mental-model DM on the Explore module powered by RR). Mediation through Dylan/Andrew is no longer the only channel — she has now demonstrated willingness to route directly to James on technical depth questions. See #33 for full intel.

## 2026-07-20: SM/SL staffing sync — the repair on stage, and it landed

15-min sync (Andrew organizer, Dylan, Lily Li, Michael Weissinger §38, James; exec-visibility context: Bill Ready at MBR + Madrigal at ET AMA). Andrew pitched **full-stack virtual-team co-ownership as a precedent** ("no primary and secondary"; a backend owner who "feels the ownership... gets up in the morning and tries to come up with new ways," not a backlog line item). James's move: co-ownership from the CG side, align on the technical roadmap, **disagree-and-commit**, naming past historical-experiment indecisiveness. Andrew: **"100% that is exactly what we want."** Close: Lily + Andrew jointly — **"thank you so much for your ownership James!"** — in front of Dylan and Michael. This is the §9 mid-year XFN-patience feedback repairing on the exact surface it was authored from: Andrew's own ask, his own operating model, his PM chain. Commitment out: retrieval-side POC named by EOW 7/24 (Yali or Hedi — LWS lane; SM/SL strategic home = modeling over heuristics). Full debrief: `work/people/reorg_july2026/reorg_followups.md`.

---

## 2026-08-25: "pUIC is really the main bet of this whole thing" — the sponsor says it to James directly

Anticipation group DM (Andrew, **Anna Kiyantseva**, **Krystal Benitez**, James), 11:42 AM (verbatim): *"Lots of great work is coming together in Anticipation – very exciting! I hope you understand how much dependency there is on getting pUIC right – it's really the main bet of this whole thing. You guys are our very best people to work on this, so I'm sure you gonna come through. Let me know if I can help anyhow to accelerate anything."* **Krystal answered for the team (11:48):** "oh we are very, very aware. A lot of iterations are in the works… rest assured, we have eggs in several baskets in hopes that we get to a breakthrough soon. And we are actively discussing our confidence in each method (the standardized hop definition will help) so we can decide if we need to double-down and/or defund any work to get to a pUIC method that effectively surfaces novel content." (Preceding context, Krystal 8/24 2:17 PM: Explore-page dogfooding of module variants needs extra work — Allen Pan looped; OTA is the fastest path; update at the execution sync.)

**Read:** This is Michael's 8/2x line ("UICs the top Anticipation priority — multiple projects dependent," source 08) in the sponsor's own words, addressed to James — praise-wrapped pressure, and the expectation now has James's name on it. Two uses: (1) **leverage** — the pUIC line (Yuke/Chuxi/Yidi/Zelun + the model-based pUIC × UPP base-model sync) is the thing Andrew has just said must not give, so CQ/GenAI asks on James's team come out of something else, in writing; (2) **exposure** — "our very best people" is the frame that becomes "they didn't come through" if pUIC misses; Krystal's "double-down and/or defund" is the mechanism to decide early rather than late — James should be the one framing that decision (confidence per method, hop definition, date), not receiving it. James did not need to reply; Krystal covered it. Anna Kiyantseva's role still unidentified (also the person Michael wants the CQ doc shared with — source 08 addendum).

# 10) Darren Regers — Sr. EM → Director, Infrastructure (promo official 2026-04-16)

## Role in my 6–12 month goals
- **Primary AI partnership.** Darren's team has an eval DS who can build eval frameworks for both PINvestigator and Pinkerton. This is the most critical capability gap in James's AI work.
- **Senior alliance (confirmed 2026-04-09).** Darren got the Director offer — official 2026-04-16. No longer "potential" — this is now a Director peer alliance with high personal trust. Darren publicly supportive of James's own Director trajectory: *"The next goal is Director James"* (Slack DM 2026-04-09).
- **Active Pinkerton sponsor (new 2026-04-09).** Darren read James's Pinkerton proposal overnight, loved it ("Love the proposal and the steps"), and is **actively searching his team for contributors** — candidates: someone named Dylan on Darren's team (NOT James's manager Dylan Wang), or the Analytics Agent folks. Proactive resource commitment before the Director role is even official.
- **Personal ally.** James and Darren are close. High-trust, low-friction collaboration.
- **Trust-ledger asset (2026-07-11).** Named #1 in James's long-game leadership trust ledger (`goals.md` Interview optionality): infra Directors are the most-recruited leadership profile at frontier labs, and Darren is the likeliest person on the board to hold hiring power somewhere that matters in 3–5 years. The deposit mechanism: make Pinkerton/eval structurally successful *for his people* — their wins landing in his org.

## Current relationship
- **Status:** Active and accelerating. Proposal read + loved 2026-04-09. Darren personally staffing Pinkerton contributors from his team. Director offer official 2026-04-16.
- **Trust level:** Very High (personal friendship + professional respect + public Director-track sponsorship)
- **What Darren wants:** Clear milestones from James so he can justify the resource investment. Continue the partnership as he moves into the Director role.

## Operating plan
- **Send Darren a formal congrats when the promo is official (2026-04-16).** High-trust sponsor moment — do not let it pass unmarked. Short and warm, not sycophantic. Calendar reminder worth setting.
- **Give him the Q2 milestones immediately.** He's ready to commit resources and is actively searching for team members to join — don't make him wait.
- **Name the contributors as soon as they're confirmed.** Whether it's "Dylan" (Darren's report) or the Analytics Agent folks — update `projects/pinkerton/pinkerton.md` staffing table the day they're committed.
- **Get the eval DS committed.** Still the single highest-leverage resource ask for the AI portfolio.
- **Keep the interface simple.** Darren manages both DS and Eng. His reports will roll up to him. No coordination overhead needed.
- **Darren is now a Director-track reference point.** When James is thinking about his own Director narrative, Darren is a trusted sounding board — same journey, just completed. Use him for 1:1 thinking-partner moments on the trajectory, not only on Pinkerton resourcing.

---

# 11) Brian Lee — EM, Activation/Growth

## Role in my 6–12 month goals
- **Visibility venue.** Brian hosts a weekly AI forum where Roberto and James are invited to showcase progress. This is a low-effort, high-visibility demo opportunity.
- **Long-standing collaborator.** James and Brian have been collaborating on debuggability and observability since early 2025. War stories together. High trust.
- **Front-end tooling expertise.** Brian's team builds front-end tools. Useful for visualization but not core to Pinkerton's LLM analysis work.

## Current relationship
- **Status:** Active collaboration. Brian started the weekly forum specifically to bring people together around AI tooling.
- **Trust level:** High (shared history, mutual respect)

## Operating plan
- **Use the forum.** Demo PINvestigator and Pinkerton M1 here. Great visibility with low coordination cost.
- **Don't force engineering collaboration.** James doesn't need front-end engineers. The domain expertise lives in James's head. Forcing a collab would create make-work.
- **Keep the relationship warm.** Brian is a good ally. Show up, share progress, don't over-promise joint deliverables.

---

# 12) Roberto Konow — Sr. EM, Search (reports to Kurchi)

> **Update 2026-08-14 — 1:1 reset lands; trust shifts guarded → transactional-open.** Roberto initiated a "re-try our 1:1" (self-flagged the prior weird vibe with a 🤣), and the meeting broke the guarded pattern on three fronts: (1) **asked James for a favor** — find a mentor for Zach Barnes (deep modeling, reads a lot of papers, wants Ranking collaborations; James will ask around — Dafang He is the obvious first candidate); (2) **offered to spend his own capital** — will talk to Jeff to unblock GPU serving for Search, the blocker on the sequence-modeling → UPP collaboration (Yichin's team wants to run experiments); (3) **shared candid intel on Alim** from their Twitter years (filed in `alim_virani_archive.md`; held as dated hypothesis). He also **pressed repeatedly** for Reflex Build to become part of Shifu — James: *"fine with it, as long as the ICs on the ground are aligned"* (strategic handling: `work/projects/reflex/program_state.md` §2026-08-14 — the concession needs papering on James's terms this week). Also raised: SearchCLIP → SSJCLIP (pin + query representation; PinCLIP possibly encoding taste/styles) → bring into the UPP collaboration. James's read: quite positive, cautiously optimistic. Context: the prior 1:1 had ended oddly (James: "how can I help?" → Roberto: "I'm wondering why you're asking that question") — the lesson held in prep and confirmed today: Roberto trusts **legible, specific trades** over open-ended offers. The 4/9 "do not re-outreach / let him come to you" plan is now fully superseded — he came.

> **Major update 2026-04-23:** Roberto's position has materially strengthened via SSJ reorg (effective 2026-05-01). He now owns Text Search end-to-end: query understanding → retrieval → light-weight ranking → blending. Absorbs Query Understanding team (An Jiang, Ishita, Aakanksha). Kurchi's framing: *"I am excited to see how Roberto's influence evolves Text search going forward."* (Note the word "influence" — Director-track language.) Roberto got the scope that was previously Krishna's while Krishna was moved to platform work. This is part of the empirical "Kurchi move" pattern (see Krishna profile below).

> **Update 2026-04-09:** Operating plan has been substantially revised after new data points. The original "ship M1 first, then talk" plan is superseded. See Current relationship + Structural context below.

## Role in my 6–12 month goals
- **Structural counterweight in Kurchi-line AI tooling.** Roberto built a funnel debugging tool on Search logs using Claude Code; Jeff highlighted it to the entire org. As of 2026-04-09, he has expanded into agentic eval tooling ("I got agents working on search eval tool"), directly into James's PINvestigator/Pinkerton territory.
- **Not a peer collaborator — organizational gravity.** Roberto reports to **Kurchi** (Sr. Director, SSJ — primary political counterweight to UPP; structurally adversarial per top-of-file). The Roberto-James competitive dynamic is partly a proxy for Dylan-vs-Kurchi positioning at the director level. **This is structural, not relational — not James's to fix at the peer layer.**
- **Peer dynamic.** Roberto ships visible demos faster; James has deeper AI craft (PINvestigator architecture, Pinkerton vision, Reflex co-ownership with Andrew/Dylan).

## Current relationship
- **Status:** Cordial surface, competitively guarded underneath. Operating with territorial awareness.
- **Trust level:** Neutral, trending guarded. Evidence accumulated over 9 days:
  - **2026-03-31:** James sent a warm peer DM congratulating Roberto on his Search Debugger tool, sharing that James + Alok have been building in similar space, telegraphing his direction ("go big with AI Agents"), and sharing Andrew Yaroshevsky's Reflex vision. **Roberto never responded (9-day silence through 2026-04-09).** The outreach was well-framed; the silence is Roberto's choice, not a failure of the message.
  - **2026-04-09 AM (Akaasha ralph-loop demo meeting):** James asked a technically legitimate maturity question about a demo from someone on Roberto's team. Jeff publicly smoothed it with *"despite James's question, it's still very impressive..."* Minor micro-friction, no relational debt — the "despite" was a graceful room-management move by Jeff, not a rebuke. See `communication.md` Pattern 7 for the delivery calibration.
  - **2026-04-09 PM (Brian Lee's recsys observability meeting):** With 5 minutes on the clock, James began pitching the Pinkerton vision. Roberto interrupted with *"I'm sorry to steal your thunder but I got agents working on search eval tool"* — a pre-apologized territorial claim planted mid-pitch. James responded correctly in the moment: *"That's great! It means we have more to build upon each other's tooling. One component you might not have is the user understanding side."* Roberto nodded reluctantly, then left mid-sentence (ambiguous — hard stop or competitive closure).
  - **2026-04-09 evening (Slack follow-up):** James posted to #recsys-observability with the Pinkerton CC skill link, vision/roadmap, partnership invite, and team name-drop (Alok Malik, Chuxi Wang). Durable written reframe of the in-meeting incident. See `communication.md` Pattern 8.

## Structural context
Roberto reports into **Kurchi**. The Roberto-James competitive dynamic is partly downstream of Kurchi's posture relative to Dylan's org. This means **direct peer outreach is unlikely to resolve the friction** because Roberto's incentives are partly driven by his reporting chain. Do not try to fix this at the peer layer.

## Revised operating plan (2026-04-09 — supersedes "ship M1 first, then talk")
- **Do NOT directly re-outreach to Roberto.** The 9-day silence is information — accept it. No "hey, wanted to check in" DM. Let Roberto come to James, not the other way around.
- **Work through higher altitude gravity.** The fix is organizational, not relational:
  - **Dylan** — brokering Reflex collaboration (confirmed 2026-04-09 DM). Dylan does not currently model Roberto as part of the Reflex conversation. See `projects/pinkerton/pinkerton.md` for Reflex context.
  - **Andrew Yaroshevsky** — Reflex sponsor (Sr. Director, Product). Sponsorship air cover.
  - **Brian Lee** — forum host, high-trust ally. Low-risk ally check-in this week: *"Hey Brian, curious what you made of the Roberto interruption today. Want to make sure I'm reading the dynamic correctly."* Not a complaint — a calibration. Brian will give a straight read on whether this is broad-pattern or James-specific.
- **Reflex is the bypass lane.** Dylan's 2026-04-09 invitation to co-own Reflex with Andrew's sponsorship is a completely separate lane from the Kurchi-line AI tooling tournament. Roberto is not in that room. James should show up cleanly there — that's where the Director-track narrative gets built.
- **Pinkerton M1 reframed.** No longer primarily "the parity move to Roberto." Now: "the technical proof that makes James the credible lead for Reflex and cross-org agentic debugging." Same artifact, different framing, cleaner narrative.
- **If collaboration ever happens, it will come through organizational gravity.** Dylan or Andrew brokering, not peer chemistry. Do not chase it.
- **Don't match Roberto's territorial moves verbally in the moment.** James's in-meeting peer-reframe response (2026-04-09 PM) was the correct in-moment shape. Follow up in writing within hours (Pattern 8). Do not escalate verbally in the room.

## Watch-outs
- **If Roberto's team demos in a room with Jeff repeatedly over the next 2-4 weeks,** the status-sensor pattern will re-activate. Monday-morning wins calibration (`communication.md` Pattern 9) is the pre-communication hygiene for this.
- **If Kurchi starts citing Roberto's work in director-level forums as evidence against Dylan's side,** the Roberto dynamic becomes a higher-stakes org problem that Dylan needs to know about. Not yet — but track for escalation signals.

---

# 12b) Krishna Kamath — Sr. EM, SSJ (new: Intent Navigation and Platform org, post-reorg 2026-05-01)

> **Added 2026-04-23.** Key empirical case study for how failed Director calibration + cautious sponsor + reorg lever can compound. James's strategic mirror.

## Role in my 6–12 month goals
- **Cautionary case study, not a stakeholder to manage.** Krishna was one data point; his story is now load-bearing for how James approaches his own Director trajectory.
- **Trust channel into Kurchi's org (historical).** Krishna has been described in `dylan_archive.md:698` as "Kurchi's most trusted lieutenant" and someone with whom James has strong direct rapport. That channel still exists but is compromised: Krishna is flight risk.

## The sequence that just happened (2026-04-23 intel)
1. **EOY 2025 calibration:** Krishna was put up for Director with strong sponsorship — Kurchi as direct manager, two Senior Directors outside his org supporting, Jeff rapport from quarterly office hours over years. All the "right" signals.
2. **Did NOT get promoted.** Feedback: *"lacked visibility outside org."*
3. **James's independent read:** Krishna has no named artifact. Text search labeling maybe, but others own it more. Diffuse good work; no flagship thing associated with his name. Consistent with the calibration feedback.
4. **Krishna asked Kurchi:** how do I improve in the next few months, try again in July?
5. **Kurchi pushed timeline out:** "Noooo, maybe in a year."
6. **Reorg (2026-05-01):** Kurchi moved Text Search Relevance (Krishna's flagship scope) to Roberto. Krishna now runs SSJ Intent Nav + new SSJ Platform team (query recs + platform optimizations, ML efficiencies, observability). Kurchi's framing: "forming the connective tissue for our experience and relevance teams." The SSJ Platform charter is the graveyard — operational reliability work without the flagship-narratable impact calibration rooms reward.
7. **Krishna's response:** taking weeks off in India. Then starting to look externally. Told James explicitly: senior managers should not be too expectant of the next role, take opportunities outside when they present themselves. Cautioned James about his own situation.

## The "Kurchi move" pattern (documented for James's reference)
**Failed promo → sponsor pushes timeline → scope rebalanced away → flight.** Sponsor confidence (stated) ≠ sponsor advocacy (fought for in calibration) ≠ sponsor resilience (sustained after setback). Krishna had the first. The second was insufficient. The third didn't materialize — Kurchi used the reorg lever to protect the org's Director bench (Roberto) at Krishna's expense.

## What made Roberto successful where Krishna failed (dimensions)
1. **Named artifacts.** Roberto shipped Search Debugger + Search Replay. Jeff celebrated by name. Krishna had diffuse good work.
2. **Vertical E2E ownership.** Roberto now owns full-stack text search. Krishna owned one stage (Relevance).
3. **Jeff rapport + shipped tools.** Roberto had both. Krishna had rapport only.
4. **Territorial discipline.** Roberto defended his lane (9-day silence on James's collaboration DM; mid-pitch territorial interruption). Krishna didn't fight for brand.
5. **Adjacent-capability consolidation.** Roberto expanded into agentic eval tooling by building, not lobbying.
6. **Reliability to sponsor.** Roberto delivers Kurchi's narrative upward predictably. Krishna was harder to build around.
7. **Cross-org visibility.** Jeff's email named Roberto org-wide. Krishna was mostly known inside SSJ.

## Implications for James
- **Dylan is not Kurchi.** Relationship is warmer, peer-like, different philosophical stance on retention (see `dylan_archive.md` 4/23 update). The Kurchi move is not a universal pattern — it's Kurchi's specific playbook. BUT the lever exists in Pinterest's org architecture; any Sr. Director can execute a scope rebalance after a failed calibration.
- **Named-thing consolidation is critical path.** Krishna's failure mode was diffuseness. James has RR + Reflex/Pinkerton as named-thing candidates — better than Krishna — but organic propagation is Krishna's exact failure mode. Active narrative consolidation at VP level is how you avoid this.
- **Krishna's advice re: external opportunities has empirical weight now.** He's not rationalizing — he's telling James a story currently unfolding on him. Holds even after accounting for survivorship bias.
- **Dylan's 4/23 retention philosophy** (`dylan_archive.md`) says she won't fight leavers. That's different from Kurchi's reorg move — but it also means Dylan won't up-invest dramatically to retain if she reads James as flight risk. Transparency with Dylan about external exploration has costs and benefits that require careful weighing.

## Operating notes
- **Do not mention Krishna's situation to anyone — even Dylan** unless James deliberately raises Krishna's case as part of his own career conversation (Option B in `H1_career_convo.md`).
- **Stay in touch with Krishna post-departure** if he leaves. He's a trust channel into the Pinterest-external recsys leader network.

---

# 13) Kartik Paramasivam — Chief Architect

## Role in my 6–12 month goals
- **CTO-level sponsor.** Reports directly to Matt Madrigal (CTO). Publicly supportive of James's work — has made it known that he thinks CG's work is very important.
- **Promo coalition member.** Dylan has hinted that Kartik's support is important for James's future. This suggests Kartik's voice matters in Director-level calibration or scope allocation decisions at the CTO table.
- **Reflex stakeholder.** Andrew is pitching Reflex to Kartik. If Kartik buys the Reflex vision, James's co-ownership of the sensing layer gets CTO-level visibility.
- **ELT engagement.** Asked detailed technical questions during the March 30 ELT Dynamic Triggering presentation. Engaged and sharp.

## Current relationship
- **Status:** Positive, mostly indirect. Kartik has connected with Dylan about James specifically. Direct interaction limited to calibration rooms and ELT presentations.
- **Trust level:** High (based on observed work quality + institutional endorsement)

## Operating plan
- **Let the work create the relationship.** PINvestigator, Pinkerton, UPP results — these are the artifacts Kartik will see. Don't force a 1:1 relationship; let it emerge through the Reflex connection and demo opportunities.
- **When Reflex lands with Kartik:** Be ready with a clear "here's the sensing layer and what it does" summary. Kartik is a Chief Architect — he'll want the system design, not the narrative.
- **Don't bypass Dylan/Rajat.** Kartik's support is a tailwind, not an alternate reporting line.
- **Trust-ledger: the one deliberate add (2026-07-11).** Highest ceiling on James's leadership trust ledger (`goals.md` Interview optionality), thinnest worked-together base — public support without shared work doesn't transfer to a hiring decision. Move: after the reorg settles, one architecture-level touchpoint (UPP-as-platform / Reflex substrate design review), framed as wanting his read, not his sponsorship. Chief Architects bond over systems thinking; this stays consistent with "let the work create the relationship" — it just gives the work a doorway.

---

# 14) Faisal Farooq — VP, Engineering (Trust & Safety, Signals)

## Role in my 6–12 month goals
- **UPP ally at the VP level.** Open and vocal supporter of UPP work. Very interested in personalization and recommendation systems.
- **Content/User Understanding connection.** His org owns content understanding and user understanding signals — directly relevant to Pinkerton M2 (User Understanding Summary) and UIC evaluation. **Bo's UU team co-developed UIC with my team — strong shipped-wins partnership at the IC level.**
- **Technical peer.** Very technical, academically inclined (KDD chair for many years). Values rigorous, research-grounded work. Sharp and engaged in technical discussions.
- **Zhao Bo's manager.** Connection into the Signals org.
- **Active Credibility Sponsor (post 5/4 EPD).** Director-advocate cultivation candidate per backlog #82 — accelerated significantly faster than prior "6-month horizon" framing.
- **Trust-ledger asset (2026-07-11).** #2 on James's leadership trust ledger (`goals.md` Interview optionality): VP-level, deeply technical, KDD chair — the profile that lands as an exec at an AI company. The Q3 advocate conversation now carries dual payload: Director-committee coverage *and* the opening of a technical peer relationship. The KDD paper (July 31 deadline) is the natural currency — he'll respect it as a real artifact.

## Current relationship
- **Status:** **Active sponsor (escalated 5/4-5/7).** Multiple direct touchpoints in past ~3 days.
- **Trust level:** **High** (escalated from Medium-High).

### Recent acceleration (5/4-5/7)
1. **5/4 EPD demo Slack DM** (Dylan + Faisal thread, 10:33 AM): *"This is great work 👏... last mile is the hardest... but at the same time capabilities are much more powerful than what we had when we built ML Flywheel (which was somewhat wannabe-agentic lol). Teams should definitely share the learnings..."* → **VP-built-the-prior-version vouching = high-credibility sponsor signal.** Dylan asked the right follow-up (*"who can we work with"*) — actively converting the offer into a working channel.
2. **5/4 dynamic triggering ELT** — engaged active in DM with cold-start concern; James responded with 3 design considerations. **Open monitor item** — re-engagement opportunity if he comes back.
3. **5/7 Jeff OH proxy presence** — Jeff repeated Faisal's *"Pinterest is investing in everyone's future"* framing as the right model for AI adoption across orgs. Faisal's voice in Jeff's voice = peer-VP narrative confluence.

## Operating plan
- **Convert open offers before they decay.** ML Flywheel collab offer (5/4) is a Faisal-initiated open loop — not yet executed. Lock scoping session within ~1-2 weeks. *"Many candidates → which is ship-worthy"* problem maps directly to Reflex Build stage.
- **Maintain visibility through natural forums** (ELT, AI forums, EPD).
- **Cold-start follow-up if he re-engages** on dynamic triggering (per `learned_dynamic_triggering_elt.md` open item).
- **Leverage his academic sensibility.** Senior technical validation for AI approaches — credible reviewer for KDD 2026 paper (Architecture chapter), RR cross-surface scaling, or any rigorous-research-grounded artifact.
- **Reuse Faisal's framings cleanly.** *"Pinterest is investing in everyone's future"* is now Jeff-validated. When discussing team adoption or AI-leveraged-leader thesis, attribute to Faisal explicitly when natural — peer-VP credit-share strengthens the cultivation arc.

## Verbatim language filed
- *"Capabilities are much more powerful than what we had when we built ML Flywheel (which was somewhat wannabe-agentic lol)"* (5/4) — self-deprecating about ML Flywheel positions James's work above his own.
- *"Pinterest is investing in everyone's future"* (proxy via Jeff 5/7) — Faisal's adoption framing, now validated and circulating.
- *"The last mile is the hardest"* (5/4) — Faisal's frame for the production-readiness gap. Connect to Pinkerton productionization conversations.

## 2026-07-25 — GenAI-signals-in-ranking thread: Dylan looped James in (DECISION OPEN — how to play it)

**The thread (8-member Slack group, screenshots on file):** Adam Avery ⟨role?⟩, Andrew Yaroshevsky (§9), Dhruvil, Lily Li, Faisal, Dylan, James +1. Topic: **integrating GenAI signal (and content-quality signals generally) directly into the ranking/organic stack.**
- **Andrew Y (initiator, last quarter):** believes signal-directly-in-stack "might be the largest lever"; senses Faisal is an evangelist too; Content MBR under-emphasizes the bet; asks Dhruvil+Lily to summarize tried/next + set a small review. His technical questions: both towers? per-activity sequence annotation? GenAI prediction directly in Utility with tuned weights?
- **Lily Li (status):** GenAI v3 integrated into pinnability as feature (content side + real-time user sequence, per-impression isGenAI → sequence-derived affinity features). First online exp as direct pinnability feature = **flat topline, no positive signal**; P2P-style user-tower sequence-embedding iteration = **negative offline, never tested online**. Their view: explicit GenAI penalty/boost belongs in **L1 utility (distribution shaping), not L3** (avoid double-counting; keep learned utility on action probabilities). Not yet a standalone L3 term.
- **Faisal (the meaty reply):** pattern generalizes to Racy/Borderline/self-harm signals. (1) Signal SOTA (beats Google, matches Hive) but push further; (2) **filter-thresholding uses <20% of signal strength** — 0.8 cutoff treating 0.79 as 0.01 is "fundamentally broken"; (3) last-mile filtering backfills slightly-different bad content + recovers too late; (4) **recsys are quality-unaware at training time → lopsided train-vs-inference incentives; must be inbuilt, not band-aided.** With Dylan he's discussed building the muscle so **any business objective (quality/safety/credibility) can be added to the stack** — same arc as the filtering-became-button-flip foundational work.
- **Close:** Andrew: "get together next week and make it happen," Lily to work with his ABP (Caitlin Boyd). **Review scheduled: "GenAI Signal in Ranking: What We Tried and What's Next" — Monday 7/27, 1:35–2:00pm PST.** James was added to the thread by Dylan at 5:53pm; **Dylan's public close (6:00pm)**: aligned with Faisal on "building a paradigm to capture quality/safety in our distribution system, happy to partner"; iterations already underway for ranking/retrieval signals; **currently experimenting with quality in L1 utility using the racy signal — GenAI could be considered**; and the load-bearing line: "**Ultimately, we should have trust in the team and leave to the team to design how the system works.**" (Reads directly on James's chime-in-or-not question: her public posture is delegate-the-design.)

**The Dylan move + James's read (7/25):** Dylan added **James** to the thread but did **not invite Dafang He** (§28 — who was supposed to lead this technically from her org) to the Monday sync. Dhruvil + Lily wrote the proposal and drove this for months. James's hesitations: (1) deep Snap experience on exactly this (quality signals into rec stacks) but new ballgame/new players; (2) unclear whether Dylan wants him in the technical design given Dafang/Dhruvil/Lily ownership; (3) incoming headcount+scope means unclear time budget.

**Engagement plan (RATIFIED 7/25 session):** Core frame — **the thread's own conclusion routes into James's platform** (Lily: explicit GenAI penalty/boost belongs in L1 utility; Dylan: racy-signal experiment already running in L1; L1 Utility = James's team's system, JJ/Rui owners, T&S filters already hosted). Engage as **platform owner receiving the work, not competing architect**. (1) **No substantive thread post pre-meeting** (Dylan closed it; posting reads as jockeying); post only a 3-line action summary after. (2) **Dhruvil DM this weekend** (additive-not-disruptive; covers NLFU alignment too) + read the proposal and the portfolio-MBR doc. (3) **Monday talking points:** the 4-place placement map (training-time / candidate-gen / L1 shaping / last-mile — endorse Lily's L1-not-L3 as platform owner); continuous L1 utility term answers Faisal's <20%-of-signal cliff (calibration first; weights tuned as tradeoff curves vs. an SSv2 guardrail budget); measurement reframe (flat-topline exp asked the engagement question of a quality mechanism — define quality metrics + SSv2 budget before mechanism, delivered gently); retrieval-side quality shaping = one-sentence later-phase seed. (4) **Bounded offer:** L1 Utility hosts the GenAI term as the next experiment behind racy; deliverable = 1–2 page placement doctrine + experiment plan, James's team hosting, **JJ (returns mid-Aug, L1 owner) writes, Rui operational — James edits, doesn't write.** (5) **Dylan 1:1:** confirm remit + how she wants Dafang positioned (folded into the Reflex role-clarity ask). (6) **Faisal 1:1 = PLAY BY EAR** pending how the Monday sync goes (James's call 7/25 — not scheduled; the training-time/UPP compare-notes + KDD seed stays in pocket).

## 2026-07-27 — GenAI review LANDED; working group formed; James = platform owner on record

- **The 1:35 review went well — James's talking points well received** (continuous-vs-threshold with their own numbers; measurement reframe; bounded L1 offer). Morning pre-work: James DM'd Lily + Dhruvil 8:30am (additive-not-disruptive); Lily revealed **the real driver: Bill + VPs 12-week GenAI-perception turnaround, Anoop Suri lead, vision doc MPR-approved last week**; L2 GenAIv3 feature exp (Dhruvil + Sameer Jain) = flat; Lily asked James's POV on L1 hosting GenAI v3 → James's principle on record: *hard-filter the confident worst-of-the-worst; use the uncertain middle as personalization signal; goal may not be SSv2 but visible user-facing treatments.*
- **James created `#genai-feed-wg`** (Dylan, Faisal, Andrew Y, Dhruvil, Lily, Michael Weissinger, Adam Avery ⟨role?⟩, Qinglong Zeng; James added **Dafang He**; Qinglong added **Jianing Sun** ⟨resolved 8/19: Qinglong's TL — drove SSD spacing for CQ + demotion on other surfaces⟩). Lily's one-pager: "Advancing GenAI Signal Adoption in Personalization." Next steps: **James + Dhruvil + Lily → concrete plan**; Michael W + Lily starting success-measurement convos with CQ (incl. perception/perceived relevance).
- **Qinglong Zeng (CQ team — new contact):** strong +1 on multi-layer-not-filtering-only + one shared metric stack. His speed-to-value stack: **(P0) demote GenAI *slop* for all users** (graded utility penalty conditioned on GenAI × domain quality × high-pain verticals — uses full score spectrum); **(P0) demote GenAI for opt-out/low-affinity users** (CQ just productionized a **GenAI user-affinity signal**; per-user penalty strength from opt-outs + hide/See-Less/report); **(P1) GenAI spacing** (reuse SSD spacing framework; P2P spacing won: ~32M low-quality GenAI impressions removed, DAU lift, +1.7% clean impressions low-signal users; HF = most sensitive surface, next target); **(P2) training-data cleaning** (offline validation first).
- **Dylan ratified priorities in the PM 1:1:** L1 Utility experiments — **GenAI = higher priority than trust and safety (racy demoted to backup signal)**; beyond filtering: (P0) Spacing/L3 SSD · (P0) L1 Utility · (P1) features in models · (P3) training data; **coordinate with Dafang.** NOTE: flips the 7/25 "GenAI behind racy" sequencing — GenAI term now leads.
- **Signal of record:** `PIN_FEATURES:content_quality_gen_ai_v3_score` (Faisal posted the mlhub link within minutes of James's ask for Dafang — warm, fast engagement).
- **Faisal DM (3:01pm): added James to the AI-pods projects doc** — follow-up to James asking at a Jeff EM sync which efforts are in the AI-pod working model. Response pending (see engagement plan).
- **Status: James + Dafang coordinated; awaiting Dafang's ping on next steps.** Faisal 1:1 still play-by-ear — today's warmth (signal link + doc add) argues for letting the WG momentum carry; pocket items stay pocketed.

## 2026-08-14 — the 7/27 thread became a CTO-visible program: **Safe Journeys**

The GenAI-signals-in-ranking thread grew into a teen-safety program. Faisal co-authored the ACP vision (*"Safe Journeys — discovery should inspire, never endanger"*) with Michael Weissinger, Dylan, and Andrew Y, and wrote his own problem-statement doc (*Teen-Aware Pinterest Experience*). **James is a named Eng POC on two of the five workstreams.** All docs filed: `work/projects/safe_journeys/sources/`.

**His July Slack argument is now the program's pillar 2, near-verbatim** — "filter-thresholding uses <20% of signal strength" became *"leveraging the entirety of the information from our content quality signals rather than simply a threshold."* Treat §14's 7/25 entry as the intellectual origin of the whole program.

**Faisal's key points, consolidated across all three sources:**
1. **The signal is SOTA and we throw most of it away.** Beats Google, matches Hive; a 0.8 cutoff treating 0.79 as 0.01 is "fundamentally broken."
2. **Last-mile filtering is structurally losing** — filtered slots backfill with slightly-different bad content, and it recovers too late.
3. **Train/inference incentive asymmetry** (his deepest point) — recsys are quality-unaware at training time, so the model has no incentive to prefer safe content and we fight our own model every request. "Must be inbuilt, not band-aided."
4. **Imperfect signals make bad gates but good gradients** — his resolution to the precision/recall objection, and the elegant part.
5. **The reward loop is the enemy** — borderline content earns engagement, engagement reinforces, feed spirals.
6. **Traditional safety metrics are the wrong shape** — prevalence measures average exposure, user reach misses individual severity. Hence density / LLM-judged feed quality / USR.
7. **He has pre-paid the engagement cost:** *"drive it down, even with localized SSv2 cost. This is the engagement we do not need on Pinterest."* Important — it means "engagement and safety are the same North Star" is a claim he has already publicly qualified.
8. **The real ambition is a platform, not a fix** — with Dylan he has discussed building the muscle so **any** business objective (quality/safety/credibility) can be added to the stack. Teen self-harm is the proof point.
9. **Method:** bias to action, explicitly not a PRD/TDD, living doc, "we will not try to perfect this document." Bring him a prototype and a sharp question, not a polished 12-week plan.

**Two proposals of his that appear nowhere in CQ's design doc:** the curated teen-safe pool (flip allowlist-by-exception → denylist-by-exception; "worst-case feed quality is bounded by the quality of the pool, not by the recall of our filters") and LLM-in-the-loop feed auditing as both metric and training signal.

**Engagement note:** the one technical contribution that *strengthens* his thesis rather than challenging it — **his <20% argument depends on calibration.** A threshold needs the score correct at one point; a graded penalty needs it correct everywhere. Going continuous raises the signal-quality bar rather than lowering it. Nobody in the docs has named this.

### 2026-08-16 — CQ political map + the Qinglong co-authorship play (from James, prepping the Mon 8/17 1:1)

**Bad-blood geometry: [Qinglong + Andre (his eng director)] vs. Dylan's org.** CQ as a bloc, not Qinglong-vs-his-own-boss. Three standing fights:
1. **CQ wants a final layer *behind Blending*** that owns all placement + quality control. Recsys side thinks this is ridiculous (architecturally: one gate can't see the candidate set for density, can't clean the P2P graph, can't carry cross-surface session state).
2. **CQ pushes L2** as the enforcement point; James's side has pushed back historically.
3. **CQ wanted spacing;** James's side countered "**do diversification instead**" — now codified in the placement doctrine (§1.3/§4.3: diversity/density over spacing).

**Approval chain: Qinglong → Andre → Faisal.** Andre = territorial, has a veto, and per Dylan "can get really annoying." **Faisal is Andre's manager = the stronger approver — and he's James's ally + the thesis-author James's doctrine amplifies.** Implication: aim joint artifacts *up at Faisal* (+ Michael); Andre's veto is not fatal.

**Dylan's handling doctrine for Andre's team:** *give them an ask, something to do, so they don't get annoyed.* The co-authorship play is exactly this, executed at the Qinglong level.

**James ↔ Qinglong specifically:** historically okay; his Slack signals he wants to collaborate. BUT the last two syncs they clashed **hard on L1-vs-L2 in front of team members** (James advocated L1 for signal placement; Qinglong adamant about not precluding L2). Nothing irreversible.

**The play (ratified direction, landing at Mon 8/17 1:1 — private):** co-author the placement doctrine, **James first author, his frame the spine**; Qinglong owns the intervention-design region (his Design Options doc's home turf, and where James's L2 concession lives), James owns placement + calibration + measurement. Sequence: open on common ground (dissolve L1/L2 as "the wrong 25% — Homefeed is a quarter, RP is ~50%"), concede first (L2-for-trajectory §5.2, his loss-reweighting = James's `(1−q)·E` §4.5, corpus placement), then offer, then point up at Faisal + Michael. **Leave the post-Blending-final-layer ownership question open (doctrine §6) — don't detonate it in the 1:1; the doc's distributed architecture wins that territory over time.** Note: `placement_doctrine_v2.md` is NOT circulation-safe — cut §7 + internal blockquotes (§3, §5.4) before sharing Thursday.

## Role in my 6–12 month goals
- **Growth org leader.** Owns all of Growth (122 reports). His org was pushed into UPP by Jeff — initial friction, but he acted magnanimously and is now a big supporter of Dylan's organization.
- **Close to Dylan.** Natural connection as they came into the org around similar times. Good political alignment.
- **Trust anchors in his org:** Brian Lee (long-term ally, AI forum host) and Tingting (owns Notifications, good relationship with James + Bella). Notifications CLR results (+286k WAU shipped/in-flight) are in Shipeng's org.

## Current relationship
- **Status:** Positive. James has publicly aligned with Shipeng on responsiveness for low signal users. Mutual respect.
- **Trust level:** Medium-High (indirect trust through Brian, Tingting, and shared UPP support)

## Operating plan
- **Maintain through allies.** Brian and Tingting are the natural relationship anchors. Keep those warm.
- **Cross-surface results tell the story.** Notifications CLR wins are the strongest proof point that UPP benefits Growth. Let the numbers speak.
- **Don't over-engage directly.** Shipeng is a Sr. Director; the relationship should be light-touch and signal-driven, not high-maintenance.

---

# 16) Yan Li — Sr. Manager, P13N-Experiences (Peer under Dylan)

**Level:** **L17 Sr. Manager** — peer-EM altitude with James + Dhruvil. Verified via Slack 2026-05-23.

## 2026-08-05: Wed touch-base #2 (announcement day; James's transcript, some garble) — leaning in, new standing structures, the Thursday frame

- **Posture: leaning in, not checking out.** "Overall it's good for Daniel's team — stay closer with real ML experts, work on deeper projects." On himself: Dylan "trying to do what's best for the organization"; "room to grow as a lead on the experiences side"; "not necessarily a setback in one dimension — could be an opportunity in another"; **"I want to lean in here."** Bittersweet losing a long-time team, said plainly, no bitterness. → Near-term exit-risk read softens; the capture-his-context-before-it-evaporates discipline stays (cheap insurance).
- **He handed James the Thursday message frame:** every team adjusts a 6-month roadmap — but adjustments here run **"based on project priority and purpose, not the report chain"** (his words: that message makes the team 安心 + freer). And: "still figuring things out" is fine **only with a concrete clock** — tell them "next 3–4 weeks → a clear answer" on where H2 roadmap adjusts.
- **New standing structures agreed live:** (1) **weekly James↔Yan 1:1, at least Q3** · (2) **three-way James+Yan+Daniel sync weekly-or-biweekly** (Yan's proposal; James's stated posture: "mostly there to learn… I honestly do not see myself making any decisions") · (3) **H2-roadmap deep-dive sit-down** (James+Yan+Daniel+related parties) **~end of wk of 8/10** — the engine behind the 3–4-week answer · (4) **James added to both IB meetings**: Tue 30-min IB leads sync (working-group register; Yan sometimes wants James's read on area-dependent things) + weekly 30–45-min **Andrew check-in** (Andrew = ultimate TL, "operation mode like Cupcake before"). James's deference explicit — asked Yan how to participate so his presence doesn't undercut Yan's leadership.
- **Q3 operating agreement (de facto):** Daniel's team continues UGC Board Recs + IB + UEB support; James: "I wasn't involved before — whatever is working, we should continue." Division: **James takes the people line first** (career, "do my agreements with Yan persist?" questions), **project/process stays Daniel→Yan for now**. Yan's structural ask: he used to arbitrate cross-team priorities solo; that's no longer appropriate — **wants James inside those decision processes** ("you also get a responsibility"). James committed support.
- **Yan on Daniel:** wants to confirm **Daniel is genuinely OK with the continued-support arrangement** — "we can even ask him how he feels"; floated a transition phase. Yan↔Daniel 1:1 Friday; Yan meets **Daniel + Alim together next week** — wants the two of them to clarify **what they each want to own**.
- **Garbled passage RESOLVED 8/5 PM:** the person with retrieval background "who knows people here and is already reconnecting" = **Daniel** (ex-TL on Homefeed CG — James confirmed while building the 8/6 meeting frame). The Monday first-meeting visitor to Yan was likely Alim (new manager, intro); the two referents were blended in transcription.
- **IB sprint outcome answer:** post-10-week sprint → **mostly dogfood, not A/B**; LLM serving constraints to solve; long iteration loop ahead.
- **His Thursday-meeting suggestion (parting note):** some team members have had **2 reorgs in 1 year** → they want certainty + stability; and **"if you want to propose that there's scope for senior team members, that's actually a good thing"** — dovetails with the Balaji/Kim skip-level design.
- **Must-wins NOT visible in the transcript** (may be partial — confirm with James before treating as missed): Daniel's H1 input mechanism+date (the hard clock) · Kim Toy allocation (needed before Thu Q&A) · +300K WAU holdout pointer · POC pair · inherited people-commitments list. Recovery = the designed async fallback: same-day draft-and-correct DM.

## 2026-08-03: First post-reorg 1:1 (12:30, moved up from Wed at his ask) — continuity frame, James's commitments, new names

- **Constructive and receptive** (matched Dylan's advance read; beat the 8/1 "likely bitter" expectation). His frame: *manager change is survivable — project change is the risk.* Concerns: **IB dogfood sprint at critical stage** (10-wk sprint, ~wk 5; ~half the engineers across his + Daniel's + Edward's teams) and **UEB/unified plumbing** (Roderick = single point of failure). Team fragility context: his team joined P13N ~mid-March, then reorg + layoffs.
- **His ask: freeze people-to-project mapping through Q3, revisit after.** Scar tissue: **AMB (IB's previous iteration) never launched last year — big morale hit.** → One of the two inputs behind James's same-day **T2 → Nov 2026** move.
- **James committed:** no immediate change; roadmap supported Q3 + very likely Q4; documented asks + priorities → funded; **Q1 = defined long-term support model with clearer API/tech-stack boundaries — ngAPI vs Unified split, Unified more self-contained on James's side.** This revives the direction of Yan's own Unity-HF ownership proposal (May) — he engaged positively ("这是一个很好的讨论点").
- **His candid IB read — 1:1-ONLY, never cite onward:** IB = visibility project (leadership ask), big investment, deliberately conservative start, small Q3/Q4 scale; **UGC Board Recs = real holdout gains (~+300K WAU per him, unverified) that leadership undervalues.** James undecided (8/3) how much of this reaches Dylan.
- The SWE-retention ask (from Dylan's AM readout) **never arose live**. New name: **Jonathan Luna — Sr SWE under Yan, works on ngAPI** (James invoked him re: the split; full context TBD).
- Next: Wednesday touch-base + the 8/4 four-way comm-plan meeting. Full transcript-level debrief: `reorg_july2026/announcement_week_timeline_2026-08.md` 8/3 banner.

## Role in my 6–12 month goals
- **Presentation-side peer EM.** Yan's team is a composite with 2 sub-EMs (Slack-verified 2026-05-23): **Daniel Liu** (Manager II, L16, ML — 8 directs) + **Edward Zhuang** (Manager I, L15, backend SWE — 7 directs). Came in during the reorg. Ownership negotiation (explore seeds, UIC-to-medoid logic, unity-gulp integrations) substantially closed via 4/3 consensus (Dylan + Dhruvil + Yan + James on CG / P13N-Experiences split).
- **Peer under Dylan.** One of the managers reporting to Dylan. Dylan wants Yan's team to lean in on Explore/IB backend work. **Partner, not peer-friction** — locked 4/3.

## Profile
- Professional, calm, mature manager. Manages up well. Contrasts with James's fast/builder style and Dhruvil's steady/framing style.
- Operating at high altitude — proposing frameworks and ownership models without deep codebase engagement yet (understandable for someone new).
- Wrote a detailed Unity-HF Ownership Proposal using "Glean and Claude Code" — unclear if his own engineers fully reviewed.
- Has TLs: AJ Oxendine (Staff SWE, direct/assertive, raising real architectural concerns), Daniel Liu (EM, ML lead, has reviewed ownership doc).

## Current relationship
- **Status:** Constructive. James welcomed the ownership doc, asked the right process question (have TLs reviewed?), offered collaborative posture. Group sync with Dylan scheduled for April 3.
- **Trust level:** Neutral/Early (limited history, no friction, no deep collaboration yet)

## IC-Level Friction
- AJ (Yan's team) and Devin (James's team) have had friction in Slack over explore seeds logic ownership. Multiple engineers on James's team independently describe AJ as difficult to work with.
- James's assessment: AJ's concerns are substantively legitimate — friction is a symptom of the ownership gap, not a tone problem. Will resolve through structural clarity.

## Operating plan
- **Welcome his ownership.** James wants CG scope contained to ML/retrieval core. Routing, explore seeds, surface glue = natural fit for Yan's team.
- **Propose maintenance vs development split.** CG maintains what it built, new surface development resourced by Yan's team.
- **Offer transition support.** Onboarding/guidance through Q2, clean handoff by May.
- **Address AJ friction in Yan 1:1, not group settings.** Frame as collaboration pattern to improve, not personnel complaint.
- **Build working relationship density.** The Dhruvil/GULP model worked through shared debugging — engineer the same organic collaboration with Yan's team.

## 2026-05-20 Update: Partner reframe locked + IB redeployment intel + Scenario E shape

Three updates carried out of the Dylan H1 career convo (week of 5/18) and prior intel.

**1. Partner-not-peer-friction reframe is locked** (per 4/3 consensus — Dylan + Dhruvil + Yan + James on CG / P13N-Experiences ownership). The earlier "active ownership boundary negotiation" frame is substantially closed. Yan = partner in the presentation-side org, not friction surface. Don't reactivate ownership-defense posture. See memory: `project_april_3_consensus_operating_frame`.

**2. Yan/IB redeployment intel — high-fragility, do NOT propagate.** Per 2026-05-15: Andrew is considering cutting Intelligent Board and redeploying Yan's ML engineers (Daniel Liu's team) onto James + Dhruvil's projects. **Paperwork prepared, not approved.** Treat as latent signal only. Do not surface to Yan, Daniel Liu, Dhruvil, or the team. If it lands, James's team gains ML capacity directly. If it doesn't, the partner frame holds as-is. See memory: `project_yan_ib_redeployment_live`. **→ LANDED 2026-07-07: this is exactly what materialized — Daniel Liu's team + IB/exploration scope reorg under James (approved, downward comms mid-July). Fragility flag lifts once Dylan's downward announcement happens; until then still do not propagate. See `reorg_july2026/daniel_liu_team_2026-07.md`.**

**3. Scenario E team-design implication.** In James's preferred Scenario E (cross-surface AI personalization capability under James), Yan reshapes as a coherent presentation-side EM — Tim potentially consolidates under him, Daniel Liu's ML team consolidates under James (desirable not essential — push but don't ship plan dependent on him). Scope trim locked from the H1 convo work: **Unity-for-IB → Yan side**, **Responsiveness → surface side**. Don't frame this to Yan directly; it's organizing logic for the Dylan input artifact, not a Yan conversation yet.

**4. Voice-transcription cleanup.** "Yen" → Yan; "Daniel Liu" → Daniel Liu (Yan's TL, ML lead). Names corrected throughout the chapter doc + artifact draft + this profile.

## 2026-07-15: Peer-feedback read (drafted gently — reorg context)
- **Strengths (from cupcake_lookback notes):** brings structure + leadership unity to ambiguous cross-team situations (authored the Unity-HF ownership proposal; the CG↔P13N transition closed as partnership, not turf war); genuinely **collective** — proactively suggested a live EPD retro session ("having a live session would be helpful for folks to share their thoughts collectively").
- **Growth (deliberately soft):** the honest read is high-altitude framing **without deep codebase engagement** (James's briefing §F). But James chose to write this **gently** — because the reorg moves **Daniel Liu's ML team out from under Yan → to James**, and piling a technical-depth critique onto someone losing ML scope reads as ungracious. Encoded only as an *opportunity* ("bring framework strength into closer contact with the execution layer"), never as a gap. Did NOT reference the AJ/Devin IC friction.

## 2026-05-23 Update: Revised preferred shape — Yan as Presentation + Performance vertical

Following Anna conversation + Tim conversation + Slack-verified org chart (see `dylan_archive.md` Appendix III-C 5/23 update for full context).

**James's revised preferred shape positions Yan as the Presentation + Performance vertical:**
- **Yan owns:** Unity ownership + PWT (Pinner Wait Time) + latency + **Tim Leung reports to him** (so Yan controls full presentation stack: ngAPI backend + Android/iOS client through Tim, plus Unity, plus PWT/latency as his own vertical).
- **Yan may absorb some of James's SWE-heavy scope** (specifics TBD — open variable).
- **Yan loses Daniel Liu's ML team** (consolidates into James, since they're "barely helping" on UIC/pUIC build despite ML-adjacency).
- **Edward Zhuang stays under Yan** (likely — provides backend SWE pool for PWT/latency/Unity vertical).

**Net read on Yan in this shape:** *Substantial scope expansion in a different domain* — bigger team, more presentation surface area, performance/latency as his own load-bearing vertical. PWT and latency are user-facing business outcomes, not "support infrastructure" — meaningful scope, not consolation.

**Pronouns:** Yan uses **he/him** (corrected 2026-05-23 — earlier Leo updates used "her" wrongly).

**Do NOT propagate this shape to Yan yet** — it's James's input to Dylan, not a Yan conversation. Yan-acceptance is Dylan's problem to navigate, not James's. The 4/3 partner-frame still holds for ongoing 1:1 cadence; team-design discussion stays at Dylan-altitude until James decides delivery.

---

## Sub-EMs under Yan (Slack-verified 2026-05-23)

### Daniel Liu — Manager II, ML Engineering (L16, sub-EM under Yan)

**NOT under ATG.** Previously written as "Daniel Lu" in Leo files due to voice transcription artifact — **real name is Daniel Liu, corrected throughout.**

- **8 direct reports** (verified Slack 5/23): Kim Toy (Sr. MLE), Yang Liu (Sr. MLE), Yongwoo Noh (Sr. MLE), Ling Lan (MLE II), Balaji Rengarajan (Staff MLE), Felix Yang (SWE II), Roderick Gao (Sr. SWE), Rita Lyu (Intern).
- **Cross-team work:** Daniel Liu's team works WITH James's team AND WITH ATG team on UIC/pUIC pipeline.
- **James's 5/23 read:** "barely helping" on the substrate build itself. Candidate for consolidation into James's CG scope in revised preferred shape.
- **Relationship:** Daniel personally said he wants to work with James + team on anticipation/UIC (per pre-China 1:1, done 4/26 sweep).

### Edward Zhuang — Manager I, Engineering (L15, sub-EM under Yan)

- **7 direct reports** (verified Slack 5/23): Josh Arriola (Sr. SWE), Jiaqi Tong (Sr. SWE), Tianhao Shen (SWE II), Allen Pan (Sr. SWE), Yutong Jin (SWE II), Yash Patil (SWE II), Sreesha Venkat (Sr. SWE).
- **All SWE — backend pool.** Likely owns Unity layer / lower-stack backend (recsys infra-side), distinct from Tim's ngAPI presentation-backend.
- **In revised preferred shape:** Edward likely stays under Yan to provide backend SWE pool for Yan's PWT/latency/Unity vertical. Could be partial absorption into James depending on what "SWE-heavy scope James gives up" resolves to.

---

# 17) Tim Leung — Manager II, Presentation (under Dylan)

**Level:** **L16 Manager II** — sub-EM altitude. Reports **directly to Dylan** (verified via Slack org chart 5/23) — NOT under Yan currently, though James's 5/23 preferred shape proposes Tim moves under Yan as part of presentation+performance consolidation.

## Scope (corrected 2026-05-23)

**Tim owns BOTH ngAPI backend AND Android/iOS client engineering** — earlier "Frontend / Client only" framing was wrong. Tim runs presentation broadly:
- **ngAPI backend engineers** — currently constrained scope ("too little scope, stuck on ngAPI" per Tim 5/23). Natural scope extension: Unity layer, where James's engineers have most knowledge.
- **Android / iOS client engineers** — heavy legacy codebase, hard to make progress per Tim's own observation.

## Role in my 6–12 month goals
- **Ally and mentee.** James sees himself as a mentor to Tim. Great interactions and collaboration history.
- **Presentation partner.** Tim's team handles all presentation-side work (server + client) that complements James's ML/retrieval org.
- **Yu Zhao connection.** Tim's TL Yu Zhao is one of the best engineers in the org. James works with Yu Zhao through JJ on responsiveness — strong collab.
- **Director-relevant constraint:** Tim's L16 altitude means he should report through an L17 peer-EM under any team-redesign (current direct-to-Dylan reporting is anomalous for the level). See [[project-team-member-levels]].

## Current relationship
- **Status:** Strong. Mentorship dynamic + active collaboration through JJ ↔ Yu Zhao on responsiveness.
- **Trust level:** High

## 2026-05-23 conversation signals
- Tim shared the ngAPI scope-constraint observation candidly.
- Tim acknowledged client engineering's legacy-code drag.
- **No indication Tim has been briefed on the proposed reporting-line move under Yan** — James's read of "should report through L17 peer" is operating logic, not a Tim conversation yet.

## In James's revised preferred shape (5/23)
- **Tim reports to Yan** (presentation + performance + Unity consolidation under Yan).
- **James does NOT take Tim or client engineering** — firm constraint. *"It'll take a lot to convince me otherwise. It just doesn't make sense unless I have Tim reporting to me and grow his client engineering scope more, which then doesn't make too much sense for Yan."*
- **ngAPI backend engineers may extend into Unity** — strengthens cross-stack linkage; backend engineers gain growth scope; Unity capability concentrated where James's engineers already have depth.

## Notable: Raymond Hsu
- Reports to Tim. Was the previous HF CG manager before James joined above him. Transitioned back to IC unwillingly by Dylan and James's decision. Holds resentment. Not an active risk but worth awareness.

## Operating plan
- **Maintain the mentorship.** Low cost, high goodwill. Tim being successful reflects well on James.
- **Keep JJ ↔ Yu Zhao collaboration strong.** This is producing real value on responsiveness.
- **Do NOT propagate reporting-line-under-Yan proposal to Tim** until Dylan-side decision lands. Premature surfacing creates uncertainty without enabling action.

---

# 18) Francisco Navarrete — Sr. Manager, Platform/Labeling (under Dylan)

> **2026-08-26 — LAID OFF this morning, with most of his team (~15 people incl. Francisco).** Per James: the outcome of a beginning-of-2026 decision that sat for months in regulatory approval (team primarily in Mexico). The "exiting to Kurchi" line below is superseded — the move never became a home. Keep the relationship warm personally; he's no longer a Pinterest ally.

## Role in my 6–12 month goals
- **Peer and ally under Dylan.** Good mutual respect — exchanged compliments during calibrations. Collaborative before the reorg.
- **Platform work overlap.** Francisco has worked on debugging tooling (never took off). His team does foundational platform work for all of Core — constantly stretched.
- **Mexico-based team.** 16 reports, primarily in Mexico.

## Current relationship
- **Status:** Positive. Mutual respect from calibration interactions. Previous collaboration. Good relationship.
- **Trust level:** Medium-High

## Key dynamic
- His team is stretched thin by horizontal platform work for all of Core. Hard to get bandwidth from them. Not a collaboration friction issue — just a resourcing reality.

## Operating plan
- **Keep the relationship warm.** Francisco is a natural ally in Dylan's org. Low-maintenance, high-trust.
- **Don't depend on his team for resourcing.** They're stretched. Factor this into any cross-team planning.

---

# 19) Kaanon MacFarlane — Director, Engineering (under Rajat)

## Role in my 6–12 month goals
- **Repositioned, not marginalized.** Previously under Dylan; now reports directly to Rajat. Working with Karina on an AI initiative for Rajat.
- **Frontend/backend, no ML.** His team (34 reports) doesn't overlap with James's ML/retrieval scope.
- **Francisco and Tim's former manager.** Both were under Kaanon before the reorg moved them to Dylan.

## Current relationship
- **Status:** Minimal direct interaction post-reorg.
- **Trust level:** Neutral

## Key context
- Dylan previously told James she "doesn't want to go through him" — this was before the reorg moved Kaanon out of her chain. Now a moot point.
- Rajat is using Kaanon + Karina for AI delivery work. They own frontend/backend execution, not ML.

## Operating plan
- **Low priority.** Kaanon's scope doesn't intersect with James's. Monitor if the AI initiative creates overlap, but unlikely given the no-ML constraint.

---

# 20) Akshanta — PM, P13N-Experiences (Yan's team)

## Role in my 6–12 month goals
- **Cross-team PM on Yan's side.** Akshanta is the PM counterpart for Yan's team. Her work overlaps with James's team on the Explore/CG boundary — she needs updates and context from James's engineers.
- **Dylan thinks she's good.** Dylan specifically named her when delivering PM tone feedback, signaling the source is credible and the relationship is worth investing in.

## Current relationship
- **Status (updated 2026-07-09): Cordial — repair landed.** Warm DM + cordial 1:1 both happened post-April. James's own read 7/9: "no real conflict with Akshanta other than our brief conversation about Lily Li."
- **History (April 2026):** two incidents created a "territorial manager" impression — (1) Slack routing her through Crystal instead of engineers, correct ask / cold delivery; (2) likely heard about the Lily Li office-hours incident PM-to-PM. She (and/or Lily) surfaced tone concerns to Dylan → April 3 yellow-flag delivery. Her account also likely corroborated the pattern in Andrew's 7/9 mid-year feedback (§9).
- **Character read (7/9):** she stuck up for Lily — a junior colleague — against a fast senior eng leader. Respect-worthy, and consistent with why Dylan rates her. Treat the advocacy as a credit, not a grievance.
- **Trust level:** Rebuilding, no active friction.

## Operating plan (updated 2026-07-09)
- **Post-reorg overlap is the real opening.** James and Akshanta may work more closely after the reorg. When the overlap materializes: invest early and first — an opening 1:1 framed around the work, ask her opinion publicly early, credit her visibly on the first collaboration. Let shared work do the repair gestures can't.
- **Until then:** normal warmth in organic interactions. No manufactured outreach.
- She's Dylan-credible — her read of James travels. The first real collaboration is worth over-investing in.

---

# 21) Lily Li — PM (newer, reports up Andrew's PM chain)

## Role in my 6–12 month goals
- **Upgraded from "low priority" 2026-07-09.** Lily reports into Andrew Y's org (new intel 7/9) — her account of the office-hours incident is almost certainly the anchor case behind Andrew's mid-year growth feedback (§9). She is the single most legible repair surface for the one named gate on the Director case (Dylan Feb: "limiting ceiling"; Andrew July: "next level of leverage").
- **Likely lands under Michael (§38)** when he starts 7/13 — chain to confirm.
- **History:** Lily was pinging James's engineers directly for mundane tasks (adding users to holdouts, etc.); Yuke escalated; James told her to back off in front of TPMs (including Akshanta's TPM). Justified ask, strong delivery.

## Current relationship
- **Status:** Wary of James (his read, 7/9). No current project overlap — no organic contact surface.
- **Trust level:** Low.

## Operating plan (upgraded 2026-07-09 — structure, not gestures)
- **Still no formal apology or cold outreach.** Unchanged from April, now with sharper reasoning: with no work surface, any approach is unanchored — she'd correctly read congratulations/welcome overtures as performative or as a trap. James's instinct on this is right.
- **Group rooms only, never cornered 1:1s.** Her wariness means she carries the interaction cost. Warmth in witnessed, agenda-driven, no-ask settings (Michael's onboarding rounds will create these organically) is safe for her; private outreach is not.
- **The real repair moment = her next ask of James's team.** The original wound was "stop coming to us"; the healing inverse is generous, fast, easy help the next time she needs something. If the XFN self-serve framework ships (§9 H2 moves), it depersonalizes the entire friction class — mundane asks get a paved road instead of a gatekeeper.
- **Horizon: months, not weeks.** Wariness decays through repeated uneventful exposure, not through words. Count neutral reps, not breakthroughs.
- **Never route repair through Michael.** He manages her (likely) and is James's close ally — any hint she's being handled via her boss deepens the damage under a layer of politeness.

## 2026-07-20: The repair moment arrived — and executed as designed

Her SM/SL staffing ask became a 15-min sync (Andrew, Dylan, Michael, James). The operating plan above said the real repair = generous, fast, structured help on her next ask of James's team — that is exactly what ran: James offered named co-ownership of the retrieval side, asked her directly where asks get stuck, and committed a POC by EOW when she asked for one ASAP (she took Friday happily). She closed with **"thank you so much for your ownership James!"** (jointly with Andrew), in front of her likely new boss Michael. First substantive positive interaction since the office-hours incident. Status shift: wariness → a working-partnership channel opening. The POC (Yali or Hedi) becomes her day-to-day contact and the Raymond-facing channel, keeping James at warm EM altitude per design. Keep counting neutral-positive reps — this was the first big one, but the horizon is still months.

---

# 22) Manu — Senior Director, Data Science (added 2026-04-11)

## Role in my 6–12 month goals
- **New stakeholder, surfaced via PINvestigator demo to Jeff (week of 2026-04-07).** Manu publicly interjected during James's demo: "Your team should follow my team — we're building something similar." Read as: legitimate adjacent work + competitive territorial signal in the room.
- **PINvestigator overlap risk.** His team is building something adjacent to PINvestigator. This is the load-bearing reason Jeff stayed silent at James's demo (didn't want to publicly referee a turf overlap in a 10-minute slot).
- **Dylan opened a door.** After the demo, Dylan shared a front-end DS tool from Manu's team to see if there are integration possibilities.

## Current relationship
- **Status:** New, low information, mildly competitive.
- **Trust level:** Unknown. Has not had a 1:1.

## Operating plan
- **Route through Kareem** (Manu's report) — turn the overlap into a partnership, not a competition. James already engaging Kareem.
- **Reframe Dylan's front-end integration ask:** "Not a front-end fit (PINvestigator is a Claude Code skill), but I see an analytics-agent integration path. I'll scope it with Kareem and JJ." Preserves the Dylan signal AND routes through the actual technical fit.
- **Strategic goal:** Get Manu's team *using* PINvestigator. The moment Manu's org is a PINvestigator user, the overlap dissolves and Jeff has nothing to referee.
- **Do not chase a direct relationship with Manu yet.** Build through Kareem first, then surface upward when there's a partnership story to tell.

## 2026-05-20 Update: Dylan actively building relationship with Manu

Per H1 career convo: Dylan named Manu as someone she is *"trying to actually also continue building some new relationship with"* — *"He actually presents a lot in terms of how the team is doing, making decisions, etc. He has a very strong opinion coming from a good place."* **Implication for James:** Manu is now a Dylan-priority-relationship-build target. The Kareem-led PINvestigator partnership path remains right, but the upward arc (Manu directly) has just gotten warmer because Dylan is independently building. If/when Manu's team is using PINvestigator, surface the win to Dylan — it reinforces her own Manu-relationship investment.

---

# 23) Kareem — Manager, Data Science (under Manu, added 2026-04-11)

## Role in my 6–12 month goals
- **PINvestigator partnership lead.** Already in motion as the manager James is engaging from Manu's org. Critical unlock for Manu-org goodwill and the path to converting Manu's "we're building something similar" into a co-pilot relationship.
- **Defuses the Jeff demo political dynamic.** If Kareem's team is using PINvestigator, the territorial signal Manu sent in the demo evaporates.

## Current relationship
- **Status:** Active outreach in progress (James engaging Kareem).
- **Trust level:** Building.

## Operating plan
- **Accelerate the partnership.** Offer PINvestigator to Kareem's team as a co-pilot. Make adoption easy.
- **Position as practitioner-to-practitioner.** Don't lead with credit framing or scope battles. Lead with "let's both ship something better together."
- **Update stakeholders.md once Kareem is committed** — promote from "in motion" to "active partnership."

---

# 24) Armando Ordorica — KDD Paper Operational Engine (added 2026-04-11)

## Role in my 6–12 month goals
- **KDD 2026 paper load-bearing co-author.** Owns Representation, Prediction, Federation, and Evaluation subsections of the Architecture chapter — i.e., most of the technical heavy-lift sections. Setting up the new repo + Cursor environment for the team.
- **The operational engine of the paper.** James is the architect (Prior Work + Architecture chapter lead + Future Work, all sole-author), but Armando is the one actually shipping the technical content for most subsections.
- **Critical bridge between James + Anna's vision and the experimental engineering work.** His framing notes (OmniSage piggyback, "predict not at point-wise change," composite rewards / user-level Explore/Exploit / global SID, PinnerSage offline results as insurance) are the spine of the paper's defense strategy.

## Current relationship
- **Status:** Active KDD collaboration. Trust unknown (new stakeholder for Leo's map; in active partnership for the paper).
- **Trust level:** Building.

## Operating plan
- **Treat as a load-bearing peer.** He owns more KDD paper sections than James does. Don't micromanage the technical subsections; trust his framing.
- **Coordinate on the OmniSage piggyback defense.** James (Architecture author) needs the one-paragraph "what's reused, what's novel, why the new construction is non-trivial" defense ready before draft v1. Don't let Armando be the only one who can answer the novelty question under reviewer pressure.
- **Watch the experiment-results dependency.** Armando flagged "feedback loop has good offline eval design, needs experiment results." If experiments slip past July 31, paper slips. PinnerSage offline results are the insurance.
- **Default is let the work speak.** Don't push credit framing. (See `feedback_credit_in_trust_relationships.md`.)

---

# 25) Olafur Gudmundsson — Sr. Staff ML Engineer (IC17), direct to Dylan (added 2026-04-11, upgraded same day)

## 2026-07-15: Level + role + peer-feedback read
- **Level confirmed: IC17 Sr. Staff ML Engineer, direct to Dylan.** **TL for MDD.** Worked with James on **Retentive Recs (Retentive Feedback Loop, UIC work, KDD Federation subsection)**.
- **Strengths (James):** raises the technical bar and adds rigor to any discussion he's in (the UBR "make the abstraction concrete" comment is the archetype); rare combination of deep intellectual grappling **and** clean articulation — an "intellectual anchor." Strong contributions across Retentive Feedback Loop + UIC.
- **Growth (James's read):** **stretched too thin** across many workstreams → limiting his ability to land deeper technical breakthroughs; plus a **reactive posture** (waits for problems to come to him rather than driving his own agenda). Net effect: **often seems stressed.** Peer-feedback framing encoded this as focus + agenda-setting + a sustainability note — the "stressed" observation was NOT stated (wellbeing read, not rubric-actionable).

## Role in my 6–12 month goals
- **KDD 2026 paper Federation subsection co-author** (with Armando).
- **Active reviewer on the UBR (Unified Cross Surface Retrieval) design doc** — his comment on 2026-04-03 ("can we outline or reference how this will be for different use cases where applicable?") is the classic senior-engineer "make the abstraction concrete" ask.
- **Coupled role:** Olafur's engagement spans both the KDD paper (Retentive Recs Federation section) AND the UPP platform design (UBR architecture review). He is not a peripheral co-author — he is engaged on the actual platform Retentive Recs runs on.

## Current relationship
- **Status:** **Active cross-project collaborator** (upgraded 2026-04-11 same day). Engaged on UBR design review + KDD Federation subsection.
- **Trust level:** Unknown, but engagement level is meaningful. Cross-artifact presence suggests broader investment.

## Operating plan
- **Take his UBR review comment seriously.** "Outline how this will be for different use cases" is a real ask for concreteness — worth addressing in the design doc revision. Route feedback via Piyush/Jiaxing, not directly (they own the doc).
- **Federation subsection coordination on KDD paper stays via Armando.**
- **Probe relationship directly if Olafur surfaces again on a third artifact.** One cross-project engagement is notable; two is a pattern worth investing in.

---

# 26) Jiacong He — Departing (Blending Team, added 2026-04-11)

## Status
- **Leaving Pinterest.** On the **blending team** — minimal impact on James's team retention.
- **Wrote the Pinterest Engineering Blog draft for Retentive Recs.** James inheriting the editor role 2026-04-11.
- **KDD paper Representation subsection co-author** (with Armando). His departure means Representation likely absorbs into Armando.

## Why he matters going forward
- **Inherit his Engineering Blog draft cleanly before his offboarding.** Critical handoff — losing the draft = losing the artifact.
- **Confirm KDD paper Representation absorption with Armando.** Avoid orphan subsection.

---

# 27) Sai — Peer Sr EM (M17), P2P Retrieval (she/her, added 2026-04-11)

## 2026-08-24: "Very close to launch approval" — the P2P v0 decision moves to a Huizhong thread; she hands HF the training-efficiency slot

Full day in the James/Piyush/Matt/Sai group DM (verbatim + reads: `work/projects/upp/upp_retrieval_em.md` 8/24 + addenda). Her posture: cooperative and concrete — "I do not want to delay the launch too much after the approval," a six-item productionization list with owners, "let's time box," Yilin named as P2P counterpart, and the p4de/GPU budget flagged as a leadership call-out (her ask). Tells: the V0-vs-V1 throwaway-work question (she's protecting her team's weeks, not blocking); "Owner: unclear, need to discuss with HF" left open for James to fill — he did, in her doc, with a Wed 8/26 ETA. Decision status at 9:36 PM: "I started a thread today, still waiting for replies from Huizhong… on top of my mind." Escalation record drafted privately (James/Matt/Dylan); nothing said to her. Private read unchanged; nothing today contradicts the good-faith trajectory.

## 2026-07-17: Shared SSJ-side friction intel directly (with Tie)

- Sai + Tie (§47) proactively told James that the Dhruvil-M.O. friction (silo→exec→demand rollouts; Dhruvil chapter 7/17 entry) is hitting their teams too, and that Kurchi is converting it into UPP concerns (Kurchi chapter 7/17 entry). **Candor/alliance signal** — continues the post-OneTrans good-faith trajectory, and sits interestingly alongside the private 小气 read: whatever her turf instincts, she keeps choosing the direct channel with James.
- **Protect as source.** Never let this surface to Dhruvil or up her chain (Huizhong, Kurchi).

## 2026-07-15: Level confirmed + peer-feedback read (private)
- **Level confirmed: M17 Senior EM** (per James, peer-EM altitude with James + Dhruvil).
- **James's public read (peer feedback):** proactive, good-faith cross-org partner — staffed P2P engineers onto UPP unasked, asked to be pulled *into* the weekly sync; strong, well-articulated technical vision for P2P Retrieval.
- **⚠️ James's PRIVATE read (trust perimeter — do NOT surface, do NOT put in any chain-readable artifact):** he thinks Sai can be **too 小气** — petty / turf-protective / small on credit and resourcing (the OneTrans parallel-build is arguably this instinct in the wild). He deliberately did NOT write this into peer feedback because her **entire chain (Huizhong, Kurchi) reads it** and they are **still in a live UPP political situation**. The 小气 read was *encoded* in the feedback only as a positive next-altitude nudge ("operate your vision at broader, org-first scope; champion the shared bet even when credit lands elsewhere") — never named. Keep the raw read here as context, never as content.

## Role in my 6–12 month goals
- **Peer Sr EM on the P2P Retrieval side.** Jiaqing (the P2P Retrieval engineer working closely with Piyush + Zihao on UPP cross-surface training) is one of Sai's reports.
- **Active cross-team partnership on UPP Prong 3 (P2P architectural discussions) + Prong 1 (cross-surface training).** Sai is proactively committing more engineers to the cross-surface effort (new signal 2026-04-11) and has asked James to add them to the weekly coordination meetings.
- **Correction:** Earlier UPP must-win log (March 2026) mistakenly logged Sai as "P2P IC, silent throughout, following Jinfeng's lead." **This was wrong.** Sai is a peer Sr EM, not an IC, and is a positive partner — not a Jinfeng proxy. Corrected in `projects/upp_retrieval.md` appendix 2026-04-11.

## Current relationship
- **Status:** **Positive and accelerating.** Likes Dylan. Likes collaborating with James. Proactively committing resources to UPP cross-surface work without needing to be asked.
- **Trust level:** High (for a cross-org peer). Operating in good faith; actively engaged.
- **What Sai wants:** Strong cross-team collaboration that moves UPP forward. Wants James and Dylan in the loop on her org's work.

## Intel (added 2026-04-11)
- **Has complained privately that Huizhong (P2P Director, Sai's manager) is too controlling and too conservative when it comes to investing in ML.** This is meaningful intel: Sai and Huizhong may have a friction point that James should be aware of when coordinating with both. Sai's frustration is not with UPP — it's with her own chain's ML investment stance. UPP is potentially a path that routes around Huizhong's conservatism via direct engagement with Dylan + James.
- Do NOT surface this intel to Huizhong, Jinfeng, or anyone outside the trust perimeter (Dylan, possibly Rajat if strategically relevant).
- **Karen-style note:** If Sai is frustrated with Huizhong's ML conservatism AND is actively committing to UPP, she may see UPP as the vehicle for the ML work Huizhong won't fund internally. That aligns incentives powerfully — Sai's self-interest and James's UPP success are coupled.

## Operating plan
- **Action this week: Slack DM Sai to acknowledge her proactive engineer commitment.** Don't wait. Short, warm, strategic:
  > "Hey Sai — thanks for staffing more folks on the cross-surface effort. Added them to the weekly sync. Really appreciate how this is coming together. Let me know if you want a quick 15-min sync sometime to share where I see this heading."
- **Continue including her in the weekly coordination meetings** as the default — she asked to be in the loop.
- **Watch for an opportunity to mention her partnership positively to Dylan.** Dylan likes Sai; Sai likes Dylan. Credit-sharing upward is zero-cost and builds the Sai–Dylan–James triangle.
- **Do NOT discuss Huizhong with Sai directly unless she brings it up.** Keep the intel as context, not content. If Sai vents about Huizhong, listen and validate; don't add fuel.
- **Default is let the work speak.** Sai is operating in good faith; don't bring transactional framing into the relationship.

## 2026-05-13: OneTrans surprise + EM-to-EM heads-up protocol established

**The event.** P2P approved a new retrieval architecture (OneTrans — unified transformer tokenization) on Tuesday 5/12. Surfaced to UPP late Tuesday night via Jiaxing's fine-tuning proposal to Piyush. OneTrans had been in development on Sai's team **since early Q1** — in parallel with UPP v0 co-design — and was not disclosed to UPP during months of nominal co-design. Architecturally, OneTrans makes UPP v0's feature-cross layer obsolete and required either a 2-3 week UPP redesign or a skip to v1.

**Behavioral data from the noon 1:1:**
- **Apologized cleanly and unprompted** for the surprise factor. Named specifically: bringing OneTrans to LR approval without an EM-to-EM heads-up was the gap. *"我們 bring to LR 之前其實可以考慮給你們一個 heads up."*
- **Accepted EM-to-EM heads-up before LR approval on coupled work** as the forward protocol. Did not accept blanket "report everything to UPP" expectation — only major coupling decisions before they ship. **This is the right norm; don't push for broader.**
- **Mature peer-EM operator frame:** *"As managers we understand, we can take care of this amongst ourselves."* Doesn't want IC-layer defensive escalation. Primed her PMs (Krystal, Matt) on her side; James primed Piyush on his side.
- **Honored UPP's work:** Recommended including Plan 3 (UPP v0 fine-tuned directly — closest to original UPP proposal) as the prioritized experiment in the joint plan. UPP v0 ships in original form; OneTrans integration runs in parallel as Plans 1/2.
- **Initiated joint half-pager to leadership** as the upward comms artifact. FYI tone, co-authored, no asks. *"我們之間我覺得我們非常有 trust 我覺得你跟我 want the same thing."*

**Cultural read (held lightly, worth tracking):** P2P (Sai's surface) does not want to be positioned as "just downstream of HF/Personalization." OneTrans is in part an identity-defensive move — P2P showcasing its own ML innovation, not just consuming UPP. James acknowledged this drive as legitimate in the 1:1, then pivoted to the peer-EM accountability ask. **Pattern hypothesis: this is not the first time. Watch for similar parallel-innovation moves; the structural fix is repositioning UPP as "shared infra surfaces co-own," not "HF's foundation model."**

**Trust state update:** Still positive net. The asymmetric co-design pattern is now visible but Sai's response to confrontation (clean apology, forward protocol, technical concession on Plan 3 prioritization, joint half-pager initiation) was the highest-grade peer-EM behavior available. Trust did not degrade; it tested and held.

**Roger intel (new, source: Sai noon 1:1):** Roger asked Sai in office hours specifically about UPP collaboration and timing — UPP is being watched at high altitude. Identity TBD (skip-level above Sai? Higher?). **Open input — need to identify Roger before next strategic engagement.**

**Forward operating notes:**
- The EM-to-EM heads-up protocol needs memorialization in `cross_org_operational_model/draft_v3_synthesized.md` as a coupled-design addendum.
- Joint half-pager co-authored post-Thursday joint sync; lands at Jeff/Dylan/Roger altitude.
- Don't bring the Q1-onward asymmetry into the joint sync tomorrow — Sai owned it, forward protocol is the artifact, relitigation hurts.

## 2026-06-03: Parallel-tracks reframe under Kurchi pressure (peer EM leveling honestly)

**Event.** Pre-OOO 1:1 with Sai. Sai told James she's getting **pressure from Kurchi about metrics in the holdout** — limits her bandwidth on UPP cross-surface. She reframed next steps as **parallel tracks**, not true collaboration on the same things. Her framing made it sound like she'd been **"handed a command, not debatable."**

**Sai's notes on her team allocation (verbatim, captured in James's notes):**
- 50% Jiaqing + 30% Suki on UPP (~80% of one FTE total split across two people)
- **P1 for them:** try different Pretrain model variants
- **P2 for them:** try different Finetuning model variants
- **Pretrain → they want to test things out themselves** (Sai's team wants pretraining ownership)
- **P2P FT → James's team runs own models with own code** (Hongtao + maybe Zhihao)

**Tactical next steps James committed to:**
- Sai talks to Jaewon + Jinfeng to align tomorrow
- Piyush sends Dylan a Slack update + asks for time next week
- **Do NOT ask Jiaqing to train certain model variants** (would put her between Sai/Kurchi marching orders and a James-side ask, no-win)
- **Ask for the team:** if good enough offline gain on P2P FT, can Sai's team help run the experiment online? — cleanest collaboration test that keeps the door open without forcing political exposure on Sai's side

**Read on Sai (not Sai's the problem here):** Sai is a peer EM under upstream sponsor pressure who's signaling honestly. *"Handed a command, not debatable"* is Sai leveling peer-to-peer, NOT Sai pulling back from partnership. The 5/13 OneTrans dynamic (clean unprompted apology + EM-to-EM heads-up protocol + technical concession on Plan 3) showed the trust line is real; it stays real here. The pressure is upstream from her (Kurchi → Rajat-non-push cascade — see §6 + §4 6/3 entries). **Pattern hypothesis confirmed:** the 5/13 *"shared infra surfaces co-own"* cultural reframe required Kurchi-and-Rajat air cover that is now structurally absent.

**Roger watcher status (carry-over from 5/13):** Identity still TBD. Re-check post-OOO when UPP architecture conversation reopens.

**James debriefed with Piyush in 1:1 immediately after** — Piyush is read in and will message Dylan.

**Operating implication:** Sai-EM trust posture unchanged. Don't bring transactional framing into the relationship. Reframe collaboration internally as "parallel tracks with controlled handoff at the online-eval boundary" — that's what Sai is offering and it's still cleaner than full decoupling.

---

# 28) Dafang He — Reflex TL + Search CLR Lead (added 2026-04-11, MAJOR UPGRADE 2026-05-31)

> **2026-08-28 — repair owed.** James's own verdict on the 8/25 Reflex call-out + same-hour DM to Dylan: "I came down too hard… the escalation was probably unwarranted." Dafang is OOO (family — Bella's, 🔒 detail). **When he's back: one direct conversation, not Slack, not about Reflex** — went to Dylan fast, should have talked to him first, tell me what you're holding. No mention of the emergency unless he raises it. Relationship bruised, not broken (he defended himself to Dylan — "many people involved" — and went home). Full record: `../projects/reflex/program_state.md` 8/25 + 8/28. **Tim's read (8/25 DM):** worries about Dafang's ability to influence technical direction and people; can't tell if bandwidth / belief / unclear uber-TL role / doesn't know how to make impact / development area — an open diagnosis, not a verdict; Tim also thought the 8/25 call-out "came at a needed time."

## 2026-05-31 scope upgrade — Reflex overall TL

**Per Tim 5/29 convo readout:** Dafang is now the **overall TL for Reflex.** Major operational role — sits at the program-execution layer under Andrew (sponsor) + Tim (PM). James's altitude moves up to architect / sponsor / cross-org orchestrator.

**Active workstreams under Dafang as Reflex TL:**
- **Driving the Reflex System Design** (consensus across the working group)
- **Owning Agent-to-Agent workstream personally** — already in discussion with Keqiang Li
- **Excited about Reinforcement Learning** as a future Reflex direction
- **Coordinating across:** JJ (Build), Bella (Simulate), Matthew Lawhon (Modeling)

Per Tim convo readout: *"Dafang He is excited to drive this as TL."* Real ownership signal, not nominal assignment.

**Implications:**
- **Trust upgrade needed.** Previous "unknown" trust read is stale — he now owns one of James's most strategically important programs. Active relationship-building required.
- **Pinkerton federation conversation will route through him.** Option 2 (A2A delegation) needs to be propagated cleanly. Dafang's instinct may default toward Option 1 (merge under Reflex) for operational simplicity — James needs to anchor him on the federated stance before that debate opens.
- **James's pre-OOO move:** make sure Dafang is set up to run during James's OOO. Direct sync before 6/4 if not already calendared.

---

## Role in my 6–12 month goals (prior scope, still active)
- **Leading the Search-based CLR workstream** under UPP Prong 1. Scoping doc for Search CLR on HF is starting; Dafang is guiding **Devin**, **Sophia**, and a UU team member on this.
- **Earliest stage of a new UPP prong expansion** — Search CLR extends UPP from HF/Notif/P2P into a 4th surface.
- Already commenting on the UBR design doc (Apr 7 — "why device type..." nomenclature question).

## Current relationship
- **Status:** Active — Reflex TL relationship is now load-bearing. Search CLR scoping continues as parallel workstream.
- **Trust level:** Building. The Reflex TL acceptance + visible excitement is a strong signal; James needs to invest now.

## Operating plan (revised 2026-05-31)
- **Reflex partnership cadence.** Set up a working rhythm (weekly?) — Dafang as TL needs architectural alignment with James as architect. The natural sync.
- **Anchor on federated Pinkerton stance early.** Don't let merge-vs-A2A debate open without James having pre-aligned Dafang on Option 2.
- **Pre-OOO handoff.** Before 6/4: explicit "you have the wheel" conversation. Andrew's "I take it from there" presumes Dafang is the operator on the ground.
- **Search CLR continues** — light-touch posture on that workstream still applies.
- **Cross-reference:** `work/projects/reflex/archive/tim_friday_5-29_debrief.md`.

---

# 29) Zihao Chen — Cross-Surface Training Driver (added 2026-04-11)

## Role in my 6–12 month goals
- **Driving UPP Prong 2 (Cross-surface training / CFM unlock for Retrieval)** with support from Piyush Maheshwari, Hongtao Lin, and Jaewon Yang.
- **Cross-surface data loading PR has landed.** Initial model training has started and seems to be working. Zihao is the technical driver on the prong that is currently the most active new build.
- Already active on UBR design doc technical discussions.

## Current relationship
- **Status:** IC engineer, active contributor. James has had operational visibility but not direct relationship building.
- **Trust level:** Building — relationship is mediated through Piyush.

## Operating plan
- **Credit him by name when updating Dylan** (as James did in the Dylan update — "Zihao Chen driving this"). Named-in-updates is the lightweight version of manager recognition.
- **Watch for promo/career signal.** If Zihao is the primary driver on a successful CFM unlock, that's promo material. James should be ready to advocate.
- **Do not over-engage.** Zihao is Piyush's to manage at the technical level; James's altitude is stakeholder + narrative.

---

# 30) Dimitra Tsiaousi — M16 Notif EM / Pinkerton co-lead (added 2026-04-11; upgraded 2026-05-14)

## 2026-07-15: Level + peer-feedback read
- **Level confirmed: M16. Doing well as EM** (James). Protects her team scope, has ambition to push forward on AI + continuous quality.
- **Strengths (James):** (1) solves for the broader **CORE** org over local optimization under tight resourcing — the Pinkerton independent-convergence story (both built compatible v0s, joined into one artifact + one 1-FTE Jeff ask); (2) strong, well-formed **point of view on content quality**. No real growth area observed — peer feedback Q3 kept honest/light (export the convergence model across the org).

## Role in my 6–12 month goals
- **James's counterpart on the Notif side** for the UPP Prong 4 operational handoff (original framing, April 2026). She's seen UPP at the strategic level; previously surfaced the March 2026 must-win comment ("UPP can evolve into the next generation of models").
- **NEW 2026-05-14: Co-lead on Pinkerton** — joint cross-surface DSAT diagnostic tool, James (HF) + Dimitra (Notifs). Both built compatible v0s on opposite surfaces independently and joined them. Going to Jeff for a 5–8 min demo with a 1-FTE ask. Owns the joint naming ("Pinkerton" landed 2026-05-14). Carries Slides 2/3/4/6/7 in the Jeff demo.

## Current relationship
- **Status:** Active peer-EM partner on a Jeff-altitude initiative. Significantly more engaged than the original April handoff posture.
- **Trust level:** Building toward medium — co-building real artifact, co-presenting to VP. The Pinkerton partnership is the upgrade vector.

## Operating plan
- **Pinkerton ops:** dry run with Dimitra + Chuxi before Jeff demo; pre-align the 1-FTE ask with her manager AND Dylan before Jeff hears it; Slide 6 diagram refinement; debrief together after the demo.
- **Joint write-back to her team:** treat Pinkerton wins as joint Notif+HF wins. Don't accidentally HF-flag a cross-surface artifact when crediting upward.
- **UPP Notif handoff (legacy track):** still on the operational handoff track separately. Don't conflate Pinkerton (DSAT diagnostic) with UPP Prong 4 (foundation-model handoff). Different workstreams; same person.
- **Watch for her definition of "clean" on handoffs:** she may have different criteria (QA expectations, metric guarantees, operational readiness) than James assumes. Ask, don't assume.

---

# 31) Zhenyu Tan — Notif ML Manager (added 2026-04-11)

## Role in my 6–12 month goals
- **Manager (likely) on the Notif ML side**, who — alongside Hongtao Lin — confirmed to James that Notif FT is Hongtao's **major Q2 project**. This is a clear ownership signal from a management peer.
- **Potentially the Notif ML team's accountability owner for the UPP handoff.** Dimitra is the strategic counterpart; Zhenyu may be the operational one.

## Current relationship
- **Status:** New stakeholder. Engagement has been through Hongtao so far.
- **Trust level:** Building — the Q2 confirmation is a positive signal.

## Operating plan
- **Confirm Zhenyu's role** (manager vs peer IC) in next session — Leo's reading is "manager" but unconfirmed.
- **If Zhenyu is the manager:** he's the right person to broker the Notif handoff with, alongside Dimitra. Separate from the IC-level ownership conversation with Hongtao.
- **Light touch for now.** Let Hongtao/James's existing channel handle coordination until the handoff gets closer.

---

# 32) Sophia — Search CLR Contributor (added 2026-04-11)

## Role in my 6–12 month goals
- **IC on the Search CLR workstream** under Dafang He's guidance. Part of the team scoping Search CLR on HF as an extension of UPP Prong 1.

## Current relationship
- **Status:** New stakeholder, early-stage workstream.
- **Trust level:** Unknown.

## Operating plan
- **Light touch. Route through Dafang.** James does not need direct engagement with Sophia at this stage.
- **Update this entry when the Search CLR workstream matures.**

---

# 33) Mira Steckel — Senior Director, Design (added 2026-04-11, renumbered from 28)

**Updated 2026-04-30: Channel held for third consecutive day; James led the reply with a cross-team coordination move ahead of the design ack, Mira lit up.** Mira opened 9:08 AM in "other fleeting thoughts" register with two notes: (1) she's asked her team to narrow which use cases show in mocks (frequent switching has been distracting feedback) and invited James to give feedback to the designers on representative use cases; (2) framed it as *"a good way of making sure we're aligning on expectations of outcomes."* James replied 11:34 AM with two messages, leading with the substantive coordination move: *"There's alot of great prompt engineering work from @Jasmine Onyia that we can leverage for LLM based pUIC. I plan to connect her with @Yuke Yan and @Chuxi Wang for some of the next steps."* — followed by the side-note ack: *"Ack on mocks. Will do, thanks so much Mira!"* Mira responded 11:35 AM: *"Love that! Definitely leverage her work as best you can!"* Pattern: leading with cross-team substance (Jasmine → Yuke/Chuxi) ahead of answering Mira's design ask inverted the conventional respond-to-the-ask-first pattern; Mira's "Love that!" + endorsement of the Jasmine connection shows the move landed. Channel now operating across three registers in three days: deep technical co-think (4/28) → artifact-spawn / vision-language gift (4/29) → casual "fleeting thoughts" + cross-team substance (4/30). Working-partnership status no longer provisional.

**Updated 2026-04-29: Working channel produced first artifact-spawn moment within 24h of activation.** Mira followed up at 10:50 AM ("Okay, this is helpful, because when Andrew says he doesn't understand why this would happen, I think he's right for the current state, but if we wanted to show something that's like alpha=2 (which probably isn't a thing, but let's roll with it) those pins might not mean much. This gives me something to chew on that we could try to show from a Pinner perspective from the design team. Thanks for helping me understand."). She mediated Andrew's confusion cleanly ("right for current state, but at alpha=2…"), introduced an alpha=2 thought experiment of her own, and committed Design-team to visualization. James replied 11:41 AM with peer-register retroactive gift on the TikTok/IG framing she'd reached for yesterday: *"Thank you Mira! Glad I can be of help. Btw, I appreciate the Tiktok/IG framing because I agree with you that that is indeed a key anchor for a lot of what we're doing in Anticipation 🙂."* Mira responded 30 min later (12:11 PM): *"yeah, that's what i'm going to ask the designers to visualize. i know it's in our vision, but i want to make it even more prominent how delightful that jump of anticipation could be."* Working channel is now actively spawning Design artifacts sourced from James's framing. New language entering Mira's vision-pitch toolkit: **"delightful jump of anticipation."** Wes-flagged TikTok/IG load-bearing miss from 4/28 closed retroactively via "Btw" peer-register move — gift landed as side-note agreement rather than packaged exec-portable language.

**Updated 2026-04-28: Direct working channel activated. Mira-initiated.** First-ever direct technical exchange. Mira DM'd James with a hand-drawn diagram trying to verify her mental model of how UIC signal works in the Explore module powered by RR. Self-deprecating warm register ("am I a designer or what?"); bypassed the Andrew/Dylan-mediated path. James responded with co-thinking depth — validated her cross-user-pattern-matching model, refined the UIC personalization mechanism, reframed the reference-pin "weirdness" as a Design opportunity (not an Eng problem), surfaced 4 concrete possibilities (semantically representative pins / spell out use-case gamut / VLM+reasoning for thematic similarity / "likely to be understood/clicked"), and linked a parallel copy-text question thread he'd already opened in #anticipation-cupcake. Posture explicitly chosen: collaborative co-think over relay-race handoff. The "let the work create the moment" watchpoint closes; new working channel is open.

## Role in my 6–12 month goals
- **Anticipation Vision co-author.** Mira co-authored the Anticipation Vision (Pinterest's vision for ALL of 2026 personalization) with Andrew Yaroshevsky and Dylan Wang. James + Anna's Retentive Recommendations is the explicitly named technical key under this vision.
- **Cross-functional Design × Engineering × Product play.** Mira is the third leg of the executive triangle on Anticipation. Her involvement is what makes this a *company-wide* vision and not just an Eng+Product play.
- **Indirect, but load-bearing.** She is part of why the CTO is publicly amplifying the Anticipation Vision at conferences.
- **Design DRI on the dogfooding feedback rollup.** Mira's team is listed as DRI on multiple Explore-module UX themes (Reference↔Recommendation connection clarity, Reference Pin cohesion, Frontier Pin landing/header issues). Her 4/28 question was, in part, calibrating which of those land in Design vs Eng — James's reframe placed the reference-pin module explicitly on Design's side.

## Current relationship
- **Status:** **Active — direct working channel established 2026-04-28.** Mira initiated. James responded same-day with substantive co-think + 4 concrete Design options + parallel work-thread link.
- **Trust level:** **Warm-and-curious, early.** First direct exchange landed cleanly. She showed up doing the cognitive work (drew a diagram, made the TikTok/IG analogy independently); he showed up co-thinking, not gatekeeping or status-asserting.
- **What Mira likely wanted from the exchange (multi-variant read):** (1) build her own internal mental model so she can defend the vision she co-signed in exec rooms; (2) calibrate Design's vs Eng's ownership of the dogfooding feedback themes; (3) test whether James is the kind of partner she can route directly to going forward. James's reply served all three.

## Operating plan
- **Treat as live working channel, not VIP-handle-with-care.** She bypassed mediation; honor that by responding with the same directness she initiated with. Don't force a meeting; don't formalize cadence prematurely.
- **Watch the response to the 4 options.** If she engages on substance (e.g., picks one or pushes back), that's a signal the channel will recur. If she thanks-and-closes, it's an episodic touch — still net-positive, but not yet a working partnership. Either is a fine outcome; do not chase.
- **Design × RR working session is the natural next moment** — but only when she or her team surface a substantive Design exploration on the reference-pin reframe. Don't propose it cold.
- **Default still let-the-work-speak.** Same trust topology as Andrew/Dylan/Anna — high-trust co-author circle. Do not bring transactional credit/role conversations into this relationship. (See `feedback_credit_in_trust_relationships.md`.)
- **Director-advocate cultivation candidate (flagged 2026-04-28).** Different lane than Andrew/Kartik/Faisal — Mira's advocacy weight is in calibration rooms where Design's view is invoked + in CTO/conference surface area for the Anticipation Vision. Worth considering as a fourth named target on the Director-advocate list, but explicitly James's call. Do not auto-promote.

---

# 34) Matt Chun — PM, UPP (reports to Andrew; added 2026-04-18)

## Role in my 6–12 month goals
- **UPP PM partner.** Matt is the product lead on UPP, the platform play James co-owns with Darren + Rajat. Direct, sustained stake in UPP's continued political success across Notif, SSJ, and Growth.
- **Andrew's product-side extension.** Reports to Andrew. In the RLHF meeting (2026-04-2x), Matt is one of two PMs Andrew is bringing (Anna + Matt); both are product-lens contributors, not agent builders. Matt's presence means Andrew is grounding Reflex feedback across surfaces, with UPP represented.
- **Bowen-era continuity.** Matt used to work closely with Bowen. That history gives him institutional context James doesn't need to re-explain.

## Current relationship
- **Status:** Strong trust, battle-tested.
- **Trust level:** **High.** Forged through shared political battles — Matt and James have fought UPP escalations against Notif and SSJ together. Shared-adversary bonding is genuine, not performative.
- **Confidence:** High.

## What Matt likely optimizes for
- **UPP's platform success** — structural alignment with James.
- **Clean cross-org execution.** UPP has required heavy political navigation; Matt values partners who can handle the politics without creating more.
- **Product clarity.** As a PM, he'll push for product-legible framing of engineering work. Don't drop him into pure architecture monologues.

## Operating plan
- **Default is peer, not stakeholder-to-manage.** No manufactured cadence. Shoulder-to-shoulder on UPP politics.
- **In the RLHF meeting:** hand him a bridge to UPP explicitly — *"the curator's conflict-resolution logic is cross-surface by design; if UPP patterns need to feed this, the scaffolding is ready."* Costs nothing; signals Matt's surface is welcome and positions curator as UPP-relevant.
- **Pre-share strategy:** not required for this meeting. Strong trust + different surface means no Matthew-guardrail risk.

## Risks
- **None flagged today.** Watch: if UPP's political landscape shifts (Kurchi warming or Shipeng cooling), Matt's read may diverge from James's. Keep the DM line open.

---

# 35) Rahul Goutam — Manager II, Blending (under Dylan; added 2026-04-18, updated 2026-05-23)

**Surname correction 2026-05-23:** Slack confirms surname is **Goutam**, NOT Goldam. Earlier memory had this wrong.

**Level:** **L16 Manager II** (sub-EM altitude). James + Dhruvil are L17 Sr. Manager (peer-EM). Rahul should report through James or Dhruvil under any team-redesign — NOT standalone direct to Dylan. See [[project-team-member-levels]].

## Role in my 6–12 month goals
- **Manager II, Blending team (HF, under Dylan).** Blending sits downstream of HF CG and Ranking — the final stage before the feed. Architecturally adjacent to James's surface and increasingly relevant to cross-surface Reflex patterns.
- **Retentive Recommendations co-sponsor.** Rahul has dedicated his best engineer, **Adreanne**, to Retentive Recs — a concrete resource investment on Anna + James's initiative. Gives him structural skin in the coalition game, not just rhetorical support.
- **2026-07-09: Adreanne nominated IC14 → IC15.** James submitted strong support ("Ready now") — velocity + feedback-loop-project end-to-end story. Draft: `work/people/peer_feedback/h12026/promo_assessments/andreanne_lemay_promo.md`. ⚠ Spelling discrepancy: this file has always said **Adreanne**; James's 7/9 dump opened with "Andreanne Lemay" and the draft uses that — **verify against Workday before submitting, then reconcile whichever is wrong.**
- **RLHF meeting attendee.** Alongside Dhruvil (HF Ranking) and James (HF CG), Rahul represents the third HF-stack surface. His Blending patterns are the natural extension target for the curator's cross-surface conflict-resolution logic.

## Current relationship
- **Status:** Warm, personal history.
- **Trust level:** **High.** James was Rahul's onboarding buddy → relational seniority + warm founding context. Friendly relationship sustained.
- **Confidence:** High.

## What Rahul likely optimizes for (inferred)
- **Team execution** — standard EM concerns for Blending's roadmap.
- **Cross-team collaboration wins** — his willingness to dedicate Adreanne to Retentive Recs signals he values shared initiatives over pure territorial defense.
- **Peer alignment with James** — historical relationship + shared coalition via Anna suggests he's wired to operate as ally, not competitor.

## Operating plan
- **Continue peer-friend default.** No manufactured cadence needed; relationship is stable.
- **In the RLHF meeting:** invite him into the curator/skeptic scaffolding publicly. Suggested line — *"Rahul, the curator's going to need to handle patterns from CG and Blending when they contradict. Can I grab 30 min to stress-test against what you're seeing in Blending?"* Acknowledges his surface, invites contribution without asking him to build agents, frames the scaffolding as cross-surface.
- **Credit Adreanne.** When Retentive Recs comes up, publicly credit the Adreanne contribution. Costs nothing; reinforces Rahul's investment decision and Adreanne's growth signal.
- **Post-meeting follow-through:** actual 30-min sync within 2 weeks. Turns a public moment into real cross-surface collaboration and locks the alignment in.

## Risks
- **Minimal today.** Long-term watch: Blending's role in final-feed attribution can create architectural tensions with CG (whose work gets credit for an engagement lift?). Not active.
- **Name convention:** "Rohu" in voice transcription = **Rahul** in writing. Always use Rahul in written artifacts.

## 2026-07-15: Peer-feedback read
- **Strength (James, genuine praise):** his work on the **interest exploration node in Blending** — a strong technical architecture that unlocked a large line of follow-up experimentation and was a real boon to both **content exploration and user interest exploration**. Built as a foundation others stand on, not a one-off. Second strength: non-territorial collaborator (dedicated his best engineer to Retentive Recs).
- **Growth (James):** couldn't find a real gap. Direction of *more* = extend impact horizontally — wider Homefeed-level ownership + propagate his Blending patterns to other Blending/surface teams.

---

# 36) Tim ⟨surname pending⟩ — Reflex PM (added 2026-05-31)

> **Distinct from [§17 Tim Leung]** (L16, Presentation). Different person, different scope. Cross-link tag to avoid future confusion: this is "Tim (Reflex PM)" or "Tim-Reflex"; §17 is "Tim Leung" or "Tim-Presentation".

**Status:** Skeleton entry. Profile to be filled out after substantive 1:1s. Captured here to lock the distinction from Tim Leung and reserve §36.

**Updated 2026-07-09: Relationship strong — Andrew's ask #1 (PM connect) is closed and healthy.** Per James: they get along really well; James has been helping him substantially across threads. Tim is **also the PM on In-Session Responsiveness** — the project JJ leads on the eng side — so there are two live collaboration surfaces (Reflex + Responsiveness). Explicitly NOT a case for the §9 growth-area work: Tim is ML-adjacent enough and the collaboration already works — he is the *positive exhibit* of James×PM partnership that Andrew can see, not a rehab stage. Keep investing on the merits.

## What's known
- **Role:** PM assigned to Reflex by Andrew Yaroshevsky. **FTE** — Andrew framed it as material escalation (5/27 hallway convo). First PM the Reflex program has had.
- **Charter (confirmed 5/29):** whole-Reflex platform PM. Works alongside Dafang He (overall TL) — Tim = product side, Dafang = technical/operational side.
- **First meeting:** Friday 2026-05-29 — James walked him through the 5-workstream roadmap. **It went well.** Per James: *"Everything went well with the convo. He will run with this."*
- **Roadmap landing read:** Tim engaged at PM altitude and is running with the framing. The 4 technical workstreams held (Build / Simulate / Modeling / A2A); the Foundation layer dissolved into Reflex's goal-setting axes (System Deliverables). See debrief for full delta.

## Goal-setting axes confirmed in convo
- SSv2 & WAU
- System deliverables
- XFN acceleration (PMs / Designers can ship ideas)

## What's NOT known yet (to populate as relationship develops)
- Full name / surname.
- Level / seat (internal transfer vs external hire vs new grad PM).
- Start date / OOO overlap with James.
- DISC-coded read on him as a person.
- Personal working style / preferred cadence.

## Role in James's 6–12 month goals
- **Director-track signal.** Andrew assigning an FTE PM to Reflex is one of the clearest sponsor-validation moments on the substrate-platform thesis. How James onboards Tim is a Director-altitude execution test.
- **Operational shape of Andrew's "funded for my team" ask.** Tim is the PM channel through which the Foundation-layer funding ask runs upstream. Loop closes when foundation workstream gets resourced for James's team.
- **Andrew-channel forwarding agent.** Per 5/27 reasoning, capability-led framing (substrate, user.md) propagates to Andrew through Tim. Pinkerton brand stays out of opening conversations.

## Operating plan (provisional, refine after intel)
- **Build the relationship at platform PM altitude.** Treat him as the PM the platform needed; not a junior assistant, not a participatory canvas. Conviction-led with optionality, per the 5/25 Dylan-model framing.
- **Run the foundation-layer ask through him to Andrew.** Don't go around him. Dylan circle-back happens in parallel (her org gets the resourcing).
- **Capability-led framing on Pinkerton.** Don't introduce the brand; let it ripen organically through working sessions.
- **Pre-OOO sequencing.** James OOO begins ~6/4. Limited window to set Tim up such that Andrew's "I take it from there" actually holds during James's absence.

## Cross-references
- `work/projects/reflex/archive/tim_friday_5-29_roadmap.md` — opening roadmap framing (Fri 5/29 convo)
- `work/projects/reflex/archive/tim_friday_5-29_debrief.md` — post-convo what-actually-emerged (5/31 readout)
- `system/session-logs/2026-05-27.md` — Andrew hallway convo + 3-ask delegation
- §9 Andrew — sponsor channel; assigned Tim
- §28 Dafang He — Reflex overall TL (Tim's operational counterpart)
- §1 Dylan — funding-ask circle-back recipient

# 37) Rahul Sharma — CSI EM, M15 (added 2026-07-09)

> **Distinct from §35 Rahul Goutam** (Blending, under Dylan). This is "Rahul-CSI"; §35 is "Rahul-Blending".

**Status:** Light entry, captured during the H1 peer-feedback cycle. Fill out as collaboration deepens.

## What's known
- **Role:** Junior SWE engineering manager (M15) in CSI; his team's work is upstream of Homefeed. Interaction surface = the CSI/Homefeed operational seam.
- **Promo:** Nominated M15 → M16 this cycle. James submitted assessment 2026-07-09: real partnership/ops positives (stepped up as main POC for the CSI–Homefeed operations meetings when other leads were out), development area = visibly setting the technical bar on his own team (Ngan/DynamicSizer staffing episode), readiness = **"Can't fully assess"** — scoped honestly to James's vantage. Draft: `work/people/peer_feedback/h12026/promo_assessments/rahul_sharma_promo.md`.
- **Working read:** collaborative when engaged, empathetic to customer teams, transparent about constraints; not yet observed operating in a deeply technical context.

## Org intel
- **Reports to a newly joined senior director (name TBD — capture when known).** She is new with little context on Rahul *or* James — which is why the 7/9 feedback was written cold-reader-safe. Relevant beyond Rahul: she is a new senior leader over CSI, an org James's team depends on daily. Worth a deliberate intro touchpoint at some point.

## Cross-references
- §26/§27-era CSI context: Kent Jiang (CSI Sr EM nominee, unity) — see `self/writing_style/peer_feedback_examples.md` for James's prior promo feedback on him.
- `work/people/peer_feedback/h12026/promo_assessments/rahul_sharma_promo.md`

# 38) Michael Weissinger — PM Director (started Mon 2026-07-13; surname confirmed 2026-07-20)

**Status:** Added 2026-07-09, ahead of his start date. Fill out once he lands.

## What's known
- **Role:** PM Director managing the non-recsys full-stack PMs (population likely includes Lily Li §21; exact chain + roster to confirm once announced org chart lands).
- **History with James:** Worked closely together at Snap for years — Michael was the recsys PM lead there. James cultivated the relationship on LinkedIn ~4 years. Before Michael decided to interview, they caught up about the possibility; during the loop Michael came to James for advice on whether to join, and thanked him for it.
- **The recruiting-win thread:** This is the "Michael close" Dylan flagged confidentially pre-OOO ("keep to yourself... maybe Andrew told you"), with James's contribution named as a pre-trip gift. Yan has also mentioned him to James (7/9) — Dylan↔Yan channel active on the hire. Confidentiality moot as of his 7/13 start.
- **Profile note:** ML-fluent PM leadership (recsys PM lead pedigree) being placed over the *non-recsys* PM population — the org is investing in the eng↔PM translation gap from the PM side, the mirror image of what Andrew's 7/9 feedback (§9) asks of James from the eng side.

## Role in James's 6–12 month goals
- **Warm senior channel into the PM org** — benefit-of-the-doubt credit, org-level context-setting ally, and a manager who knows how to work with James at speed.
- **Raises the ceiling on the §9 growth area without excusing James from it.** Andrew will be watching whether *James* changes, not whether Michael smooths things.

## Operating plan
- **Warm welcome note in his welcome email** (James, week of 7/13). Right register: peer-warm, no agenda.
- **Spend the friendship capital on org alignment only** — shared roadmap context, translation, priorities. Never on adjudicating James's personal PM friction (Lily especially — see §21).
- **Let him form his own reads.** During his onboarding rounds, James showing up warm and collaborative with PMs in rooms Michael sees is worth more than any framing delivered directly. Visible capture ("their new boss is James's guy") would deepen the Lily/Akshanta dynamic under a layer of politeness.

## Cross-references
- §9 Andrew — his feedback names the interface Michael now manages from the other side
- §21 Lily Li / §20 Akshanta — likely or possible reports; capture-risk population
- `work/people/dylan_archive.md` — the confidential "Michael close" flag (pre-OOO)

## 2026-07-20: First live working meeting — SM/SL staffing sync

Week 2 on the job. Attended the SM/SL sync (§9 2026-07-20 entry) and watched James receive a joint "thank you for your ownership" from Andrew + Lily. A strong first exhibit on exactly the eng↔PM interface he was hired to manage from the PM side — no capital spent, formed his own read from the room (per the operating plan above).

## 2026-08-14: Safe Journeys — Michael pulls James into the teen-safety program

**Michael is the PM across all five Safe Journeys workstreams** and co-authored the ACP vision with Faisal, Dylan, and Andrew Y. He owns the execution doc (*Safe Journeys Milestones & Timeline*, last updated 8/14) and **is asking James directly for opinion + ETAs** — every Milestones/Timelines field in it is TBD. Filed: `work/projects/safe_journeys/sources/03_`.

**He named James first among the Eng POCs on two workstreams** — *Safety First Ranking* and *In-Session Awareness* (alongside Qinglong §50, Dhruvil, Zisis Petrou). This is the first substantive James↔Michael working thread at Pinterest, and it rests on **Snap history**: Michael was the recsys PM lead there, and he and James shipped the suggestive-content spacing work together — the closest analogue to the teen slate problem. That shared case is the strongest thing James can lead with in the joint room, because it arrives as experience rather than critique.

**He is the channel to the CTO comment thread.** Madrigal's two comments on §3 of the vision landed 8/12; Michael answered the surface question with **~50% RP / ~25% Homefeed / ~24% board ideas** — a number that quietly breaks the doc's own "starting with Homefeed" scoping.

**Handle privately, not in the joint room:** the headline **7× spiral statistic** (after a teen taps 1 unsafe slate, USR goes 0.45% → 3.2%) **conditions on a tap** — that is selection, not causation. Combined with an uncalibrated GPT-5 judge at n=2K and no holdout, it is a credibility risk under the whole program if the CTO mandate rests on it. Michael conversation, one-on-one.

## 2026-08-2x: The Andrew debrief DM — sequencing call delivered, Michael takes the plan (filed 8/24)

After James asked him for "next steps on a joint prioritization," Michael came back with Andrew's sequencing (GenAI first for CQ-aware ranking · Racy pod rollout, borrow for self-harm short-term · self-harm rides the long-term solution), named **UICs the top Anticipation resourcing priority**, and offered to **drive the Safe Journeys plan himself** (Andrew/Dylan/Faisal by Friday → VJD → Bill later; code red pushed Bill reviews) with James as input. Asked whether to reach out to **Andrey Gusev** for Faisal resources beyond Qinglong. Verbatim + read: `work/projects/safe_journeys/sources/08_michael_andrew_debrief_sequencing.md`. Pattern: he is operating exactly as the operating plan hoped — org-alignment channel, no capital spent, asks James before moving on people.

## 2026-08-21: First joint fire — the Neeti T&S DSAT investigation (bonded)

Worked the "Elon scam pins" DSAT with James + Dhruvil in a 3-person DM, same-day on Andrew's EOD ask (**Neeti Deshmukh = VP of T&S, reports into the Chief Legal Officer** — it was *her* test account; **Becky Stoneman = Dir of Product**, thread initiator). Division of labor: James ran the Pinkerton full-funnel investigation; **Michael wrote the response message, asked the sharpening questions, and added next-step suggestions** — his "did she take positive actions on the Elon pins?" question surfaced the key confounder (she deliberately searches out + engages scam content to probe "spiral" scenarios — his word, from the Snap suggestive-content playbook). James: "we bonded." Also notable: **Michael independently uses Claude Code** (built P13n ranking documentation with it a couple weeks in; caught that there's no report head in L2, correcting one of James's agents) — the AI-native peer signal, same species as James's differentiator. The Snap-history bet (§ 8/14: lead with shared experience, not critique) is paying out in working form, three weeks ahead of the relationship plan.

---

# 39) Matt Madrigal — CTO (added 2026-07-13)

## What's known
- **Amplifies the Anticipation Vision externally** — talks about it at conferences after Andrew pitched it to him (see canonical brief; the Andrew → Madrigal chain is the vision's exec altitude ceiling).
- **2026-07 (Ads Retrieval discussion, James present): particularly interested in GPU retrieval — "bread and butter for Meta" (his phrase).** First direct signal of CTO-level interest in a specific retrieval capability, in an Ads context.

## Why it matters
- **CTO pull for a capability James's team already shipped:** CLR GPU serving is done and in production — Notif adopting, P2P already adopted, strong offline results (see `upp_retrieval_em.md` April 2026 status, Prong 1). When the CTO benchmarks GPU retrieval as industry table stakes, James's org is the one at Pinterest that built it.
- **Ads expansion framing upgrade:** Ads onboarding onto UPP rides GPU retrieval infrastructure that already exists — demand-side pull (Ads asking) + top-down pull (CTO interest) converging on the same platform.
- **Verbatim hook:** "bread and butter" — echo his own framing when GPU retrieval comes up at exec altitude (same technique as Jeff's "persona perspective").

## 2026-07-13 update — ELT meeting: detail-level intent×UPP question
- At the ELT (UPP expansion, same day): asked **"how can we leverage user intent clusters as part of UPP — at a detail level, what's the interplay between user intent modeling and UPP?"** CTO engaging on mechanism. Two James-coded programs (Anticipation substrate + UPP platform) connected at CTO altitude in one question.
- Follow-up play: 1-pager on the interplay (conditional retrieval socket → latent intent in FM → predicted intent/pUIC as the anticipation unlock) — Madrigal retells mechanisms externally; Jeff forwards 1-pagers.

## 2026-07-22 update — ads is the lever into Jeff
- Per Dylan (§1 Dylan 7/22 coaching point; §5 Jeff 7/22): **Madrigal's priorities center on ads, and that is how you motivate Jeff** (his boss). Collaboration-with-ads = Jeff's incentive. Reinforces the existing Ads×UPP thread (§40 Dinesh, §41 Jiajing, GPU-retrieval interest above) — the CTO's ads focus is now a *named motivational lever*, not just a demand signal. Jeff pointed Andrena (Dir TPM, §48) at the ads-collaboration area.

## 2026-08-12 — commented on the Safe Journeys vision doc, on the pillar James is a POC on

Two margin comments on **§3 In-session Awareness** of the ACP Safe Journeys vision (captured from a screenshot 8/14; they did not export to PDF — filed in `work/projects/safe_journeys/sources/01_`):

1. **10:19 AM — "Let's tie this back to Anticipation as well."** Anchored on the §3 header. **This is a CTO instruction pointing into James's own territory**: Anticipation Foundations is his Director-shaped scope claim, and his team owns the substrate. It is also the third distinct Madrigal touch on James-coded work (GPU retrieval 7/13 → intent×UPP interplay 7/13 → Anticipation×safety 8/12), and the first that arrives as a *directive* rather than a question.
   The technical substance is real, not narrative: **in-session awareness and anticipation are the same machinery aimed at different objectives** — anticipation predicts the user's next want, spiral detection predicts the next harm. Same user-state representation, same sequence model, same cross-surface trajectory object. Nobody else on the POC list can say that sentence about a system they own.
   **Whoever writes the tie-back paragraph owns the connection.** Andrew Y co-authored *both* the Anticipation Vision and this doc and can write it just as easily. Flagged to James 8/14 as the highest value-per-minute move available.
2. **10:13 AM — "Homefeed only or all surfaces (RP, Search)?"** Michael answered: ~50% RP, ~25% Homefeed, ~24% board ideas. The CTO's question plus that answer is the argument for a **shared-backbone (CFM/UPP)** approach over surface-by-surface enforcement — i.e. for pulling CQ's own Phase 2 forward.

**Pattern worth naming:** Madrigal engages on *mechanism* (GPU retrieval, intent clusters, now cross-surface spiral machinery), not on summary. Artifacts written at mechanism altitude are the currency — he retells mechanisms externally.

## Open
- No direct James ↔ Madrigal relationship yet — group discussions and doc comments so far. Watch for whether the GPU retrieval + intent-modeling + Anticipation×safety interest turns into asks routed through Rajat/Jeff.
- Whether other sections of the Safe Journeys vision carry Madrigal comments — only the §3 margin was captured.

---

# 40) Dinesh Govindaraj — Sr. Manager, Machine Learning Engineering, Ads (added 2026-07-13; surname+title confirmed 2026-07-19)

## What's known
- **Very friendly with ATG collaborations** — track record of working well with the central ML org.
- **Jiajing (ATG Sr. Director — see §41) has been asking James to go talk to him** (2026-07); Dylan has also approved the reach-out. Warm intro path exists.
- Sits on the Ads side of the **Ads Retrieval expansion** thread — the same space where Matt Madrigal (§39) signaled GPU retrieval interest.
- **2026-07-19 (pre-outreach intel, via James):** his team is actively working on **CG unification** on the Ads side (the space James's team spent the past year in via UPP); **potentially working on UPP** itself; and **one of his engineers is actively working with Reflex from the Ads side** — three live collaboration hooks. Team name unresolved (dictation garble, "NetJizz"-like; get the real name in the first conversation). Title confirmed from his Slack profile.
- **2026-07-19: intro Slack DM drafted** (Leo-assisted, James's opener kept): P13N CG/Retrieval intro, Jiajing roadmap hook, three them-first threads (their CG unification + UPP-if-on-radar + their Reflex engineer), 30-min ask. Deliberately did NOT use the new org name (rename ask to Dylan unsent at draft time).

## Why it matters
- **First concrete relationship move of the Ads expansion.** Everything else on Ads is demand-signal at a distance; Dinesh is a named, reachable owner.
- **The broker is the signal:** ATG's *senior leadership* is routing the Ads retrieval opportunity through James. Jiajing could point Dinesh anywhere — ranking side, internal ATG — and is pointing him at James. That's central-ML endorsement of James/UPP as the retrieval-platform counterpart for Ads.
- **Natural triangle:** James + Dinesh + ATG (Jaewon's org, Jiajing above) — Dinesh's ATG-friendliness means the collaboration idiom he already trusts is the one UPP uses.

## 2026-07-25 update — 1:1 landed; he's FUNDING Reflex, considering funding UPP in Q4
- **The 1:1 happened and landed well** (James, 7/25 dump).
- **Dinesh is funding Reflex** from the Ads side, and is **considering funding UPP in Q4** — the relationship has jumped from intro to money in under a week.
- **Agreed direction: cross-team deep-dive sessions** engaging both teams with one another going forward.
- **Q3 operating plan (ratified tier: see Q3 plan, 2026-07-25 session):** Tier-1 relationship lane in the UPP-air-cover shape — named session owners per side (Piyush for UPP-side, Dafang/JJ for Reflex-side; James curates, attends the first, then reads outcomes), a standing ~monthly Dinesh 1:1, and one Q3 exit artifact: a **"what UPP does for Ads Retrieval" one-pager by mid/late September** that Dinesh can carry into his Q4 planning — the deliverable that converts sessions into the funding decision. Each milestone here also feeds the Dylan/Jeff ads-collaboration narrative (P2P proof point, Madrigal lever, Andrena's TPM lane).
- ⚠️ **Name disambiguation:** **Jiajing (ATG Sr. Director) is NOT Jiaxing Qu (P2P Retrieval engineer, Sai's team).** Near-collision; conflated once in-session 2026-07-13 and corrected by James. Distinct people, different orgs.

## Open
- Surname, org chain (under whom on the Ads side?), and what Dinesh actually wants from retrieval — fill after first conversation.

---

# 41) Jiajing — Sr. Director, ATG (added 2026-07-13)

**Updated 2026-08-27: ATG's PM team moves under Andrew Y (§9)** — announcement cites "a longer-term vision for ATG with Chuck" (Chuck Rosenberg, VP Eng). Jiajing's eng chain unchanged as far as the excerpt shows; the product side of everything ATG does with James (pUIC/Zelun, GenRet, Simulate staffing, the Ads×UPP thread Jiajing brokered) now routes through James's own sponsor. Open: does "with Chuck" mean ATG eng re-parents to Chuck? Ask Jiajing in the next natural touch, not as a probe.

## What's known
- **Sr. Director in ATG** (central ML org — Jaewon/Hongtao/Matt Lawhon's world; exact reporting lines unconfirmed).
- **Actively brokering James ↔ Dinesh (Ads Sr. EM, §40):** has been asking James to go talk to Dinesh re: Ads collaboration (2026-07). **2026-07-19: converted to action — intro DM drafted (Dylan-approved), Jiajing named as the hook ("Jiajing shared some of the roadmaps your team has been charting").**
- **2026-07-30 — planned calibration ask:** he was present in the ATG sync where James third-degreed RecGPT progress (the sync Bella cited in her "too insecure about RecGPT" feedback, 7/27 1:1). James plans to ask Jiajing for an honest read on whether his probing style over-rotates in those settings. Frame it as "how did my questions land" — do not reference Bella's feedback. Doubles as a relationship-building touch on an already-warm lane (he's been asking James to talk).

## Why it matters
- **ATG senior leadership is routing the Ads retrieval opportunity through James.** Jiajing could point Dinesh at the ranking side or keep it ATG-internal; pointing him at James is a central-ML endorsement of James/UPP as the retrieval-platform counterpart for Ads — a Director-altitude third-party signal in the same class as Yan-alignment (Dylan reads peer/senior endorsement as operating signal).
- Converges with §39 (Madrigal GPU-retrieval interest) and the Ads demand signal — three independent pulls on the same thread.

## Open
- Surname, exact role/chain in ATG, relationship to Jaewon, what Jiajing wants out of the Ads×UPP connection (visibility? ATG resourcing story?) — fill after the Dinesh conversation.
- ⚠️ **Not to be confused with Jiaxing Qu** (P2P Retrieval engineer, Sai's team) — near-collision corrected 2026-07-13.

---

# 42) Karim Wahba — M16 Data Science Manager, PADS (added 2026-07-15)

**Level:** M16 Data Science Manager. Leads PADS (Pinterest Analytics / Data Science). Direct to Dylan's world via the analytics org (chain TBD). Dylan flagged him as a PINvestigator distribution target back in April 2026.

## Role in my 6–12 month goals
- **Cross-functional DS partner.** His team supports **Retentive Recs, Anticipation Strategies, and Reflex** — three of James's core workstreams. Data-science counterpart on measurement/analytics for the retrieval + anticipation surfaces.
- **PINvestigator connection:** Dylan proactively suggested sharing PINvestigator with Karim / PADS (2026-04-01) and had already met with him by that afternoon — organic distribution channel for James's tooling into the analytics org.

## Current relationship
- **Status:** Warm — James's own words: "a real pal." Genuinely friendly, low-friction partner.
- **Trust level:** High / collaborative.

## Operating profile (from James's 2026-07-15 peer-feedback read)
- **Strengths:** (1) Trust + judgment on leverage — trusts his team to deliver, very intentional about *when* to step in vs. stay out. (2) Excellent cross-functional partner — champions shared causes, flexible with both PM and Eng (meets each function on its terms), advocates for the right outcome over local interest. (3) Asks genuinely great clarifying questions that cut to the real problem and sharpen alignment before a group commits.
- **Growth (James's read):** His team owns an unusually broad set of areas; the opportunity is to more explicitly articulate the **common seams / connective thread** across all of it so partners can reason about his team's work as a unified strategy rather than individually strong efforts. A breadth-of-scope / narrative-coherence note, not a deficit.

## Open
- Exact reporting chain (who Karim reports to in the DS/analytics org).
- Concrete anecdotes to ground the peer-feedback strengths (James's input was trait-level; two `[Anchor:]` slots still open in `work/people/peer_feedback/h12026/peer_feedback_2026H1.md`).

---

# 43) Yingjian (YJ) ⟨surname pending⟩ — M16 SWE EM, User Understanding (added 2026-07-17)

**Level:** M16 SWE EM. **Tenure: <6 months** (joined ~Feb 2026). Likely in Hongbo's UU org (chain unconfirmed). ICs named: **Simin, Raymond, Sufyan**.

## What's known (from James's 2026-07-16 peer-feedback read)
- **His team built the UIC clustering mechanisms** that Retentive Recs depends on. Worked with James on Retentive Recommendations, UIC, PinnerSpark.
- **Strengths:** extremely detail oriented; ramped to deep component understanding in under 6 months; connects disparate workstreams (UIC, PinnerSpark) via common foundational backbones. Runs a deliberate delegation structure — gives Simin/Raymond/Sufyan room to make technical decisions and drive design discussions while pushing their thinking with deep questions.
- **Growth (James's read):** articulate a common vision for the team + success metrics beyond customer success metrics; connect the infrastructure to agility on top-line goals. Dovetails with James's Hongbo feedback (UU needs more vision-carriers).

## Open
- Surname, exact chain (Hongbo?), which Raymond this is (NOT assumed to be the Raymond on Tim's team).

---

# 44) Van Lam — M16 EM, Core Retrieval Infra (added 2026-07-17)

**Level:** M16 EM, CRI (manas indexing / cluster-swap side). **Bowen Zhou (§45) reports to him.** New Sr. Manager above: **Tao (she/her)** — much more reasonable than the prior manager; things have turned around under her direction. **Going for M17 this cycle; James's private read: not close.**

## History — H2 2025 friction (documented)
- CRI provided very little infra support; HF left to fend for itself on indexing pipeline stability. James escalated to Van's then-manager after repeated attempts to get Van to engage; the written problem statement named **lack of ownership mentality (Van, Bowen Zhou)** over pipeline stability, plus missing cross-team debugging/tooling investment. Structural context: tightly coupled pipeline halves (manas doc generation = HF-owned; doc→cluster swap = CRI-owned); alerts ambiguous across the boundary.
- The then-manager was also hard to work with; the reorg under Tao is the reset.

## 2026-07-17 peer-feedback approach (James's call: honest minimal)
- Cycle feedback written short and carefully attributed: improvements credited to "the team's recent direction" (reads as endorsing Tao), outreach credited to his engineers, explicit limited-vantage line (James's collaboration is mostly with the engineers, not Van). Growth = invitation to more direct EM-to-EM engagement on shared operational health — the historical failure, framed entirely forward. Goal: no friction with Tao, nothing attackable, committee still hears the calibration.

---

# 45) Bowen Zhou — IC16 Staff Engineer, Core Retrieval Infra (added 2026-07-17)

**Level:** IC16 Staff, CRI; reports to Van Lam (§44). **Going for IC17 this cycle; James's read: not close, but genuinely improving.** ⚠ Distinct from the blending-team Bowen who departed 2026-03-26. Surname confirmed **Zhou** (James dictated "Zou" 2026-07-16; corrected).

## Arc
- **H2 2025:** named alongside Van in James's escalation — little customer empathy ("as a staff engineer on a platform team, he didn't give a shit about the customer applications" — James's words, private).
- **2026 under Tao:** real turnaround. Proactively reaching out to ensure HF↔CRI collaboration works; helping on stability issues unprompted, including failures closer to HF's half of the pipeline. James considers this clear and good.
- **Peer feedback (2026-07-17):** trajectory-positive, no IC17-readiness endorsement — growth framed as "keep extending what he has started" (customer ownership systematic, cross-team debuggability tooling).

---

# 46) Krystal Benitez — TPM, UPP + Anticipation (added 2026-07-17; surname confirmed 2026-08-25)

**Role:** James's TPM on UPP. **Up for promotion this cycle** (level pending). ⚠ Spelling: **Krystal** with a K (repo-consistent; James's dictation homophone "Crystal" corrected via his own Slack screenshot context).

## James's read (2026-07-16, ad-hoc promo-support feedback — full text in `peer_feedback/h12026/peer_feedback_2026H1.md` §7)
- "One of the best TPMs I've ever worked with; I would vouch for her anywhere." Constantly on top of things; drives accountability and process follow-through; coordinates multiple workstreams with grace under pressure. Articulate pushback on unreasonable asks from leadership and XFN while keeping relationships intact. Unusually in tune with how the room is feeling; presents an unbiased view so groups align faster (no perceived agenda → her framing becomes the shared framing).
- **Track record in repo:** OneTrans crisis coordination (5/13); with Zihao "owned the room" when James missed the Wednesday UPP meeting; the "let's see if we don't re-litigate next week" read (politically sharp — kept out of the written feedback).
- **Technical competency:** solid; follows architecture-level discussion, represents technical state to leadership without a translator. Growth (soft, future-framed): deepen foundational technical knowledge to bridge workstreams more creatively as her influence expands.

---

- **2026-08-25:** Surname **Benitez** (Slack). She is also the TPM voice on **Anticipation/pUIC** — answered Andrew's "pUIC is the main bet" note for the team (§9 2026-08-25: iterations in flight, per-method confidence, standardized hop definition, double-down/defund call coming) and tracks Explore-variant dogfooding (OTA path, execution sync). cc'd on the UPP v0 P2P launch approval (`work/projects/upp/upp_retrieval_em.md` 8/25).

# 47) Tie ⟨surname pending⟩ — EM, P2P Ranking (Kurchi's SSJ org; added 2026-07-17)

**Role:** EM on Ranking for P2P, inside Kurchi's SSJ org (adjacent to Sai's P2P Retrieval).

**First recorded direct contact (2026-07-17):** together with Sai, told James directly that Dhruvil's teams' silo→exec→demand rollout pattern (Dhruvil chapter 7/17 entry) frustrates their teams too, and that Kurchi is raising UPP concerns citing this feedback (Kurchi chapter 7/17 entry). 1-hop intel, two independent voices.

**⚠️ Protected source** — never surface to Dhruvil or up Kurchi's chain that this came from Sai/Tie. Trust perimeter matches the other Kurchi-side intel: Dylan only, abstracted form only.

**Open:** surname, level, exact team boundary vs. Sai's retrieval org.

---

# 48) Andrena ⟨surname pending⟩ — Director, TPM (added 2026-07-22)

**Role:** Director of TPM. Surfaced 2026-07-22 when **Jeff pointed her at the ads-collaboration area** in immediate response to Dylan's "collaboration matters more when we go to ads" framing (see §5 Jeff 7/22 + §1 Dylan 7/22).

**Why it matters:** She's the TPM leadership now leaning into cross-org / ads collaboration — the exact space where James's UPP-retrieval-in-P2P launch candidate is positioned as the proof point Dylan wants to "push things forward." Likely a process/coordination ally (or gatekeeper) for the ads-collaboration narrative Jeff is being motivated by.

**Open:** surname, exact reporting line, scope of her TPM remit, and whether her involvement helps or adds process to the UPP×ads push.

---

# 49) Sen Yang — IC18 ML Engineer, Growth (under Shipeng §15; added 2026-07-25, surname confirmed same day)

**Role:** IC18 MLE in Growth (reports into Shipeng Yu's org). Surfaced as a lead in the NLFU push (`work/projects/nlfu_support_2026.md`) — member of `#p13n-growth-nlfu-leads`.

**History with James (deep):** Peers at **Snap** — same director, worked side-by-side on the same projects for close to a year, with a real competitive undercurrent ("in some ways we were competing"). "A lot of history." Sen landed at Pinterest with an **IC18 offer** while James joined at **M17** — James names "a little bit of competitiveness from my side."

**The reciprocity read (James, 7/25):** *"Whether or not Sen helps me depends heavily on whether or not I decide to help him here."* This is a two-way trade, not a favor bank James can draw on cold.

**Live threads:**
- **NLFU:** Sen is James's preferred connect for grounding the ML side (James's read: Brian Lee doesn't understand the ML side). But Sen is **stretched very thin** — deeper involvement means **funding his area more**.
- **AI tooling:** Sen offered that his team could help on AI tooling — dovetails with inbound Reflex/GenAI-tooling interest (see Reflex 7/25 program state).
- **Piyush IC17 promo:** Sen's year-end **peer feedback** would strengthen Piyush's case — a concrete reason to invest in this relationship in Q3.

**Open:** surname; exact team/charter under Shipeng; what "helping Sen here" concretely costs (headcount? funding? James's time?).

---

# 50) Qinglong Zeng — Sr. EM, Content Quality (reports to Faisal Farooq §14; added 2026-08-14)

**Role:** Senior EM on the **Content Quality** team, in **Faisal's** org. Owns the CQ signal stack and the `pin_selection` gate layer (9+ live experiments, DQv4 shipped, Pin Selection V2 with 33-country/25-language granularity — see `work/projects/reflex/pinkerton/quality_patterns.md`). Author of *Integrating Quality/Safety Objectives into the Recommendation System — Design Options* (filed: `work/projects/safe_journeys/sources/04_cq_design_options_qinglong.md`).

**First contact (2026-07-27, GenAI WG):** surfaced in `#genai-feed-wg` as a new contact; posted a prioritization stack that **aligned with James's frame** — strong +1 on multi-layer-not-filtering-only and one shared metric stack. His speed-to-value order: (P0) demote GenAI slop for all users · (P0) demote GenAI for opt-out/low-affinity users · (P1) GenAI spacing · (P2) training-data cleaning. He added Jianing Sun to the WG. Detail in §14 (7/27).

**The friction (2026-08, undocumented):** James: *"We got into it a little bit at a previous meeting."* **No record of what happened — asked twice in the 8/14c session, not supplied.** This is the gap to close before Monday.

**The structural tension (Leo read, 8/14):** his design-options doc argues **"CQ's preference is L2"** for both the utility change and the ranking-loss change, which demotes **L1 Utility — James's team's system** (JJ/Rui owners) to "an optional complementary density lever." Simultaneously its **Phase 2 puts the quality objective into the CFM/UPP pretrain backbone** — also James's — on CQ's sequencing, gated behind a CQ-run Phase 1 on notif/search. Net: enforcement moves *out of* James's L1 and *into* James's UPP, with CQ holding the definition and the timeline. His L1-gets-washed-out argument is **technically sound and not bad-faith** — it is the real objection and should be engaged on the merits.
Note also: **Faisal's own Teen-Aware doc out-scopes CQ's current teen work** ("short-term contextualized threshold changes for teens being driven by Content Quality" = Out of Scope). Part of the friction predates James.

**Outcome (2026-08-17 — the Monday 1:1 landed, play worked):** Qinglong was **quite excited** by the ideas James brought; the **start-with-common-needs framing** validated in the room. He **agreed to partner on the doc** — James writes the draft and **sends it to him by Wed 8/19**, then they iterate together. The co-authorship play is now ratified-by-outcome; the cordiality reset and the joint-artifact conversion happened in one stroke. ⚠️ Circulation-safety note still applies to the Wednesday send: `placement_doctrine_v2.md` is not circulation-safe as-is — cut §7 + internal blockquotes (§3, §5.4) first.

**Same evening — the partnership went public and the stakes jumped (Safe Journeys WG thread, 8/17 ~7:21 PM):** James posted in Michael Weissinger's workstream thread: *"In my 1:1 with @Qinglong Zeng we discussed putting together a framework around safety/quality levers that can be applied to topics 2 and 3 in your doc. Happy to take first stab at this with Qinglong and bring to this group."* Michael: "Awesome." **New timeline, CEO-grade:** Michael wants a reviewable draft **by Fri 8/21 / Mon 8/24 for Dylan + Andrew feedback**, folding into **a deliverable to Bill [Ready] by Wed 8/26**, with Andrew getting time on Bill's calendar **Fri 8/28**. The co-authored doctrine now feeds a CEO review — the Wednesday draft is on the critical path. Thread also: Dhruvil suggested looping **Dafang He** for topic 2 (ranking/blending) — James credited prior alignment and welcomed him (Dafang added to channel); James routed **topic 4 (cold start / quality corpus) to the Activation team** (Brian Lee, Paula Chuchro, Brian Zhou) rather than claiming it for P13N; Qinglong followed up pointing Michael to **Stephanie Chen ⟨CQ, new name — ran a "finding the good" (high-quality content) brainstorm, has user-research results⟩**. **Qinglong reacted (+1/"yes!") to James's partnership message itself** and then showed up in-thread building on the shared frame (the Stephanie pointer) — public co-sign of the co-authorship within hours of the 1:1. The partnership is working in public.

**Operating plan** *(pre-1:1; the co-authorship move landed 8/17 — see Outcome above)*:
- **Monday 1:1 = cordiality reset.** The move Leo recommended (unratified): **offer co-authorship** of the placement doctrine that sits *above* his options doc. Converts a potential rebuttal into a joint artifact and solves the repair in the same stroke. James stays first author.
- **Do not fight L1-vs-L2.** It is a turf fight on the 25% surface (Homefeed); RP is ~50% and CQ already has a shipped L2 demotion win there.
- **Concede the corpus layer to him generously** — `pin_selection` is correctly placed as the earliest filter; it needs a teen-specific threshold policy, not relocation.
- **Points of genuine agreement to hand him:** his loss reweighting and James's `(1−q)·E` are one mechanism at two stages; his "engagement-only ranker is structurally biased" motivation is exactly right.

**2026-08-18 — the draft exists; his 1:1 notes revealed movement:** James ran the doc build (grill → nine decisions → `joint_framework_v1.md` drafted + trade-off scaffolding, sent to James for review; full record `work/projects/safe_journeys/joint_doc_plan.md`). Qinglong's own 1:1 notes (filed: `sources/05_qinglong_1x1_2026-08-17.md`) show **he has already softened from "CQ's preference is L2" to proposing "L2 & L1 soft penalty demotions"** — L1 is in his own proposal now — and he independently wants **standardized signal calibration** (James's Ask 1 landed as his want) and has **initiated quality-aware-UPP discussion with that team**. The doc hands him three co-author entry points (`[QZ]` slots): the P0 signal pick, Galaxy calibration dates, the external publication he offered to share. Watch Wednesday: whether he fills the slots (real co-authorship) or only comments (adoption posture).

**2026-08-19 (~11 PM Slack DM) — Wednesday send landed; reception warm and *specific*; circulation expanding on schedule (from James's screenshot, 8/20):**
- **His words:** "really appreciate you taking the time to write this up. It expands my original doc with a lot more technical depth/details, and it was genuinely a pleasure to read." Named alignment points — **score calibration, the L1-vs-L2 framing for demotion, the additive-vs-multiplicative demotion trade-offs, the pass-through and iteration-cost implications** ("made the choices a lot clearer"). ⚠️ Note the named list: **L1-vs-L2 — the exact issue they clashed on hard in front of team members — is now on *his* aligned list, in James's framing.** Territory won by document, cordiality reset complete.
- **Training-time section (the doc's biggest bet — D3 density head) not yet engaged:** he noticed James live-editing it at ~11 PM ("just added more content to the training-time levers section") and committed to a proper read **8/20** + thoughts. His reaction to the head push, and whether he fills the `[QZ]` slots, is still the open co-authorship test.
- **Circulation approvals, both directions:** James proposed sharing with **Dafang He + Dhruvil** starting 8/20 → "Sure, sounds good to me!" (🤝 + thank-you reacts). Qinglong asked to share with **Jianing Sun — his TL, who drove the SSD spacing for CQ and demotion on other surfaces** (⟨role?⟩ from 7/27 WG add now resolved) → James approved ("Of course. I will do the same and encourage…" — James also signaled sharing on his own side). CQ pulling its senior TL in = investment signal, real co-ownership posture. *Boundary watch:* D5 puts SSD *adaptation* under recsys accountability; Jianing drove SSD spacing for CQ on other surfaces — keep the ownership line clean when the doc's ownership table gets his eyes.
- **One narrative flag (low stakes, cheap counter):** "it expands my original doc" keeps a parent-document story with his doc as the seed. Gracious, not hostile — but if it echoes upward ("James expanded Qinglong's doc") it dilutes first-authorship in front of Faisal/Michael/Bill. Counter in circulation language, not in reply: consistently call it "the framework Qinglong and I are co-authoring" in WG posts and share-outs. *(→ largely resolved by events 8/21 — see below.)*

**2026-08-21 — Framework shipped to the WG on Michael's date; Qinglong publicly anoints it the planning surface:** James shipped the joint framework Fri 8/21 (the Fri-8/21/Mon-8/24 gate → Bill Ready Wed 8/26 path). Comments from **Qinglong + Michael (both "quite excited") + Dhruvil + Dafang**. Same day, post-Dhruvil-1:1, Qinglong posted a WG update (verbatim: `sources/06_`): two experiments greenlit to kick off (**GenAI image spacing + GenAI L2 domain demotion**), upper-funnel-first principle, Dhruvil's two **L1** ideas folded in (marginal loss penalizing positive engagement with low-quality content — Notif exploring same at L1; controllable distribution for borderline content, feasibility w/ Dafang) — and: **"I think James's doc is a very good starting point and I will add Dhruvil's ideas to the doc and tag relevant folks… form short-term and long-term plans for quality-aware ranking."** Reads: (1) the narrative flag is countered by his own public words — it's "James's doc" in the org record now; (2) L1-vs-L2 turf line fully dissolved into James's full-funnel frame; (3) his 8/17 upper-funnel filtering analogy (indexing/unity/NGAPI) repeated = durable shared language. **Open action items (next week): HF names an L2 PoC to work with CQ** (L2 = Dhruvil's pillar — coordinate the pick, don't claim it) **+ a technical session on the James/Dhruvil ideas.** Ledger: exceeds campaign 8/21 entry #2.

**Related:** §14 Faisal (his manager) · §38 Michael Weissinger (PM across the program) · `work/projects/safe_journeys/`

# 51) Jaewon Yang — Distinguished MLE, ATG; de-facto UPP TL (promoted to DE 2026-09-01; added 2026-09-02)

**Who:** senior ATG IC (central ML org — Jiajing's world), the de-facto **UPP TL**; CFM and RecGPT both originate from his world (*"both are my projects anyway"*). Co-led the unified base retriever design for UPP×P2P; technically credible with both P13N and SSJ; pushes substance over packaging (7/22). Reciprocal-confidentiality relationship with James since 8/20 (James shared Matt's DM screenshot + the Jan-2026 promo-block history; Jaewon scored Matt below the IC17 cross-functional bar; both pledged silence) — full record `../projects/upp/l1_flashpoint_2026-08.md`.

**9/1 — promoted to Distinguished Engineer (MLE).** Told James directly, day of, in their DM — with a receipt: *"It happened soooooonn as you called 😂 Thank you so much for your support. I highly appreciate the support I receive from you and your team members. I feel blessed to work with many talented collaborators, and this is the biggest reason I enjoy working at Pinterest!"* (James had teased *"when will you be DE?"* → *"sooooooonn"* days earlier.) James: *"HUGE CONGRATS JAEWON!!!"* Screenshot filed 9/2.

**What the promo changes (Leo read, 9/2):**
- **The DE-succession read (8/21–22) needs re-examining.** Dylan's intel: an unnamed DE joining under Rajat would TL UPP, "most likely replacing Jaewon," Jaewon possibly unaware and feeling threatened. ⟨Leo inference, unconfirmed⟩ that DE ≈ **Karthik Subbian** (this file, Karthik entry near the top: DE, joined Core 8/29 from M10N, Dylan asked him to focus on UPP and pointed him at James) — the record carried both facts for a week without connecting them. UPP now has **two DEs**: Karthik (incoming, TL-designate per Dylan) and Jaewon (freshly promoted, de-facto TL, ATG). A newly minted DE is far harder to "replace"; the promo reads as the cycle landing regardless, a retention move, or a reshaped plan (co-leads? split by layer?). **Don't assume Karthik-replaces-Jaewon still holds. Ask Dylan the UPP TL shape** — fair game, the DE intel came from her.
- **Jaewon's weight rises.** As "the technical counterbalance" (§Kurchi mitigation) and James's conduit to Chuck + Jiajing, he now carries DE authority into the CFM/RecGPT/L1 governance question and the UPP×SSJ substance push. Good for the platform thesis — he has argued unified / no-special-name from the start.
- **Exposure unchanged, counterpart more senior.** The 8/20 disclosures sit with a DE now. His pledge is the only guard; don't add to the pile.
- **Receipt for the record:** *"the support I receive from you and your team members"* — an ATG DE crediting P13N Retrieval's collaboration, unprompted, in writing. Advocate-grade for the H2 Exceeds case (`../career/exceeds_h2_2026_campaign.md`); add him when the advocate list is next touched.

**Watch:** who gets announced as UPP TL and how Karthik↔Jaewon is set up (co-lead vs handoff). James's posture: keep both DE channels warm, take no side on TL-ship, route technical questions by whichever DE owns the layer.
