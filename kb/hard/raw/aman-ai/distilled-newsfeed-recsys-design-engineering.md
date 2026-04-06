# Distilled • Newsfeed RecSys Design Engineering

**Source:** https://aman.ai/sysdes/newsfeedENG/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Step 1- Understand the problem and establish design scope](#step-1--understand-the-problem-and-establish-design-scope)
* [Step 2 - Propose high level and get buy in](#step-2---propose-high-level-and-get-buy-in)
  + [Newsfeed building](#newsfeed-building)
* [Step 3 - Design deep dive](#step-3---design-deep-dive)
  + [Cache architecture](#cache-architecture)
* [Step 4 - Wrap Up](#step-4---wrap-up)

## Overview

* News feed refers to the constantly updating list of stories, updates, and content displayed in the middle of a platform’s home page.
* It includes various types of content such as status updates, photos, videos, links, app activity, and likes.
* The news feed shows content from people, pages, and groups that the user follows or is connected to on the platform.
* Designing a news feed system is a common interview question, with examples including Facebook news feed, Instagram feed, Twitter timeline, and more.

## Step 1- Understand the problem and establish design scope

* Clarify the nature of the news feed system: Determine whether it is a mobile app, web app, or both.
* Identify important features: Understand that users can publish posts and view their friends’ posts on the news feed page.
* Determine the sorting order: Clarify whether the news feed is sorted by reverse chronological order or based on topic scores.
* Assess the number of friends: Determine the maximum number of friends a user can have, which in this case is 5000.
* Consider the traffic volume: Determine the daily active users (DAU) count, which in this case is 10 million.
* Determine content types: Confirm whether the news feed can contain images, videos, or only text.
* Begin designing the system based on the gathered requirements.

## Step 2 - Propose high level and get buy in

Feed Publishing Flow:

* Feed publishing is the process by which a user publishes a post on the news feed.
* Data is written into both the cache and the database when a user publishes a post.
* The post is then populated to the news feeds of the user’s friends.

News Feed Building Flow:

* The news feed is built by aggregating posts from friends in reverse chronological order.
* This process ensures that the most recent posts appear at the top of the news feed.

Newsfeed APIs:

* News feed APIs are the primary means of communication between clients and servers.
* These APIs are HTTP-based and allow clients to perform actions such as posting a status and retrieving the news feed.
* The two most important APIs are the feed publishing API and the news feed retrieval API.

Feed Publishing API:

* The feed publishing API is used to publish a post on the news feed.
* It is an HTTP POST request sent to the server.
* The API endpoint is “/v1/me/feed”.
* Required parameters include the content of the post and an authentication token.

Newsfeed Retrieval API:

* The news feed retrieval API is used to retrieve the user’s news feed.
* It is an HTTP GET request sent to the server.
* The API endpoint is “/v1/me/feed”.
* The only required parameter is an authentication token.
* When you enter a domain name in a web browser, such as “www.example.com,” the DNS server is responsible for resolving that domain name into the corresponding IP address, such as “192.0.2.123.” This process is known as DNS resolution or DNS lookup.
* DNS servers maintain a distributed database of domain names and their associated IP addresses. When a DNS server receives a request for a domain name, it searches its database to find the corresponding IP address

High-Level Design of Feed Publishing Flow:

* Figure 11-2 illustrates the high-level design of the feed publishing flow.

### Newsfeed building

* In this section, we discuss how news feed is built behind the scenes. Figure 11-3 shows the high-level design:

## Step 3 - Design deep dive

Feed Publishing Deep Dive:

In the feed publishing flow, there are several components involved. Figure 11-4 provides a detailed design for feed publishing, and we will focus on two important components: web servers and the fanout service.

Web Servers:

* Web servers handle the incoming HTTP POST requests from users who want to publish a post on their news feed.
* They receive the POST request containing the post content and the user’s authentication token.
* The web servers validate the authentication token to ensure the user is authorized to publish a post.
* Once the authentication is verified, the web servers store the post data into the cache and the database.
* The cache allows for fast retrieval of the most recent posts, while the database provides persistent storage of the posts.

Fanout Service:

* The fanout service is responsible for populating the user’s friends’ news feeds with the newly published post.
* After the post data is stored in the cache and the database, the fanout service retrieves the list of friends for the user who published the post.
* The fanout service performs a fanout operation, which means it sends a copy of the post to each of the user’s friends.
* This process ensures that the post is propagated to the news feeds of all the user’s friends, allowing them to see the new post in their feeds.

Other Components:

* The feed publishing flow also involves other components mentioned in the high-level design, such as authentication services, cache, and database.
* The authentication services validate the user’s authentication token to ensure the user has the necessary permissions to publish a post.
* The cache stores the most recent posts for fast retrieval and display in the user’s own news feed.
* The database provides persistent storage for the posts, allowing for efficient querying and retrieval when needed.

Overall, the detailed design for feed publishing involves web servers that handle user requests, authentication services for verifying user credentials, cache for storing recent posts, database for persistent storage, and the fanout service to distribute the new posts to friends’ news feeds.

Web Servers:

* Web servers handle client requests and are responsible for enforcing authentication and rate-limiting.
* Only users with valid authentication tokens (auth\_tokens) are allowed to make posts.
* Rate-limiting is implemented to prevent spam and abusive content by restricting the number of posts a user can make within a certain period.

Fanout Service:

* The fanout service is responsible for delivering a post to all of a user’s friends.
* Two fanout models are considered: fanout on write (push model) and fanout on read (pull model).
* Fanout on write involves pre-computing the news feed during write time, immediately delivering new posts to friends’ caches.
  + Pros: Real-time generation and immediate delivery of news feeds, fast fetching of news feed.
  + Cons: Slow and time-consuming for users with many friends (hotkey problem), waste of computing resources for inactive users.
* Fanout on read involves generating the news feed during read time, pulling recent posts when a user loads their home page.
  + Pros: Efficient for inactive users, no hotkey problem.
  + Cons: Slow fetching of news feed, as it is not pre-computed.

Hybrid Approach:

* To combine the benefits and address the drawbacks of both fanout models, a hybrid approach is adopted.
* The push model is used for the majority of users to ensure fast fetching of the news feed.
* For celebrities or users with a large number of friends/followers, the pull model is employed to avoid system overload.
* Consistent hashing, a technique for distributing requests/data evenly, is utilized to mitigate the hotkey problem.

By implementing this hybrid approach and leveraging consistent hashing, the system can achieve efficient and fast delivery of news feeds while optimizing resource usage and mitigating potential bottlenecks.

1. A user sends a request to retrieve her news feed. The request looks like this: `/v1/me/feed`.
2. The load balancer redistributes requests to web servers.
3. Web servers call the news feed service to fetch news feeds.
4. The news feed service gets a list of post IDs from the news feed cache.
5. A user’s news feed is more than just a list of feed IDs. It contains username, profile picture, post content, post image, etc. Thus, the news feed service fetches the complete user and post objects from caches (user cache and post cache) to construct the fully hydrated news feed.
6. The fully hydrated news feed is returned in JSON format back to the client for rendering.

### Cache architecture

* Cache is extremely important for a news feed system. We divide the cache tier into 5 layers:

• News Feed: It stores IDs of news feeds.
• Content: It stores every post data. Popular content is stored in hot cache.
• Social Graph: It stores user relationship data.
• Action: It stores info about whether a user liked a post, replied a post, or took other actions on a post.
• Counters: It stores counters for like, reply, follower, following, etc.

## Step 4 - Wrap Up

* In this article, we have designed a news feed system consisting of two main flows: feed publishing and news feed retrieval.
* When it comes to system design interview questions, there is no one-size-fits-all solution. Each company has its own unique constraints, and it’s important to design a system that aligns with those constraints. Understanding the trade-offs involved in your design choices and technology selection is crucial.
* If time permits, discussing scalability issues can be valuable. Here are some high-level talking points to consider:
* Scaling the database: Vertical scaling vs horizontal scaling, SQL vs NoSQL, master-slave replication, read replicas, consistency models, and database sharding.
* Other considerations: Keeping the web tier stateless, leveraging data caching, supporting multiple data centers, decoupling components with message queues, and monitoring key metrics such as peak QPS and latency during news feed refreshes.
