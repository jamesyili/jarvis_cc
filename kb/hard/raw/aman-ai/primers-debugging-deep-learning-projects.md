# Primers • Debugging deep learning projects

**Source:** https://aman.ai/primers/ai/debugging-dl-projects/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Introduction](#introduction)
* [Problem Statement](#problem-statement)
* [Overall Approach](#overall-approach)
* [Types of Errors](#types-of-errors)
* [Debugging Tips](#debugging-tips)
* [Exercise](#exercise)
* [Expected Output](#expected-output)
  + [Epoch 1](#epoch-1)
  + [Epoch 2](#epoch-2)
  + [Epoch 3](#epoch-3)
* [Solutions](#solutions)

## Introduction

Debugging is one of the most useful skills you can learn as a deep learning researcher or engineer. In this section we’ll take a prebuilt codebase that performs **object segmentation** using an architecture similar to **UNet** <https://arxiv.org/abs/1505.04597>. This codebase has some bugs, and our goal will be to fix all of them so that our network trains properly.

## Problem Statement

We’re given as input to our network an image that looks like the following. This is an image with three types of shapes, potentially overlapping: circles, triangles, and squares. The shapes could be spread out all over the image, and we don’t know how many there are.

The image is of width 192 pixels, and height 192 pixels. It has 3 channels (an RGB image). Any pixel that has a shape has the value of (255, 255, 255), and any pixel that has no shape has the value of (0,0, 0).

We want to be able to predict:

The way we represent this is as an image with three channels. Each channel correspond to the particular class, so one channel for triangles, one channel for squares, and one triangle for circles. At a particular pixel value, if we have a 1 in the channel for squares, then there is a square at that pixel. Likewise for triangles and circles. Because objects may overlap on the image, we can have a pixel where both the triangle and circle channel are 1, for example.

## Overall Approach

We’ll be using a UNet style architecture, where we first downsample an image into feature maps repeatedly using CNN layers, reducing the width/height dimension while increasing the channel dimension. We then repeatedly upsample using CNN layers, increasing the width/height dimension while decreasing the channel dimension. Throughout this architecture we have residual connections across feature maps of the same width/height size (see UNet paper for more information).

The output of our model is a matrix of `num_classes` by `height` by `width`. That is, each pixel corresponds to a specific location in the image and a particular object class. The output of our network is between \([0, 1]\) and is performing a sigmoid activation per pixel. So each pixel is individually being classified as part of anywhere from 0-3 classes. We use 0.5 as a threshold for this classification.

## Types of Errors

We’ve introduced four types of errors into this codebase.

Syntax errors and logical errors should be similar to regular software engineering bugs. Algorithmic and experimental errors are probably more unique to deep learning as they may be related to your particular task/problem statement, the way you’re approaching the problem, or your experimental setup. We’ve littered all types of these bugs throughout the codebase.

1. **Syntax Error**
   * Your code doesn’t compile or run
2. **Logical Error**
   * Your code compiles but it doesn’t work the way you wanted it to.
   * You thought you were implementing something correctly but have a bug in that implementation that causes it perform some other function/operation.
3. **Algorithmic Error**
   * The code works the way you intended it to.
   * But the algorithm you were thinking of doesn’t make sense for your data/task.
4. **Experimental Error**
   * The code works, it’s the right algorithm, but you need to fix some hyperparameter or other experimental setting.

## Debugging Tips

* Pytorch is awesome in that it lets you directly print out outputs from layers, weights, gradients throughout your code. Make sure to use this to help debug!
* Try visualizing the input data, the weight magnitudes, etc in plots/images.
* Pytorch has a built in profiler you can try using as well
* Don’t be afraid to just try changing things and seeing if that helps!
* Watch out for changing a cell and then accidentally not running it. I recommend you every time make a change do Runtime -> Restart & Run All.

## Exercise

As far as we know, we’ve included **eight bugs**. After finding all of them you should be able to train the network to successfully accomplish this task. Best of luck! :)

[Colab Notebook (Pytorch)](https://colab.research.google.com/drive/1JJP9KBB8IwbX95v9Lfyxfdcspzp14lIE)

[Colab Notebook (Tensorflow)](https://colab.research.google.com/drive/15Qb544MSqDFuwLqarN0LRnn-jqxWuTH1)

## Expected Output

### Epoch 1

### Epoch 2

### Epoch 3

## Solutions

* [Pytorch](https://colab.research.google.com/drive/1HfF367oV_V2K25vf9Var_Tx4o9j2fO0p#scrollTo=ilOiCU_9EA7a)
* [Tensorflow](https://colab.research.google.com/drive/1PFJFZymPgaOLMQyQvMg5Xie7dctHcWiB)
