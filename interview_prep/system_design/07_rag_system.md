# [Design] RAG System

*Source: `interview_prep/system_design_prep.pdf`, pages 44–49. James's prep notebook — extracted text, lightly cleaned.*

---

[Design] RAG System



1. Clarifying questions: a. What does the external knowledge base consist of? Does it change over time? b. Text, images, or other modalities? PDF or some other format? c. How many pages in total? d. Do we expect any growth in pages? e. Do we need to cite document references? f. How much latency is acceptable? g. Should it be Multi-lingual to start? h. Any user feedback or follow-up questions? i. I assume we need to address safety concerns such as preventing harm, bias, and NSFW responses?

 2. Frame as ML: a. To accommodate external data sources, there are 3 types of approaches (with a pre-trained LLM):
 i. Finetuning → updating the weights of the pre-trained LLM 1. Pro: enhanced accuracy, handling of niche topics, domain-specific 2. Con: expensive to train, requires frequent retraining whenever there is new information, no referencing
 ii. Prompt engineering → better prompts to adjust the outputs 1. Pro: easy to do, cost effective, flexible

2. Con: Limited customization, Limited to LLM’s existing knowledge iii. RAG → combines real-time retrieval system with a LLM generation component
 1. Pro: access to up-to-date information (retrieval now a separate system), contextual relevance
 2. Con: implementation complexity, retrieval quality now matters b. RAG offers a balanced solution between prompt engineering and finetuning 3. Data Prep a. Document Parsing (e.g. PDF parser) i. Layout detection using object detection → segmented regions ii. Within each region run OCR if it’s detected to be text, or run some image encoder into an embedding
 iii. Structured output iv. Usually handled by some external service b. Document Chunking i. Too long of a doc loses semantic relevance easily, and hard to pick up on key details, so want to break them up into smaller chunks. Need to think about chunk size and overlap, smaller chunk size results in more fragmented knowledge making it harder to return enough context to the final LLM but returned context may be more relevant, while too large of chunk size end up losing key details again.
 ii. Can do length-based, regular expression-based, or markdown/html iii. LangChain typically handles this c. Indexing i. Organize the chunked data that enables efficient and accurate search ii. Inverted index is a mapping of words to Document IDs in which these words appear. This enables efficient full-text search by mapping each term to a list of documents. It’s foundational in search engines. Updates require carefully handling index maintenance for insertions and deletions.
 iii. Semantic Vector Based Index is a mapping of ID to high dimensional vectors. It typically allows for fast similarity search using HNSW, IVF, PQ using ANN. These trade exact recall for speed. At query time we return top K highest cosine similarity vectors.
 iv. Suppose each page contains roughly 1,500 characters and includes three images. Using length-based chunking with a chunk size of 500 characters and a 200-character overlap, each page will generate 5 text chunks and 3 image chunks. Therefore, the total number of chunks the RAG system is dealing with is 5M(1500 / (500-200) + 3)=40M. This figure is expected to grow by roughly 20 percent each year …
 4. Modeling a. Inside the RAG you would use models in 3 places. Indexing to have text and image encoders transform chunked text images into embeddings, in retrieval to transform the user query into embeddings, and the LLM in Generation.
 b. For text encoding, you might want to consider the encoder only Transformer, or some LSTM/GRU RNN network, though the former have been shown to be far more effective.
 c. For image encoding, you might want to consider an encoder only transformer or CNN. CNN are great at capturing spatial hierarchies through convolution filters.

Transformers would require turning the image into a sequence by patching, then sent into the multihead attention with positional encodings.
 d. You will want both decoders to map to the same space. You can use encoders that already do that like CLIP, or you can do image captioning. In the latter you would have an image encoder and a text decoder.
 e. Training: Typically these models are already pretrained, but since there are multiple components, you’ll likely have to tune the parameters associated with each step of the process. We can look at the top ones.
 i. Finetuning via RAFT. RAFT is to train a model based on (Question, Retrieved Docs, Answer) golden sets, where the Retrieved Docs are labeled as relevant or irrelevant. This teaches the LLM to discriminate between relevant and irrelevant sources, and force it to extract and cite evidence.
 ii. When finetuning, you can do full on model updates which can require extremely large amounts of domain-specific data, or do something like Low Rank Adaptation (LORA), where you train a delta weight matrix that is a projection from two much smaller matrices. Delta W = B*A, and you would update W with Delta W.
 f. Sampling: ANN can be improved by clustering the embeddings together and then doing both inter-cluster search and intra-cluster search, or HNSW to speed up computation.
 g. Generation: Here is where we would need effective prompt engineering i. Lots of depth here. Some reasonably effective practices I’ve seen. ii. Start simple and iterate from there. Break down complex tasks. Use specific and clear instructions. Give example outputs with the degree of specificity you want (e.g. few-shot prompting). Role-specific prompting to get the output language in the style and level you want.

 5. Eval - every part of the system, as well as the end-to-end response a. Offline Eval i. Retrieval evaluation → Precision@K, Recall@K, Hit Rate, Mean Reciprocal Rank (MRR), NDCG
 ii. How well the LLM summarizes the documents → faithfulness or groundedness, how much hallucination, reliability and consistency (across multiple runs)
 1. Human Eval 2. LLM-Eval with Human in the Loop to audit and improve the Eval instructions
 3. Fact-checking against some knowledge base of curated iii. Search Relevance techniques on the final output and input query 1. NDCG based on Human evals of relevance, correctness, completeness, conciseness, understandability
 2. F1 score which measures the overlap of the response and the reference answer at the token level
 3. Correctness measures from Machine Translation since it’s sequence of tokens in and sequence of tokens out (BLEU, ROUGE)
 b. Online Eval i. User feedback (thumbs up, thumbs down)

ii. Rephrasing the query and attempting it again (can differentiate this by time passed since last query or semantic relevance of consecutive queries)
 6. ML System a. Query expansion to increase the chances of having better retrieval b. Safety filtering of the input and of the potential output 7. Monitoring a. Failures i. Feature outages (feature distribution drift, NULL values → may lead to NULL predictions)
 ii. Stale model predictions (no retraining, data drift) iii. System failures (latency, throughput, versioning) iv. Traffic spikes (GPU / CPU utilization) v. Code path failures (what’s AB tested wasn’t what was launched) vi. Feedback loops
