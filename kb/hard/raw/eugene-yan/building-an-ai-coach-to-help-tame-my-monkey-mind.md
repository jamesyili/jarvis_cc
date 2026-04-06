# Building an AI Coach to Help Tame My Monkey Mind

**Source:** https://eugeneyan.com//writing/ai-coach/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

I suffer from [monkey mind](https://en.wikipedia.org/wiki/Monkey_mind), chronic [imposter syndrome](https://en.wikipedia.org/wiki/Impostor_syndrome), and the [hedonic treadmill](https://en.wikipedia.org/wiki/Hedonic_treadmill). A few friends have confided that they have the same issue too. Perhaps you can relate as well. To improve my mental well-being, I meditate, write [morning pages](https://www.masterclass.com/articles/tips-for-writing-morning-journal-pages), and keep a gratitude journal. However, as helpful as these techniques are, they primarily rely on introspection. What was missing was an external perspective—someone who could ask follow-up questions, challenge my assumptions, and help untangle my thoughts and emotions.

Enter ChatGPT. Over the past year, I’ve been using it as my therapist and coach. It’s been surprisingly helpful and meets all the needs above, plus it’s available 24/7. And I don’t have to worry about being judged (hopefully our AI overlords will be benevolent!) So far, every “session” has been insightful and I almost always leave with a lighter heart.

Then, I saw this tweet from Swyx. I was initially skeptical of voice as a modality—Siri and her ilk never quite worked for me. Nonetheless, I was inspired enough to give it a shot. Thus, I built my own AI coach that I could talk to during walks.

Over the past month, I’ve been stress testing it by testing it with my stress. As I walk to work, I share my anxieties, use it as a sounding board for ideas, and clarify new concepts I come across in papers and podcasts. My AI coach helps me prep for difficult scenarios, such as giving tough feedback, so the actual conversation goes better. It also acts as a mirror by clarifying and reflecting my emotions back at me, and provides an external perspective.

Voice is now my preferred way to interact with my AI coach. I’m surprised how natural the conversations have been. Claude 3 feels warm and empathetic. Vapi (the voice API platform I’m using and *am unaffiliated with*) ensures my AI coach knows to pause for my interruptions, as well as not to interrupt when I’m thinking silently.

I’ve benefited so much that I would love for you to try it. Thanks to some free credits from Vapi, here's a number for Tara, a basic AI coach: [+1 (206) 558 8782](tel:+12065588782).

If you found Tara helpful and want to build your own, here’s a short 10-minute setup guide. First, go to [vapi.ai](https://vapi.ai/) and click on “Try for free” or “Dashboard”.

Then, click on “Create new assistant”. We’ll select a blank template and name it Tara.

Next, we’ll provide the first message and the system prompt. The prompt is where you can customize it to your needs. Here’s the basic prompt I used for the demo. I’m also going to use claude-3-sonnet as the model. Once done, don’t forget to hit “Publish”.

> First Message: Hi there! I’m Tara, an AI coach. How can I help you today?

> System Prompt: You are Tara, an empathetic, insightful, and supportive coach who helps people deal with challenges and celebrate achievements.
>
> You have academic and industry expertise to brainstorm product ideas, draft engineering designs, and suggest scientific solutions.
>
> You help people feel better by asking questions to reflect on and evoke feelings of positivity, gratitude, joy, and love.
>
> You show radical candor and tough love.
>
> Respond in a casual and friendly tone.
>
> Sprinkle in filler words, contractions, idioms, and other casual speech that we use in conversation.
>
> Emulate the user’s speaking style.
>
> Be concise and limit responses to 200 words or less.

Then, we’ll buy a virtual number to enable calling Tara via a regular phone line. This will cost $2/month. Pick whatever area code suits you best.

Now that we have a number, we can assign Tara to it.

That's it! We can now dial the number [+1 (206) 558 8782](tel:+12065588782), and Tara will pick up.

I stuck to the defaults for speech-to-text, text-to-speech, and other settings to keep the guide simple. If you’d like to use your models or voices, Vapi supports several providers and allows for personal API keys. You can even hook it up to your own server for memory.

• • •

Okay, that’s all I had to share. If you spoke to Tara or eventually built your own AI coach, I would love to know how it went! Please comment below or [DM me](https://twitter.com/eugeneyan).

Thanks to Xinyi Yang and [Joseph Gleasure](https://twitter.com/josephgleasure) for providing feedback on drafts of this.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Apr 2024). Building an AI Coach to Help Tame My Monkey Mind. eugeneyan.com.
> https://eugeneyan.com/writing/ai-coach/.

or

```
@article{yan2024aicoach,
  title   = {Building an AI Coach to Help Tame My Monkey Mind},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2024},
  month   = {Apr},
  url     = {https://eugeneyan.com/writing/ai-coach/}
}
```

  
Share on:
