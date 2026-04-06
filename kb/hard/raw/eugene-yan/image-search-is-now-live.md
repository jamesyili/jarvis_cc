# Image search is now live!

**Source:** https://eugeneyan.com//writing/image-search-is-now-live/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

After finishing the image classification API, I wondered if I could go further. How about building a reverse image search engine? You can try it out here: [Image Search API](http://datagene.io/image_search_web). ([Github repositiory](https://github.com/eugeneyan/datagene))

> Update: API discontinued to save on cloud cost.

This is part of a series of posts on building a product classification API:

* [Data acquisition and formatting (part 1)](/writing/product-categorization-api-part-1-data-acquisition-and-formatting/)
* [Data cleaning and preparation (part 2)](/writing/product-categorization-api-part-2-data-preparation/)
* [API development (part 3)](/writing/product-categorization-api-part-3-creating-an-api/)
* [Image classification demo](/writing/image-categorization-is-now-live/)
* [Image search demo](/writing/image-search-is-now-live/)

## What is reverse image search?

In simple terms, given an image, reverse image search finds other similar images—this would be helpful in searching for similar looking products.

## How do I use it?

“My son has this plushie he really likes, but I don’t know what the name is… How can I find similar plushies?”

Till today, I have no idea what this is called, nor did I bother to look it up.

Simply browse and upload an image, select a category (optional, defaults to all categories), and search for similar products. Similar to image classification, this works best with product images with a white background, as that’s what the catalog images look like.

Why look up the name when you can just search via the image?

The results are not bad huh? I was surprised how powerful it was. (I found out that it’s called a Domo through this search).

Reverse image search is useful for finding products based on visual features (i.e., style, shape, colour). Have a certain sofa style you like? Or a pair of shoes? Or a jacket? Search for it via reverse image search.

Frankly, I was amazed it found more sofas with those "dimples".

(Note: You may find that it sometimes returns no/terrible results. Given the catalog only has ~200k products, there are instances where there are no results, or the results returned are the best (though terrible), given the catalog images)

For products where “how-it-looks” is the key search criteria, reverse image search provides great user experience, making it easy for users to quickly find what they want. If searching for products based on features not reflected in images (e.g., memory size, battery life, etc), regular search would work better.

## How does it work?

* Generate features from product images using (pretrained) neural network(s).
* Given a new image, generate features and calculate image similarities with existing images.
* Display images that are most similar to new image, up to a threshold (sometimes, there are simply no similar images in our catalog).

## Challenges faced

* The features generated can get pretty large in size! For example, VGG16 returns a numpy matrix with 25,088 32-bit floating points for each image. With the images I’m working with, features can grow up to 4 - 7x of image size, leading to possible scaling issues with storing and computing image similarities.
* Calculating similarities between image features (i.e., vectors) in an efficient manner was tricky. I tried multiple similarity measures and methods, and implemented a few from scratch in numpy, to find the optimal balance between speed and memory usage. And I still don’t find it fast enough.
* Serving images in HTML via a decent user interface was tricky for me. I’m no front-end/HTML guy and had to pick up a lot to have the user interface looking as it is now—and there’s still lots of room for improvement.

## Web Server updates

Previously, datagene.io was running on [Flask](https://flask.palletsprojects.com/en/1.1.x/)’s development server. While it worked well and didn’t fail, I wanted to improve on it by using [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) + nginx. From the front-end, you probably won’t notice any difference. The key difference is that it runs on multiple processes now—more than one user can be served simultaneously (not that it happens anyway haha).

P.S. I’ve just started my first course in the Georgia Tech OMS CS—Computer Vision. It’s been a blast so far and I really enjoy learning about the fundamentals of working with images. Unfortunately, it also means that I may not have time to add new features to datagene.io and write as often.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Jan 2017). Image search is now live!. eugeneyan.com.
> https://eugeneyan.com/writing/image-search-is-now-live/.

or

```
@article{yan2017image,
  title   = {Image search is now live!},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2017},
  month   = {Jan},
  url     = {https://eugeneyan.com/writing/image-search-is-now-live/}
}
```

  
Share on:
