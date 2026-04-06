# Distilled • Subarray vs. Substring vs. Subsequence vs. Subset

**Source:** https://aman.ai/code/subarray-substring-subsequence-subset/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** algorithms

---

* [Subarray](#subarray)
* [Substring](#substring)
* [Subsequence](#subsequence)
* [Subset](#subset)

## Subarray

* A subarray is a **contiguous slice** of an array and inherently maintains the order of elements (i.e., the elements of the subarray occupy consecutive positions). For example, the subarrays of array `{1, 2, 3}` are `{1}`, `{1, 2}`, `{1, 2, 3}`, `{2}`, `{2, 3}`, and `{3}`.
* The following program generates all subarrays of the specified array:

```
# Function to print all sublists of the specified list
def printallSublists(nums):
    # consider all sublists starting from i
    for i in range(len(nums)):
        # consider all sublists ending at `j`
        for j in range(i, len(nums)):
            # Function to print a sublist formed by [i, j]
            print(nums[i: j + 1])
 
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    printallSublists(nums)
```

* which outputs:

```
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
[3]
[3, 4]
[3, 4, 5]
[4]
[4, 5]
[5]
```

* Please note that there are precisely \(\frac{n}{(n+1)/2}\) subarrays in an array of size \(n\). Also, there is no such thing as a contiguous subarray. The prefix contiguous is sometimes applied to make the context more clear. So, a contiguous subarray is just another name for a subarray.

## Substring

* A substring of a string `s` is a string `s'` that occurs in `s`. A substring is almost similar to a subarray, but it is in the context of strings (i.e., a substring is a **contiguous slice** of a string).
* For example, the substrings of string `'apple'` are `'apple'`, `'appl'`, `'pple'`, `'app'`, `'ppl'`, `'ple'`, `'ap'`, `'pp'`, `'pl'`, `'le'`, `'a'`, `'p'`, `'l'`, `'e'`, `''`.
* The following program that generates all non-empty substrings of the specified string:

```
# Function to print all non-empty substrings of the specified string
def printAllSubstrings(s):
    # consider all substrings starting from i
    for i in range(len(s)):
        # consider all substrings ending at j
        for j in range(i, len(s)):
            print(s[i: j + 1], end=' ')
 
if __name__ == '__main__':
    s = 'techie'
    printAllSubstrings(s)
```

* which outputs:

```
t te tec tech techi techie e ec ech echi echie c ch chi chie h hi hie i ie e
```

## Subsequence

* A subsequence is a sequence that can be derived from another sequence by **deleting some elements without changing the order of the remaining elements** (i.e., a subsequence **maintains the relative order of the array elements**). For example, `{nums, B, D}` is a subsequence of sequence `{nums, B, C, D, E}` obtained after removing `{C}` and `{E}`.
* People are often confused between a subarray/substring and a subsequence. A subarray or substring will always be **contiguous**, but a subsequence **need not be contiguous**. That is, subsequences are not required to occupy consecutive positions within the original sequences. But we can say that both contiguous subsequence and subarray are the same.
* In other words, the subsequence is a generalization of a substring, or substring is a refinement of the subsequence. For example, `{nums, C, E}` is a subsequence of `{nums, B, C, D, E}`, but not a substring, and `{nums, B, C}` is both a subarray and a subsequence.
* Please note that a subsequence can be in the context of both arrays and strings. Generating all subsequences of an array/string is equivalent to generating a power set of an array/string. For a given set, S, we can find the power set by generating all binary numbers between \(0\) and \(2^n-1\), where \(n\) is the size of the given set. This approach is demonstrated below:

```
# Function to print all subsequences of the specified string
def findPowerSet(seq):
    # N stores the total number of subsets
    N = int(pow(2, len(seq)))
 
    # generate each subset one by one
    result = []
    for i in range(N):
        s = ''
        # check every bit of `i`
        for j in range(len(seq)):
            # if j'th bit of `i` is set, print S[j]
            if (i & (1 << j)) != 0:
                s += seq[j]
        result.append(s)
    print(result)
 
if __name__ == '__main__':
    seq = 'apple'
    findPowerSet(seq)
```

* which outputs:

```
['', 'a', 'p', 'ap', 'p', 'ap', 'pp', 'app', 'l', 'al', 'pl', 'apl', 'pl', 'apl', 'ppl', 'appl', 'e', 'ae', 'pe', 'ape', 'pe', 'ape', 'ppe', 'appe', 'le', 'ale', 'ple', 'aple', 'ple', 'aple', 'pple', 'apple']
```

## Subset

* A subset is any possible combination of the original set. The term subset is often used for subsequence, but that’s not right. A subsequence always **maintains the relative order of the array elements** (i.e., increasing index), but there is no such restriction on a subset. In other words, a subset is a **randomly ordered array which contains elements that exist in the original array**. For example, `{3, 1}` is a valid subset of `{1, 2, 3, 4, 5}`, but it is neither a subsequence nor a subarray.
* It is worth noting that all subarrays are subsequences and all subsequences are a subset, but the reverse is not valid. For instance, a subarray `{1, 2}` of array `{1, 2, 3, 4, 5}` is also a subsequence and a subset.
