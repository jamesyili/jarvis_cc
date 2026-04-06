# Youtube

**Source:** https://aman.ai/sysdes/youtubeEng/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Step 1 - Understand the problem and establish design scope](#step-1---understand-the-problem-and-establish-design-scope)
  + [Back of the envelope estimation](#back-of-the-envelope-estimation)
* [Step 2: propose high level design and get buy in](#step-2-propose-high-level-design-and-get-buy-in)
  + [Video uploading flow](#video-uploading-flow)
  + [Upload of an actual video](#upload-of-an-actual-video)
  + [Update the metadata](#update-the-metadata)
  + [Video streaming flow:](#video-streaming-flow)
* [Step 3: design deep dive](#step-3-design-deep-dive)
  + [Preprocessor](#preprocessor)
  + [DAG Scheduler](#dag-scheduler)
  + [Resource Manager](#resource-manager)
  + [Task Worker](#task-worker)
  + [Temporary Storage](#temporary-storage)
  + [Speed optimization: place upload centers close to users](#speed-optimization-place-upload-centers-close-to-users)
  + [Optimizations based on content popularity and user access pattern:](#optimizations-based-on-content-popularity-and-user-access-pattern)
  + [Error handling in the system:](#error-handling-in-the-system)
  + [Typical errors for each system component and corresponding actions:](#typical-errors-for-each-system-component-and-corresponding-actions)
* [Step 4 - Wrap up](#step-4---wrap-up)

## Overview

* YouTube looks simple: content creators upload videos and viewers click play. Is it really that simple? Not really. There are lots of complex technologies underneath the simplicity. Let us look at some impressive statistics, demographics, and fun facts of YouTube in 2020 [1] [2].
* Total number of monthly active users: 2 billion.
* Number of videos watched per day: 5 billion.
* 73% of US adults use YouTube.
* 50 million creators on YouTube.
* YouTube’s Ad revenue was $15.1 billion for the full year 2019, up 36% from 2018.
* YouTube is responsible for 37% of all mobile internet traffic.
* YouTube is available in 80 different languages.
* From these statistics, we know YouTube is enormous, global, and makes a lot of money.

## Step 1 - Understand the problem and establish design scope

* Important features: Ability to upload and watch videos.
* Supported clients: Mobile apps, web browsers, and smart TVs.
* Daily active users: 5 million.
* Average daily time spent: 30 minutes.
* International user support required.
* Supported video resolutions: Accept most resolutions and formats.
* Encryption is required.
* Maximum video size: 1GB for small and medium-sized videos.
* Leverage existing cloud infrastructures from Amazon, Google, or Microsoft.
* Design focus: Video streaming service with the following features:
  + Fast video upload capability.
  + Smooth video streaming experience.
  + Ability to change video quality.
  + Low infrastructure cost.
  + High availability, scalability, and reliability.
  + Supported clients: Mobile apps, web browsers, and smart TVs.

### Back of the envelope estimation

* The following estimations are based on many assumptions, so it is important to communicate with the interviewer to make sure she is on the same page.
* Assume the product has 5 million daily active users (DAU).
* Users watch 5 videos per day.
* 10% of users upload 1 video per day.
* Assume the average video size is 300 MB.
* Total daily storage space needed: 5 million \* 10% \* 300 MB = 150TB
* Content Delivery Network cost:
  + Amazon CloudFront is a Content Delivery Network (CDN) offered by Amazon Web Services (AWS). It is designed to help deliver content, such as web pages, videos, images, and other static or dynamic assets, to users with low latency and high data transfer speeds.
  + Here are some key features and benefits of Amazon CloudFront:
  + Global Edge Network: CloudFront has a vast network of edge locations distributed globally. These edge locations are strategically located closer to end users, allowing for reduced latency and faster content delivery.
  + Caching and Content Distribution: CloudFront caches content at its edge locations, enabling efficient content distribution. When a user requests content, CloudFront serves it from the edge location closest to the user, reducing the distance and network hops needed to retrieve the content from the origin server.
* When cloud CDN serves a video, you are charged for data transferred out of the CDN.
* Let us use Amazon’s CDN CloudFront for cost estimation (Figure 14-2) [3]. Assume 100% of traffic is served from the United States. The average cost per GB is $0.02. For simplicity, we only calculate the cost of video streaming.
* 5 million \* 5 videos \* 0.3GB \* $0.02 = $150,000 per day.

## Step 2: propose high level design and get buy in

* Leverage existing cloud services, specifically CDN and blob storage.
  + Blob storage refers to a type of storage service provided by cloud platforms, including Microsoft Azure and Amazon Web Services (AWS).
  + It is designed for storing and accessing unstructured data, such as documents, images, videos, audio files, backups, and other binary large objects (BLOBs). The term “blob” is often used as a generic term for any binary data.
  + Blob storage offers a scalable and cost-effective solution for storing large amounts of data in the cloud
* Netflix leverages Amazon’s cloud services, while Facebook uses Akamai’s CDN.

### Video uploading flow

* Components:
  + User: Watches YouTube on devices like a computer, mobile phone, or smart TV.
  + Load balancer: Distributes requests evenly among API servers.
  + API servers: Handle user requests, excluding video streaming.
  + Metadata DB: Stores video metadata, sharded and replicated for performance and high availability.
  + Metadata cache: Caches video metadata and user objects for improved performance.
  + Original storage: Blob storage system for storing original videos.
  + Transcoding servers: Convert video formats to provide optimized video streams for different devices and bandwidth capabilities.
  + Transcoded storage: Blob storage for storing transcoded video files.
  + CDN: Caches videos and streams them when the play button is clicked.
  + Completion queue: Message queue storing video transcoding completion events.
  + Completion handler: Workers that pull event data from the completion queue and update metadata cache and database.
* Video Uploading Flow:
  + Upload the actual video.
  + Update video metadata, including video URL, size, resolution, format, and user information.

### Upload of an actual video

1. Videos are uploaded to the original storage.
2. Transcoding servers fetch videos from the original storage and start transcoding.
3. Once transcoding is complete, the following two steps are executed in parallel:
   * 3a. Transcoded videos are sent to transcoded storage.
   * 3b. Transcoding completion events are queued in the completion queue.
   * 3a.1. Transcoded videos are distributed to CDN.
   * 3b.1. Completion handler contains a bunch of workers that continuously pull event data from the queue.
   * 3b.1.a. and 3b.1.b. Completion handler updates the metadata database and cache when video transcoding is complete.
4. API servers inform the client that the video is successfully uploaded and is ready for streaming.

### Update the metadata

* While a file is being uploaded to the original storage, the client in parallel sends a request to update the video metadata as shown in Figure 14-6.
* The request contains video metadata, including file name, size, format, etc. API servers update the metadata cache and database.

Here is the information organized in bullet points:

### Video streaming flow:

* When watching a video on YouTube, it starts streaming immediately without waiting for the whole video to download.
* Streaming involves receiving continuous video streams from remote source videos.
* Streaming allows for immediate and continuous video playback.
* Streaming protocols:
  + MPEG-DASH: “Dynamic Adaptive Streaming over HTTP” by the Moving Picture Experts Group.
  + Apple HLS: “HTTP Live Streaming” by Apple.
  + Microsoft Smooth Streaming.
  + Adobe HTTP Dynamic Streaming (HDS).
* Different streaming protocols support different video encodings and playback players.
* Choosing the right streaming protocol is important when designing a video streaming service.
* Video streaming from CDN:
  + Videos are streamed directly from the CDN (Content Delivery Network).
  + The edge server closest to the viewer delivers the video, resulting in minimal latency.

## Step 3: design deep dive

* High-level design consists of video uploading flow and video streaming flow.
* Refinement and optimization will be applied to both flows.
* Error handling mechanisms will be introduced.
* Video transcoding:
* Recording devices give videos a specific format, which needs to be encoded for compatibility.
  + Reasons for video transcoding:
    - Raw videos consume large storage space.
    - Different devices and browsers support specific video formats.
    - Delivering high-quality videos while maintaining smooth playback.
    - Adjusting video quality based on network conditions.
  + Encoding formats typically include:
    - Container: A basket-like structure that holds the video file, audio, and metadata (e.g., .avi, .mov, .mp4).
    - Codecs: Compression and decompression algorithms to reduce video size while preserving quality (e.g., H.264, VP9, HEVC).
* Directed acyclic graph (DAG) model:
  + Video transcoding is computationally expensive and time-consuming.
  + Different content creators have varying video processing requirements.
  + Adding abstraction allows client programmers to define tasks to execute.
  + Facebook’s streaming video engine uses a directed acyclic graph (DAG) programming model.
  + DAG model defines tasks in stages for sequential or parallel execution.
  + Adoption of a similar DAG model in the design for flexibility and parallelism.
  + Figure 14-8 represents a DAG for video transcoding.

### Preprocessor

### DAG Scheduler

### Resource Manager

### Task Worker

### Temporary Storage

* Multiple storage systems are used based on various factors.
* The choice of storage system depends on data type, data size, access frequency, and data lifespan.
* Metadata, frequently accessed by workers and with small data size, is cached in memory.
* Video or audio data is stored in blob storage.
* Temporary storage is used for data associated with video processing and is freed up once processing is complete.

### Speed optimization: place upload centers close to users

* Another way to improve the upload speed is by setting up multiple upload centers across the globe (Figure 14-24). People in the United States can upload videos to the North America upload center, and people in China can upload videos to the Asian upload center.
* To achieve this, we use CDN as upload centers.

* Message queues for loose coupling:
  + Introducing message queues enhances the system’s loose coupling, as shown in Figure 14-26.
  + Previously, without message queues, the encoding module had to wait for the output of the download module.
  + With the introduction of message queues, the encoding module no longer needs to wait for the download module’s output.
  + The encoding module can execute jobs in parallel if there are events in the message queue.

### Optimizations based on content popularity and user access pattern:

1. Serve popular videos from CDN and less popular videos from high-capacity storage video servers (Figure 14-28).
2. Encode short videos on-demand, eliminating the need to store many encoded versions for less popular content.
3. Distribute region-specific videos only to the relevant regions.
4. Consider building your own CDN and partnering with ISPs to enhance viewing experience and reduce bandwidth charges. ISPs can include Comcast, AT&T, Verizon, and others. (Note: This is a large-scale project and applicable to large streaming companies.)

### Error handling in the system:

* Recoverable errors:
  + Retry operations a few times for recoverable errors like failed video segment transcoding.
  + If the system determines that the task is not recoverable, return an appropriate error code to the client.
* Non-recoverable errors:
  + Stop running tasks associated with the video and return an appropriate error code for non-recoverable errors like malformed video format.

### Typical errors for each system component and corresponding actions:

* Upload error: Retry a few times.
* Split video error: If older client versions can’t split videos by GOP alignment, pass the entire video to the server for splitting.
* Transcoding error: Retry the transcoding operation.
* Preprocessor error: Regenerate the DAG diagram.
* DAG scheduler error: Reschedule the task.
* Resource manager queue down: Use a replica.
* Task worker down: Retry the task on a new worker.
* API server down: Stateless API servers, so requests will be directed to a different API server.
* Metadata cache server down: Data replication allows access to other nodes for fetching data. Bring up a new cache server to replace the offline one.
* Metadata DB server down:
  + Master is down: Promote one of the slaves to act as the new master.
  + Slave is down: Use another slave for reads and bring up a new database server to replace the offline one.

## Step 4 - Wrap up

In this chapter, we presented the architecture design for video streaming services like
YouTube. If there is extra time at the end of the interview, here are a few additional points:

* Scale the API tier: Because API servers are stateless, it is easy to scale API tier horizontally.
* Scale the database: You can talk about database replication and sharding.
* Live streaming: It refers to the process of how a video is recorded and broadcasted in real time. Although our system is not designed specifically for live streaming, live streaming and non-live streaming have some similarities: both require uploading, encoding, and streaming. The notable differences are:
* Live streaming has a higher latency requirement, so it might need a different streaming protocol.
* Live streaming has a lower requirement for parallelism because small chunks of data are already processed in real-time.
* Live streaming requires different sets of error handling. Any error handling that takes too much time is not acceptable.
* Video takedowns: Videos that violate copyrights, pornography, or other illegal acts shall be removed. Some can be discovered by the system during the upload process, while others might be discovered through user flagging
