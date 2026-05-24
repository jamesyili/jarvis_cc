```markdown
# Failure Modes of Internal AI Tooling Teams at Large Tech Companies (2023–2026)

**Bottom line up front:** The most common failure mode for internal AI tooling at 1000+-engineer companies in 2023–2026 is not technical — it is the collision between top-down executive enthusiasm (and the vanity metrics it spawns) and the absence of the underlying engineering hygiene (eval pipelines, review capacity, platform quality, user-centricity) that the DORA "State of AI-Assisted Software Development 2025" report identifies as the actual determinant of whether AI helps or hurts. Tools rarely fail because the model is bad; they fail because charters drift, adoption gets gamed, and incumbents (DevEx, Platform, ML Platform) absorb the team once its political sponsor moves on. For an EM at Pinterest building an investigation/orchestration agent (Pinvestigator) and an analytics tool (Pinsight), the durable strategic move is to (a) tie your tool to a named, paying internal customer with a quantified outcome, (b) co-own metrics with the Platform/DevEx incumbents rather than competing, and (c) refuse vanity adoption KPIs even when leadership wants them.

## TL;DR

- **The DORA 2025 evidence is unambiguous and uncomfortable:** AI is a force multiplier of existing org dysfunction, not a fixer of it — 90% of devs now use AI, throughput is finally up (vs. 2024 when AI adoption correlated with a −1.5% throughput / −7.2% stability hit), but stability is still negatively correlated with AI adoption, and Faros AI's *AI Engineering Report 2026: The AI Acceleration Whiplash* (22,000 developers across 4,000+ teams) found bugs per developer up 54%, incidents per PR more than tripled, and median PR review time up 441%. The bottleneck has moved from writing code to reviewing it.
- **The dominant failure mode in 2025–2026 is "tokenmaxxing" / mandate-driven adoption theater** — Meta's "Claudeonomics" leaderboard (60.2 trillion tokens in 30 days across 85,000 employees, ~$100M+ effective cost), Salesforce's ~$170/month minimum AI spend ($100 Claude Code + $70 Cursor), Microsoft's internal token leaderboard (since Jan 2026), Amazon's >80% weekly-AI-use target with engineers caught inflating usage via in-house "MeshClaw" agent (FT), and Shopify's "prove AI can't do it before you hire" mandate have all produced documented gaming behavior, with engineers running autonomous agents purely to inflate metrics. This is the textbook Goodhart pattern; it is already eroding tool credibility.
- **For an EM with two shipped internal tools, the survival playbook is narrow:** anchor to a named business-outcome KPI (not usage), build the eval/review infrastructure *before* asking for adoption, formally partner with (don't compete against) ML Platform / DevEx incumbents, and treat the charter as a permanent renegotiation rather than a fixed mandate. Tools that survived (Google's internal completion, Meta's Metamate/CodeCompose, Stripe's Minions, Pinterest's MCP ecosystem) all had explicit measurement infrastructure, a named platform-team owner, and a real customer with a real bug. Tools that died or got absorbed (CodeWhisperer → Q, Meta Responsible AI 2023, Take-Two AI tooling 2026, Microsoft consumer Copilot pre-March 2026 reorg) lacked at least one of those.

---

## Key Findings

### A. A taxonomy of failure modes (with named examples)

| # | Failure mode | Mechanism | Named examples |
|---|---|---|---|
| **1** | **Mandate-driven adoption theater / tokenmaxxing** | Exec sets a usage/spend floor; engineers game it; vanity metrics drown signal | Meta "Claudeonomics" leaderboard (reported by The Information, April 2026; ~60.2T tokens / 30 days; titles "Token Legend" / "Session Immortal"); Salesforce ~$170/mo minimum spend ($100 Claude Code + $70 Cursor, per Pragmatic Engineer reporting); Microsoft internal token leaderboard since Jan 2026; Amazon's >80% weekly-AI-use target with engineers using "MeshClaw" agent purely to pump tokens (FT); Shopify "prove AI can't do it" mandate (Lütke memo, April 2025) |
| **2** | **Shiny-new-thing without operational discipline** | Leadership pushes deployment ahead of eval pipelines, feedback loops, on-call discipline | Amazon's two recent AWS outages traced to AI agents (Kiro AI ordered "delete and recreate environment," 13-hour outage Dec 2025; Q Developer–involved outage); SVP Dave Treadwell internal email (cited by FT/BrainGrid) names "a trend of incidents and unsafe practices with a high blast radius" and "novel GenAI usage, for which best practices and safeguards are not yet fully established" |
| **3** | **Vanity metric optimization (Goodhart)** | Team optimizes for completions/sessions/acceptance rate rather than shipped value | CodeCompose's reported 22% acceptance / 8% of code authored — high, but Meta still pivoted to a multi-model GPT-4+Llama strategy via "Metamate"; GitHub Copilot's negative Net Promoter Score on accuracy (-3.5 → -24.1 → -19.8 per Recon Analytics); 44.2% of lapsed Copilot users cite distrust |
| **4** | **Hobbyist adoption ceiling / "20% wall"** | Early adopters love it; median engineer never converts; usage stalls at 15–25% | The widely-cited 20% Copilot enterprise plateau pattern; per the Morgan Stanley/RSM AI Adopter Survey (July 2025), 79% of enterprises deploy Copilot but only 3.3% of eligible M365 users adopt the paid add-on across Microsoft's 450M commercial subs — i.e., most "deployments" are *procurement exercises, not productivity gains*; Stack Overflow's 2025 Developer Survey (49,009 respondents, 177 countries): 84% use AI, only 33% trust it (and trust fell from 40% to 29% YoY per Stack Overflow's Dec 2025 blog), 46% actively distrust it, positive sentiment down from ~70% (2023) to 60% (2025) |
| **5** | **Charter collision with Platform / DevEx / ML Platform** | New AI tooling team duplicates existing platform team's surface; turf war; eventual absorption | Amazon CodeWhisperer absorbed into Amazon Q Developer (Apr 30, 2024; AWS GM Doug Seven told TechCrunch the name was "a bit of a branding fail"); Microsoft DevDiv reorganized under CoreAI (Jan 2025), Julia Liuson departed (Apr 2026) as VS Code/Visual Studio mandate shifted from IDE to agentic; Microsoft consumer + commercial Copilot merged under Jacob Andreou (Mar 2026) explicitly because Copilot hadn't gained adoption (6M DAU vs 440M ChatGPT, per Sensor Tower) |
| **6** | **Disbandment after exec sponsor departs or strategy pivots** | Team has no durable customer; loses air cover; gets dissolved | Meta Responsible AI team (Nov 2023, absorbed into product orgs per The Verge); Take-Two AI tooling team (2026, dissolved despite 7 years of pipeline work because CEO Strauss Zelnick rejects the strategic bet); Meta Reality Labs "Foundations" group dissolved into product teams (Apr 2026, Saba memo via PYMNTS/The Information) |
| **7** | **CTO-visible / business-irrelevant trap** | Tool gets earnings-call mentions but no durable production impact | Google's claim that "more than 50% of code checked in weekly is AI-generated" — sounds transformative, but DORA's own 2025 data shows stability still suffers and platform quality is the moderator; Microsoft Q2 FY2026 reported 15M Copilot paid seats — 3.3% of the 450M commercial M365 base, which The Register called "an awkward figure that landed alongside Microsoft's AI splurge" |
| **8** | **Top-down replacement that has to be unwound** | Leadership over-claims AI capability, lays off humans, then rehires | Klarna's ~700 customer-service layoffs (2023–2024) reversed by 2025; CEO Siemiatkowski: "We focused too much on efficiency and cost. The result was lower quality." Per the Orgvue / Vitreous World survey of 1,163 C-suite and senior business leaders (fielded Feb–Mar 2025): 39% had made employees redundant due to AI deployment, and **of those, 55% admit they made wrong decisions about those redundancies**. Forrester *Predictions 2026: Future of Work* separately found "55 percent of employers regret laying off workers because of AI" (Computerworld, Oct 29, 2025) |
| **9** | **Forced reorg / "AI-native" restructuring overhead** | Company rebuilds the org chart around AI before the tools have proven out | Meta's Applied AI Engineering (AAI) unit under Maher Saba (Mar–Apr 2026), with mandatory transfers and ultra-flat ~50:1 ratios; Meta is also using AI-generated performance reports and flattening layers explicitly to be "AI-native" — high-risk because the operating model is being changed before the supporting tools are validated |
| **10** | **Trust collapse / quality whiplash on the downstream side** | Throughput rises, review capacity doesn't, downstream metrics degrade | Faros AI *AI Engineering Report 2026* (22,000 devs, 4,000+ teams): median PR review time +441%, bugs/dev +54%, incidents/PR >3×, 31% more PRs merging with no review at all, PR size +51% |

### B. The 5–7 most common patterns, ranked by frequency in the 2023–2026 evidence

1. **Mandate-driven adoption theater / tokenmaxxing** — most pervasive. Documented at Meta, Microsoft, Salesforce, Amazon, Shopify (renamed leaderboard → "usage dashboard" after backlash). When leadership measures token consumption or usage rate, engineers game it; this is the single most reliable Goodhart pattern of the era.
2. **Stability/quality erosion downstream of AI throughput** — confirmed in DORA 2024 (AI adoption associated with −1.5% throughput, −7.2% stability), partially reversed in DORA 2025 (throughput now positive) but stability still negative; corroborated independently by Faros AI's 22,000-developer dataset.
3. **Charter ambiguity → absorption into Platform/DevEx incumbents** — CodeWhisperer → Q Developer (named, sourced); Microsoft's CoreAI rollup; Meta's repeated Reality Labs / AAI restructurings; pattern matches the structural finding that ~62% of orgs now have dedicated platform engineering teams (Red Hat 2024 platform-engineering survey).
4. **20% adoption ceiling** — repeatedly hit by Microsoft 365 Copilot (Morgan Stanley/RSM July 2025; 3.3% paid-add-on conversion), Stack Overflow's trust drop, and the underlying "Cautious are held in organizational stasis" archetype identified in academic diffusion research (Bick et al., arXiv 2601.21305).
5. **Top-down replacement reversals** — Klarna is the canonical case; the 55%-regret figure (Orgvue/Vitreous World Apr 2025; Forrester Oct 2025) suggests it's industry-wide; relevant for engineering orgs because the same dynamic applies to "AI replaces this team" claims.
6. **Sponsor-departure disbandment** — Meta Responsible AI (Nov 2023, The Verge); Take-Two AI tooling (2026); Microsoft DevDiv under Liuson (Apr 2026 departure). When the exec who funded the charter leaves, the team's surface area gets re-evaluated and usually compressed.
7. **Eval/feedback-loop debt causing production incidents** — Amazon Kiro–driven 13-hour outage (Dec 2025), Q Developer–involved outage; the SVP Treadwell memo explicitly names this as the cause. The DORA 2025 framing — "AI accelerates software development, but that acceleration can expose weaknesses downstream" — is the structural explanation.

### C. Early-warning diagnostic signals (per failure mode)

| Failure mode | Leading indicator | Threshold to act |
|---|---|---|
| Mandate theater / tokenmaxxing | Leadership starts citing token spend, completions, or "AI usage rate" in QBRs | Any time an exec asks for a leaderboard, treat as a category-1 risk |
| Stability erosion | PR size growing; review-time-to-merge growing; change-fail-rate creeping up | PR review time growth >50% YoY; bugs/dev >25% YoY; either should trigger an internal "rework rate" dashboard |
| Charter collision | Platform team starts shipping something that overlaps your surface; ML Platform asks "why isn't this in our stack?" | First overlap conversation → propose joint ownership in writing within 2 weeks |
| 20% ceiling | DAU/WAU ratio flat for 2 quarters; champions still the same 5 people | Adoption among engineers with ≥6 months tenure on the tool doesn't grow → drop one feature, double down on one workflow |
| Top-down replacement | Exec talks about "headcount efficiency" in same breath as AI tool | Push back in writing; require named, measurable workflow before any headcount conversation |
| Sponsor departure | Your VP sponsor changes scope, role, or leaves | Immediately audit charter; identify the next-highest-leverage exec who owns the *outcome* (not the *tool*) |
| Eval debt | Production incidents traced to AI-generated code; no incident-postmortem template for AI-caused failures | After the first AI-traced incident, require eval gates equivalent to human PR review |

### D. Political moves that turned fragile charters into durable ones

Across the cases where AI tooling survived 2023–2026 reorgs (Google's internal completion stack, Stripe's "Minions" coding agents writing 1,000+ PRs/week, Pinterest's MCP ecosystem with ~66,000 invocations/month across 844 active users saving ~7,000 hours/month, Meta's CodeCompose-now-Metamate), the recurring political moves are:

1. **Co-author metrics with the Platform/DevEx incumbents, don't compete on them.** Google's research blog explicitly attributes its internal-completion success to a "two-year collaboration between Google Core and Google Research, Brain Team" — i.e., the AI tooling team was structurally embedded in the existing IDE/code-search org from day one, not stood up next to it. Airbnb's Anna Sulkina explicitly restructured Developer Platform into "platform-agnostic teams focused on shared tooling and platform-specific teams focused on developer personas" rather than spinning up a parallel AI tooling org.
2. **Force a named internal customer with a quantified pain point.** Pinterest's MCP ecosystem ships with named owners, mandatory human-in-the-loop gates, and a quantified hours-saved number (~7,000/month per InfoQ April 2026). Stripe's Minions ships with a real, named throughput claim (1,000+ PRs/week, humans review). Tools without a named customer (Take-Two's AI workflow tooling; Meta's pre-Metamate CodeCompose before it was repositioned as a multi-model dev assistant) drift and get absorbed.
3. **Build eval infrastructure *before* requesting adoption.** Google's published methodology — the "funnel diagram" approach (model confidence → latency → quality → discoverability → engagement) — is the template. Amazon's outages are the counter-example: deploy first, eval later, get a SEV.
4. **Refuse the vanity adoption KPI even when leadership demands one.** Shopify's Farhan Thawar publicly walked back the token leaderboard after the Meta backlash, renaming it "usage dashboard" — and the relevant metric internally is now "whose tokens cost the most per token" (a proxy for deep work). The political move: make the executive ask you the harder question instead of giving them the easy one.
5. **Treat the charter as a permanent renegotiation, not a fixed mandate.** Meta's AAI/Reality Labs reorganization (Mar–Apr 2026) shows that even durable internal-AI orgs get restructured every 12–18 months. The teams that survive (Metamate, Google's completion stack) are the ones whose leaders treat the org chart as fluid and the *outcome* (devs ship working code) as the constant.
6. **Tie the tool to a regulated / measured surface** — code review, on-call, incident management — where impact is auditable. Generic "developer productivity" tools are easy to defund; tools that show up in DORA-style metrics or in an SLO dashboard are not.

---

## Details

### The DORA 2024 → 2025 reversal (and what it means)

**DORA 2024** (~5,000 respondents, *Accelerate State of DevOps Report*): 75% of devs using AI; a 25% increase in AI adoption associated with −1.5% delivery throughput, −7.2% delivery stability, −2.6% time on valuable work. 39% had low/no trust in AI-generated code. *AI adoption was net-negative for software-delivery performance.*

**DORA 2025** (~5,000 respondents, 100+ hours qualitative interviews; formally retitled *State of AI-Assisted Software Development*, released September 2025): 90% adoption (+14 pp YoY); median 2 hours/day with AI; 80% report productivity gains. *Throughput now positively correlated with AI adoption*, but stability is still negatively correlated. New "AI Capabilities Model" identifies 7 moderators: clear AI stance, healthy data ecosystems, quality internal platforms, working in small batches, user-centric focus, version-control rigor, fast feedback loops. The headline: **"AI doesn't fix a team; it amplifies what's already there."**

**Faros AI's *AI Engineering Report 2026: The AI Acceleration Whiplash*** (22,000 developers across more than 4,000 teams) corroborates the DORA stability finding hard:
- Median time in PR review: **+441%** vs. 2025; average time in PR review: **+199.6%**
- Median time to first PR review: **+156.6%**; PR size: **+51.3%**
- **31% more PRs merging with no review at all**
- **Bugs per developer: +54%** (was +9% a year earlier)
- **Incidents per PR more than tripled** ("for every code change merged, the probability of a production incident has more than tripled")
- Epics completed per developer: **+66.2%** — the lone org-level throughput win

**The METR study (and its Feb 2026 update)** is the cleanest evidence on individual productivity: 16 experienced devs averaging 5 years on repos with ~23,000 GitHub stars and 1M+ lines of code, 246 tasks, randomized; AI made them **19% slower** (Feb–June 2025 data, Claude 3.5/3.7 Sonnet). Full citation: Becker, Rush, Barnes, Rein (METR), "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity," arXiv:2507.09089 (July 12, 2025). Devs themselves predicted +24%, post-hoc still believed +20%. In Feb 2026, METR published a *methodological* update, not a retraction: their Aug 2025+ follow-up data was contaminated by self-selection (30–50% of devs declined to participate if it meant no-AI for half the tasks) — point estimates from the new (less reliable) cohort show -18% (original devs) and -4% (new devs) but with wide CIs. METR's own framing: "Based on conversations with study participants, we believe it is likely that developers are more sped up from AI tools now — in early 2026 — compared to our estimates from early 2025," but with no clean number.

### The mandate / tokenmaxxing era (Q1 2025 – Q2 2026)

The post-Shopify-memo era is now well-documented:

- **Shopify (Apr 2025):** Tobi Lütke's leaked memo — "Using AI effectively is now a fundamental expectation of everyone at Shopify," teams "must demonstrate why they cannot get what they want done using AI" before requesting headcount. AI usage added to performance and peer review questionnaires.
- **Meta "Claudeonomics" leaderboard (Apr 2026):** 85,000 employees, top 250 power users ranked, titles "Token Legend" / "Session Immortal." 60.2 trillion tokens in 30 days; at Anthropic API list prices that's ~$900M (Meta is internal; real cost likely $100M+). Top power user: 281M tokens/month. Pragmatic Engineer's Meta sources reported "massive waste," "outages caused by AI overuse," and that "those at the top of the leaderboard produce throwaway, wasteful work." Leaderboard taken offline after coverage.
- **Salesforce:** Mac widget displays personal token spend updated every 15 min; explicit minimum monthly spend (~$100 Claude Code + ~$70 Cursor = ~$170/mo, per Pragmatic Engineer); previously also a max ($250 Claude Code / $170 Cursor). Recently launched "Agentic Work Units" (AWUs) as a public rebuttal to token-as-metric.
- **Microsoft (Jan 2026 onward):** Internal token leaderboard "like Meta's"; engineers told Pragmatic Engineer they tokenmax to avoid being seen as low-AI users — e.g., asking AI to summarize internal docs they could read directly.
- **Amazon:** >80% weekly-AI-use target tracked on internal leaderboards; engineers used the in-house "MeshClaw" agent to inflate token numbers (FT). At least one team allegedly wrote a script to inflate usage 10× and topped an internal ranking (The Information).
- **Executive-class framing:** Jensen Huang (NVIDIA, GTC 2026 / All-In Podcast): "If his $500,000 engineer was not consuming at least $250,000 worth of tokens per year, he would be 'deeply alarmed.'" This is the framing that legitimizes the floor.

### Specific named team disbandments / absorptions

- **Meta Responsible AI team (Nov 2023):** Disbanded; staff absorbed into product orgs. The Verge broke it. Pattern: structural capability stripped from a central team and pushed into product, which means in practice it competes for cycles against ship deadlines.
- **Amazon CodeWhisperer → Amazon Q Developer (Apr 30, 2024):** TechCrunch quotes Doug Seven (GM/director, AI developer experiences at AWS): CodeWhisperer was "a bit of a branding fail." It "struggled to match the momentum of chief rival GitHub Copilot."
- **Microsoft DevDiv under CoreAI (Jan 2025) → Liuson departure (Apr 2026):** Nadella: "Azure must become the infrastructure for AI, while we build our AI platform and developer tools – spanning Azure AI Foundry, GitHub, and VS Code – on top of it." Liuson's 30+-year tenure ended as the org pivots away from IDEs toward "agentic development."
- **Microsoft consumer + commercial Copilot merger (Mar 17, 2026):** CNBC — Jacob Andreou over both; motivation explicitly cited as adoption gap (Copilot 6M DAU vs ChatGPT 440M, per Sensor Tower).
- **Meta CodeCompose → Metamate (early 2024):** Quietly added GPT-4 alongside Llama for internal coding; reported by Fortune Dec 2024. Quiet pivot — the original "Llama-only" charter was relaxed under usage pressure.
- **Meta Applied AI Engineering (AAI) under Maher Saba (Mar–Apr 2026):** Mandatory transfers from across Meta; Reality Labs "Foundations" group dissolved into product. WSJ + Reuters + The Information.
- **Take-Two AI tooling team (2026):** Dissolved despite 7 years of internal-workflow tooling work; CEO Zelnick rejects generative AI strategically. Outgoing leader started a consultancy.
- **Airbnb Developer Platform reorg under Anna Sulkina (2023–2025):** Restructured into "platform-agnostic teams focused on shared tooling and platform-specific teams focused on developer personas" rather than a standalone AI tooling team. Q1 2026 earnings: Chesky said AI now writes ~60% of new code; CTO leadership transferred to Ahmad Al-Dahle (ex-Meta Llama lead) at start of 2026.
- **Uber:** Pragmatic Engineer's reporting (Smith/Chada at Pragmatic Summit) — "AI adoption is slower than expected, even at a forward-thinking company like Uber. Top-down mandates are less efficient than engineers sharing their wins with peers." CTO Praveen Neppalli Naga (per The Information): "the budget I thought I would need is blown away already" — Uber exhausted its 2026 AI budget by April. ~95% of engineers use AI monthly; 70% of committed code is AI-generated; ~11% of live backend code updates entirely AI-agent-written.
- **LinkedIn:** Java→Python GenAI stack migration owned by infra (not a new AI tooling team); single OpenAI-compatible API for model-swap. "Project Nile" re-architecting the codebase to be "AI-native." LinkedIn cut engineering, product, and marketing roles in late 2025 (Shapero memo).

### Tools that visibly survived

- **Google internal completion stack:** Published methodology, eval funnel, A/B tested against developer-time outcomes. Productivity gains: 6% reduction in coding iteration time; 2.6% → ~50% of weekly checked-in code now AI-generated by 2025–2026 (Google's claim; treat the 50% as marketing-tinged but the trajectory is real).
- **Meta CodeCompose / Metamate:** Reported 22% acceptance, 8% of code authored — actually a strong number; survived because it was repositioned as an internal product (multi-model, multi-language) rather than a research artifact.
- **Stripe "Minions":** 1,000+ PRs/week, humans review. Named, measurable, owned by a real team.
- **Pinterest MCP ecosystem (your home turf):** ~66,000 invocations/month, 844 active users, ~7,000 hours/month saved, mandatory human-in-the-loop gates. The InfoQ writeup (April 2026) is the public-facing artifact — useful as internal precedent for "this is how Pinterest does it."
- **LinkedIn's Java→Python GenAI stack migration:** Survived because it was framed as a *platform* migration owned by an existing infra team, not a new tooling team.

### The CTO-visible / business-irrelevant trap

A specific pattern worth flagging: tools that get exec demos and earnings-call mentions but produce no durable production impact. Google's "more than 50% of code checked in weekly is AI-generated" claim is the highest-profile example — it's true on a definitional basis (any line touched by AI counts), but DORA's own 2025 finding that stability is still down means that "50%" is a measure of *generation*, not *durable impact*. Microsoft's earnings-call mentions of 15M Copilot paid seats sit against the 3.3% conversion rate from the Morgan Stanley/RSM AI Adopter Survey (July 2025): "If 79% deploy but only 3.3% of eligible users actually adopt the paid add-on, most 'deployments' are procurement exercises, not productivity gains."

The pattern for an internal-tooling EM: any time a tool is *primarily* described in executive comms (vs. in production SLOs, eval dashboards, or DORA-style metrics), the risk of business-irrelevance is high.

---

## Recommendations (staged, with thresholds that change them)

### Stage 1 — Now (0–60 days): Defensive instrumentation

- **Refuse to publish a usage leaderboard for Pinvestigator or Pinsight.** Publish *outcome* metrics instead: investigation-resolution-time saved per IC-hour, retrieval-experiment cycle time reduced. If leadership pushes for adoption %, give them "weekly active investigations completed using the tool with human acceptance" — not raw queries.
- **Write down the charter and named customer in one page.** Who owns the outcome if your tool disappears tomorrow? If the answer is "no one," the tool is fragile.
- **Get the eval/feedback loop infrastructure in place *before* you ask for more adoption.** Concretely: every AI-generated PR/output traceable to an internal eval, with an on-call rotation that owns regressions. If you can't point to a metric that would catch an Amazon-Kiro-style "delete and recreate" event, you don't have eval coverage.

**Trigger to escalate:** Pinterest's leadership starts asking for token spend, completions, or "AI usage rate" in eng QBRs.

### Stage 2 — Next quarter (60–180 days): Political consolidation

- **Co-sign a formal scope-of-ownership doc with ML Platform and DevEx.** Pinvestigator overlaps with ML Platform's serving/retrieval surface and DevEx's developer-workflow surface. Frame it as "joint ownership of investigation throughput" rather than "we own AI tooling." Airbnb's Sulkina model — platform-agnostic vs. platform-specific subteams — is the template.
- **Identify the highest-leverage non-EM exec sponsor whose *outcome* (not *tool*) you're accelerating.** If your VP sponsor leaves or pivots, this exec is your air cover. Lock them in by tying your tool to one of their named OKRs.
- **Publish an internal "what we won't do" doc.** Scope-starving is a stronger position than scope-creep. Pinterest's published MCP ecosystem doc is a good template because it explicitly defines what's in and out.

**Trigger to escalate:** First serious overlap conversation with Platform/DevEx; first time a sibling team ships something that does part of your job.

### Stage 3 — 6–12 months: Survival vs. exit

- **If the tool is durable (named customer, measurable outcome, eval coverage, joint ownership):** Push for it to be *absorbed* into Platform / ML Platform on your terms — i.e., as a fully staffed sub-org within the platform team, not as a tool to be ported. This is what survived at Google (Brain + Core collaboration) and at LinkedIn (Python migration owned by infra).
- **If the tool is fragile (no named customer, vanity metrics, sponsor wobbling):** Engineer your own pivot before someone else does. Identify the highest-impact business workflow Pinvestigator touches (likely on-call/investigation throughput) and reframe the tool as a *workflow product* with that one workflow as the primary surface. This is what Meta did with CodeCompose → Metamate.
- **Career optionality:** Build the public artifact (talk, blog post, conference paper) *before* you need it. Pinterest's MCP ecosystem InfoQ writeup is the kind of artifact that creates external optionality regardless of internal org outcomes.

**Trigger to escalate:** Sponsor leaves, OR adoption flatlines at <25% of addressable engineers for 2 consecutive quarters, OR Pinterest does a layoff that hits adjacent teams.

---

## Caveats

- **Confidence on DORA / METR / Faros: high.** These are the most rigorous public sources and the numbers are consistent across them (throughput up, stability down, individual perception ≠ reality).
- **Confidence on tokenmaxxing / mandate behavior: high but tilted toward Pragmatic Engineer reporting.** Orosz's sourcing (Meta, Microsoft, Salesforce, Amazon engineers; Shopify Head of Engineering on the record) is the single best body of evidence. The specific dollar figures (~$170/mo Salesforce minimum; 60.2T tokens at Meta) are well-sourced. The "$175 Salesforce + Microsoft" paired figure that floats in some secondary writeups is not corroborated by primary sources — the verifiable claim is ~$170/mo Salesforce alone. Microsoft has the leaderboard but no public floor.
- **Confidence on individual named disbandments: variable.** CodeWhisperer→Q, Meta RAI, Microsoft Copilot reorg, Take-Two AI tooling, Meta AAI/Reality Labs reorg are all primary-sourced. Beyond those, many AI tooling absorptions are not publicly documented because companies don't postmortem them. Blind/Glassdoor threads exist but aren't cited here because they're anonymous.
- **The METR Feb 2026 update is NOT a retraction.** Several secondary sources frame it as "METR backtracked." The actual METR position: the original 19% slowdown finding stands for early-2025 AI tools; the late-2025 follow-up data is methodologically compromised by self-selection; the qualitative direction is now likely positive but unquantified. Don't repeat the "backtrack" framing in internal communications.
- **Selection bias in this report:** the failures I can name are the ones that became public. The base rate of internal-AI-tooling-team failures is almost certainly higher than what's documented. Treat the absence of a named failure for any given company as the absence of evidence, not evidence of absence.
- **Pinterest-specific:** the public MCP ecosystem writeup is rare and unusually well-sourced; treat it as the template for how to communicate internal AI tooling externally, not just as a benchmark. Pinterest's Feb 2026 firing of two engineers who built scripts to track AI-driven layoffs is a different signal worth noting — there's clearly internal anxiety about AI-as-headcount-reduction, which is the political context any AI tooling lead at Pinterest is operating inside.
```