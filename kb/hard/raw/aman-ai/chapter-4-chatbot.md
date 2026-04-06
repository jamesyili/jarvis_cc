# Chapter 4 - Chatbot

**Source:** https://aman.ai/h/des/chatbot/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Clarifying Requirements](#clarifying-requirements)
* [Frame the Problem as an ML Task](#frame-the-problem-as-an-ml-task)
  + [Specifying the system’s input and output](#specifying-the-systems-input-and-output)
  + [Choosing a suitable ML approach](#choosing-a-suitable-ml-approach)
* [Data Preparation](#data-preparation)
* [Model Development](#model-development)
  + [Architecture](#architecture)
  + [Positional encoding](#positional-encoding)
  + [Absolute positional encoding](#absolute-positional-encoding)
  + [Relative positional encoding](#relative-positional-encoding)
  + [Rotary positional encoding (RoPE)](#rotary-positional-encoding-rope)
    - [Pros](#pros)
    - [Cons](#cons)
* [Training](#training)
  + [Pretraining](#pretraining)
    - [Pretraining data](#pretraining-data)
    - [ML objective and loss function](#ml-objective-and-loss-function)
    - [The outcome of the pretraining stage](#the-outcome-of-the-pretraining-stage)
  + [Supervised finetuning (SFT)](#supervised-finetuning-sft)
    - [Training data](#training-data)
    - [ML objective and loss function](#ml-objective-and-loss-function-1)
    - [The outcome of the SFT stage](#the-outcome-of-the-sft-stage)
  + [RLHF](#rlhf)
    - [Training a reward model](#training-a-reward-model)
      * [Reward model architecture](#reward-model-architecture)
      * [Training data](#training-data-1)
      * [ML objective and loss function](#ml-objective-and-loss-function-2)
      * [The outcome of reward modeling](#the-outcome-of-reward-modeling)
    - [Optimizing the SFT model](#optimizing-the-sft-model)
      * [Training data](#training-data-2)
      * [ML objective and loss function](#ml-objective-and-loss-function-3)
    - [The outcome of RLHF](#the-outcome-of-rlhf)
* [Sampling](#sampling)
  + [Deterministic methods](#deterministic-methods)
    - [Greedy search](#greedy-search)
    - [Beam search](#beam-search)
  + [Stochastic methods](#stochastic-methods)
    - [Multinomial sampling](#multinomial-sampling)
    - [Top-k sampling](#top-k-sampling)
    - [Top-p (nucleus) sampling](#top-p-nucleus-sampling)
    - [Temperature](#temperature)
    - [What are typical temperature values?](#what-are-typical-temperature-values)
    - [Repetition penalty](#repetition-penalty)
* [Evaluation](#evaluation)
  + [Offline evaluation metrics](#offline-evaluation-metrics)
    - [Traditional evaluation](#traditional-evaluation)
    - [Task-specific evaluation](#task-specific-evaluation)
      * [Common-sense reasoning](#common-sense-reasoning)
      * [World knowledge](#world-knowledge)
      * [Reading comprehension](#reading-comprehension)
      * [Mathematical reasoning](#mathematical-reasoning)
      * [Code generation](#code-generation)
      * [Composite benchmarks](#composite-benchmarks)
    - [Safety evaluation](#safety-evaluation)
      * [Toxicity and harmful content](#toxicity-and-harmful-content)
      * [Bias and fairness](#bias-and-fairness)
      * [Truthfulness](#truthfulness)
      * [User privacy and data leakage](#user-privacy-and-data-leakage)
      * [Adversarial robustness](#adversarial-robustness)
    - [Human evaluation](#human-evaluation)
  + [Online evaluation metrics](#online-evaluation-metrics)
* [Overall ML System Design](#overall-ml-system-design)
  + [Training pipeline](#training-pipeline)
  + [Inference pipeline](#inference-pipeline)
    - [Safety filtering](#safety-filtering)
    - [Prompt enhancer](#prompt-enhancer)
    - [Response generator](#response-generator)
    - [Response safety evaluator](#response-safety-evaluator)
    - [Rejection response generator](#rejection-response-generator)
    - [Session management](#session-management)
* [Other Talking Points](#other-talking-points)
* [Summary](#summary)
* [Reference Material](#reference-material)

## Overview

* ChatGPT [1] is a chatbot that was developed by OpenAI and launched in 2022. It generates human-like text based on the input it receives. The chatbot can assist with various tasks, including answering questions, providing explanations, and producing creative content.
* ChatGPT has quickly become one of the most adopted applications in history. It gained over 100 million users in less than three months after its launch [2]. This rapid growth highlights the capabilities of generative AI and its potential to help with day-to-day tasks and enhance productivity. In this chapter, we examine the key components of building a chatbot similar to ChatGPT.

## Clarifying Requirements

* Here is a typical interaction between a candidate and an interviewer:

  **Candidate**: What languages should the chatbot support?
  **Interviewer**: Initially, let’s focus on English.

  **Candidate**: We need to ensure the chatbot generates unbiased and safe outputs by having strict content moderation and algorithms in place. Is that a fair assumption?
  **Interviewer**: Certainly.

  **Candidate**: Can you specify the range of tasks the chatbot is expected to perform?
  **Interviewer**: The chatbot should be able to handle tasks like providing information and answering questions.

  **Candidate**: Does the chatbot take in or output non-text modalities, such as image, audio, or video?
  **Interviewer**: Let’s focus on a text-only chatbot for now. The input and the output are both text.

  **Candidate**: Should the chatbot handle follow-up questions? How long should the chatbot maintain the conversation context?
  **Interviewer**: Good question. The chatbot should be able to handle follow-up questions within the same conversation session. Let’s say it is expected to have a context window of at least 4096 tokens.

  **Candidate**: Is the chatbot expected to be able to browse websites, call external API, or search online?
  **Interviewer**: Let’s not focus on that in this round.

  **Candidate**: Should the chatbot personalize its interactions with users?
  **Interviewer**: Let’s not focus on personalization.

  **Candidate**: Do we have instruction-based training data?
  **Interviewer**: Yes, we have a dataset with 80,000 examples of instructions and answers.

## Frame the Problem as an ML Task

### Specifying the system’s input and output

* The input to the chatbot is a text prompt provided by the user. The prompt can be a question, a command, or any other form of textual query. The output is a relevant and contextually appropriate response generated by the chatbot.

### Choosing a suitable ML approach

* Developing a chatbot is a text generation task in which a language model processes an input prompt and generates a response. This language model typically needs billions of parameters to learn effectively; hence, they are often called large language models (LLMs).
* As we saw in previous chapters, the decoder-only Transformer is the standard architectural choice in language models. Most modern LLMs, such as OpenAI’s GPT [3], Google’s Gemini [4], and Meta’s Llama [5], are all based on the decoder-only Transformer. In line with these models, we use a decoder-only Transformer to build our chatbot.

## Data Preparation

* The effectiveness of an LLM depends on the quality of its training data, which mainly comes from web sources. This data, often automatically crawled from websites, forums, and blogs, requires special considerations and careful preparation. The most common steps include:

  + **Content extraction and parsing**
    Web-crawled data often contains extraneous elements, for example, HTML tags, advertisements, and navigation links. This step involves parsing the raw HTML content using libraries such as Beautiful Soup [6] or lxml [7] and extracting the main text body while discarding irrelevant sections. Techniques such as DOM analysis [8] and boilerplate detection [9] are applied to isolate and retain the core content relevant to language modeling.
  + **URL and domain filtering**
    Not all web domains provide high-quality or relevant content. URL filtering uses predefined rules or machine learning (ML) classifiers to exclude unwanted sources, for example, low-quality blogs, content farms, or spam sites. Domain allowlisting or blocklisting techniques are also applied to curate data from trusted and relevant sources, ensuring the dataset’s quality and reliability.
  + **Language identification**
    Crawled data often includes multilingual content, which needs to be filtered to match the target language(s) for training. Language detection tools such as fastText [10] or langid.py [11] are employed to classify and filter documents.
  + **Content quality filtering**
    Not all web content is equally valuable for training purposes. Quality assessment techniques, including readability scoring, spam detection algorithms, and heuristic checks (e.g., content length, sentence structure), are used to evaluate and filter low-quality text. ML models can also be employed to predict the quality of web content based on features extracted from the text. This step is crucial to ensure that only high-quality data is used for training.
* Along with these techniques, the following are commonly applied to both web-crawled data and other data sources, such as books, articles, and social media posts:

  + **Remove inappropriate content:** We use ML models to remove offensive, harmful, or NSFW content from training data. This ensures our model learns only appropriate and safe content.
  + **Anonymize sensitive information:** We anonymize any personally identifiable information (PII) in the dataset. This step is crucial to comply with privacy laws and ethical guidelines.
  + **Remove low-quality data:** We use ML models to remove low-quality text data. The models assess coherence, relevance, grammar, and readability. This step ensures the training data is high in quality and useful for training.
  + **Remove duplicated data (Deduplication):** We remove similar texts that might be present in different sources. For example, if the same news article is collected from multiple websites, we identify and retain only one copy. This step reduces redundancy in the training dataset and ensures the model is not overexposed to certain data.
  + **Remove irrelevant data:** We use heuristics and rule-based methods to remove irrelevant data. For example, we remove texts with non-standard characters or in languages that the chatbot is not expected to support.
  + **Tokenize text:** We use a subword tokenization algorithm such as Byte-Pair Encoding (BPE) to tokenize the text data. To review BPE, refer to Chapter 3.

## Model Development

### Architecture

* The LLM’s architecture is based on a decoder-only Transformer. While the text embedding, Transformer blocks, and the prediction head are similar to the decoder-only Transformer discussed in Chapter 2, LLMs typically use more advanced positional encoding methods.
* The following figure shows the components of a decoder-only Transformer:

* Let’s examine LLM’s positional encoding in more detail.

### Positional encoding

* In a chatbot setting, the input sequence is typically much longer than a single sentence or email. As per the interviewer’s requirements, our goal is to build a system with a context window of at least 4096 tokens. This requires a positional encoding method that allows the model to understand the positions of all the tokens and the relationships between them.
* In this section, we begin with a brief review of absolute positional encoding followed by an exploration of relative positional encoding. Finally, we delve into rotary positional embedding (RoPE) [12], a robust positional encoding method used by popular LLMs such as Llama 3 [13].

### Absolute positional encoding

* Absolute positional encoding refers to traditional methods such as sinusoidal or learnable encodings whereby each position in a sequence is represented by a unique vector.
* In this approach, encoded positions are then added to the token embeddings, providing the model with information about where each token appears in the sequence. Formally, the attention keys and queries are computed using the following equations:

  \[q\_m = W\_q (e\_m + p\_m)\]
  \[k\_n = W\_k (e\_n + p\_n)\]
  + Where:

    - \(q\_m\) is the query vector at position \(m\),
    - \(k\_n\) is the key vector at position \(n\),
    - \(W\_q\) and \(W\_k\) are learnable weight matrices,
    - \(e\_m\) and \(e\_n\) are token embeddings at positions \(m\) and \(n\),
    - \(p\_m\) and \(p\_n\) are positional vectors (either learnable or fixed) at positions \(m\) and \(n\).
* The attention score is calculated as a dot product of the query and key vectors:

\[q\_m \cdot k\_n = e\_m W\_q W\_k e\_n + e\_m W\_q W\_k p\_n + p\_m W\_q W\_k e\_n + p\_m W\_q W\_k p\_n\]

* Notice that positional encodings \(p\_m\) and \(p\_n\) depend only on absolute positions. Therefore, this approach captures only information about absolute position, limiting the model’s ability to capture relative distances between tokens and generalize to sequences with different lengths or unseen token positions. For example, a model trained on sequences of up to 512 tokens may struggle to generalize when applied to sequences with 4096 tokens. The sinusoidal patterns tend to become repetitive over long distances, resulting in a loss of information about token relationships. This shortcoming is addressed by relative positional encoding.

### Relative positional encoding

* In relative positional encoding, instead of encoding the absolute positions of tokens, we encode the differences in the positions of two tokens. This way, the model can focus on the relative distances between tokens, which is often more important than their absolute positions. For example, in a sentence, knowing that the word “car” follows the word “chased” is more informative than knowing the positions of the tokens as numbers 5 and 10.
* The attention calculation in relative positional encoding can be expressed in different ways. The T5 paper [14] suggests that the second and the third interaction terms in the original expression in absolute positional encoding can be dropped and that the fourth term could be replaced by a learnable bias.
* The following figure shows the modified attention calculation from the T5 paper:

* In contrast, the DeBerta paper [15] drops the last term and replaces the second and third terms, which consist of the absolute positional vectors \(p\_m\) and \(p\_n\), respectively, with the relative positional vector \(R\_{n-m}\):

\[\text{score}(m,n) = q\_m \cdot k\_n + q\_m \cdot R\_{n-m}\]

* Relative positional encoding allows the model to understand the relationships between tokens independently of their absolute positions. However, it introduces additional complexity because \(q\_m \cdot k\_n\) in the attention mechanism can no longer be reduced to a simple dot product. This limits our ability to use efficient techniques such as linear attention [16].
* Rotary positional embedding (RoPE), which we examine next, addresses this limitation by encoding both absolute and relative positional information through a rotation in the embedding space.

### Rotary positional encoding (RoPE)

* RoPE represents positional information as a rotation matrix applied to the token embeddings. This can be described mathematically as follows: Given an input sequence, RoPE applies a rotation matrix to each embedding. This transformation can be expressed as:

  \[q\_m^{'} = R(\theta\_m) \cdot q\_m\]
  + where \(q\_m\) is token embedding at the position \(m\), and \(R(\theta)\) is a rotation matrix parameterized by the positional angle \(\theta\_m\). This angle is typically derived from the position index \(m\) and is constructed in such a way that the rotation captures both the absolute and relative position information. This rotation matrix, constructed using trigonometric functions, rotates the embeddings in the complex plane, capturing both absolute and relative positional information.
* The following figure shows RoPE in 2D:

* Figure 4.4 shows how rotational position encoding works by rotating word embeddings in a two-dimensional space. The words “cat” and “dog” are represented as vectors, and the angle between them, denoted by \(\theta\), encodes their positional relationship. On the left, the sentence is “The cat chased the dog.” The position of “cat” is shown in red, and the position of “dog” is shown in blue. The angle between these vectors captures the relative positioning of these two words in the sentence.
* On the right, another sentence “Once upon a time, the cat chased the dog” is shown. Notice that the relative angle \(\theta\) between the “cat” and “dog” vectors is still the same, but their absolute positions are different. This demonstrates how RoPE captures both the absolute and relative positions of words, allowing the model to understand the order and distance between words in a sentence.
* In a higher-dimensional space, the rotation matrix can be extended to accommodate \(d\) dimensions.
* The following figure shows the RoPE high-dimensional rotation matrix:

#### Pros

* **Translational invariance:** RoPE encodes positional information in a way that remains consistent even when the positions of tokens shift. This helps the model handle changes in position better than other methods.
* **Relative position representation:** RoPE’s rotations encode positional information geometrically within the embedding space. This enables the model to inherently understand the relative distances between tokens, unlike traditional sinusoidal encodings, which encode position additively without leveraging this geometric insight.
* **Generalization to unseen positions:** Because RoPE encodes position through rotations, the resulting embeddings maintain consistent relationships, regardless of absolute position. This allows for better generalization across varying sequence lengths.

#### Cons

* **Increased computational cost:**
  RoPE involves additional mathematical operations (rotations) on the embeddings, which can increase computational complexity and slow down training and inference.
* **Implementation complexity:**
  Implementing RoPE correctly requires careful handling of the rotation matrix and its interaction with the attention mechanism, which can complicate the model architecture compared to simpler positional encoding methods.
* **Compatibility limitations:**
  Some efficient attention mechanisms (like linear attention) may not be directly compatible with RoPE, requiring modifications or alternative approaches.

## Training

* In earlier chapters, we explored a two-stage strategy for training language models. However, those stages are not sufficient when training advanced chatbots. Most chatbots, including ChatGPT, use a three-stage training strategy:

  1. Pretraining
  2. Supervised finetuning (SFT)
  3. Reinforcement learning from human feedback (RLHF)
* Let’s discuss each stage in more detail to understand its purpose.
* The following figure shows the three stages of training an LLM.

### Pretraining

* Pretraining is the initial stage of the training process. In this stage, a model is trained with an enormous volume of text data from the Internet. The purpose of pretraining is to create a base model with a broad understanding of language and world knowledge.
* The pretraining stage requires significant computational resources. It typically requires thousands of GPUs, costs millions of dollars, and takes months of training.

#### Pretraining data

* The pretraining data typically consists of a large corpus of general text data from various sources on the Internet, for example, web pages, books, and social media posts.
* Several datasets are commonly used when pretraining LLMs. Each serves a unique purpose, from broadening the model’s exposure to diverse language styles to deepening its understanding of specific domains. Commonly used datasets are:

  + **Common Crawl:** Common Crawl [17] is a publicly available dataset collected from a large number of web pages on the internet. It contains petabytes of data that have been regularly collected since 2008. This data often includes irrelevant information and harmful content; hence, significant data cleaning is needed to make it suitable for training LLMs.
  + **C4:** C4 [18], created by Google, is a cleaned version of the Common Crawl dataset specifically used for training LLMs.
  + **GitHub:** The GitHub dataset comprises a vast collection of open-source code repositories. Its purpose is to help the model understand programming languages and code structures.
  + **Wikipedia:** The Wikipedia dataset includes a wide range of factual information extracted from Wikipedia. This dataset is generally a more reliable source because it is written and edited more carefully.
  + **Books:** The books dataset is a collection of books across various genres. Books have long textual content and good data quality, both of which contribute to improving the performance of LLMs.
  + **ArXiv:** The ArXiv dataset contains academic materials and published papers. This dataset helps the model understand the terminology and knowledge within the academic domain.
  + **Stack Exchange:** Stack Exchange [19] is a website of high-quality questions and answers, primarily in the format of a dialogue between users.
* Most popular LLMs are trained on all or some of the listed datasets. For example, Meta’s Llama 1 model uses all the above datasets, consisting of about 1.4 trillion tokens. Table 4.1 shows the proportion of each dataset used by Llama 1 during training.
* The following figure shows the Llama 1 pretraining dataset.

#### ML objective and loss function

* As we are training a decoder-only Transformer for text generation, we use the standard next-token prediction as our ML objective. For the loss function, we employ cross-entropy loss to measure the difference between the predicted token probabilities and correct tokens.

#### The outcome of the pretraining stage

* The pretraining stage produces a model that understands language well. This model, usually referred to as the base model, predicts text to follow the given input prompt, generating relevant and meaningful text.
* The following figure shows the base model continuing a sentence.

* While the base model understands language well, it is only capable of continuing on from the text prompt. To make the model a useful chatbot that answers questions, we need to further train the base model. This leads to the next stage: supervised finetuning.

### Supervised finetuning (SFT)

* SFT, also named instruction finetuning, is the second stage of the training process. In this stage, we finetune the base model on a smaller, high-quality dataset in a (prompt, response) format. The purpose of this stage is to preserve the base model’s language understanding and world knowledge while adapting its behavior to responding to prompts instead of just continuing them.

#### Training data

* The training data for the SFT stage follows the (prompt, response) format. This data is usually called demonstration data because it demonstrates to the model how to respond to prompts.
* The following figure shows an example of demonstration data.

* The main differences between demonstration data and pretraining data, aside from format, are size and quality.

  + **Size**: Demonstration data is significantly smaller than pretraining data. It usually ranges from 10,000 to 100,000 (prompt, response) pairs. Table 4.2 shows the data sizes of popular demonstration datasets.
  + The following figure shows common demonstration datasets.

* **Quality**: Demonstration data is of higher quality compared to pretraining data. The data is usually created by educated human contractors. In specialized industries such as healthcare or finance, it is essential to hire domain experts to ensure the accuracy and relevance of data. For instance, as shown in Table 4.3, over one-third of OpenAI’s labelers for GPT’s demonstration dataset held a master’s degree [20]. While this requirement is costly, it’s crucial for producing reliable, industry-specific responses.
* The following figure shows the education levels of OpenAI’s labelers.

#### ML objective and loss function

* Although the training data differs from the pretraining stage, the model still learns a similar task: generating a text one token at a time based on the input prompt. Therefore, the ML objective and loss functions remain similar to those at the pretraining stage: next-token prediction ML objective and cross-entropy loss function.
* The following figure shows loss calculation over a (prompt, response) example.

#### The outcome of the SFT stage

* The outcome of this stage is the SFT model, a finetuned version of the base model. Instead of merely continuing the text prompt, the SFT model generates detailed and helpful responses because it has been trained on demonstration data in a (prompt, response) format.
* The following figure shows that the SFT model answers a prompt instead of continuing it.

* The SFT model usually generates a grammatically correct and reasonable response. However, it might not always generate the best response; its answers can be unhelpful or even unsafe. Figure 4.11 displays four plausible responses to a question. Only the second response is both safe and helpful. The first and fourth responses are grammatically and contextually correct but do not offer accurate advice. The third response is helpful but impolite.

* To ensure the model produces relevant, safe, and helpful responses, we must further finetune the model. This further finetuning is the primary focus of the next stage: RLHF.

### RLHF

* RLHF, also known as the alignment stage, is the final stage in the training process. This stage aligns the model to human preferences, that is, it adapts the model to generate responses preferred by humans.
* To understand RLHF, let’s briefly revisit the SFT stage. In SFT, the model learns from demonstration data to produce a plausible response to a given prompt. However, demonstration data provides the model with one plausible response for a prompt, which is not necessarily the most helpful or relevant response. Usually, multiple responses can be plausible, and some will be more relevant than others, as shown in Figure 4.11.
* If we have a separate reward model that can score how relevant a model’s response is to a prompt, we can further finetune the SFT model to generate not just any plausible response but one with a high score. This is the key idea behind RLHF. RLHF consists of two sequential steps:

  1. Training a reward model
  2. Optimizing the SFT model

#### Training a reward model

* The first step in RLHF is to train a reward model that evaluates the relevance of a response to a prompt. This model takes a (prompt, response) pair as input and produces a score predicting the helpfulness of the response. The higher the score, the more helpful the response is expected to be.

##### Reward model architecture

* Training a model to output a score is a very common task in ML. There are various architectures we can employ for reward modeling: It can be a decoder-only, encoder-only, or encoder-decoder Transformer as long as it outputs a scalar value.
* Based on public studies, there isn’t a consistent pattern of reward models being larger or smaller than the language models they are used to train. For example, OpenAI uses a 6B reward model for the 175B language model [20]. Anthropic uses language models and reward models ranging from 10B to 52B parameters [24]. A typical option is to create a copy of the SFT model and add a prediction head to produce the relevance score for the given (prompt, response) pair.

##### Training data

* To collect training data for reward modeling, we follow these steps:

  1. **Collect prompts:** Manually create a list of prompts.
  2. Generate multiple responses: Use the SFT model to generate multiple responses for each prompt.
  3. **Rank responses:** Ask contractors to evaluate those responses and rank them based on their relevance. The reason they typically rank them instead of scoring each response is that ranking reduces subjectivity and inconsistency. It is easier and more intuitive for annotators to compare responses directly than to assign numerical scores, which can vary between annotators. This approach simplifies the evaluation process and ensures more reliable data for training.
  4. **Create preference pairs:** Construct the training dataset by forming pairs in the format (prompt, winning response, losing response). In each pair, the winning response is preferred over the losing response based on the rankings from the previous step.

* Once we collect the training data, where each example is in (prompt, winning response, losing response) format, we define the ML objective and the associated loss function to train our reward model.

##### ML objective and loss function

* The reward model aims to predict a higher score for the winning response compared to the losing response. More formally, for a given (prompt, winning response, losing response), the ML objective is to maximize:

  \[S\_{win} - S\_{lose}\]
  + where:

    - \(S\_{win}\) is the predicted score for the (prompt, winning response) pair
    - \(S\_{lose}\) is the predicted score for the (prompt, losing response) pair
* To achieve this ML objective, we need a loss function that penalizes the model when the difference between the winning and losing scores is too small. A commonly used loss function for this purpose is the margin ranking loss. The loss function is defined as:

\[L = \max(0, m - (S\_{win} - S\_{lose}))\]

* Where \(m\) is a hyperparameter defining the margin. This margin indicates the minimum desired difference between the scores of the winning and losing responses. If the difference between \(S\_{win}\) and \(S\_{lose}\) is less than \(m\), the optimizer will update the model parameters so that either \(S\_{win}\) increases or \(S\_{lose}\) decreases.

##### The outcome of reward modeling

* The outcome of this step is a reward model that predicts relevance scores for (prompt, response) pairs. These scores reflect human judgments and are crucial for the second step in RLHF.

#### Optimizing the SFT model

* In the second step of RLHF, the SFT model is optimized with the help of the reward model. The purpose of this step is to adapt the SFT model to generate responses that are not only plausible but also helpful, based on the scores from the reward model.
* A common approach to optimize the SFT model is to employ a reinforcement learning (RL) algorithm such as proximal policy optimization (PPO) [25], where the SFT model is finetuned to maximize the scores predicted by the reward model. This finetuning process performs the following steps iteratively:

  1. **Generate model responses:** The model generates multiple possible responses for a given prompt.
  2. **Compute rewards:** The reward model scores these responses.
  3. **Update model weights:** The RL algorithm updates model weights to maximize the expected reward. This step reinforces responses that receive higher scores from the reward model.

##### Training data

* For this step, the training data usually includes a list of prompts created by contractors, typically ranging in number from 10,000 to 100,000.

##### ML objective and loss function

* Well-known LLMs such as ChatGPT and Llama use RL algorithms such as PPO and direct policy optimization (DPO) [26]. However, the details of these algorithms are usually beyond the scope of most ML system design interviews. For more information, refer to [27] and [28].

#### The outcome of RLHF

* The outcome of the RLHF stage is usually the final model that can be deployed as a chatbot. Table 4.4 lists some of the most popular LLMs.

* To summarize the training section, we employ a three-stage training strategy, including pretraining, SFT, and RLHF. Pretraining involves training a model on a large corpus of text to gain a broad language understanding. SFT finetunes the model to adapt its output to a (prompt, response) format. RLHF further refines the model’s responses to be helpful, safe, and aligned with human preferences.

## Sampling

* In LLMs, sampling refers to how we select tokens from the model’s predicted probability distribution to generate coherent and helpful responses.
* The following figure shows selecting the next token from predicted probabilities.

* As discussed in Chapter 2, there are various methods for generating text. Some are deterministic, while others are stochastic. In this section, we examine these methods to determine which works better for open-ended text generation.
* The following figure shows common methods for generating text.

### Deterministic methods

* Deterministic methods such as beam search work well for tasks with short, predictable text lengths. However, they are less effective for open-ended generation, such as dialogue, where output length varies. Let’s examine the common issues that arise when using deterministic methods like greedy search or beam search to generate text from LLMs.

#### Greedy search

* Greedy search selects the token with the highest probability at each step of the generation process.
* The following figure shows greedy search.

* While this method is straightforward and often produces coherent text, it has two major issues:
  + Repetition
  + Suboptimal generation
* **Repetition:** When we use greedy search to select the next tokens, the text quickly starts repeating. This is because the model sometimes gets “stuck” in loops, reusing the same sequence of tokens. This happens when the model identifies certain words following each other with high probability.
* The following figure shows repetitive output.

* **Suboptimal generation:** Greedy search ignores alternative paths during the text generation. It might miss a high-probability sequence of tokens hidden behind a low-probability token.

#### Beam search

* Beam search improves upon greedy search by considering multiple sequences simultaneously. At each step, it keeps track of the top k sequences, where k is configurable.
* The following figure shows Beam search with a beam width of 3.

* Beam search allows for more exploration and produces higher-quality text than greedy search. However, it can struggle with open-ended generation.
* Two common issues with beam search are:
  + Inefficiency
  + Repetition
* **Inefficiency:** Beam search can be computationally inefficient because it requires evaluating multiple sequences at once, which can slow down the generation process.
* **Repetition:** Beam search can lead to repetitive and generic responses. It sometimes gets stuck in a loop and repeats common phrases.
  So far, we’ve seen that deterministic methods struggle with repetition and do not work well for text generation. Let’s explore stochastic methods, which are more commonly used for text generation in LLMs.

### Stochastic methods

* Stochastic methods generate text by introducing randomness. This randomness makes them more suitable for open-ended text generation. Three popular stochastic methods are:
  + Multinomial sampling
  + Top-k sampling
  + Top-p (nucleus) sampling

#### Multinomial sampling

* Multinomial sampling selects the next token based on the probability distribution of the model’s predictions. Each token has a probability associated with it, and a token is chosen based on these probabilities.
* The following figure shows multinomial sampling.

* This approach ensures a wide variety of possible outputs. However, it introduces a significant amount of randomness, especially when the probability distribution is flat. This randomness often results in generations that are not coherent. For example, the generated text shown in Figure 4.25 is the output of the GPT-2 model using multinomial sampling.
* The following figure shows GPT-2 output using multinomial sampling.

* Due to coherence issues, multinomial sampling is rarely used in LLMs for text generation.

#### Top-k sampling

* Top-k sampling [30] is a more advanced method that selects from the k most likely tokens rather than sampling from the entire distribution
* The following figure shows Example of top-k sampling with k=3.

* Here is a step-by-step process to select the next token in top-k sampling:
* The model predicts the probability distribution for the next token, providing a probability for each token in the vocabulary.
* The tokens are sorted in descending order based on their predicted probabilities.
* The top k tokens with the highest probabilities are considered for sampling.
* The probabilities of the top k tokens are normalized to ensure they sum to 1.
* A token is sampled from this normalized distribution.
* The following figure shows GPT-2 output using top-k sampling with k=50.

* Top-k sampling balances coherence and diversity by picking from the top-k tokens. This reduces the chance of choosing irrelevant tokens while allowing some randomness. GPT-2 initially used top-k sampling, which was crucial to its success and popularity.
* A major limitation of top-k sampling is that it always picks from a fixed number of top tokens. This is problematic depending on how the predicted probabilities are spread out. Let’s understand why.
* Predicted token probabilities can be sharply or evenly distributed. With a sharp distribution, limiting choices to a fixed number of top tokens can produce nonsensical results because the model might miss the best choice. Conversely, with a fiat distribution, this fixed limit restricts the model’s creativity by not considering enough word options. For example, as shown in Figure 4.28, the model is 89% confident that the next token should be “lot,” but top-k sampling skill considers “much” and “high” as possible next tokens to sample from.
* The following figure shows Top-k sampling in sharp distribution.

* This limitation is addressed in top-p sampling, which we examine next

#### Top-p (nucleus) sampling

* Top-p sampling [31], also known as nucleus sampling, was developed in 2019. This method dynamically adjusts the number of tokens considered based on their combined probabilities. Instead of sampling only from the most likely k tokens, it chooses from the smallest possible set of tokens whose cumulative probability exceeds the probability p. This provides a more flexible and adaptive approach compared to top-k sampling.
* The following figure shows Top-p sampling adaptively chooses tokens based on the probability distribution.

* Here is a step-by-step process to select the next token in top-p sampling:
  + The model predicts the probability distribution for the next token, providing a probability for each token in the vocabulary.
  + The tokens are sorted in descending order based on their predicted probabilities.
  + Instead of selecting a fixed number of tokens, top-p sampling chooses the smallest possible set of tokens whose cumulative probability exceeds a threshold p.
  + The probabilities of the selected tokens are normalized to ensure they sum to 1.
  + A token is sampled from this normalized distribution.
* The following figure shows GPT-2 output using top-p sampling with p=0.92.

* The top-p sampling is widely used in advanced LLMs to generate human-like text. This method ensures the text is coherent and contextually relevant by focusing on the most probable tokens while allowing some randomness.
* While we covered the key aspects of different sampling methods, there are more details to each method. Two popular techniques often used in advanced sampling methods are:

  + Temperature
  + Repetition penalty

#### Temperature

* Temperature is a parameter in sampling methods that controls the randomness of predic- tions during sampling. Mathematically, the temperature parameter \(T\) scales the logits (raw scores) of the model’s output before applying the softmax function to generate probabilities. The adjusted softmax formula with temperature is given by:

  \[p\_i=\frac{\exp \left(x\_i / T\right)}{\sum\_j^n \exp \left(x\_j / T\right)}\]
  + where:
    - \(x\_i\) are the logits (raw scores) for each possible output
    - \(T\) is the temperature parameter
    - \(\rho\_i\) represents the probability of output i after applying the softmax function
* When \(T = 1\), the softmax function operates normally. When \(T > 1\), the model generates a more uniform probability distribution, making predictions more random and diverse. Higher temperatures increase randomness, which helps the model generate more creative outputs. If the model starts to stray off-topic or produce meaningless outputs, this indicates that the temperature has been set too high.
* Conversely, when \(T < 1\), the model’s output becomes more deterministic, with the highest logit values having more influence on the final prediction. Lower temperatures reduce randomness, which is more suitable for tasks requiring precise answers, such as summarization or translation. If the model starts to repeat itself, this indicates that the temperature has been set too low. A temperature of 0 consistently leads to the same output, making the sampling deterministic.
* The following figure shows Different temperature values applied to the same logits.

#### What are typical temperature values?

* Most model providers set the permissible temperature range between 0 and 2. Figure 4.32 illustrates OpenAI’s API reference for the temperature setting.
* The following figure shows OpenAI’s temperature documentation [32].

* In modern LLMs, the temperature parameter typically ranges from 0.1 to 1.5. When set beyond 1.5, outputs can become increasingly erratic and less coherent, which is undesirable. The optimal value depends on the desired behavior and is often determined empirically. The following table, created by [33], suggests possible temperature values for several use cases.
* The following figure shows the empirical temperature and top-p ranges for different tasks.

#### Repetition penalty

* Similarly, applying a repetition penalty can explicitly reduce the likelihood of generating repetitive sequences of tokens. This can be achieved by terminating the generation when repetitive n-grams are detected (as controlled by the `no_repeat_ngram_size` parameter in Hugging Face models) or by directly modifying the probabilities of tokens that have already been sampled earlier in the sequence (such as the `frequency_penalty` in the ChatGPT API).
* If you are interested in learning more about sampling methods in LLMs, refer to [30].

## Evaluation

### Offline evaluation metrics

* Evaluating LLMs like ChatGPT requires more than traditional metrics such as perplexity. These models behave in complex ways and perform differently across various tasks. Therefore, we need to assess their skills in different tasks to ensure the model is both effective and safe.
* In this section, we evaluate our LLM from the following perspectives:
  + Traditional evaluation
  + Task-specific evaluation
  + Safety evaluation
  + Human evaluation

#### Traditional evaluation

* Traditional evaluation provides an initial understanding of the LLM’s performance using typical offline metrics. A common metric is perplexity, which measures how accurately the model predicts the exact sequence of tokens in the text data. A low perplexity value indicates that the model assigns higher probabilities, on average, to the tokens in the text data.
* While these metrics are important for initial evaluation, they do not provide insights into an LLM’s capabilities or limitations. For example, a low perplexity indicates the model is good at predicting the next tokens but does not measure its ability to understand code or solve math problems.

#### Task-specific evaluation

* To effectively evaluate an LLM, we need to assess its performance across diverse tasks such as mathematics, code generation, and common-sense reasoning. This comprehensive approach helps identify the model’s strengths and weaknesses. Commonly used tasks for evaluating LLM’s capabilities are:
  + Common-sense reasoning
  + World knowledge
  + Reading comprehension
  + Mathematical reasoning
  + Code generation
  + Composite benchmarks

##### Common-sense reasoning

* Common-sense reasoning evaluates a model’s ability to make inferences based on everyday situations and general knowledge. It tests the model’s understanding of basic human experiences, logical connections, and assumptions that people naturally make. Examples include interpreting idioms, understanding cause and effect in typical scenarios, and predicting likely outcomes in social situations.
* The following figure shows a common-sense reasoning example.

* Typical benchmarks for common-sense reasoning are PIQA (Physical Interaction QA) [34], SIQA [35], HellaSwag [36], WinoGrande [37], OpenBookQA [38], and CommonsenseQA [39], each of which focuses on different aspects. For example, the CommonsenseQA benchmark is a multiple-choice question dataset for which the questions require commonsense knowledge to answer. PIQA focuses on reasoning about physical interactions in everyday situations, while HellaSwag focuses on everyday events.

##### World knowledge

* World knowledge refers to the model’s factual knowledge about the world, including historical facts, scientific information, geography, and current events. An example would be answering questions about significant historical events or scientific principles.
* The following figure shows a world knowledge example.

* Common benchmarks for this task include:
  + **TriviaQA [40]:** Questions are gathered from trivia and quiz-league websites.
  + **Natural Questions (NQ) [41]:** A dataset from Google that includes questions and answers found in natural web queries.
  + **SQuAD (Stanford Question Answering Dataset) [42]:** Contains questions based on Wikipedia articles.

##### Reading comprehension

* Reading comprehension tasks evaluate a model’s ability to understand and interpret text passages and answer questions based on them. This is critical for assessing a model’s ability to extract information from and reason in relation to given texts.
* The following figure shows a reading comprehension example from SQuAD.

* Typical benchmarks for reading comprehension are SQuAD [42], QuAC [43], and BoolQ [44].

##### Mathematical reasoning

* Mathematical reasoning tasks evaluate a model’s ability to solve mathematical problems.
* The following figure shows a mathematical reasoning example from GSM8K [45].

* Two common benchmarks for mathematical reasoning tasks are:

  + **MATH [46]:** A dataset containing problems from high school mathematics competitions.
  + **GSM8K (Grade School Math 8K) [45]:** A dataset with grade school math problems to test the model’s problem-solving skills.

##### Code generation

* Code generation evaluates a model’s ability to write syntactically correct and functional code given a natural language prompt.
* The following figure shows a code generation example from HumanEval.

* Common benchmarks for code generation are:

  + **HumanEval [47]:** Python coding tasks.
  + **MBPP (MultiPL-E Benchmarks for Programming Problems) [48]:** Multiple programming language tasks to evaluate multilingual code generation capabilities.

##### Composite benchmarks

* In addition to specific benchmarks described above, composite benchmarks combine multiple tasks for a broader assessment. Popular composite benchmarks are:

  + **MMLU (Massive Multitask Language Understanding) [49]:** Consists of multiple-choice questions from a wide range of subjects including humanities, STEM, social sciences, and more, at various difficulty levels.
  + **MMMU (Massive Multilingual Multitask Understanding) [50]:** MMMU includes a wide range of multiple-choice questions covering many subjects with varying levels of difficulty. Unlike MMLU, which focuses on English, MMMU tests the models’ ability to understand and generate accurate responses across different languages, assessing not only multilingual capabilities but also reasoning and cross-cultural knowledge.
  + **AGIEval [51]:** A comprehensive benchmark designed to test artificial general intelligence across multiple domains and tasks.
  + **Meta Llama 3 human evaluation [13]:** A high-quality human evaluation set containing 1,800 prompts that cover 12 key use cases: asking for advice, brainstorming, classification, closed question answering, coding, creative writing, extraction, inhabiting a character/persona, open question answering, reasoning, rewriting, and summarization.
* To summarize, we use various tasks and benchmarks to evaluate LLMs’ task-specific performance. This evaluation covers understanding and generating human-like responses across various domains. However, evaluation doesn’t stop there. Safety evaluation is crucial for the responsible deployment of these models. Let’s look deeper.

#### Safety evaluation

* Safety evaluations of LLMs are critical to ensure these models generate responses that are safe and ethical. These evaluations focus on various tasks that help identify and mitigate risks such as the generation of harmful content. The main aspects of safety evaluation include:

  + Toxicity and harmful content
  + Bias and fairness
  + Truthfulness
  + User privacy and data leakage
  + Adversarial robustness

##### Toxicity and harmful content

* We evaluate a model’s ability to avoid generating toxic content. Toxicity includes:

  + Hate speech
  + Abusive language
  + Content that may pose harm to individuals, groups, or society
  + Content useful for planning attacks or violence
  + Instructions for finding illegal content
* The following figure shows the model’s expected response to toxic prompts.

* Commonly used benchmarks to evaluate a model’s toxicity are:

  + **RealToxicityPrompts [52]:** Consists of about 100,000 prompts that the model must complete; then a toxicity score is automatically evaluated using PerspectiveAPI [53].
  + **ToxiGen [54]:** This benchmark tests a model’s ability to avoid generating discriminatory language.
  + **HateCheck [55]:** A suite of tests specifically for hate speech detection, covering various types of hate speech.
    Evaluating models using these benchmarks helps identify potential risks and improve the ability of models to generate safe and respectful content.

##### Bias and fairness

* We assess the model’s responses for potential biases. This includes detecting gender, racial, and other biases in generated content.
* Typical benchmarks are:

  + **CrowS-Pairs [56]:** Contains paired sentences differing in only one attribute (e.g., gender) to test for bias. This dataset enables measuring biases in 9 categories: gender, religion, race/color, sexual orientation, age, nationality, disability, physical appearance, and socioeconomic status.
  + **BBQ [57]:** A dataset of hand-written question sets that target attested social biases against different socially relevant categories.
  + **BOLD [58]:** A large-scale dataset that consists of 23,679 English text generation prompts for bias benchmarking across five domains.
    These benchmarks help us ensure the model treats all demographic groups fairly and equally.

##### Truthfulness

* We evaluate the LLM’s ability to generate truthful and factually accurate responses. This includes distinguishing between factual information and common misconceptions or falsehoods
* The following figure shows Truthfulness example from TruthfulQA.

* A common benchmark to evaluate truthfulness is TruthfulQA [59], It measures the truthfulness of a model, i.e., its ability to identify when a claim is true. This benchmark can evaluate the risks of a model generating misinformation or false claims.

##### User privacy and data leakage

* We evaluate the LLM,s tendency to leak sensitive information that it may have been exposed to during training. Since LLMs are trained on various publicly available data sources, they might know about people with a public internet presence. These assessments ensure that LLMs do not inadvertently disclose personal information. A common benchmark for this purpose is PrivacyQA [60].

##### Adversarial robustness

* Adversarial robustness tests an LLM’s ability to handle inputs intentionally designed to confuse or trick the model. This is crucial for ensuring the model’s reliability and safety in practice. Typical benchmarks for testing LLM’s adversarial robustness include AdvGLUE [61], TextFooler [62], and AdvBench [63].
* To summarize, we use various benchmarks to evaluate the safety of the LLM, which is crucial to ensure users’ safety. While both task-specific and safety evaluations are essential, human evaluation remains the most reliable method for comprehensive assessment.

#### Human evaluation

* In this approach, human evaluators are asked to rate the different aspects of an LLM such as helpfulness and safety. Human evaluation is critical for assessing nuanced aspects of helpfulness and safety that task-specific and safety benchmarks might miss.

### Online evaluation metrics

* Online evaluation metrics measure how an LLM performs when deployed in production. Commonly used metrics are:
  + User feedback and ratings
  + User engagement
  + Conversion rate
  + Online leaderboards
* User feedback and ratings: Users can rate their satisfaction with the model’s responses
* This direct feedback from users highlights areas that need improvement.
* + The following figure shows how we may collect users’ feedback.
* **User engagement:** Metrics such as “number of queries made” and “session duration” can be insightful signals to measure user engagement. High engagement levels often indicate the LLM is effective in providing helpful information.
* **Conversion rate:** Conversion rate refers to the percentage of users who make a purchase or sign up for a service after interacting with the LLM. Conversion rate is a crucial metric to monitor because higher conversion rates indicate that users find the LLM useful enough to pay for the service.
* **Online leaderboards:** Online leaderboards track the performance of various LLMs in real time, A notable example is LMSYS Chatbot Arena [64], a crowdsourced open platform designed to evaluate LLMs. These models are ranked based on more than 800,000 human pairwise comparisons.
* The following figure shows the LMArena chatbot leaderboard.

## Overall ML System Design

* Designing a chatbot system such as ChatGPT requires several components working together smoothly. Unlike traditional models, this system combines multiple services and pipelines to ensure efficiency, safety, and continuous improvement. In this section, we’ll explore two key pipelines:
  + Training pipeline
  + Inference pipeline

### Training pipeline

* The training pipeline involves three critical stages: pretraining, SFT, and RLHF. These stages collectively ensure the model is capable and that it generates helpful and safe responses

### Inference pipeline

* The inference pipeline includes several components that ensure the safety, relevance, and quality of the generated responses. This pipeline is responsible for real-time interaction with users. The key components in the inference pipeline are:
  + Safety filtering
  + Prompt enhancer
  + Response generator
  + Response safety evaluator
  + Rejection response generator
  + Session management
* The following figure shows the chatbot’s overall design.

* Let’s explore each component in more detail.

#### Safety filtering

* This component analyzes the user prompt to detect harmful, inappropriate, or unsafe queries before it is processed by the model. For example, a prompt asking for instructions on creating a harmful device will be rejected and flagged.

#### Prompt enhancer

* The prompt enhancer component refines and enriches the input prompt to make it more informative and detailed. It expands acronyms, corrects misspellings, and adds context where necessary.
* The following figure shows an example of prompt enhancement.

* This component ensures the text prompts are clear, unambiguous, and free of grammatical errors before passing it to the model, which helps the model generate better responses.

#### Response generator

* The response generator interacts with the trained LLM and utilizes top-p sampling to generate a helpful response. This component can optionally use other techniques to improve the quality and safety of the generated response. For example, it might generate multiple possible responses and then choose the one that is more appropriate based on a set of predefined criteria.

#### Response safety evaluator

* This component evaluates the generated response to detect harmful or inappropriate content before it is shown to the user. It acts as a final safeguard to ensure responses meet ethical and safety standards.

#### Rejection response generator

* This component generates a proper response when the input prompt is unsafe or the generated response is unsuitable. It provides a clear and polite explanation of why the request cannot be fulfilled.

#### Session management

* To maintain conversation context and handle follow-up questions effectively, specific handling is required. For example, when a user is chatting with a model about their favorite movies, the model needs to remember not just the current question, but also their previous mentions of different genres or films.
* This component maintains the continuity and coherence of the conversation by tracking the chat history and managing the flow of dialogue. This is achieved by feeding the chat history, along with the enhanced prompt, into the response generator. This design ensures that each response is contextually relevant by referencing previous interactions and appropriately handling the state of the conversation.

## Other Talking Points

* If there is extra time at the end of the interview, here are some additional talking points:
  + Techniques for managing dialogue states and tracking context across multiple turns[65].
  + Employing advanced or more efficient ML objectives such as multi-token prediction [66].
  + Handling very long sequence lengths [67][68].
  + Developing multimodal LLMs [69, 70].
  + Techniques such as RAG to leverage external knowledge bases and databases to enhance LLM output [71]. We explore this in Chapter 6.
  + Efficiency techniques (e.g., distillation) for faster text generation.
  + Techniques for adapting LLMs to specific domains (e.g., customer service, healthcare) without forgetting previous knowledge [72].
  + Addressing security and privacy concerns in LLMs.
  + Different optimization algorithms such as PPO, DPO, and rejection sampling [73].
  + Red-teaming LLMs to reduce harm [74].
  + Super-alignment and its importance in developing LLMs [75].
  + How in-context learning works [76].
  + Grouped query attention and its benefits [77].
  + Employing chain-of-thought prompting techniques [78]. We explore this in Chapter 6.
  + Implementing KV cache [79].
  + Enhancing trust by requiring models to produce clear and verifiable justifications for their outputs [80].

## Summary

* In this chapter, we studied the design of a generative AI chatbot system such as ChatGPT.
* We began by clarifying requirements, including text-only input and output, context handling, and safety considerations.
* We framed the chatbot as a text generation problem and selected the decoder-only Transformer architecture.
* We discussed data preparation techniques such as cleaning, filtering, anonymization, deduplication, and tokenization.
* We explored model development, focusing on positional encoding methods, especially rotary positional encoding (RoPE).
* We examined the three-stage training process:
  1. Pretraining on large text corpora.
  2. Supervised finetuning with demonstration data.
  3. Reinforcement learning from human feedback (RLHF) for alignment.
* We studied sampling methods, including greedy search, random sampling, top-k, top-p, and temperature scaling.
* We reviewed evaluation strategies, covering automatic metrics, manual reviews, and standardized benchmarks.
* We analyzed deployment, including inference services, caching, scaling, and monitoring.
* Finally, we emphasized the importance of content moderation to ensure safe and trustworthy chatbot interactions.
* Designing a chatbot like ChatGPT involves challenges across data, modeling, training, deployment, and safety. By understanding these components, we gain insight into the complexity and sophistication of building state-of-the-art generative AI systems.

## Reference Material

1. BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models, https://arxiv.org/abs/2301.12597.
2. ×Gen-MM (BLIP-3): A Family of Open Large Multimodal Models, https://www.arxiv.org/abs/2408.08872.
3. InternVL: Scaling Up Vision Foundation Models and Aligning for Generic Visual- Linguistic Tasks, https://arxiv.org/abs/2312.14238.
4. Meta’s Llama, https://llama.meta.com/.
5. Byte-Pair Encoding Tokenization. https://huggingface.co/learn/nlp-course/en/cha pter6∕5.
6. LAION-5B: An Open Large-Scale Dataset for Training Next Generation Image-Text Models, https://arxiv.org/abs/2210.08402.
7. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale, https:∕∕arxiv.org∕abs∕2010.11929.
8. Language Models are Unsupervised Multitask Learners, https://cdn.openai.com/better-language-models/language\_models\_are\_unsupervised\_multitask\_
9. learners.pdf.
10. Learning Transferable Visual Models From Natural Language Supervision. https://arxiv.org/abs/2103.00020.
11. Cross-Entropy. https://en.wikipedia.org/wiki/Cross-entropy.
12. CIDEr: Consensus-Based Image Description Evaluation, https://arxiv.org/abs/1411.5726.
13. TF-IDF Introduction, https://web.stanford.edu/class/cs276/19handouts/lecture6-tfidf-lper.pdf.
14. TF-IDF. https://en.wikipedia.org/wiki/Tf-IDF.
15. Visual Question Answering Introduction, https://huggingface.co/tasks/visual-question-answering.
16. Cross-Domain Image Captioning with Discriminative Finetuning, https://arxiv.org/abs/2304.01662.
17. Crossmodal-3600 — Multilingual Reference Captions for Geographically Diverse Images. https://research.google/blog/crossmodal-3600-1. multilingual-reference-captions-for-geographically-diverse-images∕Efficient Image Captioning for Edge Devices, https://arxiv.org/abs/2212.08985.
18. Ensemble Model Using an Image Captioning and Ranking Example, https://cloud.google.com/dataflow/docs/notebooks/runjnference\_multi\_model.
