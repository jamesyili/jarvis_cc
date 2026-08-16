# Reflex Org Design — Deep Research Prompts

**Purpose:** Inform "how would Reflex as an engineering organization actually work" — staffing, charter, adoption, metrics, failure modes. Outputs feed the Dylan team-design artifact rewrite + Reflex strategy doc + sponsor conversations.

**Use:** Paste each prompt into a deep-research tool (Claude Research, Gemini Deep Research, ChatGPT Deep Research, Perplexity). Run independently. Synthesize after.

**Context to optionally prepend to any prompt:**
> I'm scoping a new internal "AI-leveraged engineering" team at a large consumer tech company (1000+ engineers). Initial size 4-6 engineers, potentially scaling to 10-20+. The team would build agentic systems, AI-augmented developer tooling, and AI substrates that compound the productivity of ML and product engineering teams company-wide. Currently the work runs on ~1 FTE pulled from spare cycles across an ML team; I'm proposing it become a real funded team.

---

## Prompt 1 — Precedent research (org archetypes)

```
Research how leading consumer tech and AI companies have structured "AI-leveraged engineering" teams — teams whose explicit charter is to build internal tooling, agents, and AI substrates that compound the productivity of *other* engineering teams (not external-facing AI products, not classic DevEx/CI/CD/build systems).

Companies to investigate: Anthropic, OpenAI, Google DeepMind, Meta AI Infrastructure, Stripe, Linear, Vercel, Shopify, Cursor, Sourcegraph, GitHub (Copilot internal), Microsoft, Netflix, Airbnb, Uber.

For each, find:
1. Team name and reporting structure (under CTO? VP Engineering? embedded in a product org? horizontal Core team?)
2. Headcount and composition (ML engineers / backend SWE / DevEx specialists / research scientists / product / EM-led vs TL-led)
3. Charter scope — what they explicitly own vs explicitly hand off (internal agents? IDE plugins? code-review bots? eval harnesses? data labeling? prompt engineering? AI-augmented CI/CD?)
4. What they ship and to whom (internal engineers, ML teams, product teams, all of the above)
5. How they measure success (adoption metrics, velocity metrics, business outcome attribution)
6. Reported wins and failures in publicly available sources

Sources to prioritize: engineering blog posts (2024-2026), conference talks (QCon, Strange Loop, AI Engineer Summit), podcast appearances (Pragmatic Engineer, Latent Space, Lenny's), public job postings, engineering Substacks, X/Twitter threads from named engineers.

Distinguish three categories explicitly:
- "AI-leveraged engineering" (compounds other engineering output via internal tools/agents)
- "AI products" (ships to external users)
- "Classic DevEx/platform" (CI/CD, build systems, monorepo tooling — pre-AI patterns)

Return: (a) a structured comparison table across companies, (b) 3-5 distinct organizational archetypes that emerge from the data, (c) for each archetype, the conditions under which it succeeded vs struggled.
```

---

## Prompt 2 — Failure modes and political fragility

```
Research failure modes of internal AI tooling and AI-leveraged engineering organizations at large tech companies (1000+ engineers, 2023-2026 timeframe). I want to understand why some of these efforts succeed and others become "innovation theater," "cool demos nobody adopts," or get quietly absorbed/disbanded.

Specifically investigate:
1. Documented cases of internal AI tooling teams that were created and later disbanded, absorbed, or pivoted significantly
2. Common adoption failures — mandate-from-above vs grassroots-pull patterns, and where each breaks down
3. Political and organizational forces that make AI tooling charters fragile (collision with DevEx/infra/platform incumbents, ambiguous P&L attribution, "who owns velocity")
4. Goodhart's-law patterns on adoption metrics (high usage, low real impact)
5. The "shiny new thing" problem — when leadership enthusiasm for AI tooling outruns operational discipline
6. How AI tooling teams fail to cross the "hobbyist adoption → critical mass" chasm
7. Cases where AI tooling collided with existing platform/infra teams and the resulting org pathology
8. The "CTO-visible but business-irrelevant" trap — high exec attention, low durable impact

Sources: published postmortems, engineering blog retrospectives, podcast interviews where engineers candidly discuss failed initiatives, Glassdoor/Blind threads, DORA 2025 report data on AI adoption pathologies (bugs/dev +54%, incidents/PR +242%, etc.), Pragmatic Engineer deep dives on failed internal tools, X/Twitter threads from named engineers who left these initiatives.

Return: (a) a taxonomy of failure modes with named-company examples where possible, (b) the 5-7 most common patterns ranked by frequency, (c) early-warning diagnostic signals a leader could use to detect that their AI-leveraged engineering org is drifting toward each failure mode, (d) the specific political moves that turned fragile charters into durable ones in cases that survived.
```

---

## Prompt 4 — Charter, boundary, and adoption mechanism

```
I'm scoping a new internal "AI-leveraged engineering" organization (4-6 engineers initially, potentially 10-20+ at maturity) at a large consumer tech company. The team would build agentic systems, AI-augmented tooling, and AI substrates that compound the productivity of ML and product engineering teams. There are existing DevEx, infrastructure, and platform organizations the team will need to coexist with.

Research:
1. Where this charter typically sits in existing engineering org topologies — under CTO office? VP Engineering staff? sub-team of an ML org? horizontal Core platform team? federated specialists embedded in product teams?
2. How teams of this kind define their boundary against existing DevEx/platform/infrastructure teams without political collision — what scopes they claim, what they explicitly disclaim
3. The "API contract" between an AI-leveraged engineering team and the teams it serves: mandate, pull-based adoption, paved-road default, library opt-in, plugin/extension, embedded engineers, internal consulting
4. Horizontal (company-wide substrate) vs vertical (one-domain like recsys-or-ranking-only) charter framings — when does each work better? What are the transition patterns from vertical → horizontal?
5. How companies decide whether to keep capabilities concentrated in one specialist team vs distribute the skill across all teams (the "platform vs federation" question for AI tooling)
6. Adoption mechanisms: pull vs push, the "paved road" pattern vs the "mandate" pattern vs grassroots evangelism, and case studies of each
7. How internal AI tools cross the "hobbyist adoption → critical mass" chasm; the role of a "killer use case" anchor vs broad utility
8. The role of executive mandate ("CTO email saying 'use this'") vs grassroots pull — when each works, when each backfires
9. Integration touchpoints that drive adoption (IDE plugins, CI/CD hooks, code review bots, build pipeline integration, slack agents)
10. Network effects — when does internal AI tool adoption compound vs stall

Sources: company engineering blogs (Stripe, Linear, Vercel, GitHub, Anthropic, Shopify, Airbnb, Netflix, Uber, Spotify, Lyft), conference talks (LeadDev, AI Engineer Summit), Pragmatic Engineer charter/topology deep dives, Will Larson and Charity Majors on platform vs federation, books "Team Topologies" (Skelton/Pais) and "Software Engineering at Google."

Return: (a) a decision framework for charter location and boundary, (b) 3-4 concrete charter templates with reporting structure + scope + boundary policy + adoption mechanism, (c) named-company examples mapped to each template, (d) diagnostic questions to ask about a proposed AI tooling team's adoption path BEFORE staffing it, (e) the specific moves that prevent collision with existing platform/DevEx/infra incumbents.
```

---

## Prompt 5 — Team composition and growth path (recsys-domain AI-leveraged eng)

```
Research the right team composition for a small (4-6 engineers initially) "AI-leveraged engineering" team at a large consumer recommendation systems company (think Pinterest/Netflix/Spotify/YouTube/TikTok scale). The team's mandate is NOT generic developer productivity (not "internal Cursor," not "internal Copilot"). The mandate is specifically to build agentic systems that automate and compound the recsys engineering loop:

  - Agentic A/B test ideation, hypothesis generation, experiment design
  - Agentic candidate generation / ranking / blending feature exploration
  - Agentic offline-online eval (running counterfactual evals, simulating user feed responses with VLM judges, surfacing regressions before launch)
  - Diagnostic / interpretability substrate for recsys (per-user/cohort visual+narrative content signatures, multi-stage funnel tracing, cross-surface DSAT investigation)
  - Closed-loop "Detect → Build → Simulate → Prove" pipeline where agents propose, prototype, test, and write back PRs for recsys experiments, with humans defining invariants and handling exceptions via RLHF

Consumers of the team's output are recsys engineers (ML engineers building candidate generation, retrieval, ranking, blending, anticipation/personalization substrates), recsys product managers, and recsys-adjacent VPs/Directors making investment calls.

This makes the team neither classic DevEx (no CI/CD focus), nor generic-LLM-application-building (no chatbot/RAG/agent-framework-for-its-own-sake focus), nor pure research (no paper-publishing mandate). It is a hybrid: agent engineering + recsys domain expertise + diagnostic/interpretability substrate building + AB/eval infrastructure.

The team will likely grow to 10-20+ engineers over 18-24 months if successful.

Specifically investigate:
1. The right mix at the 4-6 engineer scale for THIS hybrid charter:
   - How many recsys-native ML engineers (people who've shipped production candidate generation / ranking / retrieval / eval)?
   - How many "agent engineers" / LLM application builders (people who've built production agentic loops, evals, RLHF pipelines)?
   - How many backend / infra SWE for the substrate side (sensor primitives, caching, API surfaces, observability)?
   - How many VLM / multimodal specialists (visual content signatures, agentic feed judges)?
   - Where does a research scientist fit, if at all?

2. Hiring profiles for the hybrid role — what backgrounds in 2025-26 actually predict success here?
   - Recsys eng who taught themselves LLM application building
   - LLM application engineers who picked up recsys domain context
   - Ex-applied-research scientists with productionization track record
   - DevEx engineers who pivoted to AI tooling
   - What credentials / portfolio evidence / interview signal predicts success vs vanity?

3. The "unicorn risk" — when this team needs rare hybrid talent (recsys + agent engineering + interpretability) vs when roles can be split across narrower specialists who collaborate

4. Seniority distribution — all-staff/principal vs include mid/junior. Recsys agentic eng is a frontier — does it need all-senior, or do mid-level engineers actually move faster because they're less wedded to "old" recsys patterns?

5. The role of a tech lead vs embedded EM vs hybrid TL-EM at the 4-6 scale; when an EM becomes necessary; whether this team needs an EM with recsys credibility or whether agent-engineering credibility matters more

6. Evolution from 4-6 → 10-12 → 20+ engineers — what new roles get added at each scale?
   - Specialist sub-teams (eval/metrics, substrate/interpretability, agent pipelines, RLHF/invariants)?
   - A partnership / adoption sub-team that embeds with consumer recsys teams?
   - A research arm vs all-production?

7. Common composition mistakes for recsys-domain AI-leveraged eng teams specifically (over-indexing on generic LLM-app engineers who don't understand recsys, under-investing in eval rigor, missing the interpretability substrate role, ignoring the AB/experimentation infrastructure side, hiring too many research scientists who can't ship)

8. Precedents from recommendation-systems-heavy companies — how have Netflix, Spotify, YouTube, TikTok/ByteDance, Meta (Reels/Feed/Ads), Pinterest itself, LinkedIn, Amazon (recs), Booking, DoorDash structured analogous teams?
   - What public signals exist about their AI-for-recsys-engineering investments?
   - Where do these teams sit org-wise (under the recsys VP, under a horizontal AI/ML platform org, under CTO)?
   - What composition shapes appear in their job postings and engineering blogs?

9. Cross-reference with how non-recsys agent-engineering teams (Anthropic Claude Code, Cursor, Sourcegraph, Cognition/Devin, GitHub Copilot, Replit Agent) have staffed — what transfers vs what's domain-specific to recsys

10. The role of internal mobility — at a recsys-heavy company, recruiting senior recsys engineers internally onto an AI-leveraged eng team vs external hiring of LLM-application engineers. Tradeoffs at the seed stage.

Sources: public engineering blogs (especially Netflix Tech Blog, Spotify R&D, Meta Engineering, Pinterest Engineering, YouTube/Google Research, LinkedIn Engineering, DoorDash Engineering, Airbnb), RecSys conference talks 2023-2026, AI Engineer Summit talks, podcast interviews (Latent Space, Pragmatic Engineer, Lenny's, RecSys podcasts), job postings analyzed for composition signal (search for "ML platform," "recsys infra," "AI-leveraged eng," "agentic experimentation"), Anthropic/Cursor/Sourcegraph public communications, Will Larson on staff-eng composition.

Return:
  (a) 2-3 concrete team composition templates at 4-6 / 10-12 / 20+ scales, each optimized for the recsys-domain AI-leveraged eng charter (not generic DevEx or generic LLM apps)
  (b) A hiring rubric (skills, evidence, anti-signals) for each of the hybrid role types (recsys-native agent eng, agent-eng-with-recsys-context, interpretability-substrate eng, eval/RLHF eng, VLM/multimodal specialist)
  (c) The common composition failure modes for this specific hybrid (recsys + agent eng + substrate) and how to detect them early
  (d) When to convert TL-led to EM-led structure for this kind of team
  (e) Named-company precedents from recsys-heavy companies for each composition template
```

---