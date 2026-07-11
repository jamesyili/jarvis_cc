# H1 2026 Self-Review — DRAFT v2 (2026-07-10) for James to edit

> **v2 changes (2026-07-10, per James):** shipped-impact numbers stripped by design — no ratings this cycle, nobody reads the metrics; narrative structure kept. Accomplishment #2 rebuilt: RR-to-working-mechanism + Anticipation Cupcake to final deliverable, with RR-as-backbone and cross-functional (Yan's team, product partners) bullets. Accomplishment #1 expanded: performance management, Ryan + Ray hires, Sophia + David departures as churn context alongside Bowen. All `[brackets]` resolved or removed.
>
> Deliberately excluded: reorg/charter language (Dylan's plans, unannounced), Michael close (marked confidential 6/3), Bella retention specifics (ER case closed quietly), Yuke's search, promo-budget color. All of it either leaks someone's confidence or invites questions you don't want in writing.

---

## Q1 — Key accomplishments and impact

In H1 2026, I led HF Candidate Generation through a major leadership transition without losing delivery momentum, converted Retentive Recommendations from strategy into a working retention mechanism while driving the Anticipation Cupcake workstream to its final deliverable, and helped establish Pinterest's agentic-AI foundations (Reflex, Pinkerton, PINvestigator) as programs with cross-org adoption and executive visibility.

**Kept the organization strong through transition, and made it more durable**

- The team absorbed real churn this half: Bowen departed in March, and Sophia and David also left the team. I managed through all three transitions cleanly — coverage plans in place within days, TL ownership lanes re-clarified, and no slip on in-flight commitments.
- I rebuilt the bench on both ends. I ran a rigorous EM backfill search (ten candidates evaluated against explicit seat criteria) and closed a strong hire, Alim Virani, who starts mid-July with an onboarding plan already prepared. I also hired two new engineers, Ryan and Ray, and set them up for success with scoped starter projects, clear ownership lanes, and coverage responsibilities in previously single-expert areas.
- I held the performance bar through the transition: I conducted active performance management where delivery fell below level expectations, with direct feedback and clear written expectations, so standards stayed consistent even while the org was in flux.
- The durability test came in June: I was fully offline for 3.5 weeks, and the team's delivery, on-call, and cross-org threads ran without me. That autonomy is the direct result of deliberate investment in the TL bench — area ownership, decision docs, and review-gate (rather than integration-point) operating mode.
- I prepared a strong IC16 promotion case with JJ for the July cycle (submitted), coaching him to build the evidence base himself as a leadership exercise; his pod-lead role and delegated ownership of PINvestigator and the funnel-efficiency space are the foundation of the case.

**Converted Retentive Recommendations from strategy into a working retention mechanism, and drove Anticipation Cupcake to its final deliverable**

- Retentive Recommendations is the technical backbone of the Anticipation vision for 2026 personalization, and my team owns that substrate. H1 is the half it became real: the feedback loop shipped on the CG funnel and validated the core RR hypothesis in production — the mechanism we spent 2025 building the foundation for is now live and measurable.
- pUIC shipped as a dual track: heuristic pUIC live, with model-based and LLM-based variants coming online through late H1 and the visual-signature work feeding the LLM track.
- I drove the Anticipation Cupcake workstream through to its final deliverable, working cross-functionally with Yan's and Tim's teams and with product and design partners across EPD. The workstream moved at unusual speed with executive visibility throughout, and my team's CG work carried the backend wins that made the launch real.
- When that speed produced predictable cross-team friction, I initiated and co-authored the three-EM lookback and look-forward with Yan and Tim, so the leads presented a united front and the collaboration practices carried into the next phase of Anticipation work.
- I led the public technical narrative: the Pinterest Engineering Blog post on Retentive Recs shipped in April with me as program lead, and our KDD 2026 paper (full draft complete, submission July 31) captures the architecture with my chapters on Prior Work, Architecture, and Future Work.

**Advanced company-wide AI and platform priorities beyond my team's scope**

- UPP retrieval: the must-win Notifications launch landed in Q1 with follow-on launches compounding it across surfaces. I also resolved a cross-team pretraining collision (UPP × P2P) EM-to-EM without escalation, establishing a heads-up protocol both orgs now use, and keeping UPP v0 shipping in its original form.
- Reflex: as co-architect with Product (Andrew's org), I helped shape the program into four staffed workstreams with a dedicated TL and PM. It reached EPD-wide demo audience and a product review with Bill that landed well — the Detect/Simulate architecture and the expert-judgment capture design are pieces I authored.
- Pinkerton shipped M0 to production in April and grew into a joint cross-surface DSAT diagnostic with Notifications (Dimitra) and HF, demoed to Jeff. PINvestigator moved from my prototype to org tooling: eval harness and golden set landed, adoption telemetry in place, and it's now the default tool engineers across HF reach for on metric investigations — including our senior director on live cases.
- Net effect: my team's tools and platforms are now load-bearing for other orgs' goals (Notifications ML, Growth surfaces, EPD's agentic initiative), not just Homefeed's.

## Q2 — Key learnings and missed opportunities

**Learning #1: with newer partners, my directness needs an explicit intent layer.** With long-standing partners, my speed and directness read as clarity; with newer PM partners who haven't built context with me yet, the same register can land as pressure and cost trust I then have to rebuild. I got direct feedback on this in April and acted on it immediately — repaired the two relationships and changed the default: lay out intent before the push ("my goal is to unblock X, so I'm pushing on Y — thoughts?"), and invest in relationship-building before the first hard conversation, not after. Going forward I'm treating "intent labeling" as a standing part of how I open ambiguous or high-pressure threads with anyone new.

**Learning #2: the 2025 shift from solver to mechanism-builder held up under a real test — now it needs to become structural, including my own pace.** Last year I named the integration-bottleneck pattern; H1 field-tested the fix. The June OOO proved the org runs without me, and the launches that shipped while I was out were owned end-to-end by TLs. The remaining edge is making that the default rather than the exception: I still absorb too many cross-org threads personally when stakes are high, and I've learned that operating pace is an org-design input, not a personal virtue — an org calibrated to my maximum intensity isn't durable. Going forward: the new EM owns one full pillar end-to-end from ramp, I hold a small number of review gates rather than seats in every thread, and I'm explicitly designing H2 workstreams so the bar holds without my constant push.

## Q3 — Goals for H2 2026

Lead team on the following:

- **Complete the team structure evolution:** ramp Alim to full ownership of his pillar, land coherent charters and swim lanes across Retentive Recs and Generative Retrieval, and deepen succession (TL bench, pod leads) so every major workstream has a named owner other than me.
- **Prove retention impact:** ship the pUIC dual-track to conclusive readouts, land the retention measurement, and expand the feedback loop to the broader CG funnel; submit the KDD 2026 paper.
- **Protect and extend UPP retrieval wins:** land the P2P adoption, present the cross-surface pretraining decision cleanly with options, and continue surface expansion without diluting the landed launches.
- **Scale Reflex from reviews to measurable outcomes:** SSv2 and iteration-velocity wins on the roadmap, Pinkerton federation into cross-surface adoption, and the expert-judgment capture loop producing compounding training signal.
- **Advance Anticipation foundations with ATG:** keep the UIC/pUIC substrate jointly owned and measurement-honest as it becomes the base for anticipation surfaces.

Personal improvement areas (2):

- **Intent-labeled communication with newer partners:** open high-stakes threads with intent before content; pre-wire in small forums; keep the April fix a habit, measured by zero repeat feedback of that shape in H2.
- **Durable scaling over personal intensity:** EMs/TLs own end-to-end execution and narrative artifacts; I operate at review gates and strategy altitude; workstream design assumes sustainable pace as a constraint, not a variable.
