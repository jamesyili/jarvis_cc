# LeetCode • 26. Remove Duplicates from Sorted Array

**Source:** https://aman.ai/lc_old/remove-dups-from-sorted-array/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Problem](#problem)
* [Algorithm](#algorithm)
* [Code](#code)
* [Complexity analysis](#complexity-analysis)

## Problem

* Given a sorted array \(nums\), remove the duplicates in-place such that each element appears only once and returns the new length.
* Do not allocate extra space for another array, you must do this by modifying the input array in-place with \(O(1)\) extra memory.
* See [problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) on LeetCode.

## Algorithm

* Since the array is already sorted, we can keep two pointers \(i\) and \(j\), where \(i\) is the slow-runner while \(j\) is the fast-runner. As long as \(nums[i] = nums[j]\), we increment \(j\) to skip the duplicate.
* When we encounter \(nums[j] \neq nums[i]\), the duplicate run has ended so we must copy its value to \(nums[i + 1]\). \(i\) is then incremented and we repeat the same process again until \(j\) reaches the end of array.

## Code

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        @param a list of integers
        @return an integer
        """
        
        # Handle the special case that A is empty    
        if not nums: # or "if not len(nums)" or "if len(A) == 0"
            return 0
        	
        i = 0
        for j in range(1, len(nums)):
            # Not a duplicate item            
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```

## Complexity analysis

* Time complexity: \(O(n)\). Assume that \(n\) is the length of array. Each of \(i\) and \(j\) traverses at most \(n\) steps.
* Space complexity: \(O(1)\).
