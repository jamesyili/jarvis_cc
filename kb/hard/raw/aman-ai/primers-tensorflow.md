# Primers • TensorFlow

**Source:** https://aman.ai/primers/tensorflow/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [TensorFlow Introduction](#tensorflow-introduction)
  + [Getting started](#getting-started)
    - [Creating a virtual environment](#creating-a-virtual-environment)
    - [Using a GPU?](#using-a-gpu)
  + [Motivation](#motivation)
  + [Goals of this tutorial](#goals-of-this-tutorial)
  + [Resources](#resources)
  + [Recommended code structure](#recommended-code-structure)
  + [Graph, Session and nodes](#graph-session-and-nodes)
  + [A word about variable scopes](#a-word-about-variable-scopes)
  + [Dealing with different Training/Evaluation Graphs](#dealing-with-different-trainingevaluation-graphs)
* [Building the data pipeline](#building-the-data-pipeline)
  + [Motivation](#motivation-1)
  + [Goals of this tutorial](#goals-of-this-tutorial-1)
  + [Overview of tf.data](#overview-of-tfdata)
  + [Introduction to tf.data with a Text Example](#introduction-to-tfdata-with-a-text-example)
  + [Iterators and transformations](#iterators-and-transformations)
  + [Why do we use initializable iterators?](#why-do-we-use-initializable-iterators)
  + [Data pipeline](#data-pipeline)
* [Building an image data pipeline](#building-an-image-data-pipeline)
* [Building a text data pipeline](#building-a-text-data-pipeline)
  + [File format](#file-format)
  + [Zip datasets together](#zip-datasets-together)
  + [Creating a vocabulary](#creating-a-vocabulary)
  + [Creating padded batches](#creating-padded-batches)
  + [Computing the sentence’s size](#computing-the-sentences-size)
  + [Advanced use - extracting characters](#advanced-use---extracting-characters)
* [Best Practices](#best-practices)
  + [Shuffle and repeat](#shuffle-and-repeat)
  + [Parallelization: using multiple threads](#parallelization-using-multiple-threads)
  + [Prefetch data](#prefetch-data)
  + [Order of the operations](#order-of-the-operations)
* [Create and train a TF model](#create-and-train-a-tf-model)
  + [Goals of this tutorial](#goals-of-this-tutorial-2)
  + [Defining the model](#defining-the-model)
    - [Introduction to tf.layers](#introduction-to-tflayers)
    - [Training ops](#training-ops)
    - [Putting input\_fn and model\_fn together](#putting-input_fn-and-model_fn-together)
    - [Evaluation and tf.metrics](#evaluation-and-tfmetrics)
* [TensorFlow Tips and Tricks](#tensorflow-tips-and-tricks)
  + [Be careful with initialization](#be-careful-with-initialization)
  + [Saving](#saving)
  + [TensorBoard](#tensorboard)
  + [Writing a custom activation function](#writing-a-custom-activation-function)
  + [Model summary](#model-summary)
  + [global\_step](#global_step)
* [References](#references)

## TensorFlow Introduction

* This tutorial offers an overview of the preliminary setup, training process,loss functions and optimizers in TensorFlow.
* We cover a practical demonstration of TensorFlow with an example from Vision and another from NLP.

### Getting started

#### Creating a virtual environment

* To accommodate the fact that different projects utilize different versions of Python modules, it is a good practice to have multiple virtual environments to work on different projects.
* [Python Setup: Remote vs. Local](../python-setup) offers an in-depth coverage of the various remote and local options available.

#### Using a GPU?

* Note that your GPU needs to be set up first (drivers, CUDA and CuDNN).
* For TensorFlow, just run `pip install tensorflow-gpu`. When both `tensorflow` and `tensorflow-gpu` are installed, if a GPU is available, TensorFlow will transparently make use of the GPU, without you having to carry out code changes, unlike PyTorch.

### Motivation

* The goal of this tutorial is to quickly build a TensorFlow code-base implementing a Neural Network to classify hand digits from the MNIST dataset.
* To do so, the steps you are going to implement are:

  1. Load the dataset.
  2. Define placeholders.
  3. Define parameters of your model.
  4. Define the model’s graph (including the cost function).
  5. Define your accuracy metric.
  6. Define the optimization method and the training step.
  7. Initialize the TensorFlow graph.
  8. Optimize (loop).
  9. Compute training and testing accuracies.

### Goals of this tutorial

* Learn the basics of TensorFlow.
* Learn an example of how to correctly structure a deep learning project in TensorFlow.
* Fully understand how to implement ideas in code to be able to use it for your own projects.

### Resources

* For an official **introduction** to the TensorFlow concepts of `Graph()` and `Session()`, check out the [official introduction on TensorFlow.org](https://www.TensorFlow.org/tutorials/#TensorFlow_core_tutorial).
* For a **simple example on MNIST**, read the [official tutorial](https://www.TensorFlow.org/tutorials/), but keep in mind that some of the techniques are not recommended for big projects (they use `placeholders` instead of the new `tf.data` pipeline, they don’t use `tf.layers`, etc.).
* For a more **detailed tour** of TensorFlow, reading the [programmer’s guide](https://www.TensorFlow.org/guide/) is definitely worth the time. You’ll learn more about Tensors, Variables, Graphs and Sessions, as well as the saving mechanism or how to import data.
* For a **more advanced use** with concrete examples and code, we recommend reading [the relevant tutorials](https://www.TensorFlow.org/tutorials/) for your project. You’ll find good code and explanations, going from [sequence-to-sequence in TensorFlow](https://www.TensorFlow.org/tutorials/) to an [introduction to TF layers for convolutionnal Neural Nets](https://www.TensorFlow.org/tutorials/estimators/cnn#getting_started).
* You might also be interested in [Stanford’s CS20 class: TensorFlow for Deep Learning Research](http://web.stanford.edu/class/cs20si/) and its [github repo](https://github.com/chiphuyen/stanford-TensorFlow-tutorials) containing some cool examples.

### Recommended code structure

* We recommend the following code hierarchy to organize your data, model code, experiments, results and logs:

```
data/
experiments/
model/
    input_fn.py
    model_fn.py
    utils.py
    training.py
    evaluation.py
train.py
search_hyperparams.py
synthesize_results.py
evaluate.py
```

* Here is each `model/` file purpose:
  + `model/input_fn.py`: where you define the input data pipeline
  + `model/model_fn.py`: creates the deep learning model
  + `model/utils.py`: utility functions for handling hyperparams/logging
  + `model/training.py`: utility functions to train a model
  + `model/evaluation.py`: utility functions to evaluate a model
* We recommend reading through `train.py` to get a high-level overview.
* Once you get the high-level idea, depending on your task and dataset, you might want to modify:
  + `model/model_fn.py` to change the model’s architecture, i.e. how you transform your input into your prediction as well as your loss, etc.
  + `model/input_fn` to change the process of feeding data to the model.
  + `train.py` and `evaluate.py` to change the story-line (maybe you need to change the filenames, load a vocabulary, etc.)
* Once you get something working for your dataset, feel free to edit any part of the code to suit your own needs.

### Graph, Session and nodes

* When designing a Model in TensorFlow, there are basically [two steps](https://www.TensorFlow.org/tutorials/#TensorFlow_core_tutorial).
  1. building the computational graph, the nodes and operations and how they are connected to each other
  2. evaluating / running this graph on some data
* As an example of **step 1**, if we define a TF constant (= a graph node), when we print it, we get a `Tensor` object (= a node) and not its value.

```
x = tf.constant(1., dtype=tf.float32, name="my-node-x")
print(x) # Prints Tensor("my-node-x:0", shape=(), dtype=float32)
```

* Now, let’s move to **step 2**, and evaluate this node. We’ll need to create a `tf.Session` that will take care of actually evaluating the graph.

```
with tf.Session() as sess:
    print(sess.run(x)) # Prints 1.0
```

### A word about [variable scopes](https://www.TensorFlow.org/guide/#the_problem)

* When creating a node, TensorFlow will have a name for it. You can add a prefix to the nodes names. This is done with the `variable_scope` mechanism.

```
with tf.variable_scope('model'):
    x1 = tf.get_variable('x', [], dtype=tf.float32) # get or create variable with name 'model/x:0'
    print(x1) # Prints <tf.Variable 'model/x:0' shape=() dtype=float32_ref>
```

* What happens if we instantiate `x` twice?

```
with tf.variable_scope('model'):
    x2 = tf.get_variable('x', [], dtype=tf.float32) # Prints ValueError: Variable model/x already exists, disallowed.
```

* When trying to create a new variable named `model/x`, we run into an Exception as a variable with the same name already exists. Thanks to this naming mechanism, you can actually control which value you give to the different nodes, and at different points of your code, decide to have 2 python objects correspond to the same node!

```
with tf.variable_scope('model', reuse=True):
    x2 = tf.get_variable('x', [], dtype=tf.float32)
    print(x2) # Prints <tf.Variable 'model/x:0' shape=() dtype=float32_ref>
```

* We can check that they indeed have the same value:

```
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # Initialize the Variables
    sess.run(tf.assign(x1, tf.constant(1.)))    # Change the value of x1
    sess.run(tf.assign(x2, tf.constant(2.)))    # Change the value of x2
    print("x1 = ", sess.run(x1), " x2 = ", sess.run(x2)) # Prints x1 = 2.0  x2 = 2.0
```

### Dealing with different Training/Evaluation Graphs

* Code examples design choice: theoretically, the graphs you define for training and inference can be different, but they still need to share their weights. To remedy this issue, there are two possibilities:
  1. Re-build the graph, create a new session and reload the weights from some file when we switch between training and inference.
  2. Create all the nodes for training and inference in the graph and make sure that the python code does not create the nodes twice by using the `reuse=True` trick explained above.
* Here, we’re going ahead with the second option. As you’ll notice in `train.py` we give an extra argument when we build our graphs:

```
train_model_spec = model_fn('train', train_inputs, params)
eval_model_spec = model_fn('eval', eval_inputs, params, reuse=True)
```

* When we create the graph for the evaluation (`eval_model_spec`), the `model_fn` will encapsulate all the nodes in a `tf.variable_scope("model", reuse=True)` so that the nodes that have the same names than in the training graph share their weights!
* For those interested in the problem of making training and eval graphs coexist, you can read this [discussion](https://www.TensorFlow.org/tutorials/) which advocates for the other option.
* As a side note, option 1 is also the one used in [`tf.Estimator`](https://www.TensorFlow.org/guide/estimators).

## Building the data pipeline

### Motivation

* Building the input pipeline in a machine learning project is always long and painful, and can take more time than building the actual model. In this tutorial we will learn how to use TensorFlow’s Dataset module `tf.data` to build efficient pipelines for images and text.

### Goals of this tutorial

* Learn how to use `tf.data` and the best practices.
* Build an efficient pipeline for loading images and preprocessing them.
* Build an efficient pipeline for text, including how to build a vocabulary.

### Overview of tf.data

* The `Dataset` API allows you to build an asynchronous, highly optimized data pipeline to prevent your GPU from [data starvation](https://www.TensorFlow.org/guide/performance/overview#input_pipeline_optimization). It loads data from the disk (images or text), applies optimized transformations, creates batches and sends it to the GPU. Former data pipelines made the GPU wait for the CPU to load the data, leading to performance issues.

Before explaining how `tf.data` works with a simple example, we’ll share some great official resources:

* [API docs](https://www.TensorFlow.org/api_docs/python/tf/data) for `tf.data`
* [API docs](https://www.TensorFlow.org/api_docs/python/tf/contrib/data) for `tf.contrib.data`: new features still in beta mode. Contains useful functions that will soon be added to the main `tf.data`
* [Datasets Quick Start](https://www.TensorFlow.org/guide/datasets_for_estimators): gentle introduction to tf.data
* [Programmer’s guide](https://www.TensorFlow.org/guide/datasets): more advanced and detailed guide to the best practices when using Datasets in TensorFlow
* [Performance guide](https://www.TensorFlow.org/guide/performance/overview#input_pipeline_optimization): advanced guide to improve performance of the data pipeline
* [Official blog post](https://developers.googleblog.com/2017/09/introducing-TensorFlow-datasets.html) introducing Datasets and Estimators. We don’t use Estimators in our [code examples](https://github.com/cs230-stanford/cs230-code-examples) so you can safely ignore them for now.
* [Slides from the creator of tf.data](https://docs.google.com/presentation/d/16kHNtQslt-yuJ3w8GIx-eEH6t_AvFeQOchqGRFpAD7U/edit#slide=id.p) explaining the API, best practices (don’t forget to read the speaker notes below the slides)
* [Origin GitHub issue](https://github.com/TensorFlow/TensorFlow/issues/7951) for Datasets: a bit of history on the origin of `tf.data`
* [StackOverflow](https://stackoverflow.com/questions/tagged/TensorFlow-datasets) tag for the Datasets API

### Introduction to tf.data with a Text Example

* Let’s go over a quick example. Let’s say we have a `file.txt` file containing sentences

```
I use TensorFlow
You use PyTorch
Both are great
```

* Let’s read this file with the `tf.data` API:

```
dataset = tf.data.TextLineDataset("file.txt")
```

* Let’s try to iterate over it:

```
for line in dataset:
    print(line)
```

* We get an error

```
> TypeError: 'TextLineDataset' object is not iterable
```

* Wait! What just happened? I thought it was supposed to read the data.

### Iterators and transformations

* What’s really happening is that `dataset` is a node of the TensorFlow `Graph` that contains instructions to read the file. We need to initialize the graph and evaluate this node in a Session if we want to read it. While this may sound awfully complicated, this is quite the oposite : now, even the dataset object is a part of the graph, so you don’t need to worry about how to feed the data into your model!
* We need to add a few things to make it work. First, let’s create an `iterator` object over the dataset

```
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()
```

* The `one_shot_iterator` method creates an iterator that will be able to iterate once over the dataset. In other words, once we reach the end of the dataset, it will stop yielding elements and raise an Exception.
* Now, `next_element` is a graph’s node that will contain the next element of iterator over the Dataset at each execution. Now, let’s run it

```
with tf.Session() as sess:
    for i in range(3):
        print(sess.run(next_element))

>'I use TensorFlow'
>'You use PyTorch'
>'Both are great'
```

* Now that you understand the idea behind the `tf.data` API, let’s quickly review some more advanced tricks. First, you can easily apply transformations to your dataset. For instance, splitting words by space is as easy as adding one line

```
dataset = dataset.map(lambda string: tf.string_split([string]).values)
```

* Shuffling the dataset is also straightforward

```
dataset = dataset.shuffle(buffer_size=3)
```

* It will load elements 3 by 3 and shuffle them at each iteration.
* You can also create batches:

```
dataset = dataset.batch(2)
```

* And prefetch data (in other words, it will always have one batch ready to be loaded):

```
dataset = dataset.prefetch(1)
```

* Now, let’s see what our iterator has become:

```
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()
with tf.Session() as sess:
    print(sess.run(next_element))

>[['Both' 'are' 'great']
  ['You' 'use' 'PyTorch']]
```

* As you can see, we now have a batch created from the shuffled dataset!
* All the nodes in the Graph are assumed to be batched: every `Tensor` object will have `shape = [None, ...]` where None corresponds to the (unspecified) **batch dimension**.

### Why do we use initializable iterators?

```
dataset = tf.data.TextLineDataset("file.txt")
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()
init_op = iterator.initializer
```

* The behavior of an initializable iterator is similar to the one above, but thanks to the `init_op` we can chose to “restart” from the beginning. This will become quite handy when we want to perform multiple epochs!

```
with tf.Session() as sess:
    #Initialize the iterator
    sess.run(init_op)
    print(sess.run(next_element))
    print(sess.run(next_element))
    #Move the iterator back to the beginning
    sess.run(init_op)
    print(sess.run(next_element))

> 'I use TensorFlow'
'You use PyTorch'
'I use TensorFlow' # Iterator moved back at the beginning
```

* As we use only one session over the different epochs, we need to be able to restart the iterator. Some other approaches (like `tf.Estimator`) alleviate the need of using `initializable` iterators by creating a new session at each epoch. But this comes at a cost: the weights and the graph must be re-loaded and re-initialized with each call to `estimator.train()` or `estimator.evaluate()`.

### Data pipeline

* The `model/input_fn.py` defines a function `input_fn` that returns a dictionary that looks like:

```
images, labels = iterator.get_next()
iterator_init_op = iterator.initializer

inputs = {'images': images, 'labels': labels, 'iterator_init_op': iterator_init_op}
```

* This dictionary of inputs will be passed onto the model function, explained in the next section.

## Building an image data pipeline

* Here is what a Dataset for images might look like. Here we already have a list of `filenames` to JPEG images and a corresponding list of `labels`.
* We apply the following steps for training:
  1. Create the dataset from slices of the filenames and labels
  2. Shuffle the data with a buffer size equal to the length of the dataset. This ensures good shuffling (cf. [this answer](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle/48096625#48096625))
  3. Parse the images from filename to the pixel values. Use multiple threads to improve the speed of preprocessing
  4. (Optional for training) Data augmentation for the images. Use multiple threads to improve the speed of preprocessing
  5. Batch the images
  6. Prefetch one batch to make sure that a batch is ready to be served at all time

```
dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
dataset = dataset.shuffle(len(filenames))
dataset = dataset.map(parse_function, num_parallel_calls=4)
dataset = dataset.map(train_preprocess, num_parallel_calls=4)
dataset = dataset.batch(batch_size)
dataset = dataset.prefetch(1)
```

* `parse_function` does the following:
  + Read the content of the file.
  + Decode using JPEG format.
  + Convert to float values in `[0, 1]`.
  + Resize to size `(64, 64)`.

```
def parse_function(filename, label):
    image_string = tf.read_file(filename)

    #Don't use tf.image.decode_image, or the output shape will be undefined
    image = tf.image.decode_jpeg(image_string, channels=3)

    #This will convert to float values in [0, 1]
    image = tf.image.convert_image_dtype(image, tf.float32)

    image = tf.image.resize_images(image, [64, 64])
    return resized_image, label
```

* Finally, `train_preprocess()` can be optionally used during training to perform data augmentation:
  + Horizontally flip the image with probability \(1/2\).
  + Apply random brightness and saturation.

```
def train_preprocess(image, label):
    image = tf.image.random_flip_left_right(image)

    image = tf.image.random_brightness(image, max_delta=32.0 / 255.0)
    image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    #Make sure the image is still in [0, 1]
    image = tf.clip_by_value(image, 0.0, 1.0)

    return image, label
```

## Building a text data pipeline

* Have a look at the TensorFlow seq2seq tutorial using the `tf.data` pipeline:
  + TensorFlow’s official set of [tutorials](https://www.TensorFlow.org/tutorials/)
  + Neural Machine Translation (seq2seq) Tutorial on [Github](https://github.com/TensorFlow/nmt/)

### File format

* We’ve covered a simple example in the [overview of tf.data](#overview-of-tf.data) section. Now, let’s cover a more advanced example. Let’s assume that our task is [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition). In other words, our input is a sentence, and our output is a label for each word, like in:

```
John   lives in New   York
B-PER  O     O  B-LOC I-LOC
```

* Our dataset will thus need to load both the sentences and the labels. We will store those in 2 different files, a `sentence.txt` file containing the sentences (one per line) and a `labels.txt` containing the labels. For e.g.:

```
# sentences.txt
John lives in New York
Where is John ?
```

```
# labels.txt
B-PER O O B-LOC I-LOC
O O B-PER O
```

* Constructing `tf.data` objects that iterate over these files is easy:

```
# Load txt file, one example per line
sentences = tf.data.TextLineDataset("sentences.txt")
labels = tf.data.TextLineDataset("labels.txt")
```

### Zip datasets together

* At this stage, we might want to iterate over these 2 files at the same time. This operation is usually known as a “zip”. Luckilly, the `tf.data` comes with such a function

```
#Zip the sentence and the labels together
dataset = tf.data.Dataset.zip((sentences, labels))

#Create a one shot iterator over the zipped dataset
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()

#Actually run in a session
with tf.Session() as sess:
    for i in range(2):
        print(sess.run(dataset))

> ('John lives in New York', 'B-PER O O B-LOC I-LOC')
('Where is John ?', 'O O B-PER O')
```

### Creating a vocabulary

* Great, now we can get the sentence and the labels as we iterate. Let’s see how we can transform this string into a sequence of words and then in a sequence of ids.
* Most NLP systems rely on ids as input for the words, meaning that you’ll eventually have to convert your sentence into a sequence of ids.
* Here we assume that we ran some script, like `build_vocab.py` that created some vocabulary files in our `/data` directory. We’ll need one file for the words and one file for the labels. They will contain one token per line. For instance,

```
#words.txt
John
lives
in
...
```

and

```
#tags.txt
B-PER
B-LOC
...
```

* TensorFlow has a cool built-in tool to take care of the mapping. We simply define two lookup tables:

```
words = tf.contrib.lookup.index_table_from_file("data/words.txt", num_oov_buckets=1)
tags = tf.contrib.lookup.index_table_from_file("data/tags.txt")
```

* The parameter `num_oov_buckets` specifies the number of buckets created for unknown words. The id will be determined by TensorFlow and we don’t have to worry about it. As in most of the cases, we just want to have one id reserved for the out-of-vocabulary words, we just use `num_oov_buckets=1`.
* Now that we initialized this lookup table, we are going to transform the way we read the files, by adding these extra lines

```
#Convert line into list of tokens, splitting by white space
sentences = sentences.map(lambda string: tf.string_split([string]).values)

#Lookup tokens to return their ids
sentences = sentences.map(lambda tokens: (words.lookup(tokens), tf.size(tokens)))
```

* Be careful that `tf.string_split` returns a `tf.SparseTensor`, that’s why we need to extract the values.

### Creating padded batches

* Now we can iterate and get a list of IDs of words and labels for each sentence. We just need to take care of one final thing: **batches**! But here comes a problem: sentences have different length. Thus, we need to perform an extra **padding** operation that will add special token to shorter sentences so that our final batch `Tensor` object is a tensor of shape `[batch_size, max_len_of_sentence_in_the_batch]`.
* We first need to specify the padding shapes and values

```
#Create batches and pad the sentences of different length
padded_shapes = (tf.TensorShape([None]),   # sentence of unknown size
                tf.TensorShape([None]))  # labels of unknown size

padding_values = (params.id_pad_word,   # sentence padded on the right with id_pad_word
                 params.id_pad_tag)    # labels padded on the right with id_pad_tag
```

* Note that the padding\_values must be in the vocabulary (otherwise we might have a problem later on). That’s why we get the id of the special `<pad>` token in `train.py` with `id_pad_word = words.lookup(tf.constant('<pad>'))`.
* Then, we can just use the `tf.data` padded\_batch method, that takes care of the padding!

```
#Shuffle the dataset and then create the padded batches
dataset = (dataset
        .shuffle(buffer_size=buffer_size)
        .padded_batch(32, padded_shapes=padded_shapes, padding_values=padding_values)
        )
```

### Computing the sentence’s size

* Is that all that we need in general? Not quite. As we mentioned padding, we have to make sure that our model does not take the extra padded-tokens into account when computing its prediction. A common way of solving this issue is to add extra information to our data iterator and give the length of the input sentence as input. Later on, we will be able to give this argument to the `dynamic_rnn` function or create binary masks with `tf.sequence_mask`.
* Look at the model/input\_fn.py file for more details. But basically, it boils down to adding one line, using tf.size

```
sentences = sentences.map(lambda tokens: (vocab.lookup(tokens), tf.size(tokens)))
```

### Advanced use - extracting characters

Now, let’s try to perform a more complicated operation. We want to extract characters from each word, maybe because our NLP system relies on characters. Our input is a file that looks like:

```
1 22
3333 4 55
```

* We first create a dataset that yields the words for each sentence, as usual:

```
dataset = tf.data.TextLineDataset("file.txt")
dataset = dataset.map(lambda token: tf.string_split([token]).values)
```

* Now, we are going to reuse the `tf.string_split function`. However, it outputs a sparse tensor, a convenient data representation in general but which doesn’t seem do be supported (yet) by `tf.data`. Thus, we need to convert this `SparseTensor` to a regular `Tensor`.

```
def extract_char(token, default_value="<pad_char>"):
    #Split characters
    out = tf.string_split(token, delimiter='')
    #Convert to Dense tensor, filling with default value
    out = tf.sparse_tensor_to_dense(out, default_value=default_value)
    return out

#Dataset yields word and characters
dataset = dataset.map(lambda token: (token, extract_char(token)))
```

* Notice how we specified a `default_value` to the `tf.sparse_tensor_to_dense` function: words have different lengths, thus the `SparseTensor` that we need to convert has some unspecified entries!
* Creating the padded batches is still as easy as above:

```
#Creating the padded batch
padded_shapes = (tf.TensorShape([None]),       # padding the words
                tf.TensorShape([None, None])) # padding the characters for each word
padding_values = ('<pad_word>',  # sentences padded on the right with <pad>
                '<pad_char>')  # arrays of characters padded on the right with <pad>

dataset = dataset.padded_batch(2, padded_shapes=padded_shapes, padding_values=padding_values)
```

* and you can test that the output matches your expectations:

```
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()

with tf.Session() as sess:
    for i in range(1):
        sentences, characters = sess.run(next_element))
        print(sentences[0])
        print(characters[0][1])

> ['1', '22', '<pad_word>']               # sentence 1 (words)
  ['2', '2', '<pad_char>', '<pad_char>']  # sentence 1 word 2 (chars)
```

* Question: Can you explain why we have 2 `<pad_char>` and 1 `<pad_word>` in the first batch?

## Best Practices

* One general tip mentioned in TensorFlow’s [performance guide](https://www.TensorFlow.org/guide/performance/overview#input_pipeline_optimization) is to put all the data processing pipeline on the CPU to make sure that the GPU is only used for training the deep neural network model:

```
with tf.device('/cpu:0'):
    dataset = ...
```

### Shuffle and repeat

* When training on a dataset, we often need to repeat it for multiple epochs and we need to shuffle it.
* One big caveat when shuffling is to make sure that the `buffer_size` argument is big enough. The bigger it is, the longer it is going to take to load the data at the beginning. However a low buffer size can be disastrous for training.
  + Here’s a good [answer](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle/48096625#48096625) on StackOverflow detailing an example of why.
* The best way to avoid this kind of error would be to split the dataset into train/dev/test in advance and shuffle it right away. For more, see our tutorial on [splitting datasets](../data-split).
* In general, it is good to have the shuffling and repeat at the beginning of the pipeline. For instance if the input to the dataset is a list of filenames, if we directly shuffle after that the buffer of `tf.data.Dataset.shuffle()` will only contain filenames, which is very light on memory.
* When choosing the ordering between shuffle and repeat, you may consider two options:
  + **Shuffle then repeat**: we shuffle the dataset in a certain way, and repeat this shuffling for multiple epochs (ex: `[1, 3, 2, 1, 3, 2]` for 2 epochs with 3 elements in the dataset)
  + **Repeat then shuffle**: we repeat the dataset for multiple epochs and then shuffle (ex: `[1, 2, 1, 3, 3, 2]` for 2 epochs with 3 elements in the dataset)
* The second method provides a better shuffling, but you might wait multiple epochs without seeing an example. The first method makes sure that you always see every element in the dataset at each epoch. You can also use `tf.contrib.data.shuffle_and_repeat()` to perform shuffle and repeat.

### Parallelization: using multiple threads

* Parallelization of the data processing pipeline using multiple threads is almost transparent when using the `tf.data` module. We only need to add a `num_parallel_calls` argument to every `dataset.map()` call.

```
num_threads = 4
dataset = dataset.map(parse_function, num_parallel_calls=num_threads)
```

### Prefetch data

* When the GPU is working on forward / backward propagation on the current batch, we want the CPU to process the next batch of data so that it is immediately ready. As the most expensive part of the computer, we want the GPU to be fully used all the time during training. We call this consumer / producer overlap, where the consumer is the GPU and the producer is the CPU.
* With `tf.data`, you can do this with a simple call to `dataset.prefetch(1)` at the end of the pipeline (after batching). This will always prefetch one batch of data and make sure that there is always one ready.

```
dataset = dataset.batch(64)
dataset = dataset.prefetch(1)
```

* In some cases, it can be useful to prefetch more than one batch. For instance if the duration of the preprocessing varies a lot, prefetching 10 batches would average out the processing time over 10 batches, instead of sometimes waiting for longer batches.
* To give a concrete example, suppose than \(10\%\) of the batches take 10s to compute, and \(90\%\) take 1s. If the GPU takes 2s to train on one batch, by prefetching multiple batches you make sure that we never wait for these rare longer batches.

### Order of the operations

* To summarize, a good order for the different transformations is:

  1. Create the dataset.
  2. Shuffle (with a big enough buffer size).
  3. Repeat.
  4. Map with the actual work (preprocessing, augmentation, etc.) using multiple parallel calls.
  5. Batch.
  6. Prefetch.

## Create and train a TF model

### Goals of this tutorial

* Learn how to easily build models using `tf.layers`.

### Defining the model

* Now that we have the `input` dictionary containing tensors corresponding to the data, let’s explain how we build the model.

#### Introduction to tf.layers

* This high-level TensorFlow API lets you build and prototype models in a few lines. You can have a look at the [official tutorial for computer vision](https://www.TensorFlow.org/tutorials/estimators/cnn#getting_started), or at the [list of available layers](https://www.TensorFlow.org/tutorials/estimators/cnn#getting_started). The idea is quite simple so we’ll just give an example.
* Let’s get an input tensor with a similar mechanism than the one explained in the previous part. Remember that **None** corresponds to the batch dimension.

```
#shape = [None, 64, 64, 3]
images = inputs["images"]
```

* Now, let’s apply a convolution, a ReLU activation and a max-pooling. This is as simple as

```
out = images
out = tf.layers.conv2d(out, 16, 3, padding='same')
out = tf.nn.relu(out)
out = tf.layers.max_pooling2d(out, 2, 2)
```

* Finally, use this final tensor to predict the labels of the image (6 classes). We first need to reshape the output of the max-pooling to a vector

```
#First, reshape the output into [batch_size, flat_size]
out = tf.reshape(out, [-1, 32 * 32 * 16])
#Now, logits is [batch_size, 6]
logits = tf.layers.dense(out, 6)
```

* Note the use of `-1`: TensorFlow will compute the corresponding dimension so that the total size is preserved.
* The logits will be unnormalized scores for each example.
* In the code examples, the transformation from `inputs` to `logits` is done in the `build_model` function.

#### Training ops

* At this point, we have defined the `logits` of the model. We need to define our predictions, our loss, etc. You can have a look at the `model_fn` in `model/model_fn.py`.

```
#Get the labels from the input data pipeline
labels = inputs['labels']
labels = tf.cast(labels, tf.int64)

#Define the prediction as the argmax of the scores
predictions = tf.argmax(logits, 1)

#Define the loss
loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)
```

* The `1` in `tf.argmax` tells TensorFlow to take the argmax on the axis = 1 (remember that axis = 0 is the batch dimension)
* Now, let’s use TensorFlow built-in functions to create nodes and operators that will train our model at each iteration!

```
#Create an optimizer that will take care of the Gradient Descent
optimizer = tf.train.AdamOptimizer(0.01)

#Create the training operation
train_op = optimizer.minimize(loss)
```

* All these nodes are created by `model_fn` that returns a dictionary `model_spec` containing all the necessary nodes and operators of the graph. This dictionary will later be used for actually running the training operations etc.
* And that’s all! Our model is ready to be trained. Remember that all the objects we defined so far are nodes or operators that are part of the TensorFlow graph. To evaluate them, we actually need to execute them in a session. Simply run

```
with tf.Session() as sess:
    for i in range(num_batches):
        _, loss_val = sess.run([train_op, loss])
```

* Notice how we don’t need to feed data to the session as the `tf.data` nodes automatically iterate over the dataset! At every iteration of the loop, it will move to the next batch (remember the `tf.data` part), compute the loss, and execute the `train_op` that will perform one update of the weights!
* For more details, have a look at the `model/training.py` file that defines the `train_and_evaluate` function.

#### Putting input\_fn and model\_fn together

* To summarize the different steps, we just give a high-level overview of what needs to be done in train.py

```
#1. Create the iterators over the Training and Evaluation datasets
train_inputs = input_fn(True, train_filenames, train_labels, params)
eval_inputs = input_fn(False, eval_filenames, eval_labels, params)

#2. Define the model
logging.info("Creating the model...")
train_model_spec = model_fn('train', train_inputs, params)
eval_model_spec = model_fn('eval', eval_inputs, params, reuse=True)

#3. Train the model (where a session will actually run the different ops)
logging.info("Starting training for {} epoch(s)".format(params.num_epochs))
train_and_evaluate(train_model_spec, eval_model_spec, args.model_dir, params, args.restore_from)
```

The `train_and_evaluate` function performs a given number of epochs (= full pass on the `train_inputs`). At the end of each epoch, it evaluates the performance on the development set (`dev` or `train-dev` in the course material).

Remember the discussion about different graphs for Training and Evaluation. Here, notice how the `eval_model_spec` is given the `reuse=True` argument. It will make sure that the nodes of the Evaluation graph which must share weights with the Training graph **do** share their weights.

#### Evaluation and tf.metrics

[TensorFlow doc](https://www.TensorFlow.org/api_docs/python/tf/metrics)

* So far, we’ve explained how we input data to the graph, how we define the different nodes and training ops, but we don’t know (yet) how to compute some metrics on our dataset. There are basically 2 possibilities

1. **[run evaluation outside the TensorFlow graph]** Evaluate the prediction over the dataset by running `sess.run(prediction)` and use it to evaluate your model (without TensorFlow, with pure python code). This option can also be used if you need to write a file with all the predictions and use a script (distributed by a conference for instance) to evaluate the performance of your model.
2. **[use TensorFlow]** As the above method can be quite complicated for simple metrics, TensorFlow luckily has some built-in tools to run evaluation. Again, we are going to create nodes and operations in the Graph. The concept is simple: we will use the `tf.metrics` API to build those, the idea being that we need to update the metric on each batch. At the end of the epoch, we can just query the updated metric!

* We’ll cover method 2 as this is the one we implemented in the code examples (but you can definitely go with option 1 by modifying `model/evaluation.py`). As most of the nodes of the graph, we define these metrics nodes and ops in `model/model_fn.py`.

```
# Define the different metrics
with tf.variable_scope("metrics"):
    metrics = {'accuracy': tf.metrics.accuracy(labels=labels, predictions=predictions,
              'loss': tf.metrics.mean(loss)}

# Group the update ops for the tf.metrics, so that we can run only one op to update them all
update_metrics_op = tf.group(*[op for _, op in metrics.values()])

# Get the op to reset the local variables used in tf.metrics, for when we restart an epoch
metric_variables = tf.get_collection(tf.GraphKeys.LOCAL_VARIABLES, scope="metrics")
metrics_init_op = tf.variables_initializer(metric_variables)
```

* Note that we defined the metrics, a grouped update op and an initializer. The use of the `*` in [`tf.group`](https://www.TensorFlow.org/api_docs/python/tf/GraphKeys) is a pythonic way to tell that the argument given to the function corresponds to an optional positional argument.
* Also note how we defined the metrics in a special `variable_scope` so that we can query the variables by name when we create the initializer! When you create nodes, the variables are added to some pre-defined collections of variables (TRAINABLE\_VARIABLES, etc.). The variables we need to reset for `tf.metrics` are in the [`tf.GraphKeys.LOCAL_VARIABLES`](https://www.TensorFlow.org/api_docs/python/tf/GraphKeys) collection. Thus, to query the variables, we get the collection of variables in the right scope!
* Now, to evaluate the metrics on a dataset, we’ll just need to run them in a session as we loop over our dataset

```
with tf.Session() as sess:
    #Run the initializer to reset the metrics to zero
    sess.run(metrics_init_op)

    #Update the metrics over the dataset
    for _ in range(num_steps):
        sess.run(update_metrics_op)

    #Get the values of the metrics
    metrics_values = {k: v[0] for k, v in metrics.items()}
    metrics_val = sess.run(metrics_values)
```

* That’s all! If you want to compute new metrics for which you can find a [TensorFlow implementation](https://www.TensorFlow.org/api_docs/python/tf/metrics), you can define it in the `model_fn.py` (add it to the `metrics` dictionary). It will automatically be updated during the training and will be displayed at the end of each epoch.

## TensorFlow Tips and Tricks

### Be careful with initialization

* So far, we mentioned 3 different initializer operators.

```
#1. For all the variables (the weights etc.)
tf.global_variables_initializer()

#2. For the dataset, so that we can chose to move the iterator back at the beginning
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()
iterator_init_op = iterator.initializer

#3. For the metrics variables, so that we can reset them to 0 at the beginning of each epoch
metrics_init_op = tf.variables_initializer(metric_variables)
```

* During `train_and_evaluate` we perform the following schedule, all in one session:
  1. Loop over the training set, updating the weights and computing the metrics
  2. Loop over the evaluation set, computing the metrics
  3. Go back to step 1.
* We thus need to run:
  + `tf.global_variable_initializer()` at the very beginning (before the first occurrence of step 1)
  + `iterator_init_op` at the beginning of every loop (step 1 and step 2)
  + `metrics_init_op` at the beginning of every loop (step 1 and step 2), to reset the metrics to zero (we don’t want to compute the metrics averaged over the different epochs or different datasets!)
* You can indeed check that this is what we do in `model/evaluation.py` or `model/training.py` when we actually run the graph!

### Saving

* How do you re-use the weights once you’ve trained a model? Also, maybe at some point of the training, if the performance on the validation set started to get worse, we might want to use the best weights during training.
* Saving models is easy in TensorFlow. Look at the outline below:

```
#We need to create an instance of saver
saver = tf.train.Saver()

for epoch in range(10):
    for batch in range(10):
        _ = sess.run(train_op)

    #Save weights
    save_path = os.path.join(model_dir, 'last_weights', 'after-epoch')
    saver.save(sess, last_save_path, global_step=epoch + 1)
```

* There is not much to say, except that the `saver.save()` method takes a session as input. In our implementation, we use 2 savers. A `last_saver = tf.train.Saver()` that will keep the weights at the end of the last 5 epochs and a `best_saver = tf.train.Saver(max_to_keep=1)` that only keeps one checkpoint corresponding to the weights that achieved the best performance on the validation set!
* Later on, to restore the weights of your model, you need to reload the weights thanks to a saver instance, as in

```
with tf.Session() as sess:
    #Get the latest checkpoint in the directory
    restore_from = tf.train.latest_checkpoint("model/last_weights")
    #Reload the weights into the variables of the graph
    saver.restore(sess, restore_from)
```

* For more details, check out TensorFlow’s [official documentation](https://www.TensorFlow.org/guide/saved_model)

### TensorBoard

* TensorFlow comes with an excellent visualization tool called **TensorBoard** that enables you to plot different scalars (and much more) in real-time, as you train your model.
* TensorBoard follows the following steps:
  1. Define some summaries (nodes of the graph) that will tell TensorFlow which values we want to plot.
  2. Evaluate these nodes in the `session`.
  3. Write the output to a file thanks to a `tf.summary.FileWriter`.
* To launch TensorBoard in your web-browser, run:

```
TensorBoard --logdir="expirements/base_model"
```

* Navigate to <http://127.0.0.1:6006/> and you’ll see the different plots.
* In the code examples, we add the summaries in `model/model_fn.py`.

```
# Compute different scalars to plot
loss = tf.reduce_mean(losses)
accuracy = tf.reduce_mean(tf.cast(tf.equal(labels, predictions), tf.float32))

# Summaries for training
tf.summary.scalar('loss', loss)
tf.summary.scalar('accuracy', accuracy)
```

* Note that we don’t use the metrics that we defined earlier. The reason being that the `tf.metrics` returns the running average, but TensorBoard already takes care of the smoothing, so we don’t want to add any additional smoothing. It’s actually rather the opposite: we are interested in real-time progress
* Once these nodes are added to the `model_spec` dictionary, we need to evaluate them in a session. In our implementation, this is done every `params.save_summary_steps` as you’ll notice in the `model/training.py` file.

```
if i % params.save_summary_steps == 0:
    #Perform a mini-batch update
    _, _, loss_val, summ, global_step_val = sess.run([train_op, update_metrics, loss, summary_op, global_step])
    #Write summaries for TensorBoard
    writer.add_summary(summ, global_step_val)

else:
    _, _, loss_val = sess.run([train_op, update_metrics, loss])
```

* You’ll notice that we have two different writers:

```
train_writer = tf.summary.FileWriter(os.path.join(model_dir, 'train_summaries'), sess.graph)
eval_writer = tf.summary.FileWriter(os.path.join(model_dir, 'eval_summaries'), sess.graph)
```

* They’ll write summaries for both the training and the evaluation, letting you plot both plots on the same graph!
* For more details, check out TensorFlow’s [official documentation](https://www.TensorFlow.org/guide/summaries_and_tensorboard)

### Writing a custom activation function

* To define a custom activation function, say `min_relu()` that returns \(min(0, -z)\) (instead of ReLU that returns \(max(0, z)\)):

```
def min_relu(x):
    return - tf.keras.activations.relu(-x)

tf.keras.utils.get_custom_objects().update({'min-relu': Activation(min_relu)})
```

* An example using the newly defined activation function `min_relu()`:

```
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(512, activation='min-relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])
```

### Model summary

* Call `tf.keras.Model.summary()` to print a summary of the model, which includes:
  + Name and type of all layers in the model.
  + Output shape for each layer.
  + Number of weight parameters of each layer.
  + The total number of trainable and non-trainable parameters of the model.

```
Model Summary:
____________________________________________________________________________________________________
Layer (type)                     Output Shape          Param #     Connected to                     
====================================================================================================
input_1 (InputLayer)             (None, 1, 15, 27)     0                                            
____________________________________________________________________________________________________
convolution2d_1 (Convolution2D)  (None, 8, 15, 27)     872         input_1[0][0]                    
____________________________________________________________________________________________________
maxpooling2d_1 (MaxPooling2D)    (None, 8, 7, 27)      0           convolution2d_1[0][0]            
____________________________________________________________________________________________________
flatten_1 (Flatten)              (None, 1512)          0           maxpooling2d_1[0][0]             
____________________________________________________________________________________________________
dense_1 (Dense)                  (None, 1)             1513        flatten_1[0][0]                  
====================================================================================================
Total params: 2,385
Trainable params: 2,385
Non-trainable params: 0
```

* Note that the `None` values in the output shapes of the layers indicate that the model expects the input to have a batch size as the outermost dimension, which in this case can be flexible due to the `None` value.
* Read more on TensorFlow’s [official documentation](https://www.tensorflow.org/api_docs/python/tf/keras/Model).

### global\_step

* In order to keep track of where we are in the training process, we use one of TensorFlow’s training utilities, the `global_step`.
* Once initialized, we give it to the `optimizer.minimize()` as shown below. Thus, each time we will run `sess.run(train_op)`, it will increment the global\_step by 1.
* This is very useful for summaries (notice how in the [TensorBoard](#tensorboard) section, we give the global step to the `writer`).

```
global_step = tf.train.get_or_create_global_step()
train_op = optimizer.minimize(loss, global_step=global_step)
```

* For more details, check out TensorFlow’s [official documentation](https://www.TensorFlow.org/api_docs/python/tf/train/Optimizer#minimize)

## References

* CS230 class notes from Spring 2019.
* [TensorFlow documentation: tf.keras.Model](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
* [How can I use tf.keras.Model.summary to see the layers of a child model which in a father model?](https://stackoverflow.com/questions/58657003/how-can-i-use-tf-keras-model-summary-to-see-the-layers-of-a-child-model-which-in)
