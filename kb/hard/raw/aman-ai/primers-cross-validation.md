# Primers • Cross Validation

**Source:** https://aman.ai/primers/ai/cross-validation/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Motivation](#motivation)
* [Final Model Training](#final-model-training)
* [Citation](#citation)

## Overview

* Cross-validation involves partitioning the dataset into multiple subsets and training the model multiple times. Each time, a different subset is used as a validation set, and the rest are used as training sets. This helps to give a better estimate of the model’s performance on unseen data.

## Motivation

* When you do K-fold cross validation, you are testing how well your model is able to get trained by some data and then predict data it hasn’t seen. We use cross validation for this because if you train using all the data you have, you have none left for testing. This is especially critical when you have limited data at hand.
* Also, we can use 80% of the data to train and 20% to test, but what if the 20% you happened to pick to test happens to contain a bunch of points that are particularly easy (or particularly hard) to predict? We will not have come up with the best estimate possible of the models ability to learn and predict. However, this concern can be alleviated to some extent using random sampling.
* We ideally want to use all of the data. So to continue the above example of an 80/20 split, we would do 5-fold cross validation by training the model 5 times on 80% of the data and testing on 20%. We ensure that each data point ends up in the 20% test set exactly once. We’ve therefore used every data point we have to contribute to an understanding of how well our model performs the task of learning from some data and predicting some new data.

## Final Model Training

* The purpose of cross-validation is not to come up with our final model. We don’t use the 5 instances of our trained model from the aforementioned example to do any real prediction. For that we want to use all the data we have to come up with the best model possible. The purpose of cross-validation is model checking, not model building.
* Now, say we have two models, say a linear regression model and a neural network. How can we say which model is better? We can do K-fold cross-validation and see which one proves better at predicting the test set points. But once we have used cross-validation to select the better performing model, we train that model (whether it be the linear regression or the neural network) on all the data. We don’t use the actual model instances we trained during cross-validation for our final predictive model.
  Note that there is a technique called bootstrap aggregation (usually shortened to ‘bagging’) that does in a way use model instances produced in a way similar to cross-validation to build up an ensemble model.

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledCrossValidation,
  title   = {Cross Validation},
  author  = {Chadha, Aman and Jain, Vinija},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
