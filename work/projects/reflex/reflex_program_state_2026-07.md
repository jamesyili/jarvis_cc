# Reflex — Program State, July 2026

**Captured:** 2026-07-25 context-dump session. Prior state: Dafang He = overall TL (5/29 structure), **Tim Chu** = PM (Andrew's FTE assignment; surname confirmed 7/29 from Slack), Andrew Yaroshevsky = sponsor, James = architect/sponsor altitude.

## Where James stands (7/25)

- **Wants to increase leverage with Dafang.** Dafang is the operational TL; James's influence currently runs thin there.
- **Tim (PM) 1:1 — honest and useful.** Tim was frank about what's happening and how James could be more involved. **Key signal: Tim said he wasn't sure what James's role is in all this** → James's read: **Dylan hasn't made his role clear to Tim.** James will ask Dylan to clarify it explicitly.
- **POC naming helps:** Dylan recently pulled James into a thread with Tim + Dafang and **named James, Dafang, and Tim as the three Reflex POCs.**

## Tim 1:1 notes (screenshots filed 7/25)

- **Funding for Q3 from HF CG:** how much time **JJ** spends here (main deliverables); how much time **Bella** spends here (main deliverables); more folks interested — what do we put them on?
- **Operating model with James + team — role options discussed:**
  - James as **IC working on a project**.
  - **Prove stage = opportunity** (connect with Lu / Brian / Analytics Agent; could staff someone from James's team to get it going).
  - **Detect stage = opportunity to connect with Chao and Gideon** — getting agents to produce *actionable* solutions; **evals important for measuring improvement, templates important; LR docs can be a source.**
  - **James's team's role:** the starting place for funding within HF.
  - **Janvi owns the Evolution stage** — compounding learnings into the knowledge.
- **Feedback from Tim:** **Dafang moving a bit slower than anticipated** (vs. Janvi / Chao / Sam Owens at expected pace); wants a higher-level POV of how things should work to set the scaffolding; **wants to ensure Dafang can remain overall Technical Lead**; modeling agent's place in the build stage still to figure out. **Next steps: concrete deliverables with concrete timelines (e.g., system-design 1–2-pager); weekly Tim/Dafang/James sync starting mid-August.**
- **JJ:** Tim would love more collaboration with **Janvi and Ads CG**.
- **Bella / Simulate:** presentation meeting **requested by Andrew** (sharing Chi's simulation work); James in-meeting: "Tim wrote something — leverage that as a start." **Tim: her work so far is not concrete enough**; "consider a full design later, guided by implementation first?" **Agreed timeline: V0 — something to show by mid-August.** *(Cross-filed to team_members_scope.md Bella 7/25 — third-party corroboration of the impact concern.)*
- **ATG technology goals:** RecGPT as pipeline backbone = "more of a P2"; predict-the-actions = "probably not what we want." **Tim is actively steering these conversations.**

## The time-allocation tension (feeds Q3 priorities discussion)

- James: *"Honestly this is where I want to be spending most of my time"* — he sees many concrete places he could help. But with **Retentive Recs and UPP in their current states, he doesn't know if he can afford that time.**
- Delegation levers: **JJ** was the one who "did my bidding to get things going on Reflex" — James is looking forward to **JJ's return**, and to **Rui starting to contribute more** here.

## Inbound interest signal

- **Reflex has put James's name out there.** People are reaching out about Reflex and GenAI tooling — e.g. **Brian ⟨James 7/25: "Brian (?)" — identity still soft; not confirmed to be Brian Lee of Growth⟩ from Ads**, and others.
- Dovetails with **Sen's (§49) offer** that his team could help on AI tooling — a possible tooling-alliance thread.

## Shifu ↔ Reflex (2026-07-29)

- **Dylan opened the lane herself:** after Roberto Konow's Shifu demo, she messaged the joint group (7 members incl. Andrew Yaroshevsky, Assaf Broitman) — "connect the dots between Shifu and Reflex… join force or leverage each other" — and named **Dafang, Tim Chu, and James as the P13N POCs**. Roberto shared Shifu resources: GH `pinternal-dev/ssj-agent-platform` + design doc + slides; noted **An (John) Jiang** had reached out to the Reflex team earlier.
- **First working meeting (7/29 — Tim Chu, Roberto, Assaf Broitman, Dafang, Luke DeLuccia):** readout = systems very complementary, **Shifu ahead on build, Reflex on discovery**. Next steps on record: (1) **"search is asking shifu to integrate itself within reflex"**; (2) Roberto scheduling a Shifu deep-dive for **Dafang / James / Ananth Pushpendran / JJ Hu / Janvi Palan**.
- **Leo read (7/29, unratified):** the Evans Q4 Roberto partnership-probe resolved in Reflex's favor, with Dylan's air cover — Reflex is the substrate, Shifu integrates in. Posture: warm + reciprocal (offer a Reflex deep-dive back, open vision doc + weekly), credit Shifu's build progress, **do not re-state the integration hierarchy in public channels** (Kurchi sensitivity — Tim's readout already carries it). Roberto 1:1 cadence DM (James's saved draft) queued.

## Open (queued for 7/25 session analysis)

- How to raise James's leverage with Dafang without colliding with the TL structure he himself set (5/29: operational ownership deliberately with Dafang).
- Dylan role-clarification ask (to Tim) — timing and framing.
- Whether Reflex time-share can grow in Q3, and what JJ/Rui delegation must be true for that.

## 2026-08-01 — Shifu folds INTO Reflex; James named EM POC; the refocus commitment

- **Shifu → Reflex fold confirmed** (Roberto's framing, kept verbatim for upward narration): Shifu was **further ahead on the Build agent** → leverage that and continue the functionality; **Reflex is much further ahead on discovery and the RL aspects.** Politically graceful framing — honors Search's contribution while establishing Reflex as the frame things fold into; use his words, never amplify who-integrates-into-whom.
- **James named EM POC for Reflex by Dylan** (confirmed 8/1 — "Hanlin" was a dictation artifact). The role-sentence ask is **moot**: "I don't need to be named anymore. I trust her — she'll give me the glory if it comes to that. First we need to actually deliver the glory."
- **The commitment (James, 8/1, out of the Jan-2027 regret simulation):** weeks of 8/3 + 8/10 = reorg people focus (first skip 1:1s with new skips; technical deep dives on Recommended Boards + Intelligent Boards). **From ~mid-August: James's time = (1) Reflex, (2) UPP. Everything else is delegated.**
- Staffing aligns with the window: Rui back 8/9, JJ back mid-Aug (Build), Bella Simulate demo mid-Aug, Alok on Pinkerton. Fall glory deliverable ≈ a working, demonstrated Reflex that visibly absorbed Shifu — shown, not announced.

## 2026-08-03 — Assaf widens the fold; Roberto quiet on the cadence DM; Tim OOO (Slack screenshots, filed from phone session)

- **Assaf Broitman (SSJ PM) reply in the joint thread, Thu 7/30 8:50 AM** (on Tim Chu's 7/29 meeting readout): *"while Shifu is an opportunity to expand Reflex on the dev side, lets follow up on how we best define and integrate the Search idea/define into reflex as well. We started looking into building something but I don't see any reason to duplicate work here and if we land on a good model to enable the team to bring the SSJ PM /DS/UXR agents into reflex."* Read (Leo, unratified): Search's own PM saying "into reflex" twice — affirms the substrate direction in their words (never James's, per the Kurchi sensitivity) — while **widening the fold beyond the Build agent to SSJ's PM/DS/UXR agents**, conditional on "a good model." Demand side is growing; whoever brings the integration frame to the deep-dive sets the terms.
- **Tim Chu OOO:** replied same morning *"Sounds good - let's connect when I'm back. I'll find time."* → the joint thread is parked on Tim's return.
- **Roberto DM on read:** Roberto proposed a 1:1 cadence 7/28 (*"many things UPP/Prelevance/Shifu-Reflex/etc… some cadence of 1:1s?"* + warm Alim note — Alim was the first EM he managed as an M2); James accepted 7/29 7:02 PM proposing biweekly; **no reply as of 8/3 AM** (~2.5 business days incl. weekend). Leading read: noise, not signal — Roberto's own 7/28 opener apologized for an earlier slow reply, and the whole thread is parked on Tim. Alternative held loosely: Search-side cooling after the fold went Reflex's way. Move: James sends the biweekly invite directly — Roberto requested the cadence, so scheduling it is closing a loop, not chasing.
- **Shifu deep-dive scheduling** (Roberto owns, for Dafang/James/Ananth/JJ/Janvi) still pending; if nothing by ~Thu 8/6, light thread nudge anchored to landing it when JJ is back mid-Aug.

## 2026-08-10 — Shifu deep-dive: the frame inversion; James's two closing asks land unanswered; Evolve arrives from Ads

- **The deep-dive happened (Roberto + team presenting).** Build progress genuinely strong and James says so: 156 merged PRs / 13 weeks, 20 contributors, 7 launches (+0.7% global repins Strong OR, $340K cost reduction, etc.), exec-grade deck written in "why this matters to a CTO" register.
- **⚠️ Frame inversion vs. the 8/1 record.** The deck positions Shifu as "a strategic template… for how any engineering org at Pinterest could adopt autonomous development," SSJ as "the proving ground," with "templatize for a second org" as a named next step — and the in-meeting framing slots **Reflex as an upper-funnel discovery system whose build and evolution route through Shifu**. That is the mirror image of Roberto's own 8/1 framing (Shifu ahead on Build → folds into Reflex; Reflex ahead on discovery + RL) and Assaf's 7/30 "into reflex" ×2. James's live read: subtle repackaging pressure. Sober read: narrative-level threat with a clock (frames harden if unanswered), not a verdict — the political record (Dylan's air cover, James = EM POC, their own on-record words) still stands.
- **James's closing intervention** (raised hand as time ran out; had to drop for an interview; no response received — clock, not rejection): (1) *substance over packaging — focus on what we build together;* (2) *how do we work together going forward — who contributes what to the collective effort?* → Follow-up Slack message drafted (3 versions, 8/10 session). Craft rules: propose lanes in writing using **their own words** (Roberto's build-vs-discovery framing; never the who-integrates-into-whom line — Kurchi sensitivity holds), offer to hold the pen on a working-model straw doc, land a 60-min working session. First-mover on the open question, not a recovery.
- **Evolve (NEW — from Ads).** A senior Ads MLE collaborating closely on Reflex delivered the "Evolve" design; his manager wants to collaborate too. Offline, human-governed playbook/agent-spec improvement: replay recorded cases against snapshotted fixtures (Asana/Presto/MCP) → grade Detect cards or Build PRs (numeric + rationale) → GEPA proposes single-component section-level edits → Pareto dominance gate (no-worse-everywhere, better-somewhere) → human approval + full case-bank rerun → versioned specs. **Read: third leg of the judgment layer — Detect (discovery) · Simulate (evals) · Evolve (improvement governance)** — the rigorous version of the flywheel Shifu's deck hand-waves as "continuous upskilling," and a direct answer to the outcomes-vs-activity measurement gap Shifu's own caveats name. The EvalResult contract is agent-agnostic in principle (could grade/evolve Shifu's 17 roles too). **Caveat: strong design, not a deliverable** — open gaps: eval math, schemas, held-out methodology, judge calibration, security/rollback. Value this month = direction + cross-org gravity evidence; cite the collaboration, not the maturity.
- **Cross-org gravity ledger:** Shifu *plans* a second org; Reflex *has* one arriving unasked — Ads (Evolve MLE + manager), SSJ's own PM (Assaf: PM/DS/UXR agents "into reflex"), Brian inbound, Sen's tooling offer. Adopters take a template; contributors choose a home.
- **Sober ledger + counter-move (unchanged, already scheduled):** their packaging and build velocity are real; Reflex's build layer is honestly behind (Dafang slow, Simulate pre-V0, Presto-blocked hypothesis backlog, laptop-only portability, cost untracked). The counter is the 8/1 plan: mid-Aug time shift to Reflex, JJ + Rui back, Simulate V0 mid-Aug, fall deliverable = **a working Reflex that visibly absorbed Shifu — shown, not announced.** New note for later sizing: Search is better at artifact-making, and artifacts travel to rooms James isn't in — a deliberate Reflex artifact move is warranted eventually; a move, not a crisis.
