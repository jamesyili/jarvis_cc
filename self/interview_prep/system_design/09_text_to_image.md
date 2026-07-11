# [Design] Text to Image

*Source: `interview_prep/system_design_prep.pdf`, pages 55–58. James's prep notebook — extracted text, lightly cleaned.*

---

[Design] Text to Image
Okay, James, let's convert this comprehensive "Text-to-Image Generation" system design into your preferred "Notes format." This is an incredibly relevant topic, especially for a Pinterest-like platform and a company like Anthropic, given its focus on generative AI and safety. I'll maintain your style, highlight key technical choices, and emphasize the safety and fairness aspects you raised.

1. Clarify Requirements: ● Primary Goal: Generate high-resolution, detailed images from text prompts. ● Input/Output: Text prompt → 1024x1024 pixel image. ● Text Prompt: Max 128 words, handle detailed and complex prompts. ● Language: English only (initially), but adaptable architecture for multi-language future. ● Dataset: ≈ 500 million image-caption pairs (from user assets, mostly captioned). Some captions noisy/non-English.

 ● Generation Speed: Near real-time, aim for ≤ 10 seconds per image. ● Image Diversity: Generate wide range of images (realistic, portraits, abstract, conceptual).

 ● Safety/Fairness: Crucial to ensure fairness (avoid bias by age, race, gender) and prevent generation of offensive, inappropriate, or harmful images (filters/checks needed).

2. Frame as ML Task: ● ML Objective: Generate visually detailed images that accurately adhere to the text prompt.

 ● System Input: Text prompt. ● System Output: Generated image (1024x1024 pixels). ● ML Category: Multi-modal Generative AI (Text-to-Image). ○ Approach Chosen: Diffusion Models . ■ Rationale: Prioritizes exceptional image quality and realism, offers flexibility in trading off sampling speed vs. quality. (Acknowledges Autoregressive models as alternative but highlights their complexity/statistical inefficiency for this task).

 ■ Mechanism: Iterative refinement process: starts with random noise and gradually transforms it into a clear image, guided by a text encoder.

3. Data Preparation (Data Pipeline): ● Data Source: 500 million image-caption pairs. ● Image Preparation: 1. Filtering Inappropriate Images: ■ Remove small images (< 64x64 pixels - often poor quality). ■ Deduplicate images: Remove identical or perceptually similar images (e.g., perceptual hashing). Prevents bias from redundant data.

 ■ Remove Inappropriate Images: Employ harm detection / NSFW detection models to filter out violence, nudity, etc. CRITICAL for safety requirement.

■ Remove Low-Aesthetic Images: Use specialized ML models to filter images that aren't aesthetically pleasing.

 2. Standardizing Images: ■ Adjust Image Dimensions: Resize (smaller dim matches target, e.g., 128) then center-crop to fixed input size (e.g., 128x128).

 ■ Normalize Images: Scale pixel values (e.g., [0,1] or [-1,1]). ● Caption Preparation: 1. Handle Missing/Non-English Captions: Use an image captioning model (e.g., BLIP-3) to auto-generate descriptive English captions.

 2. Enhance Captions: Use pre-trained CLIP to score image-caption relevance. If score below threshold, replace original with auto-generated caption (from BLIP-3).

 3. Remove Poorly Matched Pairs: After enhancement, remove pairs with low CLIP similarity scores. Ensures high-quality text-image alignment for training.

 4. Precompute Caption Embeddings: Use a pre-trained text encoder (e.g., T5) to pre-compute and cache caption embeddings. Reduces training computation (conditioning input).

 ● Continuous Data Flow: Collect and process newly generated data (user prompts, generated images, user feedback) to add to training set for continuous improvement.

4. Modeling (Training Pipeline): ● Architecture (for Noise Prediction): U-Net (chosen for educational purposes in context, but note DiT is also strong and often preferred in recent state-of-the-art like Sora).

 1. U-Net Components: ■ Downsampling Blocks: Convolution, Batch Norm, Activation, Max-pooling.

 ■ Cross-Attention: Crucial layer here. Queries from image features, Keys/Values from text embeddings (from text encoder). Integrates text prompt influence.

 ■ Upsampling Blocks: Transposed Convolution, Batch Norm, Activation. ■ Cross-Attention: Continues text influence during upsampling. ■ Skip Connections: (Implicit in U-Net) Pass high-res features from downsampling to upsampling path for detail preservation.

 ● Diffusion Training Process: 1. ML Objective: Minimize the difference between true noise (ϵ) and predicted noise
(ϵθ ).

 2. Loss Function: Mean Squared Error (MSE) / L2 Loss . ■ Formula: L=Et,x0 , ϵ ( ∣∣ ϵ−ϵθ ( xt ,t) ∣∣ 2) ■ Purpose: Guides model to accurately predict noise at each step of the reverse diffusion process.

 3. Steps: ■ Noise Addition: Randomly sample timestep t, apply noise directly to original image x0 to get noisy image xt using noise schedule
(xt = αˉ t
 x0 +1− αˉ t ϵ).

■ Conditioning Signals: Prepare image caption embedding and sampled timestep t for model input.

 ■ Noise Prediction: U-Net/DiT model predicts noise ϵθ given xt , t, and caption embedding.

 ■ Loss Calculation: MSE between predicted noise and actual noise. ● Challenges & Strategies for Training: 1. Resource-Intensive Training: (Mitigation strategies due to billions of parameters, high-res images, large data)
 ■ Mixed Precision Training: Use 16-bit and 32-bit floats to reduce memory/increase efficiency.

 ■ Model and Data Parallelism: Distribute training across 6000+ H100 GPUs using frameworks like FSDP/Deepspeed. CRITICAL for scale.

 ■ Latent Diffusion Models (LDM): Operate in lower-dimensional latent space (already chosen as primary approach).

 2. Slow Image Generation (during inference, but design impacts training): ■ Parallel Sampling: Parallelize generation across multiple devices. ■ Model Distillation: Train a smaller "student" model to mimic a larger "teacher" model for faster inference.

 ■ Model Quantization: Reduce precision of weights (e.g., 8-bit) for smaller size, faster generation.

 ■ Optimized Algorithms: Use faster sampling algorithms (e.g., DDIM) to reduce required diffusion steps.

5. Evaluation (Evaluation Pipeline): ● Offline Metrics: ○ Benchmark: DrawBench (curated prompts for object composition, interaction, context).

 ○ Key Areas: ■ Image Quality: ■ Metrics: Inception Score (IS), FID (Fréchet Inception Distance). (Common for assessing realism/diversity).

 ■ Image Diversity: (Measured by FID, also qualitatively). ■ Image-Text Alignment: ■ Metric: CLIPScore . ■ Process: Cosine similarity between CLIP embeddings of generated image and text prompt.

 ■ Purpose: Quantifies how well generated image matches the text description. Higher score = better alignment.

 ○ Human Evaluation: Complement automated metrics. ■ Image Quality: Raters compare generated vs. reference image for photorealism.

 ■ Text Alignment: Raters score "Does caption accurately describe image?" (Yes/Somewhat/No).

 ● Online Metrics: (Measure real-world performance & user satisfaction) ○ Click-Through Rate (CTR): Clicks on generated images. ○ Time Spent on Page: User engagement. ○ User Feedback: Direct feedback on quality/alignment.

○ Conversion Rate: Desired user action after interaction. ○ Latency: Actual generation time in production (≤ 10s goal). ○ Throughput: Images generated per second. ○ Resource Utilization: CPU, GPU, memory usage for cost optimization. ○ Average Cost per User per Month: Track cost-effectiveness, especially with repeated generations from unhappy users.

6. Overall ML System Design (Inference Pipeline): ● Components: 1. Prompt Auto-Complete Service: Suggests phrases as user types, improves UX.

 2. Prompt Safety Service: ■ CRITICAL for Safety. ■ Uses a text classification model to process user prompts. ■ Rejects prompts violating usage policies (violence, hate, nudity, etc.). 3. Prompt Enhancement: ■ Refines user prompts for clarity, coherence, detail. ■ Helps diffusion model produce better outputs. 4. Image Generation (Core): ■ Encodes enhanced text prompt (e.g., with T5 text encoder). ■ Passes tokens to the Diffusion Model to generate one or multiple images.

 5. Harm Detection: ■ CRITICAL for Safety (Defense-in-Depth). ■ Applies image classification models to generated images. ■ Flags/blocks inappropriate images (violence, nudity, bias) before display, even if previous prompt safety checks were passed.

 6. Super-Resolution Service: ■ Increases resolution of generated images (e.g., from 64x64 base to 1024x1024).

 ■ Often a cascade of multiple SR models.

7. Monitoring: ● System Health: Latency, throughput, resource utilization for all services. ● Model Performance (Offline): Continuous monitoring of CLIPScore, FID, IS on test sets.

 ● Safety/Bias Monitoring: ○ Quantify Bias: Track generations related to age, race, gender (e.g., if a prompt for 'engineer' consistently generates images of one race/gender).

 ○ Log prompts rejected by Prompt Safety Service. ○ Log images flagged/blocked by Harm Detection. ○ Regular red-teaming for new bypasses or unintended harmful generations. ● User Feedback: Analyze explicit feedback on safety and quality. ● Cost Management: Monitor average cost per user/generation.
