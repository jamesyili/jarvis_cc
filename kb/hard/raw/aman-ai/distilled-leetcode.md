# Distilled • LeetCode

**Source:** https://aman.ai/code/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** algorithms

---

* [Intro](#intro)
* [General Tips](#general-tips)
* [Patterns](#patterns)
* [Concepts](#concepts)
* [LeetCode Design Pattern Articles](#leetcode-design-pattern-articles)
* [Further Reading](#further-reading)
* [References](#references)

## Intro

* Distilled set of LeetCode problems for learning data structures and algorithms solved using Python 3.
* Refer [Python Tips and Tricks](python-tips) for an review of data structure concepts and their implementations with Python 3.
* Note that recursive (top-down) implementations store call-stacks (and hence are not \(O(1)\) space complexity). For \(O(1)\) space complexity, the computations must be performed iteratively (bottom-up) without using call-stacks.
* Here’s a list of the [full problem set](https://leetcode.com/problemset/all/) on LeetCode.

## General Tips

* These tips are from Sean Prasad’s LeetCode Patterns [Github repo](https://github.com/seanprashad/leetcode-patterns).

```
If input array is sorted, then
    - Binary search

If input array is not necessarily sorted, then
    - Sliding window
    - Two pointers

If asked for all permutations/combinations/subsets, then
    - Backtracking

If given a tree/graph/grid, then
    - DFS
    - BFS

If given a linked list then
    - Two pointers

If recursion is banned then
    - Stack

If must solve in-place then
    - Swap corresponding values
    - Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then
    - Dynamic programming

If asked for top/least K items then
    - Heap

If asked for common strings then
    - Map
    - Trie

Else
    - Map/Set for O(1) time & O(n) space
    - Sort input for O(nlogn) time and O(1) space
    
- A subarray or substring will always be contiguous, but a subsequence need not be contiguous, i.e., subsequences are not required to occupy consecutive positions within the original sequences.
```

* Check out LeetCode patterns sorted by companies/difficulty level/patterns [here](https://seanprashad.com/leetcode-patterns/).

## Patterns

* [Sorting/Searching](sorting-searching)
* [Two Pointers](two-pointers)
* [Sliding Window](sliding-window)
* [Binary Search](binary-search)
* [Hash Table](hashtable)
* [Heap](heap)
* [DFS](dfs)
* [BFS](bfs)
* [DP](dp)
* [Graphs](graphs)
* [Grid](grid)
* [Stack](stack)
* [Trie](trie)
* [Topological Sort](top-sort)
* [Misc](misc)

## Concepts

* [Asymptotic Notations](asymptotic-notations)
* [DFS vs. BFS](dfs-vs-bfs)
* [Subarray vs. Substring vs. Subsequence vs. Subset](subarray-substring-subsequence-subset)
* [Python Tips](python-tips)

## LeetCode Design Pattern Articles

* [Sliding Window patterns](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/)
* [Two Pointers Patterns](https://leetcode.com/discuss/study-guide/1688903/Solved-all-two-pointers-problems-in-100-days)
* [Substring Problem Patterns](https://leetcode.com/problems/minimum-window-substring/solutions/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems/)
* [Dynamic Programming](https://leetcode.com/discuss/study-guide/458695/Dynamic-Programming-Patterns) [Patterns](https://leetcode.com/discuss/study-guide/1437879/Dynamic-Programming-Patterns)
* [Binary Search Patterns](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)
* [Backtracking Patterns](https://leetcode.com/problems/permutations/solutions/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)/)
* [Tree Patterns](https://leetcode.com/discuss/study-guide/937307/Iterative-or-Recursive-or-DFS-and-BFS-Tree-Traversal-or-In-Pre-Post-and-LevelOrder-or-Views)
* [Graph Patterns](https://leetcode.com/discuss/study-guide/655708/Graph-For-Beginners-Problems-or-Pattern-or-Sample-Solutions)
* [Monotonic Stack patterns](https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems)

## Further Reading

* [Python for Interviewing: An Overview of the Core Data Structures](https://python.plainenglish.io/python-for-interviewing-an-overview-of-the-core-data-structures-666abdf8b698)
* [NeetCode 150/Blind 75](https://neetcode.io/)
* [Blind 50](https://www.techinterviewhandbook.org/best-practice-questions)
* [Blind 75](https://leetcode.com/list/xi4ci4ig/); [mirror](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)
* [Grind 75](https://www.techinterviewhandbook.org/grind75)
* [LeetCode Solutions](https://walkccc.me/LeetCode/preface/)
* [Sean Prasad: Leetcode Patterns](https://github.com/seanprashad/leetcode-patterns)

## References

* Python
  + [Time Complexity](https://wiki.python.org/moin/TimeComplexity)
* C++
  + [STL Time Complexity (Detailed)](http://www.cplusplus.com/reference/stl/)
  + [STL Time Complexity (Summary)](http://john-ahlgren.blogspot.com/2013/10/stl-container-performance.html)
  + [Data Structure and Algorithms Cheat Sheet](https://github.com/gibsjose/cpp-cheat-sheet/blob/master/Data%20Structures%20and%20Algorithms.md)
