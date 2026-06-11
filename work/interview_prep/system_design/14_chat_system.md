# [Design] Chat System

*Source: `interview_prep/system_design_prep.pdf`, pages 80–82. James's prep notebook — extracted text, lightly cleaned.*

---

■ Ensures final display list adheres to platform standards. ● Indexing Pipeline: (Figure 2.19 - left side) 1. Indexing Service: ■ Responsible for processing all images on the platform into embeddings (using the same trained model as the prediction pipeline).

 ■ Adds these embeddings to the index table for the Nearest Neighbor Service.

 ■ Keeps the index updated as new images are uploaded (e.g., near real-time ingestion).

 ■ Optimization: Uses vector quantization (e.g., Product Quantization) to reduce memory usage for storing billions of high-dimensional embeddings.

7. Monitoring: ● System Health: Latency, throughput, error rates of Embedding Generation, Nearest Neighbor, and Re-ranking services.

 ● Model Performance (Offline): Continuous nDCG monitoring on held-out evaluation sets to detect model/data drift.

 ● Model Performance (Online): Real-time monitoring of CTR and Average Time Spent metrics. Alerting on significant drops or unexpected changes.

 ● Data Quality: Monitor incoming image data for anomalies. Monitor clicks for changes in patterns.

 ● Nearest Neighbor Accuracy: Regularly sample ANN results and compare against Exact NN (for a small subset) to monitor the recall-precision trade-off of the ANN algorithm.

Other Potential Discussion Points (if time permits / for senior roles): ● Content Moderation: Briefly mention the integration points for safety classifiers (e.g., after initial retrieval, or as part of the re-ranking service to filter NSFW/inappropriate images). Strategic: Connects to your expertise and Anthropic's mission.

 ● Image Metadata: How tags, contextual info, etc., could be used to improve results (e.g., multi-modal embeddings, filtering).

 ● Active Learning / Human-in-the-Loop: For efficiently labeling ambiguous examples or identifying new types of similar images for training data. Strategic: Aligns with your "scaling through TLs/EMs" and "operational excellence" strength.

 ● Biases: Discuss potential biases (e.g., positional bias, popularity bias) in click data and how to mitigate them in training or re-ranking.

[Design] Chat System
 Ask Clarifying Questions: ● Primarily 1:1 or Group? Both

○ Group limit? 100 ● Mobile or Web app? Both ● Scale? 50m DAU ● Important features (e.g. attachments? Online indicators?) Online, push notification, no attachments
 ● Message size limit? Yes less than 100k characters ● E2E encryption? Maybe ● Storage time? Forever High level proposal: ● Sender client → server → receiver client ○ Server does 2 things: 1) receive message, 1) store message, 2) relay message to the right recipient(s)
 ● Sender request ○ HTTP works well, it’s classic ● Receiver request ○ Websockets (bidirectional and persistent) since it’s much more efficient, especially for the server → receiver client, downside is that there’s additional complexity since you’ll have to handle dropped connections, reconnection logic, and heartbeats
 ○ Polling (client periodically ask) or long polling (hold the connection until timeout or message)
 ● Stateful requests (client <> server) → WS ● Stateless requests (client → server: signups, profile, et.c) → HTTPS ○ Need a load balancer

● Storage: lots of chat, recent chats access frequently, might require some random access sometimes, read to write ratio is about 1:1
 ○ Nosql (HBase or Cassandra) and KvStore( dynamoDB or Redis) allow for easy horizontal scaling, low latency reads, long tail access is cheaper (relative to SQL)
 ● Data Model for 1:1 ○ Message_id ○ Sender_id ○ receiver_id ○ Content ○ Created_timestamp ● Data Model for group chats ○ channel_id ○ Message_id ○ Sender_id ○ Content ○ Created_timestamp ● Message queues are designed for async communication that decouples senders from receivers. Fault tolerance, async processing for logging, pipeline audits, handles traffic spikes via buffering. PubSub system for example allows real-time monitoring and offline logging to be multiple subscribers.

Model Sampling
1. Greedy search - take top probability token at each step a. Fast and simple, good for deterministic responses b. Tends to be hallucinate the least if model is well-trained c. Lacks diversity and can be repetitive 2. Beam search - keeps track of K most probably sequences, then at next step produce K most likely tokens, and produce the new top K most probable. Keep going until EOS token or max length. Select the sequence with highest cumulative probability.
 a. More relevant than greedy search b. Much more coherent and fluent c. Very high computational costs d. Lacks diversity and creativity 3. Top-K sampling: reduce vocab to K most probably tokens, randomly sample one token from reduced set
 a. Introduces more diversity via randomness b. Since we pruned, it prevents gibberish c. For large K this can still be less relevant 4. Top-P sampling: select the smallest set of tokens such that the cumulative probability exceeds P, then random sample from this set.
 a. Adaptive to the probability distribution b. More human like c. Still need to tune P 5. Add in a temperature term that pushes towards more deterministic versus more diversity / randomness.
