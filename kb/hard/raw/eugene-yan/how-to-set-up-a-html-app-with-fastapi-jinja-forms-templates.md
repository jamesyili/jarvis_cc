# How to Set Up a HTML App with FastAPI, Jinja, Forms & Templates

**Source:** https://eugeneyan.com//writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

I usually use [`Flask`](https://flask.palletsprojects.com/en/1.1.x/) to build and deploy REST/web apps. Flask is simple to use and apps are easy to spin up with minimal code. Today, I decided to try [`FastAPI`](https://fastapi.tiangolo.com) for my new web app, inspired by [@tiangolo](https://twitter.com/tiangolo?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)’s recent [talk](https://www.youtube.com/watch?v=k7YRGNGi4KI).

The switch was easier than expected. FastAPI has great documentation and this [article](https://amitness.com/2020/06/fastapi-vs-flask/) by [@amitness](https://twitter.com/amitness) was useful. Nonetheless, I couldn’t find any guides on how to serve `HTML` with FastAPI. Thus, I wrote this simple article to plug the hole on the internet.

> Try it out with the GitHub repo here: [`fastapi-html`](https://github.com/eugeneyan/fastapi-html)

## First, We Build a REST API

Installing `FastAPI` is as easy as (more about [`poetry`](https://python-poetry.org/docs/#installation)):

```
poetry add fastapi uvicorn
```

Then, we build a simple [REST API](https://github.com/eugeneyan/fastapi-html/blob/master/src/rest.py).

```
from fastapi import FastAPI

from src.model import spell_number  # Spell a number: 1 -> 'one', 2 -> 'two'

app = FastAPI()

@app.get('/')
def read_root():
    return 'hello world'

@app.get("/rest")
def read_item(num: int):
    result = spell_number(num)
    return {"number_spelled": result}
```

Let’s start it up…

```
poetry run uvicorn src.rest:app --reload
```

And call the REST API. The API takes in a number, and [spells](https://github.com/eugeneyan/fastapi-html/blob/master/src/model.py) it out.

```
curl -X GET "http://127.0.0.1:8000/rest?num=1234" -H  "accept: application/json"
{"number_spelled":"one thousand, two hundred and thirty-four"}
```

## Now, Let’s Make it Serve HTML

First, we’ll need to install some additional dependencies, specifically `python-multipart` for HTML forms and `jinja` for templating.

```
poetry add jinja2 python-multipart
```

Then, we’ll create a simple [HTML template](https://github.com/eugeneyan/fastapi-html/blob/master/templates/form.html):

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Form</title>
</head>
<body>
<form method="post">
    <input type="number" name="num" value="1234"/>
    <input type="submit">
</form>

<p>Result: {{ result }}</p>

</body>
</html>
```

Next, we write a simple web app that:

* Mounts the templates directory
* Receives requests, and…
* Returns results via our HTML template

```
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from src.model import spell_number

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get('/')
def read_form():
    return 'hello world'

@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})
```

Let’s start it up…

```
poetry run uvicorn src.html:app --reload
```

And give it a spin. Viola, simple as that.

Our simple web app with FastAPI, Forms, and Jinja templates

> Today, I learnt how to use FastAPI to serve HTML web apps.   
>   
> It's straightforward with jinja, templates, and HTML forms. Here's the 2-min how-to.<https://t.co/RrrISggU8o>
>
> — Eugene Yan (@eugeneyan) [July 25, 2020](https://twitter.com/eugeneyan/status/1286889428665774080?ref_src=twsrc%5Etfw)

> Update: This article trended recently on [Made With ML](https://madewithml.com/projects/1974/how-to-set-up-a-html-app-with-fastapi-jinja-forms-templates/)!

> 🏆 Today’s trending post is How to Set Up a HTML App with FastAPI ([@tiangolo](https://twitter.com/tiangolo?ref_src=twsrc%5Etfw)) by [@eugeneyan](https://twitter.com/eugeneyan?ref_src=twsrc%5Etfw) <https://t.co/1fJE6Uf4xB>  
>   
> Made With ML mostly runs on FastAPI now (with the exception of a few extensions) bc of the many advantages mentioned here by [@KaiserFrose](https://twitter.com/KaiserFrose?ref_src=twsrc%5Etfw)<https://t.co/fVluux2Y5S>
>
> — Made With ML (@madewithml) [July 27, 2020](https://twitter.com/madewithml/status/1287741565503381504?ref_src=twsrc%5Etfw)

## References

* [Serving ML with FastAPI](https://www.youtube.com/watch?v=k7YRGNGi4KI)
* [FastAPI for Flask Users](https://amitness.com/2020/06/fastapi-vs-flask/)

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Jul 2020). How to Set Up a HTML App with FastAPI, Jinja, Forms & Templates. eugeneyan.com.
> https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/.

or

```
@article{yan2020fastapi,
  title   = {How to Set Up a HTML App with FastAPI, Jinja, Forms & Templates},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Jul},
  url     = {https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/}
}
```

  
Share on:
