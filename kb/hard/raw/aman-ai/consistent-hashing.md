# Consistent Hashing

**Source:** https://aman.ai/sysdes/consistentHashing/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Consistent hashing](#consistent-hashing)
* [Hash space and hash ring](#hash-space-and-hash-ring)
* [Hash servers](#hash-servers)
* [Server Lookup](#server-lookup)
* [Remove a server](#remove-a-server)
* [Wrap up](#wrap-up)

## Overview

* Horizontal scaling requires efficient and even distribution of requests and data across servers.
* Consistent hashing is a widely used technique for achieving efficient distribution.
* The problem of distributing requests and data evenly across servers is examined in detail.
* The rehashing problem arises when attempting to balance the load across multiple cache servers using a hash method.
* The hash method involves calculating the hash of a key and using modulo division to determine the server index.
* An example scenario is presented, with 4 servers and 8 string keys along with their corresponding hashes.

* The approach of using hash(key) % N for load balancing works well when the server pool size is fixed and data distribution is even.
* Challenges arise when servers are added or removed from the pool, causing changes in the server pool size.
* When a server goes offline (e.g., server 1 in this example), the server pool size decreases, leading to different server indexes for keys with the same hash value.
* Applying the hash modulo operation (% 3 in this case) to the keys results in different server indexes, as shown in Table 5-2.

Certainly! Here are the summarized bullets with the headings included:

## Consistent hashing

* Consistent hashing is a special kind of hashing technique that minimizes key remappings during hash table resizing.
* When consistent hashing is used, only k/n keys need to be remapped on average, where k is the number of keys and n is the number of slots.
* Traditional hash tables typically require remapping nearly all keys when the number of array slots changes.

## Hash space and hash ring

* Consistent hashing utilizes a hash space and a hash ring to distribute keys across servers.
* The hash function (e.g., SHA-1) produces hash values within a defined range known as the hash space.
* The hash space ranges from 0 to 2^160 - 1 in the case of SHA-1, where each hash value corresponds to a point on the hash ring.
* The hash values are uniformly distributed across the hash ring, ensuring even distribution of keys.

**Figure 5-3: Hash space and hash ring**

* Figure 5-3 illustrates the hash space and the distribution of hash values on the hash ring, showing how keys are distributed among servers using consistent hashing.

## Hash servers

* To map servers onto the hash ring, the same hash function f is used, typically based on the server’s IP address or name.
* The hash function generates a hash value for each server, which determines its position on the hash ring.
* Figure 5-5 visually represents the mapping of four servers onto the hash ring, showcasing their respective positions in the distributed system.

## Server Lookup

## Remove a server

* When a server is removed, only a small fraction of keys require redistribution with consistent hashing. In Figure 5-9, when server 1 is removed, only key1 must be remapped to server 2.
* The rest of the keys are unaffected.

## Wrap up

**Wrap up**

* Consistent hashing offers several benefits, including minimizing key redistribution when servers are added or removed, facilitating horizontal scaling, and mitigating hotspot key issues.
* It is widely used in various real-world systems, such as Amazon’s Dynamo database, Apache Cassandra, Discord chat application, Akamai content delivery network, and Maglev network load balancer.
