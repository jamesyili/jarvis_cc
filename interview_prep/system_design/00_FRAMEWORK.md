# Framework + ML/AI System Design templates

*Source: `interview_prep/system_design_prep.pdf`, pages 1–8. James's prep notebook — extracted text, lightly cleaned.*

---

Framework
 [5-10 mins] Ask Clarifying questions: 1. What are the most important features for this product? 2. What are the success metrics? DAU, number of retries per session (small as possible), satisfaction indicators such as copy text, thumbs up, or end of session and returning the next day.

 [10-15 mins] Propose High Level and Get Buy In: 1. Enthusiasm and propose to work together on this. 2. Back of Envelope calculations for various numbers if necessary a. How many users do we expect per day and what is the average QPS? Do we expect to handle failovers?
 b. Latency i. RAM read is 300x faster than disk read (30ms), 100x faster than network read (10ms)
 ii. Worldwide roundtrip is 150 ms, which is 300x faster than a roundtrip in the same data center
 c. Downtime in a year: 99% or 0 9’s → 3.5 days, 2 9’s → 1 hour, 3 9’s → 5 mins, 4 9’s → 30 seconds
 d. X example: i. 300 MAU, 50% DAU → 150m, 2 posts per day avg, 10% has media, Data stored 5 years
 ii. QPS: 150m * 2 / (24 * 3600) = 3000 - 4000, peak is 2x so 7000 iii. Storage: text less than 0.001% → mostly media, 1mb → 30TB per day → 60 TB for 5 years
 3. Draw an initial high level blueprint, though suggest multiple approaches if possible a. APIs, web servers, data stores, cache, CDN, message queue, etc. b. Do we need API endpoints and database schemas? Where to go deeper? Ask for feedback and communicate
 4. Talk through a few concrete use-cases [15-25 mins] Design deep dive: 1. Prioritize which components to go into first. 2. For senior candidates, it’s likely about system performance such as bottlenecks and resource estimations.

 3. For each type of problem, there’s usually one or two interesting topics that’s important to dig into.

 4. Signal strengths and what you know, don’t go into unnecessary algorithm details [5 mins] Wrap up: 1. Recap the design, refresh their memory 2. Identify potential improvements that can be made

a. Error cases b. Operational issues such as monitoring and rollout c. Handling next scale curve (going from 1m → 10m → 100m) 3. Thank interviewer for their insights and collaboration
ML System Design
1. Clarify requirements a. Business objectives and metrics like DAU, MAU, satisfaction surveys, interactions, prevalence, etc.
 b. Features like interactions, posting, projects, etc. c. Data sources like user logs, labeled data, etc. d. Scale and Performance like how fast, how many DAU, how many items per DAU, growth rate, etc.

2. Frame as ML task a. Examples i. Event ticket selling → maximize number of event registrations, increase registration rate per impression
 ii. Video recommendation → maximize total watchtime iii. Ad prediction → maximize click through rate

iv. Harmful content detection → maximize accuracy, PR AUC, decrease prevalence
 v. Friend recommendation → maximize number of friendships formed b. Input and output i. Post → ML classifier → prob(harmful) ii. <user, event> → ML classifier → Prob(registration) iii. User → ML classifier → prob(event1) , … , prob(eventN) c. Supervised (classifier, regression), Unsupervised (clustering, association), RL (computer agent learns through trial and error with the environment)
3. Data prep a. ETL pipelines from data sources to transform into well-formatted data structures for training, data cleaning
 i. Structured data typically in SQL DBs 1. Pros: Easy to search, predefined schema ii. Unstructured data from logs, audio, image, text typically in NoSQL (JSON, XML, KVStore), data lakes
 1. Pros: Flexible format, supports multiple customers, single source of truth
 2. Cons: no context, slow to search, slow for real-time needs iii. Data Ingestion Layer: 1. User uploads → raw text/image/video → Data Lake (immutable copy)
 iv. Logging & Feedback: All predictions + user appeals logged back to the Data Lake for audit and continuous learning.

 1. Debuggability b. Feature engineering (manual, curated or automatic, NN style) i. Handling missing values rows → filtering is simple but depends on how much you would lose, so consider doing statistical imputation or using a new category to encode the missing data. Would go upstream from there and actually figure out what’s causing the missingness in the first place though. Usually a sign of bad logging, etc.
 ii. Log scaling, z-score normalization, min-max normalization iii. Represent categorical features as one-hot, ordinal integer, or embedding features
4. Modeling a. Establish a simple heuristic baseline → experiment with quick models to establish the end-to-end model training and serving pipeline → switch over to neural networks → consider ensembling, meta-prediction-frameworks, multi-layered frameworks for fraud detection.
 b. Factors to consider for model type: Data needs, training time, number of hyperparameters, auto-retraining, interpretability, compute costs
 c. Often times, sampling is critical to achieve good results (upsampling positives, downsample negatives, how to handle in-batch negative sampling if training embeddings via NCE, consider easy negatives and hard negatives e.g. active learning for adversarial environments)
 d. Loss function & optimizers (in DNN)

e. Dataset, how far back do you go, how big of a model are you training, predictiveness versus staleness → foundational models & finetuning on domain-specific tasks
 f. Distributed training → data parallelism is when you have identical model copies in each worker, split up the data, and do local gradient calculation and then sync up the gradients, but this doesn’t work for very very large models, model parallelism is when you split the model’s layers or even parts of layers across GPUs, then you need to send a single data batch through a sequence of these devices, so now you have to deal with how the GPUs talk to each other and how to make model partitioning and scheduling efficient. Hybrid approaches can also work, where you split data across clusters of GPUs and split model within each cluster. Basically network communication is the biggest design concern
5. Eval a. Offline i. Precision, Recall, F1, ROC-AUC (axes are TPR and FPR, focused on how well the model can distinguish between positive and negative classes), PR-AUC (much more sensitive to class imbalance because the axes are precision and recall, focused on the classifications for the positive class)
 ii. Precision@K, Recall@K, MAP, NDCG iii. BLUE for translation, ROUGE for summarization, CIDER for captioning iv. Fairness and Bias → require metrics for specific hypotheses, hard to have generalized metrics
 b. Online → A/B test is the most straightforward but requires a lot of infra to set up properly (e.g. doing user salts and multiple overlapping experimentation universes), can also consider shadow deploys or canaries to get system logs or offline simulations to estimate user behavior
6. Deployment & Serving a. Cloud vs on-device. Cloud is easy to set up, more accurate due to fewer constraints, faster inference. On-device has no latency, might be cheaper, better for privacy
 b. Model compression → knowledge distillation to produce cheaper student models, quantization either during or post-training, pruning
 c. Online test → shadow test where you run the new model along with existing model, A/B test (sample size, and randomness)
 d. Predictions → batch versus online, online systems require feature systems to also go online, which means logging of feature sets for ML model training or you’ll need separate online feature computation and offline feature computation
 e. Caching predictions (semantic caches)

f.

7. Monitoring a. Failures i. Feature outages (feature distribution drift, NULL values → may lead to NULL predictions)
 ii. Stale model predictions (no retraining, data drift) iii. System failures (latency, throughput, versioning) iv. Traffic spikes (GPU / CPU utilization) v. Code path failures (what’s AB tested wasn’t what was launched) vi. Feedback loops
AI System Design
Modern Generative models include Autoregressive models (Transformers for NLP, time series), diffusion models that do image or video generation, GANs (train both a generator and discriminator in parallel, generator produces realistic data, while discriminator distinguishes)
 Recent factors unlocking its improvements: ● Data - SSL nature of GenAI models allow it to tap into Books, Github, Social Media, curated datasets for different domains without human labeling
 ● Model size - tons more parameters (Claude hundreds of billions), FLOP counts due to model architecture
 ● Compute - advances in data and model parallelisms, stability allow training over thousands of GPUs for weeks or months at a time, also very costly and power-consuming
 ● Scaling laws: recent research suggests that model size matters much more than variants of model architecture, though the latter can help significantly with efficiency

1. Clarify requirements a. Business objectives and metrics like DAU, MAU, satisfaction surveys, interactions, prevalence, etc.
 b. Features like interactions, posting, projects, etc. c. Data sources like user logs, labeled data, etc. d. Scale and Performance like how fast, how many DAU, how many items per DAU, growth rate, etc.

2. Frame as ML task a. Generative (text, image, video, audio) versus Discriminative (classification, regression)
 b. Inputs (text, image, video, audio) and Outputs c. A single model for all modalities or multiple models for more modalities? d. Which generative algorithm is best suited and why? (Diffusion, GANs, Autoregressive)
3. Data Prep a. Structured data like SQL-like tabular data is likely not the core. LIkely unstructured data such as text, images, videos, audio, etc.
 b. Data Collection i. Scraping the internet, social media, books, videos, etc. ii. Can augment with GenAI produced dataset to improve data diversity and have more data, but synthetic data (1) may be less complex than real-world, (2) lower quality thereby spreading errors, (3) not diverse or representative enough
 iii. Typically you’ll want to collect 2 sets of data: (1) for your foundational or pretrained models, (2) for the domain-specific fine-tuning
 c. Data Cleaning i. Clean and remove misinformation, NSFW or harmful materials ii. Dedupe to assure data is representative and to ensure diversity iii. Watch for bias or other low quality content from affecting model performance
 d. Data Efficiency i. Storage in Parquet and ORC, which are column-oriented and offer things like data skipping by having statistics like max/min/counts associated with each column in the file. These lead to reduced I/O operations for faster reads. Homogeneity in the data leads to better compression like dictionary encoding, etc. which means faster data retrieval and lower storage costs.
 ii. Sharding the data row-wise, or horizontally partitioning the data across multiple devices allows parallel access, easy scalability, and fault tolerance. As with all sharding, we want the key to give us even data distribution.
 iii. Indexing for much faster searches avoids full scans, as well as inverted indexes like Lucene which (“safety” → docs1,2, “classifier” → docs1, 7,8) enables fast full-text keyword search, fuzzy search. Set up HNSW for vector search (FAISS)
 iv. May want to consider adding a caching layer for frequently accessed documents

4. Modeling a. Model architecture - Seq2seq, attention, transformers (section) b. Model Training and ML datasets i. Training process and datasets: Diffusion models denoise data to generate high-quality samples from noise, GANs rely on adversarial training.LLMs typically follow (1) pretraining on large datasets such as common crawl, (2) supervised finetuning on specific tasks relying on curated labeled datasets, (3) alignment stage to ensure outputs are aligned with values and intended behaviors.
 ii. ML objectives and loss function: LLM is to predict next token, VAE is original image reconstruction. Loss functions typically follow the same as before.
 c. Objectives and loss functions (section) d. Speed up Model Training i. Distributed Training - Data parallelism & model parallelism 1. Data parallelism uses a parameter server to update gradients and model parameters across different GPUs, using the same model copy and different data splits on each GPU
2. 3. When updating the model parameters, can do synchronous where PS waits for all gradient updates, aggregate, and send it to all devices. This has to wait for the slowest device. Async updates all other machines whenever PS gets a gradient update and finishes its own computation.

 4. Model parallelism - each device contains some set of layers, so the devices are passing the activation weights in the forward pass and the gradients in the backward pass. To go deeper, I would imagine you’d have to split the tensor operations across different devices.

 5. Can also do a hybrid approach.

ii. Mixed Precision training - uses fp32 only for critical calculations, and fp16 otherwise
 e. Model Sampling to determine how to output from the model i. Greedy search - take top probability token at each step 1. Fast and simple, good for deterministic responses 2. Tends to be hallucinate the least if model is well-trained 3. Lacks diversity and can be repetitive ii. Beam search - keeps track of K most probably sequences, then at next step produce K most likely tokens, and produce the new top K most probable. Keep going until EOS token or max length. Select the sequence with highest cumulative probability.

 1. More relevant than greedy search 2. Much more coherent and fluent 3. Very high computational costs 4. Lacks diversity and creativity iii. Top-K sampling: reduce vocab to K most probably tokens, randomly sample one token from reduced set
 1. Introduces more diversity via randomness 2. Since we pruned, it prevents gibberish 3. For large K this can still be less relevant iv. Top-P sampling: select the smallest set of tokens such that the cumulative probability exceeds P, then random sample from this set.

 1. Adaptive to the probability distribution 2. More human like 3. Still need to tune P v. Add in a temperature term that pushes towards more deterministic versus more diversity / randomness.

5. Eval a. Offline Eval i. Standard offline metrics ii. HITL evaluation iii. Hallucination (automated fact checking) iv. Safety and policy compliance b. Online Eval (engaging stakeholders on what makes most sense) i. Prompt-response latency ii. Task success rate (e.g. ticket resolved) iii. Average handle time (when human have to intervene) iv. Survey, NPS v. Engagement vi. Retention vii. Prevalence of harms
6. ML System a. Components: core model, preprocessing, content filtering, post-processing, upscaling
 b. Scalability → number of users, new features (e.g. image, video understanding and generation)
 c. User feedback and continuous learning → systems in place to retrain models with updated data to improve accuracy and relevance over time
