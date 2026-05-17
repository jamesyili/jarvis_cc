# Canonical Brief — James Li

> **Foundation context for Ethan Evans Custom-GPT consultations.** Paste this in every parallel chat as the first message before the dimension-specific question.
> Last updated: 2026-05-02

---

## Who I am

**Senior ML Engineering Manager** at Pinterest. **~12 years working career (since July 2014, Yahoo Labs); joined Pinterest September 2024 (~1 yr 9 mos at Pinterest).** Currently **M17 (Sr. EM)** with active **M18 (Director) ambition**. DISC: Di (D:88%, i:88%) — fast, direct, vision-driven, high-energy.

**Career arc:** Yahoo Labs Research Scientist (Jul 2014 – Dec 2015) → Facebook/Meta IC → Senior → Staff → EM (Nov 2015 – Feb 2021) → Snap EM Content Understanding → Head of Stories Ranking (Feb 2021 – Aug 2024) → Pinterest Sr. ML EM (Sept 2024 – present). PhD Statistics, Cornell (2014); BA Economics/Applied Math/Statistics, UC Berkeley (2009). KDD 2025 publication on Pinterest Multi-Embedding Retrieval; KDD 2018 on Facebook News Feed.

I lead the **Homefeed Candidate Generation team** — the core retrieval layer that decides what Pins are eligible to show 500M+ users. ~17 direct reports across six pods: UPP Retrieval, CLR, Retentive Recs, RecGPT, LWS, Funnel Efficiency / Real-Time / PINvestigator. Background: ML org-builder. 0→1 + scale on recsys + retention work. Currently shaping the team into a **two-track org**: Production track (UPP, CLR, LWS, Real-Time) handed to a new EM I'm hiring; Frontier track (RecGPT, Retentive Recs, AI/agentic, cross-functional) stays with me as the Director-shaped portfolio.

### Performance + ratings (recent 12 months)

- **March 2026: Exceeds rating + $1.2M equity grant over 3 years** (up from $450K refresh prior year). Total comp ~$1.35M. Dylan unprompted: *"let's get both of you up there next"* (James + Dhruvil → Director).
- **April 2026: Public exec endorsement.** Andrew (Sr. Director, Product) named me technical lead on Reflex in front of execs; Dylan publicly endorsed. Reflex/Pinkerton EPD demo to ~3,700 (CTO Matt Madrigal forum) on 5/4 with my team's Engineering Agent + Pinkerton as the showcase.
- **Pinterest Engineering Blog post (4/17)** named me publicly as program lead on Retentive Recommendations. Durable forwardable artifact.
- **KDD 2026 paper** — leading the Architecture chapter + Future Work + Prior Work. Team includes Anna (Background), Armando (Representation/Prediction), Yuke (Prediction co-author), Olafur (Federation).
- **Anticipation holdout WAU-positive in UCAN.** Six-month program now metric-moving.
- **Engineering Agent end-to-end** — demoed to Dylan + Andrew (4/29), both impressed; cross-project unblocker for Pinkerton + Reflex + recsys velocity.
- **PINvestigator demoed to Jeff (4/17)** — first VP-level shipped-tool touchpoint.
- **Status with Dylan: peak operational trust.** Quarterly career conversation accepted. April 3 "run things by me" = co-ownership not permission. April 25 Dylan-as-shield arc — she stepped in as POC for UIC/RR to absorb Rajat ad-hoc-ask flow (capital being spent on me).

### Dylan-flagged growth areas (load-bearing, current)

1. **Emotional regulation under pressure ("Maturity Ceiling," Feb 3 2026).** Dylan named: *"Your technical impact is Director-level, but your 'Emotional Tax' is too high. I cannot put you in rooms with VPs if you might explode."* Stakeholders (likely Dhruvil) reported feeling like they're "walking on eggshells." Labeled this a **limiting ceiling to the Director level** and a sign of **lack of maturity**. Behavioral probation. Recovery contract: *Boring Consistency (Low Heat, Steady Light)* replaces my natural mode (*Catalytic Clarity, High Heat, High Light*). Zero defensiveness, zero litigating the point. **Recognized as improving in March Exceeds**, but the underlying pattern is the highest-altitude behavioral edge.
2. **"Be more aggressive and faster in escalating challenges and situations" (March 2026 review feedback) — same shape as the "low-ask" pattern Ethan + Wes both flagged.** Dylan wants more proactive surfacing of issues without the emotional charge of #1. Replacement = structurally-visible operating cadence (1 promo alignment / quarter, 1 system-need / 2-3 weeks, 1 authored narrative / month, 1 sponsor nudge / month).
3. **Humble instinct flagged as Insecure Vibes** — when I land on a "humble" framing for high-altitude artifacts, grounded reviews flag it as self-erasing / over-explanation. Replacement pattern: OAV (Observe, Assert, Validate).

## Current calibration window (May 2 → May 30, 2026)

Pre-OOO window before I'm out **6/1 → 6/30**. My manager Dylan's last day is **6/12**; she's out through ~7/6. Re-entry gap 7/1 → 7/6 has no sponsor coverage.

Major events:
- **5/4** — EPD demo at CTO Matt Madrigal forum (~3,700 audience, full EPD reporting). My team's Engineering Agent + Pinkerton is the showcase.
- **5/7** — **Jeff** (peer VP) Office Hours. AI-leader-path question + Anticipation × UIC × pUIC cross-org thesis.
- **5/8** — **Rajat** (skip VP, 25 min) Office Hours. UPP framing + Pinkerton Engineering Agent + AI-leader-path question.
- **Week of 5/20** — **Dylan career conversation** (Director-trajectory; she accepted as "quarterly regular").
- **6/12** — Dylan's last day. Final sign-offs.
- **6/13** — Dylan OOO begins; Dhruvil-primary cover for my team.

JJ IC16 promo packet — my part done; Dylan's written endorsement still needed before 6/12.

## Strategic thesis (current bet)

**Umbrella thesis: Anticipation Foundations × Retentive Recs as a cross-org capability.** This is Pinterest's bet on shifting from "show users things they're searching for" to "anticipate what they want next and show that instead" — the public Anticipation Vision co-authored by Andrew (Sr. Director, Product), Dylan (my manager), and Mira (Sr. Director, Design), and amplified externally by CTO Matt Madrigal at conferences. My team owns the technical substrate that makes the vision real. Five components sit under the umbrella:

- **Retentive Recommendations (RR) = the engine.** A stateful-user-representation paradigm that replaces session-stateless retrieval with persistent user understanding (UIC, predicted UIC, OmniSage, Geometric Prediction). Six-month program now metric-moving (Anticipation holdout WAU-positive in UCAN, Engineering Blog post 4/17, KDD 2026 paper). For Pinterest, this is the named technical key under the Anticipation Vision — without RR, there is no Anticipation. For Core, RR is the architecture pattern that other surfaces (Notif, Search, P2P) must adopt to stay coherent with HF.
- **Reflex = the accelerator (subordinate to RR per Ethan Q14).** Andrew's framing: *"the industrial revolution for recommendations."* Autonomous diagnostic + simulation agent that generates investigation hypotheses and Trello cards (two cards already in production: CG signal decay, non-English search relevance). Reflex's job is to make RR scale faster across surfaces — not to replace it. For Pinterest, Reflex is how RR's gains compound. For Core, it's the AI-native engineering pattern that proves agentic loops can ship recsys experiments end-to-end.
- **PINvestigator = the eval substrate.** Sensing + diagnosis layer for the recommendation stack — detects funnel issues, surfaces specific experiments to run. Demoed to Jeff (4/17) and Rajat (4/16). It's the v0 that became Pinkerton, and the underlying observability layer that makes both RR and Reflex measurable. For Pinterest, PINvestigator is what lets us detect retention regressions before they show up in WAU. For Core, it's the cross-org diagnostic substrate other teams (Dimitra/Notif, Darren, Francisco, Dafang) are organically forking.
- **Engineering Agent = AI-leveraged leadership exemplar.** The agent that writes and ships recsys experiment code — cross-project unblocker for Pinkerton (auto-fix loop), Reflex (build stage), and CG quota tuning. Demoed to Dylan + Andrew 4/29; both impressed. Anchors the EPD demo (5/4, ~3,700 audience under CTO Matt Madrigal). For Pinterest, it's the velocity multiplier for AI-native engineering across recsys. For Core, it's the proof that "AI-leveraged Director" is a real shape — leadership through agent-amplified leverage, not just headcount.
- **UPP (Universal Pretrained Pinner representation) = retrieval platform pillar.** **Jeff-initiated** (originated as a VP-level platform bet from Jeff at the Core altitude, then operationalized through Rajat's org). Co-equal with Dhruvil's ranking platform (Core ML foundations). My side owns base retrieval architecture, surface expansion (Search/P2P), cross-surface pretraining. Four parallel workstreams (Cross-surface training, Base CLR scale-up, Foundation Model in CLR, P2P co-design). For Pinterest, UPP is the retrieval foundation that lets every surface inherit HF-quality understanding. For Core, it's Jeff's named platform play and Rajat's named top priority — the pillar against which all retrieval work in the org gets evaluated.

Yan-as-partner via **April 3 consensus** (substrate from my team; IB consumption from Yan's team). Daniel/ATG cross-team partnership in motion (pUIC update landed 5/2).

## Stakeholders

- **Dylan Wang — Sr. Director, Homefeed Recommendations.** My direct manager. Owns the entire Homefeed Recommendations org (Ranking + CG + Blending + Frontend). She is my sponsor, my Director-track advocate, and the gatekeeper for promotion calibration. High trust, peak operational, but bounded by the Feb 3 "Maturity Ceiling" feedback (emotional regulation = the behavioral edge). Operating mode: co-own-at-speed (April 3 "run things by me"), not approve-artifacts. **OOO 6/12 → ~7/6** (her last day before extended leave).
- **Rajat Chopra — VP, Engineering (Recommendations / ML Platform).** My skip-level. Dylan reports to him. System architect + org designer; UPP is his named top priority. Distant on details, optimizes for system velocity + entropy reduction + single-threaded ownership. He's already encouraged me twice ("keep pushing," March + April 2026); his mental model of me is ~25% (Pinkerton + UPP context). His sponsorship is downstream of Dylan's case for me — he ratifies what she advocates.
- **Jeff Harrell — VP, Engineering (Core).** Rajat's manager. Skip-level *one above* Rajat; not in my reporting chain. Cross-org sponsor for engineering modernization (AI-native engineering as Core's future). High-I, vibes-driven, prefers demos over decks. Current mental model of me ~0-10% (knows me as "PINvestigator guy in HF"). **More important to me right now than Rajat for Director-track signal** — his sponsorship is the lever that breaks me out of "great EM in Dylan's org" into "operator the broader Core leadership wants in bigger rooms."
- **Andrew Yaroshevsky — Sr. Director, Product (Recommendations).** Anticipation Vision co-author + Reflex sponsor + my co-presenter on the EPD demo (5/4). Andrew is the product visionary; I'm the technical lead he named publicly in front of execs. He pitched the Anticipation Vision to CTO Matt Madrigal, who now talks about it at conferences. Trust topology is high-and-accelerating; he's actively pulling me deeper into Reflex co-development. **The Andrew tension I'm constantly managing: install RR/Anticipation Foundations as my-coded program in VP heads without crowding his anticipation-vision narrative ownership.**
- **Krishna Kamath — Sr. EM, SSJ (Intent Navigation and Platform org, post-reorg 5/1).** Peer-tier EM in Kurchi's org. The cautionary tale: had Kurchi + two SDs + Jeff rapport from quarterly OH and **still didn't promote** ("visibility outside org" feedback). His sequence is the empirical "Kurchi move" — failed calibration → scope rebalance → moved sideways. **Direct relevance to me: Krishna is the proof that trusted-organic-propagation = failure mode at this altitude.** Also being floated as an OAV opener for the Dylan career conversation (intel that Pinterest does eat its own).
- **Matt Madrigal — CTO.** Andrew's sponsor; publicly amplifies the Anticipation Vision at conferences. EPD demo 5/4 (~3,700 audience) lands in his forum. **Potential Platform sponsor post-demo** — if a 60-90s clip + 1-slide + 5-bullet kit gets forwarded into his staff, that's a Sponsor Stack asset I don't currently have. I have no direct relationship with him today.
- **Dhruvil Sanghvi — peer Sr. EM (M17), Homefeed Ranking (under Dylan; under Rajat above).** My closest structural peer — same level (M17), same manager, same VP, same M17→M18 trajectory ("let's get both of you up there next"). Co-pillar dynamic on UPP: he owns ranking + Core ML foundations; I own retrieval + cross-surface pretraining. Dylan's Innovation/Core split (Feb 3) placed me Innovation, Dhruvil Core. **Risk: territorial drift if I'm not actively present in the UPP narrative** — the seam I'm holding is *"Dhruvil owns depth; I own cross-org application + outcomes + scaling mechanism."*
- **Yan Li — peer Sr. EM (M17), P13N-Experiences (under Dylan).** Same-level peer (M17, like Dhruvil and me). Owns Explore/IB surfaces + surface-side glue + routing layer. April 3 consensus: substrate from my team; IB consumption from Yan's team. Active CG ↔ Yan ownership negotiation; the Anticipation Foundations naming layer travels through this seam. Director-track readable as third-party signal — when Yan is aligned with me publicly, Dylan reads it as Director-altitude operating.
- **Roberto Konow — peer Sr. EM, Search (reports to Kurchi, not Dylan).** Structurally adversarial reporting line — Kurchi is the primary political counterweight to Dylan-line at the SD level. Post-reorg expanded scope effective 5/1: now owns Text Search end-to-end + absorbed Query Understanding. Built a Claude-Code-powered funnel debugging tool that Jeff highlighted org-wide; recently expanded into agentic eval tooling — **directly into my PINvestigator/Pinkerton territory.** The Roberto-James competitive dynamic is partly a proxy for Dylan-vs-Kurchi at director level; not mine to fix at the peer layer.
- **Daniel Liu (ATG) — cross-team partner.** ATG = Advanced Technologies Group; partner team for RR/Anticipation alignment (pUIC integration). Daniel's team and mine are co-developing the cross-surface anticipation infrastructure. The pUIC update landed 5/2 (item #4d on my pre-June plan). For Director-track narrative, ATG partnership = proof that I can move work across team lines without my reporting chain having to push it.
- **Mira Steckel — Sr. Director, Design.** Anticipation Vision co-author with Andrew + Dylan — the third leg of the executive triangle. Her involvement is what makes Anticipation a *company-wide* vision and not just an Eng+Product play. Direct working channel activated 4/28 (she initiated with a hand-drawn diagram on UIC mental model); first artifact-spawn moment 4/29 (my reframe entered her vision-pitch toolkit as "delightful jump of anticipation"). **Director-advocate cultivation candidate** — different lane than Andrew/Jeff/Rajat; her advocacy weight is in calibration rooms where Design's view is invoked + in CTO/conference surface area.

## Goals priority order (G0 → G5)

- **G0** — Inner foundation: mental resilience, emotional stability, internal scoreboard, recovery time
- **G1** — Retentive Recs / retention lift (flagship business outcome)
- **G1.5** — UPP Retrieval as co-equal platform pillar (narrative ownership ≠ IC depth)
- **G2** — Agentic AI craft (PINvestigator, Engineering Agent — what genuinely lights me up)
- **G3** — Scale the org through TLs/EMs (less required day-to-day)
- **G4** — Executive presence: brevity, calm, political fluency under pressure
- **G5** — Interview readiness / technical optionality (AI-wave; Track 3 promoted to P1/Tier 1 April 2026)

## Recent coaching landings

- **Control / lack-of-control irony (David, 5/1):** *"I want control AND I want the benefits that lack of control gives me."* Translation: stop reaching for the build lever; lean into narrative + sponsor lever.
- **Both-and Director path:** traditional org-scaling Director path AND AI-leveraged leadership Director path. Not a fork.
- **Frame Flip (Wes Kao, 4/22):** organize career/stakeholder work from "what does the org need?" first, not "what do I want?"
- **Asking ≠ Performing (4/26):** model is Dylan-shaped (co-own-at-speed), not Dhruvil-shaped (over-engineer-the-ask).

## Ethan frameworks I'm already running

- **Q11** — 5-signal early-warning dashboard for sponsor cultivation (unprompted pull / forwarding behavior / language adoption [first signal] / scope offers / sponsor capital spent on me)
- **Q13** — minimum-viable-asking floor: 3 asks for the calibration window (Dylan's written endorsement [draft for her] / 3 warm sponsor intros / one cross-org wedge to pursue post-OOO)
- **Q14** — Reflex subordinate to RR
- **Q15** — OAV (Observe / Assert / Validate); humility ≠ self-erasure

## Constraints / how to work with me

- I'm Di — fast, direct, no preamble. Brevity is a known development edge.
- Tendency to over-explain under pressure; IC-comfort instinct fires when uncertain.
- Willing to take cognitive load — don't pad, give density.
- I read fast. Lead with the answer, then the framework, then the moves.

## Meta-prompt (include in every dimension question, after my main question)

> **After answering my question:**
> 1. Identify the weaknesses or blind spots in your own reply.
> 2. Name 2–3 questions I should be asking on this topic that I'm not.
