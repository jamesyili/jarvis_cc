# Transformers / RLHF / AI Safety / Scaling — reference material

*Source: `interview_prep/system_design_prep.pdf`, pages 83–93. James's prep notebook — extracted text, lightly cleaned.*

---

Seq2seq, Attention, Transformers
 ● Seq2seq: Input sequence—>Output sequence using encoders and decoders ○ Encoder: LSTM cells and layers, each layer unrolls with token embeddings and previous hidden states as input, until EOS
 ○ Hidden states and cell states gets updated ○ These are fed into the next layer, and instead of word embeddings it’s the higher order representation from the layer below
 ○ The finally layer’s final hidden and cell states become the context vector ○ Decoder: Uses the context vector as well as the input word embedding and feeds into the LSTM cells and module, producing the hidden vector for the next word in the sequence. Separately it predicts the output word, and keeps going until it predicts EOS.

 ● Simple Attention —> decoder does cross attention with encoder tokens ○ Encoder: Processes input sequence into a set of hidden states (representations of each input token).

 ○ Decoder: Uses the context vector and performs cross-attention with the encoder's hidden states to selectively focus on relevant parts of the input sequence when generating each output token.

 ● Transformers —> multi-headed self attention + positional encodings + context matrix + (residual connections and layer norm and decoder masking)
 ○ Encoder: Made of multiple identical layers. Each layer has a multi-head self-attention mechanism followed by a position-wise feed-forward network. Positional encodings are added to the input embeddings to provide sequence order information. The output is a set of context-rich representations for each input token.

 ○ Decoder: Also made of multiple identical layers. Each layer has three sub-layers: masked multi-head self-attention (to prevent attending to future tokens), multi-head cross-attention (to attend to the encoder's output), and a position-wise feed-forward network. Positional encodings are also used. Residual connections and layer normalization are applied throughout both the encoder and decoder.

 ○ Attention(Q,K,V) = softmax(QK^T/sqrt(d_K))V

○ ○ MultiHead(Q,K,V) = Concat(head1, …, headN)W

○

○

○
RLHF / RLAIF / DPO
● Reinforcement Learning from Human Feedback ○ Consists of 3 stages: Supervised Fine Tuning on a small dataset of high-quality human curated demonstrations of desired behavior (input <> output pairs).

 ○ The LLM gives multiple responses to the same prompt, and then the human annotators compare and rank multiple responses at a time, creating a human preference dataset to train a smaller NN called reward model, which outputs a scalar reward score. Usually pairwise ranking loss.

 ○ Finetune the LLM using the reward model to maximize rewards, and balance with a KL divergence measure to prevent it from drifting too far from the original distribution (e.g. to maintain fluency).

 ○ Pro: highly effective, generalizable ○ Con: hard to train, with the final stage being very difficult to tune and can be unstable, and requires extensive, high-quality human labeling, you can get reward hacking (e.g. by being overly verbose or sycophantic)
 ● Reinforcement Learning from AI Feedback

○ Replaces the reward model by human data with a reward model by AI data with constitutional principles in the prompt. These principles can be crowdsourced with company employees, and continuously updated and modified.

 ○ Pros: scalability since we are not as dependent on human labeling to scale, transparency via the constitution → can use chain-of-thought to provide further insights
 ○ Cons: if the AI itself is not well-aligned, then biases or undesired behaviors can propagate, so humans must stay in the loop, the constitution might not be able to encode human values entirely
 ● Direct Preference Optimization ○ Skips the second stage entirely and directly optimizes policy in the model finetuning of the third step
 ○ Negative loss likelihood similar to logistic regression, increase the likelihood of the preferred response from the pair and decrease the likelihood of the rejected response from the pair
 ○ Pros: simpler and more computationally efficient, no need for separate RM model, and comparable performance
 ○ Cons: highly dependent on the data quality, less flexible for complex rewards
Loss Functions and Optimizers
● Loss ○ Cross Entropy (-SUM_categories(y_i * log(y^hat_i))) - typically better for mult-class problems since it maps to a value between 0 and 1, thereby encouraging the model to output higher probabilities for correct classes
 ■ Sensitive to class imbalance, can do weighted cross-entropy ■ Sensitive to mis-labeling which makes labeling and data-cleaning very important
 ■ Doesn’t optimize for overall quality of output in LLMs, so need alignment techniques
 ○ Mean Squared Error (SUM_instances(y_i - y^hat_i)^2) - good choice for regression problems
 ■ Can be very skewed by outliers, not great for classification problems ○ Evidence Lower Bound for VAEs - reconstruction term (MSE or BCE) wants to make the reconstruction accurate, while KL divergence term (distance between learned posterior distribution and prior distribution) wants to regularize the latent space.

 ○ L1 - alternative choice for regression problems when you don’t want to be too skewed by edge cases
 ■ Non-smoothness, optimization may run into more issues ○ Focal - variant of CE that increases loss for hard-to-classify examples ■ More compute, needs tuning focal parameter ○ Contrastive - encourages similar things to be closer in feature space while pushing dissimilar things further out → great for embedding generation
 ■ Need to construct negatives carefully, particular in-batch ● Optimizers ○ SGD and Minibatch SGD - efficient, allows you to escape local minima

○ Adam - uses exponential decaying averages of first moments in order to generate adaptive learning rates based on second moments, only 3 parameters: step size, decay rates for gradient and squared gradient
 ○ SOAP - introduces one additional hyperparameter from Adam, the preconditioning efficiency, and it doesn’t have to compute the full hessian tensor, but use approximations, and can get faster convergence MCP
● Allow AI model providers and external data sources and tools to build once instead of N x N times, while maintaining Security and Context
 ● Hosts (LLM applications like Claude Desktop) ● Client are components within the host that establishes and maintains 1:1 connections with external servers
 ● Servers provide context, tools, and prompts ● 5 core primitives ○ Servers ■ Prompts → instructions or templates that can injected int the LLM context, guiding the flow
 ■ Resources or data → allow the model the reference external information such as memory or knowledge
 ■ Tools → executable function that allows the model to call to modify files or run queries, etc.

 ○ MCP clients ■ Roots → creating a secure channel for file access on the local system (reading code, open documents, etc.)
 ■ Sampling → allows the server to request the LLM’s help when needed (e.g. formulating queries), which creates a two-way interaction that makes is more flexible and powerful

AI Safety
● Transformative AI is on its way if not already here. AI behavior can diverge from what the creators intend: toxicity, bias, dishonesty, hallucination.

 ● With the rate of progress, the applied systems need to be closely tied to the frontier AI systems, yielding predictable but also surprising developments. Empiricism is key.

 ● Core approach ○ Capabilities (improving general AI performance) ○ Alignment Capabilities (making AI helpful, honest, harmless) ■ Automated red-teaming ■ Constitutional AI ■ Debiasing ■ RLHF ○ Alignment Science (evaluating whether AI systems are truly aligned) ● Tactics and outcomes ○ Identify risks posed by AI systems and find safe ways to train powerful AI systems
 ● Defending against Chemical Biological Radiological Nuclear Risks ○ Increasingly strong deployment and security protections to increasingly power AI (ASL 3)
 ■ Specific targeting of categories of misuse of AI that can be catastrophic ■ Security controls to prevent model weight theft ○ Constitutional Classifiers to make the system much more difficult to jailbreak, minor compute overhead with large reduction in jailbreak success
 ○ Continuous synthetic jailbreak attempts via automated red-teaming, which is then used to train new classifiers
 ○ Bring others along with Bug Bounty programs, publication of known attempts to jailbreak (e.g. sophisticated influence operations by networks of people and bots) – threat intelligence assessments and operations
 ● Jailbreak is defined as some way to bypass the normal safeguards of the AI → doing things that are explicitly not desired by the creators of the AI. These can be very long prompts, modifying the style of the input, etc.

Scaling
1. Web Tier Horizontal Scaling → more servers to handle failover, traffic increases a. Vertical just means adding more memory to each computer, which is not sustainable
 b. Load Balancer helps to redirect traffic intelligently, usually pings from outside the network only hits the load balancer, which redirects traffic internally in smart way
 2. Data Tier Database replication → better performance to allow in parallel queries, better reliability and availability
 a. masters handles CRUD while slaves keep replicas and handles reads b. Data vertical scaling is adding more memory or switching machine types: high costs
 c. Data horizontal scaling (aka sharding ) is adding more servers: i. Each shard shares the same schema, but the data on each shard is unique
 ii. Uses hash function to decide which shard to store and fetch data iii. Most important is choosing a partition or sharding key that leads to even distribution of data.
 iv. Challengers with sharding: need to reshard when you have rapid growth, hotspot or hotkey problems (celebrity problems for social networks), etc.

 3. Caches are a temporary data store layer that allows better performance because you have less DB workload and you can scale the cache tier independently based on use-case
 a. Consider when reads are frequent but writes are infrequent. Keep persistent data in DB, not cache

b. Set an expiration and eviction policies (TTL and least frequently used or FIFO are good examples)
 c. Prevent the cache from being single points of failure → if cache fails, have backup DB reads, overprovisioning, etc.

 4. Stateless servers → allows for user session and authentication not to be tied to specific servers, but will require moving session data out of the web tier and into the data tier in something like MemCached/Reids/NoSQL. This enables auto-scaling based on traffic load .

 5. CDN (a kind of cache with focus on geography) → controls which servers are closest and can be used to deliver static content like image / video, CSS, etc.

 6. Data centers → requests are geo-routed, and handle emergencies like natural disasters, etc.
 a. Need data syncs, traffic redirection, automated deployment strategies and tools to keep things consistent between data centers
 7. Message queues → supports async communication and acts as buffer and distributor of requests , allows for more efficient usage of compute via decoupling of concerns
 a. Publisher & subscribers 8. Logging, metrics, monitoring, CI/CD can be seen as a separate component 1. Back of Envelope calculations for various numbers if necessary a. How many users do we expect per day and what is the average QPS? Do we expect to handle failovers?
 b. Latency

i. RAM read is 300x faster than disk read (30ms), 100x faster than network read (10ms)
 ii. Worldwide roundtrip is 150 ms, which is 300x faster than a roundtrip in the same data center
 c. Downtime in a year: 99% or 0 9’s → 3.5 days, 2 9’s → 1 hour, 3 9’s → 5 mins, 4 9’s → 30 seconds
 d. Twitter example: i. 300 MAU, 50% DAU → 150m, 2 posts per day avg, 10% has media, Data stored 5 years
 ii. QPS: 150m * 2 / (24 * 3600) = 3000 - 4000, peak is 2x so 7000 iii. Storage: text less than 0.001% → mostly media, 1mb → 30TB per day → 60 TB for 5 years
