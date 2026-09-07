---
concept: Distributed Systems Fundamentals
tags: [distributed-systems, scalability, consistent-hashing, cap-theorem, message-queues]
sources:
  - kb/hard/raw/aman-ai/consistent-hashing.md
  - kb/hard/raw/aman-ai/chat-system.md
  - kb/hard/raw/aman-ai/rate-limiter-engineering-design.md
  - kb/hard/raw/aman-ai/designing-a-unique-id-generator-in-distributed-systems.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/ad-systems|Ad Systems]]"
  - "[[hard/wiki/ml-system-design-framework|ML System Design Framework]]"
  - "[[hard/wiki/mlops-monitoring|MLOps & Monitoring]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Distributed Systems Fundamentals

Distributed systems design is a cornerstone of modern large-scale software. The core tension in every design decision is between consistency, availability, and partition tolerance — you cannot fully optimize all three simultaneously. Understanding the canonical building blocks (load balancing, hashing, ID generation, rate limiting) and how they compose is the foundation for system design interviews and production architecture decisions.

## Scaling: Horizontal vs. Vertical

**Vertical scaling** (scale-up): Add more resources (CPU, RAM, storage) to a single machine. Simpler operationally, no distribution complexity, but hard ceiling and single point of failure.

**Horizontal scaling** (scale-out): Add more machines. Enables theoretically unlimited capacity and fault tolerance, but requires efficient distribution of requests and data. The fundamental challenge: how do you route requests consistently and evenly across a dynamic pool of servers?

## Consistent Hashing

The naive approach — hash(key) % N — distributes load evenly when N is fixed. But when servers are added or removed, N changes, and nearly all keys remap to different servers. This causes a cache stampede or wholesale data migration.

**Consistent hashing** solves this by mapping both servers and keys onto a circular hash ring (using SHA-1's 0 to 2^160 − 1 range). Servers are placed at positions on the ring using hash(server_IP). A key is assigned to the first server encountered clockwise on the ring from hash(key).

When a server is removed, only the keys that were assigned to that server need to remap — to the next server clockwise. On average, only k/n keys remap (k = total keys, n = server count), versus nearly all keys in the naive approach. Adding a server is similarly cheap.

**Practical enhancements**: Real implementations use virtual nodes — each physical server maps to multiple positions on the ring — to improve load balance when server counts are small. This prevents hotspots when a single server is responsible for a disproportionately large arc of the ring.

**Used in production by**: Amazon Dynamo, Apache Cassandra, Discord, Akamai CDN, Maglev (Google's load balancer). Any system requiring cache partitioning or sharded storage benefits.

## CAP Theorem

A distributed system can guarantee at most two of:
- **Consistency**: All nodes see the same data at the same time.
- **Availability**: Every request receives a response (not necessarily the latest data).
- **Partition Tolerance**: The system continues operating during network partitions.

In practice, network partitions are a fact of life in any real distributed system — so the real choice is **CP vs. AP**:

- **CP systems** (e.g., HBase, ZooKeeper): Prioritize consistency. May refuse requests during a partition rather than return stale data. Appropriate for financial transactions, distributed locks, and any system where stale reads are harmful.
- **AP systems** (e.g., Cassandra, DynamoDB): Prioritize availability with eventual consistency. Return potentially stale data rather than fail. Appropriate for social feeds, caches, DNS.

The chat system design is an explicit CP tradeoff: "We can tolerate lower availability in the interest of consistency" because users seeing different chat histories on different devices is worse than occasional unavailability.

## Load Balancing

A load balancer sits in front of a server pool and distributes incoming requests. Strategies:

- **Round-robin**: Requests distributed sequentially. Simple but ignores server load.
- **Least connections**: Route to the server with fewest active connections. Better for variable-duration requests.
- **IP hash**: hash(client_IP) % N assigns each client to a consistent server. Useful for session affinity but degrades gracefully with consistent hashing for node changes.

**Layer 4 vs. Layer 7**: L4 load balancers operate at the TCP/IP level (faster, less context). L7 load balancers operate at the application level (HTTP) — can route based on URL path, headers, or content, enabling sophisticated routing like directing `/api/chat` to chat servers and `/api/login` to auth servers.

For stateful services (like a chat system where users have persistent WebSocket connections), load balancing is more complex: the load balancer must maintain a UserID-to-server mapping so messages can be routed to the correct server holding the user's connection.

## Unique ID Generation (Snowflake)

Distributed systems cannot use auto-increment — it requires a single write coordinator and creates a bottleneck. Requirements for distributed IDs: globally unique, 64-bit numeric, time-sortable, high throughput (10,000+ IDs/second).

**Options:**
- **UUID (128-bit)**: No coordination needed; easy to scale. But 128 bits (not 64), not numeric, not time-sortable.
- **Ticket Server**: Central auto-increment with single DB. Simple and numeric, but single point of failure.
- **Twitter Snowflake** (the canonical solution): A 64-bit ID composed of:
  - 1 bit: Sign (always 0)
  - 41 bits: Millisecond timestamp since custom epoch (Nov 4, 2010 for Twitter). Gives ~69 years of operation.
  - 5 bits: Datacenter ID (32 datacenters)
  - 5 bits: Machine ID (32 machines per datacenter)
  - 12 bits: Sequence number (4096 IDs per millisecond per machine; resets each ms)

Time-sortability is a built-in property: higher timestamp → higher ID. The 41-bit timestamp encodes milliseconds, giving a natural time ordering. Datacenter and machine IDs are assigned at startup and must be carefully managed — a misconfigured machine ID causes ID collisions.

**Clock synchronization caveat**: Snowflake assumes synchronized clocks. NTP is the standard solution, but clock skew can cause ID ordering anomalies. In chat systems, Snowflake generates global message IDs; local sequence numbers (unique only within a channel) are simpler and sufficient when cross-channel ordering isn't needed.

## Rate Limiting

Rate limiters protect services from DoS attacks, cost overruns, and server overload by capping request rates per user, IP, or device.

**Placement**: Server-side (in the application or as API gateway middleware) is preferred over client-side, which can be forged. In microservice architectures, the API gateway is the natural integration point alongside auth, SSL termination, and IP whitelisting.

**Algorithms:**

| Algorithm | How it works | Tradeoffs |
|---|---|---|
| Token bucket | Add tokens at fixed rate; each request consumes a token; burst allowed up to bucket size | Allows bursts; memory efficient; favored by Amazon/Stripe |
| Leaking bucket | FIFO queue; requests drain at fixed rate; overflow dropped | Stable outflow; burst fills queue, blocking recent requests |
| Fixed window counter | Count requests per fixed time window; drop if over limit | Simple; edge-of-window traffic spikes allow 2x bursts |
| Sliding window log | Track timestamps of each request; count within rolling window | Accurate; memory-heavy at scale |
| Sliding window counter | Weighted combination of current and previous window counts | Balance of accuracy and efficiency |

**Implementation**: Redis is the standard backend — INCR for counters, EXPIRE for TTL-based window resets. For distributed rate limiting, race conditions occur when multiple servers read-modify-write the counter simultaneously. Lua scripts (atomic execution on Redis) or sorted sets solve the race. Eventual consistency with multi-datacenter setups reduces latency at the cost of occasionally allowing slightly over-limit requests.

**Response protocol**: Return HTTP 429 with headers: `X-Ratelimit-Remaining`, `X-Ratelimit-Limit`, `X-Ratelimit-Retry-After`. Rate-limited requests can be queued for later processing rather than dropped.

## Caching Tiers and CDN

**Client cache**: Browser or app local storage. Zero latency for cached content; limited size.

**CDN**: Content Delivery Network — geographically distributed edge servers cache static and cacheable content. Requests are routed to the nearest edge node. For chat systems, CDNs can cache user avatars and media but not real-time messages.

**Application cache (Redis/Memcached)**: In-memory store between application and database. Chat systems cache the last N messages per conversation per user. Key design constraint: if all of a user's messages are on one shard, their cache should also live on one machine to avoid cross-machine lookups.

**Database read replicas**: Read from replicas, write to primary. Reduces read load on the primary but introduces replication lag (eventual consistency for reads).

## Message Queues

Message queues decouple producers from consumers and absorb load spikes. Key properties:
- **Durability**: Messages persist until acknowledged.
- **Ordering**: FIFO within a partition.
- **At-least-once vs. exactly-once delivery**: Most systems guarantee at-least-once; exactly-once requires distributed transactions or idempotent consumers.

In chat systems, message queues appear in the push notification path: offline user messages go to a notification server, which queues them for delivery via platform push services (APNs for iOS, FCM for Android). This decouples the chat server from notification delivery latency.

## Data Partitioning (Sharding)

Partition key selection is critical. For chat history:
- **Partition by MessageID**: Distributes messages across shards but forces multi-shard queries to fetch a user's conversation history. Bad for chat use cases.
- **Partition by UserID**: All messages for a user land on one shard. Fast conversation history fetch. Standard choice for chat — hash(UserID) % num_shards.

For massive scale (9.1 PB over 5 years at WhatsApp-scale), start with many logical partitions mapped to fewer physical servers. As demand grows, physical servers are added; logical partition count stays fixed, so no re-partitioning is needed.

**Key-value stores** (HBase, Cassandra) are preferred over relational databases for chat history because they scale horizontally, handle high write throughput, support fast range queries by timestamp, and are used in production by Facebook Messenger (HBase) and Discord (Cassandra).

## Service Discovery and WebSocket Communication

**Service discovery**: Dynamically maintains a registry of available service instances. Apache ZooKeeper is the standard solution — registers available chat servers, recommends the best server for a client based on geography and load. Clients connect to the selected server and maintain that connection.

**WebSocket vs. polling**: For real-time bidirectional communication, WebSocket (RFC 6455) is the standard. Starts as an HTTP connection, upgrades via handshake, maintains a persistent bidirectional TCP connection. Works through firewalls (uses port 80/443). Polling and long-polling are fallbacks — polling wastes resources on empty responses; long-polling has issues with sender/receiver on different servers. WebSocket for both send and receive paths simplifies the architecture.

## Sources

- Aman Chadha, "Consistent Hashing" — `kb/hard/raw/aman-ai/consistent-hashing.md`
- Aman Chadha, "Chat System" — `kb/hard/raw/aman-ai/chat-system.md`
- Aman Chadha, "Rate Limiter Engineering Design" — `kb/hard/raw/aman-ai/rate-limiter-engineering-design.md`
- Aman Chadha, "Designing a Unique ID Generator in Distributed Systems" — `kb/hard/raw/aman-ai/designing-a-unique-id-generator-in-distributed-systems.md`
