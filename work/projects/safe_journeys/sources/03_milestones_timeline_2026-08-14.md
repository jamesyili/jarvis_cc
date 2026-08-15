# Safe Journeys — Milestones & Timeline

> **Source of record.** Pasted verbatim by James 2026-08-14. **Last Updated: Aug 14, 2026** (i.e. today). This is **the execution doc Michael Weissinger is asking James for opinion + ETAs on.** Every "Milestones / Timelines" field is **TBD** — the ask is to fill them.

## Summary

"We have developed and got cross-functional alignment on a vision for 'Safe Journeys' on Pinterest — where our goal is for **no Pinner to be able to learn their way into harm on Pinterest**. Building off the momentum and success of the **AI Teen Pod**, Content Quality, and Trust & Safety investments we are moving forward with a focus on **reducing self-harm on the platform as measured by Unsafe Slate Rate** — a new metric we'll be defining to evaluate the experience across the app. The blueprint we develop for Safe Journeys will extend to racy, gross, weapons, substances and future sensitive categories across Pinterest."

Achieved through: (1) better measurement of what pinners see (slate-level evaluation), (2) leveraging the entirety of the information from content quality signals rather than simply a threshold, (3) proactively identifying negative spirals, (4) creating a safer cold start experience, (5) launching wellbeing features that make our leadership in this space visible.

---

## Workstream 1 — Measurement

Define and productionize **'Unsafe Slate Rate' (USR)**, "which for now is only in proof of concept form."

**POCs:** DS: **TBD** · Policy: Niki Kakarla, Stanley Washington (He/Him) · Product: Michael Weissinger

**Open issues / questions:**
- **Need a DS POC to drive the development of the metric.**
- Need to formalize and establish a timeline for: (a) human-centered prevalence assessment, (b) working with policy on the definition of slate-level self-harm assessments, (c) building a human-labeled dataset, (d) training the LLM.
- Align on what success is **until USR is available**. Initial proposal: draft off what the **Teen AI pod** developed for **racy** content success criteria.
- **Can we create and maintain a holdout using this new metric?**

**Milestones / Timelines:** TBD

**Resources:** Unsafe Slate Measurement Results - Self Harm Proof of Concept · VSC Next steps · [ACP] Volume sensitive content (VSC)

## Workstream 2 — Safety First Ranking: "Making Safety a Signal, not a gate"

**POCs:** Eng: **James Li**, Qinglong Zeng, Dhruvil Deven Badani, Zisis Petrou · Product: Michael Weissinger

**Open issues / questions:**
- **Need to work on a tech design that is scalable across surfaces and parts of the stack, and surface the tradeoffs.**
- How can we quickly apply the learnings from the **AI Teen Pod** to self-harm?

**Milestones / Timelines:** TBD

**Resources:** Search Quality Utility Unification One-Pager · **Integrating Quality/Safety Objectives into the Recommendation System — Design Options** (= Qinglong's doc, filed as `04_`) · Unified Spacing Experiment Design

## Workstream 3 — In-Session Awareness: "catch a spiral before it becomes a destination"

**POCs:** Eng: **James Li**, Qinglong Zeng, Dhruvil Deven Badani, Zisis Petrou · Product: Michael Weissinger, Chip Boyd

**Open issues / questions:**
- Should we leverage the **user-level self-harm seeker work**? If so, how? Or should we scope phase 1 to addressing **in-session spirals only**?
- How can we quickly apply the learnings from the AI Teen Pod to self-harm?
- **Should we keep any UX interventions out of scope?**

**Milestones / Timelines:** TBD

**Resources:** [ACP] Self Harm Seekers - PRD - 2026 · Self Harm Users Analysis H2 2026

## Workstream 4 — Safe Cold Start: "do not mistake uncertainty for intent"

**POCs:** Eng: **TBD** · Product: Michael Weissinger, Sari Wang (?)

**Open issues / questions:**
- Are we scoping this to only Content Quality and Ranking changes?
- If so, **what is the progress on defining a 'high quality' content corpus? Who (if anyone) is working on this?**

**Milestones / Timelines:** TBD · **Resources:** TBD

## Workstream 5 — Wellbeing Features: "make our leadership visible"

**POCs:** Eng: **Tim Leung** · Product: Michael Weissinger, Matthew Chester · Design: TBD (Michael chatting with Stephanie Ojo and Hannah Pearce about support)

**Open issues / questions:**
- Scoped to one feature, **'Mindless' scrolling interventions**. Need to discuss in the PRD whether this pertains to just Homefeed (perhaps to start) then scales to other surfaces.
- Need to identify who can support from design.

**Milestones / Timelines:** TBD

**Resources:** [Wellbeing] Mindless Scroll - Feature Reqs · T&S Interventions Framework · Interventions Framework

---

## Overall Open Questions

- **Should we structure this into a 12-week plan** (which seems to be the standard approach for projects like this)?
- **We need to establish what we're willing to trade off — both in terms of project priorities AND engagement.**

## Reference Documents

[ACP] Safe Journeys – vision · Safe Journeys – vision 1-pager · Safe Journeys Meeting Notes · Preventing Self-Harm Spirals for Teens: State Of The Union · [Wellbeing] Mindless Scroll - Feature Reqs · Borderline Content Update - Summary of H1 2026 · Measuring Success: Teen-Aware Pinterest Experience (AI Pod) · Search Quality Utility Unification One-Pager
