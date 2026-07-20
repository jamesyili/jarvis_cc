# Key Outcomes

## Charter

The organization runs three subcharters. All three inherit the same topline metric goals: **SSv2, WAU, and Cost Savings.**

| Subcharter | Scope |
|---|---|
| **Anticipation & Exploration** | pUIC (model based and LLM based), Retentive Recs, Unified Explore Backend |
| **Retrieval Modeling** | Intelligent Boards, Recommended Boards, LWS (lightweight scoring) |
| **UPP & Reflex** | UPP, the shared retrieval framework the modeling charters build on; Reflex and agentic dev velocity systems; Foundations & Efficiency (responsiveness, L1 utility, cost) |

CLR converges to one of the first two subcharters at the settle point, sized by where headcount lands under this design.

**0-to-1 initiatives.** Two incubations run with named owners and explicit graduation or sunset criteria: Generative Retrieval (RecGPT) and LLM based pUIC. Incubations graduate to a durable home or sunset; they do not drift.

**Flexibility.** The design holds capacity for new initiatives: two unallocated requisitions (L15, L13), plus the incubation model itself, which frees capacity as each bet graduates or sunsets.

---

# Technological Investments

Today, anticipation, retentive recs, and boards advance on parallel, often near duplicate foundations. One organization converges four investments:

- **A single personalization backbone.** pUIC, Retentive Recs, and Intelligent Boards depend on the same user representation and retrieval substrate. UPP becomes the shared framework CLR and LWS build on: the substrate is built once, owned centrally, and consumed by the modeling charters.
- **One LLM serving investment.** LLM based pUIC, Generative Retrieval (RecGPT), and board applications (Recsplanations, board titles) lean on the same LLM inference and serving infrastructure. Consolidated, that is one investment and one accumulating set of operational lessons instead of three.
- **AI dev velocity as shared platform.** Reflex productizes AI leveraged engineering (Pinvestigator, Pinkerton) as internal tooling that every subcharter adopts.
- **Shared modeling across boards and retrieval.** Board recommendation modeling and retrieval modeling are close disciplines; the Retrieval Modeling subcharter colocates them so techniques and infrastructure transfer directly instead of crossing a team seam.
