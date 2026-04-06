# Huggingface

**Source:** https://aman.ai/h/huggingface/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Her background](#her-background)
* [Huggingface](#huggingface)
* [My background](#my-background)

## Overview

* Chat with Nazneen talking points:

## Her background

* Following your research, most recently Zephyr (Zeh-furr) with the introduction of distilled DPO to align the model with human preference. Mistral -> parent model that was distilled
* And I believe it was also integrated with the custom search engine You.com as well
* I’ve read your NYT article, serving on the UN’s AI Advisory Body, big impact in the field both in terms of research and otherwise.
* It was great meeting you at the GenAI event with the LLama 2 release at Meta HQ

## Huggingface

* Open-Source AI Models and Libraries and we leverage these actively for our ongoing research
* Innovation in AI Research: Zeh-furr, DistilBERT, BLOOM (GPT-3 alternative decoder model)
* Leaderboards: Massive Text Embedding Benchmark (MTEB) for RAG, Open LLM Leaderboard - particularly useful since the plethora of LLMs being released
* Other researchers: Nathan Lambert
* I’ve also heard great things about the culture, very bottom up and open and I really believe in their mission to democratize good machine learning and make it accessible. It’s really important to have ideas flow

## My background

* Team lead at Amazon Music, Recommender Systems and are starting to also dive into NLP here with Amazon Bedrock.
* Collaboration with Alexa, which is the most common usecase for Amazon music, users start by saying “Alexa play music, or Alexa play taylor swifts latest song”.
* Understanding that intent, and also gaining signal from paralingusitic signals from Alexa via speech, aka the user sounds sad, there seems to be a party.
* I’m a research fellow at U of South Carolina and IIT Patna in India.
* Publication in EMNLP -> AI generated text detection
* Current topics I’m working on: surveys in
  + Hallucination mitigation: retrieval based RAG, self-refinement through reasoning like Chain of thought reasoning, prompt tuning, knowledge graphs,
  + Context length extenstion: AliBi, Rope, long lora, longqlora, yarn (yet another rope extension),
* Multimodal Classification of adverse drug reaction: unique issue of not having sufficient image data so we’re looking into modality dropout techniques there.
* Causal reasoning in large vision models:
  + LVLMs are great in processing and integrating vast amounts of visual and textual data, their actual understanding and reasoning abilities are under question. These models tend to rely heavily on statistical correlations learned from extensive training data, often leading to biased or superficial interpretations. For instance, if an LVLM is frequently exposed to images of white dogs paired with the question ‘What color is the dog?’, it may start correlating the question with the answer ‘white’ regardless of the actual color of the dog in a new image. This creates a significant gap in the model’s ability to generalize and accurately interpret novel situations
