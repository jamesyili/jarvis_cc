# Ethan Evans Review — UPP Cross-Org Operational Model v2

**✅ RAG-grounded.** Notebook: `ethan-evans-frameworks` (https://notebooklm.google.com/notebook/b8d6232f-1b8b-47e8-8ac5-99fc2d7f35b6). Session ID: `436991a2`. Two-question session run 2026-04-25b after the notebook was registered + auth was repaired in main session via `setup_auth`. Framework citations and quoted passages below are from Ethan Evans's own source material (Substack archive + 6 Lenny's-Podcast Ethan-Evans-Amazon episodes).

**Document reviewed:** `draft_v2.md`.

> **Note on revision history.** A prior version of this file was channeled from training (notebook didn't yet exist locally). The grounded review departs from the channeled review in three material places — flagged below as **[Grounded correction]**. Worth reading both if you want to see where notebook-grounded review beats training-channel review.

---

## Verdict: Senior Manager altitude as-is. Highest-leverage fix is §9.

The doc demonstrates strong functional competence and operational detail — which is what gets you to Sr. Manager. It lacks the strategic framing, influence, and decisiveness required of a Director. **It optimizes within the box rather than articulating a larger vision.**

The single most transformative change is **applying the 70% Rule to §9**. Asking peers to decide the operational model for you reads as lacking "gravitas" and executive presence, which Ethan defines as composure + decisiveness. Replacing crowdsourced questions with proposed 70% decisions instantly shifts your posture from operational coordinator to executive leader driving alignment.

---

## Five Ethan Evans frameworks, applied

### 1. The One-Page Rule

**What it requires.** Executives need to see the goal, the data, and the ask up front without digging through the weeds. Adding too much detail without an executive-level view can be triggering — execs are trained to make decisions with imperfect data, and they expect respect for their time.

**Where v2 falls short.** Opens with a meta-paragraph aimed at the working group, plunges directly into 11 sections of operational weeds. No "For leads" callout. Senior reviewers (Dylan, Dimitra, Sai, Matt Chun) have to hunt for the strategic point.

**Concrete fix.** Insert a "BLUF" box at the very top of the doc:
> **Goal:** Align on a scalable post-launch ML handoff architecture.
> **Data:** Notifications is the V0 test case.
> **Ask:** Review the accountability boundaries and commit to the proposed release cadence.

---

### 2. Scaled and Deep — via Mechanisms

**What it requires.** Executive-level leaders are both strategic *and* highly detailed, but only because they set up **mechanisms** that force depth into the week — weekly business reviews, structured cadences, scorecards. You scale to the next level when your mechanisms ensure smart decisions happen without you in the room. Without mechanisms, you're relying on individual heroics, which is Sr. Manager work.

**Where v2 falls short.** Current state is described in statuses ("Hongtao currently driving FT," "Rui stepping up") instead of an explicit accountability/owner-by-name table. No week-by-week Notif handoff mechanism. No monthly cadence to keep the operational model alive post-launch.

**Concrete fix.** In §7 Coordination Mechanisms, insert:
> **Monthly Handoff Review (MHR).** Designated surface-team owners report on integration health metrics using a standardized scorecard. Owner: base-team TL. Audience: working group + leads.

Then add a §6 accountability table (named owner per role + accountable-for column) and a week-by-week handoff mechanism.

**[Grounded correction]:** The channeled review framed this as "OAR (Ownership / Accountability / Results) table" + "weekly snapshot." OAR is *not* an Ethan Evans framework per the notebook — it's a generic instinct that mapped onto the right gap. The actual Ethan move is **mechanisms that force depth without micromanagement**, named explicitly. The fix is the same shape (named-owner table + recurring review meeting), but the framework attribution and emphasis are sharper: this isn't about ownership clarity in the abstract, it's about engineering the system so smart decisions happen without you.

---

### 3. Audience-Specific Reads

**What it requires.** Executive presence is judged differently depending on who is looking. Leaders ask: *"Are you competent and composed?"* Peers ask: *"Are you a partner or an adversary? Will you help my agenda or hinder it?"* You must frame the partnership as a win for the peer audience or it reads as adversarial tax.

**Where v2 falls short.** No surface-team value-proposition section. The Notifications, P2P, and Search teams reading this doc see what the base team won't do (won't approve launches, won't claim wins, won't retune) but no positive frame for what they get.

**Concrete fix.** Insert a "Value Proposition for Surface Teams" section after §1:
> By adopting this standardized handoff, the Notifications, P2P, and Search teams reduce ML integration time by [X weeks] and gain direct, unblocked control over their own engagement tuning.

Replace `[X weeks]` with the actual time-savings estimate from the Notif precedent.

---

### 4. The 70% Rule — *the highest-leverage fix*

**What it requires.** To operate at Director altitude, **most decisions should be made with about 70% of the information you wish you had**. Waiting for complete certainty or consensus is too slow. Crowdsourcing your decisions to peers reads as lacking gravitas and signals you can't operate at the level above.

**Where v2 falls short.** §9 asks for working-group input in 8 places, each phrased as *"Is X right? Or should it be Y?"* This is the single most altitude-deflating move in the doc. It crowdsources the answers instead of asserting them.

**Concrete fix.** Rewrite all 8 §9 items from *"Is X right? Or should it be Y?"* to a declarative proposal that invites disagree-and-commit, not opinion-collection:
> **Proposed baseline:** [X]. We will proceed with this model unless there is data proving it blocks the upcoming P2P or Search integrations. Flag any blocking objections by Friday.

The frame shifts from "what do you all think?" to "I made the call; tell me if it's broken." Same input mechanism; very different altitude.

**[Grounded correction]:** The channeled review framed this as *"reframe §9 from questions to bets-with-alternatives-and-pushback-wanted."* That's still better than v2 but it's the wrong altitude — bets-with-alternatives is collaborative-peer framing. The grounded Ethan Evans move is **declarative proposals + disagree-and-commit deadline**. You're not soliciting bets; you're announcing decisions with a defined window for blocking objections. This is the difference between a peer running a working session and an executive driving alignment.

---

### 5. The 10x Problem

**What it requires.** To demonstrate "executive need," you must prove your work solves a problem that **10x's customers, revenue, or strategic position** — not just optimizes a process. If you're only optimizing within a level, you're proving Senior Manager value, not Director value.

**Where v2 falls short.** The opener describes mechanical changes ("Surface teams own FT, base team owns platform, Notif first") without connecting any of it to a 10x business outcome. Reads as operational manual, not strategic solution.

**Concrete fix.** Rewrite the §1 Background opener to elevate:
> This charter solves the scaling bottleneck for our ML infrastructure, establishing a repeatable pattern that allows any surface team to **10x their feature deployment speed** over the next 12 months.

Then the operational changes follow as the *mechanism* by which the 10x outcome is achieved.

**[Grounded correction]:** The channeled review proposed "Magical Thinking opener — write the future as if it's already true." Magical Thinking is a Wes Kao framework, not Ethan Evans's per the notebook. The grounded Ethan Evans move is **10x Problem framing** — connect the mechanism to a multiplicative business outcome. Subtle but real difference: Magical Thinking is voice ("write declaratively"); 10x Problem is content ("connect to a multiplier"). The doc needs both, but they come from different frameworks.

---

## Where the grounded review departs from the channeled review

| Channeled review said | Grounded review says |
|----------------------|---------------------|
| Magical Thinking opener — declarative future-state voice | **10x Problem** — connect to a multiplicative business outcome (10x feature deployment speed). Magical Thinking is Wes Kao's, not Ethan's. |
| OAR (Ownership/Accountability/Results) accountability table + weekly snapshot pattern | **Scaled-and-Deep via Mechanisms** + **Monthly Handoff Review (MHR)**. Same gap, sharper framework attribution. OAR is generic instinct; "mechanisms that force depth without micromanagement" is the actual Ethan move. |
| §9 reframe from questions → bets-with-alternatives-and-pushback-wanted | **70% Rule** — declarative proposals + disagree-and-commit deadline. Bets-with-alternatives is still peer-altitude collaborative; declarative-proposals-with-blocking-window is Director-altitude. |
| Bridges of Trust → surface team value proposition | **Audience-Specific Reads** — peer audience asks "partner or adversary?" Same fix shape; sharper framework name. |
| (Implicit) — doc is mostly there, polish for altitude | **Explicit altitude verdict: Senior Manager as-is, not Director.** Names the altitude problem directly and identifies the single highest-leverage fix (70% Rule on §9). |

The biggest single correction: **§9 is the altitude problem, not an invitation-shape problem.** The channeled review treated it as collaborative voice. The grounded review names it as a Director-track decisiveness gap. The fix is sharper and the stakes are explicit.

The channeled review caught the structural gaps (opener / accountability / surface-team value / §9 / monthly snapshot) but mis-attributed several of them to frameworks that aren't actually in Ethan's source material. The grounded review confirms the gaps are real and reframes them with the correct framework names + altitude diagnosis.

---

## What I'd say if I were James's sponsor reading this doc cold — grounded

> "The bones are right. The work is competent. But you're operating at Sr. Manager altitude, not Director altitude — and the working group will read it that way too. The single move that elevates this doc from 'good operational manual' to 'executive charter' is fixing §9. Stop asking peers to make your decisions. Make the calls, propose them as 70%-confidence bets, and give the group a window to disagree. Same input, different posture. After that, add the BLUF box, the 10x outcome opener, and the Monthly Handoff Review mechanism. Then ship it. The doc and the author both step up at the same time."
>
> — Ethan Evans (notebook-grounded; session 436991a2)
