---
concept: ML Testing Strategies
tags: [ml-testing, invariance, integration-tests, ci-cd]
sources:
  - kb/hard/raw/eugene-yan/how-to-test-machine-learning-code-and-systems.md
  - kb/hard/raw/eugene-yan/dont-mock-machine-learning-models-in-unit-tests.md
  - kb/hard/raw/eugene-yan/writing-robust-tests-for-data-machine-learning-pipelines.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/mlops-monitoring|MLOps Monitoring]]"
  - "[[hard/wiki/ml-production-maintenance|ML Production Maintenance]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# ML Testing Strategies

Testing machine learning systems requires a fundamentally different mindset from testing conventional software. In regular software, logic is handcrafted and deterministic: given an input, you can predict the exact output and assert against it. In ML, the logic is learned from data. The artifact under test is a model, not a function. This distinction forces a split testing approach: testing the code that learns, and testing the learned logic itself.

## The ML-Software Testing Distinction

The core difference:

```
Software:         Input Data + Handcrafted Logic = Expected Output
Machine Learning: Input Data + Expected Output   = Learned Logic
```

Standard software testing mocks dependencies (APIs, databases, filesystems). In ML, you often need to test against the actual model — because the logic lives in the weights. Mocking a model defeats the purpose of behavioral tests.

This creates a practical challenge: models can be multi-gigabyte artifacts slow to load and run. The resolution is stratification: some tests use random or empty weights for structural checks, others run against real weights and are marked "slow" so they only execute pre-commit or pre-merge rather than on every file save.

## Pre-Train Tests: Testing Written Logic

Pre-train tests validate implementation correctness before any training happens. They catch bugs in the code you wrote — not the model you trained.

Concrete examples:
- **Output shape tests:** Given a batch of inputs, does the model return a tensor of the correct shape?
- **Output range tests:** Does a classifier return probabilities in [0, 1]? Does a regression head return unbounded values?
- **Data leak detection:** Are there duplicate rows in train and test splits? Use concatenation + deduplication to catch this automatically.
- **Overfit test:** Given a small, perfectly separable dataset, can the model fit it to 100% accuracy? If not, the architecture or training loop has a bug.
- **Monotonicity test:** Does adding capacity (more trees, more depth) monotonically increase training accuracy? This validates that the learning loop is functioning.
- **Implementation unit tests:** For custom layers, loss functions, distance metrics — test expected values against hand-computed results.

These tests run without trained weights. They execute in milliseconds and belong in CI like any software unit test.

## Post-Train Tests: Testing Learned Logic

Post-train tests check whether the model has learned the right things. Inspired by the CheckList framework for NLP behavioral testing, these encode domain knowledge about expected model behavior.

**Invariance tests** assert that predictions are unchanged when you modify features that should not matter. For a survival model, changing a passenger's name or ticket number should not affect survival probability. These tests catch spurious correlations — the model latching onto identifiers rather than signal.

**Directional expectation tests** assert the direction of effect when a meaningful feature changes. On Titanic survival: changing gender from female to male should decrease survival probability; lowering passenger class should lower it further. If these directional relationships are violated, the model has learned something wrong despite good aggregate metrics.

**Evaluation regression tests** set minimum performance thresholds. If accuracy on the test set drops below 82% or AUC below 0.84, the test fails — catching degradation from data changes or implementation updates. These double as guard rails against silent regressions in CI.

**Latency tests** measure training and inference time at the 95th or 99th percentile over many runs. Models consumed by downstream systems often have latency SLAs. Catching a 10x slowdown in CI is far cheaper than discovering it in production under load.

## Guidelines for Unit-Testing ML Models

Several anti-patterns are common in ML unit tests:

**Do not mock the actual model for behavioral tests.** The point of a behavioral test is to verify the learned logic. Mocking a model tests the mock, not the model. Two classifiers can have identical APIs but opposite output label conventions (e.g., Google's T5 NLI uses class=1 for entailment; Meta's BART uses class=2). Only testing against the real model catches this.

**Use random or empty weights for structural tests.** If you only need to check output shapes or that a model can move between CPU and GPU, initialize from config with random weights — no download required. The `transformers` library's `AutoModelForSequenceClassification.from_config(config)` pattern enables this.

**Use small, inline data samples for unit tests.** Loading CSVs or Parquet files couples unit tests to the filesystem and makes them brittle. Define sample data directly in test code so each test is self-contained. Reserve file-based data for integration tests and evaluations.

**Mark slow tests explicitly.** Pytest's `@pytest.mark.slow` (or a custom mark) lets you run fast tests continuously and slow tests only when needed. The tests that load and run real models belong in this category.

## Pipeline Testing: Robustness by Test Granularity

For data and ML pipelines, the key insight is that different test granularities respond differently to pipeline changes:

**Row-level unit tests** are the most robust. They test a single row of input → single output. When new columns or data logic are added to the pipeline, row-level tests for existing functions are typically unchanged. You only add new tests for new functions.

**Schema tests** check that a minimum set of expected columns with correct data types exist at key pipeline junctures. They're robust to data additions (new columns don't break schema tests) and catch breaking changes (removed columns, type changes). These are low-effort, high-value.

**Column/table-level unit tests** and **integration tests** are brittle. They hard-code expected output values over an entire column or table. When upstream data or logic changes, these expected values change — requiring manual updates to every affected test. They're valuable for catching integration bugs but are expensive to maintain and should be used sparingly.

**Property-based testing** (Hypothesis, Pandera) offers a middle path: generate many data inputs according to statistical specifications and assert that outputs satisfy properties rather than exact values. This is more robust to input variation but harder to apply for business-logic assertions like "items are ranked correctly after diversification."

The practical recommendation: lean heavily on row-level unit tests and schema tests, use integration tests sparingly with coarse-grained assertions (number of rows, not specific values), and invest in property-based tests for data preprocessing pipelines.

## CI for ML: What to Automate

A practical ML CI pipeline runs tests in cost-weighted order:

1. **Pre-train tests + row-level unit tests + schema tests** — milliseconds, always run.
2. **Post-train behavioral tests + evaluation regression tests** — seconds to minutes, run on PR.
3. **Model load + latency tests against real weights** — minutes, run pre-merge or nightly.
4. **Full integration tests** — minutes to hours depending on data size, run pre-merge.

The critical test to never skip: **model validation before deployment.** After retraining, hold out a recent validation slice and assert that the new model beats a naive baseline and doesn't regress on key metrics. If validation fails, do not promote the model. A stale model in production is safer than a misbehaving new one.

## Sources

- Yan, Eugene. "How to Test Machine Learning Code and Systems." eugeneyan.com, Sep 2020. https://eugeneyan.com/writing/testing-ml/
- Yan, Eugene. "Don't Mock Machine Learning Models In Unit Tests." eugeneyan.com, Feb 2024. https://eugeneyan.com/writing/unit-testing-ml/
- Yan, Eugene. "Writing Robust Tests for Data & Machine Learning Pipelines." eugeneyan.com, Sep 2022. https://eugeneyan.com/writing/testing-pipelines/
