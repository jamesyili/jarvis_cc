# OpenAI — Reid (Hiring Manager) 30-min Chat — Prep

**What it is:** 30-minute conversation with Reid Gustin, the hiring manager for the Integrity Foundations ML EM seat. Coralynn's framing: *"not an interview per se"* — but he'll go into **a lot more technical depth than the recruiter call**, he's the **source of truth on roadmap and the hard problems**, he'll share the team shape + the 30-60-90 for the seat, and he'll ask about your experience. It's a **mutual-fit gate**: pass it (both directions, green lights) and you move into the formal loop.

**Coralynn's read on him:** *"He's wonderful — probably one of my favorite hiring partners at OpenAI."* So: a real practitioner, mission-serious, the kind of HM a good recruiter protects. Walk in expecting a peer, not a gatekeeper.

**Posture:** conviction without commitment. You are assessing the seat as much as he's assessing you. 30 minutes goes *fast* — be tight, lead with substance, leave him wanting the next conversation.

---

## ⭐ If you only review three things on the plane

1. **The 30-second opener** (below) — short, because Reid already has Coralynn's notes. Don't re-deliver your resume.
2. **One technical deep-dive you can take three levels down** — pick UPP *or* Reflex/Pinkerton and rehearse going deep, not wide (see "Go deep, not wide").
3. **Your four questions for Reid** — half the value of a 30-min HM chat is what *you* ask. Memorize three.

---

## What Coralynn already has on you (build on this — don't repeat it)

Reid will walk in pre-loaded with what you established on the May 27 call. Your job is to *extend* it, not re-state it:

- **Mission-driven on integrity, with real lineage** — FB **civic integrity during the 2020 elections** (you named the lost sleep, the disillusionment, leaving Meta over the outcomes) + FB feed integrity + Snap content quality. Coralynn explicitly affirmed: *"you do have a vested interest in this space."* **This thread is already validated — let it breathe, don't oversell it.**
- **Hands-on and going deeper technically** — you told her you've gone as deep as Codex allows, **landed production code**, built things, and that this makes you a better strategic decision-maker because you understand the challenges the team actually faces. She flagged this is an *expectation* of the seat — you're aligned.
- **The prevention frame** — "preventing bad experiences through recommendation, not just optimizing good ones." That's your through-line and it landed.
- **Team size** — Snap: 2 EMs + ~25 engineers (3 pods). Pinterest now: ~10 direct + 1 manager with ~10 = ~20 total, "changes afoot."
- **Upstream technical move** — features-on-models → the model layer itself.

> **Implication:** With Reid, skip the biography. He's read it. Open with a *tight* anchor and spend your 30 minutes on (a) technical depth and (b) the questions that prove you're evaluating the seat seriously.

---

## Your 30-second opener (when he says "tell me a bit about yourself")

Short. He has the notes. Anchor + the one differentiator (hands-on depth) + genuine curiosity about *his* team.

> *"Coralynn probably gave you the arc — user-experience side of ML at scale, civic + content integrity at Facebook and Snap, now leading Homefeed candidate generation at Pinterest. The part I'd add: the direction of my work has moved upstream — into the model layer itself, foundation-model pretraining for user representation, multimodal signals — and I've stayed hands-on enough to land production code, because I lead better when I actually understand the problems my team is solving. That's the altitude your seat sits at, which is why I wanted this conversation. I'd love to hear how you frame the team and where the hard problems are right now."*

Then **stop and let him talk.** A 30-min HM chat where he does 55% of the talking is a good one.

---

## Go deep, not wide (the main shift from the recruiter call)

Reid *will* probe technical depth. The failure mode (from your Anthropic loop) is breadth-first: listing every component/metric before going deep on any. **Pick one trade-off and go three levels down, then surface back up.** Have two systems loaded, ready to take deep on demand:

### Option A — UPP / candidate generation (your core craft)
- **Level 1:** First-stage retrieval for Homefeed — foundation-model pretraining for user representation, transformer-based CG. Every retrieval decision either earns or breaks the downstream experience.
- **Level 2:** The FP/FN structure of retrieval — false-positive cost (surfacing the wrong thing early poisons the whole funnel) vs. false-negative cost (missing the right thing the user never gets a second chance to see).
- **Level 3:** A specific calibration decision — pretrain-vs-finetune split, how the user representation is conditioned, how you evaluated it offline when "not hurting but not improving" was the honest read. **Show the judgment, not just the architecture.**

### Option B — Reflex / Pinkerton (the AI-leveraged-leader bet — closest to OpenAI's world)
- **Level 1:** Agentic system — detect → simulate → build, with expert judgment captured as a compounding labeling asset; multimodal **visual user signatures** synthesized via VLM introspection.
- **Level 2:** Why the hard part is **eval + the human-in-the-loop feedback protocol**, not the model — velocity (idea-to-launch) as the optimization metric, expert labeling as the invariant that compounds.
- **Level 3:** A real design decision — loose coupling at the API boundary (Pinkerton stays "dumb but rich," reasoning lives in the consumer), allowlist-only blast radius for implementation agents, cascading-hallucination as a tier-1 guardrail.

> **Why B is your secret weapon with Reid:** an Integrity-Foundations HM at OpenAI lives in exactly this world — classifier stacks on a foundation-model API, eval-as-half-the-work, adversarial robustness, agentic systems. Reflex/Pinkerton proves you don't just *use* frontier ML, you *build* with it. If he gives you an opening, go here.

### Integrity-altitude technical lines (drop one, max — don't force)
- **Snap Discover two-tier demotion (your best war story):** *"For borderline content that's not policy-violating, the FP cost isn't symmetric across users. We tiered the demotion — smaller for users who'd consistently engaged with that category, stronger for everyone else, never full removal. Cut prevalence ~35% while preserving creator autonomy. The lesson that transfers: who pays the FP cost matters as much as the FP rate."*
- **Modern-stack take (if it drifts technical):** *"Foundation models give you a better FP/FN Pareto frontier on known harms, but they introduce new FP modes — reasoning-based over-flagging, hallucinated classifications, cipher/role-play bypasses. The work shifts from threshold tuning to adversarial calibration under distribution shift."*
- **System framing (always):** never talk about a classifier in isolation — frame it as *one layer in a multi-layer defense system with a feedback loop*: input classifier → mid-generation token-level → post-response full-context → human review → red-team loop. Each layer has its own FP/FN profile.

---

## "Why OpenAI / why this seat / why now" (he'll probe interest)

The heavy "why OpenAI" lands later (the XFN behavioral round). With Reid, give the *honest, specific* version — not the mission cliché:

> *"The direction of my work has been moving upstream toward the model layer, and OpenAI is one of the few places where operating at that altitude IS the day-to-day. Integrity specifically isn't a pivot for me — it's where I started, FB civic and feed integrity, and it's the work I lost sleep over for the right reasons. The combination — the model-layer altitude plus the stakes of getting harm-classification right on a system this many people touch — is the specific thing I want to be doing. I'm taking it seriously, and this conversation is part of how I decide."*

**Do NOT say** "I want to work on safety because it's important." Generic. Lead with the altitude + the lived lineage.

If he asks **"why leave Pinterest":** *"Pinterest is strong for me — consumer ML scope, executive sponsorship, a clear path. This isn't escape. It's that the frontier of the model layer is being defined here, and that's worth understanding seriously before deciding."* Don't volunteer Dylan / Director-track / comp / internal dynamics.

---

## Your questions for Reid (memorize 3-4 — this is half the chat)

Lead with substance and roadmap (his domain, where he's the source of truth). Save logistics.

**Substance / roadmap (lead here):**
1. *"What does the team actually own end-to-end, and what are the hardest unsolved problems on the roadmap right now — where would you say the real gaps are?"*
2. *"What's the 30-60-90 you'd want from whoever takes this seat? What does success at 6 months look like?"*
3. *"How do you think about the FP/FN trade-off on borderline content at the LLM-classifier altitude — where most of the calibration tension lives? Is adversarial robustness (cipher / reframing attacks) this team's territory or does that sit elsewhere?"* ← signals lived expertise; invites him to tell you what's genuinely hard.
4. *"What's the ratio of the work — research-adjacent ML, detection/ops, platform/infra investment? And how hands-on is the EM expected to be?"*

**Fit / team:**
5. *"What makes someone succeed in this seat — and what's the failure mode you've seen?"*
6. *"What's the team's shape today, and where do you want it to grow?"*

**Save for last / skip if time-short:**
7. *"Where would you expect someone in this seat to be in 2-3 years — deeper in Integrity, breadth into adjacent ML surfaces, scope expansion?"*

> **Don't ask Reid about comp.** That's Coralynn's lane. Don't ask "what else is open" — that telegraphs not-this-one.

---

## The loop ahead (so you know where this sits)

The Reid chat is the **gate** to a standard slate. Don't over-rotate on later rounds now — but knowing the shape helps you pitch the right things to Reid:

1. **Reid 30-min** ← *you are here.* Mutual fit + technical depth + roadmap.
2. **Text screen (2 parts):** (a) 1.5-hr **EM skills** interview — "tell me about a time" behavioral; (b) **architecture interview** — almost certainly **ML design**, likely classic ranking/recommendation. *(Coralynn preps you gate-by-gate.)*
3. **Virtual onsite (4 parts):** another EM-skills; an **XFN behavioral** — heavy "why OpenAI"; a **project retrospective / deep-dive** — deep on design decisions you and your team made (no coding).

> Standard slate, you've been on the *other* side of it many times. The EM-skills and project-deep-dive rounds are squarely your home turf. The ML-design round is where the technical_foundations corpus + system_design bank you built for the trip pay off.

---

## Traps / what NOT to do

- **Don't re-deliver the resume.** Reid has Coralynn's notes. Repeating the FB→Snap→Pinterest arc wastes a third of your 30 minutes.
- **Don't go breadth-first technical.** Pick one trade-off, go three levels deep, then surface. Senior interviewers read depth-then-breadth as senior; breadth-then-shallow as mid.
- **Always resolve an adversarial scenario** if one comes up (cipher / jailbreak / role-play). End-to-end: how it bypasses the naive classifier → which layer catches it → the FP cost of that layer. *(This is the exact thing you got set up on and didn't resolve in the Anthropic loop. Don't repeat it.)*
- **Don't over-claim integrity-as-identity.** You've *already* established it authentically — Coralynn affirmed it. Now let it sit. Over-selling now reads as trying-to-fit-the-seat and quietly erases your three years of recsys craft.
- **Don't talk comp, visa, start dates** with Reid. Wrong person, wrong stage.
- **Don't drop internal Pinterest names** (Dylan, Andrew, Faisal, Jeff). Not needed; can leak into later reference checks.
- **Don't commit to the next step on the spot** if he pushes — *"I'd want a day or two to digest before locking in the next round"* preserves your decision space and reads as deliberate, not eager.

---

## Pre-call 5-minute checklist

- [ ] Say the 30-second opener out loud once.
- [ ] Pick your **one** go-deep system (UPP or Reflex/Pinkerton) and rehearse the three-level descent out loud.
- [ ] Re-read the Snap Discover two-tier demotion line.
- [ ] Memorize **three** questions for Reid (1, 2, and 3 from the list).
- [ ] Hold the posture: peer-to-peer, you're assessing him too, 30 min goes fast — be tight.
- [ ] Water + notebook. DND on. No Pinterest Slack / tabs visible.

---

## The frame to walk in with

You're a Sr EM with active executive sponsorship at a $30B+ consumer-ML company, who started in integrity and means it, has moved upstream to the model layer, and stays hands-on enough to ship code. That's the table you're walking up to — not a seat you have to earn permission to want. Reid is "one of Coralynn's favorites" for a reason; meet him as a peer who happens to be evaluating whether his team is the right next altitude for you. Conviction without commitment. Land one deep technical thread, ask two questions that make him think, leave him wanting the next conversation.
