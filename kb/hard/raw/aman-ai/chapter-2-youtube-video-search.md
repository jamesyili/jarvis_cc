# Chapter 2 - YouTube Video Search

**Source:** https://aman.ai/h/des/youtube-video-search/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Clarifying Requirements](#clarifying-requirements)
* [Frame the Problem as an ML Task](#frame-the-problem-as-an-ml-task)
  + [Defining the ML objective](#defining-the-ml-objective)
  + [Specifying the system’s input and output](#specifying-the-systems-input-and-output)
  + [Choosing the right ML category](#choosing-the-right-ml-category)
  + [Visual search](#visual-search)
  + [Text search](#text-search)
* [Data Preparation](#data-preparation)
  + [Data engineering](#data-engineering)
  + [Feature engineering](#feature-engineering)
    - [Preparing text data](#preparing-text-data)
    - [Text normalization](#text-normalization)
    - [Tokenization](#tokenization)
    - [Tokens to IDs](#tokens-to-ids)
      * [Lookup table](#lookup-table)
      * [Hashing](#hashing)
    - [Preparing video data](#preparing-video-data)
* [Model Development](#model-development)
  + [Model selection](#model-selection)
  + [Statistical methods](#statistical-methods)
    - [Bag of Words (BoW)](#bag-of-words-bow)
    - [Term Frequency Inverse Document Frequency (TF-IDF)](#term-frequency-inverse-document-frequency-tf-idf)
  + [ML-based methods](#ml-based-methods)
    - [Embedding (lookup) layer](#embedding-lookup-layer)
    - [Word2Vec](#word2vec)
    - [Transformer-based models](#transformer-based-models)
  + [Video encoder](#video-encoder)
    - [Video-level models](#video-level-models)
    - [Frame-level models](#frame-level-models)
  + [Model training](#model-training)
* [Evaluation](#evaluation)
  + [Offline metrics](#offline-metrics)
    - [Precision@k and mAP](#precisionk-and-map)
    - [Recall@k](#recallk)
      * [Pros](#pros)
      * [Cons](#cons)
    - [Mean Reciprocal Rank (MRR)](#mean-reciprocal-rank-mrr)
  + [Online metrics](#online-metrics)
    - [Click-Through Rate (CTR)](#click-through-rate-ctr)
    - [Video Completion Rate](#video-completion-rate)
    - [Total Watch Time of Search Results](#total-watch-time-of-search-results)
  + [Serving](#serving)
    - [Prediction pipeline](#prediction-pipeline)
      * [Visual search](#visual-search-1)
      * [Text search](#text-search-1)
      * [Fusing layer](#fusing-layer)
      * [Re-ranking service](#re-ranking-service)
    - [Video indexing pipeline](#video-indexing-pipeline)
    - [Text indexing pipeline](#text-indexing-pipeline)
* [Other Talking Points](#other-talking-points)
  + [References](#references)

## Overview

* On video-sharing platforms such as YouTube, the number of videos can quickly grow into the billions. In this chapter, we design a video search system that can efficiently handle this volume of content. As shown in Figure 4.1, the user enters text into the search box, and the system displays the most relevant videos for the given text.
* Image represents a simplified web browser window simulating a video search. The top of the window displays three colored circular icons (red, pink, blue) likely representing user accounts or settings, followed by a search bar containing the search query ‘Playing guitar at night’ and a magnifying glass icon indicating a search action. Below the search bar, the text ‘Your search results:’ precedes three square boxes arranged horizontally. Each box is a different pastel color (light pink, light green, light red) and contains a black camcorder icon, representing video search results. There are no explicit URLs or parameters visible; the diagram focuses on the user input and the visual representation of the search output, suggesting a simplified model of a video search engine’s user interface.
* The following figure shows Searching videos with a text query.

## Clarifying Requirements

* Here is a typical interaction between a candidate and an interviewer.

  + **Candidate:** Is the input query text-only, or can users search with an image or video?
  + **Interviewer:** Text queries only.
  + **Candidate:** Is the content on the platform only in video form? How about images or audio files?
  + **Interviewer:** The platform only serves videos.
  + **Candidate:** The YouTube search system is very complex. Can I assume the relevancy of a video is determined solely by its visual content and the textual data associated with the video, such as the title and description?
  + **Interviewer:** Yes, that’s a fair assumption.
  + **Candidate:** Is there any training data available?
  + **Interviewer:** Yes, let’s assume we have ten million pairs of (video, text query).
  + **Candidate:** Do we need to support other languages in the search system?
  + **Interviewer:** For simplicity, let’s assume only English is supported.
  + **Candidate:** How many videos are available on the platform?
  + **Interviewer:** One billion videos.
  + **Candidate:** Do we need to personalize the results? Should we rank the results differently for different users, based on their past interactions?
  + **Interviewer:** As opposed to recommendation systems where personalization is essential, we do not necessarily have to personalize results in search systems. To simplify the problem, let’s assume no personalization is required.
* Let’s summarize the problem statement. We are asked to design a search system for videos. The input is a text query, and the output is a list of videos that are relevant to the text query. To search for relevant videos, we leverage both the videos’ visual content and textual data. We are given a dataset of ten million (video, text query) pairs for model training.

## Frame the Problem as an ML Task

### Defining the ML objective

* Users expect search systems to provide relevant and useful results. One way to translate this into an ML objective is to rank videos based on their relevance to the text query.

### Specifying the system’s input and output

* As shown in Figure 4.2, the search system takes a text query as input and outputs a ranked list of videos sorted by their relevance to the text query.
* Image represents a simplified video search system architecture. The system begins with a text query, ‘Dogs playing indoor,’ which is input into a ‘Video search system’ component. This system processes the query and retrieves relevant video results. The output is displayed as a list of video thumbnails, represented by three color-coded rectangles (light peach, light purple, and light green) each containing a black camera icon symbolizing a video clip. The ellipsis (`...`) between the middle and bottom rectangles indicates that there may be more results than are shown. The entire output is labeled ‘Results,’ indicating the final set of videos returned by the system in response to the initial text query. The arrows show the unidirectional flow of information from the text query to the video search system and then to the displayed results.
* The following figure shows Video search system’s input-output.

### Choosing the right ML category

* In order to determine the relevance between a video and a text query, we utilize both visual content and the video’s textual data. An overview of the design can be seen in Figure 4.3.
* Image represents a video search system architecture. The system begins with a text query, ‘Dogs playing indoor,’ which is fed into two parallel processing paths: a ‘Text search’ and a ‘Visual search.’ Each path processes the query independently. The ‘Text search’ path outputs a set of video results represented by pink rectangles, each containing a camera icon, indicating videos identified based on textual analysis. Similarly, the ‘Visual search’ path outputs another set of video results, represented by pale yellow rectangles with camera icons, signifying videos identified based on visual content analysis. Both sets of results are then fed into a ‘Fusing’ module, which combines the results from the text and visual searches. The fused results, a combined set of videos from both paths, are then output as the final ‘Results,’ shown as a mix of pink and yellow rectangles with camera icons, suggesting a ranked list of videos based on the combined scores from both search methods. The entire video search system is enclosed within a dashed-line box.
* The following figure shows High-level overview of the search system.

* Let’s briefly discuss each component.

### Visual search

* This component takes a text query as input and outputs a list of videos. The videos are ranked based on the similarity between the text query and the videos’ visual content.
* Representation learning is a commonly used approach to search for videos by processing their visual content. In this approach, text query and video are encoded separately using two encoders. As shown in Figure 4.4, the ML model contains a video encoder that generates an embedding vector from the video, and a text encoder that generates an embedding vector from the text. The similarity score between the video and the text is calculated using the dot product of their representations.
* Image represents a machine learning model for video retrieval based on text queries. The system consists of two main input branches: a video branch and a text branch. The video branch takes a video as input (represented by a video camera icon), which is processed by a ‘Video encoder’ to generate a ‘Video embedding’ – a numerical vector represented by a column of four values (0.1, 0.8, -1, -0.7). Similarly, the text branch takes a text query (‘Dogs playing indoor’) as input, which is processed by a ‘Text encoder’ to generate a ‘Text embedding’ – another numerical vector with four values (0.2, 0.6, -0.9, -0.4). Both video and text embeddings are fed into an ‘ML model’ (enclosed by a dashed line), which presumably compares these embeddings to determine the relevance of the video to the text query. Arrows indicate the flow of data from input to processing units and finally to the embeddings.
* The following figure shows ML model’s input-output.
* In order to rank videos that are visually and semantically similar to the text query, we compute the dot product between the text and each video in the embedding space, then rank the videos based on their similarity scores.

### Text search

* Figure 4.5 shows how text search works when a user types in a text query: “dogs playing indoor”. Videos with the most similar titles, descriptions, or tags to the text query are shown as the output.
* Image represents a simplified video search system. The process begins with a text query, ‘Dogs playing indoor,’ which is input into a ‘Text search’ component. This component accesses a database represented as a cylinder labeled ‘Video’s textual data,’ containing textual information about videos. The search uses this data to identify relevant videos. The results are displayed as a table with three columns: ‘Video ID,’ ‘Title,’ and ‘Tags.’ The ‘Video ID’ column lists the IDs of the matched videos (1 and 6 in this example). The ‘Title’ column provides the video titles, and the ‘Tags’ column lists keywords associated with each video. The dashed line indicates a connection between the textual data and the table, suggesting that the search results are derived from the database. The entire system demonstrates a text-based video search functionality, retrieving videos based on keyword matching in their titles and associated tags.
* The following figure shows Text search.
* The inverted index is a common technique for creating the text-based search component, allowing efficient full-text search in databases. Since inverted indexes aren’t based on machine learning, there is no training cost. A popular search engine companies often use is Elasticsearch, which is a scalable search engine and document store. For more details and a deeper understanding of Elasticsearch, refer to [1].

## Data Preparation

### Data engineering

* Since we are given an annotated dataset to train and evaluate the model, it’s not necessary to perform any data engineering. Table 4.1 shows what the annotated dataset might look like.
* The following table shows the annotated dataset.

| **Video name** | **Query** | **Split type** |
| --- | --- | --- |
| 76134.mp4 | Kids swimming in a pool! | Training |
| 92167.mp4 | Celebrating graduation | Training |
| 2867.mp4 | A group of teenagers playing soccer | Validation |
| 28543.mp4 | How Tensorboard works | Validation |
| 70310.mp4 | Road trip in winter | Test |

### Feature engineering

* Almost all ML algorithms accept only numeric input values. Unstructured data such as texts and videos need to be converted into a numerical representation during this step. Let’s take a look at how to prepare the text and video data for the model.

#### Preparing text data

* As shown in Figure 4.6, text is typically represented as a numerical vector using three steps: text normalization, tokenization, and tokens to IDs [2].
* Image represents a flowchart illustrating the text preprocessing steps involved in converting a natural language sentence into numerical representations suitable for machine learning models. The process begins with the input sentence, “A person is walking in Montréal !”. This sentence is then fed into a ‘Text normalization’ block, which outputs a normalized version: ‘a person walk in montreal”. This normalized text is subsequently passed to a ‘Tokenization’ block, which splits the sentence into individual tokens: [“a”, “person”, “walk”, “in”, “montreal”]. Finally, these tokens are processed by a ‘Tokens to IDs’ block, which converts each token into a unique numerical ID, resulting in the output: [33,28,4,16,99]. The entire process is depicted as a sequential flow, with arrows indicating the direction of data movement between each processing stage.
* The following figure shows Represent a text with a numerical vector.
* Let’s take a look at each step in more detail.

#### Text normalization

* Text normalization - also known as text cleanup - ensures words and sentences are consistent. For example, the same word may be spelled slightly differently; as in “dog”, “dogs”, and “DOG!” all refer to the same thing but are spelled in different ways. The same is true for sentences. Take these two sentences, for example:

  + “A person walking with his dog in Montréal !”
  + “a person walks with his dog, in Montreal.”
* Both sentences mean the same, but have differing punctuation and verb forms. Here are some typical methods for text normalization:

  + **Lowercasing:** make all letters lowercase, as this does not change the meaning of words or sentences
  + **Punctuation removal:** remove punctuation from the text. Common punctuation marks are the period, comma, question mark, exclamation point, etc.
  + **Trim whitespaces:** trim leading, trailing, and multiple whitespaces
  + **Normalization Form KD (NFKD) [3]:** decompose combined graphemes into a combination of simple ones
  + **Strip accents:** remove accent marks from words. For example: Màlaga → Malaga, Noël → Noel
  + **Lemmatization and stemming:** identify a canonical representative for a set of related word forms. For example: walking, walks, walked → walk

#### Tokenization

* Tokenization is the process of breaking down a piece of text into smaller units called tokens. Generally, there are three types of tokenization:

  + **Word tokenization:** split the text into individual words based on specific delimiters. For example, a phrase like “I have an interview tomorrow” becomes [“I”, “have”, “an”, “interview”, “tomorrow”]
  + **Subword tokenization:** split text into subwords (or n-gram characters)
  + **Character tokenization:** split text into a set of characters
* The details of different tokenization algorithms are not usually a strong focus in ML system design interviews. If you are interested to learn more, refer to [4].

#### Tokens to IDs

* Once we have the tokens, we need to convert them to numerical values (IDs). The representation of tokens with numerical values can be done in two ways:

  + Lookup table
  + Hashing

##### Lookup table

* In this method, each unique token is mapped to an ID. Next, a lookup table is created to store these 1:1 mappings. Figure 4.7 shows what the mapping table might look like.
* Image represents a simple table with two columns: ‘Word’ and ‘ID’. The ‘Word’ column lists a sample of words (animals, art, car, insurance, travel), with ellipses (…) indicating that this is a partial list of many more words. The ‘ID’ column provides a unique numerical identifier corresponding to each word in the ‘Word’ column. The table structure implies a one-to-one mapping between each word and its assigned ID, suggesting a vocabulary or lookup table where words are represented by their respective numerical IDs. No information flows between the columns; the table simply presents a static mapping of words to IDs.
* The following figure shows A lookup table.

##### Hashing

* Hashing, also called “feature hashing” or “hashing trick,” is a memory-efficient method that uses a hash function to obtain IDs, without keeping a lookup table. Figure 4.8 shows how a hash function is used to convert words to IDs.
* The following figure shows Use hashing to obtain word IDs.
* Let’s compare the lookup table with the hashing method.
* The following table shows Lookup table vs. feature hashing.

| **Feature** | **Lookup Table** | **Hashing** |
| --- | --- | --- |
| Speed | ✓ Quick to convert tokens to IDs | ✘ Need to compute hash function to convert tokens to IDs |
| ID to Token | ✓ Easy to convert IDs to tokens using a reverse index table | ✘ Not possible to convert IDs to tokens |
| Memory | ✘ The table is stored in memory. A large number of tokens will result in an increase in memory required | ✓ The hash function is sufficient to convert any token to its ID |
| Unseen Tokens | ✘ New or unseen words cannot be properly handled | ✓ Easily handles new or unseen words by applying the hash function to any word |
| Collisions [5] | ✓ No collision issue | ✘ Collisions are a potential problem |

#### Preparing video data

* Figure 4.9 shows a typical workflow for preprocessing a raw video.
* Image represents a data preprocessing pipeline for a video of a corgi running. The process begins with a video file (represented by a YouTube play button overlayed on a video still), which is fed into a ‘Decode frames’ block. This block outputs a sequence of individual frames from the video. These frames then follow two parallel paths. The upper path involves directly ‘Sampling frames’ from the decoded sequence, resulting in a subset of frames. The lower path first involves ‘Resizing’ the frames to a smaller size. These resized frames are then processed by a ‘Scaling, normalizing, and correcting color mode’ block, which performs image enhancement and standardization. Finally, the output from both paths is combined and saved as a NumPy array file named ‘frames.npy’. Arrows indicate the flow of data between each processing step.
* The following figure shows the video preprocessing workflow.

## Model Development

### Model selection

* As discussed in the “Framing the problem as an ML task” section, text queries are converted into embeddings by a text encoder, and videos are converted into embeddings by a video encoder. In this section, we examine possible model architectures for each encoder.
* The following figure shows thae text encoder’s input-output.
* The text encoder converts text into a vector representation [6]. For example, if two sentences have similar meanings, their embeddings are more similar. To build the text encoder, two broad categories are available: statistical methods and ML-based methods. Let’s examine each.

### Statistical methods

* Those methods rely on statistics to convert a sentence into a feature vector. Two popular statistical methods are:

  + Bag of Words (BoW)
  + Term Frequency Inverse Document Frequency (TF-IDF)

#### Bag of Words (BoW)

* This method converts a sentence into a fixed-length vector. It models sentence-word occurrences by creating a matrix with rows representing sentences, and columns representing word indices. An example of BoW is shown in Figure 4.11.
* The following table shows BoW representations of different sentences.

| **Text** | **best** | **holiday** | **is** | **nice** | **person** | **this** | **today** | **trip** | **very** | **with** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| this person is nice very nice | 0 | 0 | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 0 |
| today is holiday | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| this trip with best person is best | 2 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |

* BoW is a simple method that computes sentence representations fast, but has the following limitations:

  + It does not consider the order of words in a sentence. For example, “let’s watch TV after work” and “let’s work after watch TV” would have the same BoW representation.
  + The obtained representation does not capture the semantic and contextual meaning of the sentence. For example, two sentences with the same meaning but different words have a totally different representation.
  + The representation vector is sparse. The size of the representation vector is equal to the total number of unique tokens we have. This number is usually very large, so each sentence representation is mostly filled with zeros.

#### Term Frequency Inverse Document Frequency (TF-IDF)

* This is a numerical statistic intended to reflect how important a word is to a document in a collection or corpus. TF-IDF creates the same sentence-word matrix as in BoW, but it normalizes the matrix based on the frequency of words. To learn more about the mathematics behind this, refer to [7].
* Since TF-IDF gives less weight to frequent words, its representations are usually better than BoW. However, it has the following limitations:

  + A normalization step is needed to recompute term frequencies when a new sentence is added.
  + It does not consider the order of words in a sentence.
  + The obtained representation does not capture the semantic meaning of the sentence.
  + The representations are sparse.
* In summary, statistical methods are usually fast. However, they do not capture the contextual meaning of sentences, and the representations are sparse. ML-based methods address those issues.

### ML-based methods

* In these methods, an ML model converts sentences into meaningful word embeddings so that the distance between two embeddings reflects the semantic similarity of the corresponding words. For example, if two words, such as “rich” and “wealth,” are semantically similar, their embeddings are close in the embedding space. Figure 4.12 shows a simple visualization of word embeddings in the two-dimensional embedding space. As you can see, similar words are grouped together.
* The following figure shows words in the 2D embedding space.
* There are three common ML-based approaches for transforming texts into embeddings:

  + Embedding (lookup) layer
  + Word2Vec
  + Transformer-based architectures

#### Embedding (lookup) layer

* In this approach, an embedding layer is employed to map each ID to an embedding vector. Figure 4.13 shows an example.
* The following figure shows the embedding lookup method.
* Employing an embedding layer is a simple and effective solution to convert sparse features, such as IDs, into a fixed-size embedding. We will see more examples of its usage in later chapters.

#### Word2Vec

* Word2Vec [8] is a family of related models used to produce word embeddings. These models use a shallow neural network architecture and utilize the co-occurrences of words in a local context to learn word embeddings. In particular, the model learns to predict a center word from its surrounding words during the training phase. After the training phase, the model is capable of converting words into meaningful embeddings.
* There are two main models based on Word2Vec: Continuous Bag of Words (CBOW) [9] and Skip-gram [10]. Figure 4.14 shows how CBOW works at a high level. If you are interested to learn about these models, refer to [8].
* The following figure shows the CBOW approach.
* Even though Word2Vec and embedding layers are simple and effective, recent architectures based upon Transformers have shown promising results.

#### Transformer-based models

* These models consider the context of the words in a sentence when converting them into embeddings. As opposed to Word2Vec models, they produce different embeddings for the same word depending on the context.
* The following figure shows a Transformer-based model which takes a sentence—a set of words—as input and produces an embedding for each word.
* Transformers are very powerful at understanding the context and producing meaningful embeddings. Several models, such as BERT [11], GPT-3 [12], and BLOOM [13], have demonstrated Transformers’ potential to perform a wide variety of Natural Language Processing (NLP) tasks. In our case, we choose a Transformer-based architecture such as BERT as our text encoder.
* In some interviews, the interviewer may want you to dive deeper into the details of the Transformer-based model. To learn more, refer to [14].

### Video encoder

* We have two architectural options for encoding videos:

  + Video-level models
  + Frame-level models

#### Video-level models

* Video-level models process a whole video to create an embedding, as shown in Figure 4.16. The model architecture is usually based on 3D convolutions [15] or Transformers. Since the model processes the whole video, it is computationally expensive.
* The following figure shows a video-level model.

#### Frame-level models

* Frame-level models work differently. It is possible to extract the embedding from a video using a frame-level model by breaking it down into three steps:

  1. Preprocess a video and sample frames
  2. Run the model on the sampled frames to create frame embeddings
  3. Aggregate (e.g., average) frame embeddings to generate the video embedding
* The following figure shows a frame-level model.
* Since this model works at the frame level, it is often faster and computationally less expensive. However, frame-level models are usually not able to understand the temporal aspects of the video, such as actions and motions. In practice, frame-level models are preferred in many cases where a temporal understanding of the video is not crucial. Here, we employ a frame-level model such as ViT [16] for two reasons:

  1. Improve the training and serving speed
  2. Reduce the number of computations

### Model training

* To train the text encoder and video encoder, we use a contrastive learning approach. If you are interested in learning more about this, see the “Model training” section in Chapter 2, Visual Search System.
* An explanation of how to compute the loss during model training is shown in Figure 4.18.
* The following figure shows the loss computation.

## Evaluation

### Offline metrics

* Here are some offline metrics that are typically used in search systems. Let’s examine which are the most relevant.

#### Precision@k and mAP

* Precision@k measures how many of the top *k* results are relevant. It is defined as:

\[\text{Precision@k} = \frac{\text{Number of relevant items among the top } k \text{ items in the ranked list}}{k}\]

* In the evaluation dataset, each text query is associated with only one video. This means the numerator in the Precision@k formula is at most 1. As a result, Precision@k values tend to be low. For example, even if the system ranks the correct video at the top of the list, the Precision@10 is only 0.1.
* Due to this limitation, precision-based metrics such as Precision@k and Mean Average Precision (mAP) are not very informative for this specific setup.

#### Recall@k

* Recall@k measures the ratio between the number of relevant videos in the search results and the total number of relevant videos. It is defined as:

\[\text{Recall@k} = \frac{\text{Number of relevant videos among the top } k \text{ videos}}{\text{Total number of relevant videos}}\]

* Since the total number of relevant videos is always 1, the formula simplifies to:

\[\text{Recall@k} =
\begin{cases}
1, & \text{if the relevant video is among the top } k \text{ videos,}
0, & \text{otherwise.}
\end{cases}\]

##### Pros

* It effectively measures the model’s ability to find the associated video for a given text query.

##### Cons

* It depends on the choice of *k*. Selecting the right *k* value can be challenging.
* When the relevant video is not within the top *k* results, Recall@k = 0, regardless of how close it was.
* For instance, suppose Model A ranks the correct video at position 15, and Model B ranks it at position 50. If we use Recall@10, both models would have Recall@10 = 0, even though Model A performed better.

#### Mean Reciprocal Rank (MRR)

* Mean Reciprocal Rank (MRR) is a more robust metric that evaluates how highly the correct result is ranked. It measures the average reciprocal of the rank of the first relevant item across all queries. The formula is:

  \[\text{MRR} = \frac{1}{m} \sum\_{i=1}^{m} \frac{1}{\text{rank}\_i}\]
  + where *m* is the total number of queries, and *rank\_i* is the position of the first relevant video for the *i*-th query.
* This metric addresses the shortcomings of Recall@k because it rewards systems that rank the relevant video higher in the list. It is therefore an appropriate choice for offline evaluation of video search systems.

### Online metrics

* In addition to offline evaluation, real-world video search systems are also assessed using **online metrics**, which are based on real user interactions. These metrics help capture user engagement and satisfaction more effectively than offline evaluations alone. Below are some commonly used online metrics.

#### Click-Through Rate (CTR)

* Click-Through Rate measures how often users click on the retrieved videos. It is calculated as:

\[\text{CTR} = \frac{\text{Number of clicks on search results}}{\text{Number of times results are shown}}\]

* CTR is a good measure of engagement, showing how appealing the results are to users. However, it does **not** indicate whether the clicked videos were relevant or satisfying. A high CTR may simply mean the thumbnails or titles were attractive, even if the content did not match the query intent.

#### Video Completion Rate

* Video Completion Rate measures how many of the videos appearing in search results are watched until the end. It is defined as:

\[\text{Completion Rate} = \frac{\text{Number of videos watched until completion}}{\text{Number of videos clicked}}\]

* Although this metric indicates engagement, it has an important limitation: users may find a video relevant but not watch it to the end. Therefore, completion rate alone does not fully capture search result quality.

#### Total Watch Time of Search Results

* Total Watch Time measures the total time users spend watching the videos returned by the search system. It can be expressed as:

  \[\text{Total Watch Time} = \sum\_{i=1}^{n} t\_i\]
  + where \(t\_i\) is the watch duration for video *i* among the *n* videos displayed in search results.
* This metric is generally a strong indicator of relevance — users tend to spend more time watching videos that match their search intent. Therefore, Total Watch Time is often a key performance measure for evaluating search quality in production systems.

### Serving

* At serving time, the system displays a ranked list of videos relevant to a given text query. Figure 4.19 shows a simplified machine learning (ML) system design.
* The following figure shows the ML system design.

#### Prediction pipeline

* This pipeline consists of the following components:

  + Visual search
  + Text search
  + Fusing layer
  + Re-ranking service

##### Visual search

* This component encodes the text query and uses a nearest neighbor (NN) service to find the most similar video embeddings to the query embedding. To accelerate the NN search, approximate nearest neighbor (ANN) algorithms are used, as described in Chapter 2, *Visual Search System*.
* The following figure shows retrieving the top 3 results for a given text query.

##### Text search

* Using Elasticsearch, this component finds videos whose titles or tags overlap with the text query. This allows the system to retrieve textually relevant videos based on metadata and keywords.

##### Fusing layer

* This component takes two different lists of relevant videos — one from the visual search and one from the text search — and combines them into a new ranked list.
* The fusing layer can be implemented in two ways:

  1. **Weighted sum re-ranking:** Re-rank videos based on a weighted sum of their predicted relevance scores.
  2. **Model-based re-ranking:** Use a separate machine learning model to re-rank videos based on learned preferences.
* While the second approach may yield higher precision, it is computationally more expensive and slower at serving time. Therefore, the weighted-sum approach is typically preferred for efficiency.

##### Re-ranking service

* This service adjusts the ranked list of videos according to business-level logic and policies. For instance, it may prioritize verified creators, boost recent uploads, or demote potentially duplicate or low-quality videos.

#### Video indexing pipeline

* A trained video encoder is used to compute embeddings for each video. These embeddings are stored and indexed in the video index table, enabling efficient retrieval by the nearest neighbor service during search.

#### Text indexing pipeline

* This pipeline uses Elasticsearch to index video metadata, including titles, manually provided tags, and automatically generated tags.
* In many cases, when users upload videos, they may omit tags. To address this, an **auto-tagger** component can automatically generate descriptive tags for such videos. While these auto-generated tags may be noisier than manual ones, they still provide valuable information for text-based retrieval.

## Other Talking Points

* Before concluding this chapter, it’s important to note we have simplified the system design of the video search system. In practice, it is much more complex. Some improvements may include:
* Use a multi-stage design (candidate generation + ranking).
* Use more video features such as video length, video popularity, etc.
* Instead of relying on annotated data, use interactions (e.g., clicks, likes, etc.) to construct and label data. This allows us to continuously train the model.
* Use an ML model to find titles and tags which are semantically similar to the text query. This model can be combined with Elasticsearch to improve search quality.
* If there’s time left at the end of the interview, here are some additional talking points:
* An important topic in search systems is query understanding, such as spelling correction, query category identification, and entity recognition. How to build a query-understanding component? [17].
* How to build a multi-modal system that processes speech and audio to improve search results [18].
* How to extend this work to support other languages [19].
* Near-duplicate videos in the final output may negatively impact user experience. How to detect near-duplicate videos so we can remove them before displaying the results [20]?
* Text queries can be divided into head, torso, and tail queries. What are the different approaches commonly used in each case [21]?
* How to consider popularity and freshness when producing the output list [22]?
* How real-world search systems work [23][24][25].

#### References

[1] Elasticsearch. <https://www.tutorialspoint.com/elasticsearch/elasticsearch_query_dsl.htm>
[2] Preprocessing text data. <https://huggingface.co/docs/transformers/v4.42.0/preprocessing>
[3] NFKD normalization. <https://unicode.org/reports/tr15/>
[4] What is Tokenization summary. <https://huggingface.co/docs/transformers/tokenizer_summary>
[5] Hash collision. <https://en.wikipedia.org/wiki/Hash_collision>
[6] Deep learning for NLP. <http://cs224d.stanford.edu/lecture_notes/notes1.pdf>
[7] TF-IDF. <https://en.wikipedia.org/wiki/Tf%E2%80%93idf>
[8] Word2Vec models. <https://www.tensorflow.org/tutorials/text/word2vec>
[9] Continuous bag of words. <https://www.kdnuggets.com/2018/04/implementing-deep-learning-methods-feature-engineering-text-data-cbow.html>
[10] Skip-gram model. <http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/>
[11] BERT model. <https://arxiv.org/pdf/1810.04805.pdf>
[12] GPT-3 model. <https://arxiv.org/pdf/2005.14165.pdf>
[13] BLOOM model. <https://bigscience.huggingface.co/blog/bloom>
[14] Transformer implementation from scratch. <https://peterbloem.nl/blog/transformers>
[15] 3D convolutions. <https://www.kaggle.com/code/shivamb/3d-convolutions-understanding-use-case/notebook>
[16] Vision Transformer. <https://arxiv.org/pdf/2010.11929.pdf>
[17] Query understanding for search engines. <https://www.linkedin.com/pulse/ai-query-understanding-daniel-tunkelang/>
[18] Multimodal video representation learning. <https://arxiv.org/pdf/2012.04124.pdf>
[19] Multilingual language models. <https://arxiv.org/pdf/2107.00676.pdf>
[20] Near-duplicate video detection. <https://arxiv.org/pdf/2005.07356.pdf>
[21] Generalizable search relevance. <https://livebook.manning.com/book/ai-powered-search/chapter-10/v-10/20>
[22] Freshness in search and recommendation systems. <https://developers.google.com/machine-learning/recommendation/dnn/re-ranking>
[23] Semantic product search by Amazon. <https://arxiv.org/pdf/1907.00937.pdf>
[24] Ranking relevance in Yahoo search. <https://www.kdd.org/kdd2016/papers/files/adf0361-yinA.pdf>
[25] Semantic product search in E-Commerce. <https://arxiv.org/pdf/2008.08180.pdf>
