# NLP Interview Topcs

**Source:** https://aman.ai/h/NLPInterviewTopics/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [ML fundamentals](#ml-fundamentals)
* [NLP](#nlp)
  + [1point3acre Google](#1point3acre-google)

## Overview

* Make posts out of each topic if it doesn’t exist already

## ML fundamentals

* Ensemble 7/19
* Multilayer perceptron 7/20
* SVM 7/20
* Gradient boost 7/19
* Random forest7/19]]]
* Parth doc
* skip connections 7/20
* regularization 7/20
* Sys design
* Adaboost vs Adam 7/20
* Gradient descent with momentum 7/20
* word piece 7/19
* EM vs MLE 7/19

## NLP

* GPT 7/20
* BERT 7/20
* System design : Putting it all together
* Transformers, GPT, BERT 7/20
* MLM vs Causal
* Attention 7/20
* Seq2Seq 7/20
* Word2Vec
* GRU 7/20
* Stemming, Lemmatization, Stopwords 7/20
* Metrics (BLEU, ROUGE, F1) 7/20
* Clustering (LDA, K-means) 7/20
* Naive Bayes, Support Vector Machine, Linear Regression
* TF-IDF
* HMM 7/20
* speech processing primer - https://aman.ai/primers/ai/speech-processing/ - 7/18
* loss
* activation
* GNN - loss 7/20
* LLM
* Generative AI 7/20
* Privacy
* ASR- AI summer - 7/17
* Text to speech
* Conversational AI 7/20
* Research company specific/ latest in the field
* hard sampling 7/20
* negative sampling 7/20
* logistic regression - Amazon MLU - https://mlu-explain.github.io - 7/18
* linear regression - Amazon MLU - 7/18 all of MLU
* Embeddings: bag of words, Glove, fast text, rotary, absolute, relative, BERT, word2vec, embedding space
* Token decoding - 7/19
* Token sampling - 7/19
* RNN 7/20
* LSTM 7/20
* Watermarking, hallucination, log likelihood 7/20
* Autoregressive vs Autoencoder - 7/19
* contrastive
* MAE vs MSE
* LLM primer a.ai https://aman.ai/primers/ai/LLM 7/18
* Models: Llama 2, Alpaca, what have you
* Model compression
* Transformer
* NER
* Sys design NLP
* disambiguation 7/20
* Encoder vs Decoder 7/20
* Flavors of BERT 7/20
* Finetuning 7/20
* Ondevice w/ Transformers:
  + distillBERT
  + AlBERT
  + distilGPT
  + miniGPT
* Mixed experts?

### 1point3acre Google

* Ben Laobai, NLP phd, asked how to design a suggestion in the input method of a mobile phone. I answered trier tree and then said suffix tree. I was asked about the details of suffix tree, but I didn’t know. Then I asked how to rank suggestion. In fact, the next word can be inferred from the previous words, and a language model can be trained to know the probability of inferring the next word given the previous words. Then I asked if I knew word2vec.
* heckata, old asian, google research, asked about the objective function logloss of LR, and how to derive it. Finally, I asked if there was any other loss function (I said MSE, but I can actually answer hingeloss after thinking about it later). Then I asked how to use L1 and L2 in overfitting. If feature cluster, what effect does L2 and L1 have on these features. I answered if L2 is used for the weight of each feature Penalize will be more. L1 will reduce the weight of these features to 0, (he asked if it can be reduced to 0 directly, and then introduced that it may be possible to add an operator to make the value shrink to 0). Then he asked about recommendation. Soon I was completely weak. The final answer is to only consider the pairwise ranking), I proposed to use a category of information for pre-filtering and only find items that match the category info for comparison, and then he said what to do if there is no such category information. He then said that clustering can be used, and then only compared with adjacent clusters. What to do? I said that my user feature vector was directly learned. Then I was questioned if only click data was used, and no data without click was used, would collaborative filtering learn a very strange vector (I don’t understand what he is talking about). It may be due to sparse data. The learned things may not perform well on unknown data.
* A series of coding questions, I feel that there is not enough time, and the last follow-up has no time to do it, or only a little time to do it. I feel that I spend too much time on explaining ideas and simple questions, and his family has to do multiple questions, so I don’t have enough time at the end. For this kind of beginning, I have a simple question, and then have several followups. test, two questions (1) number of islands and (2) isIsomorphic string, finding isomorphic
  groups
  . Two Chinese people, an older brother is said to be a tool to deploy ml model, and a younger brother is doing performance testing. The younger brother seems to often read his feedback, but the questions asked by the younger brother are more difficult. Finally, let me ask questions, I asked which group they belonged to, and then day to day life look like. I am not interested. I’m more interested in what part of their job they enjoy. So you can ask more about this in the future. When I answered my brother’s followup later, I didn’t come up with a better solution. Finally figured it out after my brother’s prompt. [3]
  1. For the data mining problem, start to use the maximum log likelihood to push the distribution of coins. This piece has been struggling for a long time, because I am really not very familiar with it. However, after various tips, I thought of using the XDF from binomial distribution to calculate, and then thought of using the value when the derivative and gradient are 0. Why no expectations? What is the relationship with the previous expectations, and then I asked a bunch of general ml questions. It is not very clear when I asked about the difference between GBDT, decision tree and random forecast. Especially what random forest is completely forgotten, I can’t really see their enthusiasm for their work. If I were an interviewer, I might not have the opportunity to show this. But interviews are some two way process. I should at least reflect my passionated about my work. I got the definition of recall wrong. He asked me again at that time. I thought about it carefully, but I still couldn’t think of another definition, so I affirmed my answer. The result is that the definition in the classification is tp / tp + fn. It is definitely wrong to do the opposite of the interviewer in the interview. [3]
  2. The host manager interview was very bad. I felt more like a project deep dive. He couldn’t understand why there was a business score. My example didn’t work. The example is “the french” and there was no name match result. He also asked how to collect training data, how to split ml and engineering, and said that my training sample is actually very small. A very simple question. He asked if I had dealt with more challenging problems. I said no, I think he actually wanted to ask more complicated ml questions. [The deep dive results need a better example, and the challenge of ml is not obvious enough], he asked about the division of labor and cooperation, I feel that he has been looking for the very technical and ml/dm questions I have done, and I have not been able to answer this question well. Then he said that the notification problem he has done is to push the results that the user may click, but not to push too much, otherwise the loss of the user’s disable notification is huge. In addition, how often users will click on this notification is also a factor that needs to be considered, given how to model and how to train all these constraints. This is indeed a very difficult model problem, there are too many constraints. I mentioned bayesian model and model ensemble. I said to myself that the bayesian model can be used for the combine model, but in fact, I don’t know how to do these things at all, and I have no practical experience. So I actually tmd shouldn’t mention this at all. If I don’t understand very well. better not to mention it. I feel that his interview is push and explore until he finds an area that I don’t understand at all. Finally, I asked if I used dl. I answered embedding[2]
  3. Lunch business value of the data
  4. data product. The relationship between index and match on field. I asked some tricky questions. The negative example is not representative enough. Also, if a good result does not come out on the surface, how to deal with it? There is also how to deal with the expansive feature, if the offline indexing does not include the features of these entities, how to deal with it. Finally asked if it is not a linear model. It is a non linear model, how to do pairwise ranking prediction [the answer is wrong here, even if it is not a linear model, it can be judged according to the prediction function, if a single sample has a high score, it will still rank higher]. How to deal with position bias? Only sample adjacent pairs [I found it helpful to watch the technical video][3]
  5. data coding unbiased coin generates fair coin sample. I have really struggled with this for a long time, I don’t know what to do at all, and then actively communicate with the interviewer, get hints, and then solve the problem. I provided a solution that works. But there is an easier way. The second problem is k-means, and there is no time
     Hello!
     The hidden content of this post requires points higher than 188 to view
     Your current points are 1.
     Use VIP to instantly unlock reading privileges or check out other ways to earn points
     Algorithm/Data , growth team manager: I chatted about their work at the beginning, and felt that an important direction for them was personalization. Then I asked a question about the log. First build and then print out the aggregated results. He kept asking me what data structure to use for storage. I thought of a solution that uses dictionary and find user group and then recursive. How does the method work. Finally, when I wrote the code, he understood how the method works, and affirmed that the method can work. [How to explain an algorithm based on an example, combined with existing terms, what was his question at the time, when I mentioned recusion, I used the concept of group and the concept of list. Is it easier to understand these terms by giving a specific example when explaining these terms?] Finally, what is the Data structure he expects? It should be a tree, in a tree The node has content and format information, and then these information can actually be obtained during recursion, and can be directly printed according to the preorder traversal. There is no need to keep it and then print it out.
* Sharing a face-to-face experience this week, Recruiter has notified Downlevel to L4, and I also ask the recruiting team to salvage it!
* Overall, it’s a bit confusing.
* The first round, Behavior, basically asked questions related to Inclusive.
* The second round, ML Design, asked questions about ML and NLP for half an hour. The first question at the beginning asked whether they could EM. In the middle, they asked if they knew how Word Piece was implemented. Of course, most of them were basic and common questions. In the second half of the test, there is a question of Text Classification.
* The third round, Coding. I opened the door and asked how to design a 64-bit Readable Timestamp in the DB, and how to use the extra bits. . . Then I took an Index-related Coding test. I haven’t seen it in Leetcode, but it’s probably Medium to Hard, so I can finish it.
* Fourth round, ML/NLP Knowledge/Design. In fact, it is a design problem, a labeling assignment system optimization problem for text labeling with 2,000 classes, there are some logs that have been labeled based on the keyword of each class before. At first, I was a little dizzy about what this problem is, and finally designed an Extended Keyword layer to increase Recall, and a Text Classification ba‍‍‌‍‍‍‍‌‍‍‍‍‌‌‌‌‍sed filtering layer to increase Precision. Because I was confused at the beginning, I lost control of the discussion process.
* The fifth round, Coding, this is very routine. I asked a bfs variant question. There should be similar ones on Leetcode, but I can’t remember the question number. The difficulty is Medium to hard. I finished the interview in 20 minutes and ended early.
* In short, the face-to-face interviews did not go very smoothly. I read the face-to-face scriptures and thought that it would be okay to follow a routine, but some of them are not so, just for your reference.
