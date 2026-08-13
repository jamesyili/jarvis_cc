<!-- Source: https://medium.com/superagentic-ai/gepa-omni-in-superqode-three-optimizers-compete-on-a-coding-harnesses-98f9515ec5d4 · pasted verbatim by James 2026-08-12 (WebFetch was refused on Medium). Author: Shashi Jagtap, Superagentic AI, published 2026-07-26, 10 min read. Medium UI chrome trimmed; article body unedited. -->

# GEPA Omni in SuperQode: Three Optimizers Compete on a Coding Harnesses

**Shashi Jagtap · Superagentic AI · Jul 26, 2026 · 10 min read**
*Tags: Harness Engineering, Agentic AI*

The team behind GEPA has just released the Omni to make agent optimisation unified. SuperQode, our agent engineering platform for coding factories has already integrated this and experienced with tit for harness optimization. GEPA has been game changing so far but it was only limited to the text based optimization as agent evolves it need more optimisation than this text agent involved tools, memories, and other factors that needs optimisation at different level. Optimising a coding agent involves more than refining an individual prompt. The behaviour of an agent is determined by a broader harness: prompts, tools, model routing, workflow rules, execution checks, approval requirements, sandbox constraints, and evaluation policy. Improving that system requires an optimisation process that can modify useful surfaces without weakening the controls that make the agent safe and predictable.

This article documents an experimental integration between GEPA Omni and SuperQode. The objective was to determine whether three distinct optimisation engines could evaluate and improve the same complete SuperQode HarnessSpec while operating within a shared contract and a deliberately small budget. The experiment was not designed as a broad benchmark. It was a constrained systems validation intended to answer a narrower question: can a multi-engine optimiser propose a measurable harness improvement while SuperQode retains control of validation, permissions, evaluation, and adoption?

The complete configuration, task design, component versions, audit outputs, and recorded results are available in the SuperQode GEPA Omni integration record.

## Why GEPA Omni Changes the Optimisation Model

The GEPA optimize_anything interface is based on a general contract: an artefact is represented as text, an evaluator measures candidate quality, and an optimisation engine proposes revisions. The Omni release extends this model by making the optimisation engine pluggable and the optimisation workflow composable.

A single task and evaluator can now be dispatched to multiple engines through the same interface:

- GEPA applies reflective mutation, using model-generated analysis and evaluation feedback to revise a selected candidate.
- AutoResearch delegates more of the optimisation loop to an autonomous coding agent, including candidate selection, proposal, and evaluation decisions.
- Meta-Harness keeps the outer optimisation loop under framework control while using an agent to propose bounded candidate mutations.

These engines implement different search behaviours. That distinction matters because no optimisation strategy is consistently strongest across every task. In the GEPA Omni announcement, controlled Frontier-CS experiments showed that the best standalone optimiser varied by problem. The same work also demonstrated that an optimiser may plateau even when a fresh optimiser, seeded from its best candidate, can continue making progress.

Omni converts those observations into a two-stage meta-optimisation strategy. The first stage runs several engines against the same task and retains the highest-scoring result. The second stage starts a fresh optimiser from that candidate and uses the remaining budget to continue the search.

Conceptually, the composition is equivalent to the following:

```python
from gepa.optimize_anything import (
    OptimizeAnythingConfig,
    optimize_anything,
    optimize_best_of,
)
exploration = optimize_best_of(
    seed_candidate,
    evaluator=evaluate_candidate,
    objective=objective,
    configs=[
        OptimizeAnythingConfig(engine="gepa", max_token_cost=exploration_budget),
        OptimizeAnythingConfig(
            engine="autoresearch",
            max_token_cost=exploration_budget,
        ),
        OptimizeAnythingConfig(
            engine="meta_harness",
            max_token_cost=exploration_budget,
        ),
    ],
)
result = optimize_anything(
    exploration.best_candidate,
    evaluator=evaluate_candidate,
    objective=objective,
    config=OptimizeAnythingConfig(
        engine="gepa",
        max_token_cost=continuation_budget,
    ),
)
```

The SuperQode integration applies this pattern to a complete harness rather than to an isolated instruction or source file.

## Representing a SuperQode Harness as an Optimisable Artefact

A SuperQode HarnessSpec is a YAML document that defines the operational environment around a coding agent. Depending on the configuration, it can include:

- agent roles and system prompts;
- permitted tools and tool policies;
- model and provider routing;
- workflow stages and transitions;
- execution checks and release gates;
- approval requirements;
- sandbox and filesystem constraints;
- evaluation tasks and optimisation policy.

Because the resolved harness can be represented as text, it is compatible with optimize_anything. However, textual compatibility alone is not sufficient. A harness optimiser must not be allowed to increase its score by deleting checks, widening permissions, disabling approvals, or weakening the evaluation contract.

The integration therefore places a guarded SuperQode evaluator between the Omni engines and the underlying harness execution system. Every proposed candidate must pass structural and policy validation before it is eligible for a non-zero score.

The evaluation sequence is:

1. Resolve and stage a copy of the baseline HarnessSpec.
2. Provide optimiser-visible tasks and diagnostic feedback.
3. Parse each proposed candidate as a valid SuperQode harness.
4. Compare the candidate with the baseline optimisation policy.
5. Reject invalid, out-of-scope, permission-widening, or check-weakening changes.
6. Execute valid candidates through the standard SuperQode harness evaluator.
7. Evaluate the selected candidate against sealed held-out cases.
8. Write the result to a staging directory without modifying the live harness.

A rejected candidate receives a score of zero. Valid candidates receive both a score and structured diagnostic information. This diagnostic payload includes policy findings, task failures, execution usage, duration, non-regression status, cost efficiency, and latency efficiency.

In GEPA terminology, this metadata is Actionable Side Information. It gives the optimiser evidence about why a candidate succeeded or failed, allowing subsequent proposals to be based on execution feedback rather than blind YAML mutation.

## Experiment Configuration

The experiment was bounded. Its purpose was to validate the integration path, not to maximise benchmark performance. Harness rollouts were executed locally through Ollama using qwen3.5:9b. GEPA reflection used the same local model. AutoResearch and Meta-Harness used Claude Haiku through an existing authenticated Claude Code subscription session. No Anthropic API key was used. The runner removes ANTHROPIC_API_KEY and ANTHROPIC_AUTH_TOKEN from the child process so that Claude Code uses the existing subscription authentication context instead of API credentials.

The full experiment was launched with script within SuperQode repo

```bash
scripts/run_tiny_omni_experiment.sh \
  --spec examples/harnesses/omni-tiny-local.yaml \
  --mode omni
```

The tracked experiment script performs several reproducibility and safety checks before any model call. It pins the GEPA source revision used by the experiment, validates Claude Code and Ollama authentication, confirms that the selected local model is installed, prints the resolved command, and requests explicit confirmation before execution. The optimiser budget was configured as follows:

- Total optimiser evaluations: 24
- Evaluations per exploration engine: 6
- Continuation evaluations: 6
- Total proposer ceiling: $2.00 API-price-equivalent
- Candidate workers per engine: 1

The evaluation contract contained three optimiser-visible release-decision cases and two sealed held-out cases. The tasks tested positive and negative release decisions, output-format compliance, failed checks, security concerns, migration requirements, and rollback readiness. This separation between visible and held-out tasks is important. The visible set provides feedback during optimisation. The sealed set tests whether the selected candidate generalises beyond the examples that influenced the search.

## Multi-Engine Execution

All three exploration engines received the same baseline harness, evaluator, task contract, and per-engine evaluation allowance. GEPA completed six evaluations but did not produce a candidate that improved the visible score. AutoResearch also completed six evaluations without improving the baseline. Meta-Harness produced the strongest exploration candidate and reached a visible score of 1.0 within its six-evaluation allocation.

A fresh GEPA continuation was then seeded from the Meta-Harness candidate. The continuation retained the 1.0 optimiser-visible score across its six additional evaluations.

The recorded phase results were:

```
GEPA exploration
  Best score: 0.0
  Evaluations: 6
  Proposer cost equivalent: $0.000000
AutoResearch exploration
  Best score: 0.0
  Evaluations: 6
  Proposer cost equivalent: $0.180230
Meta-Harness exploration
  Best score: 1.0
  Evaluations: 6
  Proposer cost equivalent: $0.268777
GEPA continuation
  Best score: 1.0
  Evaluations: 6
  Proposer cost equivalent: $0.000000
Combined result
  Best score: 1.0
  Total evaluations: 24
  Total proposer cost equivalent: $0.449007
```

The final baseline-versus-candidate comparison was then executed against the two sealed held-out cases. The baseline failed both cases and received a score of 0.0. The candidate passed both cases and received a score of 1.0.

```
Baseline held-out result
  Score: 0.0
  Passed cases: 0
  Failed cases: 2
  Local-model tokens: 923
Candidate held-out result
  Score: 1.0
  Passed cases: 2
  Failed cases: 0
  Local-model tokens: 1,090
```

The optimiser phases consumed 10,820 local-model tokens. The final baseline-versus-candidate evaluation consumed an additional 2,013 tokens, producing a recorded total of 12,833 local-model tokens. End-to-end execution took approximately 11 minutes and 22 seconds.

The reported $0.449007 value is API-price-equivalent accounting returned by Claude Code and GEPA. It was used to enforce the experiment budget. It does not represent an API-key charge or an Anthropic invoice because the agent-backed phases used an authenticated subscription session.

## The Selected Harness Change

The winning candidate modified one field: the system prompt of the release-decider agent. The baseline requested a concise release decision but did not define a stable response schema or specify how unresolved blockers should affect the result. That ambiguity produced inconsistent behaviour on the evaluation cases. The selected candidate introduced an explicit output contract:

```
DECISION: yes
REASON: [brief explanation]
OR
DECISION: no
REASON: [brief explanation]
```

It also made the decision rule explicit:

- return yes only when all required conditions are satisfied and no blocker remains;
- return no when a required check fails or a material concern remains unresolved.

This was a narrow change, which is desirable for harness optimisation. The candidate did not replace the workflow, alter model routing, or introduce a large generated configuration. It clarified one decision boundary and made the agent response machine-verifiable.

The final audit reported:

- Changed fields: 1
- Changed surfaces: agents
- Policy violations: 0
- Warnings: 0
- Regressions: 0
- Held-out gate: passed

The optimiser did not modify permissions, execution checks, approvals, sandbox settings, model routing, or workflow structure. The candidate was written to a staging directory, and the original harness remained unchanged.

## Integration Safety Model

The principal integration requirement is that optimisation must remain subordinate to harness policy. A higher task score is not sufficient evidence that a candidate is safe to adopt. SuperQode enforces that separation through four controls.

**Structural validation**
Every proposal must parse as a valid HarnessSpec. Malformed YAML and invalid schema changes are rejected before execution.

**Mutation-surface enforcement**
The optimisation policy determines which parts of the harness may change. A candidate that modifies an unauthorised field is rejected even when the modification could improve the visible score.

**Non-regression and policy audit**
Candidates are compared with the baseline for permission expansion, weakened checks, altered approvals, and other protected behaviours. These controls remain outside optimiser control.

**Staged adoption**
The best candidate is never promoted automatically. SuperQode writes it as a separate artefact for inspection, together with reports, audit records, and evaluation evidence. Adoption remains an explicit human or controlled CI decision.

This model prevents a common optimisation failure mode: allowing the search process to redefine what counts as success. The optimiser can propose changes, but it cannot remove the guardrails used to judge those changes.

## Reproducing the Integration in SuperQode

The integration is documented as an experimental SuperQode workflow. A full Omni run requires:

- uv;
- a local Ollama service;
- qwen3.5:9b, or another model selected through --model;
- Claude Code authenticated through a subscription session for the AutoResearch and Meta-Harness engines.

You need to checkout the SuperQode repo. A smoke run can be used to verify the integration wiring without executing the complete multi-engine pipeline:

```bash
scripts/run_tiny_omni_experiment.sh \
  --spec examples/harnesses/omni-tiny-local.yaml
```

The bounded Omni pipeline is executed with:

```bash
scripts/run_tiny_omni_experiment.sh \
  --spec examples/harnesses/omni-tiny-local.yaml \
  --mode omni
```

Each run creates a unique directory under:

```
.superqode/harness-optimizations/
```

The generated run directory contains the human-readable report, structured JSON results, candidate audit ledger, evaluation artefacts, and the staged harness candidate:

```
report.md
report.json
staged/best_harness.yaml
```

The source HarnessSpec is not overwritten. The staged candidate must be reviewed and adopted separately.

For implementation details, exact component versions, known warnings, and the recorded experiment outputs, consult the GEPA Omni experiment documentation. The broader engine model and pipeline composition API are described in the GEPA article, "optimize_anything Goes omni: Pluggable Engines and Composable Optimizer Pipelines".

## Current Limitation: Agent Runtime Dependency

The local GEPA engine and the harness evaluation rollouts can operate with a local Ollama model. The current AutoResearch and Meta-Harness implementations used in this experiment rely on Claude Code. A complete three-engine Omni run therefore has a provider-specific agent-runtime dependency. Subscription authentication avoids the requirement for an Anthropic API key and makes bounded experiments practical, but it does not make the complete pipeline provider-neutral.

A future extension should make agent-backed optimisation engines runtime-pluggable in the same way that optimize_anything makes the optimisation engine pluggable. That would allow the proposer runtime to be selected independently, for example, Claude Code, Codex, another coding agent, or a fully local agent loop, without changing the SuperQode evaluation contract. Until that abstraction is available, the dependency should remain explicit. Users can still run the local GEPA engine independently, while the experiment runner clearly validates and reports the additional requirements for a complete Omni execution.

## Interpretation of the Result

The strongest exploration candidate came from Meta-Harness, demonstrating the practical value of allowing several search strategies to compete under the same evaluation contract. A fresh GEPA phase then continued from that candidate without regression. The selected change was small, passed policy review, improved the sealed held-out result, and remained easy to inspect manually.

At the same time, the experiment used only five small binary-scored tasks, a single bounded run, and an intentionally under-specified baseline. Those conditions are appropriate for integration testing but insufficient for claims about average optimiser quality or production-scale effectiveness.

A stronger evaluation programme should include representative project harnesses, multiple random seeds, richer scoring functions, repeated held-out evaluation, larger task sets, and explicit measurement of cost and latency trade-offs. It should also test whether the selected candidate remains effective across model changes and different execution environments.

## Conclusion

The GEPA Omni integration demonstrates that a complete coding-agent harness can be treated as an optimisable artefact without giving the optimiser authority over the controls that define safe execution. Three engines evaluated the same HarnessSpec under a shared budget. Meta-Harness produced the best exploration candidate, GEPA continued from that candidate, and the final result passed sealed held-out evaluation. The improvement was limited to one release-decision prompt, while permissions, checks, approvals, workflow, routing, and sandbox policy remained unchanged. The most important result is therefore not the size of the score improvement. It is the preservation of the system boundary: optimisers may search, but SuperQode continues to own validation, policy enforcement, evaluation, and adoption.

That separation provides a practical foundation for future harness optimisation research. It supports experimentation with heterogeneous optimisation engines while keeping every proposed change reviewable, reproducible, and subject to the same operational controls as any other production configuration change.

Checkout SuperQode repo and docs, optimize your harnesses with GEPA Omni and take control of your code factories.
