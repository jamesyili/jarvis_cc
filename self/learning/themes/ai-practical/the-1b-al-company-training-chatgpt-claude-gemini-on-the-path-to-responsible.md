# Edwin Chen — The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI | Edwin Chen
*Theme: ai-practical | Extracted: 2026-04-04*

## RL environments explained: simulation for real-world agent training

Lenny Rachitsky (00:34:49):
Reinforcement learning is essentially training your model to reach a certain reward. And let me explain what an RL environment is. An RL environment is essentially a simulation of real world. So think of it like building a video game with a fully fleshed out universe. Every character has a real story, every business has tools and data you can call, and you have all these different entities interacting with each other.

Edwin Chen (00:35:12):
So for example, we might build a world where you have a startup with Gmail messages, and Slack threads, and Jira tickets, and GitHub PRs, and a whole code base. And then suddenly AWS goes down. And Slack goes down. And so, "Okay. Model, well, what do you do?" The model needs to figure it out.

So we give them models tasks in these environments, we design interesting challenges for them, and then we run them to see how they perform. And then we teach them, we give them these rewards when they're doing a good job or a bad job.

And I think one of the interesting things is that these environments really showcase where models are weak at end-to-end tasks in real world. You have all these models that seem really smart on isolated benchmarks, they're good at single step tool calling. They're good at single step instruction following. But suddenly you dump them into these messy worlds where you have confusing Slack messages and tools they've never seen before, and they need to perform right actions and modify the [inaudible 00:36:06] and interact over longer time horizons where what they do in step one affects what they do in step 50. And that's very different from these kind of academic single step environments that they've been in before, and so the model just fails catastrophically in all these crazy ways.

So I think these RL environments are going to be really interesting playgrounds for the models to learn from that will essentially be simulations and mimics in real world, and so they'll hopefully get better and better at real tasks compared to all these contrived environments.

---

## Evolution of post-training: SFT to RLHF to rubrics to RL environments

Lenny Rachitsky (00:41:11):
You mentioned all the kind of the steps we've taken along the journey of helping models get smarter. Since you've been so close to this for so long, I think this is going to be really helpful for people. What's kind of like been the steps along the way from the first post-training that has most helped models advance? Where do evals fit in the RL environments? Just like what's been the steps and now we're heading towards RL environments?

Edwin Chen (00:41:33):
Originally, the way models started getting post-trained was purely through SFT. And—

Lenny Rachitsky (00:41:41):
What does that stand for?

Edwin Chen (00:41:42):
So SFT stands for supervised fine-tuning. So again, I think often in terms of these human analogies, and so SFT is a lot like mimicking a master and copying what they do.

And then RLHF became very dominant. And analogy there would be like sometimes you learn by writing 55 different essays and someone telling you which one they liked the most.

And then I think over the past year or so, rubrics and verifiers have become very important. And rubrics and verifiers are like learning by being graded and getting detailed feedback on where you went wrong.

Lenny Rachitsky (00:42:17):
And those are evals, another word for that?

Edwin Chen (00:42:19):
Yeah. So I think evals often covers two terms. One is you are using the evaluations for training because you're evaluating whether or not the model did a good job, and when it does do a good job, you're rewarding it.

And then there's this other notion of evals where you're trying to measure the model's progress like, okay, yeah, I have five different candidate checkpoints and I want to pick the one that's best in order to release it to the public. So going to run all these evals on these five different checkpoints in order to decide which one is best.

Lenny Rachitsky (00:42:51):
Awesome.

Edwin Chen (00:42:51):
Yeah, and now we have RL environments, so this is kind of like a hot new thing.

Lenny Rachitsky (00:42:55):
Awesome. So what I love about this business journey is just there's always something new. There's always this like, okay. We're getting so good at just all this beautiful data for companies and now they need something completely different. Now we're setting up all these virtual machines for them and all these different use cases.

Edwin Chen (00:43:08):
Yep.

Lenny Rachitsky (00:43:08):
And it feels like that's a big part of this industry you're in, it's just adapting to what labs are asking for.

Edwin Chen (00:43:13):
Yeah. So I really do think that we are going to need to build a suite of products that reflect a million different ways that humans learn.

Like for example, think about becoming a great writer. You don't become great by memorizing a bunch of grammar rules. You become great by reading great books, and you practice writing, and you get feedback from your teachers and from the people who buy your books in a bookstore and leave reviews. And you notice what works and what doesn't. And you develop taste by being exposed to all of these masterpieces and also just terrible writing. So you learn through this endless cycle of practicing reflection, and each type of learning that you have, again, these are all very different methods of learning to become a great writer, so just in the same way that... it's a thousand different ways that the great writer becomes great, I think there's going to be a thousand different ways that AI [inaudible 00:44:05] need to learn.

---

## Why benchmarks don't reflect real-world AI progress

Lenny Rachitsky (00:17:38):
You mentioned benchmarks. This is something a lot of people worry about is there's all these models that are always... Basically, it feels like every model is better than humans at every STEM field at this point, but to a regular person, it doesn't feel like these models are getting that much smarter constantly. What's your just sense of how much you trust benchmarks and just how correlated those are with actual AI advancements?

Edwin Chen (00:18:00):
Yeah, so I don't trust the benchmarks at all. And I think that's for two reasons. So one is I think a lot of people don't realize, even researchers within the community, they don't realize that the benchmarks themselves are often honestly just wrong. They have wrong answers. They're full of all this kind of messiness and people trust... Long as for the popular ones, people have maybe realized this to some extent, but the vast majority just have all these flaws that people don't realize. So that's one part of it.

And the other part of it is these benchmarks at the end of the day, they often have well-defined objective answers that make them very easy for models to hill-climb on in a way that's very different from the messiness and ambiguity of the real world.

I think one thing that I often say is that it's kind of crazy that these models can win IMO gold medals, but they still have trouble parsing PDFs. And that's because, yeah, even though IMO gold medals seem hard to the average person, yeah, they are hard at the end of the day. But they have this notion of objectivity that, okay, yeah, parsing a PDF sometimes doesn't have. And so it's easier for the frontier labs to hill-climb on all of these than to solve all these mess ambiguous problems in the real world. So I think there's a lack of direct correlation there.

Lenny Rachitsky (00:19:17):
It's so interesting the way you described it is hitting these benchmarks is kind of like a marketing piece. When you launch, say Gemini 3 just launched, and it's like, cool. Number one with all these benchmarks. Is that what happens? They just kind of train their models to get good at these very specific things?

Edwin Chen (00:19:31):
Yeah, so there's, again, maybe two parts to this. So one is, sometimes, yeah, these benchmarks, they accidentally leak in certain ways or the frontier labs will tweak the way they evaluate their models on these benchmarks. They'll tweak your system prompt or they'll tweak the number of times they run their model, and so on and so on in a way that games these benchmarks.

The other part of it though is it's like by optimizing for the benchmark instead of optimizing for the real world, you will just naturally climb on the benchmark and, yeah, it's basically another form of gaming it.

---
