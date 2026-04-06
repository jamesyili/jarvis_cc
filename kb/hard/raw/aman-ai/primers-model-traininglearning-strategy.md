# Primers • Model Training/Learning Strategy

**Source:** https://aman.ai/primers/ai/learning-strategy/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Learning Strategy](#learning-strategy)
  + [Sanity Check: Model Architecture](#sanity-check-model-architecture)
  + [Citation](#citation)

## Learning Strategy

### Sanity Check: Model Architecture

* Overfit on a minibatch (or a small dataset) to ensure that there are no bugs and near-perfect performance on the training set is achieved, then set the batch size to what fits in the GPU memory for maximum vectorization/parallelization.
* Overfitting a model on a small mini-batch of data is sometimes a useful technique for debugging a deep learning model. Overfitting on a mini-batch means training the model to fit the mini-batch perfectly, even if it results in poor generalization performance.
* The reason why this can be useful for debugging is that it allows you to quickly identify issues with the model architecture or training process, such as high bias or high variance. For example, if the model is not able to overfit a small mini-batch, it may indicate that the model is too shallow or has not been trained for enough epochs. On the other hand, if the model overfits the mini-batch too quickly, it may indicate that the model is too complex or that the learning rate is too high.

### Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledActFunctions,
  title   = {Model Training/Learning Strategy},
  author  = {Chadha, Aman and Jain, Vinija},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
