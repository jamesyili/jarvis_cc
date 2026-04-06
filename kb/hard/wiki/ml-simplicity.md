---
concept: ML Simplicity First
tags: [simplicity, heuristics, baselines, ml-first-rule]
sources:
  - kb/hard/raw/eugene-yan/the-first-rule-of-machine-learning-start-without-machine-learning.md
  - kb/hard/raw/eugene-yan/simplicity-is-an-advantage-but-sadly-complexity-sells-better.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/ml-system-design-framework|ML System Design Framework]]"
  - "[[hard/wiki/ml-production-maintenance|ML Production Maintenance]]"
---

# ML Simplicity First

There is a persistent and pernicious bias in ML practice: complexity signals value. Papers with more components get better reviews. Systems with more moving parts look more impressive. Engineers who build elaborate pipelines receive more credit than engineers who solve the same problem with a SQL query. This bias is expensive, and resisting it is one of the highest-leverage skills in applied ML.

## The First Rule of Machine Learning

> "Don't be afraid to launch a product without machine learning." — Google's Rule #1 of ML

The first rule of machine learning is: start without machine learning.

This sounds paradoxical. But the logic is sound. ML requires data, and to get good data you need to understand the problem. To understand the problem you need to build something. The fastest way to build something is with heuristics. If a heuristic gets you 50% of the way to your ML ceiling, and ML will take three months to build and deploy, the right order is: heuristic first, ML when the heuristic becomes unmaintainable or insufficient.

The corollary from Google: "A simple heuristic can get your product out the door. A complex heuristic is unmaintainable. Once you have data and a basic idea of what you are trying to accomplish, move on to machine learning — you will find that the machine-learned model is easier to update and maintain." The inflection point is not when ML is possible, but when the heuristic has become complex enough that ML is actually simpler.

## What to Start With Instead

Before writing any model code, explore the data. Simple correlations reveal feature-target relationships. Scatter plots expose nonlinear relationships that correlation statistics miss (e.g., ice cream sales increase with temperature up to a threshold, then decline — zero correlation, obvious nonlinearity). Box plots clarify the signal in categorical features.

With data understanding in hand, build heuristics:

- **Recommendations:** Recommend the top-performing items from the previous period, optionally segmented by category. Co-occurrence statistics on user interactions give item-to-item recommendations without any model training.
- **Classification:** Regex-based rules on structured text fields. Walmart's product classifier started with rules like "if title contains 'ring', 'wedding band', 'diamond.*bridal' → classify as ring category."
- **Anomaly/spam detection:** Rules based on volume (reviews per IP per day), timing (3am submissions), or similarity (edit distance to other reviews from the same day).
- **Forecasting:** Moving averages, seasonal adjustments, simple exponential smoothing.

These are not placeholder approaches. They are often embarrassingly competitive with ML on real problems. An exclusion list stopped scammers when a model couldn't. String comparisons beat a customer's requested neural network solution — and were faster and cheaper to maintain.

**Heuristics also bootstrap labels.** If you have no labeled data, heuristics can serve as labeling functions for weak supervision. Formalizing a regex rule as a labeling function generates thousands of approximate labels instantly. This is how you get from zero labeled data to a trainable model, without requiring a costly hand-labeling campaign upfront.

## When to Introduce ML

Three conditions suggest ML is the right next step:

1. You have a non-ML baseline that works reasonably well, and it's starting to break down — maybe you have 195 handcrafted rules and updating any one of them breaks others.
2. You have robust data pipelines and high-quality labels. Without clean data and valid labels, ML will underperform the heuristic it's meant to replace.
3. The problem has a clear metric, and the baseline doesn't move that metric sufficiently.

The presence of good labels is particularly important. If you're trying to reduce fraud but don't know how fraud looks in your data and have no labels, building an ML system is premature. Manually labeling a golden dataset first is not optional — it's what makes the ML effort meaningful.

## Why Complexity Sells (And Why That's a Problem)

Dijkstra: "Simplicity is a great virtue but it requires hard work to achieve it and education to appreciate it. And to make matters worse: complexity sells better."

Complexity sells for four reasons:

1. **It signals effort.** A system with many components looks harder to build. Harder implies more worthy.
2. **It signals mastery.** If laypeople can't understand it, the creator must be an expert.
3. **It signals innovation.** Systems built from scratch are perceived as more inventive than systems that reuse existing components.
4. **It signals completeness.** More features, more configurability, more lego blocks — complex systems appear to cover more bases.

Each of these is a bias, not a truth. The result is **complexity bias**: systematically overvaluing complex solutions and undervaluing simple ones. This leads to incentive distortions: engineers gold-plate systems to demonstrate depth, papers get rejected because the method is "too simple," and promotions go to people who built elaborate solutions to problems that had simpler answers.

## Why Simplicity Is Actually the Advantage

The empirical record on simple vs. complex in ML:

- Tree-based models outperform deep neural networks on 45 mid-sized tabular datasets.
- Greedy algorithms beat graph neural networks on combinatorial graph problems.
- Simple averaging matches or exceeds complex multi-task optimization methods.
- Simple methods dominate forecasting accuracy across 32 papers.
- Dot product beats neural collaborative filtering for item recommendation and retrieval.

Beyond empirical performance, simple systems have structural advantages:

**Simpler systems are easier to understand and test.** Fewer components mean fewer interaction effects to reason about. Tests are easier to write because there's less to isolate.

**Simpler systems are cheaper to maintain.** The bulk of a system's lifetime cost comes after deployment, often paid by engineers who didn't build it. Simple systems have fewer failure modes, are easier to debug, and are easier to hand off.

**Simpler systems survive longer.** Instagram served tens of millions of users with 13 engineers in 2012 by sticking to PostgreSQL and Redis while competitors struggled with trendy NoSQL datastores. Proven, boring technology outlasts the hype cycle.

**Simpler systems are easier to swap.** If your model is a simple logistic regression behind a clean API, replacing it with a neural network is a localized change. If your model is entangled with 15 preprocessing steps and 6 downstream consumers, replacement is a migration project.

## The Right Mental Model

The objective is to solve complex problems with the simplest possible solutions — not to build simple solutions to simple problems. A simple solution to a complex problem demonstrates genuine insight. It means you understood the problem well enough to see what was essential and what was accidental complexity.

The heuristic check: given the cost of the complexity you're about to add, is the juice worth the squeeze? If adding a neural network over a decision tree will take three months, require a new serving infrastructure, and yield a 0.5% lift — probably not. If the same investment yields a 20% lift on your primary metric — probably yes.

Occam's Razor applied to ML engineering: the simplest solution that adequately solves the problem is the right starting point. Complexity should be earned, not assumed.

## Sources

- Yan, Eugene. "The First Rule of Machine Learning: Start without Machine Learning." eugeneyan.com, Sep 2021. https://eugeneyan.com/writing/first-rule-of-ml/
- Yan, Eugene. "Simplicity is An Advantage but Sadly Complexity Sells Better." eugeneyan.com, Aug 2022. https://eugeneyan.com/writing/simplicity/
