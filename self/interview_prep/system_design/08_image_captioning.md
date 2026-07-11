# [Design] Image Captioning

*Source: `interview_prep/system_design_prep.pdf`, pages 50–54. James's prep notebook — extracted text, lightly cleaned.*

---

[Design] Image Captioning

1. Clarify Requirements:

● Primary Goal: Generate short, descriptive, and clear text captions (name suggestions) for general everyday images, specifically for designers uploading assets.

 ● Input/Output: Image → Text Caption. ● Image Type: General everyday images (not domain-specific like medical). Min resolution 256x256 pixels.

 ● Caption Length/Detail: Short, descriptive, clear. Not long/detailed. ● Language: English only. ● Dataset: Large (400M image-caption pairs). ○ Data Quality: Raw dataset may contain non-English, duplicates, irrelevant, missing captions.

 ● Latency: Quick generation (1-2 seconds acceptable). Not strict real-time. ● Ambiguous Content: System should skip suggesting a caption if image content is unclear/ambiguous (confidence threshold).

 ● Safety/Fairness: Crucial to avoid biased or offensive captions .

2. Frame as ML Task:

● ML Objective: Generate text captions that accurately describe image content, suitable for asset naming.

 ● System Input: Image. ● System Output: Text caption. ● ML Category: Multi-modal Language Generation (Image-to-Text). ○ Approach: Encoder-Decoder Framework . ■ Image Encoder: Understands visual content, encodes image into a lower-dimensional representation.

 ■ Text Decoder: Uses encoded visual info to generate the descriptive caption.

 ○ (Note: Acknowledge alternatives like BLIP-2/3, InternVL, but focus on Encoder-Decoder for this design).

3. Data Preparation:

● Data Choice: 400 million image-caption pairs. ● Caption Preparation: ○ Remove Non-English Captions: Filter out non-English captions to align with English-only requirements.

 ○ Remove Duplicates: 1. Images: Use perceptual hashing or image similarity models (e.g., CLIP image encoder).

 2. Captions: Exact match or semantic similarity (e.g., CLIP text encoder). Prevents overfitting, improves diversity.

 ○ Remove Irrelevant Captions: Use a pre-trained vision-language model (e.g., CLIP) to assess relevance (image-text similarity score). Remove pairs below a threshold (e.g., 0.25). Ensures high-quality relevant data.

 ○ Summarize Long Captions: Use an LLM (e.g., Llama) to summarize excessively long captions into concise descriptions. Ensures generated captions are short as required.

 ○ Normalize Captions: Lowercasing, trim whitespaces for consistency.

○ Tokenize Captions: Subword-level tokenization (e.g., BPE) for vocabulary efficiency and OOV handling. Convert tokens to IDs.

 ● Image Preparation: ○ Remove Low-Resolution Images: Filter out images < 256x256 pixels as per requirements.

 ○ Normalize Images: Scale pixel values (e.g., 0-1) for stable training. ○ Remove Low-Quality Images: Filter blurry, over/underexposed images using image quality assessment methods (e.g., LAION Aesthetics Predictor).

 ○ Adjust Dimensions (Resize & Center-Crop): 1. Resize: Scale image so smaller dimension matches target size (e.g., 256).

 2. Center-Crop: Crop the resized image to the final fixed square target size (e.g., 256x256), preserving aspect ratio.

4. Modeling:

● Architecture: Encoder-Decoder framework. ● Image Encoder: ○ Purpose: Process image, encode visual information. ○ Output Type: Sequence of tokens (patches) preferred over single token. ■ Rationale: Captures granular local details and global features. Aligns well with attention mechanism of text decoder, enabling selective focus on image regions for detailed captions.

 ■ (Contrast with single token: Simpler, less compute, but loses local detail, leads to generic captions).

 ○ Architecture Choice: Transformer-based (e.g., ViT) . ■ Why: Excels at capturing both local and long-range global relationships in images using self-attention. Crucial for descriptive, context-aware captions. (CNNs struggle with long-range dependencies).

 ■ Components: ■ Patchify: Divide image into fixed-size patches → flatten → linear projection into embeddings.

 ■ Positional Encoding: Assigns position info to each patch. ■ Choice: 2D (preserves spatial structure) or 1D. Learnable vs. Fixed (e.g., sine-cosine). (ViT uses learnable 1D, but experimentation is key).

 ■ Transformer Blocks: Apply self-attention and feed-forward networks.

 ● Text Decoder: ○ Purpose: Generate the caption one token at a time. ○ Architecture Choice: Decoder-only Transformer (standard for text generation).

 ○ Input: Sequence of embeddings (from Image Encoder). ● Training Strategy (Two-Stage): ○ Unsupervised Pre-training: ■ Text Decoder: Pre-train on general text data (e.g., using next-token prediction with Cross-Entropy loss).

 ■ Leverage: Use existing pre-trained decoder-only Transformers (e.g., GPT-2, Llama) to save compute.

■ Image Encoder: Leverage existing pre-trained vision models (e.g., CLIP, ViT).

 ○ Supervised Fine-tuning: ■ Train both Image Encoder and Text Decoder jointly on the 400M image-caption pairs.

 ■ ML Objective: Next-token prediction. ■ Loss Function: Cross-Entropy Loss . ■ Purpose: Guides the text decoder to accurately predict the next token in the ground truth caption sequence, given the image encoding and previously generated tokens.

 ● Sampling: ○ Method: Beam Search ■ Rationale: Prioritizes quality, consistency, and coherence for asset name suggestions.

 ■ Quality: Higher-quality captions. ■ Consistency: Deterministic output for same image. Crucial for asset management where consistent naming is preferred.

 ■ Coherence: Avoids nonsensical or ungrammatical phrases. ■ (Avoid stochastic methods like Top-K/Top-P, as they prioritize creativity/diversity over the deterministic coherence needed for asset naming).

5. Evaluation:

● Offline Metrics: ○ Validation Data: Image + multiple human-annotated reference captions (for robust training & comprehensive evaluation).

 ○ Primary Metric: CIDEr (Consensus-based Image Description Evaluation) . ■ Why: Specifically designed for image captioning. Emphasizes consensus with multiple references and weights important words (via TF-IDF). Robust to variations.

 ■ Process: 1. Represent generated and reference captions using TF-IDF. 2. Calculate Cosine Similarity between generated and each reference caption's TF-IDF vector.

 3. Aggregate (average) similarity scores. ■ Pros: Consensus-based (reliable), sensitive to important words, robust to variations.

 ■ Cons: Computationally complex, sensitive to reference quality, can penalize novel but accurate captions, relies on TF-IDF (might lack full semantic understanding).

 ○ Secondary Metrics: BLEU, ROUGE, METEOR (for broader perspective on fluency, recall, precision).

 ● Online Metrics: ○ Primary Focus: Not primary evaluation method due to difficulty in collecting direct user feedback/interaction data for backend systems.

 ○ If Applicable (e.g., if integrated into UI): Engagement metrics (e.g., adoption rate of suggested names), user feedback mechanisms for qualitative assessment.

6. Overall ML System Design (Serving):

● Components: 1. Image Preprocessing: ■ Takes raw input image. ■ Resizes, normalizes pixels, adjusts dimensions (resize & center-crop). Ensures image is consistent with model input expectations.

 2. Caption Generator (Core): ■ Receives preprocessed image. ■ Passes image through trained Image Encoder to get sequence of embeddings.

 ■ Feeds embeddings to Text Decoder . ■ Employs Beam Search to generate the caption token by token. ■ Confidence Thresholding: If cumulative probability of generated caption falls below a predefined threshold, suggestion is skipped (to handle ambiguous images).

 3. Post-processing: ■ Receives generated caption. ■ Bias/Safety Check: Identifies and replaces biased terms/phrases with neutral alternatives. Checks for offensive words and disables suggestion if found. (Strategic: Direct alignment with Anthropic's safety imperative and your strength in "power-with-softness" and "high integrity").

7. Monitoring:

● System Health: Latency (critical for 1-2s target), throughput, error rates of preprocessing, generator, and post-processing components.

 ● Model Performance (Offline): Continuous CIDEr (and other metrics) monitoring on validation/test sets to track model quality and detect degradation.

 ● Safety/Bias Monitoring: Log captions flagged/modified by post-processing. Develop internal metrics/audits for bias detection in generated captions.

 ● Ambiguity Handling: Monitor the rate of "skipped suggestions" due to low confidence. ● Data Drift: Monitor characteristics of incoming images (e.g., resolution, content themes) to ensure they match training distribution.

Other Potential Discussion Points (for senior roles / if time permits):

● Multi-Lingual Captioning: Extend to other languages. ● Domain Adaptation: Adapting the model for more specific image types beyond everyday images.

 ● Edge Device Optimization: For low-latency or offline use cases. ● Multiple Captions: Generating and ranking several plausible captions. ● Visual Question Answering (VQA): How the system's components could form a foundation for other V+L tasks.
