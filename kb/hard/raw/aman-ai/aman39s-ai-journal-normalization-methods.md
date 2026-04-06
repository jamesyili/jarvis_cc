# Aman&#39;s AI Journal • Normalization Methods

**Source:** https://aman.ai/primers/ai/norm/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [BatchNorm](#batchnorm)
  + [What does it mean in practice?](#what-does-it-mean-in-practice)
  + [The above paper showed that fixing Internal Covariate shift with BN can:](#the-above-paper-showed-that-fixing-internal-covariate-shift-with-bn-can)
  + [When not to use BN?](#when-not-to-use-bn)
* [Auto-normalization using SELU](#auto-normalization-using-selu)
  + [Benefits of SELU](#benefits-of-selu)
* [References](#references)
* [Citation](#citation)

## BatchNorm

* Accelerate your NN training and converge faster: BatchNorm (BN) and LayerNorm (LN)
* Sergey Ioffe and Christian Szegedy’s 2015 paper, “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift” introduced the idea of BN
* Internal Covariate Shift is just a fancy name for the **change in the distribution of network activations** due to the change in network parameters during training across layers. (See the figure, how activations create the shift and how BN fixes it)

### What does it mean in practice?

* Some classical algorithms and NNs expect normalized data i.e means a mean of 0 and a standard deviation of 1. The authors showed not only ensure data is normalized before entering training but ensure it stays normalized while it’s training across layers for each mini-batch.

### The above paper showed that fixing Internal Covariate shift with BN can:

* Substantially decrease training time.
* Remove the need for drop-out (or combine with dropout).
* Decrease the regularization needed.
* Allow for increased learning rate.

### When not to use BN?

* From slide 3 of [LaBonte, Tyler. Self-Normalizing Neural Networks with SELU Activation. United States: N. p., 2019. Web.](https://www.osti.gov/servlets/purl/1645692), here’s the scenarios where BatchNorm shouldn’t be used:
  + Small mini-batch sizes. BatchNorm needs batch size > 8 to obtain accurate batch statistics.
  + Can’t be used in RNNs because each time-step has different statistics.
  + Challenged by authors proposing Weight/Layer/Instance/Group/Spectral normalization.
    - Nobody agrees on the “best” way to normalize

## Auto-normalization using SELU

* Wouldn’t it be great if deep neural networks just knew how best to normalize?
* Enter SELU Activation:

\[\operatorname{selu}(x)=\lambda \begin{cases}x & \text { if } x>0 \\ \alpha e^{x}-\alpha & \text { if } x \leq 0\end{cases}\]

### Benefits of SELU

* Self-normalizing: automatically converges to zero mean, unit variance.
* Allows training of very deep networks.
* Allows strong regularization schemes.
* Ensures learning robustness.
* Theoretically, makes vanishing/exploding gradients impossible.

## References

* [LaBonte, Tyler. Self-Normalizing Neural Networks with SELU Activation. United States: N. p., 2019. Web.](https://www.osti.gov/servlets/purl/1645692)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledNormalizationMethods,
  title   = {Normalization Methods},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
