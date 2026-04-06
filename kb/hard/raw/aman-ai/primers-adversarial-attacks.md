# Primers • Adversarial Attacks

**Source:** https://aman.ai/primers/ai/attacks/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Related Papers](#related-papers)
  + [Universal and Transferable Adversarial Attacks on Aligned Language Models](#universal-and-transferable-adversarial-attacks-on-aligned-language-models)
* [Citation](#citation)

## Overview

## Related Papers

### [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043)

* Because “out-of-the-box” large language models are capable of generating a great deal of objectionable content, recent work has focused on aligning these models in an attempt to prevent undesirable generation. While there has been some success at circumventing these measures – so-called “jailbreaks” against LLMs – these attacks have required significant human ingenuity and are brittle in practice.
* This paper by Zou et al. from CMU, Center for AI Safety, and Bosch Center for AI shows that all major LLMs (OpenAI’s ChatGPT, Google’s Bard, Meta’s Llama 2, Anthropic’s Claude) can be made to do harmful activities using adversarial prompts, despite having rigorous safety filters around them. They propose a simple and effective attack method that causes aligned language models to generate objectionable behaviors.
* Specifically, their approach finds a suffix that, when attached to a wide range of queries for an LLM to produce objectionable content, aims to maximize the probability that the model produces an affirmative response (rather than refusing to answer). However, instead of relying on manual engineering, their approach automatically produces these adversarial suffixes by a combination of greedy and gradient-based search techniques, and also improves over past automatic prompt generation methods.
* Adversarial suffixes confuse the model and circumvent the safety filters. Interestingly, these adversarial prompts were found using open source LLMs and shown to transfer to even closed source, black-box LLMs.
* Specifically, we train an adversarial attack suffix on multiple prompts (i.e., queries asking for many different types of objectionable content), as well as multiple models (in their case, Vicuna-7B and 13B). When doing so, the resulting attack suffix is able to induce objectionable content in the public interfaces to ChatGPT, Bard, and Claude, as well as open source LLMs such as LLaMA-2-Chat, Pythia, Falcon, and others.
* The following figure from the paper illustrates the fact that aligned LLMs are not adversarially aligned. Their attack constructs a single adversarial prompt that consistently circumvents the alignment of state-of-the-art commercial models including ChatGPT, Claude, Bard, and Llama-2 without having direct access to them. The examples shown here are all actual outputs of these systems. The adversarial prompt can elicit arbitrary harmful behaviors from these models with high probability, demonstrating potentials for misuse. To achieve this, their attack (Greedy Coordinate Gradient) finds such universal and transferable prompts by optimizing against multiple smaller open-source LLMs for multiple harmful behaviors.

* The following figure from the paper shows screenshots of harmful content generation: ChatGPT (top left), Claude 2 (top right), Bard (bottom left), LLaMA-2 (bottom right).

* In total, this work significantly advances the state-of-the-art in adversarial attacks against aligned language models, raising important questions about how such systems can be prevented from producing objectionable information.
* [Project page](https://llm-attacks.org/); [Accelerated Coordinate Gradient (ACG) by Haize Labs](https://blog.haizelabs.com/posts/acg/)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledAdversarialAttacks,
  title   = {Adversarial Attacks},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
