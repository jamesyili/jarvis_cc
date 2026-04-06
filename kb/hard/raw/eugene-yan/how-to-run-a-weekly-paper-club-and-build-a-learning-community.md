# How to Run a Weekly Paper Club (and Build a Learning Community)

**Source:** https://eugeneyan.com//writing/paper-club/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

Over the past 18 months, the [Latent Space Paper Club](https://lu.ma/ls) has had an *unbroken* streak of hosting paper club every single week. That’s at least 80 papers, and likely more, when we consider weeks where we cover related papers (e.g., LoRA + QLoRA). Together, we’ve pre-read and discuss a paper weekly, covering the fundamentals such as:

* Key components: Attention, LayerNorm, FlashAttention, LoRA/QLoRA, ALiBi, RoPE
* Models: Transformer, BERT, T5, GPTs, Codex, LLaMAs, Mistral, CLIP, ViT, RWKV, Jamba, Mamba, Latent Consistency Models, Whisper, Moshi, Molmo, TimeGPT
* Training: InstructGPT, RLHF, RLAIF/CAI, PPO, REST, SPIN, Self-Play, Upcycling
* Inference: Speculative Decoding, Writing in the Margins, Test-time Compute
* Trends: Scaling Laws, Chinchilla, 1-bit, Synthetic Data, Gorilla, Generative Agents
* Practice: RAG, EvalGen, DocETL, LLama Guard, Copilot, Finetuning vs. RAG

> If you’re looking to get started, here’s [a year’s worth of notable papers](https://github.com/eugeneyan/llm-paper-notes).

This has equipped us with the foundation to understand how these techniques and models work, build systems and applications on top of them, and apply them at work and personal projects. But it’s not just about technical knowledge. We’ve also learned from practitioners sharing their insider know-how, built friendships at in-person meetups, and grown a community of learners and builders.

We’d like you to benefit from this too. That’s why we wrote this guide: To help you start your own paper club and learn—together—with your peers.

> Also see the [Swyx/Latent Space version](https://www.latent.space/p/paperclub) that includes (i) advice on paper curation, (ii) video walkthrough of a 3-paper pre-reading + slide prep, (iii) recordings of the Llama 3.1 and Molmo paper club, and more.

How the Latent Space Paper Club got started ~18 months ago

## What happens at paper club (doesn’t just stay at PC)

**Same time, every week.** Every Wednesday, we gather for an hour over lunch (12pm PST) to discuss a pre-selected paper. Sticking to the same time every week makes it easier to remember and attend. Also, a weekly cadence helps with building the habit.

**Pre-reading.** Pre-reading the paper helps you get the most out of the session. I usually pre-read over the weekend, for about an hour. This helps me identify what I don’t understand so I know what to clarify during the session. I’m also better equipped to share insights and help others understand the material. From experience, skipping the pre-read reduces the value I get from the discussion by ~80% or more.

Yes, please pre-read the paper

**Facilitating.** Each week, a volunteer guides the group through the paper, covering the motivation, related literature, methodology, results, etc. This usually takes around 45 minutes, with pauses after each section for quick questions. In the last 15 minutes, we have free-form discussion and discuss the paper’s implications, connect it to other work, and/or consider how to apply the ideas to our work and the broader industry.

Some facilitators prepare simple slides highlighting key charts and takeaways, but this isn’t mandatory. Personally, I’m too lazy to create slides and just screen-share my annotated paper with highlights and notes.

## How to run a paper club (with minimal effort)

**Selecting papers.** The facilitator gets to pick whatever paper they want to discuss, within the overall theme. While our paper club’s focus is language modeling, we occasionally explore key papers from other domains like vision (e.g., CLIP, ViT, LCMs), audio (e.g., Whisper, Moshi), and RL (e.g., DPO, PPO).

TIP: At the *start* of each session, ask for volunteers to facilitate *next* week’s paper. This helps you avoid a last-minute scramble to find a facilitator and paper.

**Scheduling.** We use [Luma](https://lu.ma/ls) for event management but it lacks support for recurring events. We’ve also used Discord events but it’s only visible to folks in the Discord. If you have a better solution, please share!

**Hosting.** We host sessions on a paid Zoom account (thanks Swyx!) We’ve also tried Discord Stages for a bit but had issues with screen sharing and viewing.

**Recordings.** We record the paper facilitation (via Zoom), but not the Q&A. By not recording the Q&A, we hope to encourage folks to share their experience and ghost knowledge (which is sometimes based on what they do on the job). This also incentivizes live attendance and participation in the Q&A which, IMHO, is the main benefit of paper club.

**Community.** Our paper club started as a small group that was committed to studying a key paper each week, and in the process, level up on language modeling together. Over time, we’ve grown into a core group of facilitators and regulars (Swyx, Vibhu, Eugene Cheah, Amgad, Eric, RJ, etc). Including myself, this critical mass lets us rotate amongst ourselves every two months or so, though new volunteers are always welcome!

**Inviting authors.** Occasionally, we invite authors to share their work and have had the pleasure of hosting [Llama](https://arxiv.org/abs/2407.21783), [Matryoshka Embeddings](https://arxiv.org/abs/2205.13147), [Writing in the Margins](https://arxiv.org/abs/2408.14906), [TimeGPT](https://arxiv.org/abs/2310.03589), etc. We’ve also invited [Shreya](https://x.com/sh_reya) and [Nathan](https://x.com/natolambert) to join us while we discuss their papers. Having the authors join paper club allows us to clarify our questions with them directly, and lets the authors share behind-the-scenes insights. For example, we learned from Nathan why [Molmo](https://molmo.allenai.org/blog) has such a heavy emphasis on analog clocks.

## How to read a paper (in an hour)

**Reading papers.** If you find reading academic papers challenging, [you’re not alone](https://www.science.org/content/article/how-read-scientific-paper-rev2). The [three-pass approach](https://dslsrv1.rnet.missouri.edu/resources/HowToReadAPaper.pdf) ([video](https://www.youtube.com/watch?v=SKxm2HF_-k0)) has served me well:

* First, skim to get a general idea of the paper (~10 minutes)
* Then, read to understand key points but not the details (~1 hour)
* Finally, understand the paper in-depth and take notes (3 - 6 hours)

Most of the time, unless you’re trying to replicate the paper, two passes will suffice. Nonetheless, for paper club, I tend to go into the details on methodology and results. Here’s my [walkthrough of applying the three-pass approach](https://eugeneyan.com/writing/why-read-papers/#how-to-read-papers).

**Tools.** [Zotero](https://www.zotero.org) makes it convenient to save papers to your library. It also has built-in markup tools to highlight and annotate papers. And if you come across unfamiliar terms or inscrutable math equations, take a screenshot and ask Claude to explain!

## How to facilitate a paper (even if it’s your first time)

**Topics.** When guiding the group through the paper, focus on these key aspects.

* Motivation: Why is the paper important? What problem does it address?
* Methodology: How did the paper address the problem?
* Results: What are the key findings and achievements?
* Ablations (if present): What worked, what didn’t, and why?
* Related work: How does it improve on previous work?

**Format.** Most facilitators simply walk through the PDF with their highlights and notes. Others create simple slides, including key graphs and tables to focus attention. There’s no hard and fast rule—just do what suits you best as facilitator.

• • •

Participating in a weekly paper club means covering ~50 papers a year. With just two hours per week—one hour of pre-reading and one hour of discussion—you’ll spend only ~100 hours (4 days) a year. Yet, this minimal effort likely places you in the top 5% of AI engineers and the top 0.1% of the world population in terms of AI knowledge.

So, what are you waiting for? Start your own paper club, or see you at [Latent Space](https://lu.ma/ls)!

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Nov 2024). How to Run a Weekly Paper Club (and Build a Learning Community). eugeneyan.com.
> https://eugeneyan.com/writing/paper-club/.

or

```
@article{yan2024paperclub,
  title   = {How to Run a Weekly Paper Club (and Build a Learning Community)},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2024},
  month   = {Nov},
  url     = {https://eugeneyan.com/writing/paper-club/}
}
```

  
Share on:
