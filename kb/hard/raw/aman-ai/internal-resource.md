# Internal Resource

**Source:** https://aman.ai/hidden/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [ML Algorithms](#ml-algorithms)
  + [Catch all links](#catch-all-links)
* [ChatGPT vs GPT3](#chatgpt-vs-gpt3)
* [Generating music with text or images](#generating-music-with-text-or-images)
* [Stable Diffusion](#stable-diffusion)
  + [How to generate animation with Stable Diffusion](#how-to-generate-animation-with-stable-diffusion)
  + [🚀 Stable diffusion stands out among diffusion models, Here is Why.](#-stable-diffusion-stands-out-among-diffusion-models-here-is-why)
* [ML Youtube channels](#ml-youtube-channels)
* [DALLE-2](#dalle-2)
* [Forward-Forward Algorithm](#forward-forward-algorithm)
* [ChatGPT](#chatgpt)
* [ML for Ads Ranking RecSys](#ml-for-ads-ranking-recsys)
* [Is PageRank still used at Google](#is-pagerank-still-used-at-google)
* [CLIP](#clip)
* [Quick Feature Selection Method](#quick-feature-selection-method)
* [Overfitting](#overfitting)
* [Pruning](#pruning)
* [Information Retrieval Metrics](#information-retrieval-metrics)
* [XGBoost](#xgboost)
* [Data Parallelization by Sebastian Raschka](#data-parallelization-by-sebastian-raschka)
* [Top 5 basic checks when trianing deep learning models](#top-5-basic-checks-when-trianing-deep-learning-models)
* [A list of 5 techniques to optimize deep neural network model performance during inference](#a-list-of-5-techniques-to-optimize-deep-neural-network-model-performance-during-inference)
* [Links for MLOPS](#links-for-mlops)
* [Architecture](#architecture)
* [Recommender Engine](#recommender-engine)
* [How to detect Data Drift](#how-to-detect-data-drift)
* [How to decompose Bias and Variance from the Data](#how-to-decompose-bias-and-variance-from-the-data)
* [Feature Selection Method](#feature-selection-method)
* [Self Instruct aligning language models with self generated instructions](#self-instruct-aligning-language-models-with-self-generated-instructions)

## Overview

* The content below is a work in progress and is a collection of content from [Damien Benveniste’s linkedIn posts that can be found here](https://www.linkedin.com/in/damienbenveniste/recent-activity/shares/) and [Prithivi Da](https://www.linkedin.com/search/results/content/?fromMember=%5B%22ACoAAANONyEBI75vYtjMK4f9hcDMhgneli34DsA%22%5D&heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAAANONyEBI75vYtjMK4f9hcDMhgneli34DsA&keywords=prithivi%20da&origin=FACETED_SEARCH&position=1&searchId=db1fd6da-b7b0-4e5c-ae97-bb8b90a36918&sid=aGE&sortBy=%22date_posted%22).
* Content is also from [Sebastian Raschka](https://www.linkedin.com/feed/update/urn:li:activity:7019488884581384192/)

## ML Algorithms

### Catch all links

“Machine Learning it JUST statistics!”. Sure! But before you go, can you answer the following questions?

* Why finding a set of weights for a Neural Network so that the network produces the correct output for all the training examples is a NP-hard problem? http://authors.library.caltech.edu/26705/1/88-20.pdf
* Why the Feature Selection problem is a NP-complete problem? https://www.aaai.org/…/Fall/1994/FS-94-02/FS94-02-011.pdf
* Why the Hyperparameter Optimization problem is NP-complete? https://www.cwu.edu/…/Hyperparameter%20Optimization…
* How would you implement Logistic Regression in a distributed manner? http://proceedings.mlr.press/v28/gopal13.pdf, https://link.springer.com/…/10.1007/978-981-15-1899-7\_20
* What are the pros and cons of an Iterative Re-weighted Least Square implementation over a Gradient Descent implementation for a Logistic regression?
  https://nlp.chonbuk.ac.kr/BML/slides\_freda/lec7.pdf
* How do you efficiently design a parallelized implementation of a Gradient Boosting Algorithm? https://www.kdd.org/kdd…/papers/files/rfp0697-chenAemb.pdf
* What are the trade-offs to build the trees in breadth-first-search (BFS) manner vs a depth-search-first (DFS) manner for a Random Forest algorithm?
  https://arxiv.org/abs/1910.06853
* How to modify the breadth-first-search algorithm to build efficient KD-trees for K-nearest neighbors?
  https://en.wikipedia.org/wiki/Best-first\_search
  https://citeseerx.ist.psu.edu/viewdoc/download…
* Why the algorithms to parallelize on GPUs are slightly different from the ones to parallelize on CPUs? https://www.researchgate.net/…/4202315\_Artificial…
* What is the effect of precision (e.g. float16 vs float32) in training Neural Networks? https://arxiv.org/abs/1502.02551, https://arxiv.org/abs/1412.7024, https://arxiv.org/abs/1602.02830
* How do you implement Logistic Regression on a quantum computing unit? https://arxiv.org/abs/1906.03834
* What is the best way to deploy a ML model on Kubernetes so you minimize latency while keeping modularity and maintainability high?
  https://www.analyticsvidhya.com/…/deploying-ml-models…/
  https://opensource.com/…/9/deep-learning-model-kubernetes
* Why can Logistic Regression can perfectly learn the outcomes of a AND and OR logical gate but not from a XOR logical gate?
  https://web.stanford.edu/…/23-LogisticRegression.pdf
  https://courses.engr.illinois.edu/…/Slides/Lecture20.pdf
* What are the pros and cons of using Dynamic programming VS Monte Carlo methods to optimize the Bell equations?
  https://www.cs.hhu.de/…/Dialog…/Lectures\_RL/L2.pdf
  https://richard-warren.github.io/blog/rl\_intro\_1/
* Why the Temporal-difference Learning method leads to more stable convergence of the Reinforcement learning algorithms?
  https://web.stanford.edu/…/pdphandbook/handbookch10.html
  Now that you answered those questions (or tried to!), can we take a minute now to appreciate the absurdity of the initial claim in this post? Thank you!
  —-
  Subscribe to my Newsletter to learn something new every week: https://TheAiEdge.io/
  #machinelearning #datascience #statistics

## ChatGPT vs GPT3

* What is it about ChatGPT we get so impressed by? GPT-3’s output is no less impressive but why does ChatGPT’s outputs feel “better”?
* The main difference between ChatGPT and GPT-3 is the tasks they are trying to solve.
* GPT-3 is mostly trying to predict the next token based on the previous tokens, including the ones from the user’s prompt, where ChatGPT tries to “follow the user’s instruction helpfully and safely”.
* ChatGPT is trying to align to the user’s intention (https://lnkd.in/g\_PA\_8Xc). That is the reason InstructGPT (ChatGPT’s sibling model) with 1.3B parameters gives responses that “feel” better than GPT-33 with 175B parameters.
* ChatGPT is simply a GPT-3 model fine-tuned to human generated data with a reward mechanism to penalize responses that feel wrong to human labelers.
* They are a few advantages that emerged from that alignment training process:
  + ChatGPT provides answers that are preferred over the ones generated by GPT-3
  + ChatGPT generates right and informative answers twice as often as GPT-3
  + ChatGPT leads to a language generation that is less toxic than GPT-3. However ChatGPT is still as biased!
  + ChatGPT adapts better to different learning tasks, generalize better to unseen data, or to instructions very different from the ones found in the training data. For example, ChatGPT can answer in different languages or efficiently code, even then most of the training data is using natural English language.
* For decades, language models were trained trying to predict sequence of words, where the key seemed to be in training to align to user’s intent. It seems conceptually obvious, but it is the first time that an alignment process is successfully applied to a language model of this scale.
* All the results presented in this post come from the InstructGPT article (https://lnkd.in/gnt9K9pu), and it is a safe assumption that those results carry to ChatGPT as well.

## Generating music with text or images

* Imagine if you could tell a ML model “play a funk bassline with a jazzy saxophone” and it would synthesize artificial music! Well actually, you don’t need to imagine, you can just use it!
* Introducing RIFFUSION, a Stable Diffusion model trained on Spectrogram image data: https://lnkd.in/ge9\_VE6t. The idea is simplistic:
* just pick a pre-trained Stable Diffusion model (https://lnkd.in/dpFheWYS)
* Take lot of musics with their text descriptions and convert that into Spectrogram image data
* Fine-tune to the Stable Diffusion model

=> you now have a model that can predict new spectrograms based on other spectrograms or text prompts. Just convert those spectrograms back to musics.

If you want more details on how to do it yourself you can follow the process here: https://lnkd.in/gpj\_K-UF. I discovered this website yesterday through Alpha Signal’s weekly summary: https://alphasignal.ai/. If you to learn more about stable diffusion, you can read my LinkedIn post on it: https://lnkd.in/gxBiU9fB

## Stable Diffusion

* What is STABLE DIFFUSION? It is similar to DALL-E 2 as it is a diffusion model that can be used to generate images from text prompt.
* As opposed to DALL-E 2 though, it is open source with a PyTorch implementation (https://lnkd.in/dPpjtr-d) and a pre-trained version on HuggingFace (https://lnkd.in/dpFheWYS).
* It is trained using the LAION-5B dataset (https://lnkd.in/gewm6VEV). Stable diffusion in composed of the following sub-models:
* We have an autoencoder (https://lnkd.in/dyzQgDXH) trained by combination of a perceptual loss (https://lnkd.in/dPqz68Tp) and a patch-based adversarial objective (https://lnkd.in/dJMX3ugX).
* With it, we can encode an image to a latent representation and decode it from it.
* A random noise is progressively applied to the embedding (https://lnkd.in/dq2ZUKmj). A latent representation of a text prompt is learned from a CLIP alignment to the image representation (https://lnkd.in/eGNMirji).
* We then use U-Net, a convolutional network with ResNet blocks to learn to denoise the diffused embedding (https://lnkd.in/dBppaqVK).
* The textual information is injected through cross-attention layers through the network (https://lnkd.in/dWsrEkpD).
* The resulting denoised image is then decoded by the autoencoder decoder.
* The process is described here: https://lnkd.in/d4NijqmG and one of the best explanation on Stable Diffusion here: https://lnkd.in/dpWMm\_kS. Fun model!

### How to generate animation with Stable Diffusion

But how do we generate those cool animations with STABLE DIFFUSION? Check out the one I did in Replicate: https://replicate.com/p/uzj2czjjzradtjcrzet6yfqdkq. Those animations are mostly due to the fact that it is easy to interpolate between 2 images or 2 text prompts in the latent space (embedding representations). The DALL-E 2 article explains that pretty well: https://arxiv.org/pdf/2204.06125.pdf.
You need a start and end prompt. I chose “A picture of a bear” and “A picture of an apple”.
You then encode those texts in the latent space using the text encoder of the CLIP model (https://openai.com/blog/clip/), and you use the interpolation between the 2 text prompts to guide the denoising process of a random image for a few steps. This is just to anchor the denoising process in between the 2 prompts such that the animation is less jumpy.
You then create as many intermediary interpolations between the 2 prompts as you need frames in your animation, and continue the denoising process until getting clean images.
If you need smoother animations, you simply interpolate between the generated images in the latent space.
I have had a lot of fun playing with Andreas Jansson’s implementation of animations with Stable Diffusion: https://replicate.com/andreasjansson/stable-diffusion-animation. He is using the pretrained model on Hugging Face (https://huggingface.co/…/huggingface…/diffuse-the-rest). You can learn more about it my Newsletter: https://newsletter.TheAiEdge.io/
—-
Follow me for more Machine Learning content!

### 🚀 Stable diffusion stands out among diffusion models, Here is Why.

Stable Diffusion (SD) offers Knobs to trade-off Speed, Sample quality and Guidance for high fidelity.

Here are the ideas that made those properties possible:

→ Latent diffusion: Originally Diffusion models operated on Pixel space, hence computationally exorbitant, Latent diffusion projects images to a Latent space.

This means a immaculate tradeoff between sample quality and speed. Hence SD lends itself to high quality 512x512 samples in acceptable speeds. Canva introduced text to image using SD, recently.

→ Non-Markovian noise scheduling: Diffusion models noise and de-noise images along number of time steps . Akin to sequence modelling like in RNNs.

But RNNs are better than Markov models for sequence modelling because they defy markov porperty and can learn long range relationships.

Honouring the same tradition SD uses DDIM (and cousins), a set of Non-markovian noising schedulers to accelerates sampling as opposed to slower markovian DDPM.

SD exposes num\_inference\_steps for this, more the steps, better the image quality.

→ (Noise Conditional) Score-Based Modelling:

Typically likelihood models like VAE, Flow based, EBMs and implicitly generative models like GANs have multiple challenges.

Latter is unstable (owing to mode collapse) which inspite of adversarial training trades off diversity for quality.

Former tries to model the probability density (or mass) function of the distribution of the data which quickly becomes intractable mathematically. Hence score based models offers a perfect side stepping, to model a tractable score function using schedules of noise and measures performance by score matching techniques like Fischer’s divergence.

→ Classifier free guidance: Originally diffusion was aimed at unconditional generation. To condition the generation with text, guided diffusion was introduced, it was done using an ancillary classifier model that trades-off diversity of samples for fidelity aka faithfulness to the prompt.

Idea is to use the gradient of the classifier model trained on noisy images to guide demonising during inferences.

But thanks to Jonathan Ho, he introduced classifier free guidance (CFG), SD uses this technique and exposes a single scalar parameter called “guidance scale”. CFG removes the need for one extra model. DALL-E(CLIP), GLIDE and ImageGen (T5) all use a classier based guidance.

On the downside, CFG is one of the potential reasons why you need to write elaborate prompts for SD and but that’s not the case with DALL-E.

## ML Youtube channels

Sometime we just need to sit back and relax watching videos! Here are great YouTube channels to learn Machine Learning from. Enjoy:

* What’s AI by Louis Bouchard: https://lnkd.in/euVngxvQ
* Abhishek Thakur (Practical videos, Talks) : https://lnkd.in/eTPrcvEN
* Ahlad Kumar (Deep learning, Theoretical): https://lnkd.in/eVGxpXfw
* Aladdin Persson (PyTorch, TensorFlow): https://lnkd.in/e29966pV
* Andreas Mueller: https://lnkd.in/eQYM3WyC
* Data School (Python, Machine learning, Theoretical): https://lnkd.in/eXEjf27Q
* Connor Shorten (Theoretical): https://lnkd.in/ejdwwyzq
* Jeremy Howard (Deep learning, Theoretical): https://lnkd.in/ec3DGa7g
* Rasa (Rasa, AI, NLP): https://lnkd.in/ehUe-qPE
* Yannic Kilcher (NLP, Machine learning, Deep learning, Theoretical): https://lnkd.in/ebRk-bMB
* OpenAI (NLP, Machine learning, AI): https://lnkd.in/eWvCKiqz
* Two Minute Papers (Machine Learning and AI Research, Scientific Papers): https://lnkd.in/eQY\_5\_SV
* Machine Learnia (Machine Learning, Scikit Learn, Python): https://lnkd.in/enFTrVh9
* Mark Saroufim (Machine Learning Engineering, Practical videos, Books review): https://lnkd.in/ez32nFS5
* sentdex (Python for AI and Finance): https://lnkd.in/eMsdgVbS

I found that curated list of YouTubers on this awesome repo: https://lnkd.in/eVgmFN8Y. That repo has similar lists for many other software skills, so make sure to check it out.

## DALLE-2

* How does DALL-E 2 work? DALL-E 2 generates non-deterministic images from text data.
* It is basically a combination of 2 models: a CLIP model that predicts image from text and a diffusion model that predicts non-deterministically images from image embeddings.
* First, they train a Contrastive Language-Image Pre-training (CLIP) model that predicts images with text inputs: https://lnkd.in/eGNMirji, https://lnkd.in/eHbmBb2t.
* By training that model, they obtain a CLIP text embedding T and an image embedding E.
* The second model is a Diffusion model that takes an image embedding E and predicts non-deterministic images: https://lnkd.in/erwcgzzz, https://lnkd.in/eC3FRMMq

-> Piping those 2 models together, a text caption can be used to predict an image embedding E that in turn can be used to predict non deterministic images.

* Learning those embeddings lead to interesting properties.
* For example, we can take 2 images and their resulting embeddings E1 and E2 and continuously interpolate between the 2 embeddings in the latent space.
* This results in having the capability to create new images that seem to have their styled mixed together with a lot of control.
* We can also do a very similar thing with the text embedding by having 2 text captions and their resulting embeddings T1 and T2.
* By interpolating between those 2 again in the latent space, we can continuously create images that capture the intermediate meaning of the 2 captions.
* The results are honestly baffling! I think with models like GAN and now Dall-E, we have entered an era of Machine Learning where engineers are able to put together specialized models together in a creative way to achieve what doesn’t look like what we used to call “Machine Learning” anymore.
* You can find the Dall-E 2 article here: https://lnkd.in/evk2QQWd, https://lnkd.in/e6HDhscP, and you can compare it to Dall-E 1: https://lnkd.in/etpBqDjK. If you want to play with it, you can try the OpenAI API: https://lnkd.in/ePSKNNWN

## Forward-Forward Algorithm

* We may not need the BACK PROPAGATION algorithm anymore! Hinton is presenting results on the Forward-Forward algorithm: https://lnkd.in/gkU\_tqNz.
* The first forward pass in done with real data and the second forward data is done with “negative data” and the weights are learned by computing a local gradient. It seems to have 2 advantages: first, it to work well enough on a few problems for now, and second, there seems to be possible to separate the 2 forward learning phases.
* Imagine if you could train the forward passes and the backward passes at different points in time. I will need time to build a good intuition on that one!
* At each layer, the local “target” P is the sum of the square of the activation functions squeezed in the probability space by a logistic function and a threshold.
* The real data should lead to P ~ 1 (activations above the threshold) and the negative data should lead to P ~ 0 (activations below the threshold).
* The gradient can be computed locally and the weights can be updated using that “local classification” process.
* For image classification for example, the real data could be a pair of image X and a target y (X, y), where the negative data can be an image X paired with a random target y’ (X, y’).

You can find a PyTorch implementation of the Forward-Forward algorithm in this repo: https://lnkd.in/g58uv7TK. I am looking forward to see more experimental results on that one.
I have a feeling that this is going to change Deep Learning as we know it!

## ChatGPT

* Do you know how ChatGPT was trained? ChatGPT is “simply” a fined-tuned GPT-3 model with a surprisingly small amount of data!
* Moreover, ChatGPT is using 1.3B parameters where GPT-3 uses 175B parameters! It is first fine-tuned with supervised learning and then further fine-tuned with reinforcement learning. They hired 40 human labelers to generate the training data. Let’s dig into it!
* First, they started by a pre-trained GPT-3 model trained on a broad distribution of Internet data (https://lnkd.in/gAUtxvrM).
* Then sampled typical human prompts used for GPT collected from the OpenAI website and asked labelers and customers to write down the correct output.
* They fine-tuned the model with 12,725 labeled data.
* Then, they sampled human prompts and generated multiple outputs from the model for each of the prompt. A labeler is then asked to rank those outputs.
* The resulting data is used to train a Reward model (https://lnkd.in/gdrzdWu3) with 33,207 prompts and ~10 times more training samples using different combination of the ranked outputs.
* We then sample more human prompts and they are used to fine-tuned the supervised fine-tuned model with Proximal Policy Optimization algorithm (PPO), a Reinforcement Learning algorithm (https://lnkd.in/gsDTWtga).
* The prompt is fed to the PPO model, the Reward model generates a reward value, and the PPO model is iteratively fine-tuned using the rewards and the prompts using 31,144 prompts data.

This process is fully described in here: https://lnkd.in/gnt9K9pu. The paper actually details a model called InstructGPT which is described by OpenAI as a “sibling model” to ChatGPT, so the numbers shown above may be slightly different from the exact ones used for ChatGPT.

What is it about ChatGPT we get so impressed by? GPT-3’s output is no less impressive but why does ChatGPT’s outputs feel “better”? The main difference between ChatGPT and GPT-3 is the tasks they are trying to solve. GPT-3 is mostly trying to predict the next token based on the previous tokens, including the ones from the user’s prompt, where ChatGPT tries to “follow the user’s instruction helpfully and safely”. ChatGPT is trying to align to the user’s intention (alignment research). That is the reason InstructGPT (ChatGPT’s sibling model) with 1.3B parameters give responses that “feel” better than GPT-3 with 175B parameters.

The Training

ChatGPT vs GPT-3

The Training
ChatGPT is “simply” a fined-tuned GPT-3 model with a surprisingly small amount of data! It is first fine-tuned with supervised learning and then further fine-tuned with reinforcement learning. In the case of InstructGPT, they hired 40 human labelers to generate the training data. Let’s dig into it (the following numbers were the ones used for InstructGPT)!

First, they started by a pre-trained GPT-3 model trained on a broad distribution of Internet data (GPT-3 article). Then sampled typical human prompts used for GPT-3 collected from the OpenAI website and asked labelers and customers to write down the correct outputs. They fine-tuned the model in a supervised learning manner using 12,725 labeled data point.

Then, they sampled human prompts and generated multiple outputs from the model. A labeler is then asked to rank those outputs. The resulting data is used to train a Reward model (https://arxiv.org/pdf/2009.01325.pdf) with 33,207 prompts and ~10 times more training samples using different combinations of the ranked outputs.

They then sampled more human prompts and they were used to fine-tuned the supervised fine-tuned model with Proximal Policy Optimization algorithm (PPO) (https://arxiv.org/pdf/1707.06347.pdf), a Reinforcement Learning algorithm. The prompt is fed to the PPO model, the Reward model generates a reward value, and the PPO model is iteratively fine-tuned using the rewards and the prompts using 31,144 prompts data.

## ML for Ads Ranking RecSys

At Meta, we were using many different paradigms of Recommendation Engines for ADS RANKING.
Conceptually, a recommender system is simple: you take a set of features for a user U and a set of features for an item I along with features C capturing the context at the time of the recommendation (time of the day, weekend / week day, …), and you match those features to an affinity event (e.g. did the user click on the ad or not):
click or not = F(U, I, C).

-In the early days they started with Gradient Boosting models.
Those models are good with dense features (e.g. age, gender, number of clicks in the last month, …) but very bad with sparse features (page Id, user Id, Ad Id, …).
By the way, we often talk of the superiority of Tree based models for tabular data, well this is a real exception to the rule!
Those sparse features are categorical features with literally billions of categories and very few sample events. For example, consider the time series of sequence of pages visited by a user, how do you build features to capture that information? That is why they moved to Deep Learning little by little where a page Id becomes a vector in an embedding and a sequence of page Ids can be encoded by transformers as a simple vector. And even with little information on that page, the embedding can provide a good guess by using similar user interactions to other pages.

-Typical models we were using were Multi-task learning (https://lnkd.in/gVZ7HrUz), Mixture of experts (https://lnkd.in/dE6XZvJx) or Multi-towers models (https://lnkd.in/gPZ-GfRS).
In Ads Ranking, the ranking happens in stages: first you select a sub-universe of ads (let’s say 1M ads) that relate to the user (very fast retrieval), then you select a subset of those ads (let’s say 1000 Ads) with a simple model (fast inference) and then you use a very complex model (slow inference) to rank the resulting ads as accurately as possible. The top ranked ad will be the one you see on your screen. We also used MIMO (multi-inputs multi-outputs) models to simultaneously train the simple and complex models for efficient 2 stages ranking.

-I cannot think of a model type that capture better the success of ML in our societies. Google search, Google or Facebook Ads, Youtube suggestions, Netflix movie suggestions, Amazon products search, … are all the results of decades of research in recommender systems and are all top drivers of the cash flows for those companies.

## Is PageRank still used at Google

Is PageRank still used as part of Google Search? Yes we know it is as we can see in the list of systems that are currently in use: https://developers.google.com/…/ranking-systems-guide. PageRank is a metric of importance of a website as measured by how connected that website is to others (https://snap.stanford.edu/…/cs224w…/Brin98Anatomy.pdf). It used to be the main way websites were ranked in Google Search, leading to its success at the time, but now searches are personalized where PageRank is a global metric. We don’t know how it is used, but we can pretty much guess!

* A Google search happens in stages. First, the search query is expanded and used to perform an initial Document Selection. This document selection is driven by keywords matching in a database. If I type today “google search”, Google tells me there are about 25B results related to my search.
* Then results go through a set of Recommender engines. There is most likely a simple Rec Engine first ranking a large amount of documents (maybe 100,000 or 10,000 documents) and a complex one refining the ranking of the top ranked documents (maybe 100 or 1000). Who cares about the quality of the ranking for the documents far in the list of documents! The websites are probably already ranked by PageRank in the initial document selection as it can be computed at indexing time. There is no need to send all 25B documents to the first Rec engine, and PageRank is most likely used as a cutoff to send a small subset.
* However it is unlikely that PageRank is the only cutoff parameter as some websites would never get discovered. I would expect some simple geolocalization and context matching metrics as well as randomization to be used as well.
* At this point the ranking becomes personalized, and user data becomes the main factor, but PageRank is likely to still be used as a feature for all the successive Rec Engines used in the search pipeline.

Obviously those are educated guesses as those information are not public. You can learn more about it my Newsletter: https://newsletter.TheAiEdge.io/

## CLIP

How would you know if an image is “similar” to its text caption? Conceptually, you could “simply’’ measure the cosine similarity between the image and the text. That is the idea behind CLIP (Contrastive Language-Image Pretraining: https://openai.com/blog/clip/), the OpenAI algorithm underlying Dall-E 2 (https://arxiv.org/pdf/2204.06125.pdf) and Stable Diffusion (https://arxiv.org/pdf/2112.10752.pdf). An intermediate latent vector representation of the image and the text is learned such that a high value of the dot product is indicative of high similarity.
First, they created a dataset of 400M pairs (image, text) from publicly available datasets on the internet.
Then they used a 63M parameters Transformer model (A small GPT-2 like model: https://cdn.openai.com/…/language\_models\_are…) to extract the text features T and a Vision transformer (https://arxiv.org/pdf/2010.11929.pdf) to extract the image features I.
The resulting vectors are further transformed such that the text and image vectors have the same size. With N (image, text) pairs, we can generate N^2 - N pairs where the image does not correspond to the text caption. They then take the normalized dot product (cosine similarity) between T and I. If the text corresponds to the image, the model receives a label 1 and 0 otherwise, such that the model learns that corresponding image and text should generate a dot product close to 1.
This model has a lot of applications in zero-shot learning! In typical image classification, we feed the model with an image, and the model provides a guess from a set of predefined text labels used during the supervised training. But with CLIP, we can provide the set of text labels we want the model to classify the image into without having to retrain the model because the model will try to gauge the similarity between those labels and the image.
We can virtually build an infinite amount of Image classifiers by just switching the text labels! The article ( https://arxiv.org/pdf/2103.00020.pdf) showcases the robustness of CLIP to generalize to different learning tasks without the need to retrain the model. In my opinion, this adaptability of ML models shows how much closer we are from true Artificial Intelligence! CLIP is an open-source project (https://github.com/openai/CLIP), so make sure to try it.

## Quick Feature Selection Method

This is a technique I like to perform a quick FEATURE SELECTION for Machine Learning applications. I tend to call it the “Random Bar” method! Let’s assume you have a feature set X and a target Y. Let’s create a random vector V (for example np.random.normal(size=(1, 100))) and append that vector as a new feature to X:
X’ = [X, V]
X’ is just the original feature set with additionally the new random feature. Keep in mind that this new feature cannot possibly help to predict the target Y since it is random! Now, take that data (X’, Y) and train a Supervised Learning algorithm with a Feature Importance measure that is relevant for you application. Intuitively, the mean entropy gain per split of tree based algorithms (Random Forest, Xgboost, …) is a convincing measure of feature importance to me. The statistical fluctuation of the data is such that even the random feature will be attributed a non-zero feature importance by the algorithm, but we know it is artificial. Any feature with a lower feature importance than the random feature has to be useless to predict the target and the features with a higher feature importance are at least better than random noise at predicting the target.
This is especially useful if you have thousands of features and you want to weed out quickly the ones that won’t have any impact in the learning process. This is also a method that can be used for highly non-linear data as opposed to LASSO (for example) that tends to only understand linear relationships in the data. The random feature is a “Random Bar” because this is the minimum bar a feature needs to beat to be a part of the potentially useful features set. Now it doesn’t mean there are not additional features that could be beneficial to further remove to optimize your model. Do you know if this method has a more jargon-y name?
What is your favorite feature selection method?

## Overfitting

After sharing various methods that reduce overfitting yesterday, I found some intriguing new research studying the effect of pruning on the generalization performance.

It’s been known that pruning (producing smaller models) can improve generalization performance. At the same time, we also know that larger, overparameterized models can improve generalization performance (e.g., see double decent and grokking).

So, how can we reconcile the observation that pruned models can exhibit better generalization performance with contradictory observations from double decent and grokking studies? Researchers recently showed that the reduction of overfitting due to pruning could be partly explained by the improved training process[. Pruning involves more extended training periods and a replay of learning rate schedules that are partly responsible for improved generalization performance.

On noisy datasets, however, the generalization performance improvements due to pruning can be explained by a larger loss on noisy training examples. Why is a larger loss on noisy training examples better? Presumably because the pruned models don’t try to fit these noisy examples, which adds a regularizing effect – this is somewhat similar to reducing the width of the layers.

* Suppose your deep neural network suffers from overfitting. In that case, there is a large pool of techniques and approaches to choose from (I separated the most common ones into dataset and model perspectives two days ago).

Now, the follow-up question is, which of the techniques gives you the most gain?
Weight decay (with AdamW) is definitely one you should consider in your regularization cocktail.

In the figure below, I summarized 4 references that discuss different aspects of weight decay and its effects on overfitting.

## Pruning

After sharing various methods that reduce overfitting yesterday, I found some intriguing new research studying the effect of pruning on the generalization performance.

It’s been known that pruning (producing smaller models) can improve generalization performance. At the same time, we also know that larger, overparameterized models can improve generalization performance (e.g., see double decent and grokking).

So, how can we reconcile the observation that pruned models can exhibit better generalization performance with contradictory observations from double decent and grokking studies? Researchers recently showed that the reduction of overfitting due to pruning could be partly explained by the improved training process[. Pruning involves more extended training periods and a replay of learning rate schedules that are partly responsible for improved generalization performance.

On noisy datasets, however, the generalization performance improvements due to pruning can be explained by a larger loss on noisy training examples. Why is a larger loss on noisy training examples better? Presumably because the pruned models don’t try to fit these noisy examples, which adds a regularizing effect – this is somewhat similar to reducing the width of the layers.

## Information Retrieval Metrics

I may be wrong, but I think it is quite unlikely that Google ML ENGINEERS are using typical information retrieval metrics to assess the offline performance of the ML classifiers used within Google Search or similar search engine! There are ~3.5 billion searches per day, with each search generating a lot of positive and negative samples. If you train a classifier on that data, you probably want to spam at least a few days of data if not more. It is an extremely class imbalanced problem, so you’ll probably want to downsample the majority class for the computation to be manageable. That is still tens of billions of samples for each model development at least!

A metric like Normalized Discounted Cumulative Gain (NDCG) requires the concept of relevance (gain) to part of the data. That can be achieved with manual labeling but that is NOT going to be manageable on billions of samples. Metrics like Mean Reciprocal Rank (MRR) or Mean Average Precision (MAP) requires to know the true rank of the sample, meaning if I assess a classifier on a validation data, the predicted rank per search session is not going to be meaningful if we downsampled the data, and the metrics will be extremely dependent on the specific sampling scheme.
We could imagine that we downsample the number of sessions instead of the majority class, but this forces us to only keep the top samples shown by the algorithms. That seems unwise since this will prevent ML engineers from experimenting with new sampling methods in future developments and the models will never see very negative samples, which is a bit problematic if we want to build an accurate model. The same problem occurs with a metric like Hit rate, since you need a window size.

If you order the search results by the probability of click provided by the classifier, the log-loss (or cross entropy) is a completely acceptable ranking metric. It is a point-wise metric, which means it doesn’t require us to know the predicted rank of the sample to compute a meaningful value. The probability itself will be biased by the false class distribution coming from the downsampling, but this can be corrected by recalibrating the probability p ​​using the simple formula: p’ = p / (p + (1-p) \* s), where s is the negative sampling rate (https://eva.fing.edu.uy/…/Elkan\_2001\_The\_foundations\_of…).

With a probability metric such as the log-loss, I expect more freedom for the ML engineers to experiment with new techniques. For example, in the case of search engines, we could label with 1 the clicked links and 0 the non-clicked links, but you could also imagine that the negative samples are only sampled from unsuccessful sessions (where the users did not find the right link). In a successful session, the non-clicked links are not really “bad”, they are just less interesting to the user. To be able to assess across models and teams, it might be useful to use the normalized entropy metric (https://deychak.github.io/normalized-cross-entropy) as anything above 1 is worse than random.

## XGBoost

“XGBoost is ALL you need!” Well, it is true until it is not. Algorithms like Linear Regression have their number of degrees of freedom (d.o.f. - complexity) scaling with the number of features O(M). In practice, this means that their ability to learn from the data will plateau in the regime N » M where N is the number of samples (typically large data sets). They have a high bias but a low variance and as such they are well adapted to the N > M regime. In the N < M regime, L1 regularization becomes necessary to learn the relevant features and zero-out the noise (think about having more unknowns than equations to solve a set of linear equations). Naive Bayes d.o.f. scales as O(C x M) (or O(M)depending on the implementation) where C is the number categories the features are discretized into. O(C) = O(N) in theory but not really in practice. This makes it a lower bias algorithm than LR but it is a product ensemble of univariate models and ignores the feature interactions (as LR does) preventing it from further improvements.   
A tree in its unregularized form, is a low bias (you can overfit the data to death), with d.o.f scaling as O(N), but high variance (deep trees don’t generalize well). But because a tree can reduce its complexity as much as needed, it can work in the regime N < M by simply selecting the necessary features. A Random Forest is therefore a low bias algorithm but the ensemble averages away the variance (but deeper trees call for more trees) and it doesn’t overfit on the number of trees (Theorem 1.2 https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf), so it is a lower variance algorithm. The homogenous learning (the trees tend to be similar) tends to limit its ability to learn on too much data.
XGBoost is the first (to my knowledge) tree algorithm to mathematically formalize regularization in a tree (eq. 2 https://arxiv.org/pdf/1603.02754.pdf). It is a low bias and high variance (due to the boosting mechanism) and is therefore adapted to large data scales. The GBM Boosting mechanism ensures a more heterogenous learning than RF and therefore adapts better to larger scales. The optimal regularization ensures higher quality trees as weak learners than in RF and tends to be more robust to overfitting than RF.
In the regime N » M, only low bias algorithms make sense with d.o.f. scaling as O(N). That includes algorithms like GBM, RF, Neural Networks, SVM (gaussian), KNN,… SVM has a training time complexity of O(N^3) (unmanageable!) and KNN is bad at understanding what is an important feature and has dimensionality errors scaling as O(M). Neural Networks are known to underperform compared to XGBoost on tabular data.
So, if you are working on large data, XGBoost MAY be all you need! But make sure to prove it to yourself. The no Free-Lunch Theorem doesn’t mean we cannot understand our algorithms and build an intuition on what are the best use cases to use them!
—
Follow me for more Machine Learning content!
#machinelearning #datascience #XGBoost

A question often arises when teaching is how XGBoost and LightGBM differ. The short fun-fact summary is that the tree-building algorithms are a tad different.

XGBoost’s trees are based on breadth-first search, comparing different features at each node.

LightGBM performs depth-first search, focusing on a single feature at a time and growing the tree from there.

1) BFS : Is memory intensive, take more time to execute. Likely to underfit if stop early. To control this I guess some package has ability to convert that to Uniform Cost search
I believe it will work well where dataset contains more categorical independent variable

2) DFS: Require less memory as compared to BFS. Likely to overfit and stuck in local minima situation. To control this I guess some package has ability to convert that to Depth Limit Search. I believe DFS will work well in number input features.

## Data Parallelization by Sebastian Raschka

When I started grad school, training deep neural networks on a GPU was something special – it was both tricky to do and awesome when it worked).

The world has moved on since then! Nowadays, training a model on a single GPU would be considered a major bottleneck.

Here is a quick overview of the 4 different paradigms for multi-GPU training.

1) Data parallelism
2) Model parallelism
3) Pipeline parallelism
4) Tensor parallelism

## Top 5 basic checks when trianing deep learning models

What are some of the basic things you should watch out for when training deep neural networks? Here are my top 5:

1) Make sure training loss converged
2) Check for overfitting
3) Compare accuracy to a zero-rule baseline
4) Look at failure cases
5) Plot at a confusion matrix

Bonus! some additional suggestions from the community:

6) Make sure your model is able to overfit to a small dataset (like 1000 examples) or a single minibatch. (Tip 3 from Andrej Karpathy’s “A Recipe for Training Neural Networks” https://lnkd.in/gvfgqxTQ)

7) Check whether layers have converged to a good alpha (e.g., using weightwatcher). See https://lnkd.in/gHDHDXAu

8) Check how confident your model is on out-of-distribution data (a common problem for neural nets); one out of many papers on this topic: https://lnkd.in/gsjSVYcd

9) Apply your model to new data from the application domain (e.g., if you train a handwritten digit classifier, try your own handwritten digits)

## A list of 5 techniques to optimize deep neural network model performance during inference

## Links for MLOPS

Ok, let’s learn about MLOps!

Courses:

* Made With ML: https://madewithml.com/
* Coursera - DeepLearning.AI MLOps specialization: https://lnkd.in/gVrxJqQS
* Coursera - Google MLE certificate: https://lnkd.in/gVNNpzzR
* MLOps Zoomcamp: https://lnkd.in/gt2QH7sz
* Berkeley Full Stack Deep Learning: https://lnkd.in/gG8jR2Vg
* Udemy - Deployment of Machine Learning Models: https://lnkd.in/g7TpQ\_dM
* Udemy - MLOps Fundamentals CI/CD/CT: https://lnkd.in/gkW9Gkrj
* Udemy - Testing and Monitoring Machine Learning Model Deployments: https://lnkd.in/g4qAw9Hq
* MLOps Certification Training: https://lnkd.in/guRq627D
* MLOps Engineering on AWS: https://lnkd.in/g-tnpKuY
* AWS Machine Learning University: https://lnkd.in/g-jjMk3Q
* EdX - MLOps with AWS: https://lnkd.in/gYE37jDN
* MLOps Course Certification: https://lnkd.in/gDGUXPR7
* GCP MLOps Fundamentals: https://lnkd.in/geNjGNyP
* Stanford MLSys Seminar Series: https://lnkd.in/gdNWPceY
* DataRobot MLOps Starter: https://lnkd.in/gMQYSitX
* Udacity - Become a Machine Learning Engineer for Microsoft Azure: https://lnkd.in/garedV7K
* LinkedIn - Applied Machine Learning Foundations: https://lnkd.in/ghWPcHHq
* Unifying MLOps at Microsoft: https://lnkd.in/gsKyb3Dq

Books:

* Machine Learning Engineering: https://lnkd.in/gjyw35fh
* Introducing MLOps: https://lnkd.in/gZzh\_cYz
* What Is MLOps?: https://lnkd.in/g\_vgYKMh
* Practical MLOps: https://lnkd.in/gbGnj7ss
* Reliable Machine Learning: https://lnkd.in/gCvje923
* Designing Machine Learning Systems: https://lnkd.in/gRmEkHwj

Repos:

* Awesome MLOps: https://lnkd.in/gqCWbuQT
* Awesome Production Machine Learning: https://lnkd.in/g8zfBRSB

---

I offer Machine Learning consulting services: https://lnkd.in/gqzuB6kM
I offer Data Science career mentoring: https://lnkd.in/gGBMXuR4  
10% off coupon on DataInterview.com: damien10off

## Architecture

Deep Learning requires much more of an ARCHITECT mind set than traditional Machine Learning. In a sense, the feature engineering work has been moved to the design of very specialized computational blocks in DL using smaller units (LSTM, Convolutional, embedding, Fully connected, …). I always advise to start with a simple net when architecting a model such that you can build your intuition. Jumping right away into a Transformer model may not be the best way to start.

DL is very powerful in the case of multi-modal input data: time series, tabular data, text data, image data. One approach is to encode all those different data types into a simple vector and feed that into a logistic regression (LogReg) or a linear regression (LR) (or with more fully connected layers to add non-linearity) depending on if you need to perform classification or regression. When developing a simple model, start with a low capacity network and increase little by little the complexity to reduce the bias while adding regularization to keep the variance low.

A conv layer is meant to learn local correlations. Multiple successive blocks of conv and pooling layers allows to learn the correlations at multiple scales and they can be used on image data (conv2d), text data (text is just a time series of categorical variables) or time series (conv1d). For example you can encode an image using a series of conv2d and pooling layers like in VGG (https://lnkd.in/g6Jp6NmD, https://lnkd.in/gDjUGWFE). You can encode text data using an embedding (pretrained obviously https://lnkd.in/gt5N-i6R) followed by a couple of conv1d layers. And you can encode a time series using series of conv1d and pooling layers.

I advise against using LSTM layers when possible. The iterative computation doesn’t allow for good parallelism leading to very slow training (even with the Cuda LSTM). For text and time series ConvNet are much faster to train as they make use the of the matrix computation parallelism and tend to perform on par with LSTM networks (https://lnkd.in/g-6Z6qCN). One reason transformers became the leading block unit for text learning tasks, is its superior parallelism capability compared to LSTM allowing for realistically much bigger training data sets.

In general it is not too hard to train on multi-modal data. As a simple example:

* time series vector = Pool1d(Conv1d(Pool1d(Conv1d(time series))
* image vector vector = Pool2d(Conv2d(Pool2d(Conv2d(image data))
* text vector = Pool1d(Conv1d(Pool1d(Conv1d(Embedding(text data)))
* tabular data vector = FC(FC(tabular data))
  => X = FC(FC(time series vector, tabular data vector, text vector, image vector))
  The nice thing with DL, you can train on multiple targets at once using multiple target heads: Y\_1 ~ LR(X), Y\_2 ~ LogReg(X)

## Recommender Engine

[Netflix](https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429)
[matrix factorization](https://datajobs.com/data-science-repo/Recommender-Systems-%5BNetflix%5D.pdf)
[Recsys paper](https://daiwk.github.io/hidden/assets/hidden/youtube-multitask.pdf)
[A multi-task framework for metric learning with common subspace](http://www.nlpr.ia.ac.cn/2013papers/gjkw/gk30.pdf)
[Linkedin](https://engineering.linkedin.com/blog/2021/homepage-feed-multi-task-learning-using-tensorflow)
[linkedy](https://www.linkedin.com/pulse/personalized-recommendations-iv-two-tower-models-gaurav-chakravorty/)
[DGCN: Diversified Recommendation with Graph Convolutional Networks](https://fi.ee.tsinghua.edu.cn/public/publications/b344fd48-92b0-11eb-96bc-0242ac120003.pdf)
[recsys](https://journal.hep.com.cn/fcs/EN/article/downloadArticleFile.do?attachType=PDF&id=23822)

Recommender Engine might be one of the most PROFITABLE Machine Learning Model paradigms right now but I think it doesn’t get the recognition it deserves! There are many ways to generate money with ML but the niche business applications where Rec Engines are typically used makes it a more certain high ROI ML application in general. The business value of Rec engines is clear: personalized matching between a user and a product. That is the bread and butter of many big tech companies:

* search engine: Google search, Amazon Product Search, …
* Ads ranking: Google and Meta generate 65% of the world digital ad revenue
* Feed ranking: FB, Instagram, LinkedIn, …
* Product Recommendation: Netflix’s landing page, …

The modern approach to Rec Engine can be tracked back to the 2006 Netflix Recommendation contest (https://lnkd.in/ds6WWEG3) where the Latent Matrix Factorization method won second place (https://lnkd.in/dz4q7Xnx). Surprise is a nice python implementation: http://surpriselib.com/. In a supervised learning term, we use user data, product data and context data as input to estimate the affinity of a user to a product: affinity ~ F(user data, product data, context data). Those algorithms are peculiar because we want to use the same user and product population at training time than inference time: in a sense, we want to overfit on the user behavior.

Now Deep Learning dominates the field by extending on the original linear models and it led to many new NN architectures. Embeddings provide a natural mechanism to featurize the large users and products spaces and their related behavior history. Some architecture examples:

* Multi gate Mixture of Experts for Youtube videos recommendation: https://lnkd.in/dE6XZvJx
* Multi-Task Metric Learning for multi-staged inference when the product space is too large: https://lnkd.in/dSpiR9GA, https://lnkd.in/dZErXbpE
* Two Tower models for retrieval: https://lnkd.in/dh3Xtmyc
* Multi-tower model for ads ranking in Pinterest: https://lnkd.in/d\_uPNSAH
* Diversified recommendation with Graph Convolutional Networks: https://lnkd.in/dfcVYeDJ
* Autoencoder-based recommender: https://lnkd.in/dET64Pvs

This is an interesting space and a valuable expertise to have those days. I wish there were more textbooks on the subject! One to get started: https://lnkd.in/deMyYw5e

## How to detect Data Drift

There is one simple technique I like to use to detect DATA DRIFT for Machine Learning applications. First, take a current data set and let’s call it X\_now. Then let’s take an old data set and let’s call it X\_old. You could imagine having different X\_old for different time scales: 1 week ago, 1 month ago, 1 year ago, … Let’s now create an artificial target Y\_now where all the values are 1 and another Y\_old where all the values are 0. Y\_old would be paired with the X\_old samples and Y\_now with the X\_now ones. We can concatenate X\_now with X\_old and Y\_now with Y\_old:

X = [X\_now, X\_old]  
Y = [Y\_now, Y\_old]

Now take that data (X,Y) and train a Supervised Learning algorithm that has a good built-in Feature Importance measurement process. For example, I like to take a Random Forest algorithm that has typically a Feature Importance measured as a mean entropy or Gini gain per split through the whole forest. If one or few features are coming out as having a high feature importance to predict that artificial target, this is a strong evidence that those features have been drifting over time!

What techniques do you like to use to detect Data Drift?

## How to decompose Bias and Variance from the Data

Have you ever tried to compute the BIAS and VARIANCE separately from the data? It is not as simple as one may think! I think we all know the typical decomposition formula (https://lnkd.in/gjQ3n7fj):

E[(y - f(x))^2] = Bias[f]^2 + Var[f] + sigma^2
with Bias[f] = E[f(x)] - f(x)

But did you realize that the Expected value and Variance range over different realizations of the training data D = (X, Y) sampled from the same probability distribution P(X,Y)? To obtain the Mean Square Error (MSE) you need then to run an expected value over the instance distribution this time

MSE = E\_x[E[(y - f(x))^2]]

Estimating E\_x[.] is easy, you just need to run a sum over the test set: sum(.) / N, where N is the number of samples in the test set. But how do you go about the first expectation?

One way I find intuitive to understand (https://lnkd.in/g49Q9Tjr) is to create M bootstrap samples of the training data D and to train your learner L on each of those sample. For each instance of the test set you can then predict M different values for each of the trained learners. And then you can estimate the expected value for each instance as

mean = sum\_i [ f(x\_i) ]/ M
variance = sum\_i [ (f(x\_i) - mean)^2 ]/ (M - 1)

And easily estimate the local Bias and Variance for each instance and then average over all the instances in the test set to get MSE.

The following article compares 3 different methods to estimate the Bias and Variance decomposition on real data: https://lnkd.in/gptRH8gp

Is that something you have been wondering about?

## Feature Selection Method

This is a technique I like to perform a quick FEATURE SELECTION for Machine Learning applications. I tend to call it the “Random Bar” method! Let’s assume you have a feature set X and a target Y. Let’s create a random vector V (for example np.random.normal(size=(1, 100))) and append that vector as a new feature to X:

X’ = [X, V]

X’ is just the original feature set with additionally the new random feature. Keep in mind that this new feature cannot possibly help to predict the target Y since it is random! Now, take that data (X’, Y) and train a Supervised Learning algorithm with a Feature Importance measure that is relevant for you application. Intuitively, the mean entropy gain per split of tree based algorithms (Random Forest, Xgboost, …) is a convincing measure of feature importance to me. The statistical fluctuation of the data is such that even the random feature will be attributed a non-zero feature importance by the algorithm, but we know it is artificial. Any feature with a lower feature importance than the random feature has to be useless to predict the target and the features with a higher feature importance are at least better than random noise at predicting the target.

This is especially useful if you have thousands of features and you want to weed out quickly the ones that won’t have any impact in the learning process. This is also a method that can be used for highly non-linear data as opposed to LASSO (for example) that tends to only understand linear relationships in the data. The random feature is a “Random Bar” because this is the minimum bar a feature needs to beat to be a part of the potentially useful features set. Now it doesn’t mean there are not additional features that could be beneficial to further remove to optimize your model. Do you know if this method has a more jargon-y name?

What is your favorite feature selection method?

## Self Instruct aligning language models with self generated instructions

Sergio Valmorisco Sierra
Sergio Valmorisco Sierra
• 2nd
Global Senior Data Scientist at JLL
3h • 3 hours ago

Follow

Large “instruction-tuned” language models (finetuned to respond to instructions) have demonstrated a remarkable ability to generalize zero-shot to new tasks. Nevertheless, they depend heavily on human-written instruction data that is limited in quantity, diversity, and creativity, therefore hindering the generality of the tuned model. In this work, the authors introduce SELF-INSTRUCT, a semi-automated process for instruction-tuning a pretrained LM using instructional signals from the model itself.

The overall process is an iterative bootstrapping algorithm, which starts off with a limited (175 in their study) seed set of manually-written instructions that are used to guide the overall generation. In the first phase, the model is prompted to generate more broad-coverage instructions that define (often new) tasks. Given the newly-generated set of instructions, the framework also creates input-output instances for them, which can be later used for supervising the instruction tuning. Finally, various measures are used to prune low-quality and repeated instructions. This process can be repeated for many interactions until reaching a large number of tasks.

Applying their method to vanilla GPT-3, the authors demonstrate a 33% absolute improvement over the original model on the SUPER-NATURALINSTRUCTIONS dataset, on par with the performance of InstructGPT001, which is trained with private user data and human annotations. For further evaluation, they curate a set of expert-written instructions for novel tasks, and show through human evaluation that tuning GPT-3 with SELF-INSTRUCT outperforms using existing public instruction datasets by a large margin, leaving only a 5% absolute gap behind InstructGPT001.

Code and data: https://lnkd.in/d\_Wd52Uu
Paper: https://lnkd.in/dS8wuBBh
