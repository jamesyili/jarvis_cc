# Image classification API is now live!

**Source:** https://eugeneyan.com//writing/image-categorization-is-now-live/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

After toiling for a few months on this, product image classification is now live on Datagene.io! While the [product classification API](/writing/product-categorization-api-part-3-creating-an-api/) works with product titles, the image classification API works with product images, though only for fashion. ([Github repositiory](https://github.com/eugeneyan/datagene))

> Update: API discontinued to save on cloud cost.

This is part of a series of posts on building a product classification API:

* [Data acquisition and formatting (part 1)](/writing/product-categorization-api-part-1-data-acquisition-and-formatting/)
* [Data cleaning and preparation (part 2)](/writing/product-categorization-api-part-2-data-preparation/)
* [API development (part 3)](/writing/product-categorization-api-part-3-creating-an-api/)
* [Image classification demo](/writing/image-categorization-is-now-live/)
* [Image search demo](/writing/image-search-is-now-live/)

Some facts about the image classification API:

* Works best with e-commerce like fashion images (as that’s what it was trained on)
* Top-1 validation accuracy: 0.76; Top-5 validation accuracy: 0.974
* Returns results under 300 milliseconds (will be faster in batch mode with GPU)
* Built on [Keras](https://keras.io/) and [Theano](http://deeplearning.net/software/theano/), and runs on a tiny [AWS](https://aws.amazon.com/) server without GPU.

How to play with it?
First, click on browse to select a file for upload. The file needs to have either a “.png”, “.jpg”, or “.jpeg” extension (case-insensitive).

A very simple input form for your images, with basic validation.

Then, click on the submit button below and wait patiently—results should appear in a second or so, depending on network speed and image size.

A very simple submit button.

## Here’s an example

Given a photo of a t-shirt…

I wonder if the model will also have learnt about the tagline on the t-shirt.

… here’s the result we get.

Oh, they don't have a category for smartass t-shirt.

## It works on mobile too

Look ma, web responsive!

You can also try the image classification API on mobile. On iOS, it allows you to take a photo, or select one from your photo library or iCloud drive.

Please leave suggestions on UI (or any other) improvements in the comments!

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Nov 2016). Image classification API is now live!. eugeneyan.com.
> https://eugeneyan.com/writing/image-categorization-is-now-live/.

or

```
@article{yan2016categorization,
  title   = {Image classification API is now live!},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2016},
  month   = {Nov},
  url     = {https://eugeneyan.com/writing/image-categorization-is-now-live/}
}
```

  
Share on:
