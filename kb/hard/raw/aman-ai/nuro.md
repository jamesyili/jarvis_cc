# Nuro

**Source:** https://aman.ai/h/Nuro/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Data Pipeline](#data-pipeline)
* [ML Fundies](#ml-fundies)
* [Coding Blended ML System](#coding-blended-ml-system)
* [Nuro values](#nuro-values)
* [Project deep dive](#project-deep-dive)
* [Hold](#hold)

## Data Pipeline

## ML Fundies

Sure, here’s the reformatted text for better readability:

## Coding Blended ML System

1. **Scheduler APIs**:
   * **Schedule**: Adds a task with a time period N to a task set.
   * **Deschedule**: Removes the task from the set.
   * Functionality: Run each task in the set every N minutes.
   * Example: If we add two tasks with `schedule(task1, 3)` and `schedule(task2, 5)`, then the scheduler should run task1 every 3 minutes and task2 every 5 minutes.
2. **Implementation Guidance**:
   * No pre-provided code. You need to design and then implement the system.
   * You can ask the interviewer for any necessary helper functions.
   * Reference: Please Google “cron job scheduler” for some example code.
     - TheschedulerhassomeAPIsThefirstis“schedule”toaddataskwithatimeperiodNtoatasksetThesecondis“deschedule”toremovethetaskfromthesetWeneedtoruneachtaskintheseteveryNminutesForexampleweaddtwotaskswithschedule(task13)andschedule(task25)thentheschedulershouldruntask1every3minutesandtask2every5minutes
3. **VO 1 System Design**:
   * Design a back-end system to meet two needs:
     + **Each Vehicle can report location**: “Get Dashboard” to view a map similar to Uber, showing all nearby vehicles.
     + **Vehicle Details**: Click on the vehicle through the map to see detailed information about the vehicle.
   * Scalability: Initially, there were relatively few vehicles with qps = 1k, but later it scaled to many vehicles with qps = 100k.
4. **Input Requirement**:
   * Give an array containing three-dimensional coordinate points, e.g., `[[0, 0, 1], [0, 0, 2], ...]`.
5. **Coding Categories**:
   * Divided into two types:
     + **Coding Algorithm**: Regular LeetCode question.
     + **Coding System**: Lower-level tasks such as writing a template class in C++, multi-threading, etc.
   * Personal Note: I have interviewed many people recently. If you find this helpful, please let me know! I can continue to write interviews for other companies.

     ## Nuro values

## Project deep dive

## Hold

1. **First Round - Algorithm (VO Algo)**:
   * The task involved a scenario related to “medicine saving” and “adding obstacles,” indicating a problem-solving or algorithmic challenge.
   * The candidate used a “bidirectional breadth-first search (BFS)” as a solution approach. Bidirectional BFS is an algorithm used in graph theory to find the shortest path between two nodes. It runs two simultaneous BFS, one from each node (start and end), and stops when they meet in the middle.
2. **Second Round - System Design**:
   * The challenge was similar to a “Yaoyao Baba” system. While the exact nature of this system isn’t clear without more context, the description suggests a focus on multi-threading and real-time data processing.
   * The task involved handling video frames where one thread reads a video frame and puts it into a buffer, and another thread takes the frame out of the buffer. This is a typical producer-consumer problem in concurrent programming, where synchronization between threads and managing shared resources (like buffers) is crucial.
3. **Third Round - Behavioral Questions (BQ)**:
   * This round seems to have focused on standard behavioral questions (BQ), which are typical in tech interviews.
   * Specifically, the interview may have included questions about handling project conflicts or difficult situations in a work environment. These questions are designed to assess soft skills, like communication, teamwork, problem-solving, and conflict resolution.

Your description seems to recount a multi-stage interview process, possibly for a technical or research-oriented position. The interview appears to have included various components testing different skills and knowledge areas. Let’s break it down for clarity:

1. **Interaction with Undergraduate Students**:
   * The interviewers were three undergraduate students from top universities, including one from Berkeley’s Computer Science program.
   * Their recent start at the organization suggests they might have been conducting preliminary screening or involved in a peer interview process.
2. **First Interviewer - Research and Mathematics**:
   * The first interviewer focused on discussing your research background, which you found challenging due to vocabulary limitations.
   * A mathematical (geometry) problem was presented, resembling a simplified version of RANSAC, a method used in computer vision and image analysis. Your response involved discussing RANSAC in detail.
3. **Second Interviewer - Coding Test (Image Conversion)**:
   * This part of the interview was a coding test where you were asked to write a class for image conversion. You found this task relatively simple and completed it as required.
4. **Third Interviewer - Coding Test (Elementary Mathematics)**:
   * You encountered a coding question that seemed to involve elementary mathematics, which was unfamiliar to you. The hint provided by the interviewer was not very instructive.
   * You expressed a willingness to learn the mathematical skills required if they are commonly used in the job, acknowledging difficulty with this round.
5. **Day 2 - Interaction with Higher Management**:
   * On the second day, you interacted with higher management, including the hiring manager, a senior software engineer, and others.
   * The conversation seemed more informal, focusing on personal interactions rather than technical questions.
6. **Concerns About the Interview Process**:
   * You expressed concerns about the relevance of the interview questions to practical work, especially for experienced engineers.
   * The questions did not test knowledge blind spots but were more about exposure to specific mathematical skills.
   * There was a concern about the difficulty for undergraduates to ask research-oriented questions, noting that the level of questioning has increased possibly due to a larger pool of candidates and current job market trends.
7. **Overall Reflection**:
   * You reflect on the increasing competition (“involution”) in the job market and the changing dynamics of interviews in the current corporate environment.
   * There’s a hint of frustration or disappointment with the interview process, particularly with the technical and mathematical aspects that seemed disconnected from practical job skills.

This summary indicates a challenging and varied interview process, combining technical, mathematical, and personal interaction elements, with an emphasis on theoretical knowledge and academic skills.
