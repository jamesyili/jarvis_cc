# Yuke Yan — H1 2026 Performance Feedback (FINAL draft, James, 2026-07-31; rev. 2026-08-08)

> **Status:** James's final draft, logged verbatim 2026-07-31; **revised 2026-08-08** after the verbatim peer-feedback file landed (entries dated 7/28–8/03). Next step: ER pre-review, then delivery week of 8/10 (spaced from the Aug 5 announcement, separate day from Bella's). Supersedes the working draft at `work/people/yuke_h1_2026_review_draft.md` for the feedback text itself; that file retains the ER-side context appendix (self-review transcription, claim map, timeline) and the Workday paste blocks (**re-derive those blocks from THIS text before submission — they still reflect the old v2 letter**).
>
> **2026-08-08 revision (three surgical changes + copyedits):** (1) The "minimal across the entire quarter" claim restated from *absence* to *bar* — Zelun's verbatim peer entry ("training different variations of PS-pUIC candidates, debugging experiment issues, implementing Unity side changes") directly contradicted the absolute phrasing and it was the doc's most attackable sentence. New wording pre-cites the contributions and holds the IC15 standard. (2) Strengths-acknowledgment paragraph added to Key Accomplishments so the review visibly metabolizes the glowing peer entries (Xiangyi, Zelun, Roderick) — closes off "did you even read my peer feedback?" (3) One theme-level (no-name) reference to the critical peer themes (Anna: socialize designs earlier / de-risk alternatives; Yidi: reactive discover-and-fix, wants upfront risk assessment) added to Technical Excellence — these independently corroborate §2/§3; by-name mapping stays in ER notes only, never in this doc. Plus: mid-point checkpoint (~Sept 30) added to H2 goals; 7/31 copyedit flags (1)–(3) resolved in text.
>
> **Pre-ER fix list (remaining):** Goal 4 (on-call process audit) collides with Bella's team-leadership goal — differentiate scope across the two docs (see her final's fix list).

---

## Key Accomplishments

Thank you, Yuke, for your contributions in H1 2026. You performed on par with IC15 expectations in Q1, but your delivery and ownership declined materially in Q2.

Leading frontier sampling from design through production launch in Q1, while also developing a junior engineer on the project, was a good example of IC15-level technical ownership since the problem was ambiguous and you were very hands-on as part of coming up with the solution. During this time, you also helped ramp up Chuxi and Yidi on Retentive Recommendations (RR) as their TL. In Q2, you began contributing to RecGPT, continued to TL the RR efforts, and supported Hanlin while he launched multi-embedding GPU serving.

Your peer feedback this cycle consistently recognizes strengths in cross-functional coordination, driving momentum across teams, and creating meaningful ownership space for the engineers you lead — I see these too, and they are real assets. As covered below, however, the primary measure of impact at IC15 remains the technical work you personally own and drive end-to-end, and that is where the gap lies.

The IC15 MLE role requires independently taking ambiguous ML problems, designing sound solutions, managing dependencies and technical uncertainty, and delivering end-to-end to production with minimal oversight. It also states that, while engineers at this level begin taking on leadership responsibilities, hands-on technical work remains the primary measure of impact. What I observed in Q2 for RR is that most of your activities consisted primarily of coordinating communication between myself and other RR leads to the other engineers. Your own hands-on contributions in Q2 — while present, including experiment support, model training variations, and serving-side changes — were fragmentary and did not constitute the independently owned, end-to-end technical delivery that the IC15 role requires as the primary measure of impact. In addition, within the workstreams you led during Q2, critical technical uncertainties were not resolved early, delegated components were not sufficiently understood or vetted by the team members you led, milestones slipped without timely mitigation, and delivery required repeated prompting and intervention by me.

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

These were not simply under-communication issues as you noted in your H1 self-review. Broader communication might have surfaced the problems sooner, and more proactive communication is still expected. However, the underlying gaps were incomplete technical design, insufficient validation, and inadequate review of critical assumptions before rollout. This is consistent with themes in your peer feedback this cycle regarding earlier socialization of designs, upfront risk assessment across the end-to-end pipeline, and de-risking alternative approaches before committing to a methodology. Delegating implementation is appropriate at IC15, but the technical lead remains responsible for the quality and completeness of the overall solution. That means establishing a sound design, defining success criteria, understanding and reviewing delegated components, validating key assumptions and model outputs, and ensuring that the integrated system is production-ready.

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

We will review progress against goals 1 and 2 at a mid-point checkpoint on or around September 30, including launches completed or in flight, measured or projected SSv2 impact, and any risks to the remaining H2 timeline.

These are IC15-level expectations and remain applicable regardless of project assignment. As organizational priorities evolve, you may be assigned work outside RecGPT. The expectations for independent ownership, technical quality, and sustained delivery will remain unchanged.
