# Pinterest Follow Pins

**Source:** https://aman.ai/sysdes/PinterestFollowPins/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Functional requirement](#functional-requirement)
* [Non functional requirements](#non-functional-requirements)
* [System design](#system-design)
  + [Follow entity](#follow-entity)
  + [Create Notification](#create-notification)
  + [Send Notification](#send-notification)
  + [Handling > 1M followers](#handling--1m-followers)

## Overview

* Come up with a system design for a new feeature where users can follow pins or users for updates.
* If I follow a pin or a user, whenever there is an update I should be notified when they edit a pin or post a new pin.

## Functional requirement

* Users should be able to follow different users or pins
* Users should get notified for user/pins they follow

## Non functional requirements

* DAU - 5 million
* num of pins - 5 billion
* QPS - 1 million QPS
* Read heavy
* Explanation: For Pinterest, a platform heavily focused on user-generated content, visual assets, and user interactions, it’s reasonable to assume that read operations significantly outnumber write operations due to the nature of users browsing, searching, and engaging with content.
* This puts emphasis on optimizing the system for efficient and high-speed data retrieval, making strategies like efficient indexing, caching, and using optimized file formats (such as Parquet or ORC) particularly important.

## System design

* Break down the system design into a few components:
  1. Follow entity
  2. Create notification for pin updates
  3. Send notification to users
  4. Handling update with too many followers

### Follow entity

* What happens when user clicks follow button?
* We should create an endpoint on the backedn server to store follower relationship
* When frontend hits endpoint, it would persist the follower relationship in db and return success response back to user
* Error response otherwise (network issue, invalid response, etc)

* relational db to store follower relationship
  + Non-relational database (e.g., MongoDB) : it is not great for storing relationship. It’s good for storing one-to-one mapping data that does not change often.
  + Graph database (e.g., Neo4j): the graph database is great when we need to deal with high depth of relationship between entities (e.g., social network in Facebook where we want to find friends of friends of friends). However, in our case, we are simply referring to a relationship between a user and an entity (one-to-many).

* Schema above
* A column for user and entity uuids. Another column to specify what type of entity it is (PIN vs. USER). Lastly, a column for timestamp when user started to follow the entity.

### Create Notification

* Now we have the follower relationship persisted in database, we need to figure out a way to create notification whenever followed pins/users make updates.

* User requests to create or edit pins are processed by calling an endpoint on the backend server, which then persists updates in a relational database (Pinterest’s chosen storage for pins).
* Notification Approach:
  + Synchronous: After database persistence, the backend directly notifies relevant followers and then responds to the user. This approach increases write operation latency.
  + Asynchronous: Post database persistence, the backend schedules a notification task, immediately responding to the user while notifications are processed independently. This is more suitable to avoid user wait times.
* Asynchronous Notification:
  + Ideal due to non-critical nature of notifications; users shouldn’t be delayed for pin operations.
  + Notification messages can be produced to Kafka, a message broker, either triggered by user requests or through database triggers.
* Notification Workers:
  + Workers subscribing to the Kafka topic process messages and generate notifications.
  + Workers fetch follower data from the followers table to identify users interested in the updated pins.
* Workers are kafka consumers
* This setup enables efficient and timely handling of user requests for creating or editing pins while also ensuring that notifications are generated without hindering the main user experience. The use of asynchronous processing, coupled with Kafka for message distribution, supports the scalability and responsiveness required by a platform like Pinterest.

### Send Notification

* Notifications Sent Asynchronously: Generally, notifications are sent out asynchronously.
* Different Priorities: Notifications have different priorities, and different queues may be used to handle these priorities.
* Default to Low Priority: Unless specified otherwise, notifications can be treated as low priority, and messages can be published in the low priority queue.
* Publishing Notification Messages: Once the notification messages are in the queue, they are ready for processing.
* Notification Workers: These workers subscribe to the queues and attempt to send notifications to the users.
* Finding the Backend Instance: The workers need to find the backend instance with an open connection to the user in order to forward the notification.
* Forwarding Notifications: The final step is forwarding the notification to the intended user through the identified connection.
* User Device Connection: A mobile/web user device can spin off a background service to create a web-socket connection with a notification backend instance.
* Persist Connection Information: Connection information is persisted in a key-value pair database, mapping the user ID to the machine ID (e.g., userID -> machineID).
* Worker Sending Notification: When a worker attempts to send a notification to a particular user, it looks up the backend instance managing the connection with that user in the key-value pair DB.
* Forwarding the Request: The worker then forwards the notification request to the correct backend instance using the mapping (userID -> machineID).
* Video Recommendation: It’s recommended to watch the “Scaling Push Messaging for Millions of Devices @Netflix” YouTube video. This presentation provides a detailed explanation of the notification service, complete with helpful slides.

### Handling > 1M followers

* Current Design Limitations: The existing system functions well for a small number of followers but struggles with large numbers (e.g., more than 1 million followers of a celebrity). Sending notifications to such a large audience could overwhelm the system.
* Need for Special Handling: Special handling is required for users or pins with an extremely high number of followers.
* Hybrid Approach Consideration: A hybrid approach similar to Twitter’s system could be adopted.
* Alternative to Burst Notifications: For updates with many followers, instead of sending burst notifications, a periodic client call to an endpoint (e.g., syncNotification) can be used.
* Periodic Updates: Clients (users) could be made to call this endpoint every 5 minutes, for example, to receive updates on entities with a large following.
* Avoiding Simultaneous Calls: To prevent all devices from calling the endpoint simultaneously, the period for calling can be randomized (e.g., a random time between 0 and 5 minutes). This ensures that the calls are spread out and the system is not overloaded.
