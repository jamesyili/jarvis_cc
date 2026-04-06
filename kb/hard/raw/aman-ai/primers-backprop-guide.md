# Primers • Backprop Guide

**Source:** https://aman.ai/primers/backprop/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Background: Backprop](#background-backprop)
* [Why understand Backprop?](#why-understand-backprop)
* [Backprop and Gradient Descent](#backprop-and-gradient-descent)
* [Primer: Differential Calculus](#primer-differential-calculus)
* [Primer: Chain Rule for Backprop](#primer-chain-rule-for-backprop)
* [Handling Non-differentiability in Backprop](#handling-non-differentiability-in-backprop)
  + [Example: ReLU Activation Function](#example-relu-activation-function)
  + [Example: Absolute Value Function](#example-absolute-value-function)
  + [Smooth Approximations](#smooth-approximations)
* [(Partial) Derivatives of Standard Layers/Loss Functions](#partial-derivatives-of-standard-layersloss-functions)
* [(Partial) Gradients of Standard Layers/Loss Functions](#partial-gradients-of-standard-layersloss-functions)
* [References](#references)

## Background: Backprop

* From the Wikipedia article on [Backprop](https://en.wikipedia.org/wiki/Backpropagation),

> Backpropagation, an abbreviation for “backward propagation of errors”, is a common method of training artificial neural networks used in conjunction with an optimization method such as gradient descent. The method calculates the **gradient of a loss function with respect to all the weights** in the network. The gradient is fed to the **optimization method** which in turn uses it to **update the weights**, in an attempt to **minimize the loss function**.

* Note that the terms backprop and backward pass are used interchangeably. Technically, you carry out backprop during the backward pass while training your network.

## Why understand Backprop?

* Read through Andrej Karpathy’s famous post [“Yes you should understand backprop”](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b) about the need of understanding back propagation coining it as a [Leaky abstraction](https://en.wikipedia.org/wiki/Leaky_abstraction). From the post:

> It is easy to fall into the trap of **abstracting away the learning process** — believing that you can simply **stack arbitrary layers** together and backprop will “**magically make them work**” on your data.

## Backprop and Gradient Descent

* Gradient descent is the backbone of backprop. During backprop, we update our weights using gradient descent, which is a first-order iterative optimization algorithm for finding the **minima** of our (differentiable) **loss function**.
* To minimize our loss function using gradient descent, we take steps proportional to the negative of the gradient of the function at the current point.

## Primer: Differential Calculus

* Calculus is the study of continuous change. It has two major sub-fields: *differential calculus*, which studies the rate of change of functions, and *integral calculus*, which studies the area under the curve. Differential calculus is at the core of Deep Learning, so it is important to understand what derivatives and gradients are, how they are used in Deep Learning, and understand what their limitations are.
* For a tutorial on differential calculus, please refer our [Math Primer](../math).

## Primer: Chain Rule for Backprop

* In calculus, the chain rule helps compute the derivative of **composite** functions.
* Formally, it states that:

\[\frac{d}{d x}[f(g(x))]=f^{\prime}(g(x)) g^{\prime}(x)\]

* Read more about it [here](../ai/chain-rule).

## Handling Non-differentiability in Backprop

* Non-differentiability is handled in backpropagation using a few different strategies depending on the specific case. Here are the common methods:

  1. **Subgradients**:
     + For some non-differentiable points, a subgradient can be used. Subgradients generalize the concept of gradients for non-differentiable functions. The subgradient is a set of vectors that can be considered as a replacement for the gradient. This method is often used in functions like the ReLU activation function, which is non-differentiable at zero. For ReLU, the subgradient can be defined as 0 or 1 at the non-differentiable point.
  2. **Smooth Approximations**:
     + Non-differentiable functions can be approximated by smooth functions that are differentiable. For example, the absolute value function can be approximated by a smooth function that behaves similarly but is differentiable everywhere. This allows for the use of standard backpropagation techniques.
  3. **Clipping Gradients**:
     + In some cases, gradients can be clipped or modified at non-differentiable points to ensure stable training. This involves setting the gradient to a predefined value at non-differentiable points.
  4. **Special Handling of Non-Differentiable Points**:
     + Some algorithms explicitly handle non-differentiable points by setting rules for the gradient at those points. For instance, in the case of ReLU, the gradient is typically set to zero at the point of non-differentiability (zero input) during backpropagation.

### Example: ReLU Activation Function

* The ReLU (Rectified Linear Unit) activation function is defined as:

[ \text{ReLU}(x) = \begin{cases}
0 & \text{if } x \leq 0   
x & \text{if } x > 0
\end{cases}
]

* The derivative of ReLU is:

[ \text{ReLU}’(x) = \begin{cases}
0 & \text{if } x < 0   
1 & \text{if } x > 0
\end{cases}
]

* At ( x = 0 ), ReLU is non-differentiable. In practice, the gradient at this point is often set to 0 or 1 depending on the implementation. This simplification allows the backpropagation algorithm to proceed without issues.

### Example: Absolute Value Function

* |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | For a function like the absolute value function ( f(x) = | x | ), which is non-differentiable at ( x = 0 ), we can use subgradients. The subgradient of ( | x | ) at ( x = 0 ) can be any value in the interval ([-1, 1]). In practice, a common choice is to set the gradient to 0 at ( x = 0 ). |

### Smooth Approximations

* Some functions are approximated by smooth functions that are differentiable. For instance, the Huber loss combines the mean squared error (MSE) and mean absolute error (MAE) to create a smooth approximation that behaves like the absolute value function near zero but is quadratic away from zero. This makes the loss function differentiable and suitable for backpropagation.

## (Partial) Derivatives of Standard Layers/Loss Functions

* [Sigmoid Function](../backprop/derivative-sigmoid)
* [tanh](../backprop/derivative-tanh)
* [ReLU](../backprop/derivative-relu)
* [Cost Function for Logistic Regression](../backprop/derivative-logistic-regression)
* [Cost Function for Support Vector Machines/Hinge Loss](../backprop/derivative-svm)

## (Partial) Gradients of Standard Layers/Loss Functions

* [Convolutional Layers](../backprop/gradient-conv)
* [Batchnorm: Staged Computation](../backprop/gradient-batchnorm)
* [Batchnorm: Gradient Expression](../backprop/gradient-batchnorm-expr)

## References

* [Wikipedia article on Backpropagation](https://en.wikipedia.org/wiki/Backpropagation)
* [Wikipedia article on Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
