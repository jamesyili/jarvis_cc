# AI Engineer 2023 Keynote - Building Blocks for LLM Systems

**Source:** https://eugeneyan.com//speaking/ai-eng-summit/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

I was invited to give a [talk at the inaugural AI Engineer Summit](https://www.ai.engineer/summit/schedule/building-blocks-for-llm-systems-and-products) in San Francisco. It’s largely a combination of my recent writing on [design patterns for LLM systems](/writing/llm-patterns/) and [evals for abstractive summarization](/writing/abstractive/), albeit heavily truncated (each speaker only had 18 minutes!). Here are the slides and talking points for my talk.

You may also be interested in the slides that [didn’t make the final cut](#cutting-room-floor).

• • •

Thank you for the warm welcome! I’m Eugene Yan, and today, I would like to talk to you about building blocks for LLM systems and products.

Like many of you, I’m trying to figuring out how to effectively use LLMs… in production.

So, a few months ago, to clarify my thinking, I wrote about some [patterns for building LLM systems and products](/writing/llm-patterns/). And the community seemed to like it. There’s Jason asking for this to be a seminar—so here you go Jason.

(Note: Jason’s talk was right before mine.)

Today, I’m going to focus on four of these patterns: Evaluations, Retrieval-Augmented Generation, Guardrails, and Collecting Feedback. I might not have time for collecting feedback, but we’ll see how it goes.

Okay, let’s start with evals, or what I consider the foundation.

Why do we need evals?

Well, evals help us understand if our prompt engineering, retrieval augmentation, or finetuning is on the right track. Consider it eval-driven development, where your evals guide how you build your system and product.

We can also think of evals as the test cases, where we run these tests before deploying updates to users.

And finally, if managers at OpenAI take the time to write evals or give feedback on them, you know that evals are pretty important.

But building evals is hard. Here are some things I’ve seen folks trip on.

First, we don’t have a consistent approach to evaluating LLMs.

If we look at more conventional machine learning: For regression we have mean squared error, for classification we have precision & recall, and for ranking we have NDCG. These metrics are fairly straightforward and there’s typically one main way to compute them.

What about for LLMs? Well, we have benchmarks where given a prompt and multiple choice options, we evaluate the model’s ability to get it right. MMLU is an example that’s widely used, where it assess LLMs on knowledge and reasoning on college level tasks such as math, computer science, and US history.

But there’s no consistent way to run MMLU. As Arvind and Sayash recently noted, [evaluating LLMs is a minefield](https://www.cs.princeton.edu/~arvindn/talks/evaluating_llms_minefield). They rightly pointed out that it’s unclear if we’re evaluating the LLM or if we’re evaluating the prompts evaluating the LLM.

On that very same day, [Anthropic noted the same thing](https://www.anthropic.com/index/evaluating-ai-systems). They noted out that the simple multiple choice question may not be as simple as it seems.

For example, simple formatting changes—such as using different parentheses—can lead to significant changes in accuracy. Also, the lack of consistency across implementations makes it hard to compare models based on these academic benchmarks.

Speaking of academic benchmarks, we may have already outgrown some of them. For example, let’s consider the task of summarization.

On the top, we see the human evaluation scores on the [reference summaries for the CNN/Daily Mail dataset](https://arxiv.org/abs/2007.12626). And on the bottom, we see the scores for the automated summaries geverated by various models. You don’t have to compare all the numbers, but the point is that the gold references score poorer than the automated summaries.

We see the [same thing on the XSUM dataset](https://arxiv.org/abs/2301.13848), which stands for extreme summarization. Here, the reference summaries have lower human evaluation scores than InstructGPT.

And finally, with these benchmarks being so easily available, we sometimes forget to ask ourselves if they’re a fit for our task. If we think about it, does MMLU really apply to the tasks we care about? Maybe, if we’re building a bot to answer college level example questions. But most of us are not doing that. Here’s Linus reminding us that we should measure on our specific tasks and not just rely on academic evals.

(Note: Linus’ talk was right after mine.)

As an industry, we’re still figuring out how to do evals effectively. Nonetheless, I think there are some tenets emerging.

First, we should build evals for our specific task. And it’s okay to start small. How small? Well, Teknium, who finetunes and releases a lot of open models, handcrafts an eval set of 40 questions for his domain expert task. 40 evals, that’s all it takes, and it can go very far.

Second, try to simplify the task and eval as much as possible. Although LLMs are flexible, I think we’ll have better success with evals if we try to make our task more narrow.

For example, if our task is content moderation, we can compute precision and recall on its ability to detect toxicity or bias. Or if it’s slightly broader, such as writing SQL, we can try to run the SQL to see if it executes and returns the expected result. Or if we’re extracting JSON, we can check if the extracted JSON keys and values match what we expect. Fortunately, these are fairly straightforward to evaluate because we have expected answers.

But, if our task is open-ended—such as dialogue—we may have to rely on a strong LLM to evaluate the output. Nonetheless, this can be expensive, even for a small set of 60 samples.

Finally, even if you have automated evals, don’t discount the value of eyeballing the output. Here’s [Jonathan from Mosaic](https://www.latent.space/p/mosaic-mpt-7b): “I don’t really believe that any of these eval metrics capture what we care about”. Instead, they had was a prompt to suggest games for a 3-year old and a 7-year old and they found it more valuable to see how the output changed over time.

Next, let’s get into retrieval augmented generation, or what I consider the data.

I don’t think I need to convince this audience here on the need for RAG, but very briefly, RAG is helpful as it lets us add relevant and up-to-date knowledge into our model as input context. This way, we don’t have to rely solely on the model’s knowledge.

It’s also more practical, being cheaper than continuous finetuning to add knowledge.

But, retrieving the right documents is hard. Nonetheless, since we already have great speakers, Jerry and Anton, sharing about this topic tomorrow, so I won’t go into the challenges of retrieval here. Instead, I would like to focus on the LLM side of things, and discuss some challenges that *remain* even if we have retrieval augmented generation.

The first of which is that LLMs can’t really see the all the documents that we retrieve.

Here’s an experiment from a [recent paper](https://arxiv.org/abs/2307.03172). The task is retrieval-augmented question & answer. The questions were based on historical queries on Google Search while the answers were human-annotated answers from Wikipedia.

As part of the context, they provided 20 documents that were at most 100 tokens long. So the context is max 2,000 tokens. One of these tokens contained the answer, and the rest were distractors that were relevant, but don’t contain the answer.

The question they had was: How would the position of the document containing the answer affect question-answering accuracy?

Here’s what they found.

If the answer is in the first retrieved document, accuracy was the highest.

When the answer is in the last document, accuracy is decent.

But when the answer is in the middle, accuracy plunges, to the extent that it’s even worse than without having retrieval augmentation.

The key takeaway here is this: We shouldn’t neglect retrieval just because context window sizes are increasing. Getting the most relevant documents to rank highly, in the top 1 - 3 positions, still matters.

Also, even if the answer is in the context, and in the top position, accuracy is only 75%. Thus, even with perfect retrieval, we can still expect some errors.

Another gotcha is that LLMs can’t really tell if the retrieved documents are irrelevant.

Here’s an [example I tried with GPT-4](https://chat.openai.com/share/b59cfd3d-ad6c-4a85-bb64-d41ff365b9a5): I gave it a list of the top 20 sci-fi movies, and we can think of these as movies I’ve watched. Then, I asked it if I would like Twilight. For folks not familiar with Twilight, it’s a romantic fantasy between a girl and a vampire, and some werewolves as well. I think that’s about right, because I’ve not watched it myself.

I also have this instruction where, if it thinks I won’t like Twilight, it should respond with “Not Applicable”. In recommender systems, it’s important for us to do this so we don’t make bad recommendations.

How do you think it responded?

So here’s what happened. First, it notes that Twilight is a different genre and not quite sci-fi, which is great!

But then, it suggests ET because of inter-species relationships, and I’m not quite sure how I feel about that. <audience laughs>

(Note: This was not intended to be funny and was thus a pleasant surprise 😊)

I mean, how would you feel if you got this as a movie recommendation? The point is, these LLMs are so finetuned to be helpful that they try their best to give an answer. Sometimes, it’s hard for them to decide on queries that are in the fuzzy area of relevant vs. not relevant.

So how do we best address these limitations with RAG?

First, I think there are a lot of good ideas in the field of information retrieval. Search and recommendations have been focused on showing the most relevant documents and items for decades. I think that the humble BM25, together with boosting queries, can go a long way. Also, there’s a lot that we can learn about ranking and filtering items from the field of recommender systems. Also, retrieval evaluation metrics.

I think it also helps to use a threshold to exclude irrelevant documents. In the Twilight and sci-fi movie example, I bet we could do something simple like checking item embedding distance between them and only if they’re close enough do we move to the next step.

Next in the list, we have guardrails, the mediator between our backend systems and the frontend UX.

A key concern is to make sure what we deploy is safe. What do we mean by safe? Well, we can look at OpenAI’s moderation API to look at what they compute. There’s hate, harassment, self-harm, violence, all that good stuff.

Another thing we also want to guardrail against is that of factual inconsistency, also known as hallucinations. Returning non-factual content, such as inaccuracy summaries, can lead to trustbusting experiences.

Fortunately or unfortunately, the field of summarization has been trying to address this for a very long time, so we can take a leaf from their playbook.

One approach to assessing factual inconsistency is via the natural language inference task.

The task of NLI is where, given a premise and a hypothesis, we classify if the hypothesis is true or false. For example, given the premise “John likes all fruits”, the hypothesis that “John likes apples” is true and thus entailment.

And because there’s not enough info to confirm that “John eats apples daily”, it’s neutral.

And finally, the hypothesis that “John dislikes apples” is clearly false because of the premise, and is thus a contradiction.

Do you see how we can apply this to the task of summarization? In summarization, the document is the premise and the summary is the hypothesis.

And when doing this, it helps to apply it at the sentence-level instead of the entire document. In this [example](https://arxiv.org/abs/2111.09525) here, the last sentence in the summary is incorrect. If we run the NLI task with the entire document and summary, it classifies the entire summary as correct. But, if we run it at the sentence-level, an NLI model correctly identifies that the last sentence in the summary is incorrect.

They also included a helpful ablation study, where they varied the granularity of the document: As the granularity got finer and finer, from document to paragraph to sentence, the accuracy of detecting factual inconsistency increases.

Another simple approach is that of sampling.

Here’s an example from [SelfCheckGPT](https://arxiv.org/abs/2303.08896). Given an input document, we generate the summary multiple times. Then, we check if those generated summaries are similar to each other, such as via n-gram overlap, or embedding similarity.

The assumption is that, if the summaries are wildly different, it’s because they’re not grounded on the context document and are thus hallucinations.

But, if the summaries are similar, then we can assume that they are grounded effectively and thus likely to be factually consistent with the context document.

A final approach is asking a strong LLM.

In this [paper](https://arxiv.org/abs/2303.16634), given an input document and summary, they get the LLM to return a summary score. However, the LLM has to be pretty strong and they used GPT-4 to do this. As we saw earlier, GPT-4 can be pretty pricey. For the specific use case of detecting factual inconsistency, I’ve seen similar methods outperform using an LLM and thus would suggest starting with simple instead.

Okay, to close the loop, let’s touch briefly on collecting feedback.

Why is collecting feedback important? First, it helps us understand what users like and don’t like. This is important in helping us figure out what features to double down on and what to pivot from.

Also, collecting user feedback helps with building our evaluation and finetuning dataset. New models are released every day, but evals and finetuning data is one of the few assets that can transfer across models and techniques.

But collecting feedback from users is not as straightforward as it seems. Explicit feedback, which is feedback we ask from users, can be sparse. Here’s a quick thought experiment.

For folks that use ChatGPT, how often do you click on this button to get feedback?

<About a dozen audience members, out of 500, raise their hands>

Now, you folks are the beta testers that product developers dream of. <audience laughs>

The point here is, even if we include these feedback buttons, we may not actually receive the voluminous feedback we expect.

Now, if the issue with explicit feedback is sparsity, the problem with implicit feedback is that it can be noisy. Implicit feedback is data that we organically get as people use our product, without our product asking users for feedback.

Here’s that same example: How often do you click on the copy code button?

<30-50 people raise their hands>

But, does clicking on the copy-code button mean that the code is incorrect?

(Note: At this time, the answer was not revealed.)

No. In this example, `nrows` is not a valid argument for `pandas.read_parquet`. But, if we were to consider all code snippets that were copied as positive feedback, we might have a lot of bad data in our training set.

So, how do we collect feedback? One good example is GitHub Copilot. For people not familiar with it, you type your function signature or some comments and it suggests some code. Then, given the code suggestion, we can either accept the suggestion, go to the next suggestion, or reject or ignore it. We can also accept the code and make small edits.

We do this dozens of times a day, so we can only imagine how much valuable *implicit* feedback these coding assistants get daily.

Another good example is Midjourney. For folks that don’t use Midjourney, here’s how it works: You type a prompt and it generates four images. Then, based on the images, you can either ask to rerun the prompt, choose to vary one of the images slightly—that’s what the V stands for. Or, you can choose to upscale one of the images—that’s what the U stands for.

But you know what an AI engineer sees?

Rerunning the prompt is negative feedback, because the user is saying that they don’t like any of the images generated.

Varying one of the images is small positive feedback, where the user is saying, hey, that image has potential.

Finally, choosing to upscale the image is a large positive reward, where the user likes it and wants to use that image.

Okay, that’s all I wanted to share. If you remember anything from this talk, I hope it’s these three things.

First, you need evals for your task. Just annotate 30 or 100 example for your task and try to automate evaluations on it. This will help you iterate faster on your prompt engineering, retrieval augmentation, finetuning, and so on. It’ll also help you deploy faster. Eyeballing doesn’t scale—it’s good as a final vibe check, but it doesn’t scale.

Next, reuse your existing systems as much as you can—there’s no need to reinvent the wheel. BM25 and metadata matching can get you pretty far, and so do the basic techniques from recommender systems. After all, these information retrieval techniques are optimized to rank the most relevant items on top.

Finally, UX plays a large rule in LLM products. I think a big chunk of the success with GitHub Copilot and ChatGPT is the UX—it allowed users to interact with them where they needed it, in the IDE or a chat window, instead of having to call an API. Having the right UX also makes it easier to collect useful feedback.

Alright that’s all I had. Thank you, and keep on building.

## Cutting room floor

Here are some slides that didn’t make it into the final presentation, mostly due to the strict 18 minute limit (they threatened to play the Oscars music at the 18 minute mark lol).

This was originally slide 2 and how I wanted to introduce myself as selling books at a book store, focusing on recommender systems and search. But I tried introducing myself this way to a few folks at the conference and a majority didn’t get it. Thus, I dropped it to save 20 seconds. I guess it’s more of an inside joke than anything.

This was originally slide 3, where I would say something like “At the bookstore, I primarily focus on recommender systems and search. But increasingly, like many of you, I’m trying to figure out how to make use of this new power source, connective tissue, and operating system.” But it felt too longwinded and I dropped it to save 30 seconds. Too bad, I really liked the analogy and alien lego image.

(Interestingly, OpenAI referred to LLMs as connective tissue for multi-modality too.)

On the point of not having a good way to eval LLMs, I initially had examples based on [🤗’s deep dive](https://huggingface.co/blog/evaluating-mmlu-leaderboard), which included comparisons on prompts, evaluation methodology, and ranking differences. I thought it was interesting to look at the differences but unfortunately I didn’t have the time. This and the next 3 slides after it were cut to save ~2 minutes.

Comparison between MMLU prompts.

Comparison between MMLU evaluation approach.

How model ranking changes across different MMLU implementations.

I initially had this meme on how LLMs are like (some of) us, where they focus on the intro (i.e., doc in first position) and conclusion (i.e., doc in last position). But it seemed too complex and thus was cut.

I originally wanted to share the usefulness and flexibility of the abstractive summarization task via this slide and the two slides below. But it was cut to save about 1 minute.

Abstractive summarization across multiple documents to build a timeline.

Abstractive summarization on weekly spending.

Initially had this slide as a datapoint on the severity of hallucinations in summarization, based on this [paper](https://arxiv.org/abs/2309.09558) that was barely a month old. Nonetheless, it was cut to save ~30 secs.

I initially wanted to include QG-QA as a technique to evaluate factual consistency in summarization because it’s one of two main approaches to detecting factual inconsistency in summarization (the other being NLI). But, I didn’t like the complexity of the technique and could not see myself using it in production. Thus, it was cut to save ~1 minute.

Wanted to include another example of how implicit feedback could be noisy but this example wasn’t as easy to grasp as I would like. Thus, it was cut.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Oct 2023). AI Engineer 2023 Keynote - Building Blocks for LLM Systems. eugeneyan.com.
> https://eugeneyan.com/speaking/ai-eng-summit/.

or

```
@article{yan2023aieng,
  title   = {AI Engineer 2023 Keynote - Building Blocks for LLM Systems},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2023},
  month   = {Oct},
  url     = {https://eugeneyan.com/speaking/ai-eng-summit/}
}
```

  
Share on:
