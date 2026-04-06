# Ad Online Auction

**Source:** https://aman.ai/sysdes/adonlineauction/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Functional](#functional)
* [Architecture](#architecture)

## Overview

* Allow items to be auctioned
* take bids
* Fixed auction deadline

## Functional

* 10M items per day
* 1B bids per day
* 10M / 100k items per day = 100 items per second
* 1B /100k bids per second = 10,000 bids per second

## Architecture
