# Source 09 — The GenAI side of the program: Lily's distribution one-pager, three weekly-sync notes (8/11 · 8/17 · 8/24), the UXR survey TLDR, and the Blue-GenAI-pins dev tool

> **Source of record.** Pasted by James Tue 2026-08-25 AM ("given the pivot towards GenAI, let me give you context on the framing/learnings from Dhruvil and Lily … as well as the current 12 week plan and status"). Three parts: (A) *Advancing GenAI Signal Adoption in Personalization* — Lily Li's one-pager, last updated Jul 27, 2026 (= the **Distribution** workstream one-pager of the 12-week plan; James + Dafang are DRI on the L1 utility line); (B) the *12-Week Plan to Improve User Trust* weekly alignment sync notes for Aug 24, Aug 17, Aug 11; (C) three screenshots in `09_assets/` — the iOS dev-tools "Blue GenAI pins" toggle, the UXR survey question design (Stephanie Chen), and the WIP survey TLDR. Verbatim below; Leo read at the end.

---

## A. Advancing GenAI Signal Adoption in Personalization (Lily Li, updated Jul 27, 2026)

**Key contributors:** Personalization: Andrew Yaroshevsky, Dylan Wang, Michael Weissinger, James Li, Dhruvil Deven Badani, Dafang He, Tim Leung. Content Quality: Faisal Farooq, Qinglong Zeng, Adam Avery.

### Goal
We have urgency to improve user trust regarding GenAI content. We should use a multi-layer intervention strategy rather than only filtering, and we need one shared metric stack so we can make faster tradeoffs.

Note: We hope to apply the learning beyond GenAI, to other signals, including quality, safety, credibility, and racy / borderline content. The longer-term opportunity is to build a stronger personalization stack that can incorporate these signals more systematically.

### 12-Week Plan: What We Should Try Next

| Intervention layer | Idea | Status | Proposed DRI | What it means in practice | Why it's promising |
|---|---|---|---|---|---|
| Softer downstream shaping | **Add GenAI into utility (L1) for IsGenAI_v3 image signals** | In Progress — https://helium.pinadmin.com/hf_l1_utility_gen_ai_exp/ | Personalization — **James Li + Dafang** | Use GenAI signal as part of distribution shaping so the system can trade off relevance and GenAI sensitivity more explicitly. *Qinglong Zeng:* Two types of utility changes we can make: (1) Penalize GenAI slop to minimize all pinners' exposure; (2) Penalize all GenAI for opt-out users and low gen-ai-affinity users to better honor user preferences. CQ team has just developed a GenAI user affinity signal. | Makes use of the full signal spectrum rather than a binary threshold |
| Softer downstream shaping | **SSD / diversification / spacing after utility (L2)** | In Progress — experiment not started | Personalization | Spread out or reduce concentration of GenAI content after ranking rather than only removing it. `genai_all_images_p2p_spacing`. We can reuse spacing framework we built earlier which is SSD based. | Lower-risk way to improve experience without relying only on hard filtering |
| Harder upstream enforcement | **Learn to filter more aggressively** | Evaluate next — not started | Personalization | Tighten filtering in PinSelection / early funnel / L1 so more low-confidence or low-quality GenAI content is suppressed before ranking | Most direct way to reduce bad GenAI exposure at scale |
| Harder upstream enforcement | **Remove GenAI content, and vertical-specific enforcement** | Evaluate next — not started | Content Quality | Run arms focused on removing AI content to understand the engagement trade-offs, and on specific verticals where GenAI pain is highest rather than one uniform policy. *Jianjin Dong / Sari Wang:* Proposed to consolidate this with the GenAI ablation exp for DS analysis. The CQ team picked verticals where AI load to retention is primarily sloping downwards: GenAI load vs. Retention | Different verticals may need different levels of aggressiveness |
| Model / training interventions | **Training-data interventions in UPP** | Need offline evaluation | Personalization | Remove or downweight GenAI content in training data. *Jianjin Dong:* We can try to downweight GenAI content regardless of users' preferences. Or we can try downweighting more if it is opt-out users or users with low GenAI affinity. | Could improve model behavior more fundamentally than downstream filtering alone |
| Model / training interventions | **Remove GenAI from SSv2 first** | Need offline evaluation | Content Quality | Start training-data intervention in SSv2 before broader rollout | More scoped way to learn impact before wider changes |
| Strategic alternative | **Promote authentic content directly** | Longer-term / exploratory | Personalization | Instead of only suppressing GenAI, explicitly favor authentic content where appropriate | Could become a stronger long-term framing for user value |

### What We've Tried

**1. Filtering**

What we have tried so far:
- **Global GenAI slop-domain filtering** — Filtered pins from high-confidence GenAI-heavy domains in sensitive/actionable L1s: Food & Drink, DIY & Craft, Event Planning, Gardening. Main production-style threshold: GenAI domain score ≥ 0.6. Applied across major surfaces including Home Feed, Search, P2P, and Notifications.
- **More aggressive Food & Drink domain filtering** — Tested lower domain-score thresholds specifically for Food & Drink, where GenAI slop is especially visible. Tested thresholds: 0.5, 0.45, and 0.3, compared with the existing 0.6 baseline. Goal was to increase recall on recipe / food content-farm domains while monitoring engagement and backfill quality.
- **Classifier-based GenAI opt-out filtering** — Moved from older GenAI v2 signal to GenAI v3 for disclosure and opt-out enforcement. For opt-out filtering, tested / used thresholds around: GenAI v3 score ≥ 0.12 combined with P2I category confidence, e.g. P2I v9 ≥ 0.4 for CFS opt-out filtering. This expanded the system's ability to identify GenAI pins eligible for opt-out filtering.
- **All-category GenAI opt-out backend filtering** — Tested backend filtering for users who opted out of all GenAI categories. Tested GenAI thresholds: 0.10, 0.11, 0.12. Recommended the least aggressive arm, 0.12, because it matched existing L1-level opt-out behavior and reduced over-filtering risk.

What we learned:
- **Hard filtering works best for clear cases** — effective for obvious GenAI slop domains and for honoring explicit user opt-outs; less appropriate as a blanket solution for all GenAI, because not all GenAI content is low quality.
- **Domain filtering drives strong quality wins** — GenAI domain filtering, especially in Food & Drink, materially reduced low-quality sessions and non-functional sessions. Confirms domain-level signals are good at catching scaled GenAI content-farm behavior.
- **Lower thresholds improve recall but create tradeoffs** — moving below the conservative 0.6 domain threshold catches more slop, but increases false-positive and backfill risk. The aggressive Food & Drink test showed quality wins, but also surfaced replacement-quality issues.
- **Backfill quality matters as much as filtering quality** — when we remove bad GenAI domain content, the system has to replace it with something. Some replacement content was linkless, spammy, or lower quality, so future launches need stronger backfill / substitution analysis.
- **Opt-out filtering is viable but should stay conservative** — backend opt-out filtering passed core guardrails and showed we can honor explicit pinner preferences. Best launch choice was the conservative 0.12 threshold to avoid over-filtering and keep behavior consistent across individual L1 and all-category opt-out controls.
- **Filtering should be one layer, not the whole strategy** — use filtering for clear slop and explicit user preference enforcement; use demotion, spacing, and ranking for gray-zone GenAI, density fatigue, and personalized tolerance.

**2. Adding IsGenAIv3 into ranking**

We have integrated GenAI v3 into pinnability on both content and user towers:
- Content tower: GenAI v3 is used on the candidate pin side.
- User tower: isGenAI is logged at the per-impression / per-activity level in the real-time sequence and fed into the user tower through sequence-derived affinity features.

What we learned so far:
- The first online experiment using GenAI v3 as a direct pinnability feature showed **flat topline engagement with no positive signal**.
- We then iterated with a more P2P-style approach by feeding GenAI into the user tower via sequence-level embeddings. **Offline results were negative, so we did not launch another live experiment.**

### How We Will Measure Success

1. **GenAI Prevalence** — Leverage content quality team's GenAI prevalence score to measure how much GenAI content users are actually seeing, and how that changes by vertical, threshold band, and possibly user cohort. GenAI prevalence by user affinity: for users with low affinity to AI content, we want to see prevalence go down during the experiment period; for users with higher affinity, staying stable or increasing.
2. **Perception / User Trust** — Do users feel the experience is more relevant and less frustrating? UXR measurements: survey responses (Stephanie Chen); sentiment survey (Ruixue Zhaoyang) — the original GenAI pain point, "20% of surveyed users to our daily sentiment survey reported being frustrated by 'seeing too many AI-generated images,'" was a result from this quantitative survey. "See Less" rate (i.e. hide metric) on AI pins going down as we tune targeting; ideally sliced to pinners who (1) click SL on AI-modified content, and/or (2) click "See fewer AI {topic} Pins" from the overflow menu.
3. **Engagement and retention guardrails** — continue to measure short-term engagement, but not as the only decision-maker. For larger interventions, especially ablations, also measure longer-term outcomes, including retention effects over the planned 5-week runtime. Increase in regrettable (on non-GenAI content) engagement; decrease in non-regrettable (on GenAI content) engagement; overall impressions (aka prevalence) of GenAI content.

### Other Open Questions
- How should we define prevalence?
- How should we measure perception / perceived relevance?
- How differentiated should interventions be by vertical or cohort?
- What engagement tradeoffs are we willing to accept?

---

## B. 12-Week Plan to Improve User Trust — weekly alignment sync notes

Resources: Content & Signals MBR 2026 · [In-development] Program Tracker. Slack: general forum `#12-week-plan-ai-user-trust-wg` · controls: `#search-genai-filter` (search filter), `#gen-ai-homefeed-tuner` (everything else) · T&S `#spam-owners-for-12-week-ai-user-trust-wg` · distro `#genai-feed-wg` · PMM `#genai-controls-gtm-h2-2026` · measurement `#measurement-12-week-ai-user-trust-wg`.

**Program timeline (all three weeks show the same five steps):**
- **Step 1 (July 27–31): Align and lock scope** — ⚠️ Align on goals, metrics, launch criteria · ⚠️ Finalize projects, confirm resourcing and tradeoffs · ✅ Launch and ramp Search filter
- **Step 2 (Aug 3–Sep 4): Development** — external-facing features (experiment-ready or further) · establish measurement, reporting, and baseline · external GTM strategy
- **Step 3 (Sep 7–18): Experiment and refine** — external-facing features in-experiment, LR-ready
- **Step 4 (Sep 21–Oct 2): Initial launch** — begin ramping external-facing features · track measurement shifts in perception/engagement
- **Step 5 (Oct 5–16): Expand and plan** — continue ramp based on initial impact readout · monitor and report on measured shifts · evaluate future plans based on learnings

### Aug 24, 2026 — "This week: keep on truckin' 🚚"

**Leadership Roadmap Review (link):** Overall, it was well-received! **DJV believe that for this timeframe, the tactics and projects we've outlined are the right ones to focus on.** In bringing up concerns around "does this move the needle enough," they see our current roadmap as sufficient to show action, and be a good set of features to inform future action. We should not make large-scale changes (e.g. "add in site-wide Low GenAI mode button") at this point, but rather use Step 5 "Expand and plan" to assess reception of the current plan.

What they asked for:
- Measurement of how successfully we surface awareness-drivers to users? Examples: how many users see our awareness drivers; how many times is a user shown these drivers.
- Quantifiable goals for T&S workstream.
- **More specific timeframe for distribution launches** (didn't show everything we have here for brevity).

What we may want to shift in the next few weeks:
- Consider single "opt out of all AI" toggle in settings (this was previously implemented, but never launched).
- Consider further in-app upsells (given past success) to offset narrowing of controls triggering.
- Consider increasing disclosure of "behind-the-scenes" work in GTM.

**Workstream updates and to-dos:**

**(Aligned, slightly behind schedule) Distribution** (one-pager = Part A):
- More aggressive demotion of AI content for fully opted-out users
  - **(in experiment) Homefeed:** Just relaunched experiment by using new L1 interest feature — exp data ready by end of this week. Sequencing: current experiment is full opt-out. End of next week: can likely conclude current experiment. Following this: start partial opt-out experiment; at same time, launch 3.1 experiment for opt-out.
  - **(aligned, in discussion) P2P:** Reached alignment to run L2 demotion experiment (technical discussion ongoing).
- **(on track, preparing experiment) Updating opt-outs/labeling/Search filter to GenAI image v3.1** (retraining model) (TDD): model evaluation, thresholds being selected for experiment; experiment started on Friday, ramping now; **all opt-out/filter thresholds need to be consistent across experiences.**
- **(in experiment) GenAI domain / DQv4 spam demotion on P2P:** experiment re-launched, currently running.
- **(aligned, in discussion) Spacing on Homefeed:** have alignment to run experiment, technical discussion in progress **(DRI?)**.

**(Still finalizing holdouts) Measurement** (Sponsor: Anoop Suri):
- In-app survey for AI control perception (DRI: Stephanie Chen): [Mid August Learnings] WIP deck *12 wk AI Sprint Survey Measurement* — will schedule 30 mins for shareout w/ this group when all Aug data complete. Sizing/feasibility estimate for BE/FE holdout measurement complete.
- Program holdout definition and setup (DRI: Kevin O'Sullivan): **both holdouts are set up and ready for experiments to begin** (just confirmed this morning).
- GenAI ablation holdout (DRI: Jianjin Dong, Wenjun Wang on DS): **Delayed** (see update from last week). [KO] Q4 — looking into doing the most slimmed-down version possible to get some data points before planning. Will resolve this week.

**[Possible enforcement blocker] Trust & Safety** (Sponsors: Neeti Deshmukh, David Breger) (one-pager):
- Domain Network Signal v1 launch (DRI: Ragib Ahsan): reviewing exp results tomorrow, LR ~2 weeks from now.
- Spam User Network Signal v1 launch (DRI: Beatrice Zhang) — MVP roadmap: **Phase 1 (Aug 17–Sep 4):** first batch of user clustering on sites.google and cuttly; samples to Policy and SME for review guidelines; expand clustering along additional heuristics/signals (shared image, shared link, same-day signup) and additional high-suspicion high-impression domains. **Phase 2 (Sep 7–25):** enforce in batches, highest-confidence tier first, deduped against accounts already actioned; measure precision per tier; report net-new coverage and impression impact; kick off distribution-filtering mechanism for the lower-confidence tier with the relevant eng team; continue expanding domain coverage. **Phase 3 (Q4/Jan):** longer-term engineering solution for a scalable daily-run signal, target end of Dec / early Jan.
- Policy updates (DRI: Niki Kakarla): external policy launch date **Nov 12**; interim policy changes live.
- Pre-policy-update proactive sweeps (DRI: Hannah Lynch, Siddhant Mohapatra): initial human reviews with new policy started — ~100% action rate with ads, 70–80% for product pins; advertiser-level enforcement not a perfect action rate (min-% threshold). Pulling more samples and impact data. Next: BPO capacity to review at scale. Working to get initial cluster of Etsy stolen pins approved by Risk Intelligence — unclear if approved for deactivation; BPO review unlikely near-term (tooling can't expose coordination patterns); may need less-severe intervention (e.g. "hiding" accounts) — Adam talking with Becky tomorrow.

**GenAI Controls** (Sponsors: Andrew Yaroshevsky, Raymond Han, Mira Steckel):
- **[v1 Launched] Search Filter** (DRI: Julia Starostenko) (execution plan). Learnings: overfetching does not mitigate the loss of engagement at top of feed due to low filter precision; further backend tuning will help bridge the gap without sacrificing UX. Improvement roadmap: (exp start late Aug) move filtering up-funnel to PinSelection — DRI Ahmed Fayez, Adam Kerr implementing; (end of Aug) shorten button copy to "Less AI" / modify placement (helium) — early metrics promising, metric readout targeting 8/31; (end of Aug) tune filter triggering — DRIs Mukuntha Narayanan, Raymond Liu, experiment start targeting 8/27; (mid-Sept) migrate to refreshed isGenAIv3 signal — DRI Mansour Saffar, experiment live as of last Friday, call this week whether to tune thresholds (reversioning) or proceed to full ramp; (Aug/Sept) Android — DRI Christina Yun — OneBar LR 9/9, filter pane LR 9/30; (Aug/Sept) dweb — DRI Andy Chen — OneBar+filterpane LR 9/9; mweb TBD.
- **(In Progress) Other GenAI controls** (DRI: Lily Li) (one-pager: *Making AI Controls Discoverable Across Pinterest: Product Requirements*): See More / See Less GenAI flyout — launched v2 GenAI flyout experiment Thursday last week (updated triggering); will gate the flyout later in the lifecycle (e.g. grid_index ≥ 50) and raise the unengaged-GenAI-pin threshold — push it later and toward truly disengaged Pinners; anchor the flyout to specific high-confidence GenAI pins prioritized by the L1 categories with the highest opt-out; copy/UX work to follow. Global nav UX button on HF to get to AI content controls — on track, design + eng resourcing approved, experiment ~mid-September. Talking with Design about a global opt-out button/toggle in *Refine your recommendations*.
- Insights/Analysis for genAI: Signals team AI learnings for planning — *Summary of AI load × retention analysis* · *Summary of AI load vs pinner survey fulfillment*.

**[On track, adjusting approach] PMM & User Education** (Sponsor: Rachel Hardy): GTM strategy (DRI: Catie Marques Teles) — after discussing risks and dependencies, aligned on planning around a **go/no-go date (likely 10/8)** on timing and GTM tactics; Rachel met with Vicky and is running recommendations by Sara later today; scenario planning for 10/8. Measurement strategy (DRI: Catie) — GTM focus on awareness, sentiment as guardrail (*12-Week Plan: External Perception Measurement Plan*).

### Aug 17, 2026 — "This week: continue development, roadmap review w/ DJV later this week"

**(In Progress) Distribution** (Sponsors: Anoop Suri, Andrew Yaroshevsky):
- **Experiment #1:** demote AI-modified pins (**>0.09 demoted; >0.12 is already filtered**) for fully opt-out users in homefeed L1 utility — https://helium.pinadmin.com/hf_l1_utility_gen_ai_exp/ — re-launched at the end of last week. Next steps: explore adding **GenAI user affinity signals to L1** (new signals from CQ); evaluate if we can add **11 GenAI categories to L1 LWS**; evaluate the **soft demotion penalty risk**.
- **Experiment #2:** SSD spacing in homefeed L2. Defining a DRI from LR; will reuse the CQ × Notifications framework.
- Adopting DQv4 spam signal for demotion on all surfaces (DRI: Jianjin Dong) (one-pager): Search — launched (LR); **P2P — blocked in LR, need support in alignment/approval**; HF — discussions ongoing; Notifs — to start this week.

**(Still finalizing holdouts) Measurement:** in-app survey launched, baseline results ETA next week; program holdouts — have DRI for BE holdout, need FE holdout (Kevin to discuss with Kurchi); proposal doc for 2 holdouts, FE-focused (controls UI) and BE-focused (distro); GenAI ablation holdout likely delayed given how many AI-related launches are coming (available user pool for ablation is tricky).

**PMM & User Education:** pre-review with Sara today; separate review to schedule. GTM focus on awareness, sentiment as guardrail.

**GenAI Controls:** Search filter improvement roadmap — over-fetching of non-AI results (DRI: Roberto Konow): engagement neutral / very mildly negative, mixed on relevance, **likely will not ship**, wait for up-funnel PinSelection improvement; PinSelection up-funnel (Ahmed Fayez, Adam Kerr) on track; "Less AI" copy/placement approved, iOS ramp this week, ~3 weeks data (8/31 readout); isGenAIv3 migration (Mansour) on track; Android/web/mweb (Christina Yun, Andy Chen) — OneBar LR/ship ETA Sep 9, filter pane LR Sep 24. Other controls (Lily): concluded the iOS GenAI see-more/see-less flyout experiment (learnings), wrapping Android, web starting this/next week — `ios_homefeed_gen_ai_flyout`, `android_gen_ai_flyout`. **Debugging tool for GenAI pins went live on iOS; Android & Web on OTA.** Collaborating with CQ on new triggering logic (gate later, ≥ grid_index 50; raise unengaged threshold; anchor to high-confidence pins by highest-opt-out L1s); finalized copy/iconography. Global nav button — resourcing approved, experiment ~mid-Sept.

**[On Track] Trust & Safety:** Domain Network Signal v1 — experiment launched last week, three arms at 0.1% / 0.2% / 0.6% of impressions, results expected this week; Spam User Network Signal v1 — September launch confirmed; policy external launch Nov 12, interim changes live; proactive sweeps — interim enforcement began, sweep setup in progress, good evidence of network spam/scam coordination.

### Aug 11, 2026
This week's objective: review progress on workstream definition, highlight key changes/launches, and confirm list of planned projects within each workstream w/ Eng resourcing confirmed and tradeoffs approved. (Timeline as above; no workstream detail pasted.)

---

## C. Screenshots (`09_assets/`)

1. **`devtools_blue_genai_pins.png`** — iOS Dev tools → Overlays → **"Blue GenAI pins"** (on): "Turns eligible GenAI pin reps blue. Reload or scroll the feed to refresh existing pins." This is the "debugging tool for GenAI pins" that went live on iOS per the 8/17 notes — a visual prevalence check for anyone on the app.
2. **`uxr_survey_questions.png`** — the in-app AI-control perception survey (Stephanie Chen), five questions, broad → specific: **Satisfaction** ("How satisfied are you with the amount of AI content you see on Pinterest?") · **Action** ("Have you ever taken any actions in the app to adjust how much AI you see?") · **Effective** ("How effective were the AI adjustments at improving the content you see?" — only asked of action-takers) · **Awareness** ("Before now, did you know Pinterest offers settings to specifically adjust how much AI content you see?") · **Open end** (optional). Research questions: Q1 does satisfaction correlate with taking action / awareness; Q2 are Pinners taking intentional action (likes, hides) *even if they aren't aware of formal tools*; Q3 how do action-takers feel about effectiveness; Q4 even if sentiment doesn't change, will awareness of SMSL flyouts/controls change as a first step.
3. **`uxr_survey_tldr.png`** — **TLDR and caveats (WIP — August data still in progress, numbers will change):**
   - **We have room for improvement on every measure.** Low satisfaction (**49% dsat**), few take action (**21%**), & low awareness (**23%**).
   - **Awareness of AI tools may be a prerequisite for Pinners to act** on their dissatisfaction. Although some Pinners feel they can affect their feed quality based on their engagement (e.g. likes, hides), we don't see evidence that Pinners feel there are actions they can take to affect their AI load. **8% of unaware Pinners said they took any action, vs 72% of aware Pinners.** Aware Pinners who *didn't* take action were mostly neutral to satisfied with AI load.
   - **Negative correlation between Pinners taking action on AI content and satisfaction.** Less satisfied Pinners were more likely to take action. Caveat — causality/direction undetermined, multiple interpretations work here.
   - **Pinners who acted perceived low to neutral effectiveness of their actions.** The effectiveness ratings have fewer extreme negative responses than the general satisfaction ratings. Promising but still room for improvement.

---

## Leo read (2026-08-25)

1. **The GenAI instantiation of the joint framework already exists as a running program — and James is its distribution DRI.** Lily's one-pager *is* the 12-week plan's Distribution workstream, with James + Dafang named on the L1 utility line. GenAI-first (Michael/Andrew, source 08) therefore doesn't ask the joint doc to invent a workplan; it asks it to **absorb this one** as Phase 1 and say what the framework adds on top: calibration as the launch standard (the 8/24 notes say it in their own words — "all opt-out/filter thresholds need to be consistent across experiences"), set-wise density control vs. point-wise demotion, the CQ affinity signal as the personalized penalty, the downstream-density head as the training-time objective, success criteria built from the survey numbers, and the retention instrument.
2. **The one-pager's own history is the argument for the doc's §5.** GenAI v3 as a *direct pinnability feature* → flat; v3 in the user tower via sequence embeddings → offline negative, not launched. A per-pin feature under an unchanged engagement objective has nothing to learn from — exactly the doc's diagnosis. Both Dhruvil's margin loss and the density head are *objective* changes, not feature adds; the doc should record the two failed feature attempts as the reason it prefers them.
3. **The survey reframes what the distribution lane is for.** 77% unaware, 79% never act, and action-takers rate their actions low-to-neutral. Controls and opt-out-gated demotion reach roughly a quarter of Pinners at best; the **default experience is the lever for the 49% dissatisfied** — which makes the CQ GenAI user-affinity signal (Qinglong's "type 2" utility change) the most important input to the utility experiment, and makes "partial opt-out" a smaller step than "low-affinity, never-acted." The low perceived effectiveness of actions is topic 3 (responsiveness) re-entering through the GenAI door: the closed loop after a hide/opt-out isn't visibly closing.
4. **The doc's counter #1 (source 07) is confirmed by the program's own status:** the domain-level signals (GenAI domain, DQv4) are being enforced at **L2 on P2P**, while the pin-level v3 score runs in **L1 utility on HF**. Pin-level → L1 utility/density; domain-level → L2 until L1 gains domain features. That is the fork, already resolved in practice.
5. **§9's four asks, re-read against the program:** (#1) priority call — made, GenAI first; (#3) measurement DS — staffed for GenAI (Stephanie Chen UXR, Wenjun Wang DS), unstaffed for self-harm; (#4) retention holdout — BE/FE program holdouts are set up (Kevin, 8/24) but the **GenAI ablation holdout is delayed and being slimmed** — the doc's instrument lands on a known gap, not a new ask; (#2) NLFU vs responsiveness — untouched, and the survey's "low effectiveness" finding is the first user-facing evidence for it.
6. **DJV asked for "more specific timeframe for distribution launches."** That is James's lane to answer — it is the timelines-are-the-centerpiece demand, now scoped to the work he owns (HF L1 utility → partial opt-out + v3.1 arms; L2 spacing DRI; affinity-in-L1 feasibility; P2P L2 demotion with CQ). Michael's Friday plan needs these dates from James.
7. **Open DRIs the program is waiting on from James's side:** Spacing on Homefeed "(DRI?)" (8/24) = Qinglong's 8/21 "HF to identify an L2 PoC" — still unfilled in the public notes; the L1 affinity-signal path (Dafang feasibility); the funnel/per-CG load analysis (Dhruvil AI 1–3/6/8a).
