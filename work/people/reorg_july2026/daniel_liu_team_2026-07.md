# Daniel Liu's Team — Inbound Scope & Roster (reorg, 2026-07)

**Created 2026-07-07** from the Dylan re-entry 1:1 debrief. **Status: reorg APPROVED** (Dylan aligned with Rajat + HR); **downward conversations mid-July 2026**; Alim starts 7/27. James inherits Daniel Liu (EM) + his team + their scope. This file = raw intel for the org-design proposal Dylan asked for. **No structure decision has been made — design space is deliberately open** (see "Design state" below).

This is the 5/15 latent signal landing: Andrew's IB-cut / redeploy-Yan's-ML-engineers consideration materialized. Dylan's word for the team: **"relatively underutilized"** — she'd been lending them to other personalization efforts; told James this is his opportunity to correct for that ("here are more people to do the things you need to do"). Also the 5/23 "Scenario E preferred shape" (Daniel's ML team consolidates under James — "desirable not essential") shipping for real.

---

## Daniel Liu (Manager II, L16) — the EM James inherits

- **History (load-bearing):** ex-TL on the Homefeed CG team itself (pre-James). **Dylan herself judged him not fit for management** in that era. Left Pinterest → returned via interview as a manager *outside* Dylan's scope → later reorged under Dylan (as Yan's sub-EM) → now reorged under James. Read: Dylan may be handing James her own unfinished evaluation — James's unstated second job is develop-or-document.
- **Technical rep:** solid IC, very technical, straightforward, delivers — "similar to Bella in that way" (per Bella + JJ, who know him well from his CG days; he left behind real legacy systems). Diplomatic; thinks deeply. **Interested in AI / wants his team on AI work** — aligns with Reflex / AI-Leveraged Engineering charter language.
- **The lean-in question (hold loosely):** Anna (RR PM partner, inner-circle ally) is emphatic he's **not the right EM/TLM for Retentive Recs** — lacks product instinct/motivation. James's own observation as adjacent EM matches (sidelines, watching, not engaged). **Confound James himself names:** may have held back precisely because RR was James's scope and he feared encroaching. The reorg deletes the confound → first ~30 days under James is a clean natural experiment: explicit charter + explicit permission to drive, then watch. **Anna's veto is politically decisive for RR regardless** — she co-owns the RR product narrative.
- **Next step:** James↔Daniel conversation **after** Dylan's downward announcement (sequencing deliberate — tough conversation to have before it's official).
- ⚠️ **Name disambiguation:** the "Daniel Liu (contractor)" entry in stakeholders.md was a mis-recording — the contractor is a different Daniel, surname NOT Liu. This Daniel Liu is the EM, ex-Yan sub-EM.

## Roster (8; intel as of 7/7 — 3 unknowns remain)

| Person | Level/role | What James knows |
|---|---|---|
| **Balaji Rengarajan** | Staff MLE — **their TL** | Rumor mill: deep thinker, knows a lot. James's read: sharp, picks up ML fast, willing to take responsibility, but **little observed initiative/proactivity around RR** (same encroachment confound as Daniel). **Live option: Staff anchor under Alim.** |
| **Roderick Gao** | Sr SWE | **Unified Explore Backend (UEB)** — proactively driving it; high performer (Yan speaks highly, gave him the important project); proactively reached out to James on UEB design review, praises James's team members. James: "solid — and we do need a strong IC15." Took over the UIC-adjacent work after Yang's parental leave. |
| **Ling Lan** | MLE II | **Critical to LLM-based pUIC** — built much of the actual LLM inferencing pipeline (on ATG's LLMs); works closely with Yuke + Chuxi already. Natural delivery partner for Chuxi's pUIC ramp. |
| **Kim Toy** | Sr MLE | Long-time Pinterest. Joined CLR meetings to work on CLR improvements but **hasn't actually started** — time loaned to **Dhruvil's team on UPP foundational work**. ⚠️ Watch how much stays loaned; transition it deliberately. Potential CLR coverage (Devin flight-risk hedge). |
| **Yang Liu** | Sr MLE | Worked with James's team on **UIC work before her parental leave** (Roderick took over). Supposedly a pretty solid engineer. |
| **Yongwoo Noh** | Sr MLE | **Unknown** — get workstream map from Daniel. |
| **Felix Yang** | SWE II | **Unknown** — get workstream map from Daniel. |
| **Rita Lyu** | Intern | ~2 months left — ignore for org design. |

## Inherited scope

- **Exploration module — ML work + plumbing.**
- **Intelligent Boards (IB) efforts** — the whole line.
- **Recommend-a-Board:** small but **live production traffic** on several services (Related Pins, Search); team owns several small models keeping those alive. (Per Daniel in a prior 1:1.)
- **Unity Board:** backend service mirroring Unity Home Feed. Dylan disliked past design reviews (unclear mapping to Unity HF). Roderick's read (prior conversation, different context): Unity Board is very simple, serves the same criteria as Unity HF — that's been essentially finalized.

## Design state (deliberately OPEN — do not converge yet)

- **RESOLVED 2026-07-07 (Q1, grill): mid-July downward comms lock OUTER lines only** — (1) Daniel + team + IB/exploration scope → James; (2) Alim joins 7/27 as EM of a named starting pod. Everything internal (GenRet placement, Balaji line, Ling line, Kim pivot, Daniel's settled charter) stays **explicitly provisional** — "starting state, cheap to adjust; settled structure proposed after 30–60 days of observation." James confirmed this matches Dylan's intent.

- Dylan wants a **structure proposal** from James; **she offered time to observe before deciding** — observe-first is a live option, not a failure mode.
- **Generative Retrieval does NOT have to go under Alim** (6/30 Option-2 assumption retired). More ways to skin the cat now: Bella doesn't want to move under Alim; **Balaji under Alim is an option**; the new roster changes the anchor math.
- **Fairness-to-Daniel constraint:** carving many of Daniel's people over to Alim (new, unknown manager) may be unfair to Daniel and reads badly — weigh it explicitly in any option.
- Open Alim-vs-Daniel allocation = the central design question of the proposal.
- Dylan's open question from 7/7: **who TLs the pUIC/RR space** post-Yuke — James owes a proposal (current shape: Chuxi gradual unannounced ramp + support; see team_members_scope.md 7/7 entries).

## James's immediate priorities (pre-design, ~next month)

1. **Staff Retentive Recs and make it go full steam** — something visibly happens in ~1 month; **both pUIC experiments (model-based + LLM-based) in play.**
2. Use the incoming resources to **deliver what Andrew is asking for.**
3. **Digest the IB / exploration scope on a slower clock** — don't force structure decisions before understanding the inheritance.

---

## 2026-07-14 update — charter reframed to frontier modeling; timeline decoupled; new boards intel

Corrections + additions from the 7/14 Dylan conversation + the org-design grill (system of record for structure: `org_design_proposal_2026-07_v2.md`):

- **Daniel's area = frontier ML modeling, NOT infra/KTLO.** His team drives metric gains and publishes (KDD, RecSys). This **retires the v1 proposal's "Scoring & Serving Platform / least-AI-shiny charter / motivate-him-in-via-AI-leveraged-oncall" framing** — a wrong premise. His motivation is fed by the charter *being* genuine frontier modeling (the AI/ML work he wants) — no need to bolt on AI-shine.
- **His leg = boards (retained) + LWS (inherited).** Retains **Recommend-a-Board / Intelligent Boards**; **inherits LWS** (lightweight scoring, split from CLR — a good onboarding ramp per Dylan). **Sheds the retentive-recs part of his team to Alim.** **CLR does NOT go to Daniel** (too much scope to digest at once; CLR's synergy is with Retentive Recs → targeted to Alim at settle). **UPP stays with James** as the framework both CLR and LWS build on.
- **Initial state (decoupled timeline): Daniel's team stays INTACT under Daniel.** Dylan decoupled her reorg (Daniel → James) from James's internal reorg (own clock). Initially the only reporting change is Alim onboarding with a subset of *James's own* reports — moving Daniel's reports to Alim right away is "too drastic." The RR-shed + anticipation consolidation are **deferred** to James's later proposal, out of the observation window.
- **Boards metric intel (Dylan, 7/14):** Recommend-a-Board **hasn't been a big metric driver in ~6 months** — BUT a recent **notification collaboration produced "wow" improvements.** Dylan shared the launch review and asked James to **get into the nitty-gritty.** Read: boards modeling has *latent, underexploited* impact; surface pairings (notifications) are where it unlocks. Both James's graded test (engage inherited scope deeply) and the growth thesis for the charter.
- **Underutilization confirmed from inside:** Dylan repeated "underutilized," and says the **anecdotal feeling from people within Daniel's team is that they're underutilized** too. Reinforces: under-directed talent = cheap upside for a leadership turnaround; sharpens (but does not settle) the develop-or-document read on Daniel — hold loosely, the observation window separates "direction-from-above" from "leadership" as the cause. **(Rollout caveat, 7/14b: "underutilized" is Dylan's private read — do NOT use it as a talking point to Daniel or his team.)**

## 2026-07-14b update — retention lens + 1:1 approach

From the rollout-messaging session (prep doc: `daniel_1on1_open_2026-07-14.md`):

- **Reporting line = lateral, not layered.** Daniel was **Yan's sub-EM** (Yan = Senior EM); moving under James (also Senior EM) is a **lateral re-parenting**, not a new management layer inserted above him. No demotion shape — the real work is a new-manager relationship + his team changing orgs. (Corrects an in-session slip that had him reporting to Dylan directly.)
- **Dylan's mandate for the first 1:1 = assess retention + learn what motivates him** (she pre-confirmed: **LLM-based work** excites him). So the 1:1 is **listening-first**, not a charter briefing.
- **James's decision (locked 7/14b): Daniel is NOT the lead for Retentive Recs (Anna's veto) or Reflex (too much context to transfer).** So the LLM-motivation is **not** solved by a day-1 charter change. It's a **trajectory play** — the inheritance is his opening to get more involved over time in the direction he wants, plus **future things James + Daniel build together.** Something to *work on*, not change now. (Keeps minimal-change; GenRet-home / LLM-boards / LWS-distillation are future collaboration *seeds*, not moves.)
- **Charter–motivation gap to hold:** his assigned leg (boards + LWS scoring modeling) is frontier ML but not obviously *LLM-based*, while the LLM-shiny work (RecGPT/GenRet, LLM-pUIC) sits with James/Alim. Manage via trajectory + honest growth path, not an over-promised LLM leg. **Flight-risk watch-fors** (per prep doc): flat affect on the charter, level/comp steering early, strong Yan attachment, treating boards as a dead end → two+ signals to Dylan.

## 2026-07-24 update — team named "Retrieval Modeling"; portfolio balance; Anna's LLM-backbone thread

- **Team name LOCKED: Retrieval Modeling** (James's call, after cycling through Boards/Preranking/Recommendation variants). Rationale: puts an underutilized team on the org's marquee craft (turnaround signal per Dylan's "underutilized" read), keeps the weak/risky boards surfaces as workstreams inside rather than the flag. Boundary vs. James's "Retrieval Foundations": Foundations = framework/substrate (UPP), Modeling = the models on top.
- **Initial scope: LWS + Intelligent Boards + Recommended Boards.** Portfolio read (James's engine/bet/ballast frame): **LWS = reliable gains engine** (NB: LWS is a *preranking* model — stop describing it as "scoring"); **IB = the 0-to-1 bet** (very risky, latent upside per Dylan's notification-pairing "wow"); **Rec Boards = mature ballast** (live traffic on Related Pins/Search, no metric movement ~6 months).
- **IB settle gate (~2 months):** James wants to understand the synergy before settling placement. Deciding signal: gains originating in *modeling improvements* → IB stays with Daniel; gains from *surface pairings* (notifications, Explore) → IB moves to Anticipation Modeling (Alim) at settle. James told Dhruvil 7/24 the anticipation team "likely" gets IB — placement genuinely open.
- **Anna's LLM-backbone proposal (new, 7/24):** a bunch of LLM needs should share a **single personalization backbone** — LLM pUIC, Recsplanation, Board Titles, pRelevance *(correction: pRelevance is Dhruvil's team)*, New HF Tuner, SM/SL, others — and **Anna thinks Daniel is the best fit to lead it.** This is the strongest third-party datapoint yet for the Daniel-LLM trajectory play (7/14b): a real, Anna-endorsed LLM leadership path that doesn't collide with her RR product-instinct veto (backbone = technical, not product). NOT a day-1 charter move — feed it into the observation-window design + the trajectory conversation. Nearer-term LLM seeds already in his charter: LWS distillation, LLM-boards.

## 2026-07-27 update — first DM exchange warm; Balaji step-up suggestion; Anna LLM-backbone seed planted and TAKEN

From James's Slack DM (pre-announcement, light-touch — the deep 1:1 still follows Dylan's announcement):

- **James sent Daniel the workstream-clarity material; Daniel (12:48pm): "I love the clarity here. We can discuss further how my team can help and collaborate."** Warm, engaged first substantive exchange. James offered openness to Daniel's team members stepping up to drive more; setting up time this week.
- **Daniel's step-up suggestion: Balaji** — "could be a good fit for this, but his bandwidth is a little full at this point with the **IB sprint**, so we might need to chat further." Intel: (a) Daniel proactively nominating leads = engaged-not-sidelined datapoint against the underutilization-as-leadership read; (b) Balaji currently loaded on an IB sprint; (c) Daniel envisioning Balaji stepping up **within his own workstreams** leans the fork toward *platform TL under Daniel* — feed into the Balaji decision (Dylan ask #1) but don't settle it here.
- **LLM-backbone seed planted — and taken.** James (12:56pm): "if there's a cross-org effort you and your team is passionate about — **@Anna Kiyantseva and I were talking and we think there may be a host of upcoming LLM needs that should share a single personalization backbone.**" Daniel (3:59pm): **"yes, we'd love to take on that if there's clear requirement on what we need to build or support."** The 7/24 Anna-endorsed trajectory play is now live with Daniel's enthusiasm on record, pre-announcement. His condition = clear requirements → **next move: James + Anna shape the LLM-needs requirement inventory** (LLM pUIC, Recsplanation, Board Titles, New HF Tuner, SM/SL, etc.) before the first real 1:1, so the trajectory conversation lands with substance, not vibes.
- Note: Anna's surname on record = **Kiyantseva** (from the thread mention).

## 2026-08-01 update — 7/29 conversation record + Bowen channel + behavioral read

Person-level record now lives in **`work/people/daniel_liu_archive.md`** (created 8/1, modeled on dylan_archive.md); the 8/4 1:1 prep lives in the announcement-week timeline. This file stays the team/scope record.

- **7/29 conversation (James's notes, photo-captured):** managing through change past 2–3 months — "glad for the space and collaboration," "want to contribute." Frames his team as **"Personalization Product ML"** — product use-cases (Board, Anticipation, Recsplanations); collection modeling = listwise predictions + working collections, deliberately not pointwise. **AMB/IB user-journey predictions: passionate** — IB Sprint to power exploration (lower-funnel conversion); **"want to help with the technology end to end — ownership of the entire process"**; **"want clearer responsibilities."** **LLM-based recs: curious + interested** — LLM pUIC, how LLMs get incorporated, Generative Retrieval, collaborations with ATG, UU. Team passionate about interest/journey predictions.
- **Read-throughs:** Dylan's "LLM excites him" now confirmed first-hand (the 7/14 unprompted-test is retired). His journey-predictions passion = live input to the IB gains-origin gate. His "Personalization Product ML" self-framing = an identity/naming lever for the T2 name at the Phase-2 settle (T1 stays "Curation ML" per the 8/1 delta; note "Retrieval Modeling" now = Alim's team). Anticipation-as-his-use-case vs. Alim's Anticipation Modeling charter = a real Phase-2 seam, held silently.
- **Bowen channel (James, 8/1):** Daniel is very close to **Bowen Deng** (previous EM under James) and told James he knows James is a good manager — trust pre-seeded via someone he trusts. Use silently; never as leverage.
- **Behavioral read (James, from several project meetings):** doesn't like being put on the spot; doesn't voluntarily discuss his team's plans. Prep response: pre-send reflective questions, prune live asks, reflect his own words back rather than open-ended probing.
- James's sense: **he likely already knows the reorg is happening.**
