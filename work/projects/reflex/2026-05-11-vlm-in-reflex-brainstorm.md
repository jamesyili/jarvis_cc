# VLM in Reflex — Brainstorm & Ideas

**Date:** 2026-05-11
**Status:** Brainstorm (not yet a spec)
**Context:** Reflex currently uses VLMs narrowly — DS Agent pin verification only. Pinterest is a visual platform; VLMs should be a first-class sensor across all stages.

---

## Current State

The DS Agent has a `vlm_verification` analytical check that:
- Pulls image signatures from `galaxy_pin_features_iceberg` table
- Verifies that pin visual content matches what CG metadata claims
- Used to validate hypothesis cards before promotion to Opportunities

This is ~5% of what VLMs could do in Reflex.

---

## Ideas by Stage

### Detect Stage — VLM as Detection Sensor

#### 1. Visual Feed Quality Scoring

**What:** Sample a feed session (20 pins) for a user segment x market. VLM scores visual coherence, diversity, freshness, and quality.

**Detection example:** "JP feeds are visually monotonous — 14/20 pins are white-background product shots with no lifestyle imagery. US feeds for the same interest have 60% lifestyle + 40% product, correlating with 1.3x higher closeup rate."

**Implementation:**
- Query feedview data for a segment (market x user_state x interest)
- Pull top-20 pin image_signatures
- VLM scores each pin on: composition (1-5), relevance to interest (1-5), visual freshness (dated aesthetic? current?), content type (lifestyle/product/text-heavy/UGC)
- Aggregate into a "visual feed quality" composite per segment
- Compare across markets to find gaps

**Playbook fit:** New playbook `visual_feed_quality.md` or extension of `relevance_gaps.md`.

**Value:** Surfaces quality issues invisible to engagement metrics. A feed can have decent CTR but terrible visual experience (clickbait, low-res, repetitive).

---

#### 2. Visual Relevance Gap Detection

**What:** Take pins rated irrelevant in the relevance survey, pull actual images, ask VLM "WHY is this irrelevant visually?"

**Detection example:** "60% of irrelevant pins in BR-fashion are stock photos with watermarks. 25% are pins in the wrong language (English text on Portuguese user's feed). 15% are genuinely off-topic."

**Implementation:**
- Query `corequantuxr.hf_relevance_survey_responses_2025` for relevance <= 1 pins
- Join with image_signature
- Sample 50-100 irrelevant pins per market x interest segment
- VLM classifies irrelevance reason visually: wrong_language, low_quality (blurry/watermark/screenshot), off_topic, outdated_style, offensive, too_commercial
- Compare distribution of visual irrelevance reasons across markets/segments
- Identify systematic patterns (e.g., "all irrelevant pins from CG X are watermarked stock photos")

**Playbook fit:** Extension of `relevance_gaps.md` (add "Step 7: Visual irrelevance audit").

**Value:** Current irrelevance analysis uses boolean columns (interest_match, commercial, etc.) from survey — these are human-labeled at scale but coarse. VLM adds WHY at visual level, which is actionable for content quality teams.

---

#### 3. Content Quality Stratification by CG Source

**What:** For each CG source, sample 50 pins, VLM-score visual quality. Identify which CGs serve low-quality content.

**Detection example:** "GraphSage_WebActions serves 2.3x more blurry/cropped pins than P2P_Engaged. FollowingFeed has the highest visual quality (4.2/5) but lowest diversity (mostly same aesthetic). Shopping CGs serve 90% product-only shots — fine for commerce intent but poor for inspiration browsing."

**Implementation:**
- Query feedview_pin_stats by `home_feed_reason_to_choose` (CG source)
- For each CG: sample 50 pins (stratified by engagement: 25 high-engagement, 25 low-engagement)
- VLM scores: resolution (1-5), composition (1-5), content richness (1-5), visual diversity within cohort
- Aggregate per CG: mean quality score, quality variance, "low quality rate" (% scoring < 2)
- Cross-reference with engagement: do users engage MORE with higher visual quality within the same CG?

**Playbook fit:** Extension of `market_cg_performance.md` or new playbook `cg_visual_quality.md`.

**Value:** Reveals quality issues at CG level that explain engagement gaps. A CG might underperform not because its retrieval is bad, but because it retrieves low-quality content. Budget allocation should factor visual quality.

---

#### 4. Visual Supply Gap Detection

**What:** For a search query or interest, pull top results, VLM-assess whether they actually match the intent.

**Detection example:** "Top 20 results for 'modern farmhouse kitchen' — VLM assessment: 12 are genuinely modern farmhouse kitchens, 4 are traditional/rustic (not modern), 2 are bathrooms mislabeled, 2 are ads. Visual precision: 60%. Comparable query 'scandinavian kitchen' has 85% visual precision."

**Implementation:**
- Pick high-volume queries from search feedview data
- Pull top-N results (pins) for each query
- VLM evaluates: "Does this image match the query '[X]'? Score 1-5 and explain."
- Compute visual precision per query class
- Identify query classes with systematically low visual precision
- Cross-reference with search refinement rates (do users refine more when visual precision is low?)

**Playbook fit:** New playbook `visual_supply_audit.md` (Search surface) or extension of `supply_gaps.md`.

**Value:** Search relevance today is largely text-embedding based. VLM adds ground truth on "does this LOOK like what the user wanted?" Particularly high-value for visual-first queries (home decor, fashion, food styling) where text descriptions are unreliable.

---

#### 5. Visual Trend Drift Detection

**What:** Compare pin cohorts from 30 days ago vs today for a given interest. Detect whether we're serving stale aesthetics.

**Detection example:** "Pinterest's 'living room design' content has drifted toward a 2022-2023 aesthetic (minimalist beige, dried pampas grass). External trend signals show 2026 moving toward bold color and maximalism. We're lagging trend by ~18 months for this category."

**Implementation:**
- For high-volume interests: pull pins served 30 days ago vs pins served today
- VLM describes dominant visual style of each cohort
- VLM compares: "Has the visual style shifted? Is cohort A or B more 'current'?"
- Identify interests where visual freshness is stagnating
- Cross-reference with content upload dates — are we surfacing old pins?

**Playbook fit:** New playbook `visual_trend_freshness.md` or extension of `follow_graph_health.md` (stale signals → stale content).

**Value:** Pinterest's core value prop is inspiration and trend-forward content. Serving stale aesthetics is a silent killer — users won't complain, they just leave. VLM can detect this before it shows up in retention metrics.

---

#### 6. Visual Diversity Audit

**What:** For a given user session, assess visual diversity. Are we showing the same thing 20 times?

**Detection example:** "High-engagement users in US-HomeDecor see 70% visual diversity in their feed (varied styles, angles, settings). Low-engagement users in the same segment see 45% diversity — their feed looks like the same pin repeated. Filter bubble has a visual signature."

**Implementation:**
- Sample user sessions (feed impressions within a single session)
- VLM pairwise similarity: for each pair of adjacent pins, "how visually similar are these?" (1-5)
- Compute session visual diversity score: mean pairwise dissimilarity
- Compare across engagement tiers, user states, markets
- Identify segments where visual monotony correlates with low engagement/retention

**Playbook fit:** Extension of `filter_bubble.md` (visual dimension of explore/exploit imbalance).

**Value:** The filter_bubble playbook currently measures topic diversity via CG decomposition. Visual diversity is a separate axis — you can have topic diversity but visual monotony (e.g., 5 different "modern kitchen" pins that all look identical). VLM detects the visual dimension.

---

### Build Stage — VLM as Verification Layer

#### 7. Visual Before/After for CG Experiments

**What:** After generating a CG sizer experiment change, simulate what the feed LOOKS like. Pull sample pins from the boosted CG, render a hypothetical feed comparison, VLM assesses.

**Use case:** Build Agent generates "+20% GraphSage_WebActions budget." Before human approves:
- Pull 10 representative pins from GraphSage_WebActions
- Pull 10 representative pins from the CG losing budget (e.g., P2P_Engaged)
- VLM comparison: "The boosted CG serves more diverse web-sourced content but lower image quality. The losing CG has high-quality curated pins. Net effect on feed: slight quality decrease, significant diversity increase."

**Implementation:**
- Extend CG Sizer Build Agent (Step 7: "Visual Impact Preview")
- Query `reason_to_choose` data to get sample pins per CG
- VLM scores both CG cohorts on quality, diversity, relevance
- Present to human alongside the code diff: "Here's what the numbers look like, and here's what it LOOKS like"

**Value:** Humans approve experiments based on code and metrics projections. Seeing the actual visual impact makes approval decisions much more informed. "Yes the numbers say +5% budget, but look — those pins are all low-quality product shots. Maybe we should add a quality filter."

---

#### 8. Visual Regression Detection for Config Changes

**What:** For blender utility weight changes, show what gets promoted vs demoted visually.

**Use case:** Blender Utility Build Agent generates weight changes that boost "engagement" signals. Before shipping:
- Pull pins that would be promoted (high engagement signal, low current rank)
- Pull pins that would be demoted (low engagement signal, currently ranked high)
- VLM assessment: "Promoted pins: mostly viral/clickbait content. Demoted pins: high-quality original photography. Warning: this weight change may degrade visual quality of top-of-feed."

**Implementation:**
- Extend Blender Utility Build Agent with visual preview step
- Use existing pin scoring data to identify promotion/demotion candidates
- VLM evaluates content quality shift

**Value:** Prevents "engagement farming" — weight changes that optimize metrics but degrade the visual experience. A VLM can catch what A/B tests only show after 2 weeks of data.

---

### Simulate Stage (NEW) — VLM as Judge

#### 9. VLM-as-Feed-Judge (Zero-Cost Experiment Preview)

**What:** Given an opportunity card, construct a hypothetical feed under the proposed change, and have a VLM judge whether it's better.

**Concept:** Instead of running a live A/B test (expensive, time-consuming), simulate the visual outcome:
1. Take the current feed composition for a target segment
2. Apply the proposed change (e.g., boost CG X by 20% → swap 4 of 20 pins)
3. VLM judges both feeds on: relevance, diversity, quality, inspiration, coherence
4. Output: directional confidence ("75% likely to improve feed quality for this segment")

**Implementation:**
- New stage: `simulate/` directory in Reflex
- Input: Opportunity card GID (from Detect) + proposed change spec
- Steps:
  1. Sample current feed for target segment (20 pins from feedview data)
  2. Compute treatment feed (swap pins according to proposed budget/weight change)
  3. VLM scores both on 5 dimensions (relevance, diversity, quality, inspiration, coherence)
  4. Report: per-dimension delta + overall recommendation + confidence
- Output: Simulation report attached to the Asana card

**Key insight:** This doesn't need to be accurate in absolute terms. It needs to be directionally correct — "is this change likely to help or hurt the visual experience?" Even 65% accuracy is valuable as a fast pre-filter before committing engineering time to a live experiment.

**Value:** Transforms the pipeline from "detect opportunity → build code → run expensive experiment → learn" to "detect opportunity → simulate cheaply → only build/experiment the ones that pass simulation." Could 5x the effective throughput of the system.

---

#### 10. VLM-Powered A/B Preview

**What:** Render two pin grids (control vs treatment), VLM compares side-by-side.

**Concept:** The most intuitive version of simulation — literally show what the two arms look like.

**Implementation:**
- Render control: 4x5 grid of current feed pins (image thumbnails or descriptions)
- Render treatment: same grid with proposed changes applied
- VLM comparison prompt: "Compare these two feeds for a [segment] user interested in [topic]. Which is better? Why? What risks does the treatment introduce?"
- Output: Structured comparison (per-dimension scores + qualitative narrative)

**Variations:**
- Single user archetype (e.g., "25yo female, US, interested in home decor, casual user")
- Multiple archetypes (run for 5 different user profiles, aggregate)
- Adversarial prompting ("what could go wrong with the treatment feed?")

**Value:** Makes the simulation output human-interpretable. PMs and EMs can look at the visual comparison and make a judgment call without understanding the underlying ML mechanics.

---

#### 11. Visual pRelevance Predictor (Offline Relevance Scoring)

**What:** Use VLM judgments on historical survey pins to build a cheap, fast visual relevance signal.

**Concept:** The relevance survey is expensive (human raters). VLM judgments on "is this pin relevant to this user's interest?" could serve as a cheap proxy, enabling:
- Scoring proposed feed changes without live traffic
- Augmenting the survey with more coverage
- Detecting relevance degradation between survey runs

**Implementation:**
- Take historical survey data: (pin_image, user_interest, human_relevance_score)
- Run VLM: "Rate relevance 1-5 of this [image] for a user interested in [interest]"
- Calibrate: what's the VLM-to-human correlation? (hypothesis: 0.6-0.75)
- If correlation is good enough: use VLM-relevance as a fast offline signal
- Apply to simulation: "for proposed feed changes, compute VLM-relevance delta"

**Value:** If this works, it's a game-changer. You get pseudo-relevance-survey data at 1000x the scale and 100x the speed, enabling rapid iteration without waiting for human ratings.

---

### Prove Stage (NEW) — VLM as Experiment Monitor

#### 12. Visual Experiment Arm Auditing

**What:** During a live experiment, sample feeds from control and treatment, VLM describes the visual differences.

**Concept:** Metrics tell you WHAT changed (CTR +2%). VLM tells you WHY visually ("treatment arm has more lifestyle imagery and fewer text-only pins").

**Implementation:**
- During active experiment: daily sample of 20 pins per arm (control + each treatment)
- VLM describes: dominant content types, visual quality distribution, diversity, notable patterns
- Compare across arms: "Treatment shows 30% more DIY/craft content, 15% fewer product-only pins"
- Correlate with metric movements: "the +2% CTR is likely driven by the lifestyle imagery increase"

**Playbook fit:** New prove-stage automation or extension of experiment_review playbook.

**Value:** Today, interpreting experiment results requires manual feed inspection ("go look at what's different"). VLM automates this entirely. Also catches unintended side effects: "we boosted CG X for better relevance, but it's also introducing more low-quality content."

---

#### 13. Visual Guardrail (Automated Quality Gate)

**What:** Continuous monitor that flags when a feed segment becomes visually degraded.

**Concept:** An always-on quality gate that runs during experiment ramps:
- If visual diversity drops below threshold → alert
- If visual quality drops below threshold → alert
- If content type distribution shifts dramatically → alert

**Implementation:**
- Prove stage automation runs daily during active experiments
- Samples feeds from treatment arm
- VLM scores: diversity, quality, content type distribution
- Compares to baseline (pre-experiment) and control arm
- Threshold triggers: >20% diversity drop, >0.5 quality score drop, >30% content type shift
- Output: Slack alert + Asana comment on experiment card

**Value:** Prevents shipping experiments that "win on metrics but lose on experience." A CG budget change might improve SSv2 (more successful sessions) while making the feed visually worse (users click more because pins are clickbait, not because they're inspiring). Visual guardrail catches this.

---

#### 14. Post-Ship Visual Monitoring

**What:** After an experiment ships, ongoing VLM monitoring to detect long-term visual drift.

**Concept:** Some experiments look good at launch but degrade over time (content creators adapt, supply changes, user behavior shifts). Visual monitoring catches drift.

**Implementation:**
- Weekly sample of feed segments affected by recently shipped experiments
- VLM comparison: "how does this segment look compared to 4 weeks ago (pre-ship)?"
- Trend tracking: visual quality / diversity / freshness over time
- Alert if trend is negative: "shipped experiment X 3 weeks ago, feed quality for segment Y has been declining steadily since"

**Value:** Closes the monitoring loop. Currently, shipped experiments are "fire and forget" — metrics are watched for a few weeks, then attention moves on. Visual monitoring adds a persistent quality signal.

---

## Priority Matrix

| # | Idea | Effort | Impact | Stage | Dependencies |
|---|------|--------|--------|-------|-------------|
| 3 | Content quality by CG | S | High | Detect | VLM access to pin images |
| 2 | Visual relevance gap detection | M | Very High | Detect | Survey data + VLM |
| 1 | Visual feed quality scoring | M | High | Detect | VLM + feedview data |
| 7 | Visual before/after for Build | M | High | Build | Extends existing Build agent |
| 9 | VLM-as-feed-judge | L | Transformative | Simulate | Hypothetical feed construction |
| 11 | Visual pRelevance predictor | L | Transformative | Simulate | Calibration study needed |
| 4 | Visual supply gap (Search) | M | High | Detect | Search data + VLM |
| 6 | Visual diversity audit | M | Medium | Detect | Session-level pin data |
| 5 | Visual trend drift | M | Medium | Detect | Time-series pin sampling |
| 12 | Experiment arm auditing | M | High | Prove | Active experiment access |
| 13 | Visual guardrail | M | High | Prove | Continuous monitoring infra |
| 10 | A/B preview grids | M | Medium | Simulate | Rendering pipeline |
| 8 | Config change regression | S | Medium | Build | Weight → pin mapping |
| 14 | Post-ship monitoring | S | Medium | Prove | Scheduler |

## Key Open Question

**What VLM access do we actually have?**

The DS Agent's `vlm_verification` check uses `galaxy_pin_features_iceberg` for image signatures. But the critical question is: can we pass an image (or image URL/signature) to a VLM and get a text judgment back?

Options:
- **Claude's native vision** — If we can resolve image signatures to URLs and pass them to Claude, we have VLM for free (Claude IS the VLM). Token cost is the constraint.
- **Pinterest internal VLM** — Is there a VLM MCP tool or service that takes image signatures and returns descriptions/judgments?
- **Pre-computed embeddings only** — If we only have CLIP-style embeddings, we're limited to similarity/clustering (no open-ended visual judgment).

The answer to this determines which ideas are immediately buildable vs need new infra.

---

## Suggested Next Steps

1. **Determine VLM access path** — What's available today? Can we pass images to Claude via MCP?
2. **Start with #3 (Content quality by CG)** — Smallest effort, high value, extends existing DS Agent pattern
3. **Prototype #9 (VLM-as-feed-judge)** — If VLM access works, this is the highest-leverage addition to Reflex. It creates the Simulate stage.
4. **Design the Simulate stage directory structure** — Even before implementation, define the interface: what does a simulation report look like? How does it connect Detect → Build?
