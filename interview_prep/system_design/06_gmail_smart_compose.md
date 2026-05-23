# [Design] Gmail Smart Compose

*Source: `interview_prep/system_design_prep.pdf`, pages 39–43. James's prep notebook — extracted text, lightly cleaned.*

---

Defense in Depth Strategy
● Input Validation : Schema validation, input sanitization, rate limiting ● Model Security : Adversarial robustness, prompt injection resistance ● Output Filtering : Multi-layer content filtering, explanation generation ● Audit Trail : Complete request logging, decision justification, compliance reporting
Robustness and Reliability
● Graceful Degradation : Fallback to rule-based systems during model failures ● Circuit Breakers : Automatic failover when classification accuracy drops ● Chaos Engineering : Regular testing of system resilience under attack ● Disaster Recovery : Multi-region backup, rapid recovery procedures
Privacy and Compliance
● Data Privacy : End-to-end encryption, PII detection and masking ● Regulatory Compliance : GDPR, SOC2, industry-specific requirements ● Access Control : Role-based permissions, audit logging, principle of least privilege ● Data Governance : Retention policies, right to deletion, data lineage tracking
Bias Detection and Mitigation
Proactive Bias Prevention
● Training Data Auditing : Systematic bias detection in constitutional synthetic data ● Fairness Constraints : Demographic parity enforcement during model training ● Adversarial Debiasing : Adversarial training to reduce biased predictions ● Multi-stakeholder Review : Diverse expert panels for bias assessment
Ongoing Bias Monitoring
● Real-time Metrics : Demographic breakdown of classification decisions ● Regular Auditing : Periodic bias assessment across user populations ● Feedback Loops : User community input on biased system behavior ● Mitigation Strategies : Rapid response protocols for discovered bias issues
[Design] Gmail Smart Compose
 Questions: 1) personalized to their writing style? 2) only suggest when there’s a certain level of confidence or need to suggest all the time? 3) can we use past emails or just whatever text is in the current draft? 4) language that needs to be supported? 5) controlling for bias and NSFW content? 6) how many users? Is cost a concern? Latency constraints?

 Frame as ML: <Input partial text> → Smart Compose System → <output rest of the text>

Seq2seq models (RNN such as GRUs, LSTMs versus Transformers)
 FlashAttention and GroupAttention can help mitigate the O(N^2) attention computation Data Prep: 1. Data Choice a. General text data i. Probably want to use this to train a foundational LLM model, since it’s a lot more diverse and has a lot more data, so we can get a much more powerful model.
 b. Email data i. <Email ID, Sender, Recipient, Subject, Body> ii. This is critical to adapt the specific domain of email text in general → brevity, singular focus, common phrases and styles, etc.

 2. Cleaning the data a. Need to clean the data text and normalize it to get rid of noise, then we need to tokenize the text and index the tokens to create the vocabulary.
 b. Remove Unique Identifiers → jamesli@gmail.com strip out the name, phone numbers, etc. c. Remove irrelevant characters or symbols like emojis in the first pass and focus more on the words, for websites you’ll want to remove irrelevant text to the content, (affiliate links, etc.)
 d. Remove duplicated data e. Tokenization i. Character-level, word-level, or sub-word level ii. Character level will be too conflated with meaning for each character, too overloaded, so it’s hard to learn a meaningful representation
 iii. Word level typically may be too big of a vocab (e.g. hundreds of thousands), long training times, costly, etc. And OOV happens quite often
 iv. Subword level will require more complexity to implement how to split, but can be worth the tradeoffs. Benefits are that you can decompose OOV into seen subwords, smaller vocab (sub 100k). Typical algorithms are Byte-pair Encode (BPE) or SentencePiece.
 f. Token indexing i. Token, ID → the, 0 | …. | <EOS>, 50,003 ii. Now can apply this to the raw text Modeling:

1. Encoder, Decoder, or both? a. Encoder is good for discriminative tasks (e.g. raw text → encoder → prediction on sentiment)
 b. Decoder is good for transforming input sequence into a new output sequence c. Encoder and decoder good for translation
d. e. Given Smart Compose is taking in partial text and returning remainder of text, decoder-only seems good
 2. Decoder-only components that need to be trained: a. Token embedding → word2vec style improves semantic relevance and helps with sparsity versus one-hot encoding
 b. Position embedding → add the position embedding of the tokens to the token embeddings element wise to ensure different embeddings for each position even for the same tokens. You can do fixed position embedding like the original transformer paper, which uses sine-cosine functions, or you can learn the position embeddings. The latter may give better performance but at more compute cost and may not generalize as well.
 c. Multi-head attention or self-attention → basic attention, Query/Key/Value, which processes the sequence into a set of hidden states and performs cross-attention for each output token, which is a weighted sum of value vectors. Self-attention does this H times for learning different relationships, and concats the each attention head into the linear heads. There’s also a residual layer to allow for more efficient learning.
 d. Prediction head → projects into the vocabulary space using the token probability distribution
 3. Pretraining using next token prediction task with cross-entropy loss, this is using the large corpus of diverse text dataset
 4. Finetuning the same model (or a pre-trained model) on email dataset a. Same prediction task, same loss function, calculate loss based on the email data and prediction

b. Can add in context from the email itself (e.g. recipient email, sender email, subject)
 i. Dear … → Dear John c. System prompt is very important → prompt engineering 5. Model output sampling (link) a. Prefer more deterministic methods such as greedy and top P / top K since we likely would want consistency, more common phrases, and reduce the risk of inappropriate suggestions.

 Eval 1. Offline a. Perplexity, which gets at how accurately the model predicts the exact sequence of tokens present in text data. Mathematically, this is the average negative log-likelihood of the predicted probability given the previous tokens
 b. ExactMatch@K, which is the percentage of generated phrases that are exactly N words long and match the first N words of the ground-truth text. Can have multiple versions of K to understand how well the model captures short, medium, and long responses.
 c. Standard BLEU and ROUGE scores based on human evaluation can also be used here
 2. Online a. Acceptance rate b. Usage rage c. Average completion time of emails d. System response latency e. Feedback f. Human eval for qualitative assessments ML System design
 1. Monitoring & Triggering: The service triggers the phrase generator once it identifies specific patterns such as specific keywords or number of characters typed

2. Calls Model: The phrase generator employs beam search to get top-k potential completions from the trained model.

 3. Filtering: The phrase generator interacts with the filtering component to remove long suggestions and those with low confidence scores.

 4. Post-processing: The completion with the highest score is picked and passed to the post-processing service. The service replaces gender-specific pronouns and adjusts sensitive terms.

 5. Display suggestion: The suggestion is displayed to the user for their consideration.
