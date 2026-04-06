# Diffusion Language Models: How They Work, How They Compare to Autoregressive LLMs, and Where They're Going

**Source:** https://louiswang524.github.io/blog/diffusion-llm/
**Ingested:** 2026-04-05
**Tags:** llms, recsys, ai-agents, ml-systems, generative-models

---

[Home](/) › [Blog](/blog) › Diffusion Language Models: How They Work, How They Compare to Autoregressive LLMs, and Where They're Going  
Diffusion Language Models: How They Work, How They Compare to Autoregressive LLMs, and Where They're Going
 
 April 1, 2026 · 37 min read  · [diffusion models](/tags/diffusion models)[language models](/tags/language models)[LLaDA](/tags/LLaDA)[masked diffusion](/tags/masked diffusion)[autoregressive](/tags/autoregressive)[dLLM](/tags/dLLM)[MDLM](/tags/MDLM) 
  
[1. The Left-to-Right Constraint Is a Choice](#1-the-left-to-right-constraint-is-a-choice)

Every autoregressive language model — GPT, LLaMA, Claude — generates text left to right, one token at a time. This is not a law of nature. It is a design choice, and it has costs.

 Side-by-side comparison: AR generates left-to-right; dLLM refines all positions in parallel  Autoregressive (AR) Diffusion LM (dLLM)  

  t = 1    The  🔒   ···     ···     ···     ···     ···  

t = 2    The  🔒   cat  🔒   ···     ···     ···     ···  

t = 3    The  🔒   cat  🔒   sat  🔒   ···     ···     ···  

   t = T    [M]     [M]     [M]     [M]     [M]     [M]   t = T/2    The     [M]     [M]     on     [M]     mat   

 all positions scored in parallel  t = 0    The     cat     sat     on     the     mat    sequential · each token frozen on emit parallel · all positions revised each step 

*Figure 1: Autoregressive models generate tokens left-to-right, freezing each one before moving on. Diffusion LLMs start from a fully masked sequence and refine all positions in parallel across T denoising steps.*

The choice has a clean justification: it makes the probability of a sequence easy to factorize. Instead of modeling the entire sequence at once, you decompose it into a chain of simpler terms. Each step predicts the next token given all previous ones. This lets you train each step with a simple next-token prediction loss. The training is stable, and scaling laws are well understood. Autoregressive (AR) models have dominated language modeling for good reason.

But the left-to-right constraint introduces four concrete failure modes that do not go away as you scale.

**Sequential decoding bottleneck.** Each token depends on all previous tokens, so generation is inherently serial across positions. You cannot compute token 10 until you have token 9. Modern hardware is built for parallelism, but AR generation is inherently serial. The GPU executes one token at a time, leaving most of its compute bandwidth idle. Speculative decoding and other tricks can reduce this, but they do not eliminate the fundamental dependency chain.

**No global revision.** Once a token is emitted, it is frozen. The model cannot go back. If the third word of a 200-word response was the wrong choice — and later context makes that clear — the model has no mechanism to fix it. It can only try to recover forward, which often means producing awkward or inconsistent text. Human writers revise; AR models cannot.

**Exposure bias.** During training, the model always sees the correct previous tokens, fed in by teacher forcing. At inference, it sees its own predictions — which may be wrong. This train/test mismatch is called exposure bias. The problem compounds. An early error shifts the distribution, making the next token harder to predict. That introduces another error. The gap between training and inference grows with sequence length. Modern training pipelines (Reinforcement Learning from Human Feedback, RLHF; Direct Preference Optimization, DPO) reduce the practical severity of this gap. But they do not eliminate it, and it compounds for out-of-distribution continuations.

**Greedy commitment.** The model must commit to each word before it knows the rest of the sentence. In English, the verb often determines which noun phrase makes sense, but the verb comes after the noun. AR models must make early decisions without global context. Beam search and sampling can explore alternatives, but they still commit to a prefix before seeing the full context. Neither can revise a position after it is selected.

These are not engineering bugs. They are structural consequences of the left-to-right factorization. Fixing them requires a different generative process.

[A Different Approach: Start Noisy, Refine Globally](#a-different-approach-start-noisy-refine-globally)

Diffusion language models (dLLMs) take a fundamentally different path. Instead of building a sequence left to right, they start from a fully masked or heavily noised sequence and iteratively refine it into coherent text. Every position is updated at every step. Early refinements are coarse; later ones are fine-grained. The model allows positions to be revised throughout the refinement process.

This shifts the question from “what comes next?” to “what should this position be?” — from local to global.

[What This Post Covers](#what-this-post-covers)

This post is a technical deep-dive into how diffusion language models work, written for ML practitioners who are already comfortable with transformers and autoregressive LLMs. No prior exposure to diffusion models is assumed, but we will not slow down for transformer basics.

We cover two theoretical frameworks. Continuous diffusion adds Gaussian noise to token embeddings and gave rise to the foundational ideas. Masked diffusion operates directly on discrete tokens and is the dominant approach in 2025. We then walk through three concrete models — LLaDA, Dream, and Mercury — that represent the current state of the art. The post ends with a six-dimension head-to-head comparison of dLLMs and AR models. We close with an honest assessment of whether dLLMs are ready to replace AR in practice.

By the end, you will have enough technical grounding to read the primary papers, evaluate benchmarks critically, and decide where dLLMs belong in your own work.

[2. Continuous Diffusion: The Foundation](#2-continuous-diffusion-the-foundation)

Before building a generative model, we need a process that systematically destroys information — a forward process that gradually corrupts data into pure noise. Once we understand how to destroy, we can learn to reverse the destruction.

[2.1 The Forward Process](#21-the-forward-process)

The forward process is a Markov chain over TTT steps. At each step, it takes the previous sample xt−1\mathbf{x}_{t-1}xt−1​ and produces a noisier version xt\mathbf{x}_txt​:

q(xt∣xt−1)=N(xt; 1−βt xt−1, βtI)q(\mathbf{x}_t \mid \mathbf{x}_{t-1}) = \mathcal{N}(\mathbf{x}_t;\, \sqrt{1-\beta_t}\,\mathbf{x}_{t-1},\, \beta_t\mathbf{I})q(xt​∣xt−1​)=N(xt​;1−βt​

​xt−1​,βt​I)

In plain terms: we shrink the previous signal by 1−βt\sqrt{1-\beta_t}1−βt​

​ and add independent Gaussian noise with variance βt\beta_tβt​. The scalar βt∈(0,1)\beta_t \in (0, 1)βt​∈(0,1) is a noise schedule hyperparameter — small early on and larger later.

Two shorthands clean up the algebra. Define αt=1−βt\alpha_t = 1 - \beta_tαt​=1−βt​ and αˉt=∏s=1tαs\bar{\alpha}_t = \prod_{s=1}^{t} \alpha_sαˉt​=∏s=1t​αs​. The product αˉt\bar{\alpha}_tαˉt​ tells us how much of the original signal survives after ttt steps of corruption.

Applying the Markov chain recursively and using properties of Gaussian convolutions, we get a closed-form marginal at any timestep ttt directly from x0\mathbf{x}_0x0​:

q(xt∣x0)=N(xt; αˉt x0, (1−αˉt)I)q(\mathbf{x}_t \mid \mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t;\, \sqrt{\bar{\alpha}_t}\,\mathbf{x}_0,\, (1-\bar{\alpha}_t)\mathbf{I})q(xt​∣x0​)=N(xt​;αˉt​

​x0​,(1−αˉt​)I)

In plain terms: xt\mathbf{x}_txt​ is a scaled version of x0\mathbf{x}_0x0​ plus Gaussian noise whose variance grows as αˉt\bar{\alpha}_tαˉt​ shrinks toward zero.

This closed form is the key that makes diffusion training tractable. Instead of simulating ttt Markov steps to get xt\mathbf{x}_txt​, we sample it in one shot. Training can then draw arbitrary (t,x0)(t, \mathbf{x}_0)(t,x0​) pairs without sequential rollouts — every batch element can come from a different timestep.

 Noise schedule: ᾱₜ (signal) decays from 1 to 0; 1−ᾱₜ (noise) grows from 0 to 1   

 0.25  

 0.5  

 0.75   

  

  

  

 

  1.0 0.0  0 T/2 T Timestep t →  Value  x₀: clean data xT: pure noise  

 ᾱₜ (signal) 

 1−ᾱₜ (noise) 

*Figure 2: The cosine noise schedule. ᾱₜ (signal retention) decays from 1 to 0; 1−ᾱₜ (noise level) grows from 0 to 1. The closed-form marginal q(xₜ|x₀) = N(√ᾱₜ x₀, (1−ᾱₜ)I) lets us sample any xₜ directly without simulating the chain.*

[2.2 The Reverse Process and ELBO](#22-the-reverse-process-and-elbo)

The generative model works in reverse: starting from xT∼N(0,I)\mathbf{x}_T \sim \mathcal{N}(0, \mathbf{I})xT​∼N(0,I), it denoises step by step until it recovers x0\mathbf{x}_0x0​. We approximate the true (intractable) reverse conditional with a neural network:

pθ(xt−1∣xt)=N(xt−1; μθ(xt,t), σt2I)p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t) = \mathcal{N}(\mathbf{x}_{t-1};\, \mu_\theta(\mathbf{x}_t, t),\, \sigma_t^2\mathbf{I})pθ​(xt−1​∣xt​)=N(xt−1​;μθ​(xt​,t),σt2​I)

The network predicts the mean μθ\mu_\thetaμθ​ of the denoised distribution; the variance σt2\sigma_t^2σt2​ is typically fixed to a schedule.

To train θ\thetaθ, we maximize the Evidence Lower Bound (ELBO) on log⁡pθ(x0)\log p_\theta(\mathbf{x}_0)logpθ​(x0​). The ELBO is a variational lower bound: maximizing it pushes pθp_\thetapθ​ to assign high probability to real data. It decomposes into three interpretable terms:

log⁡pθ(x0)≥Eq ⁣[log⁡pθ(x0∣x1)]⏟reconstruction−DKL(q(xT∣x0) ∥ p(xT))⏟prior matching−∑t=2TEq ⁣[DKL(q(xt−1∣xt,x0) ∥ pθ(xt−1∣xt))]⏟denoising matching at step t\log p_\theta(\mathbf{x}_0) \geq \underbrace{\mathbb{E}_q\!\left[\log p_\theta(\mathbf{x}_0 \mid \mathbf{x}_1)\right]}_{\text{reconstruction}} - \underbrace{D_\text{KL}(q(\mathbf{x}_T \mid \mathbf{x}_0)\,\|\,p(\mathbf{x}_T))}_{\text{prior matching}} - \sum_{t=2}^{T}\underbrace{\mathbb{E}_q\!\left[D_\text{KL}(q(\mathbf{x}_{t-1} \mid \mathbf{x}_t, \mathbf{x}_0)\,\|\,p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t))\right]}_{\text{denoising matching at step }t}logpθ​(x0​)≥reconstruction

Eq​[logpθ​(x0​∣x1​)]​​−prior matching

DKL​(q(xT​∣x0​)∥p(xT​))​​−∑t=2T​denoising matching at step t

Eq​[DKL​(q(xt−1​∣xt​,x0​)∥pθ​(xt−1​∣xt​))]​​

Each term has a clear role:

**Reconstruction**: how well does pθp_\thetapθ​ recover x0\mathbf{x}_0x0​ from the lightly-noised x1\mathbf{x}_1x1​? This is the final generation step, evaluated end-to-end.

**Prior matching**: does q(xT∣x0)q(\mathbf{x}_T | \mathbf{x}_0)q(xT​∣x0​) resemble the Gaussian prior p(xT)=N(0,I)p(\mathbf{x}_T) = \mathcal{N}(0, \mathbf{I})p(xT​)=N(0,I)? If the noise schedule drives αˉT→0\bar{\alpha}_T \to 0αˉT​→0, this KL is nearly zero. It is almost always treated as a constant.

**Denoising matching**: at each intermediate step ttt, how closely does the learned pθ(xt−1∣xt)p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t)pθ​(xt−1​∣xt​) match the true reverse conditional q(xt−1∣xt,x0)q(\mathbf{x}_{t-1} | \mathbf{x}_t, \mathbf{x}_0)q(xt−1​∣xt​,x0​)? This sum over ttt is the dominant training signal — it is what the model is actually optimized on.

The key insight is that q(xt−1∣xt,x0)q(\mathbf{x}_{t-1} | \mathbf{x}_t, \mathbf{x}_0)q(xt−1​∣xt​,x0​) is tractable. Conditioning on x0\mathbf{x}_0x0​ unlocks a closed-form Gaussian via Bayes’ theorem. So each KL in the sum can be computed analytically — no Monte Carlo estimation needed for the target.

 ELBO decomposition: denoising matching term dominates; reconstruction and prior matching are small  ELBO = reconstruction + prior matching + denoising matching       
Denoising matching — dominant signal
   

 Reconstruction  

 Prior ≈ 0  

 
Sum over t = 2…T → simplifies to 𝓛_simple
 

*Figure 3: The ELBO decomposes into three terms. The denoising matching term dominates — it is the sum over T timesteps that the model is trained on. The prior matching term is nearly zero with a well-designed noise schedule. This dominant term simplifies to the noise-prediction objective 𝓛_simple.*

The derivation of the ELBO follows from introducing the variational distribution qqq and applying Jensen’s inequality to log⁡pθ(x0)=log⁡∫pθ(x0:T) dx1:T\log p_\theta(\mathbf{x}_0) = \log \int p_\theta(\mathbf{x}_{0:T})\,d\mathbf{x}_{1:T}logpθ​(x0​)=log∫pθ​(x0:T​)dx1:T​. The Markov structure of qqq then factors the joint, separating the sum into per-timestep KL terms. For the full derivation, see Ho et al. (2020), Appendix A.

[2.3 The Simplified Training Objective and Score Matching](#23-the-simplified-training-objective-and-score-matching)

[Ho et al. (2020)](https://arxiv.org/abs/2006.11239) — the DDPM paper — showed that the ELBO sum simplifies to an intuitive noise-prediction loss. Use the reparameterization from the closed-form marginal: write xt=αˉt x0+1−αˉt ϵ\mathbf{x}_t = \sqrt{\bar{\alpha}_t}\,\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\,\boldsymbol\epsilonxt​=αˉt​

​x0​+1−αˉt​

​ϵ where ϵ∼N(0,I)\boldsymbol\epsilon \sim \mathcal{N}(0, \mathbf{I})ϵ∼N(0,I). Then train a network ϵθ\boldsymbol\epsilon_\thetaϵθ​ to predict ϵ\boldsymbol\epsilonϵ from the noisy input:

Lsimple=Et, x0, ϵ ⁣[∥ϵ−ϵθ(αˉt x0+1−αˉt ϵ, t)∥2]\mathcal{L}_\text{simple} = \mathbb{E}_{t,\,\mathbf{x}_0,\,\boldsymbol\epsilon}\!\left[\|\boldsymbol\epsilon - \boldsymbol\epsilon_\theta(\sqrt{\bar{\alpha}_t}\,\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\,\boldsymbol\epsilon,\, t)\|^2\right]Lsimple​=Et,x0​,ϵ​[∥ϵ−ϵθ​(αˉt​

​x0​+1−αˉt​

​ϵ,t)∥2]

In plain terms: given a noisy image, predict the noise that was added. Subtracting that prediction from the noisy input recovers an estimate of x0\mathbf{x}_0x0​.

This objective connects to score matching. The score function is ∇xtlog⁡p(xt)\nabla_{\mathbf{x}_t} \log p(\mathbf{x}_t)∇xt​​logp(xt​) — the gradient of the log-density with respect to the noisy sample. It points in the direction that increases the probability of xt\mathbf{x}_txt​ under ppp. The exact relationship between the noise predictor and the score is:

ϵθ(xt,t)≈−1−αˉt ∇xtlog⁡p(xt)\boldsymbol\epsilon_\theta(\mathbf{x}_t, t) \approx -\sqrt{1-\bar{\alpha}_t}\,\nabla_{\mathbf{x}_t}\log p(\mathbf{x}_t)ϵθ​(xt​,t)≈−1−αˉt​

​∇xt​​logp(xt​)

Predicting noise and estimating the score are the same operation, up to a scale factor that depends on the noise level at timestep ttt. This means Lsimple\mathcal{L}_\text{simple}Lsimple​ is equivalent to denoising score matching (DSM) — not just analogous to it. The uniform weighting across timesteps is the key simplification Ho et al. made relative to the full ELBO. (For the continuous-time generalization that makes this connection rigorous, see Song et al. 2020, “Score-Based Generative Modeling through Stochastic Differential Equations”, [arXiv:2011.13456](https://arxiv.org/abs/2011.13456).)

[2.4 Why Continuous Diffusion Breaks for Text](#24-why-continuous-diffusion-breaks-for-text)

So far, everything is clean. The math works because xt\mathbf{x}_txt​ lives in Rd\mathbb{R}^dRd — we can add real-valued noise, compute gradients, and train with MSE. Text is different.

Text tokens are discrete integers. A sentence is a sequence like `[42, 7, 1803, 5]`. You cannot add N(0,βtI)\mathcal{N}(0, \beta_t \mathbf{I})N(0,βt​I) to integers — the operation is undefined. Two workarounds have been tried, and both have significant limitations.

**Embed then diffuse (Diffusion-LM, Li et al. 2022).** Map tokens to continuous embeddings, diffuse in embedding space, and project back to tokens at inference via nearest-neighbor lookup. The problem is two-fold. The projection (argmax over vocabulary) is non-differentiable, which breaks the end-to-end gradient signal. And the geometry of embedding space does not reflect token probabilities — two embeddings that are close in ℓ2\ell_2ℓ2​ distance may correspond to semantically unrelated tokens. The continuous-space loss and the discrete-space goal are misaligned.

**Simplex diffusion.** Work directly in the probability simplex: represent each token position as a vector of VVV probabilities that sum to one, and define a diffusion process over that simplex. The problem here is geometric. The simplex has Riemannian geometry, not Euclidean. There is no natural Gaussian analog, the differential equations are harder to define, and most of the DDPM machinery breaks down. Austin et al. (2021) discuss exactly why continuous-space diffusion struggles with discrete data and use this analysis to motivate the discrete transition matrix approach in D3PM (Section 3.1; [arXiv:2107.03006](https://arxiv.org/abs/2107.03006)).

Both approaches treat discreteness as an obstacle to route around rather than a structure to exploit. The result is complexity without clean guarantees.

What we need is a diffusion process defined natively on discrete token sequences — one that replaces Gaussian noise with a categorical noise process where the math is as clean as DDPM. That is exactly what Discrete Denoising Diffusion Probabilistic Models (D3PM) provide, and it is the foundation of all modern masked diffusion LLMs. We cover it next.

[Discrete Diffusion: Making It Work for Text](#discrete-diffusion-making-it-work-for-text)

[3.1 D3PM — Discrete Denoising Diffusion Probabilistic Models](#31-d3pm--discrete-denoising-diffusion-probabilistic-models)

Continuous diffusion corrupts data by adding Gaussian noise to real-valued vectors. That operation has no meaning for integers. D3PM ([Austin et al., NeurIPS 2021, arXiv:2107.03006](https://arxiv.org/abs/2107.03006)) replaces the Gaussian transition kernel with a categorical one. Instead of perturbing a continuous vector, we apply a stochastic transition over the discrete vocabulary at each step.

**Categorical transition matrix.** The forward process is:

q(xt∣xt−1)=Cat(xt; xt−1Qt)q(\mathbf{x}_t \mid \mathbf{x}_{t-1}) = \text{Cat}(\mathbf{x}_t;\, \mathbf{x}_{t-1} Q_t)q(xt​∣xt−1​)=Cat(xt​;xt−1​Qt​)

Here Qt∈RV×VQ_t \in \mathbb{R}^{V \times V}Qt​∈RV×V is a row-stochastic transition matrix — every row sums to 1. The vector xt−1\mathbf{x}_{t-1}xt−1​ is a one-hot encoding over a vocabulary of size VVV. The probability of transitioning from token iii to token jjj in one step is (Qt)ij(Q_t)_{ij}(Qt​)ij​.

In plain terms: at each step, we roll a biased die for each token. The die probabilities are given by the row of QtQ_tQt​ corresponding to that token’s index.

**Absorbing state (masked diffusion).** For text, the most useful choice of QtQ_tQt​ is an absorbing-state matrix. Each non-mask token either stays the same (with probability 1−βt1 - \beta_t1−βt​) or transitions to a special `[MASK]` token (with probability βt\beta_tβt​). The `[MASK]` token is absorbing — once a token is masked, it stays masked:

(Qt)ij={1−βtif i=j≠[MASK]βtif j=[MASK],  i≠[MASK]1if i=j=[MASK](Q_t)_{ij} = \begin{cases} 1 - \beta_t & \text{if } i = j \neq \texttt{[MASK]} \\ \beta_t & \text{if } j = \texttt{[MASK]},\; i \neq \texttt{[MASK]} \\ 1 & \text{if } i = j = \texttt{[MASK]} \end{cases}(Qt​)ij​=⎩

⎨

⎧​1−βt​βt​1​if i=j=[MASK]if j=[MASK],i=[MASK]if i=j=[MASK]​

In plain terms: real tokens survive each step with probability 1−βt1 - \beta_t1−βt​. They are irreversibly erased to `[MASK]` with probability βt\beta_tβt​. Once erased, they cannot become real tokens again in the forward process. Every row sums to 1: for non-mask tokens, (1−βt)+βt=1(1 - \beta_t) + \beta_t = 1(1−βt​)+βt​=1; for the mask token, 1=11 = 11=1.

 Masked diffusion forward process: at each step, tokens are independently replaced by MASK with probability βₜ    

   

 
Forward process (corruption) →
  t = 0    The     cat     sat     on     the     mat  t = 1    The     [M]     sat     on     the     mat  t = 2    The     [M]     [M]     on     [M]     mat  t = 3    [M]     [M]     [M]     on     [M]     [M]  t = T    [M]     [M]     [M]     [M]     [M]     [M]   

*Figure 4: The masked diffusion forward process. At each step, tokens are independently replaced by [M] (MASK) with probability βₜ. The [MASK] state is absorbing — once masked, a token stays masked. By t=T, the entire sequence is destroyed.*

**Closed-form marginal.** Define Qˉt=Q1Q2⋯Qt\bar{Q}_t = Q_1 Q_2 \cdots Q_tQˉ​t​=Q1​Q2​⋯Qt​ as the product of all transition matrices up to step ttt. Then the marginal at step ttt is:

q(xt∣x0)=Cat(xt; x0Qˉt)q(\mathbf{x}_t \mid \mathbf{x}_0) = \text{Cat}(\mathbf{x}_t;\, \mathbf{x}_0 \bar{Q}_t)q(xt​∣x0​)=Cat(xt​;x0​Qˉ​t​)

In plain terms: instead of simulating ttt steps one at a time, we apply a single composite transition Qˉt\bar{Q}_tQˉ​t​ to jump directly from x0\mathbf{x}_0x0​ to xt\mathbf{x}_txt​.

For the absorbing-state matrix, this simplifies cleanly. Define αˉt=∏s=1t(1−βs)\bar{\alpha}_t = \prod_{s=1}^{t}(1 - \beta_s)αˉt​=∏s=1t​(1−βs​). Token x0(i)x_0^{(i)}x0(i)​ survives to step ttt with probability αˉt\bar{\alpha}_tαˉt​, and is masked with probability 1−αˉt1 - \bar{\alpha}_t1−αˉt​. This is structurally identical to the continuous DDPM case: αˉt\bar{\alpha}_tαˉt​ plays exactly the same role as signal retention. The only difference is that signal here is a discrete token, not a real-valued coordinate.

[3.2 The MDLM Training Objective](#32-the-mdlm-training-objective)

In continuous diffusion, the ELBO simplifies to noise prediction. In masked diffusion, it simplifies to token prediction at masked positions. This is the central result that makes masked diffusion practical.

Masked Diffusion Language Model (MDLM; [Sahoo et al., NeurIPS 2024, arXiv:2406.07524](https://arxiv.org/abs/2406.07524)) derives the exact ELBO for masked diffusion and shows that it decomposes into a weighted sum of masked language modeling losses:

LMDLM=Et, x0, xt∼q(xt∣x0) ⁣[∑i=1L1 ⁣[xt(i)=[MASK]]⋅λ(t)L⋅log⁡pθ ⁣(x0(i)∣xt)]\mathcal{L}_\text{MDLM} = \mathbb{E}_{t,\,\mathbf{x}_0,\,\mathbf{x}_t \sim q(\mathbf{x}_t|\mathbf{x}_0)}\!\left[\sum_{i=1}^{L} \mathbf{1}\!\left[x_t^{(i)} = \texttt{[MASK]}\right] \cdot \frac{\lambda(t)}{L} \cdot \log p_\theta\!\left(x_0^{(i)} \mid \mathbf{x}_t\right)\right]LMDLM​=Et,x0​,xt​∼q(xt​∣x0​)​[∑i=1L​1[xt(i)​=[MASK]]⋅Lλ(t)​⋅logpθ​(x0(i)​∣xt​)]

Here LLL is the sequence length, the indicator 1[⋅]\mathbf{1}[\cdot]1[⋅] selects masked positions, and λ(t)\lambda(t)λ(t) is a weighting function derived from the masking schedule. Specifically, λ(t)∝−dαˉt/dt1−αˉt\lambda(t) \propto -\dfrac{d\bar{\alpha}_t/dt}{1 - \bar{\alpha}_t}λ(t)∝−1−αˉt​dαˉt​/dt​, which upweights timesteps where a large fraction of tokens are already masked.

Three properties of this objective deserve attention.

**Predict-x0x_0x0​ parameterization.** The model predicts the original token x0(i)x_0^{(i)}x0(i)​, not a noise residual. The output at each masked position is a distribution over the full vocabulary. The network is a denoiser, not a noise predictor.

**Only masked positions contribute to the loss.** Unmasked tokens are directly observed in xt\mathbf{x}_txt​; their identity is known. The loss only applies where information has been destroyed — where there is something to predict. This is both efficient and principled.

**Connection to BERT’s MLM.** The objective looks identical to BERT’s masked language modeling loss. The crucial difference is that the masking schedule and weighting function λ(t)\lambda(t)λ(t) are derived from the ELBO — not chosen heuristically as in BERT. MDLM gives a principled justification for why MLM-style training is the right objective for generative masked diffusion models.

[3.3 Inference — Iterative Unmasking](#33-inference--iterative-unmasking)

At inference time, we start from a fully masked sequence and iteratively unmask it. No tokens are given; everything must be generated from the noise.

The procedure at a high level:

x_T = [MASK, MASK, ..., MASK]         # fully masked sequence of length L

for t = T, T-1, ..., 1:
    # 1. Predict original tokens for all positions in parallel
    probs = p_θ(x_0 | x_t)            # shape: [L, V]

    # 2. For each position, compute posterior probability of unmasking
    #    q(x_{t-1} | x_t, x_0) is tractable (derived from Bayes' rule on Q_t)

    # 3. Sample: unmask positions that the posterior assigns to step t
    x_{t-1} = unmask_positions(x_t, probs, t)

x_0  # fully denoised sequence

 Iterative unmasking: at each step all positions are scored in parallel, then tokens are selectively unmasked   

    

 
Reverse process (generation) →
   t = T    [M]     [M]     [M]     [M]     [M]     [M]   t = 3    [M]     [M]     [M]     on     [M]     [M]   

 
p_θ(x₀|xₜ) scored for all [M] positions in parallel
  t = 2    [M]     cat     [M]     on     [M]     mat   t = 1    The     cat     sat     on     [M]     mat   t = 0    The     cat     sat     on     the     mat    
T steps total · each step scores all positions simultaneously
 

*Figure 5: Masked diffusion inference starts from a fully masked sequence and iteratively unmasks it. At each step, the model scores all masked positions in parallel — this is the source of the parallelism advantage over autoregressive generation.*

The critical insight is that all positions are scored in parallel at every step. A single forward pass through the transformer produces logits for every `[MASK]` token simultaneously. This is where masked diffusion reclaims the GPU’s parallel compute that AR generation wastes on sequential token-by-token decoding.

**Speed-quality tradeoff.** Fewer steps TTT means faster generation but lower quality. More steps allow finer-grained refinement at the cost of more forward passes. Typical values for masked diffusion are T∈{32,64,128}T \in \{32, 64, 128\}T∈{32,64,128}. By contrast, AR generation requires exactly LLL sequential steps — one per token — with no adjustable tradeoff.

**The remasking trick.** LLaDA ([arXiv:2502.09992](https://arxiv.org/abs/2502.09992)) introduces a remasking trick during inference: rather than permanently freezing tokens once they are unmasked, re-mask a small fraction of them at each step. This lets the model revisit and correct tokens that were confidently but incorrectly predicted early in the process. The cost is a modest increase in total unmasking operations per run. The benefit is that early commitment errors do not compound through the rest of the sequence.

[3.4 Continuous vs. Masked Diffusion — A Direct Comparison](#34-continuous-vs-masked-diffusion--a-direct-comparison)

The two paradigms share the same high-level structure — forward corruption, ELBO training, iterative reverse sampling — but differ in almost every detail.

DimensionContinuous DiffusionMasked Diffusion (MDM)

Noise typeGaussian (N\mathcal{N}N)Categorical absorbing state (`[MASK]`)

Token spaceContinuous embeddingsDiscrete vocabulary

Forward processq(xt∥x0)=N(αˉtx0,(1−αˉt)I)q(\mathbf{x}_t\|\mathbf{x}_0) = \mathcal{N}(\sqrt{\bar\alpha_t}\mathbf{x}_0, (1-\bar\alpha_t)\mathbf{I})q(xt​∥x0​)=N(αˉt​

​x0​,(1−αˉt​)I)q(xt∥x0)=Cat(x0Qˉt)q(\mathbf{x}_t\|\mathbf{x}_0) = \text{Cat}(\mathbf{x}_0\bar{Q}_t)q(xt​∥x0​)=Cat(x0​Qˉ​t​)

Training objectivePredict noise ϵ\boldsymbol\epsilonϵ or scorePredict original token x0(i)x_0^{(i)}x0(i)​ at masked positions

InferenceTTT steps, sample xt−1\mathbf{x}_{t-1}xt−1​ from pθ(xt−1∥xt)p_\theta(\mathbf{x}_{t-1}\|\mathbf{x}_t)pθ​(xt−1​∥xt​)TTT steps, unmask tokens from posterior

Typical TTT100–100032–128

Key strengthRich theory; direct score estimationNative discrete tokens; tractable ELBO; fast TTT

Key weaknessRounding problem; geometry mismatch for textLess flexible noise process; no continuous gradients

2025 modelsPlaid ([arXiv:2305.18619](https://arxiv.org/abs/2305.18619))MDLM, LLaDA, Dream, Mercury

 Continuous diffusion corrupts embeddings with Gaussian noise; masked diffusion replaces tokens with MASK  Continuous Diffusion Masked Diffusion  

   t=0  t=1  +30% noise  t=2  +65% noise  t=T  pure noise    t=0    The     cat     sat     on     mat   t=1    The     [M]     sat     on     mat   t=2    The     [M]     [M]     on     [M]   t=T    [M]     [M]     [M]     [M]     [M]    xₜ = √ᾱₜ x₀ + √(1−ᾱₜ) ε   ε ~ N(0,I) P(xₜ⁽ⁱ⁾ = [M]) = 1 − ᾱₜ 

*Figure 6: The two noise mechanisms side by side. Continuous diffusion adds Gaussian noise to token embeddings — requiring a rounding step back to discrete tokens at inference. Masked diffusion replaces tokens with [MASK] natively, avoiding the geometry mismatch entirely.*

By 2025, masked diffusion has become the dominant approach for language. The reasons are practical. Training is simpler: the MDLM objective is well-founded and reduces to a familiar MLM loss. Inference is faster: T∈{32,128}T \in \{32, 128\}T∈{32,128} steps replaces hundreds or thousands. Tokens are native: no rounding step, no embedding geometry mismatch. And the ELBO is tractable in closed form, giving clean theoretical grounding. Continuous diffusion remains valuable for multimodal settings where real-valued representations are natural. For text, the discrete transition matrix approach wins on almost every dimension that matters.

[Key Models: From Research to Production](#key-models-from-research-to-production)

 dLLM model timeline: Plaid (2023), MDLM (2024), LLaDA, Dream, Mercury (2025)    

   

  

 masked diffusion  

  Plaid 2023 Scaling laws;64× gap

  MDLM 2024 PrincipledELBO for MDM

  LLaDA 2025 Scales to 8B;remasking

  Dream 2025 AR init +adaptive noise

  Mercury 2025 Commercial;1109 tok/s   continuous diffusion  masked diffusion  commercial deployment 

*Figure 7: Key milestones in diffusion language model development. Plaid (2023) closed the compute gap for continuous diffusion. MDLM (2024) gave masked diffusion a principled ELBO. LLaDA and Dream (2025) scaled masked diffusion. Mercury (2025) deployed it commercially.*

[4.1 LLaDA — Scaling Masked Diffusion](#41-llada--scaling-masked-diffusion)

LLaDA ([Nie et al., 2025, arXiv:2502.09992](https://arxiv.org/abs/2502.09992)) answered the first open question about masked diffusion LLMs: does it scale?

Before LLaDA, it was unknown whether masked diffusion would benefit from more parameters and more data the way AR models do. Scaling laws for AR transformers are well-characterized. For masked diffusion, no one had trained a model large enough to find out.

LLaDA’s answer was yes. The authors trained an 8B-parameter masked diffusion model from scratch, comparable in scale to LLaMA-3 8B. It showed competitive performance on GSM8K, MATH, and commonsense reasoning benchmarks. Older dLLMs had never approached this range. LLaDA closed that gap.

**The remasking strategy.** The key inference contribution is a remasking trick. In standard iterative unmasking, once a token is predicted and placed, it is frozen. If the model was confidently wrong early in the process, that token stays wrong and corrupts downstream predictions. LLaDA introduces a correction mechanism. At each step, after predicting all masked positions, the lowest-confidence predicted tokens are re-masked rather than finalized.

This gives the model a second chance. A wrong token does not lock in; it becomes a masked position again and can be re-predicted in a later step with more context. The cost is a modest increase in the number of unmasking operations. The benefit is that early commitment errors do not cascade.

The empirical result: LLaDA-8B is competitive with LLaMA-3-8B across reasoning benchmarks, establishing that masked diffusion is not inherently weaker — it had simply not been trained at the right scale.

[4.2 Dream — AR Initialization and Adaptive Noise](#42-dream--ar-initialization-and-adaptive-noise)

Dream 7B ([Ye et al., 2025, arXiv:2508.15487](https://arxiv.org/abs/2508.15487)) introduced two techniques that make training masked diffusion LLMs more practical.

**AR-model initialization.** Training an 8B masked diffusion model from scratch is expensive. Dream sidesteps part of that cost by starting from a pretrained AR LLM — for example, Mistral or LLaMA — and fine-tuning it to function as a denoiser. The intuition: AR models have already learned rich token-level representations across a large corpus. Those representations are useful regardless of whether generation proceeds left-to-right or via iterative unmasking. Initializing from a pretrained AR model dramatically reduces the compute needed to reach good perplexity. The analogy is BERT-style initialization for fine-tuning tasks: the representation quality transfers even when the objective changes.

**Context-adaptive token-level noise rescheduling.** Standard masked diffusion applies the same masking probability to every position in the sequence at a given timestep ttt. Dream adapts this per token based on local context. Tokens that are already tightly constrained by surrounding context receive lower masking probability — they are easy to predict, so spending training capacity on them is wasteful. Tokens in ambiguous positions, where the context provides little constraint, receive higher masking probability — they are where the model needs to learn most. This focuses training signal on the positions that are hardest to predict.

Together, these two contributions make Dream comparable in quality to training from scratch, at significantly lower compute.

[4.3 Plaid — Scaling Laws for Continuous Diffusion](#43-plaid--scaling-laws-for-continuous-diffusion)

Before the masked diffusion wave, Plaid ([Gulrajani & Hashimoto, 2023, arXiv:2305.18619](https://arxiv.org/abs/2305.18619)) established an important result for continuous (embedding-space) diffusion LMs.

The context: continuous diffusion LMs were widely considered too compute-inefficient to compete with AR models. Early comparisons, including those involving Diffusion-LM (Li et al., 2022), showed a compute gap of roughly 1000x — you needed a thousand times more compute to match AR perplexity. This framing had largely written off the entire continuous diffusion approach for language.

Plaid’s finding reframed the problem. With proper scaling — larger models, more data, and improved training recipes — the compute gap narrows to roughly 64x. That is still a gap, but it is not a fixed ceiling. It is a training efficiency problem, not an architectural one. The gap closed from 1000x to 64x purely through better scaling; there is no reason to assume 64x is the floor.

Plaid shifted the field’s framing: from “continuous diffusion can’t compete” to “it needs better scaling.” This motivated the masked diffusion work that followed. If the gap was closable, it was worth closing — and masked diffusion offered a cleaner path.

One caveat: Plaid is a continuous diffusion model. It operates in embedding space, not on discrete tokens. The masked diffusion models (MDLM, LLaDA, Dream) are a separate line of work. Plaid’s contribution is establishing that the compute gap is not fundamental, not that continuous diffusion is the right long-term approach for text.

[4.4 Mercury — Production Deployment](#44-mercury--production-deployment)

Mercury ([Khanna et al., Inception Labs, 2025, arXiv:2506.17298](https://arxiv.org/abs/2506.17298)) is the first commercially deployed dLLM. Before Mercury, dLLMs were research artifacts. Mercury demonstrated production viability.

**What it demonstrates.** Mercury Coder Mini achieves 1,109 tokens/sec on H100. Inception Labs reports this as “up to 10x faster than speed-optimized frontier models.” Benchmarks against GPT-4o Mini and Claude 3.5 Haiku show 18–19x throughput advantage in raw tokens per second.

These numbers are self-reported. The evaluation methodology, model architecture details, and training data composition are not public. Treat the speed numbers as directionally correct, not as independently verified benchmarks.

**How the speed is achieved.** AR models are bottlenecked by sequential decoding: token nnn cannot be computed until token n−1n-1n−1 is finalized. Mercury’s parallel decoding processes all positions simultaneously at each denoising step. The sequential bottleneck is eliminated. With T=32T = 32T=32 or T=64T = 64T=64 steps, the GPU executes TTT parallel forward passes rather than LLL sequential ones. For code generation at L=512L = 512L=512, that is 512 sequential AR steps versus 32–64 parallel diffusion steps.

**What is not public.** Model architecture (whether it is a masked diffusion model or a continuous variant, and how it handles conditioning). Training data composition and scale. Exact benchmark setup, including whether throughput was measured under identical hardware and batching conditions. These gaps are typical for a commercial release but matter when comparing against academic baselines.

**Significance.** Mercury moved dLLMs from “this might work at scale” to “this works in production, at commercial speed.” The benchmark debate will continue; the deployment milestone is not in doubt.

[4.5 What 2026 Is Investing In](#45-what-2026-is-investing-in)

The concentration of dLLM papers in early 2026 is a signal. The core theory is settled. The field is now investing in making dLLMs fast, controllable, and fair to evaluate.

**S2D2** ([Han et al., 2026, arXiv:2603.25702](https://arxiv.org/abs/2603.25702)) applies speculative decoding to dLLMs without a separate draft model. It uses the model’s own coarser earlier-step outputs as draft proposals, then verifies them at finer steps. The approach is training-free — no additional model is needed.

**LogicDiff** ([Aman, 2026, arXiv:2603.26771](https://arxiv.org/abs/2603.26771)) injects logical constraints into the denoising process, improving performance on formal reasoning benchmarks. It is an early attempt to give dLLMs a chain-of-thought equivalent — structured intermediate reasoning rather than direct answer generation.

**AR vs. MDM controlled comparison** ([Vicentino, 2026, arXiv:2603.22075](https://arxiv.org/abs/2603.22075)) is the first rigorous head-to-head comparison of autoregressive and masked diffusion LMs with matched model size, training data, and compute. Most prior comparisons did not control all three simultaneously. This work is essential for evaluating quality claims that ignore these controls.

**EntropyCache** ([Cheong et al., 2026, arXiv:2603.18489](https://arxiv.org/abs/2603.18489)) adapts key-value (KV) caching to dLLMs. At each denoising step, it measures token entropy: positions where the model is already confident (low entropy) skip KV recomputation. High-entropy positions — where the model is still uncertain — are recomputed fully. This reduces per-step cost without changing the model or training procedure.

[AR vs. dLLM: A Six-Dimension Comparison](#ar-vs-dllm-a-six-dimension-comparison)

Benchmarks in this space are moving fast. Numbers that look definitive today may be overturned by a paper next month. The goal here is not a verdict — it is a structured picture of where the evidence stands and where it is genuinely thin. Six dimensions, each examined on its own terms.

 Radar chart: AR LLMs vs dLLMs across generation quality, inference speed, controllability, reasoning, scalability, and safety 

 

 

 

  Gen. Quality  Inference Speed  Controllability  Reasoning  Scalability  Safety   AR LLMs  dLLMs 
Qualitative scores · 2025 evidence at matched compute · no verdict implied
 

*Figure 8: Qualitative comparison of AR LLMs and dLLMs across six dimensions (2025 evidence, matched compute). dLLMs lead on controllability; AR leads on generation quality and reasoning. No verdict is implied — the chart reflects the current state of evidence, which is actively evolving.*

[Dimension 1: Generation Quality](#dimension-1-generation-quality)

AR models still lead on most standard benchmarks — perplexity on held-out text, MMLU, HumanEval — at matched parameter counts. That lead has narrowed substantially since 2023. LLaDA-8B ([Nie et al., 2025, arXiv:2502.09992](https://arxiv.org/abs/2502.09992)) is competitive with LLaMA-3-8B on several reasoning tasks at the same scale. “Competitive” is not “equal” — but it is no longer the 1000x compute gap from early continuous diffusion work.

Before reading any quality comparison, check what was controlled. Model size, training data volume, and compute budget all affect benchmark scores. Most earlier comparisons did not control all three at once. Vicentino (2026), [arXiv:2603.22075](https://arxiv.org/abs/2603.22075), is currently the most rigorous controlled comparison — matched model size, training data, and compute. Use it as the baseline, not earlier uncontrolled results.

One measurement note: perplexity is not directly comparable between AR and dLLM. AR perplexity measures the probability of a sequence under a chain of next-token conditionals. Masked diffusion perplexity measures reconstruction probability under a different probabilistic model. They are computing different quantities. Downstream task accuracy on shared benchmarks — GSM8K, MMLU, HumanEval — is the fair metric.

[Dimension 2: Inference Speed](#dimension-2-inference-speed)

The arithmetic here matters, so let’s be explicit.

**AR decoding.** Generating a sequence of LLL tokens requires LLL sequential forward passes. Token kkk cannot be computed until token k−1k-1k−1 is done. KV caching helps: it stores key-value attention states from all previous tokens, so each new pass only needs to attend over a growing prefix rather than recompute from scratch. The attention cost per new token is O(L)O(L)O(L), amortized. Total cost is O(L2)O(L^2)O(L2), dominated by attention over the full sequence.

**dLLM decoding.** Generating a sequence of LLL tokens requires TTT forward passes, each attending over the full (partially masked) sequence of length LLL. Each pass costs O(L2)O(L^2)O(L2) attention. Total cost is O(T⋅L2)O(T \cdot L^2)O(T⋅L2). This is *more* operations than AR’s O(L2)O(L^2)O(L2) — never fewer. However, the advantage lies in wall-clock latency: each of dLLM’s TTT forward passes is parallelized across all LLL positions simultaneously on the GPU.

**Hardware parallelism advantage.** Take T=32T = 32T=32, L=2,048L = 2{,}048L=2,048. dLLM total attention operations: 32×2,0482≈134M32 \times 2{,}048^2 \approx 134M32×2,0482≈134M position-pairs. AR total attention operations: ∑k=12048k≈2,0482/2≈2.1M\sum_{k=1}^{2048} k \approx 2{,}048^2 / 2 \approx 2.1M∑k=12048​k≈2,0482/2≈2.1M position-pairs per sequence. In raw operation count, dLLM uses roughly 64x more FLOPs. Yet each dLLM step runs in parallel, saturating GPU compute across all LLL positions in a single forward pass. When TTT is small (e.g., 32) and sequences are long, this parallelism can offset the higher FLOP count in actual wall-clock time. Mercury’s 1,109 tokens/sec on H100 ([Khanna et al., 2025, arXiv:2506.17298](https://arxiv.org/abs/2506.17298)) demonstrates that the hardware advantage is real at production scale.

**KV cache asymmetry.** AR’s KV cache is a straightforward accumulation: each new token’s keys and values are appended. In masked diffusion, each denoising step sees a different partially masked sequence. The KV cache trick does not transfer directly — caching from step ttt is not reusable at step t−1t-1t−1 without modification. EntropyCache ([Cheong et al., 2026, arXiv:2603.18489](https://arxiv.org/abs/2603.18489)) is an active attempt to reclaim some of this. The gap is real but not necessarily permanent.

[Dimension 3: Controllability](#dimension-3-controllability)

This is a structural difference, not a benchmark question.

AR generates left to right. Every token is committed in order. Infilling — given a prefix and a suffix, generate the middle — is awkward. The model was not trained to see future context. Fill-in-the-Middle (FIM) training is the standard workaround: the training corpus is augmented with shuffled prefix/suffix/middle triples so the model learns to generate middles. It works, but it requires deliberate training data preparation. Infilling is learned behavior, not natural behavior.

Masked diffusion sees the entire (partially masked) sequence at every denoising step. Infilling is the default operation: fix some positions, mask the rest, denoise. The model has bidirectional context from step one. Structured output generation — fix a JSON schema in known positions, generate the values — is the same operation. Constrained story generation with required phrases is the same operation. These are not special cases requiring workarounds; they follow from the model’s native training objective.

Concrete examples where this matters: code completion given a function signature and test cases, document editing where some paragraphs are fixed, structured extraction into a predefined schema.

This advantage does not depend on benchmark results. It follows from the generative process.

[Dimension 4: Reasoning](#dimension-4-reasoning)

This is the dimension where the gap is largest and the path forward is least clear.

AR chain-of-thought works because generation is sequential. Token kkk can attend to tokens 111 through k−1k-1k−1, including all intermediate reasoning steps that have been committed so far. Earlier computation is persistent and available to later steps. Chain-of-thought is a natural consequence of the generative process, not an add-on.

Masked diffusion denoises all positions in parallel. There is no notion of “first commit the reasoning, then commit the answer.” Early positions cannot be decided before late positions because all positions update simultaneously. The model cannot naturally produce an explicit intermediate chain of thought.

Two 2026 approaches attempt to close this gap.

**EoS-by-EoS reasoning** ([Breckner & Schuster, 2026, arXiv:2603.05197](https://arxiv.org/abs/2603.05197)) sidesteps the token commitment problem. Instead of generating explicit reasoning tokens, it uses the hidden states of end-of-sequence (EoS) tokens as a reasoning scratchpad. These hidden states accumulate across denoising steps. The model can “think” through multiple diffusion steps without committing visible tokens. This is implicit chain-of-thought: the reasoning exists in activation space rather than token space.

**LogicDiff** ([Aman, 2026, arXiv:2603.26771](https://arxiv.org/abs/2603.26771)) takes a different path. It injects constraint satisfaction objectives directly into the denoising distribution. At each step, the score function is guided toward outputs that satisfy logical constraints. The reasoning structure is enforced externally rather than generated explicitly.

Neither approach currently matches AR chain-of-thought on hard mathematical or multi-step reasoning benchmarks. Whether the gap is reducible or fundamental remains an open question.

[Dimension 5: Training Efficiency and Scalability](#dimension-5-training-efficiency-and-scalability)

The training costs are more similar than the inference costs.

Both AR and masked diffusion use cross-entropy as the core training signal. AR minimizes cross-entropy on next-token prediction. Masked diffusion (under the MDLM objective) minimizes a weighted sum of cross-entropy losses at masked positions. Per-token compute during training is in the same ballpark.

The practical gap is in empirical guidance. AR teams have detailed playbooks from Chinchilla ([Hoffmann et al., 2022](https://arxiv.org/abs/2203.15556)) and subsequent work: given a compute budget, how should you split it between model size and training tokens? dLLM teams do not have an equivalent. LLaDA provides evidence that masked diffusion scales, but no systematic compute-optimal study exists for dLLMs. The optimal token-to-parameter ratio is unknown.

This is the most important open question for anyone considering a dLLM training run. You can follow Chinchilla ratios as a starting point, but you are extrapolating from an AR result. The optimal point may differ.

[Dimension 6: Memorization and Safety](#dimension-6-memorization-and-safety)

AR memorization is well-studied. Models memorize verbatim sequences, particularly repeated or high-frequency ones. Extraction attacks — prompting the model to reproduce training data — can recover sequences verbatim, especially from large models trained for many epochs. The phenomenon is documented and reasonably well characterized.

The dLLM picture is less clear, with competing hypotheses. One hypothesis: bidirectional context increases memorization. When the model reconstructs a masked token, it can attend to all surrounding tokens — potentially more context than AR sees when predicting the same token left-to-right. More context may make verbatim reconstruction easier. Counter-hypothesis: stochastic denoising reduces memorization. The noise injected during inference means the model never follows a fixed deterministic path through the sequence, which may prevent verbatim recall.

A 2026 study comparing memorization in AR and masked diffusion models provides early empirical evidence, but results at this scale may not generalize across model sizes and training datasets. This remains early-stage research.

The safety implications — for training data privacy, extraction attacks, and memorization audits — follow the same uncertainty. dLLM safety evaluation is largely undeveloped relative to AR. This is worth tracking if safety properties are a deployment requirement.

[Future Directions: Can dLLMs Replace Autoregressive Models?](#future-directions-can-dllms-replace-autoregressive-models)

Three open questions will determine the answer.

[6.1 The Three Open Questions](#61-the-three-open-questions)

[Question 1: The Scaling Question](#question-1-the-scaling-question)

No dLLM equivalent of the Chinchilla scaling laws exists. LLaDA ([Nie et al., 2025, arXiv:2502.09992](https://arxiv.org/abs/2502.09992)) showed that masked diffusion scales with model size and data. But the compute-optimal training recipe — optimal token-to-parameter ratio, learning rate schedules, data mixture — is unstudied for dLLMs.

AR’s dominance is partly a knowledge advantage. Practitioners know exactly how to train AR models compute-efficiently. Teams training dLLMs today navigate without that empirical guidance.

What would update the field: a systematic study at multiple model sizes and training budgets, with matched evaluation, tracing the compute-optimal frontier for masked diffusion. Until that exists, practitioners cannot compare the true training cost of a dLLM versus an AR model of equal capability.

[Question 2: The Reasoning Question](#question-2-the-reasoning-question)

AR chain-of-thought works because generation is sequential. Earlier tokens commit reasoning steps that condition later ones. This is a structural property of autoregressive decoding.

dLLMs denoise all positions in parallel. Reasoning tokens cannot condition generation tokens when both are denoised together. There is no natural “think first, then answer” phase.

Three potential paths forward:

**(A) Train on chain-of-thought (CoT) data.** Hope the model distributes implicit reasoning across denoising steps. No architectural change required. Evidence that this closes the hard-benchmark gap is limited.

**(B) Separate scratchpad.** A “scratchpad” denoises independently of the output, as explored in EoS-by-EoS ([Breckner & Schuster, 2026, arXiv:2603.05197](https://arxiv.org/abs/2603.05197)). Reasoning lives in activation space rather than token space.

**(C) Hybrid decoding.** Use AR for reasoning tokens and diffusion for output tokens, as in CoDAR ([Shen et al., 2026, arXiv:2603.02547](https://arxiv.org/abs/2603.02547)). Each paradigm handles the step where its structure is an advantage.

Current state: LogicDiff ([Aman, 2026, arXiv:2603.26771](https://arxiv.org/abs/2603.26771)) and EoS-by-EoS are promising early results. Neither is yet competitive with AR chain-of-thought on hard benchmarks.

[Question 3: The Inference Engineering Question](#question-3-the-inference-engineering-question)

AR models benefit from KV caching — storing key and value projections from previously decoded tokens. This yields roughly 4x memory reduction and significant latency reduction on long sequences.

dLLMs recompute full attention at every denoising step. Each step attends over the full noisy sequence, not a growing prefix. There is no prefix to cache in the AR sense.

Two approaches address this. EntropyCache ([Cheong et al., 2026, arXiv:2603.18489](https://arxiv.org/abs/2603.18489)) skips recomputation for low-entropy — high-confidence — tokens at each step. S2D2 ([Han et al., 2026, arXiv:2603.25702](https://arxiv.org/abs/2603.25702)) applies self-speculative decoding: earlier denoising steps produce draft proposals that later steps verify, requiring no separate draft model.

This is a solvable engineering problem, not a fundamental architectural limit. But it is unsolved in production today, and the gap affects real-world latency.

 Three plausible futures: A niche specialization, B quality convergence and broad adoption, C hybrid AR+diffusion architectures   

    2025 dLLMs exist Open question  

  Quality gap persists   A — Niche specialization   Niche: infilling & constrained gen  

  Scaling laws confirmed   B — Quality convergence   Broad adoption via parallel decoding  

  Best of both paradigms   C — Hybrid architectures   AR + diffusion hybrid (CoDAR-style)  

*Figure 9: Three plausible futures for diffusion LLMs. No path is endorsed — each depends on different empirical questions being resolved. The scaling question determines Future B; the reasoning question separates Future A from Futures B and C.*

[6.2 Three Plausible Futures](#62-three-plausible-futures)

No endorsement of any future. Current evidence is consistent with all three.

**Future A — Niche specialization.** dLLMs prove superior for a specific class of tasks: infilling, constrained generation, latency-sensitive parallel decoding. AR continues to dominate general-purpose generation. This requires the least from dLLMs — they need to win decisively on tasks where their structural advantages apply, not close the quality gap everywhere.

**Future B — Quality convergence and scale adoption.** dLLMs close the quality gap at scale. A Chinchilla-equivalent study shows they are compute-efficient. The parallel decoding advantage then drives broad adoption wherever inference cost matters: long-form generation, high-throughput serving. The scaling question is the critical dependency for this future.

**Future C — Hybrid architectures.** The AR vs. dLLM distinction dissolves. Models like CoDAR ([Shen et al., 2026, arXiv:2603.02547](https://arxiv.org/abs/2603.02547)) combine bidirectional diffusion conditioning for rich representations with AR decoding for sequential commitment. Neither paradigm wins outright — they merge into a new architecture capturing the structural benefits of both.

[6.3 Takeaways for the ML Practitioner](#63-takeaways-for-the-ml-practitioner)

**What to watch.**

Scaling studies for masked diffusion at multiple compute budgets.

Reasoning benchmark results that control for model size and training compute. Vicentino (2026, [arXiv:2603.22075](https://arxiv.org/abs/2603.22075)) provides the evaluation template.

Papers placing AR and dLLM head-to-head with matched training budgets, reporting downstream task accuracy rather than perplexity.

**What to try.**

LLaDA ([arXiv:2502.09992](https://arxiv.org/abs/2502.09992)) and Dream ([arXiv:2508.15487](https://arxiv.org/abs/2508.15487)) are open-source. Evaluate them on infilling benchmarks if you work on constrained generation tasks.

Mercury’s API ([arXiv:2506.17298](https://arxiv.org/abs/2506.17298)) if you need fast inference at scale and your task is coding or structured output generation.

**What to be skeptical of.**

Benchmark comparisons that do not simultaneously match model size, training data, and compute.

Speed claims from company technical reports without independent replication.

Any claim that dLLMs have “solved” reasoning. LogicDiff and EoS-by-EoS are promising, but the gap on hard benchmarks is real and large.

[References](#references)

[Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) — Ho, J., Jain, A., & Abbeel, P. (NeurIPS 2020)

[Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456) — Song, Y., Sohl-Dickenberg, J., Kingma, D. P., Kumar, A., Ermon, S., & Poole, B. (ICLR 2021)

[Structured Denoising Diffusion Models in Discrete State-Spaces](https://arxiv.org/abs/2107.03006) — Austin, J., Johnson, D. D., Ho, J., Tarlow, D., & van den Berg, R. (NeurIPS 2021)

[Diffusion-LM Improves Controllable Text Generation](https://arxiv.org/abs/2205.14217) — Li, X. L., Thickstun, J., Gulrajani, I., Liang, P., & Hashimoto, T. B. (NeurIPS 2022)

[Likelihood-Based Diffusion Language Models](https://arxiv.org/abs/2305.18619) — Gulrajani, I. & Hashimoto, T. B. (2023)

[Simple and Effective Masked Diffusion Language Models](https://arxiv.org/abs/2406.07524) — Sahoo, S. S., Arriola, M., Schiff, Y., Gokaslan, A., Marroquin, E., Chiu, J. T., Rush, A., & Kuleshov, V. (NeurIPS 2024)

[Large Language Diffusion Models (LLaDA)](https://arxiv.org/abs/2502.09992) — Nie, S., Zhu, F., You, Z., Zhang, X., Ou, J., Hu, J., Zhou, J., Lin, Y., Wen, J.-R., & Li, C. (2025)

[Mercury: Ultra-Fast Language Models Based on Diffusion](https://arxiv.org/abs/2506.17298) — Khanna, S., Kharbanda, S., Li, S., Varma, H., Wang, E., Birnbaum, S., Luo, Z., Miraoui, Y., Palrecha, A., Ermon, S., Grover, A., & Kuleshov, V. (Inception Labs, 2025)

[Dream 7B: Diffusion Large Language Models](https://arxiv.org/abs/2508.15487) — Ye, J., Xie, Z., Zheng, L., Gao, J., Wu, Z., Jiang, X., Li, Z., & Kong, L. (2025)

[CoDAR: Continuous Diffusion Language Models are More Powerful Than You Think](https://arxiv.org/abs/2603.02547) — Shen, J., Zhao, J., He, Z., & Lin, Z. (2026)

[Diffusion LLMs can think EoS-by-EoS](https://arxiv.org/abs/2603.05197) — Breckner, S. & Schuster, S. (2026)

[EntropyCache: Decoded Token Entropy Guided KV Caching for Diffusion Language Models](https://arxiv.org/abs/2603.18489) — Cheong, M., Son, D., Lim, W., & Yoo, S. (2026)

[Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison](https://arxiv.org/abs/2603.22075) — Vicentino, C. (2026)

[S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation](https://arxiv.org/abs/2603.25702) — Han, L., Wang, H., Gao, H., Xu, K., & Srivastava, A. (2026)

[LogicDiff: Logic-Guided Denoising Improves Reasoning in Masked Diffusion Language Models](https://arxiv.org/abs/2603.26771) — Aman, S. (2026)

   
 [ ← Previous Multi-Agent Patterns: Swarm, Teammates, and the Coordinator ](/blog/claude-code-multi-agent-patterns) 
 
 [ Next → TurboQuant Explained: How Google Compresses KV Caches to 3 Bits Without Losing the Plot ](/blog/turboquant-explained)
