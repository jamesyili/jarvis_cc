# NLP • Pipeline

**Source:** https://aman.ai/primers/ai/pipeline/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Data Collection](#data-collection)
* [Preprocessing](#preprocessing)
* [Tokenization](#tokenization)
* [Embedding](#embedding)
* [Model Architecture](#model-architecture)
* [Prediction](#prediction)
* [Token Sampling (Decoding)](#token-sampling-decoding)
* [De-tokenization/ De-coding/ De-embedding](#de-tokenization-de-coding-de-embedding)
* [Postprocessing](#postprocessing)
* [Evaluation](#evaluation)

## Overview

* Here, we will look at a step-by-step example of how an NLP pipeline can work, with a focus on autoregressive language models like GPT-3, which are often used for tasks like text generation.
* Each step will be linked with it’s corresponding article to help you dive deep into the subject.
* Note that this pipeline can be adapted for different tasks. For example, for tasks like text classification or named entity recognition, the pipeline might also include a step to label the data for supervised learning, and the model’s task would be to predict these labels instead of generating new text.

## Data Collection

* Gather the text data you want to use for training the model. This could be a set of books, a collection of web pages, academic papers, etc.
* Data collection for NLP involves the gathering of text data that will be used to train, validate, or test your NLP models. Here are some common methods and considerations:
  1. Public Datasets: There are numerous public datasets available for different NLP tasks. For example, the Stanford Sentiment Treebank for sentiment analysis, SQuAD for question-answering tasks, or the Penn Treebank for syntactic parsing.
  2. Web Scraping: You can scrape websites to collect data. Common sources include news websites, social media platforms, and online forums. However, always respect the website’s terms of service and privacy policies when scraping.
  3. APIs: Many online platforms like Twitter or Reddit provide APIs that allow you to collect data programmatically. Like with web scraping, ensure you are complying with the platform’s usage policies.
  4. Surveys and Manual Collection: Sometimes, you might need to collect data manually. For example, if you’re building a chatbot, you might ask human agents to engage in conversation and record their interactions.
  5. Data Augmentation: You can generate synthetic data by modifying existing data. For example, you can translate text to a different language and back, replace words with their synonyms, or rearrange words in a sentence.
  6. Purchase or License Data: There are companies and organizations that sell or license their data for research or commercial use. This can be an easy way to get high-quality, domain-specific data.
  7. Annotating Collected Data: For supervised learning tasks, you’ll need labeled data. Sometimes, you might need to manually annotate the data, or hire annotators to do it.

## [Preprocessing](/preproc)

* Prepare the text for training. This often involves steps like removing unnecessary characters or symbols, standardizing the text to a consistent format (like converting everything to lowercase), etc.

## [Tokenization](/tokenizer)

* Break the text into individual tokens, which could be words, sub-words, or characters, depending on the chosen tokenization strategy (WordPiece, SentencePiece, Byte-Pair Encoding, etc.).
* This process often includes mapping tokens to their respective unique IDs for processing by the model.

## [Embedding](/embedding)

* Each token is converted into a high-dimensional vector that represents the token in a way that captures its meaning and relationships with other tokens.
* These embeddings are usually learned during training but can also be initialized with pre-trained embeddings.

## [Model Architecture](/nlp-architectures)

* Train the model on the processed data using a variety of architectures depending on the problem at hand.
* The model learns to predict the next token in a sequence based on the previous tokens.
* This involves adjusting the model’s parameters to minimize the difference between its predictions and the actual tokens.

## Prediction

* After the model is trained, it can be used to identify named entities in new, unlabelled text. The model calculates a probability distribution over the possible labels for each token and picks the label with the highest probability.
* In NLP, once the model has been trained, it makes prediction on a set of unseen data via it’s trained model. This can take many forms, depending on the specific task at hand. Here are a few examples:
  1. Text Classification: The model predicts the category or label of a given text. For example, in sentiment analysis, the model might predict whether a given review is positive or negative.
  2. Named Entity Recognition (NER): The model predicts which parts of the text correspond to named entities such as people, places, or organizations.
  3. Machine Translation: The model predicts the translation of a sentence in one language to another language.
  4. Language Modeling: The model predicts the next word or words in a sequence. This is a fundamental task in many NLP applications, including autocomplete and chatbots.
  5. Question Answering: The model predicts the answer to a question based on a given context.

## [Token Sampling (Decoding)](../concepts/token-sampling)

* After the model is trained, it can generate new text. To do this, it calculates a probability distribution over the vocabulary for the next token, and then samples a token from that distribution. The sampling method (like greedy decoding, beam search, top-k sampling, etc.) can significantly impact the text’s quality.

## De-tokenization/ De-coding/ De-embedding

* Once the tokens have been generated, they are converted back into human-readable text.
* Detokenization is the process of reconstructing a sentence or text from its tokens. It’s essentially the reverse operation of tokenization.
* In tokenization, you break down text into smaller pieces called tokens, usually words or phrases. These tokens help machines understand our language by making it more structured and less complicated.
* However, once we have performed computations or transformations on these tokens and we want to convert them back into a format that is human-readable, we use detokenization.
* Here’s a simple example in Python using the NLTK library:

```
from nltk.tokenize.treebank import TreebankWordDetokenizer

tokens = ['Hello', ',', 'world', '!']
detokenizer = TreebankWordDetokenizer()
sentence = detokenizer.detokenize(tokens)
print(sentence)
```

Output:

```
Hello, world!
```

* In this example, we first create a list of tokens. Then we initialize a detokenizer from NLTK’s `TreebankWordDetokenizer` class. Finally, we use the `detokenize` method on our tokens to produce a complete, human-readable sentence.
* Keep in mind, the complexity of detokenization can greatly vary based on the language and the specific tokenization technique used. For example, in languages where words are often joined together, the detokenization process can be quite complex.

## Postprocessing

* Post-processing in NLP refers to the various techniques and methods applied to the output of NLP models to make them more useful, coherent, and aligned with specific application requirements. Here are some common post-processing steps:
  1. Error correction: Sometimes, NLP models, especially those dealing with text generation, might produce grammatically incorrect sentences or have spelling errors. Post-processing can involve a spell check or grammar correction step to rectify these errors.
  2. Detokenization: As discussed before, detokenization is the process of converting a sequence of tokens back into human-readable text. This is a common post-processing step following tasks like text generation, translation, etc.
  3. Text formatting: Based on the specific application, you might need to format the generated text in a certain way, such as adding punctuation, capitalizing certain words, or inserting paragraph breaks.
  4. Pruning: In tasks like named entity recognition or POS tagging, the model might produce multiple possible tag sequences with associated probabilities. Pruning involves discarding low-probability sequences to simplify the output.
  5. Contextual Rules: Sometimes, specific contextual rules might be applied to the output, especially in domain-specific applications. For example, in a medical NLP application, any drug name might need to be replaced with its generic equivalent in the final output.
  6. Decoding strategies in text generation: Techniques like beam search, nucleus sampling, or temperature tuning are often applied during the generation of text to control the diversity and quality of the output.

## [Evaluation](/metrics)

* Finally, the model’s performance is evaluated on a separate test dataset. Common evaluation metrics for NER include precision, recall, and F1 score.
