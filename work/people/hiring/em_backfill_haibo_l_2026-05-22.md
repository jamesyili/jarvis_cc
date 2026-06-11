# EM Backfill Candidate: Haibo L

**Interview rounds:** 2026-05-22 (initial — James; 4 of 5 questions covered, ran out of time on Q5)
**Role:** Frontline manager — Homefeed Candidate Generation (Bowen backfill at frontline altitude). 8–9 person ML team, active performance case (Charlie's CPP in execution), promo candidate in-flight (JJ IC16 cycle), growth plan to 12–15 over next year.
**Recommendation: Lean Yes. Move to onsite — but with targeted probes on the three soft spots below.**

---

## Summary

Currently EM on Alexa AI's offline ML experimentation platform — driving GPU efficiency across ~4K P5/P5EN GPUs and building the eval + training platform for science teams (incl. 3P model adoption: Qwen3, GPT-OSS, Llama4). Real scale, real platform muscle, real diagnostic-to-accountability arc shown in Q4. The standout signal is his Q4 stronger-TL example — specific, recent, complete (audited the stuck cross-team design, reframed the tech-debt-vs-deadline trade-off, packaged for leadership, locked in Q3 cleanup accountability). That's the strongest Q4 substance in this loop after Prashan. Three real gaps: Q2 disagreement story is essentially absent (same shape as Prashan's miss but more diffuse), Q3 perf-case framing skips the formal-plan concept entirely (worse than Prashan's flag — he never engaged with "doesn't belong on team" as a possibility), and his background is platform/infra rather than ranking-adjacent. Lean Yes is defensible because the energy frame, the scale, and the Q4 muscle are real — but converting to Yes requires onsite to resolve the perf-handling instinct and the CG-vs-platform problem-shape gap.

---

## Background

- **Amazon Alexa AI** (current) — EM on offline ML experimentation platform. Two-thirds of charter: drive GPU efficiency across ~4K P5/P5EN GPUs (consolidating per-team pools into unified pool with job prioritization, dispatch, logging — the operating cost framing is real and substantive). One-third of charter: ML platform for science teams — building eval pipelines, leaderboards, single-box offline inferencing, plus productionalizing 3P RL solutions and adopting Qwen3 / GPT-OSS / Llama4 (uplifted org from 1P-only Nova to 3P). 3 scientists dotted-line to him; partners with broader science team. No PM in org — Haibo plays PM hat across science manager partnerships.
- **Atlassian Growth** (prior) — ML-based personalization on user context + historical behavior, B2B side (signed-in users → organizational context + profile data). Left because team reorged into pure marketing GTM, drifted from ML.
- **Tenure / depth:** unspecified durations on each — get from recruiter.

**Self-stated what's-next:**
1. Cutting-edge ML tech (motivation for leaving Atlassian)
2. External-customer-facing business impact (current role is internal-customer only)
3. Big-bets culture + fast iteration (cited as reserved at larger companies)
4. Project that compounds personal growth — "if the particular project can generate great impact, it helps me advance in my career"

That energy frame maps cleanly onto this seat: cutting-edge ML + consumer-surface + Director-track project. The Atlassian exit story (reorged away from ML) is the cleanest signal here — he left a job he was no longer learning in, which is the right reflex.

---

## Strengths

- **Q4 substance is real and recent.** The agentic eval / cross-team design example is the strongest part of the interview. Two weeks ago: cross-team design discussion stuck — multiple solutions, no alignment, surfaced to leadership prematurely. Haibo's intervention: spent a week auditing the actual blocker, found the team was trying to minimize tech debt upfront (engineer-excellence reflex blocking time-pressed delivery), reframed the trade-off ("what if we accept some tech debt to unblock 60% functionality with a POC?"), built a one-pager for leadership, secured buy-in for one-month tactical work — AND held leadership honest by locking in explicit Q3 cleanup accountability. That's a complete diagnostic-to-reframe-to-package-to-accountability arc on a real recent situation. The accountability piece in particular ("we need to save one month at the beginning of Q3, otherwise this debt will accumulate and become a year's work") is mature managing-up muscle.
- **Real platform scale at Amazon.** 4K GPUs is non-trivial. The cost-optimization framing (peaks across teams adding up to low utilization → consolidate into unified pool) is correct and substantive. Job prioritization + dispatch + logging is a real platform surface. The 3P model adoption work (uplifting org from 1P Nova to Qwen3 / GPT-OSS / Llama4 with productionalized RL) is timely and high-value. Scale signal: comparable or larger than what JJ's pod operates on today.
- **Self-aware exit framing.** Atlassian → Alexa pivot was driven by "team reorged into pure marketing GTM and drifted from ML." That's the right reflex — leaving a job that no longer compounds the craft. If the same instinct holds at Pinterest, he'll stay engaged on the ML-substantive work, not drift into managing.
- **Holds leadership honest on follow-through.** The Q4 example explicitly notes he made leadership commit to the Q3 cleanup at the front, not at the end. That's the muscle for not letting tech debt accumulate — and the muscle for managing up against unrealistic timeline pressure without just absorbing the cost.
- **Conflict-de-escalating + transparent 1:1 culture.** "I always encourage them — if you have any direct feedback to me, this is the best one, the safe zone." That's a 1:1-as-trust frame, not 1:1-as-status. Combined with the public-disagreement-handled-offline instinct, it signals he won't surface team friction inappropriately upward.
- **Plays PM hat in absence of formal PM.** Current role has no PM; Haibo brokers requirements and priority with science manager partners. That cross-functional instinct will transfer to Pinterest's PM-partnership reality (Tim, Anna, etc.) — though needs to be tested for fit.
- **Adopted 3P open-source models in production.** Concrete recent technical decisions (Qwen3, GPT-OSS, Llama4) — he can talk about the state of the art and has been making consequential model-selection calls. That tracks for someone who will be partnering with Piyush and JJ on CG model evolution.

---

## Concerns / push on at onsite

### Q3 perf-case framing skipped the formal-plan concept entirely (LOAD-BEARING for this seat)

This is the most operationally specific concern. When asked about handling a performance case in the first 90 days, Haibo's framing was *entirely* "what's the knowledge gap, how can I support him." He never engaged with the possibility that the person doesn't belong on the team, never named formal performance plans, never named the manager's responsibility to make the call when support hasn't moved the needle.

That's a worse miss than Prashan's flag. Prashan at least said "I wouldn't give him a performance plan because of lose-lose dynamics" — he engaged with the concept and rejected it. Haibo didn't engage at all. Either the formal-plan tool isn't in his toolkit, or his instinct is so strongly toward "I can coach this person up" that the formal option doesn't surface.

Charlie's situation isn't that. Charlie is **already on CPP from 4/30**, completing pre-6/1. By the time a new EM lands, the perf plan is in execution. The seat needs someone who will *continue* executing a formal plan that's already in flight, in coordination with HRBP — not unwind it back into "let me diagnose the knowledge gap." This is the single most important onsite probe.

**Direct probe at onsite:** *"You inherit a team where one report is already on a formal performance plan that completes in three weeks. The diagnosis has happened. The HRBP is engaged. The plan was built with specific deliverables and missed milestones. What do you do?"* Test whether he can hold the line on the existing plan. If he reverts to diagnosis or wants to restart from coaching, that's the disqualifier for this specific seat.

### Q2 — no real disagreement story (he philosophized around it)

The Q2 prompt was about a moment where he and his manager saw things differently and how it played out. His response wove through:
- Generic preferences (good manager vs bad manager framing)
- Listening-first posture in larger orgs
- "I avoid public conflict — keep it self-contained"
- Vague reference to "one time my manager probably forgot to give me additional context and they kind of stopped me right in the middle"
- "We will sync up realignment and bring it offline"

He never described a substantive disagreement, never described holding a position, never described what was at stake. Either the story isn't there or his instinct is to file disagreements as "alignment failures" — which would track with the conflict-de-escalation pattern but would also signal that he doesn't surface enough heat upward when stakes warrant it. That's a Director-altitude problem in a seat that requires holding the line with Piyush (IC16), JJ (IC16 promo), and senior stakeholders.

**Direct probe at onsite:** *"Tell me about a specific time you and your manager actually disagreed on something material — a decision, a priority call, a person — and what you did. I want the moment where the two of you were in different positions, not the moment after alignment landed."* Test whether the disagreement story exists or whether the alignment frame is masking conflict avoidance.

### Background is platform/infra, not ranking-adjacent

Current Alexa work is **ML platform** — eval infrastructure, GPU efficiency, training platform productization. That's a real and substantive surface, but it's not consumer ranking. Different problem shape than CG (consumer retrieval at scale, online personalization, latency-sensitive serving, recall/precision trade-offs, candidate generation as the funnel's upstream stage). Atlassian Growth (B2B personalization) is closer but it's older and B2B-shaped.

For comparison: Vaidehi is CG-native. Prashan is ranking-adjacent (Instagram late-stage ranking is downstream of CG but same broad neighborhood). Haibo is further afield — he's coming from the platform side of ML, not the modeling side. He can talk about Qwen3 / GPT-OSS / Llama4 selection, but he hasn't been the one driving consumer ranking-model evolution in production. The ramp curve here is steeper than Prashan or Vaidehi.

**Onsite probes:**
1. *"Walk me through how you'd think about candidate generation vs. ranking — what's different, what skills do you need to develop, what's your current mental model of the funnel."* Test whether he understands the problem-shape shift.
2. *"What's the most operationally consequential ML modeling decision you've made yourself in the last 12 months — not platform decisions, the modeling side."* Test whether the modeling muscle is current or whether he's drifted into platform-only.

### Long-winded delivery / weaves between threads before landing

Across all four answers, Haibo took 2–4 minutes to land each point. He wove between threads, doubled back, restated. Some of that is just nerves on a first round and the verbal-thinking style — but the seat involves real Director-altitude executive presence work (1:1s with Dylan, peer-EM coordination with Dhruvil, cross-functional with Faisal-side / Andrew-side, and over time direct VP exposure). Tightness matters here. Worth flagging the delivery-style question at onsite — does it tighten under pressure? Can he land a one-sentence headline before unpacking? Dylan in particular will notice this.

### What does "what would you want me to see at 90 days" tell you?

His answer to that part of Q3 was process-shaped: "team continues to operate, clarity, tracking, auditing, stakeholders know where we are." That's the cadence-output frame. Vaidehi answered with an impact-output frame (specific E6 person, specific scope expansion, specific durable outcome). Prashan answered with retention + scope-expansion of high performers. Haibo answered with "things don't break and stakeholders know where we are" — which is the *table stakes* outcome of a first 90 days, not the *target* outcome.

This is the same gap as the Q2 / Q3 perf-case patterns: he defaults to safe / status / process / support framing rather than impact / position / outcome framing. Onsite needs to test whether he can articulate what *winning the seat* looks like — not just "things continue to operate."

### Wanting external-customer-facing impact — restlessness or alignment?

He explicitly said current internal-customer scope leaves him missing external-customer-facing work. That's a fit signal for this seat (CG is upstream of every consumer surface). But probe: is the desire to escape internal-only a healthy ambition match, or is it a pattern of restlessness that could recur when CG gets internal-feeling work (instrumentation, infra, on-call)? Worth knowing.

---

## Fit for this specific role

This seat inherits:
- An active performance case (Charlie's CPP) requiring decisive handling under HRBP coordination, with the plan already in flight
- A promo candidate (JJ IC16 cycle) needing active advocacy under calibration politics
- Daily boundary-setting against surface-team pressure
- Direct people-leadership of an 8–9 person team growing to 12–15
- Daily partnership with strong TLs (Piyush IC16, JJ IC16, Devin, Yuke) under Director-altitude political conditions

**Muscle map:**

- **Perf case:** **Major concern, hard probe required.** Q3 framing skipped formal-plan concept entirely. Worse than Prashan's flag. If onsite probe shows he can hold the line on an in-flight CPP, this resolves. If not, this is the operational disqualifier for this specific seat.
- **Promo candidate:** **Adequate but generic.** Audit + state-check + data needed is correct shape. Less specific than Vaidehi's E6 ESR story or Prashan's retention + scope-expansion frame. The instinct is fine, the muscle is unproven.
- **Boundary-setting:** **Good implicit signal from Q4** — he held leadership honest on the Q3 cleanup commitment, didn't just absorb the time pressure. But never directly tested. Worth a stronger probe.
- **Team growth:** **Adequate.** Platform org + dotted-line scientists + cross-org science partnerships. Scaling 8→15 is within demonstrated range.
- **Stronger-TL partnership:** **Adequate-to-good.** Q4 substance is real. Caveat: his example was delegate-to-senior-IC-and-hold-accountable, not earn-trust-with-deeper-IC. Slightly different shape than the actual question. Prashan was crisper here.
- **CG-vs-platform adjacency:** **Concern.** Background is further from ranking than Prashan or Vaidehi. Ramp curve will be steeper. Manageable if he understands the gap; risky if he doesn't.

---

## Comparison to other Lean Yes candidates

| | Vaidehi | Prashan | Haibo |
|---|---|---|---|
| **Background fit** | CG-native | Ranking-adjacent (Instagram late-stage) | Platform/infra (Alexa eval + GPU efficiency) |
| **Stronger-TL signal (Q4)** | Strong | Strongest in loop | Strong — diagnostic + reframe + accountability arc |
| **Perf-case instinct (Q3)** | Mature ops, decisive | Soft-on-formal-PIP (named + rejected) | Skipped formal-plan concept entirely |
| **Promo candidate instinct** | E6 ESR-value-model — specific durable outcome | Retention + scope-expansion + stretch — correct meta-frame | Audit + state-check — correct shape, no specificity |
| **Disagreement story (Q2)** | Real and substantive | Partial miss — never landed a disagreement | Essentially absent — philosophical, no moment |
| **Delivery / tightness** | Mature, lands fast | Mature, structured | Weaves, takes time to land |
| **Strongest signal** | Director-altitude operational maturity | Q4 stronger-TL frame + delivery cadence | Q4 diagnostic-to-accountability arc + 4K-GPU platform scale |
| **Recommendation altitude** | Lean Yes → onsite | Lean Yes → onsite | Lean Yes → onsite (gaps need probing) |

If all three convert at onsite, the diversification is real: Vaidehi (CG-native ops), Prashan (ranking-adjacent + stronger-TL muscle), Haibo (platform + ML modernization + diagnostic muscle). Different shapes, not redundant. Haibo would be the lowest-confidence Lean Yes of the three pre-onsite; he could become the highest-confidence if he resolves the perf-handling and disagreement-story probes cleanly, because his platform scale and 3P-model adoption signal real currency on the modern ML stack.

---

## What I'd want to see at onsite

To convert Lean Yes → Yes:

1. **Direct PIP-instinct probe — load-bearing.** *"You inherit a team where one report is already on a formal performance plan that completes in three weeks. The diagnosis has happened, HRBP is engaged. What do you do?"* If he reverts to diagnosis or restarts from coaching, this is the disqualifier for this specific seat.
2. **Real disagreement story.** *"A specific time you and your manager were in different positions on something material — the moment of disagreement, not the moment after alignment."* Test whether the story exists or whether alignment-frame is masking avoidance.
3. **CG-vs-platform problem-shape probe with a senior IC.** *"How do you think about candidate generation vs. ranking, what's the funnel-position shift, what skills do you need to develop."* Test whether he understands the adjacency gap and is calibrated for it.
4. **Modeling currency probe.** *"Most operationally consequential ML modeling decision in the last 12 months — modeling side, not platform side."* Test whether the modeling muscle is current.
5. **Impact-output framing.** *"At 90 days in this seat, what would success look like that goes beyond 'things continue to operate' — what would you actually want me to point to?"* Test whether he can articulate seat-winning outcomes, not just process-output.
6. **Delivery cadence under pressure.** Onsite loop with Dylan or a senior cross-functional partner — does he tighten under pressure, can he land a one-sentence headline before unpacking, does he weave less when stakes are higher?
7. **Why-leaving-Amazon-now.** Surface the framing. Compare to Vaidehi's Meta exit story (AI/MSL pivot shrinking non-core scope) and Prashan's Meta tenure framing. Is Haibo leaving because Alexa AI is restructuring (Amazon AGI consolidation is real and ongoing in this period), or is he leaving on his terms?

---

## Decision

**Lean Yes. Move to onsite — with the perf-handling probe as the single hard gate.** Q4 substance is real and current, 4K-GPU platform scale is non-trivial, the diagnostic-to-accountability arc is the muscle this seat needs to hold the line with senior TLs, and the energy frame (cutting-edge ML + external-customer-facing + big-bets) maps onto the seat correctly.

The three soft spots (perf-handling, disagreement story, CG adjacency) are real and need targeted onsite work, but they're testable. The perf-handling probe is the hardest gate because it's the most operationally specific to Charlie's situation. If he comes in soft on the formal-plan question at onsite, he's not the right fit for *this* seat — but he might be a strong candidate for a different seat without an in-flight CPP.

The other two probes can resolve at onsite. The CG-adjacency probe matters but is a ramp question, not a disqualifier.

## Open

- Move forward to onsite
- Loop should include: **Dylan (perf-case framing — the PIP-instinct probe must come from her or be pre-loaded into her round)**, a senior IC from CG (technical credibility + CG-vs-platform adjacency probe), a senior PM (Tim or equivalent — PM-partnership shape probe given Haibo's "no PM in current org, I play PM hat" framing)
- Pre-onsite recruiter conversation on: (1) Amazon exit framing (Alexa AI restructuring vs. his terms), (2) confirm he understands the seat is CG not platform, (3) surface the perf-handling and Charlie-specific scenario early so onsite gets the considered answer not the reflexive one
- Q5 not covered — note in feedback that the 5th question was time-cut. If onsite doesn't have a slot for it, recruiter pre-onsite is the place to surface a why-Pinterest / typical-week / structured-process question to fill the gap
