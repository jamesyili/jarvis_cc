---
concept: Vision-Language Models
tags: [vlm, clip, llava, multimodal, vision-encoder]
sources:
  - kb/hard/raw/aman-ai/primers-vision-language-models.md
  - kb/hard/raw/aman-ai/primers-vlm-architectures.md
  - kb/hard/raw/cameron-wolfe/vision-large-language-models-vllms.md
last_compiled: 2026-04-05
related: [transformer-architecture, large-language-models, diffusion-models, convolutional-neural-networks]
---

# Vision-Language Models

Vision-Language Models (VLMs) extend language models to understand and generate content that spans both images and text. After text-based LLMs demonstrated remarkable capabilities, the key question became: how do you give a language model eyes? The answer is now well-established: encode images into a token-like representation, then feed those tokens into the language model's existing processing pipeline.

VLMs are not actually much different from text-based LLMs structurally — the core LLM architecture is preserved, and visual understanding is achieved by adding a vision encoder and a modality bridge.

## Core Capabilities

VLMs support three task categories:

**Generation tasks**: Visual Question Answering (VQA), image captioning, visual commonsense reasoning, text-to-image generation

**Classification tasks**: Multimodal sentiment analysis, Natural Language Visual Reasoning (NLVR) — does this statement correctly describe this image?

**Retrieval tasks**: Cross-modal search (find images matching a text description), vision-language navigation, multimodal translation

## Architecture Fundamentals

Every VLM has three logical components:

### 1. Vision Encoder
Converts a raw image into a sequence of dense feature vectors. Common choices:
- **CNN backbone** (ResNet): Extract spatial feature maps
- **Vision Transformer (ViT)**: Divide image into fixed patches, project each to an embedding, process with transformer self-attention
- **CLIP visual encoder**: ViT or ResNet pretrained on image-text contrastive learning — the most common starting point because its visual embeddings are already semantically aligned with language

The vision encoder typically produces a set of patch-level embeddings: for a 224×224 image with 16×16 patches, ViT produces 196 patch tokens.

### 2. Modality Bridge (Projection Layer)
The visual tokens from the encoder are in a different space than the LLM's text token embeddings. The bridge projects visual features into the LLM's embedding space.

Three main approaches:

**MLP/Linear Projection**: The simplest approach. A two-layer MLP projects vision encoder output into the LLM input dimension. Used in LLaVA — surprisingly effective, often the first approach to try.

**Q-Former (BLIP-2)**: A 188M-parameter trainable transformer module with two sub-transformers: an image transformer and a text transformer. Key idea: 32 learnable **query embeddings** interact with frozen image features via cross-attention, then with text via self-attention. The Q-Former outputs a fixed 32 tokens regardless of image resolution — a bottleneck that forces extraction of only text-relevant visual information. Initialized from BERTbase weights. Enables use of fully frozen vision encoder + frozen LLM; only Q-Former is trained.

**Perceiver Resampler (Flamingo)**: Similar to Q-Former in purpose. Takes variable-length image/video features and produces a fixed 64 visual tokens via a Transformer with cross-attention. More efficient than a plain MLP or transformer for high-resolution inputs. Enables Flamingo's ability to handle arbitrarily interleaved image-text sequences.

### 3. Language Model (LLM)
A decoder-only transformer (LLaMA, GPT, OPT, FlanT5) that takes the sequence of [visual tokens + text tokens] and autoregressively generates text. The LLM's self-attention mechanism allows any text token to attend to any visual token — the model can ground words in image regions through attention patterns.

**Cross-attention variant (Flamingo)**: Instead of concatenating visual tokens with text tokens, cross-attention layers are interleaved with the frozen LLM's self-attention layers. Text tokens attend to visual features via cross-attention at each layer. Keeps the LLM fully frozen; only the cross-attention layers (and Perceiver Resampler) are trained.

## Modality Fusion Strategies

**Early fusion**: Visual and text features combined before deep processing. DALL-E concatenates image and text tokens and processes them with the same autoregressive transformer.

**Intermediate fusion**: Independent processing, then merging. LLaVA, BLIP-2, and Flamingo all use intermediate fusion — vision encoder processes the image independently, then the bridge projects into the LLM space.

**Late fusion / decision-level**: Both modalities processed deeply before combination. CLIP uses late fusion with separate vision and text encoders, only combining at the final embedding level via dot product similarity.

## Key Models

### CLIP (OpenAI, 2021) — The Foundation
CLIP (Contrastive Language-Image Pretraining) is the most influential VLM building block. It trains a vision encoder and text encoder **jointly using contrastive learning** on 400M image-text pairs scraped from the web.

Training objective: maximize similarity between the (image, text) embedding pairs for matching pairs in a batch; minimize similarity for non-matching pairs. The symmetric loss:
```
# I_e: image embeddings, T_e: text embeddings, both L2-normalized
logits = I_e @ T_e.T * exp(temperature)
loss = (cross_entropy(logits, axis=0) + cross_entropy(logits, axis=1)) / 2
```

CLIP enables zero-shot image classification: encode the query image and a set of label texts ("a photo of a cat", "a photo of a dog"), find the text with highest cosine similarity. No task-specific training required.

Limitations: struggles with abstract concepts, counting, spatial relationships, and novel combinations of known concepts.

CLIP's visual encoder is now the de facto starting point for most modern VLMs.

### ALIGN (Google, 2021)
Same contrastive dual-encoder as CLIP, but trained on **1 billion** noisy image-text pairs without expensive data cleaning. Demonstrates that scale can compensate for noise.

### LLaVA (Liu et al., 2023) — The Open-Source Benchmark
LLaVA (Large Language-and-Vision Assistant) is the most popular open-source VLM framework. Architecture:
- **Vision encoder**: CLIP's ViT (frozen)
- **Bridge**: A lightweight linear projection (MLP) mapping visual features to the LLM embedding space
- **LLM**: LLaMA-series (frozen in pretraining, fine-tuned in instruction tuning)

Training is two-stage:
1. **Alignment pretraining**: Train only the projection layer on image-caption pairs (LLM and vision encoder both frozen). Goal: align visual and language feature spaces.
2. **Instruction fine-tuning**: Fine-tune projection + LLM (CLIP still frozen) on visual instruction-following data generated by GPT-4.

LLaVA achieves 85.1% relative score vs. GPT-4 on a synthetic multimodal instruction dataset. Simple architecture, strong results.

### Flamingo (DeepMind, 2022)
Flamingo handles **interleaved image-text sequences** — a conversation that alternates between images and text naturally. Architecture:
- **Vision encoder**: NFNet (CNN) → Perceiver Resampler → 64 fixed visual tokens
- **Bridge**: Cross-attention layers interleaved with frozen LLM self-attention layers
- **LLM**: Chinchilla-based, frozen

Key capability: in-context few-shot learning for vision tasks. Show the model 4 examples of (image, answer) pairs in context, then query — it generalizes immediately. Few-shot Flamingo 80B surpasses fine-tuned models trained on thousands of times more task-specific data on several benchmarks.

### BLIP-2 (Salesforce, 2023)
BLIP-2 uses Q-Former to bridge a frozen CLIP encoder and a frozen LLM (OPT or FlanT5). The frozen components mean BLIP-2 is computationally efficient — only the Q-Former trains. Two-stage training:
1. Vision-language representation learning (Q-Former + frozen image encoder)
2. Vision-to-language generative learning (Q-Former + frozen LLM)

Enables **zero-shot instructed image-to-text generation** without end-to-end fine-tuning of the large components.

### Florence (Microsoft, 2021)
Florence is a foundation model covering the full range of VL tasks. Key choices:
- **Vision encoder**: Swin Transformer (hierarchical, handles multi-scale features)
- **Language**: Modified CLIP as decoder
- **Training data**: Image-label-description triplets
- **Fine-grained adaptation**: Task-specific "adapter" models for object-level, VL, and video representations

Achieves strong zero-shot and few-shot performance across diverse tasks.

## Training Paradigms

**Contrastive pretraining** (CLIP, ALIGN): Train encoders to align matching image-text pairs in a shared embedding space. Best for retrieval and zero-shot classification.

**Masked prediction** (BERT-style VLMs): Mask image regions or text tokens; predict the masked content. VisualBERT, VL-BERT, UNITER use combinations of:
- Masked Language Modeling
- Image-Text Matching
- Masked Region Classification
- Word-Region Alignment

**Autoregressive generation** (LLaVA, Flamingo, PaLI): Next-token prediction on interleaved image-text sequences. Naturally supports generation tasks (VQA, captioning, instruction following).

## Fine-Tuning Strategies

When adapting a pretrained VLM to a specific task:

**What to freeze vs. train**:
- **Vision encoder**: Freeze unless target visual domain differs substantially from pretraining data (e.g., medical or satellite imagery)
- **LLM layers**: Fine-tune when task involves domain-specific language (technical jargon, legal text)
- **Projection/bridge layers**: Almost always fine-tune — these need to adapt to the task's alignment requirements

**Common strategies**:
- Full fine-tuning (all layers): Most thorough, most expensive
- Partial fine-tuning: Freeze lower layers (general features), fine-tune upper + bridge
- Adapter-based: Insert small trainable modules; original weights unchanged. Parameter-efficient.
- **LoRA**: Low-rank adaptation — insert trainable low-rank matrices into attention layers. Works on any layer component. Dramatically reduces trainable parameters while preserving quality.

## Visual Encoding: Beyond CNNs

Text encoding is relatively solved — transformers work well. Visual encoding remains active research:

- **CNN features** (Faster R-CNN regions): Detect salient objects and attributes; extract region-level features. Used by VinVL, which pretrained a dedicated object-attribute detection model on four public datasets.
- **Patch embeddings** (ViT): Divide image into fixed patches, process as a sequence. SimVLM replaces patch projection with 3 ResNet blocks for richer low-level encoding.
- **Discrete latent codes** (DALL-E dVAE): Compress image patches into discrete tokens — analogous to a vocabulary for images.

The key trend: visual encoders are getting larger, hierarchical (multi-scale), and increasingly pretrained with language supervision (CLIP, SigLIP).

## Multimodal Alignment Challenge

The central technical challenge of VLMs is **semantic alignment**: ensuring that visual features and language features referring to the same concept are close in the shared embedding space. This is non-trivial because:

- Visual features are continuous, spatial, and redundant
- Language tokens are discrete, sequential, and compositional
- The mapping between pixels and words is many-to-many and context-dependent

Contrastive learning with paired data (CLIP) is currently the strongest approach to alignment. The Q-Former and Perceiver Resampler are architectural solutions to extract the textually-relevant subset of visual information, discarding irrelevant spatial detail.

## Sources

- Aman Chadha, [Vision Language Models](https://aman.ai/primers/ai/vision-language-models/)
- Aman Chadha, [VLM Architectures](https://aman.ai/primers/ai/VLM/)
- Cameron Wolfe, [Vision Large Language Models (vLLMs)](https://cameronrwolfe.substack.com/p/vision-llms)
