---
concept: Sequence Models (RNN/LSTM/SSM)
tags: [rnn, lstm, gru, sequence-models, ssm, mamba]
sources:
  - kb/hard/raw/aman-ai/coursera-dl-sequence-models.md
  - kb/hard/raw/aman-ai/primers-state-space-models.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/transformer-architecture|Transformer Architecture]]"
  - "[[hard/wiki/large-language-models|Large Language Models]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Sequence Models (RNN/LSTM/SSM)

Before transformers dominated NLP, sequence modeling was the domain of recurrent neural networks. RNNs, LSTMs, and GRUs were the workhorse architectures for language modeling, machine translation, and speech recognition from the mid-2010s through the transformer's rise in 2017. State space models (SSMs) represent a newer lineage — rooted in control theory rather than neuroscience — that offers transformer-competitive performance with linear-time inference. Understanding all three generations is essential for grasping both the history and the current frontier of sequence modeling.

## Vanilla RNN

A recurrent neural network processes sequences by maintaining a hidden state that is updated at each time step. Given input x_t and previous hidden state h_{t-1}:

```
h_t = tanh(W_hh * h_{t-1} + W_xh * x_t + b_h)
y_t = W_hy * h_t + b_y
```

The same weight matrices are reused at every time step — this parameter sharing is what gives RNNs their ability to generalize across sequence positions. In principle, this allows information from early in the sequence to influence later predictions; in practice, vanilla RNNs fail at this. During backpropagation through time (BPTT), gradients are multiplied through the recurrence at each step. When the sequence is long, gradients either vanish (become negligible) or explode (grow unbounded). The vanishing gradient problem makes vanilla RNNs unable to learn dependencies spanning more than ~10 steps, which is fatal for most real language tasks.

## LSTM: Long Short-Term Memory

LSTMs (Hochreiter & Schmidhuber, 1997) solve the vanishing gradient problem with a dedicated memory cell and a gating mechanism that controls what information to store, discard, and output.

The LSTM maintains two recurrent states: the hidden state h_t (short-term memory, output at each step) and the cell state c_t (long-term memory, the linear "highway" through time).

Three gates govern the cell state:

**Forget gate** — what to erase from cell memory:
```
f_t = σ(W_f * [h_{t-1}, x_t] + b_f)
```

**Input gate + candidate update** — what new information to write:
```
i_t = σ(W_i * [h_{t-1}, x_t] + b_i)
c̃_t = tanh(W_c * [h_{t-1}, x_t] + b_c)
```

**Cell state update** — combine forget and input:
```
c_t = f_t ⊙ c_{t-1} + i_t ⊙ c̃_t
```

**Output gate** — what to expose as hidden state:
```
o_t = σ(W_o * [h_{t-1}, x_t] + b_o)
h_t = o_t ⊙ tanh(c_t)
```

The key insight is the cell state update: gradients can flow through c_t with multiplication by f_t (which ranges 0–1 per element) rather than through the tanh nonlinearity. When forget gates are near 1, gradients pass almost unchanged over many steps — solving vanishing gradients for the memory path. LSTMs can reliably model dependencies spanning hundreds of steps.

## GRU: Gated Recurrent Unit

The GRU (Cho et al., 2014) simplifies the LSTM by merging the cell state and hidden state into a single h_t and reducing to two gates:

**Reset gate** — how much to ignore the past:
```
r_t = σ(W_r * [h_{t-1}, x_t])
```

**Update gate** — interpolation between old and new state:
```
z_t = σ(W_z * [h_{t-1}, x_t])
```

**Candidate activation** (reset gate applied to past):
```
h̃_t = tanh(W * [r_t ⊙ h_{t-1}, x_t])
```

**Final hidden state** (linear interpolation):
```
h_t = (1 - z_t) ⊙ h_{t-1} + z_t ⊙ h̃_t
```

The update gate acts as both forget and input gates simultaneously. When z_t ≈ 0, the GRU carries the old state forward unchanged. When z_t ≈ 1, it replaces the state with the new candidate. GRUs have fewer parameters than LSTMs and train faster, with comparable performance on most tasks. They are preferred when compute is constrained or when sequences don't require the full expressivity of separate cell and hidden states.

## Bidirectional RNNs and Deep RNNs

**Bidirectional RNNs (BRNNs)** run two independent RNNs in opposite directions over the input sequence and concatenate their outputs. The forward pass captures left-to-right context; the backward pass captures right-to-left. This doubles the effective context at each position and significantly improves performance on classification and tagging tasks where the full input is available. BRNNs cannot be used for autoregressive generation (the backward pass requires future tokens).

**Deep RNNs** stack multiple recurrent layers, where the output sequence of layer l becomes the input to layer l+1. Depth adds representational capacity similar to depth in feedforward networks — higher layers can learn more abstract temporal patterns. In practice, 2–4 layers of stacked LSTM/GRU is the common configuration for strong sequence-to-sequence models.

## Sequence-to-Sequence and Attention

The encoder-decoder (seq2seq) architecture, introduced by Sutskever et al. (2014) and Cho et al. (2014), uses one RNN to encode an input sequence into a fixed-size context vector and a second RNN to decode that vector into an output sequence. This enabled neural machine translation: the encoder processes a French sentence and compresses it to a vector; the decoder generates the English translation one token at a time.

The fixed-size bottleneck proved limiting for long sequences — too much information was compressed into a single vector. **Attention** (Bahdanau et al., 2015) solved this by allowing the decoder to dynamically attend to different encoder hidden states at each decoding step. Instead of a single context vector, the decoder computes a weighted sum over all encoder outputs, with weights determined by the alignment between the decoder's current state and each encoder position.

This attention mechanism — soft alignment between two sequences — was the direct conceptual precursor to the self-attention in transformers. See [[hard/wiki/transformer-architecture|Transformer Architecture]] for the full development.

## State Space Models (SSMs)

State space models represent a fundamentally different approach to sequence modeling. Rooted in control theory, an SSM describes how a latent state h(t) evolves given inputs u(t):

```
h'(t) = A * h(t) + B * u(t)
y(t)  = C * h(t) + D * u(t)
```

The matrices A, B, C, D define the dynamics. For sequence modeling, the key insight is that SSMs can be computed in two equivalent modes:
- **Recurrent mode** at inference: O(1) state per step, like an RNN, giving constant memory and linear-time inference
- **Convolutional mode** at training: unroll into a global convolution, which can be parallelized efficiently using FFT

This duality makes SSMs attractive: they combine the training efficiency of convolutions (like transformers) with the inference efficiency of recurrences (like RNNs) — without the quadratic attention cost.

**S4** (Structured State Spaces, Gu et al. 2022) introduced a parameterization of A using a special HiPPO matrix that provably captures long-range dependencies. S4 achieved state-of-the-art on the Long Range Arena benchmark, including tasks with 16K-step dependencies where transformers fail outright.

**Mamba** (Gu & Dao, 2023) extended S4 with input-dependent (selective) SSM parameters. In classical SSMs, A, B, C are fixed matrices — the same dynamics apply to every input. Mamba makes these parameters functions of the input, enabling content-based reasoning (selectively retain or discard information based on what the content is, not just temporal position). The selection mechanism connects directly to LSTM gates: like a forget gate, it lets the model flush irrelevant state when it encounters a boundary signal.

Mamba achieves linear scaling in sequence length and approximately 5x higher throughput than transformers at equivalent parameter count, while matching or exceeding transformer performance on language, audio, and genomics benchmarks. A hardware-aware parallel algorithm enables GPU-efficient training despite the input-dependent parameters breaking the standard convolution path.

**Hybrid architectures** like Jamba (AI21, 2024) and SAMBA interleave Mamba and attention layers. The rationale: SSM layers efficiently compress long context into the recurrent state; attention layers provide precise recall of specific past tokens. A small fraction of attention layers (e.g., 1 in 8 in Jamba) dramatically improves exact retrieval tasks with minimal throughput cost.

## Transformers vs. SSMs: The Current Tradeoff

Transformers have quadratic O(n²) time complexity in sequence length; SSMs achieve O(n). For sequences under ~4K tokens, transformers are faster in practice due to highly optimized FlashAttention kernels. Beyond 4K–8K tokens, SSMs' linear scaling becomes decisive. The KV cache in transformers grows linearly with sequence length (a separate constraint); SSMs have constant state size regardless of sequence length.

As of 2025, SSMs have not fully displaced transformers. Pure SSMs struggle at exact retrieval tasks where specific tokens from long history need to be recalled verbatim — the compressed recurrent state loses precise positional information. Hybrid architectures are the current consensus bet: most of the layers are SSM for efficiency, with sparse attention for retrieval.

The transformer's long-range domination reflects FlashAttention's engineering maturity more than architectural superiority. SSMs are a credible challenger for long-context and streaming applications. See [[hard/wiki/large-language-models|Large Language Models]] for how SSM-hybrid architectures are appearing in production model families (Qwen3, Jamba).

## Sources

- Aman.ai: Coursera DL Sequence Models — RNN, GRU gate equations, LSTM cell state math, BRNN, deep RNNs, seq2seq + beam search
- Aman.ai: Primers — State Space Models — S4, Mamba selective SSMs, O(n) vs O(n²) complexity, Jamba hybrid, SAMBA
