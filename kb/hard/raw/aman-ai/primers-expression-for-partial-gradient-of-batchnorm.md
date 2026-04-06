# Primers • Expression for Partial Gradient of Batchnorm

**Source:** https://aman.ai/primers/backprop/gradient-batchnorm-expr/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Introduction](#introduction)
* [Batch Normalization](#batch-normalization)
* [Notation](#notation)
* [Chain Rule Primer](#chain-rule-primer)
* [Problem Statement](#problem-statement)
* [Partial Derivatives](#partial-derivatives)
  + [Cell 1](#cell-1)
  + [Cell 2](#cell-2)
  + [Cell 3](#cell-3)
* [Recap](#recap)
* [Python Implementation](#python-implementation)
* [Key Takeaways](#key-takeaways)
* [References](#references)

## Introduction

* This topic was mostly inspired by the question in Assignment 2 of Stanford’s [CS231n](http://cs231n.github.io/assignments2016/assignment2/) which requires you to derive an expression for the gradient of the batchnorm layer. Here, we explore the derivation in detailed steps and provide some sample code.
* The overall task in the assignment is to implement a Batch Normalization layer in a fully-connected net with a forward and backward pass. While the forward pass is relatively simple since it only requires standardizing the input features (**zero mean and unit standard deviation**). The backwards pass, on the other hand, is a bit more involved. It can be done in 2 different ways:
  + **Staged computation**: break up the function into several parts, derive local gradients for each of these parts, and finally group them together by multiplying them per the chain rule.
    - Interested in the staged computation method? head over to [Backward Pass of Batchnorm](../gradient-batchnorm)!
  + **Gradient derivation**: do a “pen and paper” derivation of the gradient with respect to the inputs.
* It turns out that second option is faster, albeit nastier and you will possibly need to endure a bit of a struggle to get it done.
* The aim behind this post is to offer a clear explanation of the derivation along with the thought process so as to build insight and intuition.

## Batch Normalization

* [Batch Normalization](https://arxiv.org/abs/1502.03167) is a technique to provide any layer in a Neural Network with inputs that are zero mean/unit variance - and this is basically what they like! But Batchnorm consists of one more step which makes this algorithm really powerful. Let’s take a look at the Batchnorm Algorithm:

* Looking at the last line of the algorithm, after normalizing the input \(x\), the result is squashed through a linear function with parameters \(\gamma\) and \(\beta\). These are learnable parameters of the Batchnorm Layer which offer the model an **extra degree of freedom** in terms of letting it get back to its **original data-distribution** (the one that gets fed in as input to the batchnorm layer) if it **doesn’t like the zero mean/unit variance input** that Batchnorm aspires to set up.
  + Thus, if \(\gamma = \sqrt{\sigma(x)}\) and \(\beta = \mu(x)\), the original activation is restored.
* This is what makes Batchnorm really powerful. Put simply, we initialize the Batchnorm Parameters to transform the input to zero mean/unit variance distributions but during training Batchnorm can learn that **another distribution might serve our purpose better**.

> The “Batch” in Batchnorm stems from the fact that we’re transforming the input based on the **statistics for only a batch** (i.e., a part) of the entire training set at a time, rather than going at it at a **per-sample granularity** or the **entire training set**.

* To learn more about Batchnorm, read [“Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift”](http://arxiv.org/abs/1502.03167) (2015) by Ioffe and Szegedy. Also, [here](https://youtu.be/gYpoJMlgyXA?list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC&t=3078) is a visual explanation of Batchnorm from Stanford’s CS231n.

## Notation

* Let’s start with some notation.

| \(f\) | the final output of the network |
| \(y\) | linear transformation which scales \(x\) by \(\gamma\) and adds \(\beta\) |
| \(\hat{x}\) | normalized inputs |
| \(\mu\) | batch mean |
| \(\sigma^2\) | batch variance |

## Chain Rule Primer

* Make sure to go through [“Primer: Chain Rule for Backprop”](../../ai/chain-rule) before you proceed - understanding of the chain rule is necessary for the later sections.

## Problem Statement

* The below table shows you the inputs to each function and will help with the future derivation.

* **Goal**: Find the partial derivatives with respect to the inputs, that is \(\dfrac{\partial f}{\partial \gamma}\), \(\dfrac{\partial f}{\partial \beta}\) and \(\dfrac{\partial f}{\partial x\_i}\).
* **Methodology**: derive the gradient with respect to the centered inputs \(\hat{x}\_i\) (which requires deriving the gradient w.r.t \(\mu\) and \(\sigma^2\)) and then use those to derive one for \(x\_i\).

## Partial Derivatives

* Let’s begin by traversing the above table from left to right. At each step, we’ll derive the gradient with respect to the inputs in the cell.

### Cell 1

* Let’s compute \(\dfrac{\partial f}{\partial y\_i}\). It actually turns out we don’t need to compute this derivative since we already have it - it’s the upstream derivative (referred to as `dout` in Stanford’s CS231n and is given to us as an input to the function in Assignment 2).

### Cell 2

* Let’s work on cell 2 now. We note that \(y\) is a function of \(\hat{x}\), \(\gamma\) and \(\beta\), so let’s compute the gradient with respect to each one.

---

Starting with \(\gamma\) and using the chain rule:

\[\begin{eqnarray}
\frac{\partial f}{\partial \gamma} &=& \frac{\partial f}{\partial y\_i} \cdot \frac{\partial y\_i}{\partial \gamma} \qquad \\
&=& \boxed{\sum\limits\_{i=1}^m \frac{\partial f}{\partial y\_i} \cdot \hat{x}\_i}
\end{eqnarray}\]

* Notice that we sum from \(1 \rightarrow m\) because we’re working with batches! If you’re worried you wouldn’t have caught that, make sure to perform **dimension-checks** at every step of the process.
* The gradient with respect to a variable **should be of the same size as that same variable** so if those two clash, it should tell you you’ve done something wrong.

---

Moving on to \(\beta\) we compute the gradient as follows:

\[\begin{eqnarray}
\frac{\partial f}{\partial \beta} &=& \frac{\partial f}{\partial y\_i} \cdot \frac{\partial y\_i}{\partial \beta} \qquad \\
&=& \boxed{\sum\limits\_{i=1}^m \frac{\partial f}{\partial y\_i}}
\end{eqnarray}\]

---

and finally \(\hat{x}\_i\):

\[\begin{eqnarray}
\frac{\partial f}{\partial \hat{x}\_i} &=& \frac{\partial f}{\partial y\_i} \cdot \frac{\partial y\_i}{\partial \hat{x}\_i} \qquad \\
&=& \boxed{\frac{\partial f}{\partial y\_i} \cdot \gamma}
\end{eqnarray}\]

---

* Up to now, things are relatively simple and we’ve already most of the work. We can’t compute the gradient with respect to \(x\_i\) just yet though.

### Cell 3

* Let’s start with \(\mu\). Since \(\sigma^2\) is a function of \(\mu\), we need to add its contribution to the partial - (the missing partials are highlighted in red):

\[\dfrac{\partial f}{\partial \mu} = \frac{\partial f}{\partial \hat{x}\_i} \cdot \color{red}{\frac{\partial \hat{x}\_i}{\partial \mu}} + \color{red}{\frac{\partial f}{\partial \sigma^2}} \cdot \color{red}{\frac{\partial \sigma^2}{\partial\mu}}\]

* Let’s compute the missing partials one at a time.
  + From\[\hat{x}\_i = \frac{(x\_i - \mu)}{\sqrt{\sigma^2 + \epsilon}}\]
  + we compute:\[\boxed{\dfrac{\partial \hat{x}\_i}{\partial \mu} = \frac{1}{\sqrt{\sigma^2 + \epsilon}} \cdot (-1)}\]
  + and from\[\sigma^2 = \frac{1}{m} \sum\limits\_{i=1}^m (x\_i - \mu)^2\]
  + we calculate:\[\boxed{\dfrac{\partial \sigma^2}{\partial \mu} = \frac{1}{m} \sum\limits\_{i=1}^m 2 \cdot (x\_i - \mu)\cdot (-1)}\]
* We’re missing the partial with respect to \(\sigma^2\) and that is our next variable, so let’s get to it and come back and plug it in here.

---

* In the expression of the partial:

\[\begin{eqnarray}
\frac{\partial f}{\partial \sigma^2} &=& \frac{\partial f}{\partial \hat{x}} \cdot \frac{\partial \hat{x}}{\partial \sigma^2} \qquad \\
\end{eqnarray}\]

* Let’s focus on \(\dfrac{\partial \hat{x}}{\partial \sigma^2}\). Rewrite \(\hat{x}\) to make its derivative easier to compute:

  \[\hat{x}\_i = (x\_i - \mu)(\sqrt{\sigma^2 + \epsilon})^{-0.5}\]
  + Since \((x\_i - \mu)\) is a constant:\[\begin{eqnarray}
  \dfrac{\partial \hat{x}}{\partial \sigma^2} &=& \sum\limits\_{i=1}^m (x\_i - \mu) \cdot (-0.5) \cdot (\sqrt{\sigma^2 + \epsilon})^{-0.5 - 1} \qquad \\
  &=& -0.5 \sum\limits\_{i=1}^m (x\_i - \mu) \cdot (\sqrt{\sigma^2 + \epsilon})^{-1.5}
  \end{eqnarray}\]

---

* With all that out of the way, let’s plug everything back in our previous partial!

\[\begin{eqnarray}
\frac{\partial f}{\partial \mu} &=& \bigg(\sum\limits\_{i=1}^m \frac{\partial f}{\partial \hat{x}\_i} \cdot \frac{-1}{\sqrt{\sigma^2 + \epsilon}} \bigg) + \bigg( \frac{\partial f}{\partial \sigma^2} \cdot \frac{1}{m} \sum\limits\_{i=1}^m -2(x\_i - \mu) \bigg) \qquad \\
&=& \bigg(\sum\limits\_{i=1}^m \frac{\partial f}{\partial \hat{x}\_i} \cdot \frac{-1}{\sqrt{\sigma^2 + \epsilon}} \bigg) + \bigg( \frac{\partial f}{\partial \sigma^2} \cdot (-2) \cdot \frac{1}{m} \sum\limits\_{i=1}^m x\_i - \frac{1}{m} \sum\limits\_{i=1}^m \mu \bigg) \qquad \\
&=& \bigg(\sum\limits\_{i=1}^m \frac{\partial f}{\partial \hat{x}\_i} \cdot \frac{-1}{\sqrt{\sigma^2 + \epsilon}} \bigg) + \bigg( \frac{\partial f}{\partial \sigma^2} \cdot (-2) \cdot \mu - \frac{m \cdot \mu}{m} \bigg) \qquad \\
&=& \sum\limits\_{i=1}^m \frac{\partial f}{\partial \hat{x}\_i} \cdot \frac{-1}{\sqrt{\sigma^2 + \epsilon}} \qquad \\
\end{eqnarray}\]

* Finally, we have:

\[\boxed{\frac{\partial f}{\partial \mu} = \sum\limits\_{i=1}^m \frac{\partial f}{\partial \hat{x}\_i} \cdot \frac{-1}{\sqrt{\sigma^2 + \epsilon}}}\]

Note that there’s a summation in \(\dfrac{\partial \hat{x}\_i}{\partial \mu}\) because we want the dimensions to add up with respect to `dfdmean` and not `dxnormdmean`.

---

* We finally arrive at the last variable \(x\). Again adding the contributions from any parameter containing \(x\) we obtain:

\[\dfrac{\partial f}{\partial x\_i} = \frac{\partial f}{\partial \hat{x}\_i} \cdot \color{red}{\frac{\partial \hat{x}\_i}{\partial x\_i}} + \frac{\partial f}{\partial \mu} \cdot \color{red}{\frac{\partial \mu}{\partial x\_i}} + \frac{\partial f}{\partial \sigma^2} \cdot \color{red}{\frac{\partial \sigma^2}{\partial x\_i}}\]

* The missing pieces are easy to compute at this point:

\[\dfrac{\partial \hat{x}\_i}{\partial x\_i} = \dfrac{1}{\sqrt{\sigma^2 + \epsilon}}\]
\[\dfrac{\partial \mu}{\partial x\_i} = \dfrac{1}{m}\]
\[\dfrac{\partial \sigma^2}{\partial x\_i} = \dfrac{2(x\_i - \mu)}{m}\]

* Thus, our final gradient is:

  \[\frac{\partial f}{\partial x\_i} = \bigg(\frac{\partial f}{\partial \hat{x}\_i} \cdot \dfrac{1}{\sqrt{\sigma^2 + \epsilon}}\bigg) + \bigg(\frac{\partial f}{\partial \mu} \cdot \dfrac{1}{m}\bigg) + \bigg(\frac{\partial f}{\partial \sigma^2} \cdot \dfrac{2(x\_i - \mu)}{m}\bigg)\]
  + Note the following trick:\[\left(\sigma^{2}+\epsilon\right)^{-1.5}=\left(\sigma^{2}+\epsilon\right)^{-0.5}\left(\sigma^{2}+\epsilon\right)^{-1}=\left(\sigma^{2}+\epsilon\right)^{-0.5} \frac{1}{\sqrt{\sigma^{2}+\epsilon}} \frac{1}{\sqrt{\sigma^{2}+\epsilon}}\]

---

* Let’s plug in the partials and see if we can simplify the expression some more:

\[\begin{eqnarray}
\frac{\partial f}{\partial x\_i} &=& \bigg(\frac{\partial f}{\partial \hat{x}\_i} \cdot \dfrac{1}{\sqrt{\sigma^2 + \epsilon}}\bigg) + \bigg(\frac{\partial f}{\partial \mu} \cdot \dfrac{1}{m}\bigg) + \bigg(\frac{\partial f}{\partial \sigma^2} \cdot \dfrac{2(x\_i - \mu)}{m}\bigg) \qquad \\
&=& \bigg(\frac{\partial f}{\partial \hat{x}\_i} \cdot \dfrac{1}{\sqrt{\sigma^2 + \epsilon}}\bigg) + \bigg(\frac{1}{m} \sum\limits\_{j=1}^m \frac{\partial f}{\partial \hat{x}\_j} \cdot \frac{-1}{\sqrt{\sigma^2 + \epsilon}}\bigg) - \bigg(0.5 \sum\limits\_{j=1}^m \frac{\partial f}{\partial \hat{x}\_j} \cdot (x\_j - \mu) \cdot (\sqrt{\sigma^2 + \epsilon})^{-1.5} \cdot \dfrac{2(x\_i - \mu)}{m} \bigg) \qquad \\
&=& \bigg(\frac{\partial f}{\partial \hat{x}\_i} \cdot (\sigma^2 + \epsilon)^{-0.5} \bigg) - \bigg(\frac{(\sigma^2 + \epsilon)^{-0.5}}{m} \sum\limits\_{j=1}^m \frac{\partial f}{\partial \hat{x}\_j} \bigg) + \bigg(\frac{(\sigma^2 + \epsilon)^{-0.5}}{m} \cdot \frac{x\_i - \mu}{\sqrt{\sigma^2 + \epsilon}} \sum\limits\_{j=1}^m \frac{\partial f}{\partial \hat{x}\_j} \cdot \frac{(x\_j - \mu)}{\sqrt{\sigma^2 + \epsilon}} \bigg )\qquad \\
&=& \bigg(\frac{\partial f}{\partial \hat{x}\_i} \cdot (\sigma^2 + \epsilon)^{-0.5} \bigg) - \bigg(\frac{(\sigma^2 + \epsilon)^{-0.5}}{m} \sum\limits\_{j=1}^m \frac{\partial f}{\partial \hat{x}\_j} \bigg) + \bigg(\frac{(\sigma^2 + \epsilon)^{-0.5}}{m} \cdot \hat{x}\_i \sum\limits\_{j=1}^m \frac{\partial f}{\partial \hat{x}\_j} \cdot \hat{x}\_j \bigg )\qquad \\
\end{eqnarray}\]

* Finally, we factorize by the \(\frac{(\sigma^2 + \epsilon)^{-0.5}}{m}\) factor and obtain:

\[\boxed{\frac{\partial f}{\partial x\_i} = \frac{(\sigma^2 + \epsilon)^{-0.5}}{m} \bigg [\color{red}{m \frac{\partial f}{\partial \hat{x}\_i}} - \color{blue}{\sum\limits\_{j=1}^m \frac{\partial f}{\partial \hat{x}\_j}} - \color{green}{\hat{x}\_i \sum\limits\_{j=1}^m \frac{\partial f}{\partial \hat{x}\_j} \cdot \hat{x}\_j}\bigg ]}\]

## Recap

* Let’s summarize the final equations we derived. Using \(\dfrac{\partial f}{\partial \hat{x}\_i} = \dfrac{\partial f}{\partial y\_i} \cdot \gamma\), we obtain the gradient with respect to our inputs:

\[\boxed{\color{red}{\frac{\partial f}{\partial \beta} = \sum\limits\_{i=1}^m \frac{\partial f}{\partial y\_i}}}\]
\[\boxed{\color{blue}{\frac{\partial f}{\partial \gamma} = \sum\limits\_{i=1}^m \frac{\partial f}{\partial y\_i} \cdot \hat{x}\_i}}\]
\[\boxed{\frac{\partial f}{\partial x\_i} = \frac{\color{red}{m \dfrac{\partial f}{\partial \hat{x}\_i}} - \color{blue}{\sum\limits\_{j=1}^m \dfrac{\partial f}{\partial \hat{x}\_j}} - \color{green}{\hat{x}\_i \sum\limits\_{j=1}^m \dfrac{\partial f}{\partial \hat{x}\_j} \cdot \hat{x}\_j}}{m\sqrt{\sigma^2 + \epsilon}}}\]

## Python Implementation

* Here’s an example Python implementation using the equations we derived. To compress the code a bit further, you can get creative with shorter variable names - this can also help accommodate the recommended \(80\) characters limit in Stanford’s CS231n.

```
def batchnorm_backward(dout, cache):

	N, D = dout.shape
	x_mu, inv_var, x_hat, gamma = cache

	# intermediate partial derivatives
	dxnorm = dout * gamma

	# final partial derivatives
	dx = (1. / N) * inv_var * (N*dxnorm - np.sum(dxnorm, axis=0) 
		- x_hat*np.sum(dxnorm*x_hat, axis=0))
	dbeta = np.sum(dout, axis=0)
	dgamma = np.sum(x_hat*dout, axis=0)

	return dx, dgamma, dbeta
```

* This version of the Batchnorm backward pass can give you a significant boost in speed. Timing both versions, you observe a superb \(3x\) increase in speed!

## Key Takeaways

* Learned how to use the chain rule in a staged manner to derive the expression for the gradient of the batch norm layer.
* Saw how a smart simplification can help significantly reduce the complexity of the expression for `dx`.
* Finally, implemented it as part of the backward pass with Python. This version of the function resulted in a \(3x\) speed increase!

## References

* [Deriving the Gradient for the Backward Pass of Batch Normalization](https://kevinzakka.github.io/2016/09/14/batch_normalization/) was the major inspiration behind this post.
* [Clément Thorey’s Blog](http://cthorey.github.io./backpropagation/) offers a similar tutorial that covers the gradient derivation of Batchnorm.
