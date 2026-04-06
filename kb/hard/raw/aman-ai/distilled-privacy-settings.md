# Distilled • Privacy Settings

**Source:** https://aman.ai/sysdes/privacy-settings/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Design Goals/Requirements](#design-goalsrequirements)
* [Scale Estimation and Performance/Capacity Requirements](#scale-estimation-and-performancecapacity-requirements)
  + [Traffic estimates](#traffic-estimates)
* [System APIs](#system-apis)
* [High Level System Design](#high-level-system-design)
* [Detailed Component Design](#detailed-component-design)
* [Extended Requirements](#extended-requirements)

## Overview

* On Facebook, you may have noticed that you can set different privacy levels for the posts you publish to be only visible to a specific set of users like public, friends, friends of friends, etc.

## Design Goals/Requirements

* Functional requirements:
  + Enable a user to specify the different levels of privacy for a post so that it is only visible to a particular set of users on Facebook.
  + For simplicity, implement two levels of privacy, Public and Friends.
* Non-functional requirements:
  + **Minimum latency**: Users should have a real-time chatting experience with minimum latency.
  + **High consistency:** Our system should be highly consistent; users should see the same privacy settings on all their devices.
  + **Relatively high availability but not at the cost of consistency (due to [CAP theorem](../cap-theorem)):** As we know from the CAP theorem, that we can have either high availability or high consistency, we can tolerate lower availability in the interest of consistency (but high availability is still desirable).
  + **Read-heavy service:** Our service should support a heavy read load. There will be a lot of read requests compared to modifying privacy settings for posts. Thus the number of read requests will be far greater than write requests.
* Complex Levels:
  + Friends of friends, and Custom Groups

## Scale Estimation and Performance/Capacity Requirements

* Some back-of-the-envelope calculations based on average numbers.

### Traffic estimates

* **Daily Active Users (MAUs):** 1B.
* **Number of posts for which privacy settings would be set:** 2B.
* **Read requests for the privacy level of posts (to make them visible to the correct audience)**: 100B.

## System APIs

* Once we have finalized the requirements, it’s always a good idea to define the system APIs. This should explicitly state what is expected from the system. These would be running as microservices on our application servers.
* We can have SOAP or REST APIs to expose the functionality of our service.
* The following could be the definition of the write API to set the privacy level for a particular post:

  ```
    setPrivacyLevel(user_id, post_id, privacy_level_enum, timestamp)
  ```

  + Parameters:
    - `user_id (number):` The ID of the user for whom the system will set the privacy level.
    - `post_id (number)`: ID of the post.
    - `timestamp (number):` The current timestamp to record privacy adjustment request.
  + Returns: (Bool) Success
* The following could be the definition of the read API to check if a user can view a particular post or not:

  ```
    canView(user_id, post_id, timestamp)
  ```

  + Parameters:
    - `user_id (number):` The ID of the user for whom the system will query the privacy level.
    - `post_id (number)`: ID of the post.
    - `timestamp (number):` The current timestamp for the request.
  + Returns: (Bool) Success

## High Level System Design

* To define the different privacy levels, we will use the Enum Data Type.
* The elements of this enum will be as follows:
  1. Public
  2. Friends
  3. Friends of Friends
  4. Custom
* This enum will be stored along with each post in the database.

* Steps Involved:
  1. To check whether a particular post is visible to a specific user or not, we will review the privacy level enum.
     a. If it is set to Public, then it will be visible to everyone.
     b. If it is set to Friends, we will check if the current user is a friend of the post’s author. If yes, then the post will be displayed on the UI.
  2. We will also need to discuss how we will **store and fetch the user’s friend list** to **efficiently check** if the post can be displayed. One possible way is to store the friends data of the users in a Key-Value Store.
     a. Key will be the User ID, and the value will be a set of all the friends that the user has.
     b. Since this data will be massive, it will be sharded across multiple servers using User ID as the key.
     c. We will also need to discuss what will happen if a shard dies and create a fault-tolerant design.

## Detailed Component Design

* It includes various components, such as:
  + Application servers to run system APIs as microservices.
  + Caches for fast retrieval.
  + Load balancers to distribute load as evenly as possible, and ensure crashed servers are taken out of the load distribution loop.

## Extended Requirements

* Friends of friends privacy settings:
  1. Given the scale of Facebook, we cannot enumerate through all the friends of friends as it will be an extensive list and increase the system’s latency.
  2. One possible way to solve this challenging problem is to perform an intersection of the **post’s owner** and the **viewer’s friend lists**.
  3. If the intersection results in a non-empty set, the viewer is a friend of friend of the owner, and thus the post can be displayed.
