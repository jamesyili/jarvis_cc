---
concept: Diffusion Models
tags: [diffusion, ddpm, stable-diffusion, text-to-image, latent-diffusion]
sources:
  - kb/hard/raw/lilian-weng/what-are-diffusion-models.md
  - kb/hard/raw/jay-alammar/the-illustrated-stable-diffusion.md
  - kb/hard/raw/aman-ai/primers-diffusion-models.md
last_compiled: 2026-04-05
related: [generative-adversarial-networks, vision-language-models, convolutional-neural-networks]
---

# Diffusion Models

Diffusion models are the dominant paradigm for high-fidelity generative modeling. They generate images (and audio, video, 3D, and more) by learning to reverse a gradual noise-addition process. Unlike GANs, they train with stable regression-style objectives. Unlike VAEs, they don't require restrictive architectural constraints. The result is a framework that combines strong sample quality, probabilistic interpretability, and reliable scaling behavior.

## The Core Idea

**The central insight**: destroying information (adding noise to an image) is easy and mathematically well-defined. If you can learn to reverse that destruction step-by-step, you can generate new images by starting from pure noise and denoising toward realistic images.

Training creates a dataset of (noisy image, noise amount) pairs automatically — take any training image, add a controlled amount of Gaussian noise, and you have a training example. The model learns to predict the noise that was added (noise prediction) or equivalently, the clean image underlying the noise.

Inference runs this process backward: start from pure Gaussian noise, repeatedly apply the learned denoising function for T steps (typically 50–1000), gradually refining toward a coherent image.

## Forward Diffusion Process (Noising)

The forward process defines a Markov chain that gradually corrupts data with Gaussian noise over T timesteps:

```
q(x_t | x_{t-1}) = N(x_t; sqrt(α_t) * x_{t-1}, (1 - α_t) * I)
```

Where `α_t` is the noise schedule — a sequence of values controlling how much noise is added at each step. The key mathematical convenience: given the original image `x_0`, you can directly sample the noisy version at any timestep t without stepping through all intermediate steps:

```
q(x_t | x_0) = N(x_t; sqrt(ᾱ_t) * x_0, (1 - ᾱ_t) * I)
```

where `ᾱ_t = ∏_{i=1}^{t} α_i`. As t → T, `ᾱ_t → 0` and the distribution approaches a standard normal N(0, I). This "reparameterization trick" is what makes training efficient — any step of noisy data can be sampled in one operation.

## Reverse Diffusion Process (Denoising)

The reverse process is what the model learns. At each step t, given `x_t`, predict `x_{t-1}`:

```
p_θ(x_{t-1} | x_t) = N(μ_θ(x_t, t), Σ_θ(x_t, t))
```

In practice, the neural network `ε_θ` is parameterized to **predict the noise** `ε` that was added, rather than directly predicting `x_{t-1}`. The denoised estimate is then:

```
x_0_hat = (x_t - sqrt(1 - ᾱ_t) * ε_θ(x_t, t)) / sqrt(ᾱ_t)
```

This noise prediction parameterization (Ho et al., 2020) turns the variational lower bound training objective into a simple MSE loss:

```
L_simple = E_{t, x_0, ε} [ || ε - ε_θ(sqrt(ᾱ_t)*x_0 + sqrt(1-ᾱ_t)*ε, t) ||² ]
```

A model trained to minimize this loss learns a principled probabilistic generative model, even though the training looks like regression.

## DDPM vs. DDIM

### DDPM (Denoising Diffusion Probabilistic Models — Ho et al., 2020)
- Stochastic reverse process: each denoising step adds noise back in a controlled way, maintaining the Markov property
- Requires 1000 steps for high-quality generation (slow at inference)
- Produces diverse outputs due to stochasticity
- Gold standard for quality

### DDIM (Denoising Diffusion Implicit Models — Song et al., 2020)
- Deterministic reverse process: given the same initial noise, always produces the same image
- Can use 50–100 steps with minimal quality loss vs. DDPM's 1000
- Enables meaningful latent space interpolation: interpolating between starting noise vectors produces smooth transitions in image space
- Tradeoff: slightly less diversity

## Noise Schedule

The noise schedule controls the signal-to-noise ratio at each timestep:

- **Linear schedule** (original DDPM): `β_t` linearly increases from 0.0001 to 0.02. Works well for 256×256 images but over-destroys information for larger resolutions.
- **Cosine schedule** (improved DDPM): Signal degrades more gradually; better quality for high-resolution generation.
- **Learned schedules**: Some models learn optimal schedules jointly with the denoising network.

## Latent Diffusion Models (LDM) — Stable Diffusion

Running diffusion directly on pixel images is slow: a 512×512×3 image has ~800K dimensions. **Latent diffusion** (Rombach et al., 2022 — the Stable Diffusion paper) moves the diffusion process into a compressed latent space.

**Three-component architecture of Stable Diffusion**:

1. **CLIP Text Encoder**: Converts input text prompt into 77 token embeddings × 768 dimensions. This is the CLIP text encoder (a transformer language model), not fine-tuned.

2. **UNet + Scheduler (in latent space)**: The actual diffusion process. Operates on a compressed latent tensor of shape (4, 64, 64) instead of the full pixel image (3, 512, 512) — a 48× reduction in dimensions. Runs for 50–100 steps. Takes the text embeddings as conditioning via cross-attention.

3. **VAE Decoder**: Decodes the final latent tensor back to pixel space. Runs only once at the end. The VAE encoder is used during training to compress images into the latent space.

The latent space compression is what makes Stable Diffusion fast enough for practical use — the expensive iterative denoising runs in a small latent space, with only a single VAE decode at the end.

**Training the latent diffusion model**:
- Encode all training images to latent space with the VAE encoder (frozen after VAE training)
- Train the UNet noise predictor on these latent representations
- Condition on CLIP text embeddings via cross-attention in the UNet

## Classifier-Free Guidance (CFG)

Classifier-free guidance enables strong text-to-image conditioning without a separate classifier network.

**The problem**: An unconditional diffusion model generates diverse but uncontrolled images. A naive conditional model follows the text prompt but may generate bland, low-variation outputs.

**The solution** (Ho & Salimans, 2022):
- During training, randomly drop the text condition 10–20% of the time (unconditional training). The model learns both `ε_θ(x_t)` and `ε_θ(x_t | c)`.
- At inference, blend both predictions:

```
ε_guided = ε_θ(x_t) + w * (ε_θ(x_t | c) - ε_θ(x_t))
```

The **guidance scale `w`** (often called CFG scale, default 7–12) controls the tradeoff:
- Low w: diverse but may not match prompt
- High w: closely matches prompt but can over-saturate, lose realism

Benefits: no external classifier needed, single model handles both conditional and unconditional generation, simple to implement.

## UNet Architecture for Diffusion

The noise predictor in most pixel-space and latent-space diffusion models is a **UNet**:

- **Encoder path**: Progressively downsamples spatial resolution while increasing channel depth (Conv → ResNet blocks → Self-attention → MaxPool)
- **Decoder path**: Progressively upsamples with transposed convolutions
- **Skip connections**: Connect encoder layers to their symmetric decoder layers — the key feature that preserves spatial detail during reconstruction (see [[hard/wiki/convolutional-neural-networks|CNNs]])
- **Timestep conditioning**: The current denoising step t is embedded and injected into each ResNet block (via AdaGN or FiLM-style modulation)
- **Text conditioning**: Cross-attention in middle and decoder blocks — Query from image features, Key/Value from CLIP text embeddings

This architecture is ideal for diffusion: the encoding path compresses global context, the decoding path reconstructs spatial detail, and skip connections ensure no spatial information is lost.

## Diffusion Transformer (DiT)

Recent work (Peebles & Xie, 2022) replaces the UNet with a pure transformer backbone:

- Patchify the latent image into tokens
- Process with standard transformer blocks (with adaLN conditioning for timestep and class)
- Unpatchify to reconstruct the denoised latent

DiT scales more cleanly than UNet with model size (transformer scaling laws apply). DiT-XL achieves state-of-the-art FID scores on ImageNet. Used in Stable Diffusion 3, FLUX, and other next-generation models.

## Text-to-Image Pipeline

End-to-end Stable Diffusion inference:

1. Tokenize and encode text prompt → 77 × 768 text embeddings via CLIP text encoder
2. Sample random Gaussian noise tensor: shape (4, 64, 64)
3. For t = T down to 1 (e.g., 50 DDIM steps):
   - UNet takes (noisy latent, t, text embeddings) → predicted noise
   - Apply CFG: blend unconditional and conditional predictions with guidance scale
   - Scheduler computes `x_{t-1}` from `x_t` and predicted noise
4. VAE decoder converts final latent (4, 64, 64) → pixel image (3, 512, 512)

## Comparison to Prior Generative Models

| | GANs | VAEs | Flow Models | Diffusion |
|--|------|------|-------------|-----------|
| Training stability | Unstable (mode collapse) | Stable | Stable | Very stable |
| Sample quality | High | Low-medium (blurry) | Medium | State-of-the-art |
| Likelihood | No explicit | Approximate (ELBO) | Exact | Approximate (ELBO) |
| Inference speed | Fast (one pass) | Fast (one pass) | Fast (one pass) | Slow (many steps) |
| Controllability | Moderate | Limited | Limited | Excellent with CFG |

Diffusion models beat GANs on image synthesis (Dhariwal & Nichol, 2021): FID 3.94 at 256×256 with classifier guidance, matching BigGAN while being more stable to train.

## Notable Systems

- **DALL-E 2** (OpenAI): Diffusion in CLIP latent space, guided by CLIP image embeddings
- **Stable Diffusion** (Stability AI): Latent diffusion on LAION-5B; open-source
- **Imagen** (Google): Cascaded pixel-space diffusion + large language model (T5) for text encoding
- **GLIDE** (OpenAI): Pixel-space diffusion with classifier-free guidance + text conditioning
- **Midjourney**: Proprietary, latent diffusion variant
- **SDXL**: Improved Stable Diffusion with larger UNet and refined conditioning

## Sources

- Lilian Weng, [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
- Jay Alammar, [The Illustrated Stable Diffusion](http://jalammar.github.io/illustrated-stable-diffusion/)
- Aman Chadha, [Primers: Diffusion Models](https://aman.ai/primers/ai/diffusion-models/)
