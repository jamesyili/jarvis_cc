# Natural Language Processing • Language Models

**Source:** https://aman.ai/primers/ai/language-model/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** llms, ml-fundamentals

---

* [Language Modeling and Recurrent Neural Networks (RNN)](#language-modeling-and-recurrent-neural-networks-rnn)
* [N-gram language models](#n-gram-language-models)
* [Neural Language Model](#neural-language-model)
* [Evaluating language models](#evaluating-language-models)
* [Contextual Embeddings](#contextual-embeddings)
* [ELMo: Embeddings from Language Models](#elmo-embeddings-from-language-models)
* [GPT-3: Generative Pre-trained Transformer 3](#gpt-3-generative-pre-trained-transformer-3)
* [Citation](#citation)

## Language Modeling and Recurrent Neural Networks (RNN)

* Language modeling involves predicting the next word in a sequence based on the context of the preceding words.
* A language model, like Gboard or a query completion system, assigns probabilities to text sequences, effectively creating a probability distribution over the next word given the context.

## N-gram language models

* An n-gram language model chunks a text into n consecutive words (4-gram, 5-gram), making a Markov assumption that to predict word t+1, only the last n-1 words are necessary.
* For instance, a 4-gram model would only consider the last three words. However, if the model doesn’t encounter a specific data sequence within its window, it assigns a probability of zero.
* Furthermore, n-grams can lack context and coherence, as they only consider 3-4 words at a time, leading to a sparsity problem.
* The below slide [(source)](https://web.stanford.edu/class/cs224n/) depicts this.

## Neural Language Model

* Unlike n-gram models, a neural language model takes a sequence of words as input and outputs a probability distribution of the next word.
* Early models were window-based, focusing on a fixed range of preceding words and discarding those farther away, but these were only precursors to the more advanced RNN models.

## Evaluating language models

* Perplexity is the standard metric for evaluating language models, with lower scores indicating better performance.

## Contextual Embeddings

* While traditional word embeddings in NLP are context-free, meaning a word like “bank” would have the same representation regardless of context (e.g., river bank vs. financial institution), contextual embeddings provide a solution.
* These generate different representations based on the surrounding text.

## ELMo: Embeddings from Language Models

* ELMo (Peters et al., 2018) introduced contextualized word embeddings.
* Instead of using a fixed embedding for each word, ELMo takes the entire sentence into account before assigning each word an embedding.
* This is achieved through a bidirectional LSTM trained on a specific task. ELMo, therefore, can assign different representations to the same word based on its context.
* The below slide [(source)](https://web.stanford.edu/class/cs224n/) depicts this.

## GPT-3: Generative Pre-trained Transformer 3

* GPT-3 is a powerful language model that predicts the probability of the next word given a context.
* Its novelty lies in its ability for flexible “in-context” learning.
* It demonstrates rapid adaptation to completely new tasks through in-context learning, essentially learning how to learn from the context.
* GPT-3 can also be used as a knowledge base, given its vast training data and ability to generate contextually relevant responses.

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2021Distilled,
  title   = {Language Models},
  author  = {Jain, Vinija and Chadha, Aman},
  journal = {Distilled Notes for Stanford CS224n: Natural Language Processing with Deep Learning},
  year    = {2021},
  note    = {\url{https://aman.ai}}
}
```
