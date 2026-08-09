# P13N Retrieval — EM Primer

**From:** James Li · **To:** Daniel Liu, Alim Virani · **Date:** August 2026

This is my read of the organization as it stands: what each workstream is, who is doing what, where I think we are fragile, and what is decided versus genuinely open heading into the end-state design.

It is a starting point, not a finished picture. Some of it is wrong, and the parts about your areas are the parts I am least sure of. I would rather hand you something concrete to correct than a blank page.

*[Square-bracketed italics are gaps I know about. Part of what our walkthroughs are for.]*

---

## 1. How we'll operate — ground rules for this table

We're basically strangers starting over together, all three of us. That's not a problem to manage; it's the founding condition. These are the rules I want us to run by, starting Monday. Push back on any of them at the table.

**1. First Team.** This table is your first team; your own team is your second. When your team's interest and this table's interest pull apart, we say it here and settle it here — not in the hallway. That means each of us will sometimes carry home a decision our team wouldn't have picked, and own it as ours.

**2. We cut once.** We're in observe mode through the fall. Around November we make the structure calls together, on criteria we agree in advance, and then the structure stands. Moving people between managers is expensive for everyone underneath us; after we settle, it's reserved for serious exceptions. (The interim state stays as announced: a starting state, cheap to adjust. The stability promise attaches to what we settle in November.)

**3. Every team gets a scoreboard, a flag, and its share of the plumbing.** Each team inherits metric goals spanning top-line engagement, retention, and cost; a mission — a year from now, each of these teams is known across Pinterest for something; and org obligations, named explicitly rather than discovered. No team gets to be all-glory or all-plumbing.

**4. We start from strength — and act like it.** This is a high-performing group: end-to-end systems experts, deep modeling experts, and a real IC15/IC14 bench. The obligation that creates is a standing question at this table, every week: who are our best people, what energizes them right now, and what would make them leave?

**5. No ceilings from us on our best people.** Time, opportunities, visibility: my job is to remove every limit that's mine to remove, and to go fight the ones that aren't. The cost we accept: investment follows talent and energy, and the most exciting problems will not be spread evenly.

**6. Decision rights, said once.** Final calls are mine. What I want from this table is your honest reads and disagree-and-commit when we land. We won't re-litigate this.

**7. Nothing leaves this table as a maybe.** While we're building the map — and especially while structure is open — teams hear decisions, from their own manager, with notice. Never scenarios, never previews. That's what makes it safe for the three of us to think out loud in this room.

**8. AI-first operations.** We operate AI-first as a norm, not a slogan: before we add process, meetings, or headcount, the default question is "what does this look like AI-leveraged?" This isn't aspiration — we're already doing it. Reflex is the program-level bet, and PINvestigator and Pinkerton are live examples of engineering leverage in regular use. Daniel's Pin tools are the same pattern from the Curation side. The cost we accept: we spend real time building leverage a quarter-driven team would skip — and all three of us work this way ourselves; it doesn't get delegated downward.

**9. We don't fund everything — because we can't.** That's arithmetic, not philosophy. So we're selective and decisive: fewer things, funded properly, with named owners. And what we don't fund gets an explicit no — said out loud, with a reason — not a slow starvation. The cost we accept: we will decline or kill work that is genuinely good, and we'll own that call rather than letting things die of neglect.

---

## 2. The organization at a glance

**Name:** P13N Retrieval. Dhruvil's organization is P13N Ranking. Together we cover personalization for Homefeed and the surfaces built on it.

**Scope, in one sentence:** the pre-ranking funnel end to end — from user signal to what the ranker sees — plus the anticipation modeling built on top of it, including retentive recommendations, predictive user-interest modeling, and boards and exploration ML.

**The boundaries that matter:**
- **Ranking starts where we end.** We decide what candidates exist and which survive to scoring. Dhruvil's org ranks them.
- **Surfaces belong to P13N-Experiences.** We own the models and the retrieval path, not the product surface.
- **ATG** is a research partner across generative retrieval and pUIC, not a delivery dependency we control.

**The three teams as of the August announcement:**

| Team | EM | Center of gravity |
|---|---|---|
| **Retrieval Foundations** | James | The shared substrate every leg builds on — UPP — plus Reflex, the AI-enabled dev-velocity accelerator; and, for the interim, the main-stack engines (CLR, LWS, L1 Utility, RecGPT) until the T2 settle |
| **Curation ML** | Daniel | Boards and collections intelligence. Daniel is already running this as a program map — Intelligent Board, Collection P13N, Module Platforms, UPP ML Foundation, plus a team-wide AI Harness line — and I've mirrored that structure in §4 rather than inventing my own |
| **Retrieval Modeling** | Alim | Anticipating what a Pinner wants next: the interests that bring someone back, with content and serving path ready |

### Setting accountability for impact

Accountability for this group runs along five axes, and each of the three teams carries responsibility on all five — with guidance and trade-offs called out explicitly, not discovered. Incubations are the high-risk axis, so we spread them deliberately across teams while capturing the synergies between them. The stance throughout: the maximal amount of bottoms-up innovation, with top-down alignment on goals, initiatives, and direction.

1. **Topline metrics.** We exist to drive meaningful impact to Pinners, and to do it efficiently. Representative annual numbers, to be aligned: **~3.5% SSv2** (engagement), **~0.5% WAU** (retention), **~$2M cost savings**. Against the 2025 baseline in §3, engagement and retention step up meaningfully; the cost number normalizes after 2025's deprecation harvest.
2. **Incubation of new initiatives.** The frontier bets aligned with organizational strategy — usually 0→1, usually the biggest eventual levers for topline growth, always in need of patience and right-sized investment. Every initiative gets a **named incubation owner and explicit graduation-or-sunset criteria**. The lineage — roughly one funded bet a year becoming a topline lever — is this org's actual signature: LWS (2023), CLR (2024), L1 Utility (2025), UPP Retrieval (2025), RecGPT (2025 — now one of the highest-performing CGs), Predicted User Interest Clusters / Retentive Recs (2026), Intelligent Boards (2026). §3 tells this story properly — including the sunset that proves the discipline is real.
3. **Cross-org initiatives.** Prioritized company efforts we support because we're accountable for the surfaces we own — even when it stretches us. In H2 2026: NLFU Growth; Content Quality (Teen Safety, GenAI controls); See More / See Less. Named leads in §5.
4. **Oncall.** Together with the other teams under Personalization: stewardship that keeps Homefeed, BMI, and Board systems stable, with metric fluctuations monitored and root-caused — HF and BMI metrics; unity-homefeed, unity-gulp, unity-board. Stability through the realignment is part of the job, not an interruption of it.
5. **Organizational contributions.** *[To be filled at the table — hiring, calibration, interviewing, mentoring. The axis is named now so it doesn't ship empty.]*

*(A sixth heading in my accountability draft — Streamlined Technological Investments — is still to be written; parked here so it isn't lost.)*

### Missions — the flag each team flies

Rule 3 promises every team a flag: a year from now, each team is known across Pinterest for something. Below are candidates, not decisions — I want each of us to pick, or rewrite, our own at the table. The test I applied to each: it names a capability, it implies the axis it drives, and you could say it in a hallway.

**Retrieval Foundations (mine):**
1. *"Personalization built once — the substrate every Pinterest surface stands on."* (The UPP flag; measured in cross-surface adoptions.)
2. *"The engine room: the most reliable gains-per-dollar in Personalization."* (The engines + cost axes; the interim-true version.)
3. *"The team that makes every ML team faster — substrate below, AI leverage above."* (UPP + Reflex together; measured in adoption and velocity.)

My lean: 1 as the end-state flag, 3 if Reflex's demonstration lands first. 2 is true but every team would claim it.

**Curation ML (Daniel's — starting points only, yours to rewrite):**
1. *"Boards that build themselves — Pinterest's home for LLM-native curation."*
2. *"From discovery to curation: the ML that turns saves into collections, and collections into return visits."*
3. *"The frontier LLM team of Personalization — recommendations that understand what you're making."*

**Retrieval Modeling (Alim's — same caveat):**
1. *"Know what a Pinner wants next — and have it ready when they arrive."*
2. *"Retention, modeled: we own the interests that bring Pinners back."*
3. *"The anticipation engine behind Pinterest's retention story."*

**Where confusion reliably happens** — worth naming so we handle it deliberately rather than rediscovering it:
- **UPP is consumed, not shared.** CLR and LWS both build on UPP as a framework. That is a dependency, not joint ownership.
- **The explore→boards path crosses teams.** The pin-level exploration module introduces new concepts to a user; Intelligent Boards is the step that converts introduction into real adoption. They flow into each other and do not currently sit together.
- **LLM-pUIC appears on two maps.** It shows up in the Retentive Recs program (area 5) and in Daniel's Intelligent Board program (area 7). Designed overlap for now — Ling's pipeline serves both — but it's a named seam to settle, not one to discover.
- **Oncall follows the charter, not the reporting line.** LWS and boards paging moved with their charters on day one; L1 and real-time ops sit with Rui under Foundations & Efficiency.
- **Some people work a charter their manager does not hold.** This is real today and is on the list to resolve.

---

## 3. The record: September 2024 → today

This is the history lesson — how this org got here, told honestly, for the two of you and for anyone who needs this context cold. The full 2025 launch log and the H1 2026 LR tracker both live in [#p13n-relevance-lr](https://pinterest.slack.com/archives/C05UMECTDDJ), with per-launch links threaded through this document. §2's incubation list is this story compressed; here it is uncompressed. *[A few tracker-referenced rows aren't ingested yet — the 5/18–5/20 notification rows, hf_shopping_control_l1_utility (7/21), position-aware sampling (7/24); remaining brackets mark those.]*

### September 2024 — what I walked into

I took over Homefeed CG in September 2024: roughly twenty engineers, strong technical bones, and morale at its recorded low — the September 2024 EVS read 7.1 engagement, 6.8 management support, 5.9 recognition. The prior EM moved back to an IC role, where he has since been more effective. The bets that defined the next eighteen months were set in my first few months, and they were my calls: double down on CLR as the successor to the heuristic CG stack, keep the LWS engine compounding, modernize the two-tower retrieval line, and run the whole portfolio on an incubation cadence — one funded frontier bet a year, graduated or sunset on evidence. (§2's list: LWS was 2023's bet, before I arrived; CLR was mine for 2024.)

The organizational turnaround ran in parallel: the twenty-person group split into two subteams with clear swim lanes, a real TL bench (three IC16s and an IC15) empowered with area ownership, Bowen's transition to first-time EM, and six new hires on the way to ~50% growth. By March 2025 the EVS read 8.4 engagement / 9.8 management support / 9.4 recognition, and it held through September. One paragraph on this because §3 is a technical history — but the people arc is the reason the technical one happened.

### 2025 — the CLR year

**The cumulative 2025 numbers, as tracked in the launch log:**

| Metric | 2025 cumulative |
|---|---|
| Total Successful Sessions (SSv2) | +2.12% |
| Save / Revisitation / Social / Download sessions (SRSD, SSv2) | +2.27% |
| Homefeed Repins | +22.52% |
| Weekly Active Users | +0.33% |
| Daily Active Users | +0.17% |

On cost: the per-launch savings claims sum to roughly $4.5M annualized — closer to $5M counting the $500k credited to P2P for the Navboost GSS migration — against about $180k in accepted cost increases. Treat the total as directional: at least one item is probably double-counted (interest-service savings appear on both the enabling CLR launch and the final deprecation).

**The headline is CLR.** The biggest modeling initiative of the year, and the story the cumulative numbers mostly tell: Conditional Learned Retrieval went from an interests-only technique in January to the general conditioning framework of the stack by December — and each expansion let us deprecate the heuristic CGs it replaced rather than carry them forever. Interest CLR retired the interest-service use cases and, by November, the service itself ($424k); Board CLR replaced the board-based CG budgets on the grid and put ~+140k global MAU on the board doing it; Pin CLR closed the year at HF long clickthroughs +2.41%. Gains at every replacement, and a simpler system after each one. The launch-by-launch record is in area 2.

**The infra and cost campaign.** A deliberate, year-long line of deprecations and optimizations, anchored by JJ:

- [Interest Service fully deprecated](https://pinterest.slack.com/archives/C0145F4SW9G/p1763678558103699) (Nov) — $424k; topicfeed, SEO, notifs, and bestpin use cases migrated into unity-homefeed. The CLR launch that made it possible is in area 2's record.
- Index and data reductions — [Apiary index reduction](https://pinterest.slack.com/archives/C05UMECTDDJ/p1742410424419839) ($360k, Mar), [chunk-invalidation deprecation](https://pinterest.slack.com/archives/C05UMECTDDJ/p1738019384245619) ($180k, Jan) with the follow-on [subchunk ablation](https://pinterest.slack.com/archives/C05UMECTDDJ/p1765413405679339) ($111–140k, Dec), [UCPD pin-selection data deprecation](https://pinterest.slack.com/archives/C05UMECTDDJ/p1765828625983819) ($183k, Dec), and [ItemSage embedding quantization](https://pinterest.slack.com/archives/C05UMECTDDJ/p1754606731956039) ($29.6k, Aug).
- [Navboost P2P query-expansion migration to GSS](https://pinterest.slack.com/archives/C05UMECTDDJ/p1752187888854679) (Jul) — neutral metrics, and it helped P2P retire a Manas cluster ($500k, credited there).
- [Aperture Flink migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1757536190743189) (Sep) — $82k and the first step off the legacy PinPin workflows.

**Shopping retrieval.** Wei-Ting and JJ's corpus line, plus a serving-efficiency capstone:

- [Corpus iterations for merchant diversity](https://pinterest.slack.com/archives/C05UMECTDDJ/p1741884764749959) (Mar), [offsite conversion items](https://pinterest.slack.com/archives/C05UMECTDDJ/p1744925845556009) (Apr — US WAU +0.17%), [item-pin selection v7](https://pinterest.slack.com/archives/C05UMECTDDJ/p1744994460115069) (Apr — HF trustworthy fresh impressions without ads +5.79%, pin reports −7.85%), and [corpus + CG size tuning](https://pinterest.slack.com/archives/C05UMECTDDJ/p1758919208235309) (Sep — TMPL-excl-Etsy HF impressions +7.30%).
- [Shopping load tuning with reinforcement learning](https://pinterest.slack.com/archives/C05UMECTDDJ/p1763511551356659) (Nov) — a learned layer deciding how hard to load the shopping path: $260k saved with sitewide repins +0.51%.

**New-user work with Activations.** The NUX line — Jenny, Zihao, and Lingzhi with the Activations team; the surface is theirs, the CG work was ours:

- [New User Onboarding Revamp](https://pinterest.slack.com/archives/C073LHUATAB/p1750710687360639) (Jun) — replaced the topic picker with use cases and sample pins, with [CG budget tuning](https://pinterest.slack.com/archives/C05UMECTDDJ/p1741986856092679) behind it (Mar — SSv2 sessions +0.91%, HF time spent +2.31%).
- [NUX-TT](https://pinterest.slack.com/archives/C05UMECTDDJ/p1761685357062779) (Oct) — a dedicated two-tower CG for new and low-signal users: +0.8% 14d WAU; [expanded to all NUX and resurrected users](https://pinterest.slack.com/archives/C05UMECTDDJ/p1765217743107349) in Dec.
- [Viewer demographic features in Pinnability](https://pinterest.slack.com/archives/C05UMECTDDJ/p1761078628991149) (Oct) — +0.9% 14d WAU, and a pattern the log flags as applicable to every HF CG.

Two smaller 2025 items worth knowing exist: the [first See More adoption in HF retrieval](https://pinterest.slack.com/archives/C05UMECTDDJ/p1754437085563129) (Aug, with an Oct [time-weights follow-up](https://pinterest.slack.com/archives/C05UMECTDDJ/p1760053649721209)), and [negative-signal interest filtering](https://pinterest.slack.com/archives/C05UMECTDDJ/p1748023005202089) (May — HF interest hides −12.79%).

### LWS + L1 Utility — the engine that never stopped

The oldest incubation on §2's list (2023, before I arrived) and the steadiest scoreboard we have. 2025 read like a metronome — training-stack modernization, the L1/L2-alignment campaign, evaluation science, GPU serving — the launch-by-launch record is in area 3. L1 Utility is the line's 2025 incubation graduate: a first-in-Core business-control layer between preranking and ranking that now carries the shopping, freshness, and diversity knobs (area 4). The line also produced the org's publishing flag: the preranking paper accepted at RecSys with an oral, Hedi lead author. The H1 2026 chapter kept the pace: the training-serving alignment rebuild that fixed a years-old 20× objective distortion, the Unified Tower on GPU with the largest report reduction on record (−12.72%), a training-data line worth $126k/yr, and July's GPU model scaling. Area 3 has the launch-by-launch record.

### Multi-Embedding — built, published, sunset

The modernization of the main-stack two-tower line, driven by Yuke Yan and collaborators — a genuinely successful arc, and worth telling in full because of how it ends:

- [Multi-Embedding replaced single-embedding retrieval](https://pinterest.slack.com/archives/C05UMECTDDJ/p1737572814741049) (Jan 2025) — differentiable clustering to capture distinct user interests; a genuinely new paradigm for two-tower retrieval, later accepted at KDD 2025.
- [Model-farm migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1738870441029699) (Feb) — 4× model capacity, which reads as 4× experiment velocity; large-ID-embedding iteration became possible at all. [Ray + mixed precision](https://pinterest.slack.com/archives/C05UMECTDDJ/p1736814345772019) had already bought 80% training throughput in Jan, and [ARF + ID embeddings](https://pinterest.slack.com/archives/C05UMECTDDJ/p1746574717967769) (May) fully productionized ME with 3-day retrains and $236k saved.
- A fast feature cadence all year — [OmniSage + UVE](https://pinterest.slack.com/archives/C05UMECTDDJ/p1736290438322359) (Jan), [sequence tuning to L350](https://pinterest.slack.com/archives/C05UMECTDDJ/p1750181539495689) (Jun), [Swish + cosine schedule](https://pinterest.slack.com/archives/C05UMECTDDJ/p1752597482418049) (Jul), [time embeddings + closeup sequence](https://pinterest.slack.com/archives/C05UMECTDDJ/p1753910233721999) (Jul — the first temporal information and the first closeup-sequence adoption in retrieval), [PinCLIP](https://pinterest.slack.com/archives/C05UMECTDDJ/p1755878411983569) (Aug), and [UOEv3 / DERM](https://pinterest.slack.com/archives/C05UMECTDDJ/p1759273867020149) (Oct — first time UOE V3 features paid off in ME).
- [Fresh-pins](https://pinterest.slack.com/archives/C05UMECTDDJ/p1755792006754419) and [expanded-neardup](https://pinterest.slack.com/archives/C05UMECTDDJ/p1759769828063359) freshness injections (Aug–Oct) — HF 28d-fresh impressions +1.02%, fresh long clickthroughs without ads +4.04%.
- Serving and quantization — [Manas quantization](https://pinterest.slack.com/archives/C05UMECTDDJ/p1737490967725759) (Jan, $225k), [product quantization](https://pinterest.slack.com/archives/C05UMECTDDJ/p1748377362047569) (May, $148k), and the [viewer tower on GPU](https://pinterest.slack.com/archives/C05UMECTDDJ/p1759848557880399) (Oct) — our first retrieval model served on GPU: P99 latency 99ms → 17ms, $150k.
- [Training data to Iceberg UID-sort](https://pinterest.slack.com/archives/C05UMECTDDJ/p1759244355967909) (Oct) — ME trained on the same data as Pinnability, unifying the retrieval–ranking data pipeline; $330k.

Then the honest turn, and the one I want this table to internalize: **we defunded ME.** By H1 2026 we were carrying two next-generation retrieval paradigms — ME and RecGPT — competing for the same candidate budget and the same investment dollars, and RecGPT was winning on ceiling: by April 2026 it was the top-performing CG on Homefeed. The call was consolidation: ME's candidate budget moved to RecGPT, the line went to maintenance, and the modeling energy followed the winner. The line was still delivering when we called it — a [4× training speedup](https://pinterest.slack.com/archives/C05UMECTDDJ/p1768424327996589) in January (19.3h → 4.75h, with clickthrough gains riding along) and [full-funnel retrieval modeling](https://pinterest.slack.com/archives/C05UMECTDDJ/p1774905507502699) in March — which is exactly the point: we sunset it on portfolio evidence, not on failure. The concrete close: on June 30, [150 sizers moved from ME to RecGPT](https://pinterest.slack.com/archives/C05UMECTDDJ/p1782851752999499), roughly doubling RecGPT's pin coverage. A KDD-published paradigm we built ourselves, sunset on evidence — that is §2's graduation-or-sunset discipline being real rather than rhetorical.

### RecGPT — the successor paradigm

The 2025 incubation that became the top candidate generator on Homefeed. The H1 2026 arc, launch by launch: [established as an HF candidate generator](https://pinterest.slack.com/archives/C05UMECTDDJ/p1769480099905659) in January — HF repins +0.86% (unique users) with serving cost driven from $970k to $571k and then to ~$300k/yr; cost was the launch blocker, and we broke it. [Onto BMI the next day](https://pinterest.slack.com/archives/C05UMECTDDJ/p1769641976895319) as the first unified L0-retrieval + L1-scoring ensemble (BMI repins +3.63%). By April it had exceeded its goal and become the **#1-performing CG across Homefeed**; [Manas migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1776701719670599) landed the same month ($59k/yr, unblocking the SMS path), [diversity improvements](https://pinterest.slack.com/archives/C05UMECTDDJ/p1778094842675639) added +50% pin coverage in May, and on June 30 the ME sizer inheritance took impression share up +89%. The ceiling question now is impression share, not model quality. The full state is area 10.

### Retentive Recs — vision to validation

The retention charter came out of the Anticipation Vision — Andrew, Dylan, and Mira's authorship, amplified publicly by Matt Madrigal as one of the things he's most excited about for Pinterest personalization — and Retentive Recs is its named technical key. The 2025 groundwork ran through CLR: [PinnerSpark interests](https://pinterest.slack.com/archives/C05UMECTDDJ/p1757021202811669) (Sep 2025 — WAU +0.11%, use-case adoption +0.12%) and [User Interest Cluster v2](https://pinterest.slack.com/archives/C05UMECTDDJ/p1767729395300429) (LR posted Jan 6, 2026, straddling the year boundary — DAU +0.17%, WAU +0.14%, ~$322k saved), which built the pipeline that predicted-UIC feeds today.

H1 2026 kept the line compounding: [frontier sampling](https://pinterest.slack.com/archives/C05UMECTDDJ/p1772557075488349) shifted UIC retrieval toward exploration (Mar — SSv2 +0.22%, and the first evidence for predicted UIC), [UIC diversification in SSD](https://pinterest.slack.com/archives/C05UMECTDDJ/p1777065083952529) landed on the honest second attempt (Apr — V1 was withdrawn as irreproducible after the January fresh-content spike, the team's own call), and [new-use-case rewards](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780676924633739) put clean DAU/WAU cells on the board (Jun — +0.092% / +0.066%, concentrated in non-core and casual users). April 2026 is when the bet stopped being a hypothesis: a program-level UCAN holdout validated top-line WAU lift in our largest market. The engineering blog post shipped April 17; Jeff amplified it in #core-eng in late July; the KDD 2026 paper went in July 31. Where it stands now — dual pUIC tracks converging, Chuxi as TL — is area 5's story.

### UPP — built once, everywhere

The bet that we build personalization once, centrally, instead of every surface training its own variant — Jeff has been a proponent since inception. The lineage runs straight through the record above: the Homefeed retrieval line proved the components; UPP is their generalization. Bowen carried the retrieval layer until his departure in March 2026; Piyush has held the full architecture since. The proof points so far: Notifications launched on it in Q1 2026, and the notif line has kept compounding — UPP Retrieval CLR V0 delivered +156k global WAU (stat-sig, OEC neutral) with broad email/push engagement lifts, V1 +130k, and the v2 iteration flipped the win to MAU (+226k stat-sig) with content-quality gains riding along. On the model side, the [Foundation Model integrated into HF CLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780360528626209) in June — HF repins +0.85%, repin-rate lifts on every CLR CG (Board CLR +7%) — crucial for scaling the UPP base model, with download and freshness trade-offs named rather than buried. V0 beat P2P's production model head-to-head — SSv2 wins in US and Canada, engagement wins globally; Search is adopting; V1's foundation-model component has been building since June. The P2P launch is gated (relevance recovery and the P10 WAU check) — the full state is area 1.

### Reflex and the AI tooling line

Ground rule 8 has a history; AI-first started as practice and became a program. Pinkerton began as a summer-2025 hackathon prototype and shipped its first production milestone in April 2026. PINvestigator was built inside the H1 2026 metric investigations, demoed to Jeff that April, and has been in regular weekly investigative use since. Reflex itself started as Andrew's autonomous-diagnostics prototype; we moved to explicit co-development in April 2026, Dafang took technical lead in May, Tim came on as PM, and Shifu folded in at the end of July on the strengths framing (Shifu ahead on Build, Reflex ahead on discovery). Dylan named the POC trio — me, Dafang, Tim — on August 1. Simulate demos mid-August. And by June, Reflex had production launches of its own — the first agent-surfaced, agent-implemented experiment shipped June 4 (area 9). The program state is area 9.

### The year-over-year read (as of August 2026)

Both logs are threaded above, so here's the honest compare — same naive cumulative-sum method both years, with one asymmetry worth knowing: the 2026 tracker is *stricter* about what counts (withdrawn results, pre-AA flags, regressions named), so the two totals aren't inflated equally:

- **Pace — read it with the capacity context.** 2025 delivered +2.12% SSv2 across the full year, with essentially the whole org feeding that number. H1 2026 sums to **~+1.5%** through late July (my own reconciliation, 8/8) from ~40 launches — matching 2025's pace *while a real fraction of our best capacity sat in two 0→1 bets that by design pay nothing into SSv2 yet* (UPP gated pre-launch on P2P, retentive recs in its convergence lull). Same engine output, smaller engine share — and measured under stricter rules.
- **Mix.** 2025's impact was engagement-harvest: one flagship (CLR) on essentially one surface, the LWS metronome beside it, funded by a ~$4.5M deprecation campaign. H1 2026 is a portfolio: five independently delivering lines — CLR, LWS + L1, RecGPT, Retentive Recs, UPP-on-notifications — across four surfaces, with savings redeployed into new engines rather than banked.
- **Retention — and none of it shows in the SSv2 comparison.** From byproduct to product line. 2025's single biggest absolute-count win was Board CLR (~+120k WAU / +140k MAU); the H1 2026 notification launches each beat it — +156k WAU (V0), +130k (V1), +226k MAU (v2) — the largest per-launch retention numbers in either log, on a surface the 2025 log barely touched. (Listed per-launch, not summed: the V1-vs-V0 baseline question is open.) Add UIC signals and NLFU responsiveness as the other two mechanisms, plus the April program-level holdout validation. Retention is what this org was funded on — this is the trajectory line that matters most, and it's banked, not pending.
- **The discipline completed its first full cycle.** 2025 demonstrated incubate-and-graduate. H1 2026 added the half most teams never do: sunsetting our own KDD-published paradigm on portfolio evidence.
- **A capability class that didn't exist.** Zero AI-in-the-loop launches in 2025. H1 2026 has production experiments detected *and implemented* by agents, an agent-driven CG deprecation with real SSv2 gains, and AI-tuned budgets.
- **The caveat to hold.** 2025's wins were banked; 2026's biggest are still in flight — UPP's P2P gate, both pUIC experiments, and Intelligent Boards all resolve in the next quarter, more simultaneous unresolved bets than this team has ever carried. That is the context for every prioritization call we make this fall.

### August 2026 — the reorg that created this org

Announced August 5: the Homefeed CG name retired, P13N Retrieval created. Daniel's team re-parented intact from Yan Li's org; Alim hired externally (Etsy; anticipation-ML background), starting a week early on 7/27. The design is deliberately two-phase: T1 now — minimal moves, interim assignments as in §4's table — and T2 in October–November, when we decide the durable shape together, with input from the team. The rest of this document is that work.

---

## 4. The workstreams — areas and leads

Ten areas, each with a TL and an EM. Over the next two months we decide the long-term structure (T2: October–November), with input from all the team members.

A note on the shape of this list, because it's deliberate. These are **areas, not teams**: capabilities named durably, so the product bets inside them can graduate or sunset without redrawing the map ("LLM for Recommendations" survives even if a given MVP doesn't). Every area carries **one TL and one EM** — a single accountable pair, and a visible map of where the leadership seats are. The list is **flat on purpose**: areas are the stable unit; which areas cluster into which team is exactly the T2 decision, and I don't want today's execution to pre-draw November's structure. And where a funnel genuinely crosses org lines — Retentive Recs — the legs are named explicitly, with leads in other orgs, because accountability follows the funnel, not the reporting line. Cross-org initiatives sit in their own list (§5): obligations with named leads, not charters.

| # | Area | TL | EM |
|---|---|---|---|
| 1 | UPP Retrieval | Piyush | James |
| 2 | Conditional Learned Retrieval | Devin | James |
| 3 | Lightweight Scoring | Yali | James |
| 4 | Responsiveness, L1 Utility | JJ | James |
| 5 | Retentive Recs (UIC, pUIC) | Chuxi (Retrieval) · Andreanne (Blending) · Simin (UU) | Alim (Retrieval) · Rahul (Blending) · Yingjian (UU) |
| 6 | Unified Explore Backend | Roderick | Daniel |
| 7 | LLM for Recommendations (Intelligent Boards, etc.) | Balaji | Daniel |
| 8 | Collection Personalization (Recommended Boards, etc.) | Yongwoo | Daniel |
| 9 | Reflex | Dafang | James |
| 10 | RecGPT / Generative Retrieval | Bella | James |

### 1. UPP Retrieval — TL: Piyush · EM: James

UPP is the bet that we build personalization once, centrally, instead of every surface training its own variant. It owns the cross-surface user representation and the retrieval substrate that CLR and LWS consume. If it works, every leg of this org gets faster and cheaper at the same time. That is also why it's the most contested thing we own — when a substrate starts winning, everyone develops an opinion about where it should live.

Where we are: V0 beat the P2P production model head-to-head. SSv2 wins in US and Canada, engagement wins globally. We are not launched. Semantic relevance regressed, and the launch is gated on recovering b2.5pre@4 (organic) to above −0.3% — it sits at −2.17% today. The P2P team is on it: bundling the post-ranking utility relevance change with our experiment, pushing irrelevant pins down per CG, and testing a different sampling scheme in parallel. One to two weeks before we know. The P10 WAU drop is the second blocker. Meanwhile Search is adopting V0 and is worried about GPU capacity on their side. Training time used to be the concern; the V1 improvements made it roughly neutral.

- **Staffing:** Piyush (TL) with Zihao on cross-surface training. Partner side: Yifan Li, Fan Jiang, Jiaxing Qu from P2P — Jiaxing is at 50% and I'm resolving whether that becomes 100% or two people, with Sai Xiao next week. *[Full contributor map: fill in at walkthrough.]*
- **The Curation ML leg:** Daniel's UPP ML Foundation program (Kim as DRI — unified data pipeline, SearchSage CLR, notification label volume recovery; PM Matt Chun) is the substrate's second engine room. That's how UPP stays "consumed, not shared" while still being built by more than one team.
- **Launch history:** none yet on P2P — V0 is the first launch candidate there. Elsewhere the record is building:
  - 2025 groundwork: the [CLR feature-alignment launch](https://pinterest.slack.com/archives/C05UMECTDDJ/p1765218319127799) (annotations v7 + legacy feature deprecations, Dec 2025) aligned HF CLR training data for a unified base model across HF and notif surfaces — fresh repins +2.50%, HF interest repins +6.92%.
  - Notifications (2026): **UPP Retrieval CLR V0** — global WAU +156k (stat-sig), OEC neutral, broad email/push engagement lifts; **V1** — WAU +130k (stat-sig); **v2** — MAU +226k (stat-sig), engagement flat, with content-quality wins (racy −3%, low-quality −4.3%). *[Two tracker flags to confirm: whether V1 is measured against V0's baseline or on top of it, and the sign convention on the v2 slop metric.]*
  - [UPP: Foundation Model in CLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780360528626209) (Jun) — the FM integrated into the unified HF CLR model: SSv2 +0.07%, HF repins +0.85%, repin-rate lifts on every CLR CG (Board CLR +7%); accepted trade-offs on downloads (−1.53%) and freshness, named in the LR. Crucial for scaling the UPP base model.
  - *[Experiment-by-experiment P2P history: I'll walk you through it live.]*
- **Risk:** high. Ambitious modeling, contested ownership, and delivery now partly dependent on other orgs' capacity (P2P eng, Search GPUs).
- **Work type:** genuinely both. Deep modeling (cross-surface training in a batch, weighting, loss functions, optimizers) and serious systems work (serving paths, GPU efficiency).
- **Strategic weight:** the highest-leverage thing we own. It's also the org's most visible story upward — treat anything UPP-related as exec-facing by default.
- **Politics:** there's an active discussion above us about where the personalization substrate should live; I'm handling it, but you should know it exists. The launch is deliberately being run through the new decision process as an exemplar, which means the trade-off calls get made above me — that's protection, not exposure, as long as we disclose first. Relevance-side partners (Kurchi's team) are warm as of this week; keep them that way.
- **AI leverage:** *[honest placeholder — the training/eval loop has room for it; I haven't mapped this.]*
- **Leadership runway:** the Search extension is a real second act for whoever drives it, and the cross-org seat on this work is the most visible IC platform in the org.

### 2. Conditional Learned Retrieval (+ GULP) — TL: Devin · EM: James

Frontier retrieval modeling on the main candidate-generation stack, including GPU-served retrieval in production. GULP rides with CLR. This has historically been one of our most reliable sources of gains — and we deliberately under-funded it in H1 while capacity went to UPP and Retentive Recs. We've been harvesting an engine we stopped investing in. That's a choice with a shelf life, and part of why Ryan and Rui come in on the engineering side this half, likely starting with serving efficiency.

- **Staffing:** Devin (TL) with Yichi; Ryan and Rui joining on engineering this half.
- **Launch history (2025):** the deepest gains record in the log, even in a deliberately under-funded year. The arc that matters: CLR started the year as an interests-only technique and ended it as a general conditioning framework.
  - [CLR on Recommended Interests + Unity migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1736186706302699) (Jan) — SSv2 +0.22% (P6 +0.46%), and it deprecated the interest-service use cases that funded the later shutdown (>$350k).
  - [CLR for Board More Ideas](https://pinterest.slack.com/archives/C05UMECTDDJ/p1736873003693229) (Jan) — the first application beyond the interest grid: BMI time spent +2.11%, repins +3.79%. The log credits this launch with setting the expand-CLR agenda for the whole year.
  - [Unified Interest + Board CLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1747156807722349) (May) — one model where four-plus were headed: ~21 eng-weeks a year saved, training 70% faster with conditional filtering. Enriched the same month with [large ID embeddings + OmniSage/UVE](https://pinterest.slack.com/archives/C05UMECTDDJ/p1747950234242069) (HF interest repins +27.77%).
  - [Board CLR replacing board-based CG budgets](https://pinterest.slack.com/archives/C05UMECTDDJ/p1750447116383969) (Jun) — the headline launch: global MAU +0.06% (~+140k users), WAU +0.08% (~+120k), SSv2 +0.18%, HF downloads +2.15%, $50k saved.
  - [Single Scorpion request](https://pinterest.slack.com/archives/C05UMECTDDJ/p1759772029867969) (Oct) — all condition-model requests collapsed into one: $350k, and the prerequisite for GPU serving and request-level feature optimization. [Fresh-pins injection](https://pinterest.slack.com/archives/C05UMECTDDJ/p1759860794391089) landed the same month (HF fresh repins without ads +7.01%).
  - [Conditioned user sequence](https://pinterest.slack.com/archives/C05UMECTDDJ/p1763420412291149) (Nov) — sequence modeling in CLR for the first time; the log is explicit that this is the baseline most 2026 CLR/FM modeling builds on.
  - [Pin-based CLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1765288812801759) (Dec) — pins as a condition: SSv2 +0.13%, HF long clickthroughs +2.41%; opens UIC-signal retrieval and the notif landing-page surface.
  - GULP: BMI became the first HF-powered surface on the GULP backend — [H1 groundwork](https://pinterest.slack.com/archives/C05UMECTDDJ/p1752707334520919) (Jul), [CG + blending migration complete](https://pinterest.slack.com/archives/C05UMECTDDJ/p1762464743739679) (Nov).
- **Launch history (H1 2026):** under-funded and still compounding — plus the engineering hardening that came with Ryan's arrival.
  - Modeling: [Semantic IDs for long-tail](https://pinterest.slack.com/archives/C05UMECTDDJ/p1768924779474889) (Jan — SSv2 +0.13%, strongest for new-user cohorts), [DHEN feature reweighing](https://pinterest.slack.com/archives/C05UMECTDDJ/p1769031767040289) (Jan — repins +0.27%, Interest CLR repins +1.32%), [router simplification](https://pinterest.slack.com/archives/C05UMECTDDJ/p1775519133081589) (Apr — repins +0.39%; conditions become config mappings, unblocking Search CLR on HF and Semantic-ID conditions), [indyRank/pageRank feature deprecation](https://pinterest.slack.com/archives/C05UMECTDDJ/p1776363549969239) (Apr — deleting two stale features *gained* +0.43% repins: feature hygiene as engagement work), [ARF stabilization](https://pinterest.slack.com/archives/C05UMECTDDJ/p1778005051946709) (May — sitewide repins +0.81%, fresh neardup repins +5.40%, with a named shopping-clickout regression).
  - Serving: [GPU serving via attached data](https://pinterest.slack.com/archives/C05UMECTDDJ/p1774896000652059) (Mar — **$650k saved, model latency −85%**; approved with named intent/non-shopping-clickout regressions and the CG-distribution-shift hypothesis still under confirmation — the honest version of a big win). [Claude-tuned condition budgets](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780068356468789) (May — SSv2 +0.18%, exploiting the freed GPU capacity; AI-in-the-loop). [Pin CLR on BMI-on-GULP](https://pinterest.slack.com/archives/C05UMECTDDJ/p1773417052639199) (Mar — BMI repins +4.24%, unlocking Pin CLR for the notif landing page and exploration modules).
  - Config hardening (Ryan): [Unity Experiment Configuration migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1782410368379009) (Jun) and [Manas dynamic-field indexing](https://pinterest.slack.com/archives/C05UMECTDDJ/p1784744650552249) (Jul) — model config through the normal code lifecycle: less oncall, no per-model boilerplate PRs, AI-agent-editable.
- **Risk:** low on delivery, real on concentration — too much of it lives in Devin's head.
- **Work type:** deep modeling at the core, with a meaningful GPU-serving systems layer.
- **Strategic weight:** the workhorse of the main stack. Retention of gains here buys us the room to place bets elsewhere.
- **Politics:** quiet today. Its end placement is an open design question, which makes it the workstream most likely to be discussed by people not in this room — rule 7 applies.
- **AI leverage:** *[placeholder — candidate: AI-assisted experiment triage; not mapped.]*
- **Leadership runway:** a TL bench question more than a TL question — who backs Devin up is an org-level gap we've named but not proven.

### 3. Lightweight Scoring — TL: Yali · EM: James

Lightweight preranking — the reliable gains engine of the org, and the oldest incubation on §2's list. It just keeps delivering: GPU serving productionized and stable, the training pipeline re-architected from forty-plus hours down to about seven, and the preranking paper accepted at RecSys with an oral. See More / See Less has its retrieval-side home here. Oncall moved with the charter on day one.

- **Staffing:** Yali (TL) with Hedi.
- **Launch history (2025):** the log reads like a metronome — modeling, serving, and evaluation advancing at once.
  - Training-stack modernization — [Ray adoption](https://pinterest.slack.com/archives/C05UMECTDDJ/p1738348976419399) (Jan: throughput 138k → 305k examples/sec, training 17h → 8.5h), the [auto-retrain framework](https://pinterest.slack.com/archives/C05UMECTDDJ/p1736383505853879) (Jan: HF time spent +0.37%), and the [SOAP optimizer](https://pinterest.slack.com/archives/C05UMECTDDJ/p1741970550753649) (Mar: SSv2 +0.19%).
  - The L1/L2-alignment campaign — the quiet theme of the year: [OmniSage + UVE features](https://pinterest.slack.com/archives/C05UMECTDDJ/p1741654477038219) (Mar), the long-impression [distillation](https://pinterest.slack.com/archives/C05UMECTDDJ/p1743706304255179) and [training-objective](https://pinterest.slack.com/archives/C05UMECTDDJ/p1749240681217589) deprecations (Apr/Jun: HF reports −14.67% and −10.92%), [pairwise loss](https://pinterest.slack.com/archives/C05UMECTDDJ/p1744914999260489) (Apr), [L1 calibration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1742241633880649) (Mar), and [learnable gating for UOE/DERM features](https://pinterest.slack.com/archives/C05UMECTDDJ/p1760731988281299) (Oct: total time in app +0.21%).
  - Evaluation science — Hedi's [online alignment metrics](https://pinterest.slack.com/archives/C05UMECTDDJ/p1747244009848059) (May) and [offline replay](https://pinterest.slack.com/archives/C05UMECTDDJ/p1762371808654119) (Nov): the first reliable quantitative forecast of online metric shifts for pre-ranker models, and a framework the log notes is used beyond this team.
  - [GPU serving and model scale-up](https://pinterest.slack.com/archives/C05UMECTDDJ/p1761252306724919) (Oct) — SSv2 +0.17% and the door open to next-generation architectures.
  - [Calibration data to Iceberg](https://pinterest.slack.com/archives/C05UMECTDDJ/p1762301780573529) (Nov) — ~$220k a year.
- **Launch history (H1 2026):**
  - [Training-serving alignment](https://pinterest.slack.com/archives/C05UMECTDDJ/p1773963091524149) (Mar) — redesigned the training objective from first principles and fixed a years-old distortion: the repin:closeup weight ratio was 20:1 in training but 400:1 at serving. SSv2 +0.10%, HF hides −4.40%.
  - [Unified Tower + Transact on GPU](https://pinterest.slack.com/archives/C05UMECTDDJ/p1773177168614229) (Mar) — replaced the split CPU/GPU two-tower architecture: HF reports −12.72% (largest reduction on record), unblocking foundation models and 16k sequences.
  - [Rank distillation loss](https://pinterest.slack.com/archives/C05UMECTDDJ/p1777919860405979) (May — the student learns the teacher's ordering, not just pointwise scores; HF clicks +1.15%).
  - The training-data line: [funnel-log removal](https://pinterest.slack.com/archives/C05UMECTDDJ/p1779409650194399) (May — $46k/yr) and [PROD→L2-dataset migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1784675597815519) (Jul — SSv2 +0.20%, $80k/yr).
  - [Model scaling on GPU](https://pinterest.slack.com/archives/C05UMECTDDJ/p1785359965349809) (Jul — RMSNorm + batched MaskNet + larger head: SSv2 +0.12% at neutral latency and cost).
  - The CG-onboarding arc: [BoardCLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1767991644190129) (Jan) then [the shopping CGs](https://pinterest.slack.com/archives/C05UMECTDDJ/p1775853312102959) (Apr — 55 thread replies) took LWS/L1 coverage of CG budgets from 68.9% to ~79%, with trustworthy-product outbound click rate +10.39% — evidence LWS picks genuinely better product pins.
- **Risk:** concentration. A great deal of reliable output depends on two people.
- **Work type:** modeling-led with a solid serving-systems spine.
- **Strategic weight:** the steadiest scoreboard we have, and now a publishing flag too (the RecSys oral).
- **Politics:** See More / See Less is a co-ownership seat with the front end (Yali with Raymond Hsu, no primary or secondary) and it's high-visibility. Success criteria for that seat are still being firmed up — I own that conversation.
- **AI leverage:** *[placeholder.]*
- **Leadership runway:** Hedi is having a real moment (lead author, oral at RecSys). The question of who presents, and how we stage it, is open and worth doing deliberately.

### 4. Responsiveness, L1 Utility — TL: JJ · EM: James

Mid-funnel utility selection — the shopping, freshness and safety knobs, diversity controls — plus in-session responsiveness. L1 Utility was 2025's incubation graduate (a first-in-Core launch), and the serving-optimization line around it has been one of our best cost stories. Note the split from area 3 is deliberate: Lightweight Scoring is a modeling engine; this is where business control meets the funnel, and it deserves its own accountable pair. L1 and real-time ops sit with Rui under Foundations & Efficiency — ops placement and TL accountability are different things, on purpose.

- **Staffing:** JJ (TL). *[Roster beyond JJ: fill at walkthrough.]*
- **Launch history (2025):**
  - The L1 serving line — [mini-batch serving optimization](https://pinterest.slack.com/archives/C05UMECTDDJ/p1741107892271839) (Mar: $345k) extended to [BMI and HFNP](https://pinterest.slack.com/archives/C05UMECTDDJ/p1745594528225029) (Apr).
  - [L1 Utility itself](https://pinterest.slack.com/archives/C05UMECTDDJ/p1756830835739129) (Sep): a business-control layer for diversity, shopping, and freshness ahead of Pinnability — HF pin hides −3.46%, P99 latency −35ms, $115k.
- **Launch history (H1 2026):** the L1 layer matured into the org's control plane, and the responsiveness charter put its first big point on the board.
  - The L1 Utility arc: [UIC & SID diversity control](https://pinterest.slack.com/archives/C05UMECTDDJ/p1769104749291599) (Jan — first use of L1 for global cross-CG control; the $37k cost increase was itself a success signal: better diversity drove more searching), [presort cutoff 1.3×→1.7×](https://pinterest.slack.com/archives/C05UMECTDDJ/p1774030092822119) (Mar — the cheapest win-per-effort in the tracker), [iterative diversity](https://pinterest.slack.com/archives/C05UMECTDDJ/p1781198598004049) (Jun — SSv2 +0.17% for one added for-loop) with its [latency-recovering follow-up](https://pinterest.slack.com/archives/C05UMECTDDJ/p1783548180035799) (Jul — p99 −5.7ms).
  - Serving: [dynamic sizer migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1775758163913739) (Apr — async model-driven sizing, unblocking all future PHP models; 67 thread replies), [sub-chunk request CG](https://pinterest.slack.com/archives/C05UMECTDDJ/p1779395517757559) (May — recycles unconsumed pins straight from the chunk cache, skipping LWS and Pinnability entirely: SSv2 +0.14%, $48k saved), [deep-RL shopping load tuning](https://pinterest.slack.com/archives/C05UMECTDDJ/p1778691704025289) (May — the neural successor to 2025's tabular policy: SSv2 +0.15%, P6 countries).
  - Responsiveness: [closeup cache invalidation for NLFUs](https://pinterest.slack.com/archives/C05UMECTDDJ/p1783447873989479) (Jul) — one of the largest NLF WAU wins to date (+37k WAUs, p=0.03), shipped on the legacy user-context sequence ahead of the real-time one; feeds the NLFU initiative in §5.
- **Risk:** JJ is the most-loaded name on this map — TL here, Build lead in Reflex, anchor of the infra campaign, and named on two cross-org initiatives (§5). That concentration is a design input for T2, not a footnote.
- **Work type:** systems-led with business-logic judgment; the responsiveness side adds a real-time flavor.
- **Strategic weight:** the layer where topline, cost, and safety trade off explicitly — which makes it the natural home of the org's efficiency story.
- **Politics:** quiet. The knobs it owns (shopping load, freshness, safety) are exactly the ones other orgs ask about first — disclose-first applies.
- **AI leverage:** *[placeholder — the RL load-tuning launch suggests the pattern generalizes.]*
- **Leadership runway:** the TL seat itself is the growth story here, and whoever picks up the responsiveness charter properly gets a lane nobody else is in.

### 5. Retentive Recs (UIC, pUIC) — a three-legged program

**Leads:** Retrieval — Chuxi (TL) / Alim (EM) · Blending — Andreanne (TL) / Rahul (EM) · UU — Simin (TL) / Yingjian (EM)

Retention-optimized recommendations: predict the interests that bring a Pinner back, and have the content ready when they arrive. Two predictive user-interest tracks — model-based and LLM-based — plus the feedback loop that closes it. This is the org's one deliberately three-legged program: retrieval here, blending and user understanding in their own orgs, with a TL/EM pair named per leg — because accountability follows the funnel, not the reporting line. It runs on a standing sync cadence across the legs.

We're in a deliberate launch lull while both tracks converge: model-based is ahead but carries serving-path debt; LLM-based isn't performing yet and is being repositioned. Both experiments land in the next few weeks. I'll be blunt about the stakes: this leg carries retention, retention is the metric the anticipation vision was funded on, and the program's first validated win (the April UCAN holdout, §3) needs successors. That's by design. It's still a risk.

- **Staffing:** Chuxi (TL, Retrieval). Alim's pod — Yidi, Alok, Lionel — staffs the surrounding work. On the LLM track, Ling has been critical (she built much of the LLM inferencing pipeline), with Zoudu, and Ru Chen just joined.
- **Launch history:** the lull is now; the record behind it is real, and it spans all three legs.
  - [UIC signals in CLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1767729395300429) (Jan) — the workstream's foundation: UIC v2 built and fully integrated, replacing legacy followed interest. DAU +0.17%, WAU +0.14%, ~$322k saved, UIC CG engagement on par with the top ML candidate generators.
  - [Frontier sampling in UIC × CLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1772557075488349) (Mar) — landmarks at the boundary of known interests: SSv2 +0.22%, confirmed diversity gains, and the first evidence for predicted UIC.
  - [UIC diversification in SSD](https://pinterest.slack.com/archives/C05UMECTDDJ/p1777065083952529) (Apr) — HF reports −14.82%, hides −2.61%. The V1 before it was withdrawn as irreproducible (the January fresh-content spike had inflated its treatment group) — the team's own call, and the kind of integrity worth naming out loud.
  - [New-use-case rewards in Downstream Rewards](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780676924633739) (Jun) — DAU +0.092% / WAU +0.066% All Users, concentrated in non-core and casual users, plus reusable new-use-case labels beyond Pinnability.
  - [PinnerSpark v0.1 in CLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780533136484609) (Jun) — better LLM, richer pin representation, stale-signal cleanup: markedly strongest for P10 users (in-segment retention WAU +0.34%), with up to ~$250k/yr of cleanup savings.
  - Blending leg (Andreanne): [personalized interest exploration in blending](https://pinterest.slack.com/archives/C05UMECTDDJ/p1782229305520809) (Jun) — one exploration pin per request balancing new-to-app against new-to-user: windowed stat-sig WAU gains, traded against more hides — a deliberate exploration-budget reallocation.
- **Risk:** high, and time-boxed — the next few weeks of experiment results tell us a lot.
- **Work type:** deep modeling, with the LLM track adding a prompt/inference engineering layer.
- **Strategic weight:** this is Alim's charter core and the retention story for the whole org. Evidence here changes every conversation we have upward.
- **Politics:** exec attention on retention is real and personal — results here get read at levels above Dylan. Handle readouts with care: disclose early, frame honestly. And note the LLM-pUIC seam with area 7 (§2's confusion list) — designed overlap, named to be settled.
- **AI leverage:** the LLM-pUIC track *is* an AI-leverage bet on the modeling itself.
- **Leadership runway:** Chuxi is TL on the hardest open problem in the org — the support structure around her is something I want this table to own together.

### 6. Unified Explore Backend — TL: Roderick · EM: Daniel

In Daniel's structure this is the Module Platforms program — Roderick as DRI with Esteban, PM coverage from Anna Kiyantseva, Akshatha, and Emun. Consolidating the explore surfaces so the charter and the systems agree, plus the LLM-track serving side; Lionel has been ramping as Roderick's backend partner from the Retentive side. The charter/reporting-line alignment is on the open list (§6).

*[Daniel: this one's yours — I've deliberately left the substance for you to write. The framing I care about: where does UEB's charter naturally live so its systems and its reporting agree, and what does it need from areas 1 and 5?]*

### 7. LLM for Recommendations (Intelligent Boards, etc.) — TL: Balaji · EM: Daniel

Daniel's Intelligent Board program: Intelligent Boards MVP (offline first), LLM-based pUIC, and Next Board Prediction — PM Emun, Balaji as DRI, Ling at 50%. The area name is deliberate: the charter is the LLM-for-recommendations capability, not any single MVP — bets inside it graduate or sunset without redrawing the map. It's also one of §2's two 2026 incubations, which means a named incubation owner and explicit graduation criteria apply here from day one.

*[Daniel: yours to write — including success metrics with Product, which I care about being explicit before momentum sets them implicitly.]*

### 8. Collection Personalization (Recommended Boards, etc.) — TL: Yongwoo · EM: Daniel

Daniel's Collection P13N program: Board Rec (UGC Board, SMB Board) and Board Ranker (a cross-team project, currently without PM coverage) — Yongwoo as DRI, with Felix and Ling at 50%. A live production surface with real latent upside through surface pairings.

*[Daniel: yours to write. The one thing I'll carry over from my earlier read: product direction here is genuinely unclear to me, and I'd rather understand it properly than decide — this is a walkthrough where I'm mostly listening.]*

### 9. Reflex — TL: Dafang · EM: James

The AI-enabled dev-velocity accelerator: productizing AI-leveraged engineering practice as an internal platform every workstream can adopt. Deliberately small and nimble, measured on adoption and measurable velocity gains. This is the program behind ground rule 8 — PINvestigator is already in regular investigative use, Pinkerton is folded in, and Simulate demos mid-August. Search has active integration interest. Worth noting: Daniel's team already runs an AI Harness line of its own (code-quality agents, ML engineering skills, a curation-ML knowledge base — deliberately "everyone," not a staffed pod), which is exactly the team-level adoption pattern Reflex needs to prove. My honest read: what Reflex needs most right now is a visible, working demonstration — shown, not announced. That's on me to stage.

- **Staffing:** Dafang overall, JJ on Build, Tim on product; Alok owns the Pinkerton line.
- **Launch history:** adoption milestones plus — as of June — production LRs of its own:
  - [Shopping L2R migration to CLR](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780608693645509) (Jun 4) — **the first end-to-end production experiment surfaced by Reflex Detect agents and implemented by the Reflex Build Agent under engineer supervision.** Retired a stale legacy model and part of the 2–3× relevance gap the Detect agents had surfaced.
  - [Following Feed + GraphSage CG deprecation](https://pinterest.slack.com/archives/C05UMECTDDJ/p1784241608815299) (Jul 16) — Reflex-driven removal of the two weakest CGs: SSv2 +0.17%, use-case adoption +0.75%, at neutral cost; shopping/MDD regressions acknowledged and under discussion.
  - Same pattern, adjacent: [Claude-tuned CLR condition budgets](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780068356468789) (May 29) — AI tuning budgets from experiment feedback.
  - §3 has the platform timeline: Pinkerton hackathon → production; PINvestigator; the Shifu fold; Simulate V0 mid-August.
- **Risk:** moderate — the risk isn't technical, it's attention. Programs like this die of quiet neglect, not failure.
- **Work type:** systems and platform work, plus the craft of making AI leverage real in day-to-day engineering.
- **Strategic weight:** this is my flag for the org and it stays with me. It's also the thing Dylan named me the EM point-of-contact for — exec visibility is built in.
- **Politics:** we're absorbing Shifu on a strengths framing — Shifu was ahead on Build, Reflex ahead on discovery. Use that framing, always. No spiking the ball; the people involved read everything we say about it.
- **AI leverage:** it *is* the AI-leverage play.
- **Leadership runway:** JJ's Build ownership is a real leadership lane, and every workstream that adopts Reflex creates an adoption-champion role inside it.

### 10. RecGPT / Generative Retrieval — TL: Bella · EM: James

Generative retrieval in production on Homefeed. I want to say this plainly because it used to get miscast: this is a gains-producing engine, not an experiment. It launched to production in early 2026, and by April it had exceeded its goal and become the **#1-performing CG on Homefeed**. Serving migrated to Manas with real cost savings and dev-velocity gains, and the candidate budget expanded — largely inherited from ME as part of the consolidation (§3). The job now is impression share: its ceiling has been set by share, not model quality, and that's a solvable constraint. There's an early collaboration exploring whether a generative model could retrieve and rank in a single pass; genuinely early, and I'm not planning around it.

- **Staffing:** Bella (TL) with Hanlin.
- **Launch history (H1 2026):**
  - [HF RecGPT CG established](https://pinterest.slack.com/archives/C05UMECTDDJ/p1769480099905659) (Jan 27) — HF repins +0.86% (unique users), shares +2.89%; serving cost driven $970k → $571k → ~$300k/yr (by replacing 100 CLR pins). Cost was the launch blocker; it broke.
  - [BMI RecGPT unified retrieval/ranking CG](https://pinterest.slack.com/archives/C05UMECTDDJ/p1769641976895319) (Jan 28) — first unified L0-retrieval + L1-scoring ensemble in one service; BMI repins +3.63%, ~$295k/yr with savings expected from the GULP migration.
  - [Manas migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1776701719670599) (Apr — $59k/yr, parity, unblocked the SMS path) and [UserEventsView migration](https://pinterest.slack.com/archives/C05UMECTDDJ/p1780951119193459) (Jun — off the custom legacy sequence stack at $0, unblocking in-session sequences and the OmniSage upgrade).
  - [Diversity improvements](https://pinterest.slack.com/archives/C05UMECTDDJ/p1778094842675639) (May) — Future Window Token Prediction + Gaussian noise: +50% pin coverage, SSv2 +0.08%.
  - [ME sizer inheritance](https://pinterest.slack.com/archives/C05UMECTDDJ/p1782851752999499) (Jun 30) — 150 sizers: pin coverage +100%, impression share +89.3%, sitewide repins +0.42%, with the intent-expressions −0.13% regression named as the trade.
- **Risk:** low-to-moderate as an engine; the open question is ambition — how hard we push impression share.
- **Work type:** deep modeling, with ATG as the research partner on the frontier end.
- **Strategic weight:** our clearest claim to a Pinterest-leading LLM-era rec stack — and the winner of the two-paradigm consolidation, which raises the bar for what it owes.
- **Politics:** ATG collaboration boundary — partner, not dependency. And where GenRet lands at the settle is on the open list; same rule-7 discipline as CLR.
- **AI leverage:** the modeling is the leverage; the interesting second-order question is what the single-pass exploration implies if it works.
- **Leadership runway:** the engine needs a scaling champion, and the landing question means real influence for whoever builds the strongest case with evidence.

---

## 5. Prioritized cross-org initiatives and seams

Obligations with named leads — funded via named deliverables on existing engines, never ringfenced headcount, and nothing ships empty:

| Initiative | Lead(s) | EM |
|---|---|---|
| Content Exploration | Bella | James |
| Content Quality (Teen Safety, GenAI controls) | JJ | James |
| See More / See Less | Yali | James |
| NLFU Growth | ISR: JJ · Modeling: Devin | James |

- **NLFU (New Low Frequency Users) Growth** — supporting the Growth-led effort. Note the authorization for the associated metric trade-off expires end of September.
- **See More / See Less** — a co-ownership seat: Yali on retrieval, Raymond Hsu on the front end, no primary or secondary. High visibility.
- **Content Quality** — scope and counterpart are still thin. Flagged so it does not ship empty.
- **Content Exploration** — the newest of the four; Bella carries it alongside RecGPT. *[Scope: fill as it firms up.]*
- **The UPP ownership seam** — there is an active discussion above us about where the personalization substrate should live. I am handling it; you should know it exists.

---

## 6. What is decided, and what is open

**Decided — not reopening:**
- The interim team structure announced in August, and the current reporting lines.
- Team charter cores: curation quality is Daniel's center of gravity; retentive recommendations is Alim's; UPP and Reflex stay with me — and that's an end-state decision, not an interim one. I'm telling you now so nobody spends design cycles on options that aren't real. The why, briefly. UPP: it's a substrate with multiple consumers and an active ownership discussion above us — it has to be neutral ground, not report into one of its customers, and the work right now is mostly managing up and across, which is mine to do. Reflex: Dylan named me the point of contact, and a norm that applies to every team gets sponsored from the level that spans every team. Notice what I kept — the two most contested, least-harvestable things we own; you two inherit the engines and the clean charters. And neither is forever: when UPP is boring and the seam is settled, it's transferable. When Reflex is demonstrated and adopted, it gets a home.
- The clock: we design the end state together and decide around early November. No ad-hoc structural moves before then.

**Open — this is the agenda:**
- The organizing principle for how the three charters divide.
- Where CLR ends up.
- Where generative retrieval lands.
- Whether Intelligent Boards stays where it is, decided on where its gains actually originate.
- Consolidating the Unified Explore Backend so its charter and its reporting lines agree.
- Balaji's scope.
- The profile of the two open requisitions.
- The remaining reporting lines that sit with me today.

How we decide is ground rule 6, and how we talk about it outside the room is ground rule 7. Every project walkthrough ends with the same question — *where does this naturally live, and is that settled or open?* — and the running list we build together is the raw material for November.
