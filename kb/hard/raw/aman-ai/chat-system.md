# Chat System

**Source:** https://aman.ai/sysdes/chatSystem/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Step 1: Understand the problem](#step-1-understand-the-problem)
* [Step 2 - Propose high-level design and get buy-in](#step-2---propose-high-level-design-and-get-buy-in)
* [Scale Estimation and Performance/Capacity Requirements](#scale-estimation-and-performancecapacity-requirements)
  + [Traffic estimates](#traffic-estimates)
  + [Storage estimates](#storage-estimates)
  + [Bandwidth estimates](#bandwidth-estimates)
* [System APIs](#system-apis)
  + [Polling](#polling)
    - [Long Polling](#long-polling)
  + [Web Socket](#web-socket)
* [High level design](#high-level-design)
* [Stateless Services:](#stateless-services)
* [Stateful Service:](#stateful-service)
* [Third-party Integration:](#third-party-integration)
* [Scalability:](#scalability)
* [Adjusted High-level Design:](#adjusted-high-level-design)
* [Storage:](#storage)
* [Data Models:](#data-models)
* [Message table for 1-on-1 chat:](#message-table-for-1-on-1-chat)
* [Message ID:](#message-id)
* [Step 3: Design deep dive](#step-3-design-deep-dive)
* [Service Discovery:](#service-discovery)
* [Message flows](#message-flows)
* [Message synchronization across multiple devices](#message-synchronization-across-multiple-devices)
* [Small group chat flow](#small-group-chat-flow)
  + [How will clients maintain an open connection with the server?](#how-will-clients-maintain-an-open-connection-with-the-server)
  + [How can the server keep track of all the opened connections to efficiently redirect messages to the users?](#how-can-the-server-keep-track-of-all-the-opened-connections-to-efficiently-redirect-messages-to-the-users)
  + [What will happen when the server receives a message for a user who has gone offline?](#what-will-happen-when-the-server-receives-a-message-for-a-user-who-has-gone-offline)
  + [How many chat servers do we need?](#how-many-chat-servers-do-we-need)
  + [How do we know which server holds the connection to which user?](#how-do-we-know-which-server-holds-the-connection-to-which-user)
  + [How should the server process a ‘deliver message’ request?](#how-should-the-server-process-a-deliver-message-request)
  + [How does the messenger maintain the sequencing of the messages?](#how-does-the-messenger-maintain-the-sequencing-of-the-messages)
* [Managing user’s status](#managing-users-status)
* [Data partitioning](#data-partitioning)
  + [Partitioning based on MessageID](#partitioning-based-on-messageid)
  + [Partitioning based on UserID](#partitioning-based-on-userid)
* [Cache](#cache)
* [Load balancing](#load-balancing)
* [Fault tolerance and Replication#](#fault-tolerance-and-replication)
  + [What will happen when a chat server fails?](#what-will-happen-when-a-chat-server-fails)
* [Extended Requirements](#extended-requirements)
  + [Group chat](#group-chat)
  + [Push notifications](#push-notifications)
* [Further Reading](#further-reading)
* [Step 4: Wrap Up](#step-4-wrap-up)

## Overview

* A chat app serves various functions depending on the target audience, so understanding the specific requirements is crucial.
* Identifying the intended focus of the chat system (e.g., group chat, one-on-one chat) is essential to design the system accordingly.
* Thoroughly exploring and clarifying the feature requirements is important to ensure the system meets the desired functionality.

## Step 1: Understand the problem

* Clarify the type of chat app: one-on-one or group-based.
* Determine if it’s a mobile app, web app, or both.
* Identify the scale of the app: startup or massive scale.
* Define the group chat member limit and important features.
* Discuss message size limit, encryption, chat history retention, and other specific requirements.
* Emphasize features like low delivery latency, small group chat, online presence, multiple device support, and push notifications.

## Step 2 - Propose high-level design and get buy-in

* To develop a robust design for a chat system, it is important to understand the communication flow between clients and servers. In a chat system, clients can be mobile or web applications, and they interact with a central chat service that encompasses all the required features. Our focus will be on the core operations that the chat service must support, including:
  + Receiving messages from other clients.
  + Determining the appropriate recipients for each message and forwarding it to them.
  + Storing messages for offline recipients and delivering them when they come online.

* When a client wants to initiate a chat, it establishes a connection with the chat service using one or more network protocols. The choice of network protocols is crucial for a chat service, and it’s worth discussing this aspect with the interviewer.
* In most client/server applications, including chat applications, requests are initiated by the client. In the context of chat messaging, the sender uses the HTTP protocol, a widely adopted web protocol, to communicate with the chat service. The client opens an HTTP connection and sends the message, instructing the service to deliver it to the receiver. By using the keep-alive header, the client can maintain a persistent connection with the chat service, reducing the number of TCP handshakes. Many popular chat applications, such as Facebook, initially utilized HTTP for sending messages.
* On the receiver side, things become more intricate. Since HTTP is client-initiated, it poses challenges for server-initiated message delivery. Over time, various techniques have been employed to simulate server-initiated connections, including polling, long polling, and WebSocket. These techniques are important topics often discussed in system design interviews, so let’s explore each of them.
* Functional requirements:
  + Messenger should support 1-1 conversations between users.
  + Messenger should keep track of the online/offline statuses of its users.
  + Messenger should support the persistent storage of chat history.
* Non-functional requirements:
  + **Minimum latency**: Users should have a real-time chatting experience with minimum latency.
  + **High consistency:** Our system should be highly consistent; users should see the same chat history on all their devices.
  + **Relatively high availability but not at the cost of consistency (due to [CAP theorem](../cap-theorem)):** As we know from the CAP theorem, that we can have either high availability or high consistency, we can tolerate lower availability in the interest of consistency (but high availability is still desirable).
* Extended Requirements:
  + **Group Chats:** Messenger should support multiple people talking to each other in a group.
  + **Push notifications:** Messenger should be able to notify users of new messages when they are offline.

## Scale Estimation and Performance/Capacity Requirements

* Some back-of-the-envelope calculations based on average numbers.

### Traffic estimates

* **Daily Active Users (DAUs)**: 1B.
* **Number of messages each user send**: 50.
* **Total number of messages sent per day**: 50 billion.

### Storage estimates

* **Message size**: 100 bytes.
* **Storage needed for one day worth of messages**: 50 billion messages \* 100 bytes = 5 TB/day.
* **Storage needed to store five years of chat history**: 5 TB \* 365 days \* 5 years ~= 9.1 PB.
  + Besides chat messages, we also need to store users’ information, messages’ metadata (ID, Timestamp, etc.). Not to mention, the above calculation doesn’t take data compression and replication into consideration.

### Bandwidth estimates

* **Upload/download needed**: 5 TB (per day) / 86400 sec (per day) ~= 58 MB/s
  + Since each incoming message needs to go out to another user, we will need the same amount of bandwidth 25MB/s for both upload and download.

## System APIs

* Once we have finalized the requirements, it’s always a good idea to define the system APIs. This should explicitly state what is expected from the system. These would be running as microservices on our application servers.
* We can have SOAP or REST APIs to expose the functionality of our service. The following could be the definition of the API for sending the message:

```
sendMessage(api_dev_key, user_id, addressed_user_id, chat_id)
```

* Parameters:
  + `api_dev_key (string):` The API developer key of a registered can be used to, among other things, throttle users based on their allocated quota.
  + `user_id (number):` The ID of the author of the message (can also be `author_id`).
  + `addressed_user_id (number):` The ID of the user whom the message is addressed to.
  + `chat_id (number):` The ID of the chat session where this message needs to be linked to.
  + `timestamp (number):` The timestamp of the message.
* We can have SOAP or REST APIs to expose the functionality of our service. The following could be the definition of the API for retrieving the message:

```
getMessage(api_dev_key, user_id, user_to_id, chat_id)
```

* Parameters:
  + `api_dev_key (string):` The API developer key of a registered can be used to, among other things, throttle users based on their allocated quota.
  + `user_id (number):` The ID of the current user trying to retrieve the latest chat messages.
  + `chat_id (number):` The ID of the chat session where this message needs to be linked to.
  + `timestamp (number):` The timestamp of the message.
* Returns: (JSON) Returns a JSON object containing a list of messages, each having `author_id` (the ID of the user whom the message is authored by), `message_text` (the contents of the message), `timestamp` (the timestamp of the message).

### Polling

* Polling is a technique where the client regularly queries the server to check if there are any new messages available. However, polling can be inefficient and resource-consuming. The client repeatedly sends requests to the server, even when there are no new messages, leading to unnecessary resource usage. This can be costly for both the client and the server, as valuable server resources are consumed to respond with a “no” answer most of the time.

#### Long Polling

* In long polling, the client keeps the connection open until new messages are available or a timeout is reached.
* Once new messages are received, the client immediately sends another request to the server to continue the process.
* Drawbacks of long polling include potential issues when sender and receiver are connected to different chat servers, difficulty in determining if a client is disconnected, and inefficiency when users do not engage in frequent chats.

### Web Socket

* WebSocket is the most common solution for sending asynchronous updates from server to client.
* WebSocket connection is initiated by the client and is bi-directional and persistent.
* It starts as an HTTP connection and can be upgraded to a WebSocket connection via a handshake.
* WebSocket allows the server to send updates to the client over the persistent connection.
* WebSocket connections can work even with firewalls in place as they use port 80 or 443, which are commonly used by HTTP/HTTPS connections.
* Using WebSocket for both sender and receiver sides is technically feasible and shown in Figure 12-6.

* By using WebSocket for both sending and receiving, it simplifies the design and makes implementation on both client and server more straightforward. Since WebSocket connections are persistent, efficient connection management is critical on the server-side.

## High level design

* At a high level, we will need a **chat server** that will be the central piece orchestrating all the communications between users. When a user wants to send a message to another user, they will connect to the chat server and send the message to the server; the server then passes that message to the other user and also stores it in the database.
  + In summary, our system needs to handle the following use cases:
    1. **Receive** incoming messages and **deliver** outgoing messages.
    2. **Store** and **retrieve** messages from the database.
    3. Keep a record of which user is **online** or has gone **offline**, and notify all the relevant users about these status changes.
* WebSocket is chosen as the main communication protocol between the client and server for its bidirectional communication.
* Other features of a chat application, such as sign up, login, and user profile, can still use the traditional request/response method over HTTP.
* The chat system is divided into three major categories: stateless services, stateful services, and third-party integration, as depicted in Figure 12-7.

## Stateless Services:

* Stateless services handle public-facing request/response operations such as login, signup, and user profile management.
* These services can be monolithic or individual microservices.
* They are typically behind a load balancer that routes requests based on the request paths.
* Service discovery plays a crucial role in providing the client with a list of DNS host names of chat servers to connect to.

## Stateful Service:

* The chat service is the only stateful service in the system.
* Each client maintains a persistent network connection to a chat server.
* The service discovery works closely with the chat service to prevent server overloading.

## Third-party Integration:

* Push notification integration is important for notifying users about new messages, even when the app is not running.
* Proper integration of push notifications is crucial for a chat app.

## Scalability:

* At a small scale, all services can fit on a single server.
* Even at the designed scale, theoretically, all user connections could be accommodated on one modern cloud server.
* The number of concurrent connections a server can handle becomes the limiting factor.
* However, designing for a single server raises concerns about single points of failure and scalability limitations.
* It is acceptable to start with a single server design as a starting point, but it should be communicated as a starting point rather than a final solution.

## Adjusted High-level Design:

* The high-level design, as shown in Figure 12-8, incorporates the various components discussed and their relationships within the system.

## Storage:

* The data layer in a chat system requires careful consideration.
* The choice between relational databases and NoSQL databases is important and depends on data types and read/write patterns.
* Two types of data exist: generic data (user profiles, settings, friends lists) and chat history data.
* Generic data is typically stored in reliable relational databases using techniques like replication and sharding.
* Chat history data has unique characteristics:
  + Enormous amount of data is processed in chat systems (e.g., Facebook Messenger and WhatsApp process 60 billion messages a day).
  + Only recent chats are accessed frequently, while older chats are less commonly accessed.
  + Random access of data may be required for features like search, viewing mentions, or jumping to specific messages.
  + The read-to-write ratio for 1-on-1 chat apps is approximately 1:1.
* Key-value stores are recommended for chat system storage due to their scalability, low latency, and ability to handle large data indexes.
* Key-value stores have been successfully adopted by reliable chat applications such as Facebook Messenger (using HBase) and Discord (using Cassandra).

## Data Models:

* Message data is crucial in a chat system.
* For 1-on-1 chat, a message table can be designed with a primary key (message\_id) to determine message sequence.
* Relying on the created\_at timestamp alone is insufficient since multiple messages can be created simultaneously.

## Message table for 1-on-1 chat:

* The message table (shown in Figure 12-9) includes the primary key (message\_id) to establish message sequence.

## Message ID:

* Generating a unique and sortable message\_id is important for ensuring the order of messages in a chat system.
* Two requirements for message\_id:
  + Unique: Each message\_id must be unique.
  + Sortable by time: Newer messages should have higher IDs than older messages.
* The “auto\_increment” keyword in MySQL can satisfy these requirements, but it’s not available in NoSQL databases.
* Another approach is to use a global 64-bit sequence number generator like Snowflake, as discussed in “Chapter 7: Design a unique ID generator in a distributed system.”
* A third approach is to use a local sequence number generator where IDs are only unique within a specific group.
* Local sequence numbers work well for maintaining message sequence within one-on-one or group channels.
* Implementing a local ID generator is easier compared to a global ID implementation.

## Step 3: Design deep dive

## Service Discovery:

* Service discovery plays a crucial role in recommending the best chat server to a client based on specific criteria.
* Apache Zookeeper is a popular open-source solution used for service discovery.
* It registers all the available chat servers in the system.
* Based on predefined criteria such as geographical location or server capacity, it selects the best chat server for a client.
* Service discovery ensures efficient routing of client requests to the appropriate chat server.

## Message flows

* It is interesting to understand the end-to-end flow of a chat system.
* In this section, we will explore 1 on 1 chat flow, message synchronization across multiple devices and group chat flow.
* 1 on 1 chat flow
  + Figure 12-12 explains what happens when User A sends a message to User B.

## Message synchronization across multiple devices

* Many users have multiple devices. We will explain how to sync messages across multiple devices. Figure 12-13 shows an example of message synchronization.

## Small group chat flow

* In comparison to the one-on-one chat, the logic of group chat is more complicated. Figures 12-14 and 12-15 explain the flow.

* The design mentioned earlier is suitable for small user groups, such as WeChat with a maximum of 500 users.
* However, for larger groups with thousands of members, informing all members about online status becomes resource-intensive and time-consuming.
* In a group with 100,000 members, each status change would generate 100,000 events, causing performance issues.
* To address this bottleneck, a possible solution is to fetch online status only when a user enters a group or manually refreshes the friend list.
* By fetching online status selectively, the system can optimize performance and reduce the number of unnecessary status updates for large groups.

#### How will clients maintain an open connection with the server?

* We can use HTTP [Long Polling](../long-polling) or [WebSockets](../long-polling). In long polling, clients can request information from the server with the expectation that the server may not respond immediately. If the server has no new data for the client when the poll is received, instead of sending an empty response, the server holds the request open and waits for response information to become available. Once it does have new information, the server immediately sends the response to the client, completing the open request. Upon receipt of the server response, the client can immediately issue another server request for future updates. This gives a lot of improvements in latencies, throughputs, and performance. However, the long polling request can timeout or receive a disconnect from the server; in that case, the client has to open a new request.

#### How can the server keep track of all the opened connections to efficiently redirect messages to the users?

* The server can maintain a hash table, where “key” would be the `UserID` and “value” would be the **connection object**. So whenever the server receives a message for a user, it looks up that user in the hash table to find the connection object and sends the message on the open request.

#### What will happen when the server receives a message for a user who has gone offline?

* If the receiver has disconnected, the server can notify the sender about the delivery failure. However, if it is a temporary disconnect, e.g., the receiver’s long-poll request just timed out, then we should expect a reconnect from the user. In that case, we can ask the sender to **retry** sending the message.
* This retry could be embedded in the client’s logic so that users don’t have to retype the message. The server can also store the message for a while and retry sending it once the receiver reconnects.
* The obvious last resort is to simply send a **Push Notification** to the user if they’re offline.

#### How many chat servers do we need?

* Let’s plan for 500 million connections at any time. Assuming a modern server can handle 50K concurrent connections at any time, we would need 10K such servers.

#### How do we know which server holds the connection to which user?

* We can introduce a software load balancer in front of our chat servers; that can map each `UserID` to a server to redirect the request.

#### How should the server process a ‘deliver message’ request?

* The server needs to do the following things upon receiving a new message: 1) Store the message in the database, 2) Send the message to the receiver, and 3) Send an acknowledgment to the sender.
* The chat server will first find the server that holds the connection for the receiver and pass the message to that server to send it to the receiver. The chat server can then send the acknowledgment to the sender; we don’t need to wait to store the message in the database (this can happen in the background). Storing the message is discussed in the next section.

#### How does the messenger maintain the sequencing of the messages?

* We can store a timestamp with each message, which is the time when the server receives the message. However, this will still not ensure the correct ordering of messages for clients. The scenario where the server timestamp cannot determine the exact order of messages would look like this:

  1. User-1 sends a message `M1` to the server for User-2.
  2. The server receives `M1` at `T1`.
  3. Meanwhile, User-2 sends a message `M2` to the server for User-1.
  4. The server receives the message `M2` at `T2`, such that `T2` > `T1`.
  5. The server sends the message `M1` to User-2 and `M2` to User-1.
* So User-1 will see `M1` first and then `M2`, whereas User-2 will see `M2` first and then `M1`.
* To resolve this, we need to keep a sequence number with every message for each client. This sequence number will determine the exact ordering of messages for EACH user. With this solution, both clients will see a different view of the message sequence, but this view will be consistent for them on all devices.

## Managing user’s status

* We need to keep track of user’s online/offline status and notify all the relevant users whenever a status change happens. Since we are maintaining a connection object on the server for all active users, we can easily figure out the user’s current status from this. With 500M active users at any time, if we have to broadcast each status change to all the relevant active users, it will consume a lot of resources. We can do the following optimization around this:

  1. Whenever a client starts the app, it can **pull the current status of all users in their friends’ list**.
  2. Whenever a user sends a message to another user that has gone offline, we can **send a failure to the sender and update the status on the client**.
  3. Whenever a user comes online, the server can always **broadcast that status with a delay of a few seconds (by batching updates from people)** to see if the user does not go offline immediately.
  4. Clients can pull the status from the server about those users that are being shown on the user’s viewport. This should not be a frequent operation, as the server is **broadcasting the online status of users and we can live with the stale offline status of users for a while**.
  5. Whenever the client starts a new chat with another user, we can **pull the status at that time**.
* The following diagram shows the detailed component design for Facebook messenger:

* Design Summary:
  + Clients will open a connection to the chat server to send a message; the server will then pass it to the requested user.
  + All the active users will keep a **connection open** with the server to receive messages.
  + Whenever a new message arrives, the chat server will **push it to the receiving user on the long poll request**.
  + Messages can be stored in **HBase**, which supports **quick small updates and range-based searches**.
  + The servers can **broadcast the online status of a user** to other relevant users.
  + Clients can **pull status updates for users who are visible in the client’s viewport on a less frequent basis**.

## Data partitioning

* Since we will be storing a lot of data (3.6PB for five years), we need to distribute it onto multiple database servers. So, what will be our partitioning scheme?

### Partitioning based on MessageID

* If we store different messages of a user on separate database shards, fetching a range of messages of a chat would be very **slow**, so we should **not adopt this scheme**.

### Partitioning based on UserID

* Let’s assume we partition based on the hash of the UserID so that we can keep all messages of a user on the same database. If one DB shard is 4TB, we will have “`3.6PB/4TB ~= 900`” shards for five years. For simplicity, let’s assume we keep 1K shards. So we will **find the shard number** by `hash(UserID) % 1000` and then store/retrieve the data from there. This partitioning scheme will also be very quick to fetch chat history for any user.
* In the beginning, we can start with fewer database servers with multiple shards residing on one physical server. Since we can have multiple database instances on a server, we can easily store multiple partitions on a single server. Our hash function needs to understand this logical partitioning scheme so that it can map multiple logical partitions on one physical server.
* Since we will store an unlimited history of messages, we can start with a large number of logical partitions that will be mapped to fewer physical servers. Then, as our storage demand increases, we can add more physical servers to distribute our logical partitions.

## Cache

* We can cache a few recent messages (say last 15) in a **few recent conversations that are visible in a user’s viewport (say last 5)**. Since we decided to store all of the user’s messages on one shard, the cache for a user should entirely reside on one machine too.

## Load balancing

* We will need a load balancer **in front of our chat servers** that can map each UserID to a server that holds the connection for the user and then direct the request to that server. Similarly, we would need a load balancer for our cache servers.

## Fault tolerance and Replication#

### What will happen when a chat server fails?

* Our chat servers are holding connections with the users. If a server goes down, should we devise a mechanism to transfer those connections to some other server? It’s **extremely hard to failover TCP connections** to other servers; an easier approach can be to have clients **automatically reconnect** if the connection is lost.
* Should we store **multiple copies of user messages**? We cannot store only one copy of the user’s data because if the server holding the data crashes or is down permanently, we don’t have any mechanism to recover that data. For this, either we have to store multiple copies of the data on different servers or use techniques like **Reed-Solomon encoding to distribute and replicate it**.

## Extended Requirements

### Group chat

* We can have separate group-chat objects in our system that can be stored on the chat servers. A group-chat object is identified by `GroupChatID` and will also maintain a list of people who are part of that chat. Our load balancer can direct each group chat message based on `GroupChatID`, and the server handling that group chat can iterate through all the users of the chat to find the server handling the connection of each user to deliver the message.
* In databases, we can store all the group chats in a separate table partitioned based on `GroupChatID`.

### Push notifications

* In our current design, users can only send messages to online users; if the receiving user is offline, we send a failure to the sending user. Push notifications will enable our system to send messages to offline users.
* For Push notifications, each user can opt-in from their **device** (or a **web browser**) to get notifications whenever there is a new message or event. Each manufacturer maintains a set of servers that handles pushing these notifications to the user.
* To have push notifications in our system, we would need to set up a **Notification server**, which will take the messages for **offline** users and send them to the **manufacturer’s push notification server**, which will then send them to the user’s device.

## Further Reading

* [M Now Offers Suggestions to Make Your Messenger Experience More Useful, Seamless and Delightful](https://about.fb.com/news/2017/04/m-now-offers-suggestions-to-make-your-messenger-experience-more-useful-seamless-and-delightful/)

## Step 4: Wrap Up

* The presented chat system architecture supports both 1-to-1 chat and small group chat, utilizing WebSocket for real-time communication between clients and servers.
* The key components of the chat system include chat servers for real-time messaging, presence servers for managing online presence, push notification servers for sending push notifications, key-value stores for chat history persistence, and API servers for other functionalities.
* Additional talking points for further discussion during the interview:
  + Extending the chat app to support media files, addressing topics such as compression, cloud storage, and thumbnails.
  + Exploring end-to-end encryption, referencing Whatsapp’s implementation for secure message transmission.
  + Discussing client-side caching of messages to reduce data transfer between the client and server.
  + Improving load time by implementing a geographically distributed network for caching users’ data, channels, etc., similar to Slack’s approach.
  + Considering error handling strategies, including handling chat server errors and implementing a message resend mechanism.
* These additional topics demonstrate a deeper understanding of chat system design and can be discussed if time permits during the interview.
