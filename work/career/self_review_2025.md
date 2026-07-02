# 2025 Self-Review (year-end, rating cycle) — as submitted

> Saved to repo 2026-07-02 (pasted by James during the H1 2026 self-review drafting session). This is the canonical template for future review cycles: summary line → bolded themes → evidence bullets in Q1; learnings with "going forward" operating changes in Q2; team goals + personal improvement areas in Q3. The H1 2026 cycle dropped Q4-Q6 (inclusion / strength / opportunity) and carries no rating.

---

**Q1: Looking back, what were your key accomplishments and what was the impact on team, function and/or Pinterest priorities? Consider your goal outcomes, REG, our values and the overall impact you had on team, function and/or Pinterest priorities.**

In 2025, I led HF Candidate Generation to become a more durable, high-leverage organization. I did this by growing the team and scaling its leadership bench, strengthening technical and operational foundations across retrieval and early-funnel systems, and delivering significant metric and efficiency gains. We also amplified impact beyond our scope by enabling important initiatives in Growth/Activation and Notifications ML.

**Built a much stronger team and leadership bench**

A major focus in 2025 was ensuring the organization could deliver with higher autonomy and clarity. When I joined in late 2024, team morale was quite low due to a combination of factors (Sept 2024 EVS scores 7.1 engagement, 6.8 management support, 5.9 recognition). I took over the team from the EM at the time, who reported to me. Through the course of 2025, I rebuilt the team structure and its leadership bench, grew the team size by 50%, all while substantially increasing the morale and technical vision of the team.

- With Dylan's help, I helped to transition Raymond (former EM of HF CG) into a better fit role of IC, where he is currently demonstrating higher performance and adding more value to the organization.
- I identified a small group of TLs (3 IC16s, 1 IC15), empowered them with technical area ownership and clarified swim lanes. This enabled a strong leadership bench and increased the org's overall capacity to take on more ambiguous and cross-cutting initiatives.
- I hired and onboarded 6 new engineers while improving the social-wellbeing, diversity, and inclusiveness of the team. Then I implemented a skills-focused coaching session for the team, and doubled down on better understanding of team members' career goals and matched these to business needs. These resulted in a substantial improvement in the overall sentiment (Mar 2025 EVS scores: 8.4 engagement, 9.8 management support, 9.4 recognition).
- I executed a re-organization of the 20 people group into 2 subteams which strengthened the execution focus of each area, improved ownership clarity, and cross-functional mapping with Product. As part of this change, I also vetted and successfully transitioned Bowen Deng as a first time Engineering Manager. We maintained high team morale (Sept 2025 EVS scores: 8.4 engagement, 9.2 management support, 8.8 recognition) and sustained a high performance culture.

**Achieved substantial topline Impact and strategic outcomes**

The team delivered +2.1% SSv2 and +0.33% WAU through a portfolio of retrieval modernization, funnel efficiency, and quality investments.

- We shipped Conditional Learned Retrieval framework as well as multiple meaningful improvements, enabling this to be the foundation for replacing most heuristic CGs on HF and for further scale.
- We shipped multi-Embedding Learned Retrieval which grew to be the most performant CG, and the technique was also recognized at KDD 2025 as an accepted paper.
- We landed L1 Utility for the first time in Core, setting a strong foundation for further funnel efficiency improvements to come.
- We also established much stronger foundations for the Light Weight Scoring model via GPU serving and improved offline and online metric correlations that will accelerate experiment velocity in the L1 modeling space.
- The team also delivered ~$3M/year in annualized cost savings by simplifying and consolidating the stack (efficiency + deprecations + migrations), increasing iteration capacity and reducing KTLO drag. Along the way we deprecated dependence on legacy services: pinnacle2, topics/interest service, bestpins3, as well as greatly reduced dependencies on Apiary.
- I set the direction, aligned with cross organizational peers, and oversaw the technical execution plan for Retentive Recommendations, a cross-functional initiative with the UU team, HF Blending team, Product and PADS. Together, we converted an ambitious high level product strategy into a technical foundation spanning signal generation as well as major stages of the recommendation funnel, as well as a clear measurement plan for use-case expansion. Within 6 months I oversaw the multi-team execution leading to shipped/queued launches across Retrieval/Ranking/Blending, including one that drove +0.14% DAU, +0.11% WAU, and +0.1% SSv2 Unique Users.

**Advanced company-wide outcomes outside of my team's scope**

- My team and I enabled the critical NUX Revamp project to be launched while still also achieving the 1% NUX 14d WAU Growth goal established jointly with the Growth Activation team.
- My team and I enabled critical Growth outcomes: I aligned with Notifications leads Ravi Kiran Holur Vijay Tingting Zhu to have Bella Huang work closely with their engineers on improving the Notifications ML stack as well as ramp up their new tech lead. This resulted in 5 launches with cumulated expected gain of 1.5M WAU, as well as stronger technical collaborations between the teams which facilitated fast progress later in the half when establishing the Unified Personalization Platform retrieval experiment.
- I served as the Organizing Committee Chair for ML Day 2025 to increase Pinterest's ML brand and recruiting pull. This led to a very successful event with 2000+ external attendees. Chuck R (VP, ATG) explicitly recognized the event as an important showcase and a meaningful factor in candidate decisions to join Pinterest.
- I also improved many operating mechanisms on the broader HF team. I clarified the operational swimlanes between HF relevance and Core Serving Infrastructure, Core Retrieval Infra, Core Machine Learning Infra, as well as drove ideation and cross-org alignment on stabilization efforts to reduce friction and increase debuggability during incidents and outages. I helped to instigate, organize, and mobilize several Homefeed Repin drop investigations that ended up being root-caused eventually, and through the process, guided the team to add better monitoring and debugging dashboards for HF. I also started working closely with Konish to improve the Disco Weekly Ops monitoring.

**Q2: Looking back, what were some key learnings and/or missed opportunities that you encountered? How can these be used to drive greater impact in the future?**

Learning #1: In a few cross-org threads, my bias for speed and clarity sometimes outpaced the amount of shared context in the room—especially when priorities, resourcing, or ownership boundaries were still fluid. Even when my intent was to reduce ambiguity, moving too quickly (or sounding too certain) can unintentionally reduce trust, trigger resistance, or create rework because partners don't feel fully looped in early enough.

Going forward, I'm tightening my operating model for ambiguous cross-team work so we preserve speed and increase alignment: pre-wire key stakeholders in smaller forums, explicitly separate facts vs hypotheses, and drive decisions via short written pre-reads that surface options/tradeoffs and invite input before a decision date. This should reduce political friction, prevent late surprises, and increase the pace at which multi-org efforts convert into shipped outcomes.

Learning #2: Because I hold a high bar and can unblock quickly, I sometimes became the integration point across multiple initiatives—especially when the work was high-stakes or cross-team. The downside is that it can unintentionally signal the org can't run without me, and it limits throughput because decisions, narrative, and quality control become overly centralized.

Going forward, I'm shifting more intentionally from "solver/integrator" to "setter of constraints + builder of mechanisms." That means empowering TLs and EMs to own end-to-end execution and the narrative artifacts, while I keep a small number of high-leverage review gates. This creates a more scalable org, increases leadership bench strength, and frees my time for strategy, cross-org alignment, and longer-horizon investments.

**Q3: Looking ahead, what are your/your employee's goals for the first half of the year?**

Lead Team on the following:

- Further consolidate the stack (UPP direction): drive consolidation work that moves us toward a unified personalization platform, including continued CLR adoption to replace heuristic CGs.
- Achieve ambitious SSv2 goals: scale up Retrieval / LWS model capacity (quality + efficiency) and progress Generative Recommendations (RecGPT) from prototype → measurable, production-ready milestones.
- Grow retention (WAU/MAU): execute the next phase of Retentive Recommendations with a clear proof plan (KPIs, guardrails, decision dates) and high-signal launches.
- Cost savings + user experience: expand business logic in L1 utilities, ship personalized budget tuning, and improve responsiveness & feedback loops so we can trade off cost/latency/quality with more control.
- Grow i18n ecosystems + content freshness: strengthen merit-driven distribution and advance the content exploration funnel to improve freshness/coverage while protecting relevance.

Personal improvement areas (2):

- Pre-alignment + exec communication: be more deliberate in ambiguous cross-org contexts by pre-wiring stakeholders early and using consistent framing (facts → options → lean → invite input → decision date) to reduce friction and rework.
- Scale execution through leaders: ensure major workstreams are owned end-to-end by TLs/EMs with clear artifacts (decision docs, measurement plans, launch postmortems), with me operating at review gates rather than as the integration bottleneck.

**Q4: How have you/your employee contributed to creating an inclusive workplace culture?**

In 2025, I focused on creating an inclusive, high-trust culture of the HF Candidate Generation where people feel respected, heard, and able to do their best work.

- Built belonging through fair, transparent team mechanisms: I set clear norms around respectful debate and decision-making, ensured roles/expectations were explicit (especially during reorg/onboarding), and made recognition and feedback more consistent so newer and quieter voices weren't disadvantaged. I also prioritized high-quality onboarding and mentorship to help new hires integrate socially and technically quickly.
- Coached leaders to be more inclusive (scaling impact): I explicitly coached TLs/EMs on inclusive leadership behaviors e.g., facilitating meetings to balance airtime, actively soliciting dissenting perspectives, giving feedback in a way that is candid but respectful, and watching for "default ownership" patterns that can unintentionally sideline others. The goal was to make inclusion a shared leadership standard, not something dependent on me.
- Actively addressed issues early: When tension or misalignment arose (especially in cross-functional settings), I worked to separate facts from stories, reduce blame, and "debug the system, not the person," which helped maintain psychological safety while still holding a high bar.
- From EVS, we see the non-discrimination scored 9.2, improving +1.4 since Sep 2024, and landing +1.3 above benchmark (7.9).

**Q5: Top Strength: Drives Results**

I consistently create clarity on what success looks like and mobilize the org to deliver quality outcomes, even when the work spans multiple teams and technical domains. (This maps to the "Drives Results" expectation of setting a clear definition of success, inspiring velocity, and delivering a track record of outcomes—not just activity.)

Examples:

- I led HF Candidate Generation to deliver measurable product outcomes—+2.1% SSv2 and +0.33% WAU (~+1.1M WAU)—while also driving ~$3M/year in annualized cost savings through consolidation, deprecations, and efficiency work.
- I didn't treat these as isolated launches; I ran a portfolio across modernization (learned retrieval foundations like CLR / multi-embedding), consolidation (deprecations of legacy systems), and scaling (platformization that enabled other surfaces), which is why the impact was both material and durable.
- I also drove execution that enabled broader company priorities (e.g., NUX/Growth and Notifications) rather than optimizing for Homefeed-only wins.

**Q6: Top Opportunity: Manages Ambiguity**

My biggest development edge is to keep my speed and decisiveness while increasing early alignment and "felt collaboration" in ambiguous cross-org situations (especially when priorities/resourcing/ownership boundaries are still fluid). This maps directly to the "Manages Ambiguity" expectation: keeping strategic initiatives moving forward despite incomplete information—without creating avoidable rework or friction.

Examples:

- In a few high-stakes cross-team contexts, I've seen that my default of moving quickly to reduce ambiguity can sometimes land as "already decided," which can trigger partner resistance or require extra alignment cycles later.
- I have already provided discussions in earlier sections on how I plan to address this opportunity going forward.
