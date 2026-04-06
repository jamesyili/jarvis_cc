# Primers • Partial Derivative for SVM/Hinge Loss

**Source:** https://aman.ai/primers/backprop/derivative-svm/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* The partial derivative of the multiclass hinge loss function (that multiclass-SVM deploys) with respect to the weights \(w\_j\) is:

\[\text{for the correct class, i.e., }j = y\_i:\\
\nabla\_{w\_{y\_i}} L\_i = - \left( \sum\_{j\neq y\_i} \mathbb{1}(w\_j^Tx\_i - w\_{y\_i}^Tx\_i + \Delta > 0) \right) x\_i\\
\\\\
\text{for the incorrect classes, i.e., }j \neq y\_i:\\
\nabla\_{w\_j} L\_i = \mathbb{1}(w\_j^Tx\_i - w\_{y\_i}^Tx\_i + \Delta > 0) x\_i\]

---

* Starting with the SVM loss function for a single datapoint:

\[L\_i = \sum\_{j\neq y\_i} \left[ \max(0, w\_j^Tx\_i - w\_{y\_i}^Tx\_i + \Delta) \right]\]

* Differentiating the function to obtain the gradient with respect to the weights corresponding to the correct class \(w\_{y\_i}\), we obtain:

  \[\boxed{\nabla\_{w\_{y\_i}} L\_i = - \left( \sum\_{j\neq y\_i} \mathbb{1}(w\_j^Tx\_i - w\_{y\_i}^Tx\_i + \Delta > 0) \right) x\_i}\]
  + where \(\mathbb{1}\{\cdot\}\) is the indicator function that is 1 if the condition inside is true or 0 otherwise.
* Note that this is the gradient only with respect to the **row** of \(W\) that corresponds to the **correct class**.
* To build some intuition as far as this expression goes, you’re simply **counting the number of classes that didn’t meet the desired margin** (and hence contributed to the loss function) and then the **data vector** \(x\_i\) **scaled by this count** is the effective gradient.

---

* For the other rows where \(j \neq y\_i \), the gradient is:

\[\boxed{\nabla\_{w\_j} L\_i = \mathbb{1}(w\_j^Tx\_i - w\_{y\_i}^Tx\_i + \Delta > 0) x\_i}\]

## References

* [Stanford CS231N optimization notes](http://cs231n.github.io/optimization-1/)
