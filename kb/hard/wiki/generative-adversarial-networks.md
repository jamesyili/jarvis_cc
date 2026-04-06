---
concept: Generative Adversarial Networks
tags: [gan, generative-models, stylegan, mode-collapse]
sources:
  - kb/hard/raw/aman-ai/primers-generative-adversarial-networks-gans.md
  - kb/hard/raw/aman-ai/chapter-7-realistic-face-generation.md
  - kb/hard/raw/aman-ai/chapter-8-high-resolution-image-synthesis.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/diffusion-models|Diffusion Models]]"
  - "[[hard/wiki/vision-language-models|Vision-Language Models]]"
---

# Generative Adversarial Networks

Generative Adversarial Networks (GANs), introduced by Goodfellow et al. in 2014, are a class of generative models that learn to synthesize new data instances by training two neural networks in opposition. The result, when training succeeds, is a generator that can produce outputs indistinguishable from real data. GANs remain one of the most influential architectures in modern computer vision despite being increasingly challenged by diffusion models.

## The Core Framework

A GAN consists of two networks:

- **Generator (G):** Takes random noise z (typically sampled from a uniform or Gaussian distribution) as input and produces a synthetic data instance G(z). The generator never sees real data directly; it only receives gradient signal from the discriminator.
- **Discriminator (D):** Takes either a real data instance x or a generated instance G(z) as input and outputs a scalar indicating the probability that the input is real.

The two networks are trained alternately. When training the discriminator, the generator's weights are frozen; when training the generator, the discriminator's weights are frozen. This prevents a moving-target problem where both networks chase each other simultaneously.

The adversarial dynamic is elegant: the generator tries to fool the discriminator into classifying its outputs as real; the discriminator tries to detect the deception. If training succeeds, the generator's distribution converges toward the real data distribution, and the discriminator is left flipping a coin (50% accuracy).

## Loss Functions

**Minimax Loss** is the formulation from the original paper:

```
min_G max_D E_x[log D(x)] + E_z[log(1 − D(G(z)))]
```

The discriminator maximizes this: it wants D(x) close to 1 for real data and D(G(z)) close to 0 for fakes. The generator minimizes it: it wants D(G(z)) close to 1. In practice, the generator often maximizes log D(G(z)) instead of minimizing log(1 − D(G(z))) to avoid vanishing gradients early in training when D can easily distinguish fakes.

**Wasserstein Loss (WGAN)** replaces the discriminator with a "critic" that outputs an unbounded real number rather than a probability. The critic loss is D(x) − D(G(z)); the generator loss is −D(G(z)). The training objective approximates the Earth Mover (Wasserstein) distance between real and generated distributions. Advantages over minimax: less vulnerable to vanishing gradients, avoids mode collapse more reliably, and provides a meaningful loss signal even when the discriminator is trained to optimality. WGAN requires clipping or gradient-penalizing the critic's weights to satisfy a Lipschitz constraint.

## Training Dynamics and Failure Modes

GAN training is notoriously unstable. Three failure modes dominate:

**Vanishing Gradients:** If the discriminator becomes too strong too quickly, D(G(z)) → 0 and the generator's gradient signal disappears. The generator cannot learn. Wasserstein loss and modified minimax loss both mitigate this.

**Mode Collapse:** The generator discovers a narrow subset of outputs that consistently fool the current discriminator and collapses to producing only those outputs. The discriminator then learns to reject them, the generator shifts to another narrow mode, and the two rotate without covering the full data distribution. Unrolled GANs address this by training the generator against a lookahead of future discriminator states. Wasserstein loss also helps by requiring the discriminator to be trained to near-optimality before each generator update.

**Failure to Converge:** GANs frequently oscillate rather than converge to an equilibrium. Regularization techniques — adding noise to discriminator inputs, penalizing discriminator weights — can improve stability. In practice, GAN training often requires extensive hyperparameter tuning and monitoring of both loss curves.

## Architectural Improvements

**DCGAN** (Deep Convolutional GAN) replaced fully connected layers with convolutional/transposed-convolutional layers, added batch normalization to both networks, and established architectural best practices (strided convolutions instead of pooling, ReLU in generator, LeakyReLU in discriminator). DCGAN made GANs stable enough for practical use.

**Progressive GANs** (ProGAN, Karras et al. 2017) start training at low resolution (4x4) and progressively add layers to both generator and discriminator, gradually increasing resolution to 1024x1024. This stabilizes training by letting the networks first learn coarse structure before fine details. The approach produced the first photorealistic high-resolution face images.

**StyleGAN** (and StyleGAN2) separated high-level style (coarse structure, pose, identity) from fine-grained detail by mapping the latent vector through a mapping network into an intermediate style space W, then injecting style at each convolutional layer via adaptive instance normalization (AdaIN). Noise is added at each layer for stochastic variation (hair, stubble, pores). StyleGAN2 removed a characteristic "droplet" artifact by redesigning the normalization. These architectures produce the most photorealistic synthetic faces to date.

**Conditional GANs (cGAN)** condition both generator and discriminator on a class label y, allowing controlled generation (e.g., generate a digit "7" rather than a random digit). They model P(X|Y) rather than the unconditional P(X). Extensions include image-to-image translation (pix2pix), which adds a pixel-wise reconstruction loss alongside the adversarial loss, and CycleGAN, which learns unpaired image-to-image translation using cycle-consistency loss.

**BigGAN** scaled GANs to large class-conditional image synthesis by using larger batch sizes, applying spectral normalization to stabilize training, and conditioning on class information via truncated noise sampling to trade diversity for fidelity.

## GAN Architecture for Face Generation

For realistic face generation at 1024x1024, the GAN generator uses a series of upsampling blocks. Each block applies transposed convolution (ConvTranspose2d) to increase spatial resolution, followed by a normalization layer and a non-linear activation. Four normalization options are commonly used: Batch Normalization (normalizes across the batch dimension), Layer Normalization (across features within one sample), Instance Normalization (per-channel per-sample, effective for style transfer), and Group Normalization (divides channels into groups, works at small batch sizes). The discriminator mirrors the generator with downsampling blocks that progressively reduce spatial dimensions while increasing channel depth.

**Truncated Sampling** at inference time clips the latent noise to a range (e.g., within 2 standard deviations), trading diversity for fidelity. This produces more "typical" faces at the cost of unusual or extreme outputs.

## Evaluation Metrics

**Inception Score (IS)** measures two properties simultaneously: generated images should be confidently classifiable (low label entropy per image) and the set of generated images should be diverse (high marginal label entropy). IS uses a pretrained Inception v3 classifier. Higher IS indicates better quality and diversity, but IS has known weaknesses — it can be gamed and does not compare to the real data distribution.

**Fréchet Inception Distance (FID)** is the preferred metric. FID computes the distance between the distribution of features extracted from real images and generated images using a pretrained Inception v3 network, treating each distribution as a multivariate Gaussian and computing the Fréchet distance between them. Lower FID is better. FID penalizes both low fidelity and low diversity and correlates better with human judgment than IS.

**Human evaluation** remains the gold standard for perceptual quality, but is expensive and not reproducible.

## GANs vs. Diffusion Models

GANs dominated generative image synthesis from roughly 2014–2021. Diffusion models have since surpassed them on FID and diversity for unconditional and text-conditioned generation. Key tradeoffs:

| Property | GANs | Diffusion Models |
|---|---|---|
| Training stability | Difficult | Stable |
| Generation speed | Fast (single forward pass) | Slow (many denoising steps) |
| Image quality | High (especially faces) | State-of-the-art |
| Mode coverage | Mode collapse risk | Full distribution |
| Attribute control | Structured latent space | Harder without guidance |

GANs retain advantages for applications that need fast generation, structured latent space manipulation (face attribute editing, interpolation), or moderate resolution. For open-ended, high-resolution synthesis, diffusion models dominate.

## Sources

- Chadha, Aman. "Primers: Generative Adversarial Networks (GANs)." aman.ai. https://aman.ai/primers/ai/gan/
- Chadha, Aman. "Chapter 7: Realistic Face Generation." aman.ai. https://aman.ai/h/des/face-generation/
- Chadha, Aman. "Chapter 8: High-Resolution Image Synthesis." aman.ai. https://aman.ai/h/des/high-res-synthesis/
