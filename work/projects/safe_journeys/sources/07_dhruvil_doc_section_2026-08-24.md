# Source 07 — Dhruvil's section added to the joint CQ doc (Mon 2026-08-24)

> **Source of record.** Pasted by James 2026-08-24. Dhruvil Deven Badani wrote a full review section directly into the joint framework doc (`joint_framework_v1.md`) — summary, observations, and eight suggested action items. Follows Qinglong's 8/21 commitment (source 06: *"I will add Dhruvil's ideas to the doc and tag relevant folks"*). Dhruvil went past ideas and wrote a **review + workplan**.
>
> **Timing:** lands Monday 8/24. Dylan/Andrew review is today; **Bill Ready deliverable Wed 8/26; Bill review Fri 8/28** (Andrew's slot). Tab 2 is still headers-only per D7.

---

## Dhruvil's section, verbatim

**Summary**

> No concerns with running experiments to gather data and learnings. However, many of these things will need to be addressed before LR approval / shipping.

**Observations**

- We should set success criteria & goals, so that we know when we've done enough.
- The prioritization of interventions today only considers effectiveness to the genAI problem. The prioritization should also consider funnel efficiency + most importantly, risk.
- GenAI still seems like a personalization problem, as compared to safety. We should therefore lean towards more principled solutions. Adding interventions late in the funnel can act as a mask/bandaid for deficiencies earlier in the funnel.
  - We have many stages of personalization before blending: retrieval, LWS, ranking — they should be able to, in theory, figure out if a user likes AI generated content or not.
  - We should bias towards more principled and funnel-efficient approaches, not just what solves the problem in the short term most effectively.
- The primary risk introduced by interventions in blending is: **hurting the correlation of L2 model's offline evaluation with online performance.**
  - The more re-ranking we add after L2, the lesser the correlation.
  - HF L2 is one of the few models with high offline-online correlation.
  - A hit to the correlation will affect velocity and hence achievability for WAU/SSv2 goals.
  - With UPP, HF offline evaluation is often the bellwether for all surfaces since it is the most accurate. So, a hit to HF L2 offline-online correlation can affect other surfaces' WAU/SSv2 progress too.
  - What's even riskier is that changes slated to drive X% impact to WAU/SSv2 can drive X*K % (K<1) if the changes after L2 in fact reduce the improvements coming from L2. And we have no way of knowing this since we cannot simulate the lack of blending interventions offline once they are shipped.
  - There is no counterfactual here, hence we must have measurement.
  - There is no counterfactual here, hence we must be extremely careful. Else we risk being in a position where we have to make a call between genAI and WAU/SSv2 goals.
- By default, late-funnel experiments can overlap the impact from early-funnel experiments. We should run combined experiments to see the additional efficiency of late-funnel solutions on top of early funnel solutions.
- **Slate problem does not necessarily mean the problem or the fix is in blending.**
  - The slate can look bad even if L2/blending are fine. This happens if the input to L2/blending has a high load of genAI content. The slate is bound to look genAI-heavy then.
  - We should do a funnel analysis and then solve where the problem(s) actually are.
- Based on the genAI score distribution, it is possible small changes in genAI score can cause large shifts, particularly in the blending layer.
  - We should measure the amount of re-ranking compared to control, since that can introduce risk to L2 offline-online correlation.
  - genAI score calibration becomes a must.
  - We should add some measures in blending to prevent over-sensitivity to the genAI score.
- We should prioritize model interventions which include lower debt. Some of which seem to have been successful on notifications from Akshay Iyer and the team.
  - For LR, LWS, L2: **margin loss** to increase the gap in core between non-genAI positives and genAI positives. Worked well on notifications LR per Akshay.
  - Mainly for LR (and LWS if it uses in-batch negatives): using **positives for low-quality items (as marked by VLM) as in-batch negatives.** Worked well on notifications LR per Akshay.
  - Look at calibration error rate for HF L2 for different genAI score buckets. If need be, consider using genAI score as a feature in the calibration layer.
- **L2 model ideas, including using the new genAI signal.**
  - Try the new genAI signal in sequence modeling.
  - If we didn't try the genAI score in the impression sequence, we should. That can help debias the model.
  - Evaluate calibration error rate for pins in different buckets of genAI score.
  - Add L2 offline eval broken down by different buckets of genAI score.
  - Margin loss as above, to incentivize non-genAI positives over genAI positives in general.
  - Use the genAI sequence & candidate signals to come up with a more personalized affinity loss.
- **Questions on the early-funnel**
  - Do we know which CGs, if any particular ones, are particularly responsible for high genAI load? Can we run an affinity analysis to find the CGs that are sending genAI candidates even to users who do not want them?
  - Should we consider controllable distribution in L1 utility? That can solve the problem to a large extent for all the parts before L2/blending.

**Suggested action items**

| # | Owner(s) as written | Item |
|---|---|---|
| 1 | [PADS?] | Set up success criteria & goals |
| 2 | [PADS?] | Funnel analysis to understand where the problem(s) lie |
| 3 | [PADS, in progress?] | Add genAI prevalence to Helium |
| 4 | Zisis Petrou · Dhruvil | Set up measurement for `correlation(offline eval, online performance)` for HF L2 |
| 5 | **James Li** · Qinglong · Dafang · Dhruvil | Revisit priorities to consider funnel efficiency + WAU/SSv2 risk, not just genAI effectiveness |
| 6 | **James Li** · Dafang | Answer the early-funnel questions — particularly whether we can control the load entering L2 |
| 7 | **James Li** · Dafang · Dhruvil | Figure out how to run blending experiments on top of L1 experiments, to get marginal impact of late-funnel interventions. *"This would imply that the early-funnel interventions need to be prioritized."* |
| 8 | Sameer Jain · Dhruvil | Follow up on HF L2 model interventions |
| 9 | Rahul Goutam · Dhruvil | Find PoCs for HF blending |
| 10 | **James Li** | Follow up with the HF LR and LWS teams on model interventions |

---

## Leo read (2026-08-24)

### 1. What actually happened: the criteria moved, and the work moved with them

The section is **80% correct and 100% consequential.** The technical content is largely right and much of it is already in the doc. The consequential part is structural, and it is two moves stacked:

**Move A — a new prioritization rubric.** The doc today ranks levers by effectiveness against the problem. Dhruvil installs a three-axis rubric: *effectiveness × funnel efficiency × risk*, "most importantly, risk." Whoever sets the criteria sets the priority stack. The rubric is defensible on the merits — and the risk axis it installs (**HF L2 offline-online correlation**) is a quantity that only his pillar can measure or adjudicate.

**Move B — the work relocates upstream.** "Do it as early in the funnel as possible" moves the build into James's pillar (retrieval, CGs, LWS, L1 utility) while blending — Dhruvil's pillar post-reorg (Rahul Goutam + ~5–6 MLEs) — becomes the thing to be protected from intervention. Item 7 says the quiet part in writing: *"This would imply that the early-funnel interventions need to be prioritized."*

**The asymmetry in the action-item table is the tell.** Four of ten items name James Li — including the three genuinely open-ended ones (revisit priorities, answer the early-funnel questions, follow up with LR and LWS). Dhruvil appears on six items, always as the second name, never as sole owner, and the two items nearest his own turf are routed to his report and his neighbor (Rahul, Sameer) with him pairing. **James was assigned the work; Dhruvil was assigned the review.** Add the summary's framing — *"many of these things will need to be addressed before LR approval / shipping"* — and the section functions as a **launch-review gate written in advance.**

This matches his documented style (stakeholders §3): *repetition of one load-bearing fact without stating its implication.* The offline-online correlation fact is repeated five times; the implication — "blending interventions should not ship without my team's clearance" — is never stated, so it never has to be defended. Recognizing the pattern is a Leo read. **It stays in the repo. It is never said in a room.**

### 2. What he is right about — concede fast, loudly, by name

These cost James nothing and buy back the pen:

- **Success criteria & goals are genuinely missing.** The doc has a 12-week shape (§8) but no "when have we done enough" for the genAI instantiation. Real gap, and the biggest one.
- **Funnel analysis before intervention.** Correct, and it is the doc's own §2 diagnosis logic applied one level down.
- **Slate problem ≠ blending problem.** Correct, important, and it strengthens §4's "composition upstream, precision downstream" framing rather than undercutting it.
- **Combined L1×blending experiments for marginal impact.** Correct — and it is *James's* upper-funnel argument in stronger, measurable form.
- **The model-intervention menu is excellent** (margin loss; VLM-flagged positives as in-batch negatives; genAI score in the impression sequence; calibration error by genAI bucket; offline eval bucketed by genAI score). Low-debt, with Notif proof points from Akshay. These **strengthen §5**, which is James's own training-time push.
- **genAI score calibration is a must.** This is already §7 of the doc, CQ-owned, on the critical path. He is re-deriving James's section — say so warmly, and that is itself a claim to the pen.

### 3. Where it needs a counter — three hard facts, all non-political

**(a) "All upstream" is not currently available for genAI — the signal is domain-level and L1 cannot consume it.**
This is the decisive fact and it comes from CQ's own doc, not from James. Source 04, Option 1A-i cons: *"Image-level only today. L1 utility cannot consume domain/landing-page-level signals (**GenAI-domain**, DQv4)."* And CQ's own L2-preference rationale: *"The majority of quality signals are domain/landing-page-level (GenAI-domain, DQv4, link quality), which L1 cannot consume today."*
So for **genAI specifically** — the subject of the entire section — the upper-funnel-first prescription hits a capability gap. The fork is: either **L1 gains domain-signal capability (a build, needing a date and an owner)**, or genAI enforcement necessarily lives at L2/blending in the near term. Dhruvil's section does not acknowledge this fork. Naming it is technically decisive, factually sourced to CQ, and carries zero territorial charge.

**(b) The washout argument and the dilution argument are the same phenomenon — and both resolve to "make L2 quality-aware."**
CQ's position (source 04): an engagement-only L2 *washes out* L1 demotion. Dhruvil's position: post-L2 blending *dilutes* L2 gains (the X*K argument). These cannot both be used as vetoes on opposite ends of the funnel — they are one fact seen from two sides: **wherever the quality objective is absent, the layer that lacks it reverses the layer that has it.** The answer both arguments converge on is the doc's §5 spine: put the quality objective *into* the model, so there is nothing to wash out and nothing to override. Dhruvil's own model-intervention menu is exactly that. **His section is an argument for §5, and it should be integrated there as one.**

**(c) Risk must be a measured budget, not a direction.**
Taken literally, "any re-ranking after L2 degrades correlation, and correlation protects WAU/SSv2 velocity" argues against *all* post-L2 enforcement in perpetuity — including the racy filtering and diversity rules already in production. It needs a **magnitude**: correlation degradation per unit of re-ranking, so there is a budget that can be *spent*, not merely defended. That is precisely his own item 4 (Zisis). Support it enthusiastically — and hold it to producing a number.

**(d) The "no counterfactual" claim is false, and the doc already owns the fix.**
*"We cannot simulate the lack of blending interventions offline once they are shipped, hence no counterfactual."* There is one: a **holdout**. §7 already carries the ε hold-back of suppressed content and the stack-level retention holdout. A blending-intervention holdout gives exactly the counterfactual he says doesn't exist. Offering it converts his strongest rhetorical point into an argument for James's own instrument.

### 4. The real threat to the artifact

The doc's value to James is that it became **the org's planning surface** (Qinglong, 8/21: *"James's doc is a very good starting point"*) — that is what earned the Qinglong anointment and backstops the Dylan CQ/T&S lead grant. The threat is not Dhruvil's content; it is the doc **degrading into stacked author blocks** — James's framework, then Qinglong's additions, then Dhruvil's review appended at the end. A doc with three appended sections has no author.

The counter is not gatekeeping. It is **doing the editorial work nobody else will**: fold Dhruvil's section into the existing spine rather than let it sit as a block. **Whoever integrates owns the frame.** It is the highest-leverage move available and it is cheap.

### 5. Timing

Bill deliverable Wed 8/26, review Fri 8/28. If the section goes to the exec tab raw, Tab 2 inherits (a) an action-item list reading "James Li owes four answers" and (b) a story that genAI prioritization is unsettled and risky — the opposite of D1/D7's "timelines are the centerpiece."

Note also that the section **implicitly answers §9 decision #1** (relative priority: genAI vs. teen safety) by loading genAI with a full workplan, without the leadership call having been made. That is scope creep into a decision James deliberately escalated, and it should be pushed back to §9 rather than absorbed.

**The D10 precedent applies.** When topic 3 wasn't ready, James chose an honest "not yet" over knob-turning dressed as design — and that decision earned credibility. Same move here: Tab 2 presents the **framework + the teen-safety timeline**, with genAI as the second instantiation **gated on the funnel analysis and the success criteria**. Consistent, honest, and it converts Dhruvil's two best asks into James's own gate.

---

## Ranked next steps

**1. Today, in the Dylan 1:1 — use the section as the price tag on the prioritization ask.** (Cheap, time-critical.)
Prep §2 already asks Dylan to name what CQ displaces. This section *is* the concrete answer: four action items with James's name, three open-ended, plus a launch-review gate. Bring it as evidence, not as a complaint. Also worth her read: whether the genAI workplan proceeds before §9 decision #1 is called — that is her escalation to make, not James's to absorb.

**2. Before Wednesday — integrate, don't append.** (Highest leverage.)
The editorial pass that folds the section into the spine:
- **New §0/§4.0 — success criteria & goals for the genAI instantiation.** His #1 observation, a real gap, credited to him. Criteria written now are criteria James wrote.
- **§4 — adopt the three-axis rubric (effectiveness × funnel efficiency × risk) and *apply* it** to the existing lever list. Applying the rubric is the act of ownership.
- **§5 — fold in the model-intervention menu** (margin loss, VLM-positives-as-in-batch-negatives, genAI in impression sequence, bucketed calibration + bucketed offline eval), credited to Dhruvil/Akshay with the Notif proof points. This is the section's best material and it reinforces James's own push.
- **§7 — offline-online correlation as a named measurement requirement with a budget**, paired with the existing ε hold-back; plus the blending-intervention holdout as the counterfactual.
- **§8 Phase 1 — funnel analysis + genAI prevalence in Helium** as weeks 1–4 measurement tasks.
- **§9 — push the genAI-vs-teen-safety sequencing back where it belongs** (decision #1), rather than letting the section resolve it silently.
- **§10 — the two early-funnel questions with James as owner and a date**, so they are scoped rather than open-ended.

**3. Answer the two early-funnel questions properly — this is where James wins.**
- **(a) CG-level genAI load + affinity analysis.** Cheap, on James's turf, and it doubles as the funnel analysis (item 2). This is the single best thing James can put on the table this week: it converts him from "owes four answers" to "brought the data that settles the prioritization."
- **(b) Controllable distribution in L1 utility.** Largely already the doc's P0 (density control at L1, §4/§8). Answer: *yes, it's the P0, here is the design — and here is the constraint*: genAI-domain is a **domain-level signal L1 cannot consume today** (fact (a) above). That constraint is the honest limiter, and it is what keeps some L2/blending work legitimately in scope.

**4. Propose the combined-experiment design rather than receive it.**
A 2×2 factorial (L1 intervention on/off × blending intervention on/off) yields the marginal-impact number, the correlation delta, *and* the counterfactual in one design — answering three of his observations at once. Item 7 names James first; proposing the design is owning it.

**5. Coordinate the L2 PoC, don't claim it.**
Qinglong's open ask (source 06) puts "HF to identify an L2 PoC" on James, while Dhruvil is staffing his own side (Rahul for blending, Sameer for L2 model). Per prep §2, get Dylan's read before answering Qinglong. L2 is Dhruvil's pillar — coordinate the pick with him.

**6. One message to Dhruvil, before the section hardens.**
Short, warm, "us vs. the problem" — his S/C profile wants Safety and Partnership, and the final call on his own turf:
- Concede by name the four things he's right about (success criteria, funnel analysis, slate≠blending, combined experiments) and adopt the three-axis rubric outright.
- Note that calibration is already §7 and the model interventions are going into §5 — merging, not appending.
- Put the two forks on the table as questions, not positions: the **domain-signal capability gap at L1** (so "all upstream" needs a build with a date), and **correlation-as-budget** (his Zisis measurement, held to a number).
- Offer the **blending holdout** as the counterfactual.
- Ask him to own the one thing only he can: the magnitude of correlation degradation per unit of re-ranking.

**Tone discipline (Karen watch, 8/22 flashpoint self-review):** James's documented pattern is buying closeness with intel rather than judgment, and the live watch is that dislike-driven moves toward Matt/Dhruvil reopen the XFN-patience narrative. Every artifact here must read as **technical synthesis, never territory defense.** No sentence implying Dhruvil is protecting his org may exist anywhere near the doc, the Slack thread, or the Dylan conversation.
