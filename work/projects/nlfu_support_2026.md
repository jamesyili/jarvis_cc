# NLFU (New Low Frequency User) — P13N support ask, H2 2026

**Captured:** 2026-07-25 (screenshots of `#p13n-growth-nlfu-leads`, 13-member private channel) · **Status:** live, James looped in by Dylan ~7/24 · **James's obligations:** (1) inventory existing P13N work that already helps NLFU — Dylan publicly named "@Dhruvil and @James can confirm"; (2) decide whether to fund further.

## What it is

Top-down leadership push for P13N to support NLFU (New Low Frequency User) growth efforts, driven from Growth (Brian Lee carrying the H2 plan). Channel members include Brian Lee, Dylan, Dhruvil, Andrew Yaroshevsky, Rajat Chaturvedi, Tim Leung (§17), Rahul Goutam (§35), Caitlin Boyd (Andrew's ABP), Sen Yang (IC18 MLE, Growth — §49), Paula Chuchro ⟨role?⟩, James.

## The proposal arc (thread summary)

- **Background trade-off review** (Brian, quoting the "DJV/DVJ" discussion — acronym verbatim from thread): unconstrained "dream-big" version = **3% NLF WAU goal costing 2.8% SSv2 trade-offs**. Takeaway: go focused instead — tightly prioritized 3-month scope.
- **Updated proposal (Brian):** Goal **~0.5% NLFU WAU via a focused 3-month sprint**. Ask: **4 dedicated HCs from HF, ringfenced (2 CG, 2 ranking)**, alongside already-funded SSJ/Signals/Growth resources; scope = signals, model debiasing, LFU work on UPP; est. **0.5% SSv2 trade-off, to be proposed to DVJ**. Why: EOQ MAU levers hitting diminishing returns; BizOps+Growth say the most efficient path to 5% MAU growth is evergreen retention converting irregular/low-frequency users into durable WAU/MAU.
- **Infra (Brian → Dylan):** discuss whether infra budget changes are needed to reflect NLF investments on HF and UPP.
- **Rajat Chaturvedi:** wants to understand how the 4-HC number was derived; pushes **leaner AI-PDLC-type setup, phased**. Timeframe: in the meeting **with Vicky and Jeff**, SSv2 trade-offs were OK'd **only for Q3 (end of Sept)** — work back from that.
- **Brian (pushback on timeframe):** net-new fundamental workstreams — **UPP debiasing, fine-tuning, unified training data pipeline** — need >2 months of clock time; wants **3-month funding**; open to suggestions from what worked on the HF side to accelerate UPP + HF-ranker work.
- **Dylan (5:47):** there is **ongoing NLF work in P13N already** — e.g. **UPP NLF, GULP in SEO/notif, See-more/see-less in NLF** — some already discussed/funded; "**@Dhruvil Deven Badani and @James Li can confirm.**" Suggests replacing "X ppl × Y months" with **list-the-items-then-prioritize**.
- **Dylan (6:18):** focus on the goal (0.5% NLFU) and trade-offs; **how to achieve it is the team's to design**; ringfencing "isn't the most efficient even for within P13N projects, as many projects touch different areas." Caitlin Boyd to set a **follow-up meeting early next week**.

## James's reads (7/25)

- **Brian Lee doesn't understand the ML side** of this ("doesn't know what the fuck is going on for the ML side").
- **Sen (IC18 MLE, Growth under Shipeng — full profile now at stakeholders §49):** ex-Snap peer of James (~1 yr side-by-side, same director, competitive history) — the right connect for how P13N can actually help. **Reciprocity read: whether Sen helps James depends heavily on whether James decides to help Sen here.** Sen offered his team's help on **AI tooling**. Side payoff: **Sen's year-end peer feedback would strengthen Piyush's IC17 promo case.** Constraint: Sen is **stretched very thin** — pulling him in deeper means **funding his area more**.

## H2 candidate proposals (working list, 2026-07-25 session)

**James's three:**
1. **NLFU × Responsiveness follow-ups** — joint launch recently landed (JJ was helping Growth); follow-up items on surfaces NLFU frequents, e.g. Search. Needs JJ to scope precisely (post-return).
2. **RR offsite-signal NLFU experiments, iteration round** — was promising, gains disappeared after ~2 weeks of experimentation; needs iterations to get right (Leo diagnostic: novelty-decay vs. underpowered-LFU-cohort vs. one-time distribution shift — split readout new-exposure vs. repeat, add long-horizon retention metric).
3. **Fund more NLFU-targeted experiments in RR** (dual-purpose: helps James's RR agenda with Growth money).

**DECISION (7/25): the outward Monday message carries James's three + Leo's #5 only** (LLM pUIC × **PinnerSpark** — PinnerSpark ⟨new to record⟩ worked great for NLFU previously; James called the combination "a great idea"). #4 and #6 stay in-pocket as inventory/later material. Message drafted in-session and emailed to James 7/25 (ephemeral — not kept in repo); send after the Dhruvil DM.

**Leo's three (added same session):**
4. **NLFU segment eval suite + LFU debiasing on UPP** — per-segment offline metrics + online dashboards for low-frequency users across UPP/P2P V0/V1; LFU-aware training (upweighting, short-history robustness). Formalizes the "UPP debiasing" line Brian hand-waved, and makes every existing UPP launch automatically legible as NLFU work (inventory leverage: instrumentation converts existing investment into NLFU credit).
5. **LLM pUIC repositioned as the sparse-user interest engine** — model-based pUIC needs behavioral history LFUs don't have; LLM-based pUIC's structural advantage is inferring interests from few signals + content semantics. Aiming the slowed LLM track at the NLFU segment gives it a fundable niche (Growth budget) instead of head-on competition with model pUIC on the general population.
6. **NLFU-targeted Dynamic Triggering** — for LFUs the visit is the scarce event; tune trigger/notif models on irregular users' receptivity windows. Alok owns DT at ~50% — doubles as his concrete, metric-moving back-on-point scope. (Optional 7th, foldable into #4: an L1-utility serving policy for low-history users — first-N-impressions quality/serendipity budget so LFU sessions don't get popularity slop.)

## Open / queued for analysis (2026-07-25 session)

- Build the **inventory of existing P13N/James-org work that already serves NLFU** (Dylan's public "can confirm" makes this a due item — her staff mtg Monday + the Caitlin follow-up meeting are the natural deadlines).
- **Fund-or-not decision:** does James put his own headcount behind NLFU beyond the inventory?
- **The Sen play:** connect for ML grounding + Piyush-promo feedback, against the fund-his-area-more cost.

## 2026-09-03 — a CLR lever gets a name

- **Devin — CLR UIC-condition tuning for NLFU** is now **A/SSv2 #7** on the Exceeds scoreboard (`../career/exceeds_h2_2026_campaign.md`; Notion H2 milestones, wk of 8/31). First James-org NLFU item with a named owner and a launch framing. The 7/25 "inventory of existing work that serves NLFU" item is still open — this is one row of it.
