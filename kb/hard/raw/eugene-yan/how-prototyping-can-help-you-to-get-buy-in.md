# How Prototyping Can Help You to Get Buy-In

**Source:** https://eugeneyan.com//writing/prototyping-to-get-buy-in/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

Sometimes, well-thought-out proposals backed by extensive research and data will fail to convince decision-makers. But a demo of a simple prototype will get them excited and ready to commit. I’m surprised how often this happens.

While we should still [start projects with a one-pager](/writing/what-i-do-before-a-data-science-project-to-ensure-success/#first-draw-the-map-to-the-destination-one-pager) to clarify, socialize, and get feedback on our ideas, if we’re not making headway, one option is to build and demo a prototype.

## Why prototypes work: They’re more concrete

Prototypes make **our vision more accessible**. For non-technical laymen, ideas and designs can be *too abstract*. It’s hard to imagine the end-user experience from a document. In contrast, prototypes—especially those with a graphical user interface (GUI)—make it easier to understand the deliverable’s look and feel. By helping others understand our ideas better, we increase our chances of getting buy-in.

Prototypes also serve as **proof of technology**. What we claim to do with data and machine learning can be a stretch. (That said, the reverse, where we’re expected to do magic with a 500-row excel, also happens.) While trying to get buy-in, I’m occasionally met with skepticism—“Is that *really* doable?” By building a prototype, the proposal becomes real and achievable, making it easier to convince decision-makers.

> “It always seems impossible until it is done.” – Nelson Mandela

Last, prototypes make it **easier to get feedback**. Instead of attending a presentation or reading a proposal, people can interact with our app. They can test it with their data (e.g., product images, user interactions) and see the outcomes. By letting them interact with a prototype of our proposed idea, we increase our chances of getting feedback.

## But prototypes don’t explain “Why”

While prototypes can show “What does it look like?” and “How will it work?”, **they don’t explain “Why should we build it?”** Thus, if the *“why”* for the project is still unclear, we’re better off writing a [one-pager](/writing/what-i-do-before-a-data-science-project-to-ensure-success/#first-draw-the-map-to-the-destination-one-pager) to clarify the problem, intent, and success criteria. Else, it doesn’t matter how well our prototype works if it doesn’t solve the *right* problem.

Also, **depending on the scale of the project, a quick prototype may not be viable**. Large scale projects (e.g., drone delivery, self-driving cars, in-house ML platform) will need significant resources and can’t be prototyped in a week or two. Getting a first prototype off the ground might require months, if not years.

## How a prototype worked when a roadmap didn’t

In a previous role, I tried convincing stakeholders that our team should start working on computer vision. We had a massive catalog of product images and could use it to serve customers better. We would start with image classifiers to improve product categorization, before adapting them for image search and recommendation.

However, I failed to get buy-in. Some felt that our team lacked the expertise (read: “You won’t be able to do it”) and that it wasn’t a viable business opportunity.

I was disappointed but undeterred. If I couldn’t build it at work, I would have to build it in my free time. Using image data scraped from Amazon, I hacked together a [`Theano`](https://en.wikipedia.org/wiki/Theano_(software)) implementation (it was a *while* back) of [ResNet](https://en.wikipedia.org/wiki/Residual_neural_network) and applied transfer learning for [image classification](/writing/image-categorization-is-now-live/). To build [image search](/writing/image-search-is-now-live/), I used embeddings from the penultimate layer and calculated cosine similarity. This took months to learn and build but it worked decently.

Demo of image classifier and image search on fashion products

The effort was well worth it. Stakeholders were clearly excited when I demo-ed the prototypes. In particular, they found image-based search & recommendation to be a compelling use case, especially for visual shopping (e.g., fashion, furniture, toys). (A big chunk of transactions came from fashion.) This kickstarted our effort to invest in GPU clusters and work on computer vision applications.

Image search on toys and furniture

In 2018, the image search feature went live on the app.

Now customers can visually search for products via photos ([source](https://liveatpc.com/lazada-introduces-ai-powered-image-search-feature/))

## How to build a prototype now?

Many libraries make it easier to build and deploy machine learning prototypes in `Python`. For web application frameworks, [`Flask`](https://palletsprojects.com/p/flask/) and [`Bottle`](https://bottlepy.org/docs/dev/) are widely used while [`FastAPI`](https://fastapi.tiangolo.com) is gaining popularity. I recently switched to `FastAPI` and like it very much. Here’s a [great comparison](https://amitness.com/2020/06/fastapi-vs-flask/) for `Flask` users by [Amit Chaudhary](https://twitter.com/amitness).

To build a basic front-end, we can use a combination of [`Jinja`](https://palletsprojects.com/p/jinja/) templates and [`CSS`](https://www.w3.org/Style/CSS/Overview.en.html), and perhaps a framework like [`Bootstrap`](https://getbootstrap.com). [`Streamlit`](https://www.streamlit.io) is also a popular option. (I haven’t tried `Streamlit` though and would love to hear your experience with it.)

To serve our prototype, we can use [`Docker`](https://www.docker.com) to wrap and deploy it in a [container](https://www.docker.com/resources/what-container). For cloud servers, I tend to use Amazon Elastic Compute Cloud (EC2) [spot instances](https://aws.amazon.com/ec2/spot/) as they’re cheap. There are also options such as [Heroku](https://www.heroku.com) and [Digital Ocean](https://www.digitalocean.com).

Not sure how to get started? Here are a couple of additional resources:

* [Deploying machine learning with FastAPI and Heroku](https://testdriven.io/blog/fastapi-machine-learning/)
* [Setting up FastAPI with Jinja, Forms, and Templates](/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/)
* [Adding a checkbox and download button to a FastAPI web app](/writing/fastapi-html-checkbox-download/)

## Learn from my mistake with an early prototype: `curl`

One of my first machine learning projects was a title-based product classifier. I was able to build a system that achieved 95% accuracy and was looking to get user feedback. Thus, I wrapped it in a `Flask` app and deployed it on our internal servers.

To use the product classifier, all you had to do was to update the product title in the [`curl`](https://curl.haxx.se/docs/manpage.html) command below. It was as simple as it could get (or so I thought). After sharing the `curl` command and API specs with business and ops stakeholders, I eagerly monitored the logs for my first users.

```
curl -d '{"title":"title of product"}' -H "Content-Type: application/json" -X POST http://internal-url/categorize
```

No one used it 😞. I learned that most of my stakeholders were on windows machines and didn’t have easy access to `curl`. They were also unfamiliar with using the terminal or a tool like [Postman](https://blog.postman.com/curl-and-postman-work-wonderfully-together/)—I had to simplify it further.

To get around this, I spent some time building a simple front-end (the predecessor to the image classifier and image search UI) and shared my prototype again. This time around, instead of a `curl` command, stakeholders received a web url.

A simple GUI for product classification

The result? My tiny two-thread `Flask` server crashed from too many concurrent requests.

I learned a valuable lesson from this experience: No matter how good your tech is, non-technical users are unlikely to try unless it has a GUI and is easy to use. Since then, I’ve always taken the time to add a simple GUI to my prototypes.

## Try building a prototype early in your next project

Are you having difficulty communicating your vision and getting buy-in? Why not spend a week or two building a prototype? You’ll be surprised how effective they can be.

Do you have stories and experiences of prototypes helping to push a project forward? I would love to hear about them in the comments below.

> Why do prototypes get buy-in when well-written proposals backed by data fail?  
>   
> Because they are:  
> • More concrete than abstract ideas  
> • A proof of technology  
> • Interactive and easier to give feedback on  
>   
> But when do they fail? How should we build one?👇<https://t.co/OTERqwkj4L>
>
> — Eugene Yan (@eugeneyan) [October 14, 2020](https://twitter.com/eugeneyan/status/1316171360281006080?ref_src=twsrc%5Etfw)

**Thanks** to Yang Xinyi for reading drafts of this.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Oct 2020). How Prototyping Can Help You to Get Buy-In. eugeneyan.com.
> https://eugeneyan.com/writing/prototyping-to-get-buy-in/.

or

```
@article{yan2020prototype,
  title   = {How Prototyping Can Help You to Get Buy-In},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Oct},
  url     = {https://eugeneyan.com/writing/prototyping-to-get-buy-in/}
}
```

  
Share on:
