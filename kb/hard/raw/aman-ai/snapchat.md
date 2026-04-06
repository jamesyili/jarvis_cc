# SnapChat

**Source:** https://aman.ai/sysdes/snapchat/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Overview](#overview)
* [Functional Requirements](#functional-requirements)
* [Non-Functional Requirements](#non-functional-requirements)
* [Back of the Envelope Estimates](#back-of-the-envelope-estimates)
* [Data Model-Entity Relationship](#data-model-entity-relationship)
* [High Level Design](#high-level-design)
* [Main Components —](#main-components-)
* [Services we need —](#services-we-need-)
* [High level:](#high-level)
  + [Timeline](#timeline)
* [Detailed](#detailed)
* [Basic Low Level Design](#basic-low-level-design)
* [Complete Code](#complete-code)

## Overview

[Youtube video](https://www.youtube.com/watch?v=ZxBp6K8jbRM)

* DB: TTL
* Snapchat is a social networking platform where users can —
* Upload and share Photos and videos
* Create stories
* Tag another user/location in the post ( photo/video)
* Watch the feed of other users they follow.
* Follow other users
* Chat with other people
* Can control the visibility of their content by making it public( accessible to everyone) or private
* Designing Snapchat would involve:
* Conduct market research: Understand the target audience, their needs and preferences, and what features they expect from a social media app.
* Define the concept and features: Based on the research, define the concept and features of the app, such as messaging, video and photo sharing, filters, and geolocation.
* Create a wireframe: Create a rough layout of the app, including the user interface and navigation.
* Design the UI: Use a design software to create the visual elements of the app, such as the logo, color scheme, and typography.
* Develop the app: Using a programming language such as Swift or Java, write the code for the app, integrating the features and UI designs.
* Test the app: Use beta testers to identify and fix any bugs or issues before releasing the app to the public.
* Launch the app: Release the app on the App Store and Google Play, and promote it through various channels, such as social media and advertising.
* Monitor and update: Monitor the performance of the app, collect feedback from users, and continue to update the app with new features and improvements based on user needs.
* In this post we will design Snapchat ( simple version) with the most important features and components.

## Functional Requirements

* User should be able to create a short lived Story
* User’s followers or friends should be able to see the story in their story feed.
* The system should send notifications to the followers about the story.
* Stories should disappear after 24 hours(configurable).
* User should be able to see who has viewed the story and count of total views.

## Non-Functional Requirements

* The system should be highly available and can be eventually consistent.
* The system should have low latency.
* The system should be highly scalable.

## Back of the Envelope Estimates

* Total Daily active users = 1 M
* If every 1 out of every 10 users post a story everyDay
* Total stories posted in one day = 10^5
* Stories have text, multiple images and short videos
* Avg Memory required for Text story = 200 Bytes
* Avg Memory required for Image story = 100 KB \* 5 images = 500 KB
* Avg Memory required for Video story = I MB \* 2 = 2 MB
* 50% text + 40% image + 10% video =
* Text - 5 x 10^4 x200 bytes = 10^ 7 bytes
* Images-> 4 x 10^4 x 500 x 10^3 bytes= 2 x 10^10 bytes
* Videos -> 10^4 x 2 X 10^6 bytes = 2 x 10^10 bytes
* Total ~50 GB per day
* This data will not be accumulated and will be deleted per day.

## Data Model-Entity Relationship

* We will be using NoSQL databases to store the photo data in the form of a key value store as well capture the relationship between the different entities. We need high reliability wrt data.
* Users
  + Fields -
  + Username : String
  + Email : String
  + Password : String
  + Functionality —
  + Users can post photos and location to the photos.
  + Users can follow other people and have followers.
  + Users can get the feed of other people they are following
  + Users can like and comment photos
* Follow
  + User\_id1 : Int
  + User\_id2 : Int
  + Functionality —
  + User 1 can follow user2
  + User 2 can follow user1
* Post — Photos
  + Fields —
  + PostId : Int
  + User\_id : Int ( Foreign key from users table)
  + Photo Url : String
  + Caption: String
  + Post\_Timestamp: DateTime
  + Location : String
  + Functionality —
  + Post — Photos are used to generate feed
  + Post — Photos can be captioned and timestamped
* Likes
  Like\_id : Int
  User\_id:Int
  Post\_id: Int
  Timestamp: DateTime
  Functionality —
  Users can like the post-photos
  — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
  Comment
  Comment\_id : Int
  Post\_id: Int
  User\_id: Int
  Caption\_text : String
  Timestamp: DateTime
  Functionality —
  Users can comment on the post-photos
  Users can also reply to the prior comments

## High Level Design

Assumptions
There will be more reads than writes so we need to design read heavy system — More Slaves replicas ( where we can perform read operations fast)
We will be scaling horizontally (scale — out).
Services should be highly available.
Latency should be ~350ms for the feed generation.
Consistency vs Availability vs Reliability: Availability and Reliability are more important than consistency in this case.
The system is read heavy ( people see photos more than posting)

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

## Main Components —

Mobile Client : These are users accessing snapchat
Application Servers : Read, write and notification server
Load Balancer : Route and direct the requests to the required server performing designated service.
Cache (Memcache) : It’s a massive system to serve million of users fast. We will be caching the data based on LRU.
CDN : To improve the latency and throughput.
Database : To store the data based on the Data model above and fetch data from the Storage using the required path.
Storage (HDFS or Amazon S3) : To upload and store the photos.
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

## Services we need —

Like Service
Follow Service
Comment Service
Post Service
Generate Feed service

* To fetch the recent, most popular and relevant photos of people user follows
  Let’s say to create the news feed, the system pulls 50 photos on the timeline. To do so, the application server will fetch the metadata of recent 50 photos from the people’s post which the user follows.
  Then submit these 50 photos to the ranking algorithm which will score it based on the likeness, comments, user activity etc.
  To achieve great efficiency in feed generation, we should dedicate designated servers which continuously keep generating the feed for the users and store it in a table.
  The moment user login the system, the servers fetch the feed by querying the above table and show the results and store the timestamp.

## High level:

* Timeline generation, Pull or Push based? Always push because pull based will require user to get following list, get all recent posts from users. VERY time consuming.
* Add a service that does a pull based approach that will pregenerate their timeline before they open Snap.

* READ HEAVY SYSTEM NOT WRITE HEAVY SYSTEM so it will work like below:

* Caveat, celebrity users: They have 25 million + follower, so that is too many to push, so we will use a hybrid approach where we will have regular users push to our timeline and pull from celebrity timeline.

### Timeline

* DynamoDB has functionality for TTL : Time to live, so it will only live for 24 hours
* Timeline could just be an entry in the database with post ids with timestamps and sorted by timestamps in dynamoDB:

## Detailed

1) Post something, a story, image uploaded to S3
2) URL of S3 will be stored in push service
3) This will be saved within DynamoDb
4) When end user loads snap, it will fetch from timeline service :
5) Filter will remove posts after 24 hours
6) End user streams object from S3 via presigned URL. A presigned URL in Amazon S3 is a URL that provides temporary access to an object stored in an S3 bucket.
7) It allows you to grant time-limited access to the object to users or applications without requiring them to have AWS credentials or permissions.

## Basic Low Level Design

```
import java.util.*;

class User {
    private String id;
    private String username;
    private List<ChatMessage> chatMessages;
    private List<Story> stories;

    public User(String username) {
        this.id = UUID.randomUUID().toString();
        this.username = username;
        this.chatMessages = new ArrayList<>();
        this.stories = new ArrayList<>();
    }

    public void sendChatMessage(User recipient, String content) {
        ChatMessage chatMessage = new ChatMessage(this, recipient, content);
        chatMessages.add(chatMessage);
        recipient.receiveChatMessage(chatMessage);
    }

    public void receiveChatMessage(ChatMessage chatMessage) {
        chatMessages.add(chatMessage);
    }

    public void addStory(Story story) {
        stories.add(story);
    }

    public List<ChatMessage> getChatMessages() {
        return chatMessages;
    }

    public List<Story> getStories() {
        return stories;
    }

    public String getId() {
        return id;
    }

    public String getUsername() {
        return username;
    }
}

class ChatMessage {
    private User sender;
    private User recipient;
    private String content;
    private Date timestamp;

    public ChatMessage(User sender, User recipient, String content) {
        this.sender = sender;
        this.recipient = recipient;
        this.content = content;
        this.timestamp = new Date();
    }

    public User getSender() {
        return sender;
    }

    public User getRecipient() {
        return recipient;
    }

    public String getContent() {
        return content;
    }

    public Date getTimestamp() {
        return timestamp;
    }
}

class Story {
    private User owner;
    private String content;
    private int duration;

    public Story(User owner, String content, int duration) {
        this.owner = owner;
        this.content = content;
        this.duration = duration;
    }

    public User getOwner() {
        return owner;
    }

    public String getContent() {
        return content;
    }

    public int getDuration() {
        return duration;
    }
}

class SnapchatSystem {
    private Map<String, User> users;

    public SnapchatSystem() {
        this.users = new HashMap<>();
    }

    public void registerUser(String username) {
        User user = new User(username);
        users.put(user.getId(), user);
    }

    public void removeUser(String userId) {
        users.remove(userId);
    }

    public User getUser(String userId) {
        return users.get(userId);
    }
}

public class SnapchatApp {
    public static void main(String[] args) {
        SnapchatSystem snapchat = new SnapchatSystem();

        // Register users
        snapchat.registerUser("user1");
        snapchat.registerUser("user2");

        // Send chat messages
        User user1 = snapchat.getUser("user1");
        User user2 = snapchat.getUser("user2");
        user1.sendChatMessage(user2, "Hello, how are you?");

        // Print chat messages for a user
        User user = snapchat.getUser("user2");
        List<ChatMessage> chatMessages = user.getChatMessages();
        System.out.println("Chat Messages for User: " + user.getUsername());
        for (ChatMessage chatMessage : chatMessages) {
            System.out.println("Sender: " + chatMessage.getSender().getUsername());
            System.out.println("Content: " + chatMessage.getContent());
            System.out.println("Timestamp: " + chatMessage.getTimestamp());
            System.out.println();
        }

        // Add stories
        user1.addStory(new Story(user1, "Story 1", 10));
        user2.addStory(new Story(user2, "Story 2", 10));
        
        user = snapchat.getUser("user2");
        List<Story> stories = user.getStories();
        System.out.println("Stories for User: " + user.getUsername());
        for (Story story : stories) {
            System.out.println("Content: " + story.getContent());
            System.out.println("Duration: " + story.getDuration());
            System.out.println();
        }
    }
}
```

## Complete Code

* Upload and Share Photos and Videos:

```
Complete Code
Upload and Share Photos and Videos:
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def handle_upload():
    file = request.files['file']
    # Save the file to a storage service (e.g., AWS S3)
    # Generate a URL for the uploaded file
    # Store the file URL and metadata in the database
    return 'OK'

if __name__ == '__main__':
    app.run()
```

* Create Stories:

```
class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    file_url = Column(String)
    # Add more story fields as needed

# Implement a route to handle story creation and retrieval
# Store the story metadata in the database
# Use a storage service (e.g., AWS S3) to store story files
```

* Tag Another User/Location in the Post (Photo/Video):

```
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    file_url = Column(String)
    tagged_users = Column(String)  # Comma-separated list of user IDs
    location = Column(String)
    # Add more post fields as needed

# Implement a route to handle post creation and retrieval
# Store the post metadata in the database
# Use a storage service (e.g., AWS S3) to store post files
```

* Watch the Feed of Other Users They Follow:

```
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)

class Follow(Base):
    __tablename__ = 'follows'
    follower_id = Column(Integer, primary_key=True)
    followed_id = Column(Integer, primary_key=True)

# Implement a route to fetch the feed for a user
# Retrieve the posts from users the current user follows
# Display the feed to the user
```

* Follow Other Users

```
@app.route('/follow', methods=['POST'])
def handle_follow():
    follower_id = request.json['follower_id']
    followed_id = request.json['followed_id']
    # Store the follow relationship in the database
    return 'OK'
```
