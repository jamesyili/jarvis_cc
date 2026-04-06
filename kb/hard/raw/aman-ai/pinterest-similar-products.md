# Pinterest Similar Products

**Source:** https://aman.ai/sysdes/PinterestSimilarProduct/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Function requirements](#function-requirements)
* [Key metrics/data](#key-metricsdata)
* [System design](#system-design)
  + [Background Pinterest Search](#background-pinterest-search)

## Overview

* Design a system to detect similar products and provide more context to users.
* How to tell whether two products are similar
  + Two shoes same size same color, different orientation
* What do you mean by better content

## Function requirements

* Detect products that are too similar
* Provide non duplicate data/content to users

## Key metrics/data

* num of users + estimated growth
* Database/storage size
* Reads vs Writes operation ratio
* Volume of request

## System design

### Background Pinterest Search
