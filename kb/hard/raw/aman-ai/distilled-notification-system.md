# Distilled • Notification System

**Source:** https://aman.ai/sysdes/notificationsystem/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Step 1: Understand the problem and establish design scope](#step-1-understand-the-problem-and-establish-design-scope)
* [Step 2: Propose high-level design and get buy-in](#step-2-propose-high-level-design-and-get-buy-in)
* [Step 3 - design deep dive](#step-3---design-deep-dive)
* [Step 4: Wrap up](#step-4-wrap-up)

## Overview

* A notification system is a popular feature in many applications.
* Notifications provide important information to users such as breaking news, product updates, events, and offerings.
* The chapter focuses on designing a notification system that includes three types of notification formats: mobile push notification, SMS message, and Email.
* Figure 10-1 provides an example of each notification format.

## Step 1: Understand the problem and establish design scope

* Clarification questions are important to understand the requirements of the notification system.
* The system supports three types of notifications: push notification, SMS message, and email.
* The system is a soft real-time system, aiming for timely delivery of notifications with some acceptable delay under high workload.
* The supported devices include iOS devices, Android devices, and laptop/desktop.
* Notifications can be triggered by client applications or scheduled on the server-side.
* Users have the option to opt-out and stop receiving notifications.
* The system sends out 10 million mobile push notifications, 1 million SMS messages, and 5 million emails per day.

## Step 2: Propose high-level design and get buy-in

* The high-level design supports various notification types: iOS push notification, Android push notification, SMS message, and Email.
* The design is structured into sections for different types of notifications.
* The first type is iOS push notification.

* To send an iOS push notification, we need three components: Provider, APNS, and iOS Device.
* The Provider is responsible for building and sending notification requests to the Apple Push Notification Service (APNS).
* The Provider requires the following data to construct a push notification: Device token (a unique identifier for the device) and Payload (a JSON dictionary containing the notification’s content).
* APNS is a remote service provided by Apple that propagates push notifications to iOS devices.
* The iOS Device is the end client that receives the push notifications.

* Android adopts a similar notification flow. Instead of using APNs, Firebase Cloud Messaging (FCM) is commonly used to send push notifications to android devices.

* The notification system serves as the central component for sending and receiving notifications.
* Initially, a single notification server is used, providing APIs for services 1 to N and building notification payloads for third-party services.
* Third-party services are responsible for delivering notifications to users, and careful attention should be given to extensibility and the availability of services in different markets.
* Users receive notifications on their iOS, Android, SMS, or Email devices.
* The initial design has three identified problems: a single point of failure (SPOF) with a single notification server, difficulty in scaling different components independently, and potential performance bottlenecks.
* The improved high-level design addresses these problems by moving the database and cache out of the notification server, adding more notification servers for horizontal scaling, and introducing message queues for decoupling system components.
* Figure 10-10 illustrates the improved high-level design.

## Step 3 - design deep dive

* Reliability is a crucial aspect of designing a notification system in distributed environments.
* Preventing data loss is a key requirement. The notification system achieves this by persisting notification data in a database and implementing a retry mechanism.
* The notification log database is used for data persistence, ensuring that notifications are not lost (Figure 10-11).
* Additional components and considerations in the design include notification templates, notification settings, rate limiting, retry mechanisms, security in push notifications, monitoring queued notifications, and event tracking.
* These components and considerations enhance the functionality, performance, and security of the notification system.
* The design is updated based on the identified challenges, incorporating solutions such as moving the database and cache out of the notification server, horizontal scaling with multiple notification servers, and introducing message queues for decoupling system components.

* **Will recipients receive a notification exactly once?**
  + Due to the distributed nature of the system, duplicate notifications may occur, making exact once delivery impossible.
  + To minimize duplication, a dedupe mechanism is introduced based on event IDs, discarding previously seen events.
  + Careful handling of failure cases is necessary to avoid unnecessary duplicate notifications.
* **Notification Template**
  + Notification templates are used to create customized notifications based on a preformatted structure.
  + Templates help maintain consistency, reduce margin errors, and save time when sending out millions of notifications.
  + Example template for push notifications: body and call-to-action (CTA) sections with customizable parameters.
* **Notification Setting**
  + Users are provided with fine-grained control over notification settings to manage the volume of notifications they receive.
  + Notification settings are stored in a table, including fields such as user ID, notification channel (push, email, SMS), and opt-in status.
  + Before sending a notification, the system checks if the user has opted-in to receive that specific type of notification.
* **Rate Limiting**
  + To prevent overwhelming users with excessive notifications, rate limiting is implemented to restrict the number of notifications a user can receive.
  + Over-sending notifications can lead to users disabling notifications entirely, affecting the user experience.
* **Retry Mechanism**
  + When a third-party service fails to send a notification, it is added to a message queue for retrying.
  + If the issue persists, developers are alerted to investigate and resolve the problem.
* **Security in Push Notifications**
  + Push notification APIs for iOS and Android apps use appKeys and appSecrets to ensure secure communication.
  + Only authenticated and verified clients are allowed to send push notifications via the system’s APIs.
* **Monitor Queued Notifications**
  + Monitoring the number of queued notifications is essential to assess the system’s performance.
  + A large number of queued notifications indicates a potential delay in processing by workers, requiring additional resources.
  + Figure 10-12 (credit to [7]) provides an example of queued messages awaiting processing.

## Step 4: Wrap up

* Notifications play a crucial role in keeping users informed and engaged with important information.
* The scalable notification system design supports multiple formats: push notification, SMS, and email.
* Message queues are used to decouple system components, improving scalability and flexibility.
* Reliability is ensured through a robust retry mechanism to minimize failure rates.
* Security measures, such as appKey/appSecret, authenticate and verify clients sending notifications.
* Tracking and monitoring components capture important statistics throughout the notification flow.
* User settings are respected, allowing users to opt-out of receiving notifications.
* Rate limiting helps manage the frequency of notifications to avoid overwhelming users.
* Congratulations on completing the chapter and understanding the design of a scalable notification system!
