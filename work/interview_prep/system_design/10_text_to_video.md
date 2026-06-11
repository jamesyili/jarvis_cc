# [Design] Text to Video

*Source: `interview_prep/system_design_prep.pdf`, pages 59–65. James's prep notebook — extracted text, lightly cleaned.*

---

● Prompt Distribution Analysis: Track common prompts, emerging trends, and any problematic prompt patterns.

Other Potential Discussion Points (for senior roles / if time permits): ● Consistency Models: For even faster generation. ● RLHF for Quality/Alignment: Applying human feedback (or AI feedback) to refine generated image quality and alignment beyond simple loss functions. Strategic: Directly links to Anthropic's core alignment work.

 ● Inpainting/Outpainting: Extending functionality. ● Personalization: Fine-tuning models to specific user styles/concepts. ● Advanced Controls: ControlNet for precise control over generated images. ● Ethical AI: Deep dive into the ethical challenges of generative AI (deepfakes, misinformation, copyright, representational harm). Strategic: Your strengths in high integrity and analytical thinking.

[Design] Text to Video



1. Clarify Requirements: ● Primary Goal: Generate 5-second, 720p (1280x720 pixels), 24 FPS videos from text descriptions.

 ● Input/Output: Text prompt → Video. ● Latency (Generation): A few minutes initially (acceptable), with future optimization. ● Content Category: General, diverse genres/subjects. ● Language: English text input only (initially). ● Audio Output: Silent videos (initially).

● Training Data: 100 million diverse video-caption pairs (some noisy/non-English). ● Pre-existing Assets: Access to a pre-trained text-to-image model (assumed for extension).

 ● Compute Budget: Over 6000 H100 GPUs (significant resources available). ● Safety/Fairness: Crucial to prevent generating offensive or harmful videos.

2. Frame as ML Task: ● ML Objective: Generate videos that visually and temporally align with a given text prompt.

 ● System Input: Descriptive text prompt. ● System Output: 5-second, 720p, 24 FPS video. ● ML Category: Multi-modal Generative AI (Text-to-Video). ○ Approach: Latent Diffusion Model (LDM) . ■ Rationale: Extends successful text-to-image diffusion to video. Crucially, operates in a lower-dimensional latent space (instead of directly in pixel space) to reduce computational complexity and memory (e.g., 512x efficiency gain from 8x spatial and 8x temporal compression).

 ■ Core LDM Components: 1. Compression Network (VAE): ■ Visual Encoder: Maps raw video pixels → compressed latent representation (reduces frame count + resolution).

 ■ Visual Decoder: Reconstructs original video frames from latent space.

 2. Diffusion Model (within LDM): Learns to denoise these lower-dimensional latent representations.

3. Data Preparation (Data Pipeline): ● Data Source: 100 million diverse video-caption pairs. ● Video Preparation: 1. Filter Inappropriate Videos: ■ Remove low-quality/short/slow-motion/distorted videos (e.g., as per Movie Gen).

 ■ Deduplication: Eliminate identical videos (e.g., perceptual hashing) for diverse training.

 ■ Harmful Videos: Use harm-detection models to identify and remove explicit/inappropriate content. CRITICAL for safety requirement.

 2. Standardize Videos: ■ Adjust video length: Split longer videos into 5-second clips. ■ Standardize frame rate: Re-encode to 24 FPS. ■ Adjust video dimensions: Resize/crop to 1280x720 pixels. 3. Precompute Latent Representations: ■ Pass all standardized videos through the pre-trained VAE's Visual Encoder to obtain latent representations.

■ Cache/Store these latent representations: Avoids on-the-fly computation during training, significantly speeding up diffusion training. (Calculation: ~2MB/video, 200TB for 100M videos - manageable).

 ● Caption Preparation: 1. Handle Missing/Non-English Captions: Use video captioning models (e.g., LLaMa3-Video, LLaVA) to automatically generate descriptive captions.

 2. Re-captioning: Improve existing captions (even if present) using pre-trained video captioning models to generate longer, more detailed versions. Improves quality and text alignment (Sora team finding).

 3. Precompute Caption Embeddings: Use a text encoder (e.g., from a pre-trained text-to-image model) to precompute and store embeddings for all captions. Speeds up LDM training (conditioning input).

4. Modeling (Training Pipeline): ● Architecture Choice: DiT (Diffusion Transformer) for videos . 1. Rationale: Based on Sora's success, higher scalability with data/compute due to Transformer nature, flexible for multi-modal adaptation. (Acknowledging U-Net as a viable alternative but choosing DiT).

 2. DiT Components for Video: ■ Patchify: Divides video into 3D fixed-size patches → flatten → linear project to patch embeddings. (Similar to image patchify but 3D).

 ■ Positional Encoding: Assigns spatio-temporal position info to each patch. (e.g., 3D coordinates, or RoPE from OpenSora). Can be learnable or fixed.

 ■ Transformer: Processes sequence of patch embeddings + conditioning signals (text prompt, timestep) to predict noise for each patch.

 ■ Unpatchify: Converts predicted noise vectors back to original video dimensions.

 ● Training Process (Diffusion Model): 1. ML Objective: Minimize reconstruction loss (accurate noise prediction). 2. Loss Function: Mean Squared Error (MSE) / L2 Loss . ■ Formula: $L_{MSE} = ||\text{predicted_noise} - \text{actual_noise}||^2$. ■ Purpose: Guides the DiT model to accurately predict the noise added to the latent representation, enabling high-quality video reconstruction.

 3. Steps per Iteration: ■ Noise Addition: Randomly sample timestep, add noise to precomputed latent video representation.

 ■ Noise Prediction: DiT model predicts noise from noisy latent video + text embedding + timestep.

 ■ Loss Calculation: MSE between predicted and actual noise. ● Challenges & Strategies for Training (Addressing Scale/Data Scarcity): 1. Lack of Large-Scale Video-Text Data: ■ Strategy 1 (Chosen): Train DiT on both image-text and video-text data (treat images as single-frame videos) in a single stage. Leverages hundreds of millions of image-text pairs.

 ■ (Alternative: Pretrain on image data, then finetune on video data - 2 stages).

 2. Computational Cost of High-Resolution Video Generation:

■ LDM Approach: Training in lower-dimensional latent space (already chosen).

 ■ Precompute Video Representations: Cache latent representations to avoid redundant computations (already chosen).

 ■ Spatial Super-Resolution Model: Generate lower-resolution videos with DiT, then use a separate model to upscale to 720p/1080p/4K.

 ■ Temporal Super-Resolution Model: Generate at lower FPS (e.g., 12 FPS), then interpolate frames to achieve 24 FPS.

 ■ Efficient Architectures: Use optimized attention implementations (e.g., FlashAttention ) and Mixture of Experts (MoE) to accelerate training.

 ■ Distributed Training: Tensor parallelism (or other techniques) to parallelize training across 6000 H100 GPUs. Critical for managing memory and compute for large models and data. Strategic: Aligns with your "scaling through TLs/EMs" and "operational excellence" strengths.

5. Evaluation: ● Offline Metrics (Focus on VBench/Movie Gen Bench for comprehensive testing): ○ Frame Quality: Assess individual frames. ■ Metrics: FID (Fréchet Inception Distance), Inception Score (IS). (Average over all frames).

 ■ Limitations: Don't capture temporal consistency. ○ Temporal Consistency: How smoothly content transitions between frames. ■ Metric: FVD (Fréchet Video Distance) . ■ Process: Generate videos → extract features (e.g., using pre-trained I3D model) → calculate mean/covariance of features for generated vs. real videos → compute Fréchet distance.

 ■ Goal: Lower FVD indicates more realistic and temporally consistent videos.

 ○ Video-Text Alignment: How accurately generated video reflects text description. ■ Metric: CLIP Similarity Score . ■ Process: Extract frame-level visual features (CLIP image encoder) and textual features (CLIP text encoder) → compute cosine similarity per frame → aggregate (average/max).

 ■ Goal: High CLIP similarity indicates strong alignment. ○ Human Evaluation: Crucial for subjective assessment. Compare pairs of videos from different models, assess quality, consistency, and alignment.

 ● Online Metrics: ○ Click-Through Rate (CTR): User clicks on generated videos. ○ Time Spent on Page: Engagement with generated video content. ○ User Feedback: Likes, shares, explicit feedback on quality/relevance. ○ Conversion Rate: (If applicable for e.g., ad generation).

6. Overall ML System Design (Inference Pipeline): ● Components: 1. Text Prompt Input: User provides text.

2. Text Encoder: Converts text prompt → text embedding (precomputed/cached). 3. Diffusion Model Inference: ■ Starts with pure noise in latent space. ■ Iteratively denoises using the trained DiT model (conditioned on text embedding and timestep).

 ■ Outputs a fully denoised latent video representation. 4. Visual Decoder: ■ Uses the VAE's Visual Decoder (from the compression network) to convert the latent video representation back into pixel space.

 ■ Outputs a lower-resolution, lower-FPS video. 5. Temporal Super-Resolution (Optional/Future): Interpolates between generated frames for smoother motion.

 6. Spatial Super-Resolution (Optional/Future): Upscales video resolution (e.g., from 720p to 1080p/4K).

 7. Post-processing (CRITICAL for Safety): ■ Applies harm-detection models/filters to generated video frames and overall content.

 ■ Checks for biased terms/visuals , offensive content. ■ If harmful, blocks or modifies the generated video. Strategic: Directly addresses the safety requirement and your expertise.

7. Monitoring: ● System Health: Latency (critical to meet 1-2min target, future faster), throughput, GPU utilization, error rates.

 ● Model Performance (Offline): Continuous monitoring of FVD, CLIP similarity, FID/IS. ● Safety/Bias Monitoring: ○ Track frequency of harmful/biased generations flagged by post-processing. ○ Set up alerts for new types of harmful content. ○ Regular red-teaming exercises to find vulnerabilities in safety guards (as per Anthropic context).

 ● User Feedback: Collect and analyze explicit user feedback on safety and quality of generated videos.

 ● Data Drift: Monitor characteristics of incoming text prompts and potential shifts in generated video content over time.

Other Potential Discussion Points (for senior roles / if time permits): ● Sampling Flexibility: Supporting variable durations, resolutions, aspect ratios. ● Downstream Applications: Inpainting, video-to-video stylization, animating images. ● Control Mechanisms: Desired motion level, camera vs. object motion (e.g., ControlNet for text-to-video).

 ● Efficiency: Progressive distillation, different noise schedulers, noise conditioning augmentation.

 ● Personalization: Fine-tuning model to a particular subject or user. ● Ethical Implications: Broader discussion on responsible AI development for generative video.
