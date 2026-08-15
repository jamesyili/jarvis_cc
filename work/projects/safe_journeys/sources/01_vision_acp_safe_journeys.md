# [ACP] Safe Journeys — "discovery should inspire, never endanger"

> **Source of record.** Extracted verbatim from the PDF James uploaded 2026-08-14 (`0de9a14a-...Safe20Journeys...vision.pdf`, 5 pages).
> **Authors:** Michael Weissinger · Faisal Farooq · Dylan Wang · Andrew Yaroshevsky
> **Doc type:** the first-principles / strategy doc. Subtitle: *A strategy to make Pinterest safe by design.*
> **CTO comments captured 2026-08-14 from a screenshot James supplied — see "CTO comment thread" section at the bottom. They did not export to PDF.**

**Framing note (verbatim):** "This is a Core strategy for determining when borderline content is safe to distribute – and when it is not. We start with the clearest proof point: eliminating self-harm spirals in teen discovery. The blueprint will extend to racy, gross, weapons, substances and future sensitive categories across Pinterest."

---

## Opening

Pinterest exists to help people imagine and create a life they love. That promise is bigger than any one Pin or policy decision: discovery should leave every Pinner more inspired, more capable, and more in control than when they arrived. For teens especially, Pinterest must be a place that expands possibility – never one that turns a vulnerable moment into a darker destination.

Today, we can miss that bar even when Pin-level safety numbers look good. **An ambiguous rope pin may be permissible alone. Place it beside depressive quotes and other harm-adjacent Pins, and its meaning changes: the slate is clearly unsafe.** Yet we inspect Pins and learn from engagement one action at a time. A pause, close-up, or repin can be read as intent; similarity systems reward it; the next slate gets darker.

- *Figure 1.* An individual pin describing how to tie a knot. Safe? **Yes.**
- *Figure 2.* The exact same pin in a slate of pins which are also deemed individually safe and non-violative. Safe? **No.**

"This is a **discovery-design gap, not just a filtering gap**. Filtering remains essential for violative content, but it cannot see every harmful association or prevent permissible content from becoming harmful in aggregate. Our goal is simple: **no Pinner should be able to learn their way into harm on Pinterest.**"

Five pillars: (1) better measurement of what pinners see (slate-level evaluation), (2) leveraging the entirety of the information from content quality signals rather than simply a threshold, (3) proactively identifying negative spirals, (4) creating a safer cold start experience, (5) launching wellbeing features that make our leadership visible.

---

## 1. Unsafe Slates — make the real problem measurable

"You get what you measure." Current self-harm prevalence ≈ **0.03%** because it asks only: *is this Pin violative?* Right for enforcement, blind to the experience. An LLM can judge the rope Pin safe alone; show it the full slate and it judges what the Pinner actually sees.

**Unsafe Slate Rate (USR)** = north-star metric for Safe Journeys: the share of recommendation slates unsafe for the Pinner and their context. The rater considers the pin *in the context of the entire slate*. "This raises the prevalence numbers orders of magnitude and turns an invisible problem into an optimization target."

Cited precedent: **Google Research SlateQ** (slate as a joint action, not a bag of independent items); more recent **slate-aware ranking** moving that reasoning upstream into ranking rather than leaving it to a final filter.

### Table 1 — the same experience, measured two ways via LLM (directional, pending verification)

| What we measure | What the data shows |
|---|---|
| % of all pinner pin impressions exceeding the self-harm threshold | **0.03%** |
| % of **teen** pin impressions exceeding the self-harm threshold | **0.0015%** |
| % of teen **slates** the LLM judge called unsafe (same guidelines!) = USR | **0.45%** — **300× higher** |
| **Spiraling:** after a teen taps just **1** unsafe slate, their USR rises | **7×** (0.45% → **3.2%**) |
| **Teen-level impact (user reach):** teens seeing ≥1 unsafe slate | **297K teens (2.3%)** |

*Source: one full day of organic feed impressions (dt = 2026-08-02); 5K LLM-judged session samples for "unsafe" slates; 2K LLM-judged teen active days for spiraling and teen-level impact. Pin "violative" = self-harm model score ≥ 0.193 (decision = 2). Slate "unsafe" = LLM judge (**gpt-5, rubric `self_harm_enforcement_v1`**) rated the slate UNSAFE, reweighted to the teen slate population via stratified sampling. **LLM judge results not human calibrated.***

"The data tells a clear story: most unsafe experiences are not a single enforcement miss. They are harmful combinations that our previous measurement could not see. Unsafe Slate Rate gives us a clear mandate: **drive it down, even with localized SSv2 cost. This is the engagement we do not need on Pinterest.**"

## 2. Safety-first Ranking — make safety a signal, not a gate

Today safety is largely a binary gate at the end of the funnel: a Pin above threshold is removed; everything below is treated as equally eligible. "Too coarse for borderline content and blind to the slate."

"We will give ranking a **continuous safety objective**. Models will use the full spectrum of policy and quality signals to prefer safer content and disfavor rising risk – even when a Pin is permissible alone. **They will learn against Unsafe Slate Rate, not only Pin-level labels**, finding the relevance and safety trade-off without manual rules for every cohort and surface."

Cited: **Meta — "Harm Mitigation in Recommender Systems under User Preference Dynamics"** (jointly optimizes CTR and harm mitigation while modeling how today's recommendations shape tomorrow's preference) — named as "perhaps the closest technical analogue." Plus the broader multi-objective recommender literature.

"Working backwards from the metric improves the stack: **ranking** can penalize slate risk; **retrieval** can stop sourcing unsafe combinations; **engagement hygiene** can keep ambiguous actions from training Pin2Pin and embeddings as strong positive preference; and **blending** can enforce spacing and diversity. Pin-level prevalence could not show whether those levers worked. Unsafe Slate Rate will."

## 3. In-session Awareness — catch a spiral before it becomes a destination

"A low average can hide an unacceptable tail." If a thousand teens each see 0.45% unsafe slates on average, but one teen spends an entire session in unsafe slates, the average does not make that experience acceptable.

Build a **journey risk signal** across Homefeed, Related Pins, Search, and Notifications. Tracks: risk concentration, sensitive-topic density, acceleration, cross-surface loops. V1 = transparent rules (repeated unsafe slates, rising density, sensitive topic reappearing across surfaces). Over time, a sequence model recognizes spirals earlier.

When risk rises: increase safety weight in ranking, enforce stronger spacing/diversity, stop reintroducing the pattern on another surface, re-seed from positive interests. For sustained sensitive intent, offer respectful paths toward safer, supportive content. "The experience should **restore agency, not punish curiosity**."

"Safety-first ranking lifts every feed. In-session awareness protects the Pinner for whom the average is not enough."

## 4. Safe Cold Start — do not mistake uncertainty for intent

"New teens are our highest-risk cohort because the system has almost no reliable history. It is guessing, and the first ambiguous interactions can set an outsized direction. **We should not grant those signals trust they have not earned.**"

Begin with a high-confidence, age-appropriate discovery state: broad enough to feel alive, deliberately safer than the open corpus. Declared interests and proven-positive content weigh more than fleeting implicit engagement. Early interactions with borderline content get **discounted from ranking, Pin2Pin, embeddings, and candidate generation**. Personalization expands as the system earns confidence.

"This is not a sanitized Pinterest or a permanent walled garden. It is a deliberate first mile."

## 5. Wellbeing Hero Features — make our leadership visible

Wellbeing + Marketing lead four teen hero features:
- **Stop or Limit Infinite Scroll** — intentional stopping points
- **Take a Break Reminder** — periodic compassionate prompts
- **Limit Notification Volume for Teens**
- **Scale School Focus Modal**

"Pinterest should respect a teen's time and attention, not compete for every spare moment."

---

## Close

"Unsafe Slates makes the problem visible. Safety-first Ranking changes what the system learns and serves. In-session Awareness protects the Pinner when risk concentrates. Safe Cold Start prevents fragile first steps from becoming risky. Wellbeing Hero Features make our stance on teen safety unmistakable.

Safe Journeys raises the floor: no Pinner should be able to learn their way into harm. But safety is the foundation, not the full ambition. **Perceived Relevance raises the ceiling**: it improves discovery for every Pinner, including teens, by optimizing for what feels right to them in the moment."

---

## CTO comment thread (captured from screenshot, 2026-08-14)

All comments dated **Aug 12, 2026**. Margin comments on §3 *In-session Awareness*. Two highlights visible in the body: the §3 subtitle *"catch a spiral before it becomes a destination"*, and the sentence *"track risk concentration, sensitive-topic density, acceleration, and cross-surface loops."*

| Time | Author | Comment |
|---|---|---|
| **10:19 AM** | **Matt Madrigal (He/Him) — CTO** | **"Let's tie this back to Anticipation as well."** *(anchored on the §3 In-session Awareness header)* |
| **10:13 AM** | **Matt Madrigal (He/Him) — CTO** | **"Homefeed only or all surfaces (RP, Search)?"** *(anchored on the journey-risk-signal sentence)* |
| **10:16 AM** | Michael Weissinger *(reply)* | **"All surfaces – for context ~50% of unsafe slates sampled were from RP, ~25% home feed, ~24% board ideas."** + Google Doc link (`docs.google.com/document/d/11E4SKk-00KvNv6TqnodH-rmy9GzbdPwOk_X4Nq-209M`, bookmark `id.czkh989m17rd`). One 👍 reaction. A second 👍 sits on the 10:19 comment. |

### Why these two comments matter (Leo read, 2026-08-14)

**1. "Tie this back to Anticipation" is a CTO instruction pointing into James's own territory — and it landed on the pillar James is an eng POC on.**
Anticipation = the vision co-authored by Andrew Yaroshevsky + Dylan Wang + Mira, pitched to Madrigal by Andrew, and amplified by Madrigal externally at a conference as one of the things he is most excited about for personalization/ML at Pinterest (`work/projects/reflex/pinkerton/pinkerton.md`, `retentive_recs.md` §Anticipation Vision). **James's team owns the technical substrate** — "Anticipation Foundations" is his Director-shaped scope claim (RR engine + Reflex eval + CLR backbone; `work/communication.md`). Madrigal has *already* engaged on the UPP×intent interplay at ELT level: *"how can we leverage user intent clusters as part of UPP — what's the interplay between user intent modeling and UPP?"* (`work/projects/upp/upp_retrieval_em.md`).
Note also: **Andrew and Dylan are co-authors of BOTH the Anticipation Vision and this Safe Journeys doc.**
The technical substance behind the instruction is real, not just narrative: **in-session awareness and anticipation are the same machinery pointed at different objectives.** Anticipation predicts the user's next want; spiral detection predicts the user's next harm. Same user-state representation, same sequence model, same cross-surface trajectory object.

**2. The surface breakdown contradicts the "start with Homefeed" scoping.**
Faisal's Teen-Aware doc says *"starting with Homefeed."* Michael's own data says Homefeed is **~25%** of unsafe slates — **Related Pins is ~50%, board ideas ~24%.** Consequences:
- Homefeed-first optimizes the smaller half. **RP is 2× Homefeed.**
- The whole L1-vs-L2 argument in Qinglong's doc (`04_`) is Homefeed/blender-centric. On **RP/P2P — the biggest surface — CQ already has a proven L2 demotion launch** (LQS Rate V2 −0.87%), so James's L1 is not the lever there at all.
- **A problem split ~50/25/24 across three surfaces cannot be fixed surface-by-surface at L2.** The only lever that touches all surfaces at once is the **shared pretrain backbone (CFM/UPP)** — which is James's. That is Qinglong's own Phase 2, currently gated behind a CQ-run Phase 1 on notif/search. The CTO's "all surfaces?" question plus Michael's own numbers are the argument for **pulling Phase 2 forward**.
- **"Board ideas" (~24%) has no owner anywhere in the milestones doc** (`03_`).
