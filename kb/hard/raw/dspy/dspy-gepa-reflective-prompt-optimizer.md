# dspy.GEPA — Reflective Prompt Optimizer (API reference, advanced features, implementation)

**Source:** https://dspy.ai/api/optimizers/GEPA/overview/ · https://dspy.ai/api/optimizers/GEPA/GEPA_Advanced/ · https://github.com/stanfordnlp/dspy/blob/main/dspy/teleprompt/gepa/gepa.py
**Ingested:** 2026-08-15
**Tags:** dspy, prompt-optimization, gepa, credit-assignment, feedback-function, instruction-proposer, component-selection, pareto-frontier, compound-ai-systems

> **Ingest note:** three artifacts concatenated. The published docs pages are mkdocs sources, so their
> `::: dspy.GEPA` blocks are mkdocstrings directives — the rendered API surface actually comes from the
> docstrings in `gepa.py`, which is why the implementation file is included in full as part 3.
> Companion paper ingested separately: `gepa-reflective-prompt-evolution-can-outperform-reinforcement-learning.md`.
> Worked-example tutorials (`gepa_aime`, `gepa_papillon`, `gepa_facilitysupportanalyzer`,
> `gepa_trusted_monitor`, `gepa_ai_program`) are notebooks and were not ingested.

---

## Part 1 — Docs: `dspy.GEPA` overview

# dspy.GEPA: Reflective Prompt Optimizer

**GEPA** (Genetic-Pareto) is a reflective optimizer proposed in "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning" (Agrawal et al., 2025, [arxiv:2507.19457](https://arxiv.org/abs/2507.19457)), that adaptively evolves _textual components_ (such as prompts) of arbitrary systems. In addition to scalar scores returned by metrics, users can also provide GEPA with a text feedback to guide the optimization process. Such textual feedback provides GEPA more visibility into why the system got the score that it did, and then GEPA can introspect to identify how to improve the score. This allows GEPA to propose high performing prompts in very few rollouts.

<!-- START_API_REF -->
::: dspy.GEPA
    handler: python
    options:
        members:
            - auto_budget
            - compile
            - get_params
        show_source: true
        show_root_heading: true
        heading_level: 2
        docstring_style: google
        show_root_full_path: true
        show_object_full_path: false
        separate_signature: false
        inherited_members: true
<!-- END_API_REF -->

One of the key insights behind GEPA is its ability to leverage domain-specific textual feedback. Users should provide a feedback function as the GEPA metric, which has the following call signature:
<!-- START_API_REF -->
::: dspy.teleprompt.gepa.gepa.GEPAFeedbackMetric
    handler: python
    options:
        members:
            - __call__
        show_source: true
        show_root_heading: true
        heading_level: 2
        docstring_style: google
        show_root_full_path: true
        show_object_full_path: false
        separate_signature: false
        inherited_members: true
<!-- END_API_REF -->

When `track_stats=True`, GEPA returns detailed results about all of the proposed candidates, and metadata about the optimization run. The results are available in the `detailed_results` attribute of the optimized program returned by GEPA, and has the following type:
<!-- START_API_REF -->
::: dspy.teleprompt.gepa.gepa.DspyGEPAResult
    handler: python
    options:
        show_source: true
        show_root_heading: true
        heading_level: 2
        docstring_style: google
        show_root_full_path: true
        show_object_full_path: false
        separate_signature: false
        inherited_members: true
<!-- END_API_REF -->

## Usage Examples

See GEPA usage tutorials in [GEPA Tutorials](../../../tutorials/gepa_ai_program/index.md).

### Inference-Time Search

GEPA can act as a test-time/inference search mechanism. By setting your `valset` to your _evaluation batch_ and using `track_best_outputs=True`, GEPA produces for each batch element the highest-scoring outputs found during the evolutionary search.

```python
gepa = dspy.GEPA(metric=metric, track_stats=True, ...)
new_prog = gepa.compile(student, trainset=my_tasks, valset=my_tasks)
highest_score_achieved_per_task = new_prog.detailed_results.highest_score_achieved_per_val_task
best_outputs = new_prog.detailed_results.best_outputs_valset
```

## How Does GEPA Work?

### 1. **Reflective Prompt Mutation**

GEPA uses LLMs to _reflect_ on structured execution traces (inputs, outputs, failures, feedback), targeting a chosen module and proposing a new instruction/program text tailored to real observed failures and rich textual/environmental feedback.

### 2. **Rich Textual Feedback as Optimization Signal**

GEPA can leverage _any_ textual feedback available—not just scalar rewards. This includes evaluation logs, code traces, failed parses, constraint violations, error message strings, or even isolated submodule-specific feedback. This allows actionable, domain-aware optimization. 

### 3. **Pareto-based Candidate Selection**

Rather than evolving just the _best_ global candidate (which leads to local optima or stagnation), GEPA maintains a Pareto frontier: the set of candidates which achieve the highest score on at least one evaluation instance. In each iteration, the next candidate to mutate is sampled (with probability proportional to coverage) from this frontier, guaranteeing both exploration and robust retention of complementary strategies.

### Algorithm Summary

1. **Initialize** the candidate pool with the unoptimized program.
2. **Iterate**:
   - **Sample a candidate** (from Pareto frontier).
   - **Sample a minibatch** from the train set.
   - **Collect execution traces + feedbacks** for module rollout on minibatch.
   - **Select a module** of the candidate for targeted improvement.
   - **LLM Reflection:** Propose a new instruction/prompt for the targeted module using reflective meta-prompting and the gathered feedback.
   - **Roll out the new candidate** on the minibatch; **if improved, evaluate on Pareto validation set**.
   - **Update the candidate pool/Pareto frontier.**
   - **[Optionally] System-aware merge/crossover**: Combine best-performing modules from distinct lineages.
3. **Continue** until rollout or metric budget is exhausted. 
4. **Return** candidate with best aggregate performance on validation.

## Implementing Feedback Metrics

A well-designed metric is central to GEPA's sample efficiency and learning signal richness. GEPA expects the metric to returns a `dspy.Prediction(score=..., feedback=...)`. GEPA leverages natural language traces from LLM-based workflows for optimization, preserving intermediate trajectories and errors in plain text rather than reducing them to numerical rewards. This mirrors human diagnostic processes, enabling clearer identification of system behaviors and bottlenecks.

Practical Recipe for GEPA-Friendly Feedback:

- **Leverage Existing Artifacts**: Use logs, unit tests, evaluation scripts, and profiler outputs; surfacing these often suffices.
- **Decompose Outcomes**: Break scores into per-objective components (e.g., correctness, latency, cost, safety) and attribute errors to steps.
- **Expose Trajectories**: Label pipeline stages, reporting pass/fail with salient errors (e.g., in code generation pipelines).
- **Ground in Checks**: Employ automatic validators (unit tests, schemas, simulators) or LLM-as-a-judge for non-verifiable tasks (as in PUPA).
- **Prioritize Clarity**: Focus on error coverage and decision points over technical complexity.

### Examples

- **Document Retrieval** (e.g., HotpotQA): List correctly retrieved, incorrect, or missed documents, beyond mere Recall/F1 scores.
- **Multi-Objective Tasks** (e.g., PUPA): Decompose aggregate scores to reveal contributions from each objective, highlighting tradeoffs (e.g., quality vs. privacy).
- **Stacked Pipelines** (e.g., code generation: parse → compile → run → profile → evaluate): Expose stage-specific failures; natural-language traces often suffice for LLM self-correction.

## Custom Instruction Proposal

For advanced customization of GEPA's instruction proposal mechanism, including custom instruction proposers and component selectors, see [Advanced Features](GEPA_Advanced.md).

## Further Reading

- [GEPA Paper: arxiv:2507.19457](https://arxiv.org/abs/2507.19457)
- [GEPA Github](https://github.com/gepa-ai/gepa) - This repository provides the core GEPA evolution pipeline used by `dspy.GEPA` optimizer.
- [DSPy Tutorials](../../../tutorials/gepa_ai_program/index.md)


---

## Part 2 — Docs: `dspy.GEPA` advanced features

# dspy.GEPA - Advanced Features

## Custom Instruction Proposers

### What is instruction_proposer?

The `instruction_proposer` is the component responsible for invoking the `reflection_lm` and proposing new prompts during GEPA optimization. When GEPA identifies underperforming components in your DSPy program, the instruction proposer analyzes execution traces, feedback, and failures to generate improved instructions tailored to the observed issues.

### Default Implementation

By default, GEPA uses the built-in instruction proposer from the [GEPA library](https://github.com/gepa-ai/gepa), which implements the [`ProposalFn`](https://github.com/gepa-ai/gepa/blob/main/src/gepa/core/adapter.py). The [default proposer](https://github.com/gepa-ai/gepa/blob/main/src/gepa/proposer/reflective_mutation/reflective_mutation.py#L53-L75) uses this prompt template:

````
I provided an assistant with the following instructions to perform a task for me:
```
<curr_param>
```

The following are examples of different task inputs provided to the assistant along with the assistant's response for each of them, and some feedback on how the assistant's response could be better:
```
<side_info>
```

Your task is to write a new instruction for the assistant.

Read the inputs carefully and identify the input format and infer detailed task description about the task I wish to solve with the assistant.

Read all the assistant responses and the corresponding feedback. Identify all niche and domain specific factual information about the task and include it in the instruction, as a lot of it may not be available to the assistant in the future. The assistant may have utilized a generalizable strategy to solve the task, if so, include that in the instruction as well.

Provide the new instructions within ``` blocks.
````

This template is automatically filled with:

- `<curr_param>`: The current instruction being optimized
- `<side_info>`: Structured markdown containing predictor inputs, generated outputs, and evaluation feedback


Example of default behavior:

```python
# Default instruction proposer is used automatically
gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=dspy.LM(model="gpt-5", temperature=1.0, max_tokens=32000, api_key=api_key),
    auto="medium"
)
optimized_program = gepa.compile(student, trainset=examples)
```

### When to Use Custom instruction_proposer

**Note:** Custom instruction proposers are an advanced feature. Most users should start with the default proposer, which works well for most text-based optimization tasks.

Consider implementing a custom instruction proposer when you need:

- **Multi-modal handling**: Process images (dspy.Image) alongside textual information in your inputs
- **Nuanced control on limits and length constraints**: Have more fine-grained control over instruction length, format, and structural requirements
- **Domain-specific information**: Inject specialized knowledge, terminology, or context that the default proposer lacks and cannot be provided via feedback_func. This is an advanced feature, and most users should not need to use this.
- **Provider-specific prompting guides**: Optimize instructions for specific LLM providers (OpenAI, Anthropic, etc.) with their unique formatting preferences
- **Coupled component updates**: Handle situations where 2 or more components need to be updated together in a coordinated manner, rather than optimizing each component independently (refer to component_selector parameter, in [Custom Component Selection](#custom-component-selection) section, for related functionality)
- **External knowledge integration**: Connect to databases, APIs, or knowledge bases during instruction generation

### Available Options

**Built-in Options:**

- **Default Proposer**: The standard GEPA instruction proposer (used when `instruction_proposer=None`). The default instruction proposer IS an instruction proposer as well! It is the most general one, that was used for the diverse experiments reported in the GEPA paper and tutorials.
- **MultiModalInstructionProposer**: Handles `dspy.Image` inputs and structured multimodal content.

```python
from dspy.teleprompt.gepa.instruction_proposal import MultiModalInstructionProposer

# For tasks involving images or multimodal inputs
gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=dspy.LM(model="gpt-5", temperature=1.0, max_tokens=32000, api_key=api_key),
    instruction_proposer=MultiModalInstructionProposer(),
    auto="medium"
)
```

We invite community contributions of new instruction proposers for specialized domains as the [GEPA library](https://github.com/gepa-ai/gepa) continues to grow.

### How to Implement Custom Instruction Proposers

Custom instruction proposers must implement the `ProposalFn` protocol by defining a callable class or function. GEPA will call your proposer during optimization:

```python
from dspy.teleprompt.gepa.gepa_utils import ReflectiveExample

class CustomInstructionProposer:
    def __call__(
        self,
        candidate: dict[str, str],                          # Candidate component name -> instruction mapping to be updated in this round
        reflective_dataset: dict[str, list[ReflectiveExample]],  # Component -> examples with structure: {"Inputs": ..., "Generated Outputs": ..., "Feedback": ...}
        components_to_update: list[str]                     # Which components to improve
    ) -> dict[str, str]:                                    # Return new instruction mapping only for components being updated
        # Your custom instruction generation logic here
        return updated_instructions

# Or as a function:
def custom_instruction_proposer(candidate, reflective_dataset, components_to_update):
    # Your custom instruction generation logic here
    return updated_instructions
```

**Reflective Dataset Structure:**

- `dict[str, list[ReflectiveExample]]` - Maps component names to lists of examples
- `ReflectiveExample` TypedDict contains:
  - `Inputs: dict[str, Any]` - Predictor inputs (may include dspy.Image objects)
  - `Generated_Outputs: dict[str, Any] | str` - Success: output fields dict, Failure: error message
  - `Feedback: str` - Always a string from metric function or auto-generated by GEPA

#### Basic Example: Word Limit Proposer

```python
import dspy
from gepa.core.adapter import ProposalFn
from dspy.teleprompt.gepa.gepa_utils import ReflectiveExample

class GenerateWordLimitedInstruction(dspy.Signature):
    """Given a current instruction and feedback examples, generate an improved instruction with word limit constraints."""

    current_instruction = dspy.InputField(desc="The current instruction that needs improvement")
    feedback_summary = dspy.InputField(desc="Feedback from examples that might include both positive and negative cases")
    max_words = dspy.InputField(desc="Maximum number of words allowed in the new instruction")

    improved_instruction = dspy.OutputField(desc="A new instruction that fixes the issues while staying under the max_words limit")

class WordLimitProposer(ProposalFn):
    def __init__(self, max_words: int = 1000):
        self.max_words = max_words
        self.instruction_improver = dspy.ChainOfThought(GenerateWordLimitedInstruction)

    def __call__(self, candidate: dict[str, str], reflective_dataset: dict[str, list[ReflectiveExample]], components_to_update: list[str]) -> dict[str, str]:
        updated_components = {}

        for component_name in components_to_update:
            if component_name not in candidate or component_name not in reflective_dataset:
                continue

            current_instruction = candidate[component_name]
            component_examples = reflective_dataset[component_name]

            # Create feedback summary
            feedback_text = "\n".join([
                f"Example {i+1}: {ex.get('Feedback', 'No feedback')}"
                for i, ex in enumerate(component_examples)  # Limit examples to prevent context overflow
            ])

            # Use the module to improve the instruction
            result = self.instruction_improver(
                current_instruction=current_instruction,
                feedback_summary=feedback_text,
                max_words=self.max_words
            )

            updated_components[component_name] = result.improved_instruction

        return updated_components

# Usage
gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=dspy.LM(model="gpt-5", temperature=1.0, max_tokens=32000, api_key=api_key),
    instruction_proposer=WordLimitProposer(max_words=700),
    auto="medium"
)
```

#### Advanced Example: RAG-Enhanced Instruction Proposer

```python
import dspy
from gepa.core.adapter import ProposalFn
from dspy.teleprompt.gepa.gepa_utils import ReflectiveExample

class GenerateDocumentationQuery(dspy.Signature):
    """Analyze examples with feedback to identify common issue patterns and generate targeted database queries for retrieving relevant documentation.

    Your goal is to search a document database for guidelines that address the problematic patterns found in the examples. Look for recurring issues, error types, or failure modes in the feedback, then craft specific search queries that will find documentation to help resolve these patterns."""

    current_instruction = dspy.InputField(desc="The current instruction that needs improvement")
    examples_with_feedback = dspy.InputField(desc="Examples with their feedback showing what issues occurred and any recurring patterns")

    failure_patterns: str = dspy.OutputField(desc="Summarize the common failure patterns identified in the examples")

    retrieval_queries: list[str] = dspy.OutputField(desc="Specific search queries to find relevant documentation in the database that addresses the common issue patterns identified in the problematic examples")

class GenerateRAGEnhancedInstruction(dspy.Signature):
    """Generate improved instructions using retrieved documentation and examples analysis."""

    current_instruction = dspy.InputField(desc="The current instruction that needs improvement")
    relevant_documentation = dspy.InputField(desc="Retrieved guidelines and best practices from specialized documentation")
    examples_with_feedback = dspy.InputField(desc="Examples showing what issues occurred with the current instruction")

    improved_instruction: str = dspy.OutputField(desc="Enhanced instruction that incorporates retrieved guidelines and addresses the issues shown in the examples")

class RAGInstructionImprover(dspy.Module):
    """Module that uses RAG to improve instructions with specialized documentation."""

    def __init__(self, retrieval_model):
        super().__init__()
        self.retrieve = retrieval_model  # Could be dspy.Retrieve or custom retriever
        self.query_generator = dspy.ChainOfThought(GenerateDocumentationQuery)
        self.generate_answer = dspy.ChainOfThought(GenerateRAGEnhancedInstruction)

    def forward(self, current_instruction: str, component_examples: list):
        """Improve instruction using retrieved documentation."""

        # Let LM analyze examples and generate targeted retrieval queries
        query_result = self.query_generator(
            current_instruction=current_instruction,
            examples_with_feedback=component_examples
        )

        results = self.retrieve.query(
            query_texts=query_result.retrieval_queries,
            n_results=3
        )

        relevant_docs_parts = []
        for i, (query, query_docs) in enumerate(zip(query_result.retrieval_queries, results['documents'])):
            if query_docs:
                docs_formatted = "\n".join([f"  - {doc}" for doc in query_docs])
                relevant_docs_parts.append(
                    f"**Search Query #{i+1}**: {query}\n"
                    f"**Retrieved Guidelines**:\n{docs_formatted}"
                )

        relevant_docs = "\n\n" + "="*60 + "\n\n".join(relevant_docs_parts) + "\n" + "="*60

        # Generate improved instruction with retrieved context
        result = self.generate_answer(
            current_instruction=current_instruction,
            relevant_documentation=relevant_docs,
            examples_with_feedback=component_examples
        )

        return result

class DocumentationEnhancedProposer(ProposalFn):
    """Instruction proposer that accesses specialized documentation via RAG."""

    def __init__(self, documentation_retriever):
        """
        Args:
            documentation_retriever: A retrieval model that can search your specialized docs
                                   Could be dspy.Retrieve, ChromadbRM, or custom retriever
        """
        self.instruction_improver = RAGInstructionImprover(documentation_retriever)

    def __call__(self, candidate: dict[str, str], reflective_dataset: dict[str, list[ReflectiveExample]], components_to_update: list[str]) -> dict[str, str]:
        updated_components = {}

        for component_name in components_to_update:
            if component_name not in candidate or component_name not in reflective_dataset:
                continue

            current_instruction = candidate[component_name]
            component_examples = reflective_dataset[component_name]

            result = self.instruction_improver(
                current_instruction=current_instruction,
                component_examples=component_examples
            )

            updated_components[component_name] = result.improved_instruction

        return updated_components

import chromadb

client = chromadb.Client()
collection = client.get_collection("instruction_guidelines")

gepa = dspy.GEPA(
    metric=task_specific_metric,
    reflection_lm=dspy.LM(model="gpt-5", temperature=1.0, max_tokens=32000, api_key=api_key),
    instruction_proposer=DocumentationEnhancedProposer(collection),
    auto="medium"
)
```

#### Integration Patterns

**Using Custom Proposer with External LM:**

```python
class ExternalLMProposer(ProposalFn):
    def __init__(self):
        # Manage your own LM instance
        self.external_lm = dspy.LM('gemini/gemini-2.5-pro')

    def __call__(self, candidate, reflective_dataset, components_to_update):
        updated_components = {}

        with dspy.context(lm=self.external_lm):
            # Your custom logic here using self.external_lm
            for component_name in components_to_update:
                # ... implementation
                pass

        return updated_components

gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=None,  # Optional when using custom proposer
    instruction_proposer=ExternalLMProposer(),
    auto="medium"
)
```

**Best Practices:**

- **Use the full power of DSPy**: Leverage DSPy components like `dspy.Module`, `dspy.Signature`, and `dspy.Predict` to create your instruction proposer rather than direct LM calls. Consider `dspy.Refine` for constraint satisfaction, `dspy.ChainOfThought` for complex reasoning tasks, and compose multiple modules for sophisticated instruction improvement workflows
- **Enable holistic feedback analysis**: While dspy.GEPA's `GEPAFeedbackMetric` processes one (gold, prediction) pair at a time, instruction proposers receive all examples for a component in batch, enabling cross-example pattern detection and systematic issue identification.
- **Mind data serialization**: Serializing everything to strings might not be ideal - handle complex input types (like `dspy.Image`) by maintaining their structure for better LM processing
- **Test thoroughly**: Test your custom proposer with representative failure cases

## Custom Component Selection

### What is component_selector?

The `component_selector` parameter controls which components (predictors) in your DSPy program are selected for optimization at each GEPA iteration. Instead of the default round-robin approach that updates one component at a time, you can implement custom selection strategies that choose single or multiple components based on optimization state, performance trajectories, and other contextual information.

### Default Behavior

By default, GEPA uses a **round-robin strategy** (`RoundRobinReflectionComponentSelector`) that cycles through components sequentially, optimizing one component per iteration:

```python
# Default round-robin component selection
gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=dspy.LM(model="gpt-5", temperature=1.0, max_tokens=32000, api_key=api_key),
    # component_selector="round_robin"  # This is the default
    auto="medium"
)
```

### Built-in Selection Strategies

**String-based selectors:**

- `"round_robin"` (default): Cycles through components one at a time
- `"all"`: Selects all components for simultaneous optimization

```python
# Optimize all components simultaneously
gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=reflection_lm,
    component_selector="all",  # Update all components together
    auto="medium"
)

# Explicit round-robin selection
gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=reflection_lm,
    component_selector="round_robin",  # One component per iteration
    auto="medium"
)
```

### When to Use Custom Component Selection

Consider implementing custom component selection when you need:

- **Dependency-aware optimization**: Update related components together (e.g., a classifier and its input formatter)
- **LLM-driven selection**: Let an LLM analyze trajectories and decide which components need attention
- **Resource-conscious optimization**: Balance optimization thoroughness with computational budget

### Custom Component Selector Protocol

Custom component selectors must implement the [`ReflectionComponentSelector`](https://github.com/gepa-ai/gepa/blob/main/src/gepa/proposer/reflective_mutation/base.py) protocol by defining a callable class or function. GEPA will call your selector during optimization:

```python
from dspy.teleprompt.gepa.gepa_utils import GEPAState, Trajectory

class CustomComponentSelector:
    def __call__(
        self,
        state: GEPAState,                    # Complete optimization state with history
        trajectories: list[Trajectory],      # Execution traces from the current minibatch
        subsample_scores: list[float],       # Scores for each example in the current minibatch
        candidate_idx: int,                  # Index of the current program candidate being optimized
        candidate: dict[str, str],           # Component name -> instruction mapping
    ) -> list[str]:                          # Return list of component names to optimize
        # Your custom component selection logic here
        return selected_components

# Or as a function:
def custom_component_selector(state, trajectories, subsample_scores, candidate_idx, candidate):
    # Your custom component selection logic here
    return selected_components
```

### Custom Implementation Example

Here's a simple function that alternates between optimizing different halves of your components:

```python
def alternating_half_selector(state, trajectories, subsample_scores, candidate_idx, candidate):
    """Optimize half the components on even iterations, half on odd iterations."""
    components = list(candidate.keys())

    # If there's only one component, always optimize it
    if len(components) <= 1:
        return components

    mid_point = len(components) // 2

    # Use state.i (iteration counter) to alternate between halves
    if state.i % 2 == 0:
        # Even iteration: optimize first half
        return components[:mid_point]
    else:
        # Odd iteration: optimize second half
        return components[mid_point:]

# Usage
gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=reflection_lm,
    component_selector=alternating_half_selector,
    auto="medium"
)
```

### Integration with Custom Instruction Proposers

Component selectors work seamlessly with custom instruction proposers. The selector determines which components to update, then the instruction proposer generates new instructions for those components:

```python
# Combined custom selector + custom proposer
gepa = dspy.GEPA(
    metric=my_metric,
    reflection_lm=reflection_lm,
    component_selector=alternating_half_selector,
    instruction_proposer=WordLimitProposer(max_words=500),
    auto="medium"
)
```


---

## Part 3 — Implementation: `dspy/teleprompt/gepa/gepa.py`

```python
import inspect
import logging
import math
import random
from dataclasses import dataclass
from typing import Any, Literal, Optional, Protocol, Union

from gepa import GEPAResult
from gepa.core.adapter import ProposalFn
from gepa.proposer.reflective_mutation.base import ReflectionComponentSelector

from dspy.clients.lm import LM
from dspy.primitives import Example, Module, Prediction
from dspy.teleprompt.gepa.gepa_utils import DspyAdapter, DSPyTrace, PredictorFeedbackFn, ScoreWithFeedback
from dspy.teleprompt.teleprompt import Teleprompter
from dspy.utils.annotation import experimental

logger = logging.getLogger(__name__)

AUTO_RUN_SETTINGS = {
    "light": {"n": 6},
    "medium": {"n": 12},
    "heavy": {"n": 18},
}


@experimental(version="3.0.0")
class GEPAFeedbackMetric(Protocol):
    def __call__(
        self,
        gold: Example,
        pred: Prediction,
        trace: Optional["DSPyTrace"],
        pred_name: str | None,
        pred_trace: Optional["DSPyTrace"],
        program_trace: Optional["DSPyTrace"] = None,
    ) -> Union[float, "ScoreWithFeedback"]:
        """
        This function is called with the following arguments:
        - gold: The gold example.
        - pred: The predicted output.
        - trace: Optional. The trace of the program's execution.
        - pred_name: Optional. The name of the target predictor currently being optimized by GEPA, for which
            the feedback is being requested.
        - pred_trace: Optional. The trace of the target predictor's execution GEPA is seeking feedback for.
        - program_trace: Optional. The full execution trace of the program, supplied at scoring time when a
            `dspy.Flex` submodule is being optimized. Declare this parameter to score against how an answer was
            produced (e.g. `len(program_trace)` as an LM-call count), rather than only whether it was correct.
            Unlike `trace`, it is populated during candidate *scoring*.

        Note the `pred_name` and `pred_trace` arguments. During optimization, GEPA will call the metric to obtain
        feedback for individual predictors being optimized. GEPA provides the name of the predictor in `pred_name`
        and the sub-trace (of the trace) corresponding to the predictor in `pred_trace`.
        If available at the predictor level, the metric should return dspy.Prediction(score: float, feedback: str)
        corresponding to the predictor.
        If not available at the predictor level, the metric can also return a text feedback at the program level
        (using just the gold, pred and trace).
        If no feedback is returned, GEPA will use a simple text feedback consisting of just the score:
        f"This trajectory got a score of {score}."
        """
        ...


@experimental(version="3.0.0")
@dataclass(frozen=True)
class DspyGEPAResult:
    """
    Additional data related to the GEPA run.

    Fields:
    - candidates: list of proposed candidates (compiled DSPy modules)
    - parents: lineage info; for each candidate i, parents[i] is a list of parent indices or None
    - val_aggregate_scores: per-candidate aggregate score on the validation set (higher is better)
    - val_subscores: per-candidate scores keyed by validation instance id
    - per_val_instance_best_candidates: for each val instance id, a set of candidate indices achieving the best score
    - discovery_eval_counts: Budget (number of metric calls / rollouts) consumed up to the discovery of each candidate

    - total_metric_calls: total number of metric calls made across the run
    - num_full_val_evals: number of full validation evaluations performed
    - log_dir: where artifacts were written (if any)
    - seed: RNG seed for reproducibility (if known)

    - best_idx: candidate index with the highest val_aggregate_scores
    - best_candidate: the compiled DSPy module for best_idx
    """

    # Data about the proposed candidates
    candidates: list[Module]
    parents: list[list[int | None]]
    val_aggregate_scores: list[float]
    val_subscores: list[dict[Any, float]]
    per_val_instance_best_candidates: dict[Any, set[int]]
    discovery_eval_counts: list[int]

    # Optional data
    best_outputs_valset: dict[Any, list[tuple[int, Prediction]]] | None = None

    # Optimization metadata
    total_metric_calls: int | None = None
    num_full_val_evals: int | None = None
    log_dir: str | None = None
    seed: int | None = None

    @property
    def best_idx(self) -> int:
        scores = self.val_aggregate_scores
        return max(range(len(scores)), key=lambda i: scores[i])

    @property
    def best_candidate(self) -> Module:
        return self.candidates[self.best_idx]

    @property
    def highest_score_achieved_per_val_task(self) -> dict[Any, float]:
        return {
            val_id: self.val_subscores[list(self.per_val_instance_best_candidates[val_id])[0]][val_id]
            for val_id in self.per_val_instance_best_candidates
        }

    @staticmethod
    def _candidate_components(cand: Module) -> dict[str, str]:
        """The candidate's optimized components. It can be either instruction text per predictor, or
        the full `module_src` of each `dspy.Flex` submodule under its parameter path."""
        from dspy.teleprompt.gepa.gepa_flex_utils import enumerate_flex_submodules

        components = {name: pred.signature.instructions for name, pred in cand.named_predictors()}
        for path, flex in enumerate_flex_submodules(cand).items():
            components[path] = flex.module_src
        return components

    def to_dict(self) -> dict[str, Any]:
        cands = [self._candidate_components(cand) for cand in self.candidates]

        return dict(
            candidates=cands,
            parents=self.parents,
            val_aggregate_scores=self.val_aggregate_scores,
            best_outputs_valset=self.best_outputs_valset,
            val_subscores=self.val_subscores,
            per_val_instance_best_candidates={
                val_id: list(s) for val_id, s in self.per_val_instance_best_candidates.items()
            },
            discovery_eval_counts=self.discovery_eval_counts,
            total_metric_calls=self.total_metric_calls,
            num_full_val_evals=self.num_full_val_evals,
            log_dir=self.log_dir,
            seed=self.seed,
            best_idx=self.best_idx,
        )

    @staticmethod
    def from_gepa_result(gepa_result: "GEPAResult", adapter: "DspyAdapter") -> "DspyGEPAResult":
        return DspyGEPAResult(
            candidates=[adapter.build_program(c) for c in gepa_result.candidates],
            parents=gepa_result.parents,
            val_aggregate_scores=gepa_result.val_aggregate_scores,
            best_outputs_valset=gepa_result.best_outputs_valset,
            val_subscores=gepa_result.val_subscores,
            per_val_instance_best_candidates=gepa_result.per_val_instance_best_candidates,
            discovery_eval_counts=gepa_result.discovery_eval_counts,
            total_metric_calls=gepa_result.total_metric_calls,
            num_full_val_evals=gepa_result.num_full_val_evals,
            log_dir=gepa_result.run_dir,
            seed=gepa_result.seed,
        )


@experimental(version="3.0.0")
class GEPA(Teleprompter):
    """
    GEPA is an evolutionary optimizer, which uses reflection to evolve text components
    of complex systems. GEPA is proposed in the paper [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457).
    The GEPA optimization engine is provided by the `gepa` package, available from [https://github.com/gepa-ai/gepa](https://github.com/gepa-ai/gepa).

    GEPA captures full traces of the DSPy module's execution, identifies the parts of the trace
    corresponding to a specific predictor, and reflects on the behaviour of the predictor to
    propose a new instruction for the predictor. GEPA allows users to provide textual feedback
    to the optimizer, which is used to guide the evolution of the predictor. The textual feedback
    can be provided at the granularity of individual predictors, or at the level of the entire system's
    execution.

    To provide feedback to the GEPA optimizer, implement a metric as follows:
    ```
    def metric(
        gold: Example,
        pred: Prediction,
        trace: Optional[DSPyTrace] = None,
        pred_name: Optional[str] = None,
        pred_trace: Optional[DSPyTrace] = None,
        program_trace: Optional[DSPyTrace] = None,
    ) -> float | ScoreWithFeedback:
        \"""
        This function is called with the following arguments:
        - gold: The gold example.
        - pred: The predicted output.
        - trace: Optional. The trace of the program's execution.
        - pred_name: Optional. The name of the target predictor currently being optimized by GEPA, for which
            the feedback is being requested.
        - pred_trace: Optional. The trace of the target predictor's execution GEPA is seeking feedback for.
        - program_trace: Optional. The program's execution trace, supplied at scoring time when a `dspy.Flex`
            submodule is being optimized. Declare it to score against how the answer was produced (e.g. an
            LM-call penalty). Defaults to None.

        Note the `pred_name` and `pred_trace` arguments. During optimization, GEPA will call the metric to obtain
        feedback for individual predictors being optimized. GEPA provides the name of the predictor in `pred_name`
        and the sub-trace (of the trace) corresponding to the predictor in `pred_trace`.
        If available at the predictor level, the metric should return {'score': float, 'feedback': str} corresponding
        to the predictor.
        If not available at the predictor level, the metric can also return a text feedback at the program level
        (using just the gold, pred and trace).
        If no feedback is returned, GEPA will use a simple text feedback consisting of just the score:
        f"This trajectory got a score of {score}."
        \"""
        ...
    ```

    GEPA can also be used as a batch inference-time search strategy, by passing `valset=trainset, track_stats=True, track_best_outputs=True`, and using the
    `detailed_results` attribute of the optimized program (returned by `compile`) to get the Pareto frontier of the batch. `optimized_program.detailed_results.best_outputs_valset` will contain the best outputs for each task in the batch.

    Examples:
    ```
    gepa = GEPA(metric=metric, track_stats=True)
    batch_of_tasks = [dspy.Example(...) for task in tasks]
    new_prog = gepa.compile(student, trainset=trainset, valset=batch_of_tasks)
    pareto_frontier = new_prog.detailed_results.val_aggregate_scores
    # pareto_frontier is a list of scores, one for each task in the batch.
    ```

    Args:
        metric: The metric function to use for feedback and evaluation.
        auto: The auto budget to use for the run. Options: "light", "medium", "heavy".
        max_full_evals: The maximum number of full evaluations to perform.
        max_metric_calls: The maximum number of metric calls to perform.
        reflection_minibatch_size: The number of examples to use for reflection in a single GEPA step. Default is 3.
        candidate_selection_strategy: The strategy to use for candidate selection. Default is "pareto",
            which stochastically selects candidates from the Pareto frontier of all validation scores.
            Options: "pareto", "current_best".
        reflection_lm: The language model to use for reflection. Required parameter. GEPA benefits from
            a strong reflection model. Consider using `dspy.LM(model='gpt-5', temperature=1.0, max_tokens=32000)`
            for optimal performance.
        skip_perfect_score: Whether to skip examples with perfect scores during reflection. Default is True.
        instruction_proposer: Optional custom instruction proposer implementing GEPA's ProposalFn protocol.
            **Default: None (recommended for most users)** - Uses GEPA's proven instruction proposer from
            the [GEPA library](https://github.com/gepa-ai/gepa), which implements the
            [`ProposalFn`](https://github.com/gepa-ai/gepa/blob/main/src/gepa/core/adapter.py). This default
            proposer is highly capable and was validated across diverse experiments reported in the GEPA
            paper and tutorials.

            See documentation on custom instruction proposers
            [here](https://dspy.ai/api/optimizers/GEPA/GEPA_Advanced/#custom-instruction-proposers).

            **Advanced Feature**: Only needed for specialized scenarios:
            - **Multi-modal handling**: Processing dspy.Image inputs alongside textual information
            - **Nuanced control over constraints**: Fine-grained control over instruction length, format,
              and structural requirements beyond standard feedback mechanisms
            - **Domain-specific knowledge injection**: Specialized terminology or context that cannot be
              provided through feedback_func alone
            - **Provider-specific prompting**: Optimizations for specific LLM providers (OpenAI, Anthropic)
              with unique formatting preferences
            - **Coupled component updates**: Coordinated updates of multiple components together rather
              than independent optimization
            - **External knowledge integration**: Runtime access to databases, APIs, or knowledge bases

            The default proposer handles the vast majority of use cases effectively. Use
            MultiModalInstructionProposer() from dspy.teleprompt.gepa.instruction_proposal for visual
            content or implement custom ProposalFn for highly specialized requirements.

            Note: When both instruction_proposer and reflection_lm are set, the instruction_proposer is called
            in the reflection_lm context. However, reflection_lm is optional when using a custom instruction_proposer.
            Custom instruction proposers can invoke their own LLMs if needed.
        component_selector: Custom component selector implementing the [ReflectionComponentSelector](https://github.com/gepa-ai/gepa/blob/main/src/gepa/proposer/reflective_mutation/base.py) protocol,
            or a string specifying a built-in selector strategy. Controls which components (predictors) are selected
            for optimization at each iteration. Defaults to 'round_robin' strategy which cycles through components
            one at a time. Available string options: 'round_robin' (cycles through components sequentially),
            'all' (selects all components for simultaneous optimization). Custom selectors can implement strategies
            using LLM-driven selection logic based on optimization state and trajectories.
            See [gepa component selectors](https://github.com/gepa-ai/gepa/blob/main/src/gepa/strategies/component_selector.py)
            for available built-in selectors and the ReflectionComponentSelector protocol for implementing custom selectors.
        add_format_failure_as_feedback: Whether to add format failures as feedback. Default is False.
        use_merge: Whether to use merge-based optimization. Default is True.
        max_merge_invocations: The maximum number of merge invocations to perform. Default is 5.
        num_threads: The number of threads to use for evaluation with `Evaluate`. Optional.
        failure_score: The score to assign to failed examples. Default is 0.0.
        perfect_score: The maximum score achievable by the metric. Default is 1.0. Used by GEPA
            to determine if all examples in a minibatch are perfect.
        log_dir: The directory to save the logs. GEPA saves elaborate logs, along with all candidate
            programs, in this directory. Running GEPA with the same `log_dir` will resume the run
            from the last checkpoint.
        track_stats: Whether to return detailed results and all proposed programs in the `detailed_results`
            attribute of the optimized program. Default is False.
        use_wandb: Whether to use wandb for logging. Default is False.
        wandb_api_key: The API key to use for wandb. If not provided, wandb will use the API key
            from the environment variable `WANDB_API_KEY`.
        wandb_init_kwargs: Additional keyword arguments to pass to `wandb.init`.
        track_best_outputs: Whether to track the best outputs on the validation set. track_stats must
            be True if track_best_outputs is True. The optimized program's `detailed_results.best_outputs_valset`
            will contain the best outputs for each task in the validation set.
        warn_on_score_mismatch: GEPA (currently) expects the metric to return the same module-level score when
            called with and without the pred_name. This flag (defaults to True) determines whether a warning is
            raised if a mismatch in module-level and predictor-level score is detected.
        seed: The random seed to use for reproducibility. Default is 0.
        gepa_kwargs: (Optional) Additional keyword arguments to pass directly to [gepa.optimize](https://github.com/gepa-ai/gepa/blob/main/src/gepa/api.py).
            Useful for accessing advanced GEPA features not directly exposed through DSPy's GEPA interface.

            Available parameters:
            - batch_sampler: Strategy for selecting training examples. Can be a [BatchSampler](https://github.com/gepa-ai/gepa/blob/main/src/gepa/strategies/batch_sampler.py) instance or a string
              ('epoch_shuffled'). Defaults to 'epoch_shuffled'. Only valid when reflection_minibatch_size is None.
            - merge_val_overlap_floor: Minimum number of shared validation ids required between parents before
              attempting a merge subsample. Only relevant when using `val_evaluation_policy` other than 'full_eval'.
              Default is 5.
            - stop_callbacks: Optional stopper(s) that return True when optimization should stop. Can be a single
              [StopperProtocol](https://github.com/gepa-ai/gepa/blob/main/src/gepa/utils/stop_condition.py) or a list of StopperProtocol instances.
              Examples: [FileStopper](https://github.com/gepa-ai/gepa/blob/main/src/gepa/utils/stop_condition.py),
              [TimeoutStopCondition](https://github.com/gepa-ai/gepa/blob/main/src/gepa/utils/stop_condition.py),
              [SignalStopper](https://github.com/gepa-ai/gepa/blob/main/src/gepa/utils/stop_condition.py),
              [NoImprovementStopper](https://github.com/gepa-ai/gepa/blob/main/src/gepa/utils/stop_condition.py),
              or custom stopping logic. Note: This overrides the default
              max_metric_calls stopping condition.
            - use_cloudpickle: Use cloudpickle instead of pickle for serialization. Can be helpful when the
              serialized state contains dynamically generated DSPy signatures. Default is False.
            - val_evaluation_policy: Strategy controlling which validation ids to score each iteration. Can be
              'full_eval' (evaluate every id each time) or an [EvaluationPolicy](https://github.com/gepa-ai/gepa/blob/main/src/gepa/strategies/eval_policy.py) instance. Default is 'full_eval'.
            - use_mlflow: If True, enables MLflow integration to log optimization progress.
              MLflow can be used alongside Weights & Biases (WandB).
            - mlflow_tracking_uri: The tracking URI to use for MLflow (when use_mlflow=True).
            - mlflow_experiment_name: The experiment name to use for MLflow (when use_mlflow=True).

            Note: Parameters already handled by DSPy's GEPA class will be overridden by the direct parameters
            and should not be passed through gepa_kwargs.

    Note:
        Budget Configuration: Exactly one of `auto`, `max_full_evals`, or `max_metric_calls` must be provided.
        The `auto` parameter provides preset configurations: "light" for quick experimentation, "medium" for
        balanced optimization, and "heavy" for thorough optimization.

        Reflection Configuration: The `reflection_lm` parameter is required and should be a strong language model.
        GEPA performs best with models like `dspy.LM(model='gpt-5', temperature=1.0, max_tokens=32000)`.
        The reflection process analyzes failed examples to generate feedback for program improvement.

        Merge Configuration: GEPA can merge successful program variants using `use_merge=True`.
        The `max_merge_invocations` parameter controls how many merge attempts are made during optimization.

        Evaluation Configuration: Use `num_threads` to parallelize evaluation. The `failure_score` and
        `perfect_score` parameters help GEPA understand your metric's range and optimize accordingly.

        Logging Configuration: Set `log_dir` to save detailed logs and enable checkpoint resuming.
        Use `track_stats=True` to access detailed optimization results via the `detailed_results` attribute.
        Enable `use_wandb=True` for experiment tracking and visualization.

        Reproducibility: Set `seed` to ensure consistent results across runs with the same configuration.
    """

    def __init__(
        self,
        metric: GEPAFeedbackMetric,
        *,
        # Budget configuration
        auto: Literal["light", "medium", "heavy"] | None = None,
        max_full_evals: int | None = None,
        max_metric_calls: int | None = None,
        # Reflection configuration
        reflection_minibatch_size: int = 3,
        candidate_selection_strategy: Literal["pareto", "current_best"] = "pareto",
        reflection_lm: LM | None = None,
        skip_perfect_score: bool = True,
        add_format_failure_as_feedback: bool = False,
        instruction_proposer: "ProposalFn | None" = None,
        component_selector: "ReflectionComponentSelector | str" = "round_robin",
        # Merge-based configuration
        use_merge: bool = True,
        max_merge_invocations: int | None = 5,
        # Evaluation configuration
        num_threads: int | None = None,
        failure_score: float = 0.0,
        perfect_score: float = 1.0,
        # Logging
        log_dir: str | None = None,
        track_stats: bool = False,
        use_wandb: bool = False,
        wandb_api_key: str | None = None,
        wandb_init_kwargs: dict[str, Any] | None = None,
        track_best_outputs: bool = False,
        warn_on_score_mismatch: bool = True,
        use_mlflow: bool = False,
        # Reproducibility
        seed: int | None = 0,
        # GEPA passthrough kwargs
        gepa_kwargs: dict | None = None,
    ):
        try:
            inspect.signature(metric).bind(None, None, None, None, None)
        except TypeError as e:
            raise TypeError(
                "GEPA metric must accept five arguments: (gold, pred, trace, pred_name, pred_trace). "
                "See https://dspy.ai/api/optimizers/GEPA for details."
            ) from e

        self.metric_fn = metric

        # Budget configuration
        assert (max_metric_calls is not None) + (max_full_evals is not None) + (auto is not None) == 1, (
            "Exactly one of max_metric_calls, max_full_evals, auto must be set. "
            f"You set max_metric_calls={max_metric_calls}, "
            f"max_full_evals={max_full_evals}, "
            f"auto={auto}."
        )
        self.auto = auto
        self.max_full_evals = max_full_evals
        self.max_metric_calls = max_metric_calls

        # Reflection configuration
        self.reflection_minibatch_size = reflection_minibatch_size
        self.candidate_selection_strategy = candidate_selection_strategy

        assert reflection_lm is not None or instruction_proposer is not None, (
            "GEPA requires a reflection language model, or custom instruction proposer to be provided. "
            "Typically, you can use `dspy.LM(model='gpt-5', temperature=1.0, max_tokens=32000)` to get a good reflection model. "
            "Reflection LM is used by GEPA to reflect on the behavior of the program and propose new instructions, and will benefit from a strong model. "
        )

        self.reflection_lm = reflection_lm
        self.skip_perfect_score = skip_perfect_score
        self.add_format_failure_as_feedback = add_format_failure_as_feedback

        # Merge-based configuration
        self.use_merge = use_merge
        self.max_merge_invocations = max_merge_invocations

        # Evaluation Configuration
        self.num_threads = num_threads
        self.failure_score = failure_score
        self.perfect_score = perfect_score

        # Logging configuration
        self.log_dir = log_dir
        self.track_stats = track_stats
        self.use_wandb = use_wandb
        self.wandb_api_key = wandb_api_key
        self.wandb_init_kwargs = wandb_init_kwargs
        self.warn_on_score_mismatch = warn_on_score_mismatch
        self.use_mlflow = use_mlflow

        if track_best_outputs:
            assert track_stats, "track_stats must be True if track_best_outputs is True."
        self.track_best_outputs = track_best_outputs

        # Reproducibility
        self.seed = seed

        self.custom_instruction_proposer = instruction_proposer
        self.component_selector = component_selector
        self.gepa_kwargs = gepa_kwargs or {}

        if "reflection_prompt_template" in self.gepa_kwargs:
            raise ValueError(
                "reflection_prompt_template cannot be passed via gepa_kwargs when using dspy.GEPA. "
                "DspyAdapter implements its own propose_new_texts, so reflection_prompt_template is unused. "
                "To customize reflection behavior, pass a custom ProposalFn via the instruction_proposer parameter instead."
            )

    def auto_budget(
        self, num_preds, num_candidates, valset_size: int, minibatch_size: int = 35, full_eval_steps: int = 5
    ) -> int:
        num_trials = int(max(2 * (num_preds * 2) * math.log2(num_candidates), 1.5 * num_candidates))
        if num_trials < 0 or valset_size < 0 or minibatch_size < 0:
            raise ValueError("num_trials, valset_size, and minibatch_size must be >= 0.")
        if full_eval_steps < 1:
            raise ValueError("full_eval_steps must be >= 1.")

        V = valset_size
        N = num_trials
        M = minibatch_size
        m = full_eval_steps

        # Initial full evaluation on the default program
        total = V

        # Assume upto 5 trials for bootstrapping each candidate
        total += num_candidates * 5

        # N minibatch evaluations
        total += N * M
        if N == 0:
            return total  # no periodic/full evals inside the loop
        # Periodic full evals occur when trial_num % (m+1) == 0, where trial_num runs 2..N+1
        periodic_fulls = (N + 1) // (m) + 1
        # If 1 <= N < m, the code triggers one final full eval at the end
        extra_final = 1 if N < m else 0

        total += (periodic_fulls + extra_final) * V
        return total

    def compile(
        self,
        student: Module,
        *,
        trainset: list[Example],
        teacher: Module | None = None,
        valset: list[Example] | None = None,
    ) -> Module:
        """
        GEPA uses the trainset to perform reflective updates to the prompt, but uses the valset for tracking Pareto scores.
        If no valset is provided, GEPA will use the trainset for both.

        Parameters:
        - student: The student module to optimize.
        - trainset: The training set to use for reflective updates.
        - valset: The validation set to use for tracking Pareto scores. If not provided, GEPA will use the trainset for both.
        """
        from gepa import GEPAResult, optimize

        from dspy.teleprompt.gepa.gepa_flex_utils import enumerate_flex_submodules
        from dspy.teleprompt.gepa.gepa_utils import DspyAdapter, LoggerAdapter

        assert trainset is not None and len(trainset) > 0, "Trainset must be provided and non-empty"
        assert teacher is None, "Teacher is not supported in DspyGEPA yet."

        # dspy.Flex submodules get their code optimized, not just their instructions.
        flex_submodules = enumerate_flex_submodules(student)
        instruction_predictors = list(student.named_predictors())

        num_components = len(instruction_predictors) + len(flex_submodules)
        if self.auto is not None:
            self.max_metric_calls = self.auto_budget(
                num_preds=max(num_components, 1),
                num_candidates=AUTO_RUN_SETTINGS[self.auto]["n"],
                valset_size=len(valset) if valset is not None else len(trainset),
            )
        elif self.max_full_evals is not None:
            self.max_metric_calls = self.max_full_evals * (len(trainset) + (len(valset) if valset is not None else 0))
        else:
            assert self.max_metric_calls is not None, "Either auto, max_full_evals, or max_metric_calls must be set."

        logger.info(
            f"Running GEPA for approx {self.max_metric_calls} metric calls of the program. This amounts to {self.max_metric_calls / len(trainset) if valset is None else self.max_metric_calls / (len(trainset) + len(valset)):.2f} full evals on the {'train' if valset is None else 'train+val'} set."
        )

        if valset is None:
            logger.warning(
                "No valset provided; Using trainset as valset. This is useful as an inference-time scaling strategy where you want GEPA to find the best solutions for the provided tasks in the trainset, as it makes GEPA overfit prompts to the provided trainset. In order to ensure generalization and perform well on unseen tasks, please provide separate trainset and valset. Provide the smallest valset that is just large enough to match the downstream task distribution, while keeping trainset as large as possible."
            )
        valset = valset or trainset
        # 35 matches the default minibatch_size in auto_budget(); when the valset is
        # at or below this size, suggesting further reduction is unhelpful since GEPA
        # would already evaluate the full valset per step.
        if len(valset) > 35:
            logger.info(
                f"Using {len(valset)} examples for tracking Pareto scores. You can consider using a smaller sample of the valset to allow GEPA to explore more diverse solutions within the same budget. GEPA requires you to provide the smallest valset that is just large enough to match your downstream task distribution, while providing as large trainset as possible."
            )
        else:
            logger.info(f"Using {len(valset)} examples for tracking Pareto scores.")

        rng = random.Random(self.seed)

        def feedback_fn_creator(pred_name: str, predictor) -> "PredictorFeedbackFn":
            def feedback_fn(
                predictor_output: dict[str, Any],
                predictor_inputs: dict[str, Any],
                module_inputs: Example,
                module_outputs: Prediction,
                captured_trace: "DSPyTrace",
            ) -> "ScoreWithFeedback":
                trace_for_pred = [(predictor, predictor_inputs, predictor_output)]
                o = self.metric_fn(
                    module_inputs,
                    module_outputs,
                    captured_trace,
                    pred_name,
                    trace_for_pred,
                )
                if hasattr(o, "feedback"):
                    if o["feedback"] is None:
                        o["feedback"] = f"This trajectory got a score of {o['score']}."
                    return o
                else:
                    return dict(score=o, feedback=f"This trajectory got a score of {o}.")

            return feedback_fn

        feedback_map = {k: feedback_fn_creator(k, v) for k, v in instruction_predictors}

        # Build the DSPy adapter that encapsulates evaluation, trace capture, feedback extraction, and instruction proposal
        adapter = DspyAdapter(
            student_module=student,
            metric_fn=self.metric_fn,
            feedback_map=feedback_map,
            failure_score=self.failure_score,
            num_threads=self.num_threads,
            add_format_failure_as_feedback=self.add_format_failure_as_feedback,
            rng=rng,
            reflection_lm=self.reflection_lm,
            custom_instruction_proposer=self.custom_instruction_proposer,
            warn_on_score_mismatch=self.warn_on_score_mismatch,
            reflection_minibatch_size=self.reflection_minibatch_size,
        )

        # Seed candidate: instruction text per non-flex predictor, plus the current module_src of
        # each dspy.Flex submodule as its code component.
        seed_candidate = {name: pred.signature.instructions for name, pred in instruction_predictors}
        for path, flex in flex_submodules.items():
            seed_candidate[path] = flex.module_src

        gepa_result: GEPAResult = optimize(
            seed_candidate=seed_candidate,
            trainset=trainset,
            valset=valset,
            adapter=adapter,
            # Reflection-based configuration
            reflection_lm=(lambda x: adapter.stripped_lm_call(x)[0]) if self.reflection_lm is not None else None,
            candidate_selection_strategy=self.candidate_selection_strategy,
            skip_perfect_score=self.skip_perfect_score,
            reflection_minibatch_size=self.reflection_minibatch_size,
            module_selector=self.component_selector,
            perfect_score=self.perfect_score,
            # Merge-based configuration
            use_merge=self.use_merge,
            max_merge_invocations=self.max_merge_invocations,
            # Budget
            max_metric_calls=self.max_metric_calls,
            # Logging
            logger=LoggerAdapter(logger),
            run_dir=self.log_dir,
            use_wandb=self.use_wandb,
            wandb_api_key=self.wandb_api_key,
            wandb_init_kwargs=self.wandb_init_kwargs,
            use_mlflow=self.use_mlflow,
            track_best_outputs=self.track_best_outputs,
            display_progress_bar=True,
            raise_on_exception=True,
            # Reproducibility
            seed=self.seed,
            **self.gepa_kwargs,
        )

        new_prog = adapter.build_program(gepa_result.best_candidate)

        if self.track_stats:
            dspy_gepa_result = DspyGEPAResult.from_gepa_result(gepa_result, adapter)
            new_prog.detailed_results = dspy_gepa_result

        return new_prog

```
