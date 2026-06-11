# Transformers (training & recsys) Resources

High-trust sources only. Knowledge for lessons is drawn from here, not parametric guesses.

## Knowledge

- **[Nathan Lambert — _The RLHF Book_](https://rlhfbook.com)** _(James already has the PDF — confirm edition)_
  Post-training / alignment: SFT, preference data, reward modeling, PPO, DPO. **Use for:** Phase-1 **Stream B** (post-training → RLHF), and the recsys/Reflex crossover (engagement-as-preference, RL for ranking).
- **[Sebastian Raschka — _Build a Large Language Model (From Scratch)_ (Manning, 2024)](https://www.manning.com/books/build-a-large-language-model-from-scratch)** · code: [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) — **PHASE 2 (at computer); not needed for Phase 1**
  **The spine for the train-from-scratch track.** Ch1 intro · Ch2 text data (BPE, data loaders, embeddings) · Ch3 attention · Ch4 GPT model · **Ch5 pretraining on unlabeled data (THE training-loop chapter)** · Ch6 finetune-for-classification · Ch7 instruction finetuning · App.A PyTorch · **App.D training-loop bells & whistles (warmup, cosine decay, grad clip)** · **App.E LoRA (parameter-efficient finetuning)**. **Use for:** Ch5 = Lessons 01–03 ground truth; App.D = L03; Ch2 = L02 (data); Ch6/7 + App.E = the finetuning + LoRA bridge into CFM scaling. **Skip/skim Ch3–4** (forward architecture James already knows — LR-0001). **Gap:** zero recsys content — the recsys translation is what this workspace's lessons add.
- [Andrej Karpathy — "Let's build GPT: from scratch, in code, spelled out" (video, 1h56m)](https://www.youtube.com/watch?v=kCc8FmEb1nY)
  Builds + trains a decoder-only transformer following *Attention Is All You Need*, ending at the core of nanoGPT. **Use for:** the canonical from-scratch training walkthrough; the training loop; self-attention in code.
- [karpathy/nanoGPT (repo)](https://github.com/karpathy/nanoGPT)
  ~300-line `train.py` (training loop) + ~300-line `model.py` (GPT). Reproduces GPT-2 (124M). **Use for:** the reference training loop, config, checkpointing, the exact optimizer/LR setup.
- [karpathy/build-nanogpt (repo)](https://github.com/karpathy/build-nanogpt)
  Step-by-step git history reproducing GPT-2 from an empty file. **Use for:** seeing the model + training built incrementally.
- [Andrej Karpathy — "A Recipe for Training Neural Networks" (blog, 2019)](http://karpathy.github.io/2019/04/25/recipe/)
  The definitive debugging-and-process playbook (overfit-one-batch, loss sanity checks, fix-one-thing-at-a-time). **Use for:** the entire debugging track.
- [The Annotated Transformer — Harvard NLP](https://nlp.seas.harvard.edu/annotated-transformer/)
  Line-by-line PyTorch implementation of the original paper with prose. **Use for:** encoder-decoder details, label smoothing, the original LR schedule (warmup).
- [Vaswani et al. — "Attention Is All You Need" (2017)](https://arxiv.org/abs/1706.03762)
  The primary source. **Use for:** the canonical architecture, the LR schedule, the complexity/path-length table.
- [Dive into Deep Learning (d2l.ai) — Attention & Transformers chapters](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)
  Free textbook with runnable code + math. **Use for:** rigorous derivations, alternative explanations, exercises.
- [3Blue1Brown — Neural Networks / Transformers series](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
  Visual intuition for attention and backprop. **Use for:** geometric intuition when a mechanism isn't clicking.

### Recsys-specific (already in James's world)
- `artifacts/transformers-for-recsys.html` — his own consolidated doc (fundamentals → recsys → TransAct v1/v2 → UPP FM/CFM/scaling).
- SASRec (Kang & McAuley 2018), BERT4Rec (Sun et al. 2019), TransAct (KDD 2023), TransAct V2 (CIKM 2025) — primary recsys-transformer sources; cited in the HTML.

## Wisdom (Communities)

- [r/MachineLearning](https://reddit.com/r/MachineLearning)
  High-signal, research-leaning. **Use for:** sanity-checking design intuitions, training-failure troubleshooting.
- [EleutherAI Discord](https://www.eleuther.ai/community)
  Practitioners who train LLMs at scale. **Use for:** real-world training/scaling questions.
- _Note:_ community participation not yet confirmed as a preference — propose, don't push. (Update here if James opts out.)

## Gaps
- No single canonical "training a *ranking* transformer from scratch" walkthrough as clean as nanoGPT — recsys training is fragmented across papers + internal docs. The recsys lessons will bridge nanoGPT's loop to the ranking setting (BCE + sampled softmax + future-action loss) using James's own CFM/TransAct notes as the ground truth.
