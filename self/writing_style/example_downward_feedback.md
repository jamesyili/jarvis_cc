> **VOICE EXEMPLAR COPY (2026-08-01)** — duplicated into `self/writing_style/` as a downward-review voice exemplar (James-authored final). **Canonical: `work/people/downward_reviews/h12026/bella_h1_2026_feedback_final.md`** — the pre-ER fix list below applies there; refresh this copy once the delivered version is final.

# Bella Huang — H1 2026 Performance Feedback (FINAL draft, James, 2026-07-31)

> **Status:** James's final draft, logged verbatim 2026-07-31 (Leo's v2 draft deleted same day as superseded). Next step: ER pre-review alongside the Yuke final, then delivery **early in the week of 8/10, before the Simulate demo**, on a separate day from Yuke's. Case record + strategy appendix: `work/people/bella_huang_h1_2026_review_draft.md` (Appendices A–B, strip-before-ER).
>
> **Pre-ER fix list (Leo flags, 2026-07-31):** (1) "Jaewong" → **Jaewon** (name-normalization rule of record). (2) **Team-leadership goal collides with Yuke's goal 4** — both docs assign an oncall-process audit; they talk daily → differentiate scope in both docs (Bella = P13N-wide process/ownership/escalation redesign; Yuke = team-internal automation feeding it) or swap hers to the Capacity Audit; show ER both docs side by side. (3) Grammar: CE paragraph ends without a period ("…for the workstream for relevant stakeholders"); "The GPU-allocation discussions is one example"; "the exercise I led here" — name it (HF oncall revamp). (4) **Promo paragraph absent** — the 7/25 plan called for killing promo ambiguity in writing; decide in-doc vs. verbal (open item B5 in the case record).

---

## Key Accomplishments

Thank you, Bella, for your contributions in H1 2026. You led the team's efforts in RecGPT / Generative Retrieval, led Zihao and Yidi in creating the Content Exploration model and CG, and contributed to retrieval modeling (mostly through the introduction of unimpressed datasets).

On RecGPT, you led the modeling workstream and helped drive alignment with Hanlin, Chuxi, Yuke, and ATG on the RecGPT and Homefeed Retrieval roadmap. You helped champion this effort and drove through obstacles towards its initial launch. This work took up a lot of alignment and model iterations. Afterwards, you identified the importance of certain infrastructure unblocks, including the Manas migration, UserEventsView migrations, and transition from user-sequence training data to FeedView session data. However, the Manas migration work was stalled for quite some time and you had challenges leveraging Hanlin to produce meaningful momentum on this work until I stepped in. In addition, a significant impact bottleneck was RecGPT's limited share of candidate impressions. Increasing that share was not prioritized early enough in the half. Only after I pushed for a concrete action did you work with Hanlin to double the impressions at neutral cost.

In Content Exploration, you led the initial design and championing of a shared Manas-based indexing and retrieval framework across Homefeed, P2P, and Search, and left the implementation and tracking to Zihao and others. You pitched in to unblock the workstream such as when you identified and resolved model-mismatch and experiment-configuration issues that were affecting experimental validity and production integration, which is how this work with its current LR is showing an increased non-graduated content impressions by 10% and has the potential to reduce fragmentation across surface-specific pipelines. However, it is worth noting that you did not proactively communicate progress for the workstream for relevant stakeholders

Your work on the unimpressed dataset produced positive technical and business results, including a launch on Multi-Embedding CG and another for the LWS model. You also began extending this work beyond Homefeed by sharing the approach with P2P and contributing to their early-funnel model improvements.

Taken together, the landed impact falls below expectations for IC16 across H1. While there were many experiments and foundational investments made, it will be important to convert them into completed launches driving substantial metric movement or capabilities and influence across partner teams. The lack of feedback from senior tech leads (e.g. Olafur in Content Exploration or Jaewong in RecGPT) also suggests a lack of influence at the right level. Ensuring alignment and consistent communication with technical leaders across the company will enable you to consistently shape technical direction and land consequential decisions across organizational boundaries.

## Improvement Areas

### Strategic clarity and adaptation

RecGPT is a strategically important investment from our team. A workstream of this scope requires a written technical and execution strategy that explains the intended outcome, the major bets, how each effort contributes to the larger goal, the dependencies and bottlenecks, the milestones along the way, and how progress will be measured before final metric impact arrives. You jointly developed the plan with ATG, and various folks approved it. The gap was therefore not that no plan existed. The gap was in driving that plan as the senior technical owner and adapting it decisively as results emerged. Several planned efforts were delayed or discontinued, but the portfolio was not consistently reworked into a clear revised sequence of priorities, milestones, and decisions that maintained a credible path to impact. The most important example was the mismatch between the modeling investments being pursued and the candidate-generation sizer constraints limiting their impact. CG-sizer tuning and increasing RecGPT's candidate-impression share were necessary to unlock and measure the value of the modeling work, but they were not prioritized early enough. Given your technical depth in the candidate-generation systems, I expected you to proactively and independently identify this as a critical dependency and lead the necessary work across modeling, sizing, and serving.

This lack of clarity affects more than manager visibility. If the strategy, priorities, and measures of progress are not explicit, contributions, particularly junior engineers you're leading, cannot confidently understand how their work connects to the larger outcome, or when the team should continue, change direction, or stop an investment. This sentiment was expressed by multiple team members during my 1:1s with them. At IC16, you are expected to turn ambiguity into a plan that others can understand and execute, secure buy-in on that plan, and maintain a shared view of progress without being prompted.

Heading into H2, I expect you to prioritize your time and energy towards landing the highest ROI strategic bets you have set forth with the team and rally momentum in the generative retrieval and content exploration workstreams amongst the junior engineers working in that space.

### Communication and Influence

I also did not see sufficient evidence in H1 of cross-team technical influence at the level expected of IC16. Although you worked with several IC17+ engineers and senior partners, the available feedback and artifacts do not demonstrate that you were consistently shaping technical direction, driving consequential decisions across organizational boundaries, or being relied upon as a senior technical leader beyond your immediate workstream. The absence of peer feedback is not, by itself, the basis for this assessment, but it is consistent with the broader gap in demonstrated organizational influence and leverage.

In addition, in several conversations with stakeholders around Content Exploration for example, they remarked that they're confused whether you are driving that workstream from the CG team or if Zihao was, as no one was there representing the group in terms of updates or blockers. As a result, there were several delays to the CE CG due to pipeline blockers that could have been easily unblocked if it were escalated earlier. As you started to get more involved in Reflex Simulate, I am noticing a similar gap. From those involved here, the feedback was that the work completed so far was not concrete enough for others to build on, and there is too little visibility into what you're planning. At your level, 0-to-1 uncertainty on projects is expected; the leadership requirement is to convert that uncertainty into concrete artifacts, milestones, decisions, and a path that others in the workstream can rely on and iterate against.

In H2, your leadership should be visible through a written and agreed roadmap, explicit milestones and decision points, proactive communication of progress and risks, clear direction for contributors, and cross-team decisions and capabilities that you drive through adoption. It is critical that you can communicate progress and blockers consistently for the workstreams that you are leading - RecGPT and Content Exploration. I expect you to keep it current without prompting and to flag changes, risks, and decisions when they arise rather than when stakeholders ask. For Reflex, we have since aligned on a first demonstrable V0 for mid-August.

### Team leadership

As an IC16 engineer, you are expected to contribute leadership beyond your immediate technical projects. This includes engaging in team-level decisions, helping resolve shared constraints, and proposing constructive paths forward even when the topic is not directly within your preferred area of focus. I saw you engaging substantially less in team level conversations about improving processes such as shared compute utilization, oncall processes, and indexing pipeline health in H1. The GPU-allocation discussions is one example: after others drafted a proposal, you raised concerns about the proposed approach, but did not develop and drive a constructive alternative that balanced the needs of the broader team. More generally, your participation in many team-level planning and operating discussions was limited relative to what I expect from one of the team's most senior engineers, and even declined from previous years' engagement.

Heading into H2, I expect you to drive at least one team-level operations improvement, by engaging actively, synthesizing the relevant trade-offs, recommending a solution, and help the team reach and implement a decision. Your leadership should improve how the broader team operates, not only advance the workstreams you directly own.

## Goals for H2

For H2, we have aligned on the following priorities and deliverables. These goals are intended to translate the improvement areas above into concrete outcomes.

### RecGPT, Unimpressed Dataset, and Teacher Distillation

Deliver at least 0.4% cumulative SSv2 improvement in H2 across RecGPT, the unimpressed dataset, and teacher distillation. You are responsible for continuing to set the technical direction and prioritization across this portfolio and driving the work end-to-end—from problem definition and experiment design through implementation, productionization, results analysis, and launch. This includes maintaining a clear view of how the individual investments fit together, addressing enabling constraints such as candidate coverage and serving, and revising priorities when experiments do not produce the expected results.

### Content Exploration

Deliver the initial Content Exploration launch and enable other teams, including Content Success, P2P, and Search, to use the shared framework to advance their own goals. Success is not limited to completing the initial Homefeed launch. It also includes providing usable architecture, documentation, onboarding support, and clear ownership so that partner teams can adopt the capability without depending on continued hands-on involvement from you for every step. Ideally, we should be able to point to concrete adoption or committed adoption plans from these teams by the end of H2.

### Reflex Simulate

Continue contributing meaningfully to the 0-to-1 development of Reflex Simulate, including:

1. Share a written document describing the V0 approach before the demonstration.
2. Demonstrate a working V0 by mid-August 2026.
3. After the demonstration, document the next use cases, evaluation approach, dependencies, and path toward a reusable capability.
4. Migrate the work into the Reflex repository as the project matures and according to the agreed program plan.

This is a highly ambiguous space. At IC16, the expectation is that you help convert that ambiguity into concrete artifacts, decisions, milestones, and a direction that the broader Reflex program can build on.

### Team Leadership

Lead the improvement and clarification of P13N oncall processes as your concrete H2 team-leadership contribution. This is similar to the exercise I led here, which includes:

1. Auditing the current on-call workflow, recurring operational issues, and major sources of manual effort.
2. Proposing a prioritized operational plan, including opportunities for automation, improved documentation, monitoring, ownership, and escalation.
3. Building alignment with the affected engineers and technical leads.
4. Driving the agreed changes through implementation and adoption.
5. Defining how we will determine whether the new process has improved operational effectiveness.

More broadly, I expect you to participate proactively in team-level planning and operational discussions, develop constructive proposals when you identify problems, and drive the group toward decisions and solutions.

> **VOICE EXEMPLAR COPY (2026-08-01)** — duplicated into `self/writing_style/` as a downward-review voice exemplar (James-authored final). **Canonical: `work/people/downward_reviews/h12026/yuke_h1_2026_feedback_final.md`** — the pre-ER fix list below applies there; refresh this copy once the delivered version is final.

# Yuke Yan — H1 2026 Performance Feedback (FINAL draft, James, 2026-07-31)

> **Status:** James's final draft, logged verbatim 2026-07-31. Next step: ER pre-review, then delivery week of 8/10 (spaced from the Aug 5 announcement, separate day from Bella's). Supersedes the working draft at `work/people/yuke_h1_2026_review_draft.md` for the feedback text itself; that file retains the ER-side context appendix (self-review transcription, claim map, timeline) and the Workday paste blocks (**re-derive those blocks from THIS text before submission — they still reflect the old v2 letter**).
>
> **Pre-ER fix list (Leo flags, 2026-07-31):** (1) "on par with expectations of IC15 expectations" — doubled word in the opening line. (2) "via another junior engineer" reads oddly against the very-hands-on point ("with"/"alongside"?). (3) Stray double period at the end of goal 4. (4) Goal 4 (on-call process audit) collides with Bella's team-leadership goal — differentiate scope across the two docs (see her final's fix list).

---

## Key Accomplishments

Thank you, Yuke, for your contributions in H1 2026. You performed on par with expectations of IC15 expectations in Q1, but your delivery and ownership declined materially in Q2.

Leading frontier sampling from design through production launch via another junior engineer in Q1 was a good example of IC15-level technical ownership since the problem was ambiguous and you were very hands-on as part of coming up with the solution. During this time, you also helped ramp up Chuxi and Yidi on Retentive Recommendations (RR) as their TL, etc. In Q2, you began contributing to RecGPT, continued to TL the RR efforts, and supported Hanlin while he launched multi-embedding GPU serving.

The IC15 MLE role requires independently taking ambiguous ML problems, designing sound solutions, managing dependencies and technical uncertainty, and delivering end-to-end to production with minimal oversight. It also states that, while engineers at this level begin taking on leadership responsibilities, hands-on technical work remains the primary measure of impact. What I observed in Q2 for RR is that most of your activities consisted primarily of coordinating communication between myself and other RR leads to the other engineers. Your own contributions (code written, model trained, designs produced) were minimal across the entire quarter, far below the expectations of your role. In addition, within the workstreams you led during Q2, critical technical uncertainties were not resolved early, delegated components were not sufficiently understood or vetted by the team members you led, milestones slipped without timely mitigation, and delivery required repeated prompting and intervention by me.

As a result, your overall H1 performance fell short of IC15 MLE expectations in sustained hands-on impact, technical excellence, and end-to-end accountability.

## Improvement Areas

### Sustained Hands-On Impact

The IC15 MLE role requires a sustained record of hands-on technical work that delivers substantial impact to team goals and business metrics. While engineers at this level also lead projects and other contributors, the primary measure of impact remains the technical work they personally own and drive.

Frontier sampling was the clearest example in H1 of you meeting this expectation. You led the work from technical design through production launch, establishing an initial foundation for personalized user exploration. However, this level of hands-on ownership and delivery was not sustained across the half.

Specifically:

1. Frontier sampling was the clearest production launch that you personally owned end-to-end during H1. You contributed to other efforts, including pUIC, RecGPT, and infrastructure work, but these contributions did not add up to the sustained record of independently owned delivery expected at IC15.
2. Both pUIC tracks missed their H1 milestones. Model-based pUIC online serving, which you owned, was not delivered by its original end-of-May milestone and remained incomplete at the end of July.
3. The multi-embedding GPU serving change had passed launch review in 2025, but its rollout slipped by several months. Moving the rollout forward required repeated follow-up, escalation, additional engineering support, and close management oversight.
4. In several Q2 1:1s, I was unable to identify a sufficient set of hands-on technical deliverables that you had personally completed relative to IC15 expectations. Much of the implementation progress in the workstream was owned by other contributors, while your updates primarily described or coordinated their work.

I want to remind you that collective results, coordination, and partial contributions are not substitutes for the hands-on deliverables you personally own at IC15. In H2, you need to demonstrate sustained hands-on impact by personally owning substantial technical work from problem definition through implementation, production launch, and measured results. Your impact should be clearly attributable not only to your coordination or leadership of others, but also to your own technical decisions and completed engineering work.

### Improving Technical Excellence

The IC15 MLE role requires independently delivering sound, production-ready ML solutions; anticipating and resolving core technical uncertainties; applying rigorous evaluation practices; and ensuring that project contributors follow technical best practices. Your H1 performance did not consistently meet this standard.

The clearest example was model-based pUIC, where several foundational technical questions were resolved too late:

1. Serving signal: The serving track advanced before the correct user-sequence signal had been identified and adequately tested or vetted. This contributed to approximately one month of delay.
2. Modeling design: Modeling implementation was delegated to an ATG partner without sufficient visibility into the technical details. A substantive design discussion did not occur until June, when it became clear that the model was using only a subset of the interactions the group expected.
3. Embedding validation: The embedding predictions were not fully vetted before integration, contributing approximately another week of delay.

These were not simply under-communication issues as you noted in your H1 self-review. Broader communication might have surfaced the problems sooner, and more proactive communication is still expected. However, the underlying gaps were incomplete technical design, insufficient validation, and inadequate review of critical assumptions before rollout. Delegating implementation is appropriate at IC15, but the technical lead remains responsible for the quality and completeness of the overall solution. That means establishing a sound design, defining success criteria, understanding and reviewing delegated components, validating key assumptions and model outputs, and ensuring that the integrated system is production-ready.

In H2, I expect you to demonstrate a higher and more consistent technical bar by resolving critical data, modeling, evaluation, and serving uncertainties before rollout; producing and driving timely design reviews; validating offline and online behavior; and delivering maintainable, tested, and well-documented production solutions.

### Higher Levels of Accountability

The IC15 MLE role requires leading complex projects with minimal oversight: establishing milestones, managing dependencies, anticipating risks, adjusting plans when circumstances change, and driving commitments to completion. Your H1 performance showed significant gaps in this area.

As the technical lead for Retentive Recommendations during most of H1, you were accountable not only for reporting workstream status, but also for establishing technical direction, maintaining visibility into delegated work, identifying risks, supporting contributors, and driving the overall outcome.

That accountability fell short in several ways:

1. In model-based pUIC, critical technical uncertainties and design gaps were not identified and resolved early enough to protect the committed timeline.
2. Delegated modeling work progressed without sufficient technical visibility and review, allowing a fundamental mismatch in expected training interactions to remain undiscovered until June.
3. More than one team member reported that they did not receive sufficient clarity about their responsibilities or timely support when they were blocked.
4. The multi-embedding GPU rollout slipped by several months without the delay, underlying risks, and recovery plan being proactively surfaced from within the workstream.
5. Progress across these efforts required repeated prompting, follow-up, and management intervention rather than being driven independently.

At IC15, you are accountable for outcomes; providing updates or conveying the status of other contributors' work is not a substitute for personally driving the workstream's technical design, execution, risk management, and delivery. Following our discussion in late June, your Slack responsiveness improved, and I appreciate that adjustment. Responsiveness is necessary, but it is not the full expectation. End-to-end accountability means independently identifying what needs to happen, setting and maintaining a credible plan, finding risks before they result in missed milestones, supporting contributors promptly, and driving the work to production without repeated prompting. The same pattern shows in ME GPU serving: a rollout that passed launch review in 2025 slipped by several months without the slip being flagged from within the workstream. Owning a space means the problems in it are yours to find before they find us, and that is the standard we expect at IC15 regardless of role title.

Your 2025 performance and your frontier sampling work in Q1 demonstrate that you are capable of this level of ownership. The gap in H1 was sustaining it consistently. In H2, I expect you to operate with minimal oversight, maintain clear ownership of both your own work and delegated components, surface risks promptly with proposed mitigations, and deliver against your commitments.

## Goals for H2

Your H2 priorities are sustained hands-on impact, technical excellence, and end-to-end accountability.

1. Accountability for impact: across the entirety of your H2's work, you are expected to deliver launches that collectively deliver at least 0.2% SSv2 improvement attributable to your work.
2. RecGPT impact: While assigned to RecGPT, lead at least two material launches end-to-end. End-to-end ownership includes problem definition, design, implementation, evaluation, productionization, experimentation, results analysis, and the resulting ship, iterate, or stop decision.
3. Engineering excellence: Deliver production-ready work that is thoroughly designed, tested, vetted, documented, and monitored. Identify technical risks early, manage dependencies, and deliver committed milestones without repeated follow-up or escalation.
4. Team-process contribution: Own the auditing of the team's workflow on-call processes, identify recurring manual work and operational gaps, draft a proposal on how to improve, obtain sign-off from key team members, and land the automation steps.
5. Execution and communication: Provide a concise weekly written update covering completed work, upcoming milestones, risks, and changes to scope or dates. Surface risks when they become known, together with a proposed mitigation and updated plan.

These are IC15-level expectations and remain applicable regardless of project assignment. As organizational priorities evolve, you may be assigned work outside RecGPT. The expectations for independent ownership, technical quality, and sustained delivery will remain unchanged.
