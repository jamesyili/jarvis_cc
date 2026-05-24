# Composing an AI-Leveraged Engineering Team for Recsys: Templates, Evolution, and Failure Modes

## TL;DR

- **At 4–6 engineers, the only composition that works is a 2-2-1-1 split: two recsys-native ML engineers (one staff-level with shipped candidate gen/ranking/eval), two agent engineers (one of whom is the unicorn hybrid who's done both), one substrate/backend SWE, and one player-coach TL — with a VLM specialist deferred and a research scientist explicitly NOT hired until scale forces it.** Hire the unicorn TL first; everything else is recoverable.
- **The dominant failure mode is hiring generic LLM-application engineers and calling them "agent engineers for recsys" — they ship chatbots and RAG demos, not Detect→Build→Simulate→Prove loops. The second is hiring research scientists too early — they paper-publish instead of writing back PRs.** Detect both early via a 30-day "ship one closed-loop experiment that lands in a real recsys PR" check.
- **Convert TL-led to EM-led at ~7 engineers (Larson's TLM-trap threshold), and pick an EM whose credibility is in agent engineering and ML platform shipping discipline, not recsys per se — the recsys-native staff engineer should anchor domain credibility.** Sub-team specialization (eval/RLHF, substrate/interpretability, agent pipelines, partnerships) only emerges at 12+, and a research arm only at 20+.

## Key Findings

1. **The closest public precedent for "agentic recsys engineering loops" is not a team — it's a one-person experiment.** Xu Ning, AI/ML Engineering Director at Snap, posted on LinkedIn: *"I gave Claude Code two GPUs and a week. Its team of agents ran ~500 experiments and built a state-of-the-art recommender model."* The setup was two NVIDIA L4 GPUs, MovieLens-25M, and Claude Code running autonomously over ~5 days. The framing was explicitly "team of agents," not a single linear loop. The implication: the human leverage point shifts from writing experiments to defining invariants, constraints, and what to give the agents — which is exactly your charter.

2. **The largest documented production-deployed agentic recsys system (Spotify's "You Say Search, I Say Recs," RecSys 2025) had 16 authors on the paper.** The role mix includes a VP of Personalization Research (Mounia Lalmas), a Senior Director of Engineering, Personalization (Ziad Sultan), a Director of Personalization Research (Paul N. Bennett), a senior PM (Christine Doig Cardet), Research Scientists (Enrico Palumbo, Ali Vardasbi), and a mix of Senior SWEs and Research Engineers. The system runs at ~450 ms p75 latency with +3% online success on new-release search and offline gains of +115% / +91% / +25% / +15% (LLM-as-judge) across four query slices. **This is the reference shape for a 15–20-person agentic recsys org, not a 4–6 seed team.**

3. **Pinterest's ML Platform — the closest organizational analog to a "substrate for recsys engineers" team — started in late 2017 as a two-engineer team trying to unify dozens of product engineers' stacks.** David Liu's "A Decade of AI Platform at Pinterest" retrospective is explicit: *"Scrappy ML Platform Team (2018–2019): A tiny two-eng team tried to unify much bigger teams' stacks and learned that incentives, not complaints, determine adoption."* The team only grew once specific product teams had organizational reasons to adopt. For an AI-leveraged engineering team, this means: at seed scale, you must be paired with one or two consumer recsys teams that have a goal tied to your output.

4. **Netflix's Recommendation Systems Research and Engineering org (Justin Basilico, Director, Recommendation Systems Research and Engineering) shows a distinctive three-track title structure: Research Scientist (modeling/algorithms — e.g., Harald Steck, Ehtsham Elahi, James McInerney, Moumita Bhattacharya), Senior Research Engineer (algorithms-in-production — e.g., Ehsan Saberian, Sudarshan Lamkhede, Linas Baltrunas), and Software Engineer (platform/serving). The Research Engineer is the load-bearing role.** This title distinction matters: it's the recsys-native engineer who can both read a paper and ship a counterfactual eval pipeline. For your team, the equivalent is the "recsys-native ML engineer who can write back PRs" — not a Research Scientist.

5. **LinkedIn already has a named team for the diagnostic/interpretability substrate piece: REx ("prescriptions for relevance models").** The LinkedIn Engineering ML Infrastructure page states verbatim: *"REx (a.k.a 'prescriptions for relevance models') builds tools to troubleshoot online AI models — providing AI and AI Infra teams with observability and interpretability of AI models in production."* This is the cleanest precedent for the interpretability-substrate-for-recsys role. Sized as one team within ML Infra; specific headcount undisclosed.

6. **Spotify's Homepage Personalization, led by Maria Dimakopoulou (Director of ML), is — per the Netflix PRS 2024 workshop bio — "a team of 60 people responsible for generating, ranking and distributing personalized content recommendations across music, podcasts and audiobooks on the Homepage of 600+ million listeners."** This is the order-of-magnitude scale of a *mature* recsys-vertical team at a major consumer recsys company — useful as a reference for what you're augmenting, not what you're building.

7. **The agentic-AI labor market in 2026 is the binding constraint.** Per the Stanford HAI 2026 AI Index (using Lightcast labor-market data): *"Skills related to Agentic AI grew from just 0.06% of postings in 2024 to 0.23% in 2025. That's a more than 280% increase in a single year, representing nearly 90,000 job postings in the US alone."* Forward-deployed engineer listings *"surged over 800% in 2025 alone."* Per KORE1's 2026 hiring-cycle data, production-agent-engineer roles close in 5–9 weeks at $185K–$320K base when stack-named, with cold-outreach response rates of 9–14% (vs. ~30% for general AI engineering). Hiring three agent engineers simultaneously is an 18-week search, not a 6-week one — which means **the 4–6-engineer team is also the 6-month team**.

8. **Generic agent-engineering team analogs (Cursor, Claude Code, Sourcegraph Cody) staffed differently than your charter requires.** Per Gergely Orosz's Pragmatic Engineer reporting: Boris Cherny joined Anthropic in September 2024; founding PM Cat Wu was part of the original core (her research on computer-use agents prompted Boris to extend the tool); *"Boris and the Claude Code team released a dogfooding-ready version in November 2024 — two months after the first prototype. On the first day, around 20% of the Engineering team used it, and by day five, 50% of Engineering was using Claude Code."* The team grew to ~10 engineers by July 2025. Cursor as a $60B+ company has ~50–300 engineers total. The transferable lesson is "stay small longer than you think," not the specific mix — because their charter is dev tooling, not domain-specific recsys leverage.

## Details

### (a) Three composition templates

#### Template A — Seed (4–6 engineers, months 0–9)

**Slot 1: Tech Lead / Founding Engineer (1).** Staff/Principal level. Hybrid profile: 5+ years in recsys (candidate generation or ranking, ideally both) AND has shipped at least one production agent loop with non-trivial evals. This is your unicorn. You will not find them quickly — budget 10–14 weeks. Reports to a recsys VP or ML Platform VP. Acts as TL/M (player-coach) per Larson's framework — code-contributes 50%+, owns architecture, runs hiring.

**Slot 2: Recsys-native ML engineer (1).** Senior (L5/L6 equivalent). Has shipped a production candidate generator, ranker, or eval pipeline at scale (>10M DAU). Knows IPS/doubly-robust off-policy eval, interleaving (the Airbnb 50x-sensitivity pattern), log feature parity. Brings domain credibility to consumer teams. **Internal hire if at all possible** — recruits from existing recsys orgs at the parent company carry institutional trust your team cannot otherwise buy.

**Slot 3: Agent engineer (1).** Mid-senior. Has built and shipped a production agent loop with proper evals (LLM-as-judge with calibrated rubrics, trajectory replay, tool-use observability). Knows the failure modes the Anthropic team documented (CoT-manipulation susceptibility, distribution collapse in VLM judges, the "auto-accept mode only works on peripheral code" lesson). Does NOT need recsys background — pairs with Slot 2.

**Slot 4: Substrate / backend SWE (1).** Senior. Owns the sensor primitives, caching layer, API surfaces, tracing/observability for multi-stage funnel decomposition. This is the role most teams skip and then regret at month 6, when the agent outputs can't be reproduced, cached, or traced through ranking stages. Should have built telemetry/observability platforms before, not just consumed them.

**Slot 5: Eval / interpretability engineer (1; mid-level OK).** Owns the eval substrate: golden sets, calibrated VLM-judge rubrics, per-user/cohort visual+narrative content signatures, counterfactual replay (per the IPS/doubly-robust lineage Eugene Yan documents and Netflix has published on). This is the role that ages best — eval rigor compounds. Mid-level often outperforms senior here because they're less wedded to "old" recsys eval patterns (offline AUC, NDCG) and more open to LLM-as-judge with calibration.

**Slot 6 (optional, hire month 4–6): second agent engineer OR second substrate SWE.** Decide based on whether your first two months' bottleneck is "agents don't propose useful experiments" (hire agent eng) or "we can't trace what they did" (hire substrate). Default: second substrate SWE — eval/observability debt is harder to recover from than agent-design debt.

**What you do NOT hire at this scale:**
- **VLM/multimodal specialist** — partner with the parent company's content-understanding team. Hiring a dedicated VLM engineer at 4–6 over-rotates on a single technique.
- **Research scientist** — every research scientist hire at this scale is a 6-month delay to your first written-back PR. The recsys-native staff TL reads papers; you do not need a separate person whose mandate is novel methods.
- **Dedicated EM** — see TL/EM section below.
- **Designer or PM** — your consumers ARE PMs and engineers. They write the specs.

**Reference precedent:** Pinterest's 2017 "two-engineer ML Platform team" successfully bootstrapped what is now the substrate behind hundreds of millions of inferences per second. The bootstrap was not staffed for the eventual scale — it was staffed for proving incentives align.

#### Template B — Adolescence (10–12 engineers, months 9–18)

By 10–12 you split into **three named pods** under a dedicated EM:

**Pod 1: Agent Pipelines (3–4).** The Detect→Build→Simulate→Prove loop owners. 1 staff agent engineer (TL of the pod), 1–2 mid-level agent engineers, 1 recsys-native ML engineer embedded for domain grounding. Owns hypothesis generation, experiment design, candidate/ranking/blending feature exploration agents, and the PR-write-back machinery.

**Pod 2: Eval & Interpretability Substrate (3–4).** 1 staff eval engineer (probably your original Slot 5, promoted), 1 substrate SWE, 1 mid-level eval engineer, and at this stage you ADD 1 VLM/multimodal specialist who owns visual+narrative content signatures and feed-judge agents. This is the pod that LinkedIn calls REx; it is the pod whose absence makes the team look like an "internal Cursor."

**Pod 3: Adoption / Partnership (2–3).** Forward-deployed engineers (per Anthropic's "applied AI" team model). They embed with consumer recsys teams for 6–12 weeks, instrument the agent loop into the consumer's experimentation workflow, then rotate. Without this pod, your output gets adopted by exactly two consumer teams and stalls. **One of these FDEs should rotate from the Agent Pipelines pod every 6 months** — preserves continuity of judgment.

**Leadership shape:** 1 EM (whose credibility is agent eng + ML platform shipping, not necessarily recsys — the recsys-native staff anchors domain credibility); 1 staff TL per pod; a Director or staff TL serving as overall TL/architect (often the original TL, now de-coding).

**Reference precedent for this shape:** Spotify's published agentic search/recs effort at RecSys 2025 had 16 authors — a Senior Director of Engineering, a VP of Research, a Director of Research, multiple Senior SWEs, multiple Research Scientists, a senior PM, and Research Engineers — sized at the production-ready stage. Your 10–12 team is the pre-production version of this.

#### Template C — Scale (20+ engineers, months 18–24)

Add a **fourth pod and a small research arm**:

**Pod 4: RLHF / Invariants (3–4).** Owns the human-in-the-loop systems: how humans define invariants, exceptions, and reward signals that the agents respect. Includes data engineers who curate trajectory datasets, RLHF infra engineers, and rubric designers (likely senior AI Trainer / Eval scientist hybrids — per the 2026 market, $145K–$260K, thin supply per the AI Career Lab market analysis). This pod's existence prevents the "auto-accept mode" failure that even the Claude Code team flags ("works best for tasks on the product's edges, not core business logic" — recsys ranking IS core business logic).

**Research arm (2–3, NOT a separate org).** One research scientist + 1–2 research engineers, reporting to the same EM/Director, embedded in pods on rotation. Their mandate is publishable methods that flow back into the substrate within 6 months — NOT a paper-publishing-only mandate. Netflix's title distinction (Senior Research Engineer vs. Research Scientist, both reporting under the same Director) is the model.

**Specialist roles added:**
- **AI Safety / Trust engineer (1)** — owns guardrails on the agent's write-back-PR authority (the Cursor "Bugbot → Automations" lineage; Cursor's Jonas Nelle frames it as "humans aren't always initiating; they're called in at the right points in this conveyor belt").
- **Forward-deployed adoption pod grows to 4–5**, with one named partnership manager per major consumer-recsys vertical (e.g., one each for candidate gen, ranking, blending).
- **Substrate/observability sub-team grows to 5–6** as the trace volume becomes its own scaling problem. LinkedIn's T-REX experimentation platform operates at this scale: per LinkedIn Engineering's official T-REX team page, *"Every day, more than forty thousand experiments are run on nearly eight thousand metrics computed to accelerate innovations in every aspect of LinkedIn."* That scale requires dedicated platform engineers.

**EM-of-EMs structure:** A Director plus two EMs (Agent+Eval; Substrate+Partnerships). Total org ~22–25.

---

### (b) Hiring rubric (tight)

| Role | Strong signals | Anti-signals |
|---|---|---|
| **Recsys-native agent eng (unicorn TL)** | Shipped both a ranker/candgen at >10M DAU AND a production agent loop with evals. Can name specific IPS variance reduction tricks AND specific LLM-judge calibration techniques. References from both recsys director AND agent-eng peer. | "Built an agent framework"; only ML papers and zero shipping; resume reads as either pure recsys OR pure agent eng, never both. |
| **Agent-eng with recsys context** | Production agent loops with budget caps, retry strategies, trajectory replay. Strong opinions on when NOT to use an agent. Knows the difference between LLM-as-judge precision and recall. Backend/distributed-systems-shaped resume. | LangChain-only stack; demo-grade RAG; no eval harness in their last project; resume optimized around prompt engineering. |
| **Interpretability-substrate eng** | Built telemetry/observability platforms; has shipped a feature store, a causal tracing system, or an experimentation platform component. Can articulate the cost of training-serving skew. | Frontend-shaped career; treats "observability" as Grafana dashboards; never owned a stateful migration. |
| **Eval / RLHF eng** | Has constructed golden sets that survived a model upgrade. Knows calibration-error metrics, consensus-entropy aggregation (per recent VLM-judge literature). Can write a rubric. Domain expertise (former rater team manager, or content quality background) is a multiplier. | "Did some labeling at Scale AI"; sees evals as a one-time setup task; can't explain LLM-judge biases (style preference, distribution collapse). |
| **VLM / multimodal specialist (hire at 10+)** | Shipped CLIP-style retrieval or multimodal embeddings in production at scale; understands keyframe extraction tradeoffs (per Pinterest visual embedding work and the PRISM-style YouTube Shorts audit literature); knows VLM-judge failure modes (overconfidence, low rating variance). | Diffusion-model-only background; published in CV venues without production deployments; treats multimodal as "just add images." |

---

### (c) Common composition failure modes for THIS hybrid (and early detection)

1. **The "Internal Cursor" trap.** Team gets staffed with developer-productivity-minded engineers who build a great IDE plugin for recsys engineers, instead of agentic experiments. **Detection:** By week 8, ask "what's the first PR an agent wrote back?" If the answer is "we're still building the agent harness," you've drifted. **Prevention:** Make the first milestone a single shipped agent-proposed-and-PR'd ranking experiment, even if trivial.

2. **The "LLM application demo" trap.** Generic LLM-app engineers build chatbots/RAG demos with no recsys evaluation rigor. **Detection:** Resumes skew to LangChain/LlamaIndex with no IPS/counterfactual-eval literacy. The team produces impressive-looking demos that consumer recsys teams won't adopt. **Prevention:** Slot 2 (recsys-native ML eng) must be hired *before* Slot 3 (agent eng), not after.

3. **The "research lab" trap.** Hiring one or two research scientists too early. **Detection:** Output is conference submissions, not consumer-team adoption. After 6 months, the count of accepted PRs to consumer-team repos is < 5. **Prevention:** No research scientist at 4–6 scale. Add at 18–20 max, embedded in pods.

4. **The interpretability-substrate gap.** Team builds agents but consumer recsys engineers can't reproduce or trust outputs. **Detection:** A consumer recsys engineer asks "why did the agent propose this?" and the team can't answer in <30 minutes. **Prevention:** Slot 4 (substrate SWE) hired in the first 4 engineers, not the second 4. LinkedIn REx exists because LinkedIn learned this the hard way.

5. **The VLM premature optimization.** Hiring a multimodal specialist at 4–6 because VLM-judges-of-feed are cool. **Detection:** Team spends month 3–5 evaluating CLIP variants instead of writing the closed-loop harness. **Prevention:** Defer multimodal to 10+ scale; partner with existing content-understanding team for VLM-judge primitives.

6. **The all-staff trap.** Composition is 5 staff engineers, no mid-level. **Detection:** Architectural debates that don't resolve; everyone holds opinions about the right way to do X. **Prevention:** At least 1 mid-level out of 4–6. Mid-levels move faster because they're less wedded to "the way we did recsys evaluation in 2021." For frontier work, mid-level engineers with 3–5 years post-college and 1–2 years of agent/LLM exposure consistently outperform staff engineers with deep but stale recsys backgrounds.

7. **The "we'll hire externally for agent eng credibility" trap.** Skipping internal recsys engineers because "they don't know LLMs." **Detection:** The first hires are all from Anthropic/OpenAI/Cursor backgrounds. The team produces beautiful agent architectures that don't fit the parent company's ranking stack. **Prevention:** At least 50% of the first 4 hires are internal recsys-native moves, with external agent-eng experience layered on top.

8. **Missing the AB/experimentation infrastructure relationship.** Team builds agents that propose experiments but can't actually run them through the parent company's experimentation platform. The reference scale is non-trivial: per LinkedIn Engineering's official T-REX team page, *"Every day, more than forty thousand experiments are run on nearly eight thousand metrics computed to accelerate innovations in every aspect of LinkedIn."* Plugging into a platform of that complexity is not a side quest. **Detection:** Month 4 surprise that the agent's "PR" can't actually be ramped without manual T-REX-equivalent setup. **Prevention:** Slot 4's first deliverable is a write API into the parent experimentation platform.

---

### (d) When to convert TL-led to EM-led

Larson's framework, drawn from *An Elegant Puzzle: Systems of Engineering Management* (2019) and reinforced in his Dec 18, 2020 essay "Tech Lead Management roles are a trap": managers supporting fewer than 4 engineers function as TLMs (limited career growth, but works); managers supporting more than 8–9 become coaches/safety-nets (too busy to invest). The sweet spot is 4–6 direct reports per EM.

**Concrete rule for this team:**
- **0–6 engineers:** TL/M (player-coach). The unicorn TL/founding engineer carries both hats. **Do not hire an EM yet** — the talent is in the doing.
- **7 engineers:** the trap zone. The TL/M is overloaded; technical decisions slip; 1:1s are skipped. This is the inflection point Larson's framework warns about.
- **8 engineers:** Convert. Hire a dedicated EM.

**What kind of EM?** Counter to instinct: pick the EM whose credibility is **agent engineering + ML platform shipping discipline**, NOT recsys per se. Two reasons:
1. Your recsys-native staff TL (Slot 1 / Slot 2) already anchors recsys credibility with consumer teams.
2. The structural risk of this team is research/demo drift, not domain irrelevance. The EM's job is to enforce shipping rhythm, eval rigor, and the PR-write-back invariant — all of which require ML platform muscle, not necessarily ranking-model expertise.

**Specifically avoid:** an EM whose strongest credential is "ran a ranking team at $BigCo" but has never shipped an LLM-eval pipeline. They will optimize for the wrong things and let the agent-eng pods drift into research mode.

At 12+, the TL/EM split becomes one EM per pod, with one Director.

---

### (e) Named-company precedents mapped to templates

| Template | Closest precedent | What transfers | What does not |
|---|---|---|---|
| **A (4–6)** | **Pinterest ML Platform, 2017–2019** — David Liu: "Scrappy ML Platform Team (2018–2019): A tiny two-eng team tried to unify much bigger teams' stacks" | Bootstrap with one or two consumer-team partners; incentives-first thinking; layer-by-layer adoption | Pinterest's was infra-only; yours is infra + agents + domain |
| **A (4–6)** | **Claude Code team, Sep 2024 – Jul 2025** — Boris Cherny joined Anthropic in September 2024 with founding PM Cat Wu; dogfood version in Nov 2024 (50% of Anthropic Engineering using it by day five); ~10 engineers by July 2025 | Stay tiny longer than you think; dogfood internally first; the founder-eng's judgment is the bottleneck | Anthropic was building a horizontal coding tool; you're building vertical recsys leverage |
| **A (4–6)** | **Xu Ning's Snap one-person + agent-fleet experiment** — Director, AI/ML Engineering at Snap, posted: *"I gave Claude Code two GPUs and a week. Its team of agents ran ~500 experiments and built a state-of-the-art recommender model."* | The "constraints before code, review tests not code" mental model; agent-team-as-leverage thinking | One-person experiments are not teams; you need the substrate and eval rigor that the experiment skipped |
| **B (10–12)** | **LinkedIn ML Infrastructure + REx + T-REX, current state** | Named substrate team (REx) for observability/interpretability; experimentation engine team operating at "more than forty thousand experiments...on nearly eight thousand metrics" per day; clean separation between feature platform, productionalization, and modeling automation pods | LinkedIn's is org-wide; yours is one team |
| **B (10–12)** | **Netflix Recommendation Systems Research & Engineering (Justin Basilico, Director, Recommendation Systems Research and Engineering)** | Three-track titles (RS / Senior RE / SWE) — the Research Engineer is the load-bearing role; AIMS foundation model team for shared eval substrate | Netflix's research scientist density is higher than yours should be |
| **B (10–12)** | **DoorDash dispatch DS team** — *"a dispatch data science team that is diversified across disciplines (OR, ML, causal inference, statistics) and industry experience (ridesharing, gig economy, Google)"* | Multi-disciplinary mix per pod is correct; explicit dual-track (simulation + experimentation) | DoorDash is logistics, not feed recsys |
| **C (20+)** | **Spotify Personalization Research + Engineering** — 16-author production agentic search/recs paper (Lalmas, Sultan, Bennett, Palumbo, Tamborrino, Bouchard, Doig Cardet et al.); Maria Dimakopoulou (Director of ML, Homepage Personalization) leads "a team of 60 people responsible for generating, ranking and distributing personalized content recommendations across music, podcasts and audiobooks on the Homepage of 600+ million listeners" | The role-mix shape of the 16-author paper is the explicit template; ~450ms p75 production-latency target; LLM-as-judge offline evaluation deltas (+115%/+91%/+25%/+15%) as the eval bar | Spotify is mature; you're scaling toward this, not starting here |
| **C (20+)** | **Pinterest ML Platform + Ads ML Infra + Core ML Infra + ATG, coordinated via "ML Foundations"** | Three parallel infra orgs that need explicit coordination forum; "AI Products" multidisciplinary embed model (product eng + design + content + DS + PM) for shipping novel surfaces | Pinterest's split is horizontal infra; yours is vertical agent leverage |
| **C (20+)** | **Aampe** — 46 employees in 2025, "agentic infrastructure for adaptive customer experience" using RL-based per-user agents running ~150,000 simultaneous experiments per customer team | Headcount-to-experiment-volume ratio as a leverage benchmark; data-scientist-and-engineer pairing as the core unit | Aampe is RL-not-LLM-shaped and externally facing; yours is internal-tooling |

---

### (f) The 3–5 highest-leverage, lowest-supply 2026 hiring profiles

1. **Recsys-native production engineer with shipped agent loops (the unicorn TL).** Per KORE1's 2026 hiring data, comparable senior agentic platform roles close in 7+ weeks at $245K base when stack-named. The recsys-overlap subset is materially thinner. Realistic supply: a few hundred people globally; realistic addressable: ~50–100. **This is your hardest hire and your highest-leverage one.**

2. **Eval / rubric-design engineer with LLM-judge calibration depth.** Per the AI Career Lab 2026 market analysis, the going rate is $145K–$260K but supply is *"thin because most UX researchers haven't pivoted yet."* Domain expertise multiplier — former content-policy or rater-program leads are gold. This role tends to be undervalued at hiring time and disproportionately valuable at month 12.

3. **Substrate/observability engineer who's built experimentation-platform internals.** The LinkedIn T-REX team, the Airbnb ERF team (which the Airbnb engineering blog credits Maxime Beauchemin, Adrian Kuhn, Jeff Feng, Gurer Kiratli for), the DoorDash ML Workbench team — alumni of these specific systems are the right pool. Hiring competition with the AI infra labs (Anthropic, OpenAI) is intense because the same skill set sells there.

4. **Forward-deployed engineer with recsys org credibility.** Following the Anthropic applied-AI team model — per JobsByCulture's analysis of Anthropic hiring announcements: *"Anthropic is scaling its applied AI team 5x in 2026 to meet surging enterprise demand. The company is adding forward-deployed engineers and technical architects — the 'human layer' that makes enterprise AI deals close."* Your variant — embedded with recsys teams specifically — has near-zero direct talent pool. Build it from internal rotations.

5. **VLM/multimodal engineer with VLM-as-judge experience (not just CLIP).** Wait until 10+ scale, but when you do hire, the bar is "has written calibrated VLM-judge rubrics in production and handled distribution collapse / overconfidence" — not "knows multimodal models." That subset is small; expect a 12–16-week search.

## Recommendations

**Months 0–3 — Hire the TL/M and protect the charter.**
- Single hiring priority: the unicorn TL (recsys + agent eng + interpretability). Do not hire the second person until this person is in place; you will hire wrong without their judgment.
- Co-located with one named consumer-recsys partner team that has a goal tied to your output. No partner = no incentive alignment = no adoption.
- Charter document explicitly says "NOT internal Cursor / NOT chatbot / NOT research arm." Re-read monthly.

**Months 3–9 — Build to 4–6 in the 2-2-1-1 shape.**
- Hire order: Slot 2 (recsys-native ML), Slot 4 (substrate SWE), Slot 3 (agent eng), Slot 5 (eval). Slot 6 floats.
- First milestone (month 5): one closed-loop "Detect → Build → Simulate → Prove" agent that has written one PR adopted by your consumer-team partner.
- **Threshold to revisit composition:** if month 5 milestone slips, swap a slot — usually the missing piece is substrate (Slot 4 came too late) or recsys-domain grounding (Slot 2 too late).

**Months 9–18 — Split into pods only when forced.**
- Convert TL/M → dedicated EM at engineer 8, not before.
- Add forward-deployed pod the moment a second consumer team requests integration (typically month 10–14).
- Add VLM specialist when feed-judge becomes the bottleneck (not before — premature multimodal is the most common over-rotation).
- **Threshold to slow hiring:** if PR-write-back-to-consumer-PR ratio drops below 1:3 (i.e., agents are proposing 3x more than gets shipped), stop hiring and fix the eval/substrate layer.

**Months 18–24 — Add the research arm and RLHF/invariants pod only after the substrate is mature.**
- One research scientist max, embedded, with a 6-month flow-back-to-substrate mandate.
- RLHF/invariants pod is the last pod to hire; it requires the trajectory data your earlier pods generate.
- **Threshold to convert to multi-EM/Director structure:** at 18 engineers, with two pods each ≥6 people.

## Caveats

- **The empirical base is thin.** No public company has documented a team with exactly this charter at this scale. The Spotify and Pinterest precedents are adjacent (production agentic search; ML platform substrate) but not isomorphic. Treat the templates as informed inference, not validated patterns.
- **The Xu Ning "500 experiments in 5 days" datapoint was sourced from a LinkedIn post snippet; the full body — including specific NDCG/Recall@K numbers — could not be retrieved through public web tooling.** The qualitative framing (one human + agent fleet, two NVIDIA L4 GPUs, MovieLens-25M, ~5 days, "state-of-the-art recommender model") is well-supported across multiple indexed snippets; the precise quantitative claims should be verified directly from Xu Ning's LinkedIn feed before citing externally.
- **The 2026 agentic AI hiring market is moving faster than this report's compensation/timeline figures.** The 280% YoY and 800% forward-deployed growth come from the Stanford HAI 2026 AI Index (Lightcast data); the per-role salary bands are from KORE1, JobsByCulture, and the AI Career Lab as of Q1–Q2 2026 and may already be outdated; treat them as direction-of-travel, not point estimates.
- **Internal-mobility-vs-external-hire tradeoff is company-specific.** The recommendation to favor internal recsys engineers for 50%+ of seed hires assumes the parent company has a recsys org of >50 ML engineers and a healthy mobility culture. If either is absent, weight external agent-eng hiring higher and budget an extra 3–6 months for domain ramp.
- **The "research scientist not until 18+" recommendation is contested.** A counterargument: a single research scientist embedded from day 1 can accelerate novel-eval-methods adoption (counterfactual eval, off-policy estimators, LLM-judge calibration). The case against is the higher likelihood of paper-publishing-as-default behavior at small scale. Reasonable leaders disagree; the safe default is "wait."
- **VLM-judge reliability is itself an open research question.** Recent work ("Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation," 2026) shows VLM judges can be manipulated via CoT rewriting, inflating false-positive rates by up to 90%. This is a real risk for any team relying on VLM-judges-of-feed as a primary eval substrate. Build redundancy (human spot-check, A/B-test-as-ground-truth backstop) into the eval layer from day 1.