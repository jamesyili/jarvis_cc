# Source 06 — Qinglong's Slack update after his 1:1 with Dhruvil (Fri 2026-08-21)

Posted to the working-group Slack after James shipped the joint framework to the WG (Fri 8/21, hitting Michael's Fri-8/21/Mon-8/24 date). Captured verbatim from James, 8/22.

> Sharing some updates after my 1:1 with Dhruvil Deven Badani today:
>
> Where we're aligned:
> We should kick off both the GenAI image spacing experiment and the GenAI L2 domain demotion experiment. All funnel interventions are necessary, but we should do as much as possible at the upper funnel to minimize triggering L2 reranking — this is similar to our current filtering setup where we have indexing, unity and NGAPI level filtering integrations and all of them are necessary to ensure both funnel efficiency and filtration effectiveness.
>
> Additional ideas Dhruvil raised (to address the load concern):
> Adding a marginal loss at L1 to penalize positive engagement with low-quality content — a new approach that Notif is exploring at their L1 level. Adding controllable distribution for borderline content at L1 (technical feasibility requires more discussions with Dafang)
>
> So there will be two action items for next week:
> We need HF to identify an L2 PoC to work with CQ on setting up the two experiments above. We should also set up a separate technical discussion on all the new ideas shared by James and Dhruvil, and form short-term and long-term plans for quality-aware ranking. I think James's doc is a very good starting point and I will add Dhruvil's ideas to the doc and tag relevant folks to discuss more about technical feasibility of each option and pro/cons.
>
> Thanks everyone for the discussion and have a good weekend!

## Why this source matters (Leo read, 8/22)

1. **"James's doc is a very good starting point… I will add Dhruvil's ideas to the doc"** — the doc is now the org's planning surface for **quality-aware ranking** (his phrase; a named program is forming around James's artifact). The 8/19 "expands my original doc" parent-document story is countered by Qinglong's own public words.
2. **L1 is fully back in the plan** — both of Dhruvil's ideas are L1 interventions, folded under the full-funnel/upper-funnel-first frame the joint doc argued. The 8/14 "CQ's preference is L2" turf line is gone from the public record.
3. **Dhruvil's L1 marginal-loss idea = the exact mechanism gap the 8/21 Neeti T&S investigation exposed** (positive engagement with low-quality content generalizes; negatives don't; positives on later-reported pins never scrubbed). The T&S lane and the CQ lane are converging on the same fix — the concrete substance of James's CQ-coordination POC pitch to Dylan.
4. **Open action item with staffing implications: "HF to identify an L2 PoC to work with CQ"** — L2 ranking is Dhruvil's pillar; coordinate the pick with him rather than claiming it. Watch whether this lands as a T2-board line.
