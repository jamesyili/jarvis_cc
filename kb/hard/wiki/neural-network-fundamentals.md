---
concept: Neural Network Fundamentals
tags: [neural-networks, activation, backpropagation, fundamentals]
sources:
  - kb/hard/raw/aman-ai/primers-activation-functions.md
  - kb/hard/raw/aman-ai/primers-backprop-guide.md
  - kb/hard/raw/aman-ai/primers-gradient-descent-and-backprop.md
  - kb/hard/raw/aman-ai/cs231n-neural-networks-part-1-setting-up-the-architecture.md
  - kb/hard/raw/aman-ai/primers-ai.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/neural-network-training|Neural Network Training]]"
  - "[[hard/wiki/regularization|Regularization]]"
  - "[[hard/wiki/optimization-algorithms|Optimization Algorithms]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 0  # not obviously relevant
knowledge_updated: 2026-09-07
---

# Neural Network Fundamentals

Neural networks are computational models loosely inspired by biological neurons. Their power comes not from any single idea but from the combination of: hierarchical feature learning, non-linear activation, and gradient-based weight updates. This article covers the architectural foundations — from the perceptron to deep MLPs — and the mechanisms that make them trainable.

## From Perceptron to MLP

The **perceptron** is the simplest neural unit: it takes a weighted sum of inputs, adds a bias, and applies a threshold. A single perceptron can only learn linearly separable functions. Stacking perceptrons into layers — forming a **Multi-Layer Perceptron (MLP)** — unlocks the ability to learn arbitrary non-linear mappings, provided each layer applies a non-linear activation.

An MLP with L layers computes:

```
z[l] = W[l] · a[l-1] + b[l]
a[l] = f(z[l])
```

where `f` is an activation function, `W[l]` are weight matrices, and `b[l]` are bias vectors. The key insight is that without non-linearity between layers, any deep network collapses to a single linear transformation — the activation function is what gives depth its meaning.

**Hidden layers** create intermediate representations. Each neuron in a hidden layer acts as a feature detector, responding to particular patterns in the preceding layer's activations. The final layer produces the output — class logits, regression values, or embeddings depending on the task.

## Activation Functions

Activation functions introduce non-linearity. The choice of activation has significant practical consequences for training stability, gradient flow, and representational power.

**Sigmoid** squashes input to (0, 1) and is interpretable as a probability:
`σ(x) = 1 / (1 + e^{-x})`
It saturates at both extremes, which causes **vanishing gradients** in deep networks — gradients near 0 or 1 are nearly zero, blocking weight updates in earlier layers.

**Tanh** centers outputs around zero (range: −1 to 1), making it preferable to sigmoid for hidden layers in practice, but it still suffers from saturation and vanishing gradients.

**ReLU (Rectified Linear Unit)** is the dominant modern choice for hidden layers:
`ReLU(x) = max(0, x)`
It avoids vanishing gradients for positive inputs and is computationally cheap. The downside is the **dead neuron problem**: neurons whose pre-activation is consistently negative receive zero gradient and stop learning permanently.

**Leaky ReLU** addresses dead neurons by allowing a small negative slope (typically 0.01) for negative inputs, ensuring gradient flow even when the neuron is inactive. The slope is a hyperparameter, not learned.

**ELU (Exponential Linear Unit)** goes further — it produces negative outputs for negative inputs via an exponential term, allowing the network to "nudge" weights in both directions. More expressive than Leaky ReLU but more expensive to compute.

**SELU (Scaled ELU)** is self-normalizing: with LeCun Normal initialization, activations converge toward zero mean and unit variance across layers without explicit batch normalization. This is powerful for sequential architectures but requires careful setup (LeCun initialization + Alpha Dropout).

**GELU (Gaussian Error Linear Unit)** weights inputs by their probability of being greater than zero under a Gaussian distribution. It is the standard in modern transformer models (BERT, GPT) and outperforms ReLU on NLP benchmarks. Smooth everywhere, avoids the dead neuron issue, and empirically strong on language tasks.

**SiLU (Sigmoid Linear Unit)**, also known as Swish, is defined as `x · σ(x)`. Smooth and non-monotonic, it has shown strong empirical performance in vision and language models. Like GELU, it lacks a sharp zero threshold.

**Softmax** is not a hidden-layer activation but an output activation for multi-class classification. It maps a vector of logits to a probability distribution summing to 1:
`softmax(s_i) = exp(s_i) / Σ_j exp(s_j)`

**Practical selection guide:**
- Default hidden layers: ReLU or GELU
- Transformers: GELU or SiLU
- Binary classification output: sigmoid
- Multi-class output: softmax
- Self-normalizing deep networks: SELU (with careful init)

## Backpropagation

Backpropagation is the algorithm that computes the gradient of the loss with respect to every weight in the network. It is not a separate optimization algorithm — it is the mechanism for computing gradients, which an optimizer like SGD or Adam then uses to update weights.

**Conceptually:** backprop applies the chain rule of calculus backward through the computational graph of the network. Each node in the graph stores its output from the forward pass and its local gradient contribution. During the backward pass, gradients flow from the loss back through every operation.

**The chain rule** for a composite function `f(g(x))`:
`d/dx[f(g(x))] = f'(g(x)) · g'(x)`

In a network, the gradient of the loss L with respect to a weight W in layer l is:
`∂L/∂W[l] = ∂L/∂z[l] · ∂z[l]/∂W[l]`

where `∂L/∂z[l]` (called delta) is propagated backward from the output using the chain rule across all subsequent layers.

**Non-differentiability** at points like ReLU's zero is handled via subgradients — the gradient is conventionally set to 0 (or sometimes 1) at exactly x=0, and this approximation works well in practice.

**Computational graphs** make backprop systematic. Modern frameworks (PyTorch, JAX) build the graph dynamically during the forward pass and then traverse it in reverse. This abstraction allows arbitrary architectures to be trained without hand-deriving gradients.

**Forward pass** (stores intermediate activations):
```
Z = W1·X + b1
A = σ(Z)
ŷ = w2·A + b2
L = (1/m)||ŷ - y||²
```

**Backward pass** (computes gradients via chain rule):
```
∂L/∂W1 = (w2ᵀ · (2/m)(ŷ - y) ⊙ A ⊙ (1 - A)) · Xᵀ
```

The key insight from Karpathy: backprop is a **leaky abstraction**. Bugs in network architecture often manifest as pathological gradients — vanishing, exploding, or wrong signs. Understanding backprop lets you diagnose training failures rather than blindly stacking layers and hoping the optimizer "figures it out."

## Weight Initialization

Poor initialization can cause gradients to vanish or explode from layer 1 of training. The goal is to keep the variance of activations stable across layers.

**Xavier (Glorot) Initialization** is designed for sigmoid and tanh activations. It sets weight variance to `1/n`, where n is the number of inputs to the layer:
`W ~ N(0, 1/n_in)` or uniform over `[-√(6/(n_in + n_out)), +√(6/(n_in + n_out))]`

This keeps the variance of inputs and outputs roughly equal, preventing signal amplification or attenuation.

**He Initialization** is designed for ReLU networks. Because ReLU kills half the inputs (the negatives), it compensates by doubling the variance:
`W ~ N(0, 2/n_in)`

In PyTorch: `torch.nn.init.kaiming_normal_(weight, mode='fan_in', nonlinearity='relu')`

**LeCun Initialization** (`1/n_in`) is designed for SELU activations and is a prerequisite for self-normalization.

**Zero initialization** for biases is standard and safe. **Never initialize all weights to zero** — all neurons would compute the same function and gradients would be identical, breaking symmetry.

## The Vanishing/Exploding Gradient Problem

In deep networks (many layers), gradients are multiplied together across layers during backprop. If the weight matrices are slightly larger than identity, gradients **explode** exponentially with depth. If slightly smaller, they **vanish** exponentially — earlier layers receive nearly zero gradient and learning stalls.

Partial mitigations:
- Proper initialization (Xavier, He)
- Non-saturating activations (ReLU, GELU instead of sigmoid)
- Batch normalization
- Residual/skip connections (used in ResNets and Transformers)
- Gradient clipping (for exploding gradients in RNNs)

## Putting It Together

A well-functioning MLP requires all these pieces working together: sensible architecture (depth/width appropriate to the task), non-saturating activations, careful weight initialization, a meaningful loss function, and a gradient-based optimizer. Backpropagation ties it all together by efficiently computing gradients. The modular nature of computational graphs means these principles compose — whether the "network" is a 3-layer MLP or a 100-layer ResNet, the same machinery applies.

---

## Sources

- Aman Chadha, "Primers: Activation Functions," aman.ai, 2026-04-05
- Aman Chadha, "Primers: Backprop Guide," aman.ai, 2026-04-05
- Aman Chadha, "Primers: Gradient Descent and Backprop," aman.ai, 2026-04-05
- Aman Chadha, "CS231n: Neural Networks Part 1 — Setting Up the Architecture," aman.ai
- Aman Chadha, "Coursera-DL: Improving Deep Neural Networks," aman.ai, 2026-04-05
