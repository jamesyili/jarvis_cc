# EM Story Grill Plan — Next Session

**Purpose:** Structured grilling questions for the 6 Pinterest stories to be added to `Sr. EM Interview Prep.md`.
**Format per story:** Context → Action → Results → Learnings. One question per turn. James's recommended answer / default assumption noted where applicable.
**Source plan:** This session, 2026-05-22. James locked the 6-story set after iterating on the AI-forward arc.

---

## The locked 6-story set

1. **Reflex genesis with Andrew Y** — AI-forward, senior co-dev
2. **Pinkerton genesis + cross-org adoption** — AI-forward, technical vision
3. **Coaching Bowen to manage out Charlie** — skip-level coaching the new manager through formal perf case
4. **Bowen → Staff Promo + EM Transition** — fills existing stub, high-performer story
5. **Piyush turnaround — underperformer → IC17 promo-ready** — performance recovery
6. **Retentive Recommendations genesis** — flagship technical-vision story, AI-forward Director-track program

Snap stories all stay as legacy reference.

---

## Story 1 — Reflex genesis with Andrew Y

**Context-gathering**
1. When did Andrew first surface the Reflex idea publicly to you, and what was the original framing? (Memory says 4-stage pipeline — Detect/Build/Simulate/Prove — was formalized 4/15. Was the idea older than that? Did you have prior conversations?)
2. Who else was in the founding circle on the Andrew side and the Dylan side? (Memory: Anna K, Matt Chun, Tim Chu on Andrew side; you, Dhruvil, Rahul Goutam, Dylan on Dylan side.)
3. What was your specific opening contribution that earned you the "expert-in-loop" role? (CG codepath knowledge? RLHF feedback design? Both?)
4. Was there a moment where Andrew committed to landing Reflex code in git for explicit co-dev with you? What was the trigger?

**Action**
5. What was the Feedback Curator + Skeptic design specifically — what's the gap it closes? Why did it land on you to design vs. Andrew's team?
6. The 5-PR execution pack pre-RLHF meeting — what's the load-bearing decision in that pack? Which PR did you fight hardest to land in the sequencing?
7. The frame-capture-deferred-to-contribution moment with Andrew at the Rajat meeting (4/16) — walk me through what happened. What did Andrew say? What did you choose to do in the moment vs. what was your instinct?
8. The pre-RLHF meeting reframe — "experience-the-system, not proposal-review" — was this your call or Andrew's? What changed because of it?

**Results**
9. What landed in production from the Reflex co-dev, and what's the metric you'd point to?
10. What did Andrew's behavior toward you change after the co-dev arc kicked in? (Memory hints at trust + air cover but I don't have specifics.)
11. What did this arc cost you — political, time, or scope?

**Learnings**
12. What did this arc teach you about co-developing with a Sr Director who's also a sponsor? Anything you'd do differently?
13. Where does Reflex stand today as Engine vs Accelerator framing — and how is that landing with Dylan?

---

## Story 2 — Pinkerton genesis + cross-org adoption

**Context-gathering**
1. When did Pinkerton (then Pinsight) first emerge as your idea? What was the catalyst — a specific user-experience failure, a research paper, a 1:1 with someone?
2. Who was the first person besides you who said "this should be a thing"? (Dylan? Dhruvil? Andrew?)
3. M0 shipped to production 2026-04-07 week (2 PRs landed) — what specifically shipped? Walk me through what M0 actually does in a sentence.
4. When did the agentic-recsys-vision concept (`pinkerton-agentic-vision.md`) crystallize as the long-term roadmap?

**Action**
5. The 4/16 Rajat demo — what did you actually demo? What did Rajat say verbatim? How did his "I'll talk about the big picture later" land in the room with Andrew there?
6. The Pinsight → Pinkerton rebrand on 5/16 — what drove it? Was it Dimitra's call entirely, or was there a Pinterest-internal reason?
7. The visual user signature primitive (VLM saves + closeups, structured + narrative schema, bottom-up taxonomy) — what's the technical insight that makes it different from existing user-rep work like UPP?
8. Pattern A architecture decision (Pinkerton stays dumb-but-rich, reasoning lives in consumer) — what was Pattern B? Why did you choose A?
9. The joint Jeff demo deck (5/14) with Dimitra (Notifs) + Chuxi (HF) — what's your role on the deck specifically? Why did you take Slide 1 only (~45 sec opener)?
10. What was Chuxi's onboarding to Pinkerton M1 like — how did the 20% commit happen?

**Results**
11. How did the Rajat 4/16 demo change Rajat's stake in Pinkerton specifically? (Memory says he's now VP-level stakeholder on fix-loop.)
12. What's the current adoption state — who's using Pinkerton M0/M1 in production beyond your team?
13. What does the Pinkerton-as-Reflex's-diagnostic-substrate positioning unlock that the separate-workstream framing didn't?

**Learnings**
14. What did the Dimitra naming concession (you let her own the name) teach you about cross-org launches?
15. The frame-capture moment from the Rajat meeting — would you do it the same way now, or differently?

---

## Story 3 — Coaching Bowen to manage out Charlie

**Context-gathering (the biggest gap — I have minimal context)**
1. When did Bowen become an EM under you? At what level was he when he started managing — was he new to management?
2. Charlie was on Bowen's team — when did Charlie's underperformance surface? Was it before or after Bowen took over the team?
3. Did Bowen identify the underperformance independently, or did you (skip-level) flag it first?
4. What was Charlie's specific gap — technical depth, execution speed, scope ownership, communication, accountability? What was the SBI (situation/behavior/impact) shape?

**Action**
5. What did Bowen's initial instinct look like — was he soft on the formal-plan concept (like Prashan in the recent loop), or did he go straight to documenting? What did you have to coach him on?
6. Walk me through the HRBP engagement — when did you bring HRBP in? Was that your call or Bowen's?
7. Did you let Bowen own the conversation with Charlie, or did you co-pilot? When and how did you decide?
8. Was there a moment where Bowen wanted to step back from the management-out and you held the line?
9. The decision to exit Charlie pre-6/1 (before James's OOO + Dylan's OOO) — whose call was that primarily?

**Results**
10. How did the management-out actually land — clean exit package? Resignation? Where is Charlie now?
11. What did Bowen do differently as an EM after this — what's the durable change?
12. Team impact — morale, productivity, peer signal?
13. Dylan's view of how Bowen handled it (and how you coached) — what did she say about it later?

**Learnings**
14. What did you take from this skip-level coaching arc that you didn't already know from the Snap Yitong/Stella case?
15. Is there a moment where you almost over-intervened? What kept you from doing it?

---

## Story 4 — Bowen → Staff Promo + EM Transition

**Context-gathering**
1. Was Bowen an EM under you who *then* promoted to Staff IC and transitioned out of management? Confirm the arc direction — EM → Staff IC, not the other way.
2. When did Bowen first signal he wanted Staff IC vs. continuing as EM? Was it his pull, your push, or organizational shape?
3. What was Bowen's scope as EM at the time the Staff conversation started?

**Action**
4. What scope expansion did you architect for Bowen to make the Staff case — what specifically did he own that wasn't his before?
5. How did you handle the dual track — Bowen as EM still landing team commits while also building the Staff-IC narrative?
6. What was the promo packet narrative — the headline impact, the scope evidence, the cross-team signal?
7. Who advocated for Bowen in calibration besides you? Did Dylan champion it, or did you carry it alone?
8. Was there friction or skepticism in calibration? What was the pushback, if any?
9. How did you frame the EM-to-Staff transition publicly to the team — what was the messaging?

**Results**
10. Bowen's promo — when did it land? What level Staff IC?
11. How is the EM backfill going (the current 9-candidate hiring loop)? Is the seat shape changing post-Bowen?
12. What did the team's response to the transition look like — buy-in, concern, neutral?

**Learnings**
13. What did this teach you about pulling for a high performer's promotion when it requires architecting scope around them?
14. Anything you would do differently in pacing the EM-to-Staff transition (specifically the team-disruption side)?

---

## Story 5 — Piyush turnaround from underperformer to IC17 promo-ready

**Context-gathering**
1. When did you first identify Piyush as underperforming? Inherited him from prior manager, or surfaced during your tenure?
2. What was the underperformance shape — technical depth gap, scope ownership, execution, communication, accountability? Be specific.
3. What level was Piyush when underperformance surfaced? What level is he at now (IC16 going for IC17? IC15 going for IC16? Confirm the exact ladder.)
4. Was anyone else involved in the assessment that he was underperforming — peer ICs, his TL, your manager?

**Action**
5. What was your initial intervention — formal plan, scope adjustment, mentorship pairing, project shift, or something else?
6. Was there a specific project / scope move that started the turnaround?
7. Who else did you involve in the development — mentor pairing, cross-team exposure, specific stretch assignments?
8. What conversations did you have with Piyush directly that were load-bearing? Anything that stands out — a moment where he heard the feedback differently than before?
9. How long did the turnaround take from first intervention to "promo-ready"?
10. What did the calibration cycle for the previous level look like — did he get a clean signal, or was there ambiguity that you navigated?

**Results**
11. Current state — is the IC17 promo packet in progress, or has it landed?
12. What's the specific evidence package — the headline impact, the scope, the cross-team signal?
13. What's Piyush doing today that he wasn't doing before the turnaround? Behavioral change, not just titular.
14. Team impact — has Piyush become a model for other ICs who were stuck?

**Learnings**
15. What did this teach you about distinguishing "actually underperforming" from "wrong-context underperformance"? (Memory hints at this from the Stella story — she ended up doing well elsewhere.)
16. What would you do differently in the next Piyush-shaped case?

---

## Story 6 — Retentive Recommendations genesis

**Context-gathering**
1. When did the Retentive Recommendations concept first crystallize as a coherent organizing principle (vs. a collection of related projects)? Calendar date if you can; otherwise quarter.
2. Was there a specific catalyst — a paper you read, a conversation with Krishna/Anna/Dylan/Andrew, a metric that surfaced, an exec ask?
3. Who else was at the founding circle besides you — naming explicit credit for what you built on?
4. What's the relationship between Retentive Recommendations and Krishna's role — did you inherit program lead from him, or did the program come together post-Krishna?

**Action**
5. What's the founding insight — what makes RR different from prior recsys frames at Pinterest (engagement-max, watchtime, etc.)?
6. How does RR connect the underlying components — UPP, OmniSage, UIC, Geometric Prediction, LLM reasoning, Feedback Loop? Which are foundational, which are application, which are exploratory?
7. The Pinterest Engineering Blog post (inherited from Jiacong's draft) — what was your specific contribution? Did you take over the narrative spine, or just shepherd the team-edits process?
8. The KDD 2026 paper — what's your scope across Prior Work + Architecture (chapter lead) + Future Work? Who do you lead in the working group?
9. How did the program get "James publicly named as program lead" — was there an explicit moment / announcement, or did it ratify gradually?
10. What's the Engine + Accelerator framing — when did that crystallize and with whom?

**Results**
11. What's shipped under the RR banner that wouldn't have shipped without it as an organizing principle?
12. Engineering Blog post status (memory says done 2026-04-17) — what was the reception inside Pinterest? Outside?
13. KDD paper status — soft draft target end of April, full draft July, notification November. On track?
14. What's RR doing for the team that the prior recsys framing couldn't do — what's the durable change in how the team operates?
15. VP-level mental model — how many VPs have RR installed as "James-led" today? (Memory has this — Jeff went 0-10% → 55-65% in 5/7 OH. Others?)

**Learnings**
16. What did this teach you about taking over a program from someone (Krishna) who left it incomplete?
17. What's the lesson about authoring a research narrative as an EM (the KDD paper specifically)?
18. The Wes-Kao-grounded headline statements (memory: `wes-james-situations.md` Q14 — RR <15-word headline) — when did the language sharpen? Was that David coaching? Wes notebook? Your own iteration?

---

## How to run the next session

1. Open this file. Pick a story to start with.
2. Answer each question with as much specificity as you have. Names, dates, decisions, verbatim quotes if you remember them.
3. I'll draft the story in the Sr. EM Interview Prep file as we go, then refine on your feedback.
4. Stories are independent — we can do them in any order. Suggested order:
   - **Reflex + Pinkerton first** (highest AI-forward leverage, partial context already)
   - **Bowen + Charlie + Bowen-promo together** (shared protagonist, two stories from one timeline)
   - **Piyush turnaround** (standalone)
   - **RR genesis** (heaviest narrative load — save for last when you have momentum)

## Notes on what I already have (vs. need from you)

| Story | What I have | What I need |
|---|---|---|
| Reflex genesis | Strong context from session logs + memory — Detect/Build/Simulate/Prove pipeline, Feedback Curator + Skeptic design, 5-PR execution pack, frame-capture moment | The specific verbatim moments + your behind-the-scenes reasoning + the cost/political-side |
| Pinkerton genesis | Strong context — M0 ship, Rajat demo, Pinsight rebrand, VLM signature, Pattern A, Jeff joint demo | Same — verbatim moments + behind-the-scenes |
| Bowen + Charlie coaching | Minimal — backlog mentions Charlie CPP but Bowen's role in it is undocumented | **Full grill needed.** This is the largest gap. |
| Bowen → Staff Promo | Minimal — only a header stub | **Full grill needed.** |
| Piyush turnaround | Minimal — Piyush named as IC16 in pod structure but underperformer history undocumented | **Full grill needed.** |
| RR genesis | Moderate — program-lead status, Engineering Blog, KDD paper, Engine framing | The *founding moment* + Krishna handoff + technical-vision spine — undocumented in session logs |
