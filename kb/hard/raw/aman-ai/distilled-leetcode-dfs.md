# Distilled • LeetCode • DFS

**Source:** https://aman.ai/code/dfs/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** algorithms

---

* [Pattern: Backtracking/DFS](#pattern-backtrackingdfs)
  + [[17/Medium] Letter Combinations of a Phone Number](#17medium-letter-combinations-of-a-phone-number)
    - [Solution: Recursion](#solution-recursion)
      * [Complexity](#complexity)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs)
      * [Complexity](#complexity-1)
  + [[39/Medium] Combination Sum](#39medium-combination-sum)
    - [Problem](#problem)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-1)
      * [Complexity](#complexity-2)
  + [[40/Medium] Combination Sum II](#40medium-combination-sum-ii)
    - [Problem](#problem-1)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-2)
      * [Complexity](#complexity-3)
  + [[46/Medium] Permutations](#46medium-permutations)
    - [Problem](#problem-2)
    - [Solution: Using the `itertools` library](#solution-using-the-itertools-library)
    - [Solution: Recursive, take any number as first](#solution-recursive-take-any-number-as-first)
    - [Solution: Recursive, insert first number anywhere](#solution-recursive-insert-first-number-anywhere)
    - [Solution: Reduce, insert next number anywhere](#solution-reduce-insert-next-number-anywhere)
    - [Solution: Recursion](#solution-recursion-1)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-3)
      * [Complexity](#complexity-4)
  + [[47/Medium] Permutations II](#47medium-permutations-ii)
    - [Problem](#problem-3)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-4)
      * [Complexity](#complexity-5)
  + [[77/Medium] Combinations](#77medium-combinations)
    - [Problem](#problem-4)
    - [Solution: Using a library](#solution-using-a-library)
    - [Solution: Recursion](#solution-recursion-2)
    - [Solution: Iteration](#solution-iteration)
    - [Solution: Reduce](#solution-reduce)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-5)
      * [Complexity](#complexity-6)
  + [[78/Medium] Subsets](#78medium-subsets)
    - [Problem](#problem-5)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-6)
      * [Complexity](#complexity-7)
  + [[90/Medium] Subsets II](#90medium-subsets-ii)
    - [Problem](#problem-6)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-7)
      * [Complexity](#complexity-8)
  + [[91/Medium] Decode Ways](#91medium-decode-ways)
    - [Problem](#problem-7)
      * [Solution: Bottom-up/Iterative DP](#solution-bottom-upiterative-dp)
      * [Complexity](#complexity-9)
    - [Solution: One-liner](#solution-one-liner)
    - [Solution: DP + DFS](#solution-dp--dfs)
      * [Complexity](#complexity-10)
  + [[98/Medium] Validate Binary Search Tree](#98medium-validate-binary-search-tree)
    - [Problem](#problem-8)
    - [Solution: Inorder traversal](#solution-inorder-traversal)
    - [Complexity](#complexity-11)
  + [[94/Easy] Binary Tree Inorder Traversal](#94easy-binary-tree-inorder-traversal)
    - [Problem](#problem-9)
    - [Solution: Iteration with Stack](#solution-iteration-with-stack)
    - [Solution: Recursion](#solution-recursion-3)
    - [Solution: Recursive one-liner](#solution-recursive-one-liner)
      * [Complexity](#complexity-12)
  + [[102/Easy] Binary Tree Postorder Traversal](#102easy-binary-tree-postorder-traversal)
    - [Problem](#problem-10)
    - [Solution: Recursion with List](#solution-recursion-with-list)
      * [Complexity](#complexity-13)
    - [Solution: Iteration with Queue](#solution-iteration-with-queue)
      * [Complexity](#complexity-14)
  + [[102/Easy] Binary Tree Zigzag Level Order Traversal](#102easy-binary-tree-zigzag-level-order-traversal)
    - [Problem](#problem-11)
    - [Solution: Recursion with List](#solution-recursion-with-list-1)
      * [Complexity](#complexity-15)
    - [Solution: Iteration with Deque](#solution-iteration-with-deque)
      * [Complexity](#complexity-16)
  + [[105/Medium] Construct Binary Tree from Preorder and Inorder Traversal](#105medium-construct-binary-tree-from-preorder-and-inorder-traversal)
    - [Problem](#problem-12)
    - [Solution: Recursion](#solution-recursion-4)
      * [Complexity](#complexity-17)
  + [[106/Medium] Construct Binary Tree from Inorder and Postorder Traversal](#106medium-construct-binary-tree-from-inorder-and-postorder-traversal)
    - [Problem](#problem-13)
    - [Solution: Recursion](#solution-recursion-5)
      * [Complexity](#complexity-18)
  + [[107/Medium] Binary Tree Level Order Traversal II](#107medium-binary-tree-level-order-traversal-ii)
    - [Problem](#problem-14)
    - [Solution: Recursion with List](#solution-recursion-with-list-2)
      * [Complexity](#complexity-19)
    - [Solution: Iteration with Queue](#solution-iteration-with-queue-1)
      * [Complexity](#complexity-20)
  + [[108/Easy] Convert Sorted Array to Binary Search Tree](#108easy-convert-sorted-array-to-binary-search-tree)
    - [Problem](#problem-15)
    - [Solution: DFS with list slicing](#solution-dfs-with-list-slicing)
      * [Complexity](#complexity-21)
    - [Solution: DFS with list indices](#solution-dfs-with-list-indices)
      * [Complexity](#complexity-22)
  + [[124/Hard] Binary Tree Maximum Path Sum](#124hard-binary-tree-maximum-path-sum)
    - [Problem](#problem-16)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-8)
  + [[129/Medium] Sum Root to Leaf Numbers](#129medium-sum-root-to-leaf-numbers)
    - [Problem](#problem-17)
    - [Solution: Recursive DFS](#solution-recursive-dfs)
    - [Solution: BFS with Queue](#solution-bfs-with-queue)
    - [Solution: DFS with Stack](#solution-dfs-with-stack)
  + [[131/Medium] Palindrome Partitioning](#131medium-palindrome-partitioning)
    - [Problem](#problem-18)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-9)
      * [Complexity](#complexity-23)
  + [[133/Medium] Clone Graph](#133medium-clone-graph)
    - [Problem](#problem-19)
    - [Solution: BFS + Queue](#solution-bfs--queue)
    - [Solution: Iterative Backtracking/DFS + Stack](#solution-iterative-backtrackingdfs--stack)
    - [Solution: Recursive Backtracking/DFS](#solution-recursive-backtrackingdfs)
  + [[140/Hard] Word Break II](#140hard-word-break-ii)
    - [Problem](#problem-20)
    - [Solution: DP/Memoization](#solution-dpmemoization)
    - [Solution: DP + Python’s LRUCache](#solution-dp--pythons-lrucache)
      * [Complexity](#complexity-24)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-10)
      * [Complexity](#complexity-25)
  + [[144/Easy] Binary Tree Preorder Traversal](#144easy-binary-tree-preorder-traversal)
    - [Problem](#problem-21)
    - [Solution: Recursive one-liner](#solution-recursive-one-liner-1)
      * [Complexity](#complexity-26)
    - [Solution: Recursion](#solution-recursion-6)
      * [Complexity](#complexity-27)
    - [Solution: Iteration with Stack](#solution-iteration-with-stack-1)
      * [Complexity](#complexity-28)
  + [[145/Easy] Binary Tree Postorder Traversal](#145easy-binary-tree-postorder-traversal)
    - [Problem](#problem-22)
    - [Solution: Recursive one-liner](#solution-recursive-one-liner-2)
      * [Complexity](#complexity-29)
    - [Solution: Recursion](#solution-recursion-7)
      * [Complexity](#complexity-30)
    - [Solution: Iteration with Stack](#solution-iteration-with-stack-2)
      * [Complexity](#complexity-31)
  + [[173/Medium] Binary Search Tree Iterator](#173medium-binary-search-tree-iterator)
    - [Problem](#problem-23)
    - [Solution](#solution)
  + [[199/Medium] Binary Tree Right Side View](#199medium-binary-tree-right-side-view)
    - [Problem](#problem-24)
    - [Solution: DFS, combine right and left](#solution-dfs-combine-right-and-left)
      * [Complexity](#complexity-32)
    - [Solution: BFS/Level-order, iterative](#solution-bfslevel-order-iterative)
      * [Complexity](#complexity-33)
    - [Solution: BFS with Deque](#solution-bfs-with-deque)
      * [Complexity](#complexity-34)
    - [Solution: DFS, first come first serve](#solution-dfs-first-come-first-serve)
      * [Complexity](#complexity-35)
  + [[212/Hard] Word Search II](#212hard-word-search-ii)
    - [Solution: DFS/Backtracking with Trie](#solution-dfsbacktracking-with-trie)
    - [Optimizations](#optimizations)
      * [Complexity](#complexity-36)
  + [[226/Easy] Invert Binary Tree](#226easy-invert-binary-tree)
    - [Solution: Recursive Pre-Order Traversal DFS](#solution-recursive-pre-order-traversal-dfs)
      * [Complexity](#complexity-37)
    - [Solution: Iterative Pre-Order Traversal DFS with Queue](#solution-iterative-pre-order-traversal-dfs-with-queue)
      * [Complexity](#complexity-38)
  + [[230/Medium] Kth Smallest Element in a BST](#230medium-kth-smallest-element-in-a-bst)
    - [Problem](#problem-25)
    - [Solution: Iterative inorder traversal with a Deque of length `k`](#solution-iterative-inorder-traversal-with-a-deque-of-length-k)
      * [Complexity](#complexity-39)
    - [Solution: Recursion](#solution-recursion-8)
      * [Complexity](#complexity-40)
  + [[235/Medium] Lowest Common Ancestor of a Binary Search Tree](#235medium-lowest-common-ancestor-of-a-binary-search-tree)
    - [Problem](#problem-26)
    - [Solution: DFS Recursion](#solution-dfs-recursion)
      * [Complexity](#complexity-41)
    - [Solution: DFS Iteration](#solution-dfs-iteration)
      * [Complexity](#complexity-42)
  + [[Medium] Lowest Common Ancestor of a Binary Tree (without Root Node)](#medium-lowest-common-ancestor-of-a-binary-tree-without-root-node)
    - [Problem](#problem-27)
    - [Solution: Iteration](#solution-iteration-1)
      * [Complexity](#complexity-43)
    - [Solution: Recursion](#solution-recursion-9)
      * [Complexity](#complexity-44)
    - [Solution: DFS Iteration (Post-order Traversal with a Stack)](#solution-dfs-iteration-post-order-traversal-with-a-stack)
      * [Complexity](#complexity-45)
    - [Solution: Iteration (Path-building and finding the last node where the paths match)](#solution-iteration-path-building-and-finding-the-last-node-where-the-paths-match)
      * [Complexity](#complexity-46)
  + [[236/Medium] Lowest Common Ancestor of a Binary Tree](#236medium-lowest-common-ancestor-of-a-binary-tree)
    - [Problem](#problem-28)
    - [Solution: DFS Recursion One-liner](#solution-dfs-recursion-one-liner)
      * [Complexity](#complexity-47)
    - [Solution: DFS Iteration (Post-order Traversal with a Stack)](#solution-dfs-iteration-post-order-traversal-with-a-stack-1)
      * [Complexity](#complexity-48)
    - [Solution: DFS Iteration (Path-building and finding the last node where the paths match)](#solution-dfs-iteration-path-building-and-finding-the-last-node-where-the-paths-match)
      * [Complexity](#complexity-49)
    - [Solution: DFS Recursion](#solution-dfs-recursion-1)
      * [Complexity](#complexity-50)
  + [[257/Easy] Binary Tree Paths](#257easy-binary-tree-paths)
    - [Problem](#problem-29)
    - [Solution: Preorder traversal](#solution-preorder-traversal)
      * [Complexity](#complexity-51)
  + [[282/Hard] Expression Add Operators](#282hard-expression-add-operators)
    - [Problem](#problem-30)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-11)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-12)
  + [[297/Hard] Serialize and Deserialize Binary Tree](#297hard-serialize-and-deserialize-binary-tree)
    - [Problem](#problem-31)
    - [Solution: Recursive DFS preorder traversal](#solution-recursive-dfs-preorder-traversal)
      * [Complexity](#complexity-52)
  + [[332/Hard] Reconstruct Itinerary](#332hard-reconstruct-itinerary)
    - [Problem](#problem-32)
    - [Solution: Recursive DFS](#solution-recursive-dfs-1)
    - [Solution: Iterative DFS + Stack](#solution-iterative-dfs--stack)
      * [Complexity](#complexity-53)
  + [[339/Medium] Nested List Weight Sum](#339medium-nested-list-weight-sum)
    - [Problem](#problem-33)
    - [Solution: BFS](#solution-bfs)
      * [Complexity](#complexity-54)
    - [Solution: One-liner](#solution-one-liner-1)
      * [Complexity](#complexity-55)
    - [Solution: Recursive Backtracking/DFS](#solution-recursive-backtrackingdfs-1)
      * [Complexity](#complexity-56)
    - [Solution: Iterative Backtracking/DFS using Stack](#solution-iterative-backtrackingdfs-using-stack)
      * [Complexity](#complexity-57)
  + [[366/Medium] Find Leaves of Binary Tree](#366medium-find-leaves-of-binary-tree)
    - [Solution: Backtracking/DFS using Post-order Traversal](#solution-backtrackingdfs-using-post-order-traversal)
  + [[426/Medium] Convert Binary Search Tree to Sorted Doubly Linked List](#426medium-convert-binary-search-tree-to-sorted-doubly-linked-list)
    - [Problem](#problem-34)
    - [Solution: DFS in-order traversal](#solution-dfs-in-order-traversal)
  + [[428/Hard] Serialize and Deserialize N-ary Tree](#428hard-serialize-and-deserialize-n-ary-tree)
    - [Problem](#problem-35)
    - [Solution: Recursive DFS Pre-order Traversal](#solution-recursive-dfs-pre-order-traversal)
      * [Complexity](#complexity-58)
  + [[429/Medium] N-ary Tree Level Order Traversal](#429medium-n-ary-tree-level-order-traversal)
    - [Problem](#problem-36)
    - [Solution: Recursion](#solution-recursion-10)
      * [Complexity](#complexity-59)
    - [Solution: Iteration with Queue](#solution-iteration-with-queue-2)
      * [Complexity](#complexity-60)
  + [[472/Hard] Concatenated Words](#472hard-concatenated-words)
    - [Problem](#problem-37)
    - [Solution: DFS with Memoization](#solution-dfs-with-memoization)
      * [Complexity](#complexity-61)
  + [[489/Hard] Robot Room Cleaner](#489hard-robot-room-cleaner)
    - [Problem](#problem-38)
    - [Solution: Recursive DFS](#solution-recursive-dfs-2)
  + [[515/Medium] Find Largest Value in Each Tree Row](#515medium-find-largest-value-in-each-tree-row)
    - [Problem](#problem-39)
    - [Solution: BFS/Level-order Traversal](#solution-bfslevel-order-traversal)
    - [Solution: Recursive Backtracking/DFS with Pre-order Traversal](#solution-recursive-backtrackingdfs-with-pre-order-traversal)
      * [Complexity](#complexity-62)
    - [Solution: Iterative Backtracking/DFS with Stack](#solution-iterative-backtrackingdfs-with-stack)
      * [Complexity](#complexity-63)
  + [[543/Easy] Diameter of Binary Tree](#543easy-diameter-of-binary-tree)
    - [Problem](#problem-40)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-13)
      * [Complexity](#complexity-64)
  + [[589/Easy] N-ary Tree Preorder Traversal](#589easy-n-ary-tree-preorder-traversal)
    - [Problem](#problem-41)
    - [Solution: Recursion](#solution-recursion-11)
      * [Complexity](#complexity-65)
    - [Solution: Iteration with Stack](#solution-iteration-with-stack-3)
      * [Complexity](#complexity-66)
  + [[590/Easy] N-ary Tree Postorder Traversal](#590easy-n-ary-tree-postorder-traversal)
    - [Problem](#problem-42)
    - [Solution: Recursion](#solution-recursion-12)
      * [Complexity](#complexity-67)
    - [Solution: Iteration with Stack](#solution-iteration-with-stack-4)
      * [Complexity](#complexity-68)
  + [[695/Medium] Max Area of Island](#695medium-max-area-of-island)
    - [Solution: Recursive DFS](#solution-recursive-dfs-3)
      * [Complexity](#complexity-69)
    - [Solution: Iterative DFS](#solution-iterative-dfs)
      * [Complexity](#complexity-70)
  + [[721/Medium] Accounts Merge](#721medium-accounts-merge)
    - [Problem](#problem-43)
    - [Solution: DFS Iterative](#solution-dfs-iterative)
    - [Solution: DFS Recursion](#solution-dfs-recursion-2)
    - [Solution: BFS](#solution-bfs-1)
    - [Solution: Union-Find](#solution-union-find)
  + [[863/Medium] All Nodes Distance \(K\) in Binary Tree](#863medium-all-nodes-distance-k-in-binary-tree)
    - [Problem](#problem-44)
    - [Solution: BFS by converting tree to a bidirected graph](#solution-bfs-by-converting-tree-to-a-bidirected-graph)
      * [Complexity](#complexity-71)
    - [Solution: BFS + HashMap](#solution-bfs--hashmap)
      * [Complexity](#complexity-72)
    - [Solution: DFS](#solution-dfs)
      * [Complexity](#complexity-73)
  + [[865/1123/Medium] Smallest Subtree with all the Deepest Nodes / Lowest Common Ancestor of Deepest Leaves](#8651123medium-smallest-subtree-with-all-the-deepest-nodes--lowest-common-ancestor-of-deepest-leaves)
    - [Problem](#problem-45)
    - [Solution: DFS/Post-order traversal](#solution-dfspost-order-traversal)
      * [Complexity](#complexity-74)
  + [[889/Medium] Construct Binary Tree from Preorder and Postorder Traversal](#889medium-construct-binary-tree-from-preorder-and-postorder-traversal)
  + [Problem](#problem-46)
    - [Solution: Recursion](#solution-recursion-13)
      * [Complexity](#complexity-75)
  + [[938/Easy] Range Sum of BST](#938easy-range-sum-of-bst)
    - [Problem](#problem-47)
    - [Solution: Recursion](#solution-recursion-14)
      * [Complexity](#complexity-76)
    - [Solution: Recursive Backtracking/DFS](#solution-recursive-backtrackingdfs-2)
      * [Complexity](#complexity-77)
    - [Solution: Recursive Backtracking/DFS](#solution-recursive-backtrackingdfs-3)
      * [Complexity](#complexity-78)
    - [Solution: Iterative Backtracking/DFS + Stack](#solution-iterative-backtrackingdfs--stack-1)
      * [Complexity](#complexity-79)
  + [[987/Hard] Vertical Order Traversal of a Binary Tree](#987hard-vertical-order-traversal-of-a-binary-tree)
    - [Problem](#problem-48)
    - [Solution: BFS/DFS with Global Sorting](#solution-bfsdfs-with-global-sorting)
      * [Complexity](#complexity-80)
    - [Solution: BFS/DFS with Partition Sorting](#solution-bfsdfs-with-partition-sorting)
      * [Complexity](#complexity-81)
  + [[1087/Medium] Brace Expansion](#1087medium-brace-expansion)
    - [Problem](#problem-49)
    - [Solution: Backtracking/DFS](#solution-backtrackingdfs-14)
      * [Complexity](#complexity-82)
  + [[1382/Medium] Balance a Binary Search Tree](#1382medium-balance-a-binary-search-tree)
    - [Problem](#problem-50)
    - [Solution: Recursive in-order traversal + Rebuild](#solution-recursive-in-order-traversal--rebuild)
      * [Complexity](#complexity-83)
  + [[2002/Medium] Maximum Product of the Length of Two Palindromic Subsequences]](#2002medium-maximum-product-of-the-length-of-two-palindromic-subsequences)
    - [Problem](#problem-51)
    - [Solution: Recursive/Top-Down DP](#solution-recursivetop-down-dp)
    - [Solution: Recursive/Top-Down DP + Memoization](#solution-recursivetop-down-dp--memoization)
    - [Solution: Recursive/Top-Down DP + Memoization](#solution-recursivetop-down-dp--memoization-1)
      * [Complexity](#complexity-84)

## Pattern: Backtracking/DFS

* There are six types of DFS tree traversal:
  + Pre-order, NLR
  + In-order, LNR
  + Post-order, LRN
  + Reverse pre-order, NRL
  + Reverse in-order, RNL
  + Reverse post-order, RLN
* For more, refer [Wikipedia: Tree traversal](https://en.wikipedia.org/wiki/Tree_traversal).

### [17/Medium] Letter Combinations of a Phone Number

* Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
* A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

* Example 1:

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

* Example 2:

```
Input: digits = ""
Output: []
```

* Example 3:

```
Input: digits = "2"
Output: ["a","b","c"]
```

* Constraints:
  + `0 <= digits.length <= 4`
  + `digits[i] is a digit in the range ['2', '9'].`
* See [problem](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) on LeetCode.

#### Solution: Recursion

* One of the first things you should always do is look at the constraints. Quite often, you can figure out what sort of approach needs to be taken simply from looking at the input size. In an interview, asking your interviewer about the constraints will also show your attention to detail - on top of giving you information.
* In this particular problem, the length of the input is extremely small, `0 <= digits.length <= 4`. With such small input sizes, we can safely assume that a brute force solution in which we generate all combinations of letters will be accepted.
* Whenever you have a problem where you need to generate all combinations/permutations of some group of letters/numbers, the first thought you should have is backtracking. Backtracking algorithms can often keep the space complexity linear with the input size.

```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'}
            
        if len(digits) == 0:
            return []
            
        if len(digits) == 1:
            if digits[0] not in digit_map.keys():
                return []
                
            return [c for c in digit_map[digits[0]]]
            
        head_strs = [c for c in digit_map[digits[0]]]
        tail_combinations = self.letterCombinations(digits[1:])
        
        return [h + t for h in head_strs for t in tail_combinations]
```

##### Complexity

* Time: \(O(4^N \cdot N)\), where \(N\) is the length of `digits`. Note that 4 in this expression is referring to the maximum value length in the hash map, and not to the length of the input. The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to \(N\) to build the combination. This problem can be generalized to a scenario where numbers correspond with up to \(M\) digits, in which case the time complexity would be \(O(M^N \cdot N)\). For the problem constraints, we’re given, \(M = 4\), because of digits 7 and 9 having 4 letters each.
* Space: \(O(N)\), where \(N\) is the length of digits. Not counting space used for the output, the extra space we use relative to input size is the space occupied by the recursion call stack. It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack. As the hash map does not grow as the inputs grows, it occupies \(O(1)\) space.

#### Solution: Backtracking/DFS

* **Intuition**:
  + There aren’t any smart tricks needed for this problem - the hard part is just figuring out how to correctly generate all possible combinations, and to do this using a standard backtracking algorithm template. Let’s break down the problem, by starting with an input that is only 1-digit long, for example `digits = "2"`. This example is trivial - just generate all letters that correspond with `digit = "2"`, which would be `["a", "b", "c"]`.
  + What if instead we had a 2-digit long input, `digits = "23"`? Imagine taking each letter of `digit = "2"` as a starting point. That is, lock the first letter in, and solve all the possible combinations that start with that letter. If our first letter will always be “a”, then the problem is trivial again - it’s the 1-digit case, and all we have to do is generate all the letters corresponding with `digit = "3"`, and add that to “a”, to get `["ad", "ae","af"]`. This was easy because we ignored the first letter, and said it will always be “a”. But we know how to generate all the first letters too - it’s the 1-digit case which we already solved to be `["a", "b", "c"]`.
  + As you can see, solving the 1-digit case is trivial, and solving the 2-digit case is just solving the 1-digit case twice. The same reasoning can be extended to n digits. For the 3-digit case, solve the 2-digit case to generate all combinations of the first 2 letters, and then solve the 1-digit case for the final digit. Now that we know how to solve the 3-digit case, to solve the 4-digit case, solve the 3-digit case for all combinations of the first 3 letters, and then solve the 1-digit case for the final digit. We could extend this to infinity, but, don’t worry, for this problem we’re finished after 4.

* **Algorithm**:
  + As mentioned previously, we need to lock-in letters when we generate new letters. The easiest way to save state like this is to use recursion. Our algorithm will be as follows:
    - If the input is empty, return an empty array.
    - Initialize a data structure (e.g. a hash map) that maps digits to their letters, for example, mapping “6” to “m”, “n”, and “o”.
    - Use a backtracking function to generate all possible combinations.
      * The function should take 2 primary inputs: the current combination of letters we have, `path`, and the `index` we are currently checking.
      * As a base case, if our current combination of letters is the same length as the input `digits`, that means we have a complete combination. Therefore, add it to our answer, and backtrack.
      * Otherwise, get all the letters that correspond with the current digit we are looking at, `digits[index]`.
      * Loop through these letters. For each letter, add the letter to our current path, and call backtrack again, but move on to the next digit by incrementing `index` by 1.
      * Make sure to remove the letter from `path` once finished with it.

```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0: 
            return []
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations
```

##### Complexity

* Time: \(O(4^N \cdot N)\), where \(N\) is the length of `digits`. Note that 4 in this expression is referring to the maximum value length in the hash map, and not to the length of the input. The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to \(N\) to build the combination. This problem can be generalized to a scenario where numbers correspond with up to \(M\) digits, in which case the time complexity would be \(O(M^N \cdot N)\). For the problem constraints, we’re given, \(M = 4\), because of digits 7 and 9 having 4 letters each.
* Space: \(O(N)\), where \(N\) is the length of digits. Not counting space used for the output, the extra space we use relative to input size is the space occupied by the recursion call stack. It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack. As the hash map does not grow as the inputs grows, it occupies \(O(1)\) space.

### [39/Medium] Combination Sum

#### Problem

* Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.
* The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
* It is guaranteed that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.
* Example 1:

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

* Example 2:

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

* Example 3:

```
Input: candidates = [2], target = 1
Output: []
```

* Constraints:
  + `1 <= candidates.length <= 30`
  + `1 <= candidates[i] <= 200`
  + `All elements of candidates are distinct.`
  + `1 <= target <= 500`
* See [problem](https://leetcode.com/problems/combination-sum/) on LeetCode.

#### Solution: Backtracking/DFS

```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, index, path, res):
            if target < 0:
                # don't add to the path since we went negative
                return # backtracking
            
            # target matched; add to the path
            if not target:
                res.append(path)
                return # backtracking
            
            for i in range(index, len(candidates)):
                dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)
                
        res = []
        dfs(candidates, target, 0, [], res)
        return res
```

##### Complexity

* Time: \(O(n \* 2^n)\) since in each step, the number of subsets doubles as we add an additional element to the existing subsets, therefore, we will have a total of \(O(2^n)\) subsets, where \(n\) is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be \(O(n \* 2^n)\).
  + The reason the number of subsets doubles as we add each element to all the existing subsets is as follows:
    - Let’s start with [1] -> [[1]] (so number of subsets: 2); let’s add 2: [1, 2] -> [[1], [2], [1,2]] (so number of subsets: 4); let’s add 3: [1, 2, 3] -> [[1], [2], [3], [1,2], [1,3], [2,3], [1,3,2], [1,2,3]] (so number of subsets: 8); let’s add 4: [1, 2, 3, 4] -> [[1], [2], [3], [1,2], [2,3], [3,4], [1,3], [1,4], [2,4], [1,2,3], [2,3,4], [1,3,4], [1,3,2], [1,2,3,4]] (so number of subsets: 16);
* Space: \(O(n \* 2^n)\)

### [40/Medium] Combination Sum II

#### Problem

* Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to target.
* Each number in `candidates` may only be used once in the combination.
* Note: The solution set must not contain duplicate combinations.
* Example 1:

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

* Example 2:

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

* Constraints:
  + `1 <= candidates.length <= 100`
  + `1 <= candidates[i] <= 50`
  + `1 <= target <= 30`
* See [problem](https://leetcode.com/problems/combination-sum-ii) on LeetCode.

#### Solution: Backtracking/DFS

```
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, path, res):
            # early termination
            if target < 0:
                return # backtracking

            # early termination
            if not target:
                res.append(path) 
                return # backtracking

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                if nums[i] > target:
                    break
                # note that dfs() doesn't need the index parameter since this is taken care of by list slicing: "candidates[i+1:]"
                dfs(nums[i+1:], target - nums[i], path + [nums[i]], res)

        res = []
        candidates.sort()
        dfs(candidates, target, [], res)
        return res
```

##### Complexity

* Time: \(O(N \* 2^N)\) since in each step, the number of subsets doubles as we add each element to all the existing subsets, therefore, we will have a total of \(O(2^N)\) subsets, where \(N\) is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be \(O(N \* 2^N)\).
* Space: \(O(N \* 2^N)\)

### [46/Medium] Permutations

#### Problem

* Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.
* Example 1:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

* Example 2:

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

* Example 3:

```
Input: nums = [1]
Output: [[1]]
```

* Constraints:
  + `1 <= nums.length <= 6`
  + `-10 <= nums[i] <= 10`
* All the integers of `nums` are unique.
* See [problem](https://leetcode.com/problems/permutations/) on LeetCode.

#### Solution: Using the `itertools` library

```
def permute(self, nums):
    return list(itertools.permutations(nums))
```

* Note that returns a list of tuples. If needed, you could easily turn it into a list of lists:

```
def permute(self, nums):
    return map(list, itertools.permutations(nums))
```

#### Solution: Recursive, take any number as first

* Take any number as the first number and append any permutation of the other numbers.

```
def permute(self, nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
```

#### Solution: Recursive, insert first number anywhere

* Insert the first number anywhere in any permutation of the remaining numbers.

```
def permute(self, nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]
```

#### Solution: Reduce, insert next number anywhere

* Use reduce to insert the next number anywhere in the already built permutations.

```
def permute(self, nums):
    return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                                for p in P for i in range(len(p)+1)],
                  nums, [[]])
```

#### Solution: Recursion

```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
            
        elif len(nums) == 1:
            return [nums]
        
        ans = []
        for index in range(len(nums)):
            head = [nums[index]]
            tail = nums[0:index] + nums[index+1:]
            ans.extend([head + permutation for permutation in self.permute(tail)])
        
        return ans
```

#### Solution: Backtracking/DFS

```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            # when we have visited all the elements once
            if not nums:
                res.append(path)
                # return # backtracking

            # we can keep exploring to traverse all the possible paths
            for i in range(len(nums)):
                # skip nums[i] in the next traversal but add it to the path
                dfs(nums[:i] + nums[i+1:], path+[nums[i]], res)

        res = [] # to store the main result
        path = []
        dfs(nums, path, res) # or just send [] for path
        return res
```

* Note that the above solution accesses `num[len(nums)+1]` but that does not raise an `IndexError`. This is because the slicing operation doesn’t raise an error if both your start and stop indices are larger than the sequence length. This is in contrast to simple indexing —- if you index an element that is out of bounds, Python will throw an index out of bounds error. However, with slicing it simply returns an empty sequence.
* Same approach; rehashed:

```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(arr, curr_soln):
            # Our current route through the search space is finished
            if len(curr_soln) == n:
                ans.append(curr_soln[:])
                return
            # We can keep exploring
            for i in range(len(arr)):
                head = arr[i]
                tail = arr[0:i] + arr[i+1:]
                curr_soln.append(head)
                backtrack(tail, curr_soln)
                curr_soln.pop()
        
        backtrack(nums, [])
        return ans
```

##### Complexity

* Time: We know that there are a total of \(n!\) permutations of a set with \(n\) numbers. In the algorithm above, we are iterating through all of these permutations with the help of the two `for` loops. In each iteration, we go through all the current permutations to insert a new number in them. To insert a number into a permutation of size \(n\) will take \(O(n)\), which makes the overall time complexity of our algorithm \(O(n\*n!)\).
* Space: All the additional space used by our algorithm is for the result list and the queue to store the intermediate permutations. If you see closely, at any time, we don’t have more than \(n!\) permutations between the result list and the queue. Therefore the overall space complexity to store \(n!\) permutations each containing \(n\) elements will be \(O(n\*n!)\).

### [47/Medium] Permutations II

#### Problem

* Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in any order.
* Example 1:

```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

* Example 2:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

* Constraints:
  + `1 <= nums.length <= 8`
  + `-10 <= nums[i] <= 10`
* All the integers of `nums` are unique.
* See [problem](https://leetcode.com/problems/permutations/) on LeetCode.

#### Solution: Backtracking/DFS

```
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            if not nums and path not in res:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
                
        res = []
        dfs(nums, [], res)
        return res
```

##### Complexity

* Time: \(TODO\)
* Space: \(TODO\)

### [77/Medium] Combinations

#### Problem

* Given two integers `n` and `k`, return all possible combinations of `k` numbers out of the range `[1, n]`.
* You may return the answer in any order.
* Example 1:

```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

* Example 2:

```
Input: n = 1, k = 1
Output: [[1]]
```

* Constraints:
  + `1 <= n <= 20`
  + `1 <= k <= n`
* See [problem](https://leetcode.com/problems/combinations/) on LeetCode.

#### Solution: Using a library

* First the obvious solution - Python already provides this functionality and it’s not forbidden, so let’s take advantage of it.

```
from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))
```

#### Solution: Recursion

* But doing it yourself is more interesting, and not that hard. Here’s a recursive version.

```
class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
```

#### Solution: Iteration

* Here’s an iterative one:

```
class Solution:
    def combine(self, n, k):
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs
```

#### Solution: Reduce

* Same as that iterative one, but using reduce instead of a loop:

```
class Solution:
  def combine(self, n, k):
    return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)],
                  range(k), [[]])
```

#### Solution: Backtracking/DFS

```
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, k, path, res):
            if len(path) == k: # or if k == 0:
                res.append(path)
                return 
                
            for i in range(len(nums)):
                dfs(nums[i+1:], k, path+[nums[i]], res)                
                
        res = []
        dfs(range(1,n+1), k, [], res)
        return res
```

##### Complexity

* Time: TODO
* Space: TODO

### [78/Medium] Subsets

#### Problem

* Given an integer array `nums` of unique elements, return all possible subsets (the power set).
* The solution set must not contain duplicate subsets. Return the solution in any order.
* Example 1:

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

* Example 2:

```
Input: nums = [0]
Output: [[],[0]]
```

* Constraints:
  + `1 <= nums.length <= 10`
  + `-10 <= nums[i] <= 10`
  + `All the numbers of nums are unique.`
* See [problem](https://leetcode.com/problems/subsets/) on LeetCode.

#### Solution: Backtracking/DFS

```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, currentPath, answer):
            answer.append(currentPath)
                
            for i in range(len(nums)):
                dfs(nums[i+1:], currentPath + [nums[i]], answer)        
        
        answer = []
        dfs(nums, [], answer)
        return answer
```

##### Complexity

* Time: Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, therefore, we will have a total of \(O(2^N)\) subsets, where \(N\) is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be \(O(N\*2^N)\).
* Space: All the additional space used by our algorithm is for the output list. Since we will have a total of \(O(2^N)\) subsets, and each subset can take up to \(O(N)\) space, therefore, the space complexity of our algorithm will be \(O(N\*2^N)\).

### [90/Medium] Subsets II

#### Problem

* Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).
* The solution set must not contain duplicate subsets. Return the solution in any order.
* Example 1:

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

* Example 2:

```
Input: nums = [0]
Output: [[],[0]]
```

* Constraints:
  + `1 <= nums.length <= 10`
  + `-10 <= nums[i] <= 10`
* See [problem](https://leetcode.com/problems/subsets-ii/) on LeetCode.

#### Solution: Backtracking/DFS

```
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            if path not in res:
                res.append(path)

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], path + [nums[i]], res)
                
        res = []
        nums.sort()
        dfs(nums, [], res)
        return res
```

##### Complexity

* Time: TODO
* Space: TODO

### [91/Medium] Decode Ways

#### Problem

* A message containing letters from `A-Z` can be encoded into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

* To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, “11106” can be mapped into:

  + `"AAJF"` with the grouping `(1 1 10 6)`
  + `"KJF"` with the grouping `(11 10 6)`
* Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.
* Given a string `s` containing only digits, return the number of ways to decode it.
* The test cases are generated so that the answer fits in a 32-bit integer.
* Example 1:

```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

* Example 2:

```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

* Example 3:

```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

* Constraints:
  + `1 <= s.length <= 100`
  + `s contains only digits and may contain leading zero(s).`
* See [problem](https://leetcode.com/problems/decode-ways/) on LeetCode.

##### Solution: Bottom-up/Iterative DP

* The intuition here is that the problem asks us to calculate the number of ways to decode a certain string, but to do that, we have to calculate all possible subsequences present in the string. That will give us the number of different decodings. Hence the problem can be reduced down to finding the number of substrings in this string.
* Now, number of substrings of any substring can be found in two ways:
  + By using for loops(resulting in \(O(n^2)\))
  + By using dp: (resulting in \(O(n)\))
* The only change in this problem with the usual problem of substrings is that we have to take care of edge cases like `0` in front of a number, and use a map to map the values, instead of reporting the number directly.
* Algorithm:
  + The problem can also be modelled is essentially a variation of the `n-th` staircase problem with `n = [1, 2]` steps.
  + We generate a bottom up DP table, initialized to 0.
  + The tricky part is handling the corner cases (for e.g., s = “30”). Most elegant way to deal with those error/corner cases, is to allocate an extra space, `dp[0]`.
  + Let `dp[i]` denotes the number of decodings possible for (i.e., the number of ways to parse) the string `s[1: i]`, i.e., upto the `[i-1]`-th element of `s`. In other words, to calculate decoding upto `i-th` character of `s`, we need to know `dp[i+1]`. Hence, when we calculate `dp[len(s)]` or `dp[-1]`, it will give us the number of decodings till `s[len(s)-1]`, hence the answer.
    - `dp[i]` gives the number of decodings until the `[i-1]`-th element of `s` in consideration, and since we are considering till `s[i-1]`, hence only one letter can be placed at the end, resulting in new sequences. This is the number of sequences which are formed by using the last one character.
    - `dp[i-1]` gives the number of decodings until the `[i-2]`-th element of `s` in consideration, and since we are considering till `s[i-2]`, hence two letters can be placed at the end, resulting in new sequences. This is the number of sequences which are formed by using the last two characters.
    - `dp[i-2]` gives the number of decodings until the `[i-3]`-th element of `s` in consideration, and since we are considering till `s[i-3]`, hence three letters can be placed at the end, resulting in new sequences. This is the number of sequences which are formed by using the last three characters.
  + For example:
    - s = “231”
    - index 0: extra base offset. `dp[0] = 1`
    - index 1: # of ways to parse “2” => `dp[1] = 1`
    - index 2: # of ways to parse “23” => “2” and “23”, `dp[2] = 2`
    - index 3: # of ways to parse “231” => “2 3 1” and “23 1” => `dp[3] = 2`
  + For the edge cases:
    - If `s[i-1]==0` means that the last character cannot be used for making new decodings, as we don’t have code for 0, hence we test this condition using `if 1 <= int(s[i-1]) <= 9`
    - If the last two digits in consideration add up to give more than 26, we have the same problem as before with having no code assigned to them and hence no decodings possible for this case either. We check this using `if 10 <= int(s[i - 2] + s[i - 1]) <= 26`.
    - After these two edge cases, all conditions have been accounted for and we simply return the result.

```
def numDecodings(s): 
    if not s:
        return 0

    dp = [0 for x in range(len(s) + 1)] 
    
    # base case initialization
    dp[0] = 1 
    # the case of handling s starting with '0'. 
    # alternative: Treating as an error condition and immediately returning 0 is recommended. 
    # it's easier to keep track and it's an optimization.
    dp[1] = 0 if s[0] == "0" else 1

    for i in range(2, len(s) + 1): 
        # one step jump
        # pay close attention to the comparators. note that it is 0 <, not 0 <=. 
        if 0 < int(s[i - 1:i]) <= 9:
            dp[i] += dp[i - 1]
        # two step jump
        # pay close attention to the comparators. note that it is 10 <=, not 10 <
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
            
    return dp[len(s)]
```

##### Complexity

* Time: \(O(n)\)
* Space: $$O(n)$

#### Solution: One-liner

```
def numDecodings(self, s):
    return reduce(lambda(v,w,p),d:(w,(d>'0')*w+(9<int(p+d)<27)*v,d),s,(0,s>'',''))[1]*1
```

* More readable version:

```
def numDecodings(self, s):
    v, w, p = 0, int(s>''), ''
    for d in s:
        v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
    return w
```

* `w` tells the number of ways
* `v` tells the previous number of ways
* `d` is the current digit
* `p` is the previous digit

#### Solution: DP + DFS

* Build a tree of possible decoding scenarios you can obtain from a random string.
* The number of leaves in the tree essentially is the number of ways the string can be decoded.
* We are going to build our tree with DFS from our original string, trying to decode either as:
  + A single digit (and call `dfs` again with remaining string).
  + Both single digit and double digit, when the double digits are less than or equal to 26 (and call `dfs` again with remaining strings).
* Our base case is when we have only a single digit left in our string or when we have nothing left in the string. In that case, we return 1 back up the recursion stack.
* **Growing a tree**:

* **Dyanmic Programming**:
* We can see that this type of tree has a lot of redundant sub-trees. Dynamic Programming to the rescue!! (In the code below, we use `lru_cache` decorator which essentially memoizes the function calls with argument-returned value pairs. So, when we call the same function with same arguments, and if that recursive call has been made before, it is just retrieved from memoized pair).

* After you have got a hang of the thinking process, we will have to handle issues with zeros.
  + Zeros can be in the middle or at the start.
    - If it is at the start, there is no way to decode the string.
    - If it is in the middle:
      * If it can be paired with the digit before zero (and is less than or equal to 26, then we can keep on growing our subtrees)
      * If it cannot be paired with the digit before zero, we have to destory that subtree. This might even render the whole string undecodable.

```
class Solution:
    def numDecodings(self, s:str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None)
        def dfs(string):
            if len(string)>0:
                if string[0] == '0':
                    return 0
            if string == "" or len(string) == 1:
                return 1
            if int(string[0:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first+second
            else:
                return dfs(string[1:])

        result_sum = dfs(s)

        return result_sum
```

##### Complexity

* Time: \(O(n)\)
* Space: $$O(1)$

### [98/Medium] Validate Binary Search Tree

#### Problem

* Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
* A valid BST is defined as follows:
  + The left subtree of a node contains only nodes with keys less than the node’s key.
  + The right subtree of a node contains only nodes with keys greater than the node’s key.
  + Both the left and right subtrees must also be binary search trees.
* Example 1:

```
Input: root = [2,1,3]
Output: true
```

* Example 2:

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 104].`
  + `-2^31 <= Node.val <= 2^31 - 1`
* See [problem](https://leetcode.com/problems/validate-binary-search-tree/) on LeetCode.

#### Solution: Inorder traversal

* Inorder traversal leads to a sorted array if it is a valid Binary Search Tree (BST).

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low= -math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
                
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root)
```

* Cleaner solution:

```
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        # Empty trees are valid BSTs.
        if not node:
            return True        
        
        output = []
        self.inOrder(root, output)
        
        # Fun fact: Inorder traversal leads to a sorted array if it is 
        # a Valid Binary Search Tree.
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    # Time complexity of inorder traversal is O(n)
    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
```

#### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\) for `output`

### [94/Easy] Binary Tree Inorder Traversal

#### Problem

* Given the `root` of a binary tree, return the inorder traversal of its nodes’ values.
* Example 1:

```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

* Example 2:

```
Input: root = []
Output: []
```

* Example 3:

```
Input: root = [1]
Output: [1]
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 100].`
  + `-100 <= Node.val <= 100`
* Follow up: Recursive solution is trivial, could you do it iteratively?
* See [problem](https://leetcode.com/problems/binary-tree-inorder-traversal/) on LeetCode.

#### Solution: Iteration with Stack

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Convert BST to ascending sequence
        '''            
        output, stack = [], []
   
        while stack or root:
            if root:
                stack.append(root)
                root =root.left
            else:
                temp =stack.pop()
                output.append(temp.val)
                root= temp.right
           
        return output
```

#### Solution: Recursion

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node, nums):
            '''
            Convert BST to ascending sequence
            '''    
            if node:
                inorder(node.left, nums)
                nums.append(node.val)
                inorder(node.right, nums)
        
        nums = []            
        inorder(root, nums)
        return nums
```

#### Solution: Recursive one-liner

```
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
```

* Related: pre-order traversal:

```
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
```

* Related: post-order traversal:

```
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [102/Easy] Binary Tree Postorder Traversal

#### Problem

* Given the `root` of a binary tree, return the postorder traversal of its nodes’ values. (i.e., from left to right, level by level).

* Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

* Example 2:

```
Input: root = [1]
Output: [[1]]
```

* Example 3:

```
Input: root = []
Output: []
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 2000].`
  + `-1000 <= Node.val <= 1000`
* See [problem](https://leetcode.com/problems/binary-tree-level-order-traversal/) on LeetCode.

#### Solution: Recursion with List

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output =[]
        self.dfs(root, 0, output)
        return output
    
    def dfs(self, root, level, output):
        
        if not root:
            return
        
        if len(output) < level+1:
            output.append([])
            
        output[level].append(root.val)    
        self.dfs(root.left, level+1, output)
        self.dfs(root.right, level+1, output)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

#### Solution: Iteration with Queue

* A binary tree level order traversal generally recommends a breadth first search (BFS) approach with the use of a queue data structure. When we process a node (`curr`), we’ll push the node’s children onto the end of the queue in the order in which we want to traverse (in this case, left to right). In this way, we’ll have finished putting the next row in the queue at the same time we finish iterating through this row.
* To help us keep track of the rows, we just nest the main loop inside another loop. At the beginning of the outer loop, we capture the queue length, which will tell us how long the row is. Then we can iterate through that many nodes, popping them off the queue’s front one at a time, then process any end-of-row instructions. In the case of this problem, that will mean pushing the current row array (`row`) onto our answer array (`ans`).
* We’ll continue this process until the `queue` is empty, at which point we will have reached the end of the binary tree, and can return `ans`.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, ans = deque([root] if root else []), []
        
        while len(queue):
            row = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                row.append(curr.val)
                
                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
                    
            ans.append(row)
            
        return ans
```

##### Complexity

* Time: \(O(n)\) where \(n\) is the number of nodes in the binary tree
* Space: \(O(n)\) for `ans`

### [102/Easy] Binary Tree Zigzag Level Order Traversal

#### Problem

* Given the `root` of a binary tree, return the zigzag level order traversal of its nodes’ values. (i.e., from left to right, then right to left for the next level and alternate between).

* Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

* Example 2:

```
Input: root = [1]
Output: [[1]]
```

* Example 3:

```
Input: root = []
Output: []
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 2000].`
  + `-1000 <= Node.val <= 1000`
* See [problem](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) on LeetCode.

#### Solution: Recursion with List

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        self.dfs(root, 0, output)
        
        for i in range(len(output)):
            if i % 2 !=0:
                output[i].reverse()
            else:
                continue
        return output
    
    def dfs(self, root, level, output):
        if root is None:
            return
        
        if len(output) < level+1:
            output.append([])
        
        output[level].append(root.val)
        self.dfs(root.left, level+1, output)
        self.dfs(root.right, level+1, output)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

#### Solution: Iteration with Deque

* Using the double ended queue functionality. We `pop` from left for odd levels and `pop` from right for even levels. Trick is to flip the order of left and right when we are appending from left.

```
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: 
        return []
    queue = collections.deque([root])
    res = []
    even_level = False
    
    while queue:
        n = len(queue)
        level = []
        for i in range(n):
            if even_level:
                # pop from right and append from left.
                node = queue.pop()
                # to maintain the order of nodes in the format of [left, right, left, right] 
                # we push right first since we are appending from left
                if node.right: queue.appendleft(node.right)
                if node.left: queue.appendleft(node.left)
            else:
                # pop from left and append from right
                node = queue.popleft()
                # here the order is maintained in the format [left, right, left, right] 
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level.append(node.val)
        res.append(level)
        even_level = not even_level
        
    return res
```

##### Complexity

* Time: \(O(n)\) where \(n\) is the number of nodes in the binary tree
* Space: \(O(n)\) for `ans`

### [105/Medium] Construct Binary Tree from Preorder and Inorder Traversal

#### Problem

* Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the `inorder` traversal of the same tree, construct and return the binary tree.
* Example 1:

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

* Example 2:

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

* Constraints:
  + `1 <= preorder.length <= 3000`
  + `inorder.length == preorder.length`
  + `-3000 <= preorder[i], inorder[i] <= 3000`
  + `preorder and inorder consist of unique values.`
  + `Each value of inorder also appears in preorder.`
  + `preorder is guaranteed to be the preorder traversal of the tree.`
  + `inorder is guaranteed to be the inorder traversal of the tree.`
* See [problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) on LeetCode.

#### Solution: Recursion

* Explanation:
  + Consider this input:

  ```
    preorder: [1, 2, 4, 5, 3, 6]
    inorder: [4, 2, 5, 1, 6, 3]
  ```

  + The obvious way to build the tree is:
    1. Use the first element of `preorder`, the `1`, as `root`.
    2. Search it in `inorder`.
    3. Split `inorder` by it, here into `[4, 2, 5]` and `[6, 3]`.
    4. Split the rest of `preorder` into two parts as large as the `inorder` parts, here into `[2, 4, 5]` and `[3, 6]`.
    5. Use `preorder = [2, 4, 5]` and `inorder = [4, 2, 5]` to add the left subtree.
    6. Use `preorder = [3, 6]` and `inorder = [6, 3]` to add the right subtree.
* Detailed explanation:
  + Recall preorder and inorder traversal:

    - The reason we are given two types of binary tree traversals is because it is not possible to construct binary tree from a single traversal. The following two different trees have the same preorder traversal but are not the same tree because they have a different structure.
    - The following two different trees have the same inorder traversal but are not the same tree because they have a different structure.
    - Thus these traversals on there own are not guaranteed to map to a unique binary tree. Our solution should always create the same binary tree for a given input. To put another way, there is only one possible solution for each input.
  + Building the tree:
    - Recall a preorder traversal visits nodes in the order of `root, left, right`.
    - Recall an inorder traversal visits nodes in the order of `left, root, right`.
  + Thus, the root of the subtree will always be the first element in preorder. To construct the left subtree, we take all the nodes to the left of the root value (from `inorder`). To construct the right subtree, we take all the nodes to the right of the root (from `inorder`).
  + Implementation details:
    - The tree is constructed in a recursive depth-first manner (recursion tree below). Two separate recursive calls are made for left and right subtree respectively.
    - At each recursive call we only look at nodes that are potential candidates for later subtrees. When we go the left, we only want nodes from both `inorder` and `preorder` that reside in the left subtree. same for when we go to the right.
      * For the `inorder` array,
        + Going to the left, we want all nodes to the left of the root. that is `inorder[:root_index]`
        + Going to the right, we want all nodes to the right of the root. that is `inorder[root_index + 1:]`
      * For the `preorder` array,
        + Going to the left, we want all nodes that could eventually become a root, for a left subtree.
        + Going to the right, we want all nodes that could eventually become a root, for a right subtree.
    - We use the root\_index from the `inorder` array, because `preorder` cannot provide us with unambiguous information about which nodes reside in the left and right subtrees.
    - We know excluding the root value in `preorder` (`preorder[0]`), some set of nodes must belong to the right, and some set of nodes most belong to the left.
    - It turns out that the `root_index` from inorder corresponds to the last element in the `preorder` array that belongs to the left subtree. This is because inorder traversal visits nodes in the order `left, root, right` .
      * Left: `preorder[1:root_index + 1]`
      * Right: `preorder[root_index + 1:]`

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:        
        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        # Get root from preorder
        root = TreeNode(preorder[0])
        
        # Get index of the root in inorder
        root_index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        
        return root
```

* Similar approach; simplified:

  + Consider the worst case for this: A tree that’s not balanced but is just a straight line to the left. Then `inorder` is the reverse of `preorder`, and already the cost of step 2, searching in `inorder`, is `O(n^2)` overall. Also, depending on how you “split” the arrays, you’re looking at `O(n^2)` runtime and possibly `O(n^2)` space for that as well.
  + You can bring the runtime for searching down to `O(n)` by building a map from value to index before you start the main work, and I’ve seen several solutions do that. But that is `O(n)` additional space, and also the splitting problems remain. To fix those, you can use pointers into `preorder` and `inorder` instead of splitting them. And when you’re doing that, you don’t need the value-to-index map, either.
  + Consider the example again. Instead of finding the `1` in `inorder`, splitting the arrays into parts and recursing on them, just recurse on the full remaining arrays and stop when you come across the `1` in `inorder`. That’s what the above solution does. Each recursive call gets told where to stop, and it tells its subcalls where to stop. It gives its own root value as stopper to its left subcall and its parent`s stopper as stopper to its right subcall.
  + P.S.: We’re popping elements from `preorder` and `inorder`. Since popping from the front with `pop(0)` is expensive `O(n)`, we reverse them before we start so we can use the cheap `O(1)` popping from the back.

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
            
    preorder.reverse()
    inorder.reverse()
    
    return build(None)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [106/Medium] Construct Binary Tree from Inorder and Postorder Traversal

#### Problem

* Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.
* Example 1:

```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

* Example 2:

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

* Constraints:
  + `1 <= preorder.length <= 3000`
  + `inorder.length == preorder.length`
  + `-3000 <= preorder[i], inorder[i] <= 3000`
  + `preorder and inorder consist of unique values.`
  + `Each value of inorder also appears in preorder.`
  + `preorder is guaranteed to be the preorder traversal of the tree.`
  + `inorder is guaranteed to be the inorder traversal of the tree.`
* See [problem](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) on LeetCode.

#### Solution: Recursion

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder or not inorder:
            return None

        if len(postorder) == 1:
            return TreeNode(postorder[-1])            
            
        root_index = inorder.index(postorder.pop())
        root = TreeNode(inorder[root_index])
        
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:])
        
        return root
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [107/Medium] Binary Tree Level Order Traversal II

#### Problem

* Given the `root` of a binary tree, return the bottom-up level order traversal of its nodes’ values. (i.e., from left to right, level by level from leaf to root).

* Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

* Example 2:

```
Input: root = [1]
Output: [[1]]
```

* Example 3:

```
Input: root = []
Output: []
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 2000].`
  + `-1000 <= Node.val <= 1000`
* See [problem](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) on LeetCode.

#### Solution: Recursion with List

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        self.dfs(root, 0, output)
        return output[::-1]
    
    def dfs(self, root, level, output):
        if root is None:
             return
            
        if len(output) < level+1:
            output.append([])
            
        output[level].append(root.val)
        self.dfs(root.left, level+1, output)
        self.dfs(root.right, level+1, output)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

#### Solution: Iteration with Queue

* A binary tree level order traversal generally recommends a breadth first search (BFS) approach with the use of a queue data structure. When we process a node (`curr`), we’ll push the node’s children onto the end of the queue in the order in which we want to traverse (in this case, left to right). In this way, we’ll have finished putting the next row in the queue at the same time we finish iterating through this row.
* To help us keep track of the rows, we just nest the main loop inside another loop. At the beginning of the outer loop, we capture the queue length, which will tell us how long the row is. Then we can iterate through that many nodes, popping them off the queue’s front one at a time, then process any end-of-row instructions. In the case of this problem, that will mean pushing the current row array (`row`) onto our answer array (`ans`).
* We’ll continue this process until the `queue` is empty, at which point we will have reached the end of the binary tree, and can return `ans[::-1]`.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue, ans = deque([root] if root else []), []
        
        while len(queue):
            row = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                row.append(curr.val)
                
                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
                    
            ans.append(row)
            
        return ans[::-1]
```

##### Complexity

* Time: \(O(n)\) where \(n\) is the number of nodes in the binary tree
* Space: \(O(n)\) for `ans`

### [108/Easy] Convert Sorted Array to Binary Search Tree

#### Problem

* Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
* A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
* Example 1:

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

* Example 2:

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

* Constraints:
  + `1 <= nums.length <= 104`
  + `-104 <= nums[i] <= 104`
  + `nums is sorted in a strictly increasing order.`
* See [problem](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) on LeetCode.

#### Solution: DFS with list slicing

* The idea is to find the root first, then recursively build each left and right subtree:

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Convert ascending sequence to balanced BST
        '''
        if len(nums) == 0: # Our list is empty
            return None
        if len(nums) == 1: # Our list has only one element
            return TreeNode(nums[0])

        # Here is one illustration before the code:
        # Assuming that we already have a sorted list : [1, 2, 5, 7, 9, 12, 14]
        # The middle value is 7, which is also our very first root
        # root.left will apply the same thought recursively with a sorted list: [1, 2, 5]
        # root.right will apply the same thought recursively with a sorted list: [9, 12, 14]
        # Below is the final code:

        mid = len(nums) // 2
        new_node = TreeNode(nums[mid])
        new_node.left = self.sortedArrayToBST(nums[:mid])
        new_node.right = self.sortedArrayToBST(nums[mid+1:])
        return new_node
```

* This might be nice and easy to code up, but the asymptotic complexity is bad. Since Python slicing takes \(O(n)\) where `n` is the size of the slice, therefore this algorithm has runtime \(O(n\log{n})\), space \(O(n)\), whereas it could be done in \(O(n)\) runtime and \(O(\log{n})\) space complexity if passing indices of the start and end of string instead of the slices directly.

##### Complexity

* Time: \(O(n\log{n})\) where \(n\) is the number of nodes in the binary tree
* Space: \(O(n)\)

#### Solution: DFS with list indices

* The previous solution use slices to split the list; however, it takes \(O(n)\) to slice, making the entire algorithm \(O(n\log{n})\). Therefore, we create a helper function to pass in the bounds of the array instead, making it \(O(n)\):

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, lower, upper):
        if lower == upper:
            return None

        mid = (lower + upper) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, lower, mid)
        node.right = self.helper(nums, mid+1, upper)

        return node
```

* Please note the if `lower == upper: return None` statement – since we are passing in bounds, `nums` will never be None. Therefore, we check if the lower and upper bounds are the same for our base case.

##### Complexity

* Time: \(O(n)\) where \(n\) is the number of nodes in the binary tree
* Space: \(O(\log{n})\)

### [124/Hard] Binary Tree Maximum Path Sum

#### Problem

* A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
* The path sum of a path is the sum of the node’s values in the path.
* Given the `root` of a binary tree, return the maximum path sum of any non-empty path.
* Example 1:

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

* Example 2:

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 3 * 104].`
  + `-1000 <= Node.val <= 1000`
* See [problem](https://leetcode.com/problems/binary-tree-maximum-path-sum/) on LeetCode.

#### Solution: Backtracking/DFS

* Basics:

* Base cases:

* Important Observations:
  + These important observations are very important to understand line 9 and 10 in the code.
  + For example, in the code (`Line 9`), we do something like `max(get_max_gain(node.left), 0)`. The important part is: why do we take maximum value between 0 and maximum gain we can get from left branch? Why 0? Check the two images below first.
  + The important thing is “We can only get any sort of gain IF our branches are not below zero. If they are below zero, why do we even bother considering them? Just pick 0 in that case. Therefore, we do `max(<some gain we might get or not>, 0)`.
* Going down the recursion stack for one example:

  + Because of this, we do line 12 and 13. It is important to understand the different between looking for the maximum path INVOLVING the current node in process and what we return for the node which starts the recursion stack. Line 12 and 13 take care of the former issue and Line 15 (and the image below) takes care of the latter issue.
  + Because of this fact, we have to return like line 15. For our example, for node 1, which is the recursion call that node 3 does for `max(get_max_gain(node.left), 0)`, node 1 cannot include both node 6 and node 7 for a path to include node 3. Therefore, we can only pick the max gain from left path or right path of node 1.

```
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
     max_path = float("-inf") # placeholder to be updated
     def get_max_gain(node):
         nonlocal max_path # This tells that max_path is not a local variable
         if node is None:
             return 0
             
         gain_on_left = max(get_max_gain(node.left), 0) # Read the part important observations
         gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations
             
         current_max_path = node.val + gain_on_left + gain_on_right # Read first three images of going down the recursion stack
         max_path = max(max_path, current_max_path) # Read first three images of going down the recursion stack
             
         return node.val + max(gain_on_left, gain_on_right) # Read the last image of going down the recursion stack
             
     get_max_gain(root) # Starts the recursion chain
     return max_path
```

* Same approach; rehashed:

```
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxPath(root):
            nonlocal maxSum
            if not root:
                return 0
            
            left = maxPath(root.left)
            right = maxPath(root.right)
            maxSum = max(maxSum, left + right + root.val)
            return max(left + root.val, right + root.val, 0)
        
        maxSum = -math.inf # or -float('inf')
        maxPath(root)
        return maxSum
```

```
class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxSum
    
    def dfs(self, root):
        if not root:
            return float('-inf')
        
        sumLeft = self.dfs(root.left)
        sumRight = self.dfs(root.right)
        
        self.maxSum = max(self.maxSum, 
                               sumLeft, 
                               sumRight, 
                               root.val, 
                               sumLeft + root.val + sumRight,
                               sumLeft + root.val,
                               sumRight + root.val)
        
        return root.val + max(sumLeft, sumRight, 0)
```

### [129/Medium] Sum Root to Leaf Numbers

#### Problem

* You are given the `root` of a binary tree containing digits from `0` to `9` only.
* Each root-to-leaf path in the tree represents a number.

  + For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.
* Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
* A leaf node is a node with no children.
* Example 1:

```
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

* Example 2:

```
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 1000].`
  + `0 <= Node.val <= 9`
  + `The depth of the tree will not exceed 10.`
* See [problem](https://leetcode.com/problems/sum-root-to-leaf-numbers/) on LeetCode.

#### Solution: Recursive DFS

* DFS traversal with leaf node judgement.
  + A node is a leaf node if `node.left` is `None` and `node.right` is `None`.
* Step 1:
  + Start DFS traversal from root node and initial tree number 0.
  + Update tree number with current node value on each level.
* Step 2:
  + If current node is leaf node, return tree number.
  + If current node is non-leaf node, DFS down to next level with summation (+).

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, node: Optional[TreeNode], tree_num = 0) -> int:
        if not node:
            # empty tree or empty node
            return 0
        
        # update tree_num with current node
        tree_num = 10 * tree_num + node.val

        if not node.left and not node.right:
            # leaf is reached, return tree_num
            return tree_num
        else:
            # DFS down to next level
            return self.sumNumbers(node.left, tree_num) + self.sumNumbers(node.right, tree_num)
```

#### Solution: BFS with Queue

```
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]): # BFS with queue
        deque, res = collections.deque(), 0
        
        if root:
            deque.append(root)
            
        while deque:
            node = deque.popleft()
            
            if not node.left and not node.right:
                res += node.val
                
            if node.left:
                node.left.val += node.val*10
                deque.append(node.left)
                
            if node.right:
                node.right.val += node.val*10
                deque.append(node.right)
                
        return res
```

#### Solution: DFS with Stack

```
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]): # DFS with stack
        stack, res = [], 0
        
        if root:
            stack.append(root)
            
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res += node.val
                
            if node.right:
                node.right.val += node.val*10
                stack.append(node.right)
                
            if node.left:
                node.left.val += node.val*10
                stack.append(node.left)
                
        return res
```

### [131/Medium] Palindrome Partitioning

#### Problem

* Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.
* A palindrome string is a string that reads the same backward as forward.
* Example 1:

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

* Example 2:

```
Input: s = "a"
Output: [["a"]]
```

* Constraints:
  + `1 <= s.length <= 16`
* See [problem](https://leetcode.com/problems/palindrome-partitioning/) on LeetCode.

#### Solution: Backtracking/DFS

* **Overview**:
  + The aim is to partition the string into all possible palindrome combinations. To achieve this, we must generate all possible substrings of a string by partitioning at every index until we reach the end of the string. Example, `abba` can be partitioned as `["a","ab","abb","abba"]`. Each generated substring is considered as a potential candidate if it a Palindrome.
* **Intuition**:
  + The idea is to generate all possible substrings of a given string and expand each possibility if is a potential candidate. The first thing that comes to our mind is Depth First Search. In Depth First Search, we recursively expand potential candidate until the defined goal is achieved. After that, we backtrack to explore the next potential candidate.
  + Backtracking incrementally build the candidates for the solution and discard the candidates (backtrack) if it doesn’t satisfy the condition.
  + The backtracking algorithms consists of the following steps:
    - \(Choose:\) Choose the potential candidate. Here, our potential candidates are all substrings that could be generated from the given string.
    - \(Constraint:\) Define a constraint that must be satisfied by the chosen candidate. In this case, the constraint is that the string must be a palindrome.
    - \(Goal:\) We must define the goal that determines if we have found the required solution and we must backtrack. Here, our goal is achieved if we have reached the end of the string.
* **Algorithm**:
  + In the backtracking algorithm, we recursively traverse over the string in depth-first search fashion. For each recursive call, the beginning index of the string is given as \(start\).
  + Iteratively generate all possible substrings beginning at \(start\) index. The \(end\) index increments from \(start\) till the end of the string.
  + For each of the substrings generated, check if it is a palindrome.
  + If the substring is a palindrome, the substring is a potential candidate. Add substring to the \(currentPath\) and perform a depth-first search on the remaining substring. If current substring ends at index \(end\), \(end+1\) becomes the \(start\) index for the next recursive call.
  + Backtrack if \(start\) index is greater than or equal to the string length and add the \(currentPath\) to the result.

```
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, output, currentPath):
            if not s:
                # reached the end of the string? add currentPath to the output
                output.append(currentPath)
                return
            
            for i in range(1, len(s)+1):
                if isPal(s[:i]):
                    # if s[:i] is a palindrome, add it to currentPath
                    # and work on the substring after index i
                    dfs(s[i:], output, currentPath+[s[:i]])
                
        def isPal(s):
            return True if s == s[::-1] else False
            
        output = []
        dfs(s, output, [])
        return output
```

##### Complexity

* Time: \(O(n \cdot 2^{n})\), where \(n\) is the length of string \(s\). This is the worst-case time complexity when all the possible substrings are palindrome.
  + Example, if = s = `aaa`, the recursive tree can be illustrated as follows:
  + Hence, there could be \(2^{n}\) possible substrings in the worst case. For each substring, it takes \(O(n)\) time to generate substring and determine if it a palindrome or not. This gives us time complexity as \(O(n \cdot 2^{n})\)
* Space: \(O(n)\), where \(n\) is the length of the string \(s\). This space will be used to store the recursion stack. For s = `aaa`, the maximum depth of the recursive call stack is 3 which is equivalent to \(n\).

### [133/Medium] Clone Graph

#### Problem

* Given a reference of a node in a connected undirected graph.
* Return a deep copy (clone) of the graph.
* Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

* Test case format:
* For simplicity, each node’s value is the same as the node’s index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.
* An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
* The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
* Example 1:

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

* Example 1:

```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

* Example 3:

```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

* Constraints:
  + `The number of nodes in the graph is in the range [0, 100].`
  + `1 <= Node.val <= 100`
  + `Node.val is unique for each node.`
  + `There are no repeated edges and no self-loops in the graph.`
  + `The Graph is connected and all nodes can be visited starting from the given node.`
* See [problem](https://leetcode.com/problems/clone-graph/) on LeetCode.

#### Solution: BFS + Queue

* Use a dict to map original nodes to their clones `{node: clone_node}`. This dict also serves as a visited set to make sure you don’t loop indefinitely during DFS/BFS.

```
class Solution(object):
    def cloneGraph(self, node: 'Node') -> 'Node':
         if not node: return
         # map original nodes to their clones
         d = {node : Node(node.val)}
         q = deque([node])
        
         while q:
             for i in range(len(q)):
                 currNode = q.popleft()
                 for neigh in currNode.neighbors:
                     if neigh not in d:
                         # store copy of the neighboring node
                         d[neigh] = Node(neigh.val)
                         q.append(neigh)
                     # connect the node copy at hand to its neighboring nodes (also copies)
                     d[currNode].neighbors.append(d[neigh])
        
         # return copy of the starting node
         return d[node]
```

#### Solution: Iterative Backtracking/DFS + Stack

* Use a dict to map original nodes to their clones `{node: clone_node}`. This dict also serves as a visited set to make sure you don’t loop indefinitely during DFS/BFS.

```
class Solution(object):
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return
        d = {node: Node(node.val)}
        stack = [node]
        
        while stack:
            curNode = stack.pop()
            for neigh in curNode.neighbors:
                if neigh not in d:
                    # store copy of the neighboring node
                    d[neigh] = Node(neigh.val)
                    stack.append(neigh)
                # connect the node copy at hand to its neighboring nodes (also copies)                    
                d[neigh].neighbors.append(d[curNode])

        # return copy of the starting node 
        return d[node]
```

#### Solution: Recursive Backtracking/DFS

* Use a dict to map original nodes to their clones and set to store the visited nodes.

```
class Solution(object):
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(n, m, visited):
            if n in visited:
                return
                
            visited.add(n)
            
            if n not in m:
                m[n] = Node(n.val)
            
            for neigh in n.neighbors:
                if neigh not in m:
                    # store copy of the neighboring node
                    m[neigh] = Node(neigh.val)
                # connect the node copy at hand to its neighboring nodes (also copies)    
                m[n].neighbors.append(m[neigh])
                dfs(neigh, m, visited)
                
        if not node:
            return node
        m, visited = dict(), set()
        dfs(node, m, visited)
        
        # return copy of the starting node
        return m[node]
```

### [140/Hard] Word Break II

#### Problem

* Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
* Note that the same word in the dictionary may be reused multiple times in the segmentation.
* Example 1:

```
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

* Example 2:

```
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
```

* Example 3:

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
```

* Constraints:
  + `1 <= s.length <= 20`
  + `1 <= wordDict.length <= 1000`
  + `1 <= wordDict[i].length <= 10`
  + `s and wordDict[i] consist of only lowercase English letters.`
  + `All the strings of wordDict are unique.`
* See [problem](https://leetcode.com/problems/word-break-ii) on LeetCode.

#### Solution: DP/Memoization

1. Every time, we check whether `s` starts with a word. If so, we check whether the substring `s[len(word):]` starts with a word, etc.
2. `resultOfTheRest` is updated by successive recursive calls to `helper` calling until we hit the last word. If the last word is in the dict, we append it to res. The last word is `dog ==> 'res = ["dog"]`.
3. This time, we skip `else`, since we fulfill the condition `if len(word) == len(s)`. We store it in memo: `{'dog': ['dog']}`
4. Then we return to `resultOfTheRest = self.helper(s[len(word):], wordDict, memo)`
   `s = "sanddog"` because we start with “cat” (cat is the first word in the dict) and “cat” leads to “sand”.

   ```
   resultOfTheRest = ["dog"]
   word = "sand"
   item = "sand dog"
   res = ["sand dog"]
   memo ={'dog': ['dog'], "sanddog":["sand dog"] }
   ```
5. Why do we need `memo`?
   * We always recurse to the last word in the string and backtrack, so storing all possible combinations of the substring in the memo saves time for the next iteration of the whole string. For example, “catsanddog,” if we don’t store “dog,” then we have to iterate through the dictionary. This is very DP.
6. Using a print statement to print “s” below “for word in wordDict:”

   ```
   s catsanddog
   s sanddog
   s sanddog
   s sanddog
   s sanddog
   s dog
   s dog
   s dog
   s dog
   s dog
   {'dog': ['dog']}
   res ['sand dog']
   s sanddog
   {'dog': ['dog'], 'sanddog': ['sand dog']}
   res ['cat sand dog']
   s catsanddog
   s anddog
   s anddog
   s anddog
   res ['and dog']
   s anddog
   s anddog
   {'dog': ['dog'], 'sanddog': ['sand dog'], 'anddog': ['and dog']}
   res ['cat sand dog', 'cats and dog']
   s catsanddog
   s catsanddog
   s catsanddog
   {'dog': ['dog'], 'sanddog': ['sand dog'], 'anddog': ['and dog'], 'catsanddog': ['cat sand dog', 'cats and dog']}
   ```

```
class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(s: str, wordDict: List[str], memo: Dict) -> List[str]:
            if s in memo: return memo[s]
            if not s: return []
            
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    res.append(word)
                else:
                    resultOfTheRest = helper(s[len(word):], wordDict, memo)
                    for item in resultOfTheRest:
                        item = word + ' ' + item
                        res.append(item)
            memo[s] = res
            return res

        return helper(s, wordDict, {})
```

* Removing the nested function structure (and using a default argument for “memo” as a hack) also works:

```
class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str], memo: Dict = {}) -> List[str]:
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if s.startswith(word):
                if len(word) == len(s):
                    res.append(word)
                else:
                    resultOfTheRest = self.wordBreak(s[len(word):], wordDict, memo)
                    for item in resultOfTheRest:
                        res += [word + ' ' + item] # item = word + ' ' + item; res.append(item)
        memo[s] = res
        return res
```

#### Solution: DP + Python’s LRUCache

* Recursion using python’s built-in `lru_cache` caching decorator and minimizing the parameters passed between helper function calls:

```
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(maxsize=None)
        def dp(i):
            res = []
            for word in wordDict:
                if word != s[i:i+len(word)]:
                    continue
                elif len(word) == len(s)-i:
                    res.append(word)
                else:
                    for sentence in dp(i+len(word)):
                        res.append(word + ' ' + sentence)        
            return res
        
        return dp(0)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\) because of memoization.

#### Solution: Backtracking/DFS

```
class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def dfs(idx, path):
            if (len(s) == idx):
                res.append(' '.join(path))
                
            for i in range(idx, len(s)):   
                tmp = s[idx:i+1]
                if (tmp in wordDict):
                    dfs(i+1, path+[tmp])

        dfs(0, [])
        return res
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

### [144/Easy] Binary Tree Preorder Traversal

#### Problem

* Given the `root` of a binary tree, return the preorder traversal of its nodes’ values.

* Example 1:

```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

* Example 2:

```
Input: root = []
Output: []
```

* Example 3:

```
Input: root = [1]
Output: [1]
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 100].`
  + `-100 <= Node.val <= 100`
* Follow up: Recursive solution is trivial, could you do it iteratively?
* See [problem](https://leetcode.com/problems/binary-tree-preorder-traversal/) on LeetCode.

#### Solution: Recursive one-liner

* In postorder traversal, the order should be `root -> left -> right`.

```
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

#### Solution: Recursion

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output =[]
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
        
        output.append(root.val)
        self.dfs(root.left, output)
        self.dfs(root.right, output)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: Iteration with Stack

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack = [root]
        
        while stack:
            temp = stack.pop()
            if temp:
                output.append(temp.val)
                
                # note that because we're using a stack, the order is reversed: R -> L
                stack.append(temp.right)
                stack.append(temp.left)
        
        return output
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

### [145/Easy] Binary Tree Postorder Traversal

#### Problem

* Given the `root` of a binary tree, return the postorder traversal of its nodes’ values.

* Example 1:

```
Input: root = [1,null,2,3]
Output: [3,2,1]
```

* Example 2:

```
Input: root = []
Output: []
```

* Example 3:

```
Input: root = [1]
Output: [1]
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 100].`
  + `-100 <= Node.val <= 100`
* Follow up: Recursive solution is trivial, could you do it iteratively?
* See [problem](https://leetcode.com/problems/binary-tree-postorder-traversal/) on LeetCode.

#### Solution: Recursive one-liner

* In preorder traversal, the order should be `left -> right -> root`.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

#### Solution: Recursion

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
            
        self.dfs(root.left, output)
        self.dfs(root.right, output) 
        output.append(root.val)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: Iteration with Stack

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack = [root]
        
        if not root:
            return None
        
        # iterate only when there are elements inside the stack
        while stack:
            
            # pop the element from stack and stored it into temp
            temp = stack.pop()
            
            # append the value of temp to output
            output.append(temp.val)
            
            # Now traverse through left node and add the node to stack
            if temp.left:
                stack.append(temp.left)
                
            # else traverse through right node and add to stack
            if temp.right:
                stack.append(temp.right)
        
        # After iterating through the stack,  print the result in reverse order.  
        return output[::-1]
    
    
        # Example: Iteration 1 : #stack=[1] - first iteration, temp =1, 
            #output[1]
            #temp.left is Null
            #temp.right is [2]
            # stack =[2]
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

### [173/Medium] Binary Search Tree Iterator

##### Problem

* Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):

  + `BSTIterator(TreeNode root)` Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
  + boolean `hasNext()` Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
  + `int next()` Moves the pointer to the right, then returns the number at the pointer.
* Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
* You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.
* Example 1:

```
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 105].`
  + `0 <= Node.val <= 106`
  + `At most 105 calls will be made to hasNext, and next.`
* See [problem](https://leetcode.com/problems/binary-search-tree-iterator/) on LeetCode.

##### Solution

```
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val
        
    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
```

### [199/Medium] Binary Tree Right Side View

#### Problem

* Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
* Example 1:

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

* Example 2:

```
Input: root = [1,null,3]
Output: [1,3]
```

* Example 3:

```
Input: root = []
Output: []
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 100].`
  + `-100 <= Node.val <= 100`
* See [problem](https://leetcode.com/problems/binary-tree-right-side-view/) on LeetCode.

#### Solution: DFS, combine right and left

* Compute the right view of both right and left left subtree, then combine them. For very unbalanced trees, this can be `O(n^2)`, though.

```
class Solution(object):
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        
        return [root.val] + right + left[len(right):]
```

##### Complexity

* Time: \(O(n)\) average case; \(O(n^2)\) worst case
* Space: \(O(1)\)

#### Solution: BFS/Level-order, iterative

* Traverse the tree level-by-level and add the last value of each level to the view. This is `O(n)`.

```
class Solution(object):
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
                
        return view
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: BFS with Deque

```
class Solution(object):
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deque = collections.deque()
        
        if root:
            deque.append(root)
            
        res = []
        while deque:
            size, val = len(deque), 0
            for _ in range(size):
                node = deque.popleft()
                val = node.val # store last value in each level
                if node.left:
                    deque.append(node.left)
                    
                if node.right:
                    deque.append(node.right)
            res.append(val)
            
        return res
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: DFS, first come first serve

* DFS-traverse the tree right-to-left, add values to the view whenever we first reach a new record depth. This is `O(n)`.

```
class Solution(object):
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                    
                collect(node.right, depth+1)
                collect(node.left, depth+1)
                
        view = []
        collect(root, 0)
        return view
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [212/Hard] Word Search II

* Given an `m x n` board of characters and a list of strings words, return all words on the board.
* Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
* Example 1:

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

* Example 2:

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

* Constraints:
  + `m == board.length`
  + `n == board[i].length`
  + `1 <= m, n <= 12`
  + `board[i][j] is a lowercase English letter.`
  + `1 <= words.length <= 3 * 104`
  + `1 <= words[i].length <= 10`
  + `words[i] consists of lowercase English letters.`
  + `All the strings of words are unique.`
* See [problem](https://leetcode.com/problems/word-search-ii/) on LeetCode.

#### Solution: DFS/Backtracking with Trie

* **Intuition**:
  + The problem is actually a simplified crossword puzzle game, where the word solutions have been given on the board embedded with some noise letters. All we need to to do is to cross them out.
    > Intuitively, in order to cross out all potential words, the overall strategy would be to iterate the cell one by one, and from each cell we walk along its neighbors in four potential directions to find matched words. While wandering around the board, we would stop the exploration when we know it would not lead to the discovery of new words.
  + One might have guessed the paradigm that we would use for this problem. Yes, it is backtracking, which would be the backbone of the solution. It is fairly simply to construct a solution of backtracking.
  + The key of the solution lies on how we find the matches of word from the dictionary. Intuitively, one might resort to the hashset data structure (for e.g., `set()` in Python). This could work.
  + However, during the backtracking process, one would encounter more often the need to tell if there exists any word that contains certain prefix, rather than if a string exists as a word in the dictionary. Because if we know that there does not exist any match of word in the dictionary for a given prefix, then we would not need to further explore certain direction. And this, would greatly reduce the exploration space, therefore improve the performance of the backtracking algorithm.
  + The capability of finding matching prefix is where the data structure called Trie would shine, comparing the hashset data structure. Not only can Trie tell the membership of a word, but also it can instantly find the words that share a given prefix. As it turns out, the choice of data structure (Trie vs. hashset), which could end with a solution that ranks either the top \(5\%\) or the bottom \(5\%\).
  + Here we show an example of Trie that is built from a list of words. As one can see from the following graph, at the node denoted `d`, we would know there are at least two words with the prefix d from the dictionary.
  + We have a problem about implementing a Trie data structure. One can start with the Trie problem as warm up, and come back this problem later.
* **Algorithm**:
  + The overall workflow of the algorithm is intuitive, which consists of a loop over each cell in the board and a recursive function call starting from the cell. Here is the skeleton of the algorithm.
  + We build a Trie out of the words in the dictionary, which would be used for the matching process later.
  + Starting from each cell, we start the backtracking exploration (i.e., `backtracking(cell)`), if there exists any word in the dictionary that starts with the letter in the cell.
  + During the recursive function call `backtracking(cell)`, we explore the neighbor cells (i.e., `neighborCell`) around the current cell for the next recursive call `backtracking(neighborCell)`. At each call, we check if the sequence of letters that we traverse so far matches any word in the dictionary, with the help of the Trie data structure that we built at the beginning.
  + Here is an overall impression how the algorithm works. We give some sample implementation based on the rough idea above. And later, we detail some optimization that one could further apply to the algorithm.

```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ROW,COL = len(board), len(board[0])
        #to keep track of duplication, dont revisit
        result, visited = set(), set()
        
        def dfs(r,c,trieNode,wordSoFar):
            #base case
            if (r < 0 or c < 0 or 
                r == ROW or c == COL or
                board[r][c] not in trieNode.children or (r, c) in visited):
                return
            
            #mark position as visited
            visited.add((r, c))
            #update node because we know it exists
            trieNode = trieNode.children[board[r][c]]
            #update word with new character we just reached
            wordSoFar += board[r][c]
            
            #add if we found the word
            if trieNode.isWord:
                result.add(wordSoFar)
            
            #else run dfs
            dfs(r-1, c, trieNode, wordSoFar)
            dfs(r+1, c, trieNode, wordSoFar)
            dfs(r, c+1, trieNode, wordSoFar)
            dfs(r, c-1, trieNode, wordSoFar)
            
            #remove for backtracking
            visited.remove((r, c))
            
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,root,"")
        return list(result)
```

* Rephrased:

```
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords
```

#### Optimizations

* In the above implementation, we applied a few tricks to further speed up the running time, in addition to the application of the Trie data structure. In particular, the Python implementation could run faster than 98% of the submissions. We detail the tricks as follows, ordered by their significance.

  > Backtrack along the nodes in Trie.

  + One could use Trie simply as a dictionary to quickly find the match of words and prefixes, i.e., at each step of backtracking, we start all over from the root of the Trie. This could work.
  + However, a more efficient way would be to traverse the Trie together with the progress of backtracking, i.e., at each step of `backtracking(TrieNode)`, the depth of the TrieNode corresponds to the length of the prefix that we’ve matched so far. This measure could lift your solution out of the bottom \(5\%\) of submissions.
  > Gradually prune the nodes in Trie during the backtracking.

  + The idea is motivated by the fact that the time complexity of the overall algorithm sort of depends on the size of the Trie. For a leaf node in Trie, once we traverse it (i.e., find a matched word), we would no longer need to traverse it again. As a result, we could prune it out from the Trie.
  + Gradually, those non-leaf nodes could become leaf nodes later, since we trim their children leaf nodes. In the extreme case, the Trie would become empty, once we find a match for all the words in the dictionary. This pruning measure could reduce up to \(50\%\) of the running time for the test cases of the online judge.
  > Keep words in the Trie.

  + One might use a flag in the Trie node to indicate if the path to the current code match any word in the dictionary. It is not necessary to keep the words in the Trie.
  + However, doing so could improve the performance of the algorithm a bit. One benefit is that one would not need to pass the prefix as the parameter in the `backtracking()` call. And this could speed up a bit the recursive call. Similarly, one does not need to reconstruct the matched word from the prefix, if we keep the words in Trie.
  > Remove the matched words from the Trie.

  + In the problem, we are asked to return all the matched words, rather than the number of potential matches. Therefore, once we reach certain Trie node that contains a match of word, we could simply remove the match from the Trie.
  + As a side benefit, we do not need to check if there is any duplicate in the result set. As a result, we could simply use a list instead of set to keep the results, which could speed up the solution a bit.

##### Complexity

* Time: \(\mathcal{O}(m(4\cdot3^{l-1}))\), where \(m\) is the number of cells in the board and \(l\) is the maximum length of words.

  + It is tricky is calculate the exact number of steps that a backtracking algorithm would perform. We provide a upper bound of steps for the worst scenario for this problem. The algorithm loops over all the cells in the board, therefore we have \(M\) as a factor in the complexity formula. It then boils down to the maximum number of steps we would need for each starting cell (i.e., \(4\cdot3^{L-1}4\)).
  + Assume the maximum length of word is \(l\), starting from a cell, initially we would have at most 4 directions to explore. Assume each direction is valid (i.e. worst case), during the following exploration, we have at most 3 neighbor cells (excluding the cell where we come from) to explore. As a result, we would traverse at most \(4\cdot3^{l-1}4\) cells during the backtracking exploration.
  + One might wonder what the worst case scenario looks like. Well, here is an example. Imagine, each of the cells in the board contains the letter `a`, and the word dictionary contains a single word `['aaaa']`. Voila. This is one of the worst scenarios that the algorithm would encounter.
  + Note that, the above time complexity is estimated under the assumption that the Trie data structure would not change once built. If we apply the optimization trick to gradually remove the nodes in Trie, we could greatly improve the time complexity, since the cost of backtracking would reduced to zero once we match all the words in the dictionary, i.e. the Trie becomes empty.
* Space: \(mathcal{O}(n)\), where \(n\) is the total number of letters in the dictionary.

  + The main space consumed by the algorithm is the Trie data structure we build. In the worst case where there is no overlapping of prefixes among the words, the Trie would have as many nodes as the letters of all words. And optionally, one might keep a copy of words in the Trie as well. As a result, we might need \(2n\) space for the Trie.

### [226/Easy] Invert Binary Tree

* Given the `root` of a binary tree, invert the tree, and return its root.
* Example 1:

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

* Example 2:

```
Input: root = [2,1,3]
Output: [2,3,1]
```

* Example 3:

```
Input: root = []
Output: []
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 100].`
  + `-100 <= Node.val <= 100`
* See [problem](https://leetcode.com/problems/invert-binary-tree) on LeetCode.

#### Solution: Recursive Pre-Order Traversal DFS

* In a recursive call:
  + If `node` is `null` or `None` return (base case for recursion).
  + Create a `temp` variable to keep the right child.
  + Update the node’s right child with the left.
  + Update the node’s left child with the temp variable.
  + Finally, return the `node`.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(head):
            if head is None:
                return
                
            temp = head.left
            head.left = head.right
            head.right = temp
            
            reverse(head.left)
            reverse(head.right)
            
            return head
        return reverse(root)
```

* Concise (with no `temp` variable and nested function):

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\) for callstacks

#### Solution: Iterative Pre-Order Traversal DFS with Queue

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = collections.deque([root])
   
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            
            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
        
        return root
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\) for `queue`

### [230/Medium] Kth Smallest Element in a BST

#### Problem

* Given the `root` of a binary search tree, and an integer `k`, return the `k-th` smallest value (1-indexed) of all the values of the nodes in the tree.
* Example 1:

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

* Example 2:

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

* Constraints:
  + `The number of nodes in the tree is n.`
  + `1 <= k <= n <= 104`
  + `0 <= Node.val <= 104`
* Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
* See [problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) on LeetCode.

#### Solution: Iterative inorder traversal with a Deque of length `k`

* Loop through array `k` times, every time put the largest index in visited. Uses \(O(k)\) space by using a “stack” cut off at `k` elements.

```
class Solution(object):
    def kthSmallest(self, root, k):
        dq = collections.deque(maxlen=k)
        
        while True: # or while root or stack:
            while root:
                dq.append(root)
                root = root.left
            root = dq.pop()
        
            if k == 1: # count down; could count up as well (if i == k)
                return root.val
            k -= 1 # count down; could count up as well (i=0; i+=1)
        
            # or
            # k -= 1 # count down; could count up as well (i=0; i+=1)
            # if k == 0: # count down; could count up as well (if i == k)
            #     return root.val
                        
            root = root.right
```

##### Complexity

* Time: \(O(n)\) worst-case since you have to go through the entire tree if the tree is completely “left-leaning” (only left children, no right children). \(O(max(h, k))\) average case.
* Space: \(O(k)\)

#### Solution: Recursion

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, node: Optional[TreeNode]):
        if not node:
            return
            
        self.helper(node.left)
        
        self.k -= 1 # count down; could count up as well (i=0; i+=1)
        if self.k == 0: # count down; could count up as well (if i == k)
            self.res = node.val
            return
        
        self.helper(node.right)
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        self.helper(root)
        return self.res
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(k)\)

### [235/Medium] Lowest Common Ancestor of a Binary Search Tree

#### Problem

* Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
* According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
* Example 1:

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

* Example 2:

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

* Example 3:

```
Input: root = [2,1], p = 2, q = 1
Output: 2
```

* Constraints:
  + `The number of nodes in the tree is in the range [2, 105].`
  + `-109 <= Node.val <= 109`
  + `All Node.val are unique.`
  + `p != q`
  + `p and q will exist in the BST.`
* See [problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) on LeetCode.

#### Solution: DFS Recursion

* We can solve this using the approaches to find [LCA in a binary tree](#236medium-lowest-common-ancestor-of-a-binary-tree).
* But, binary search tree’s property could be utilized, to come up with a better algorithm.
* Lets review properties of a BST:
  + Left subtree of a node N contains nodes whose values are lesser than or equal to node N’s value.
  + Right subtree of a node N contains nodes whose values are greater than node N’s value.
  + Both left and right subtrees are also BSTs.
* **Intuition**:
  + Lowest common ancestor for two nodes p and q would be the last ancestor node common to both of them. Here last is defined in terms of the depth of the node. The below diagram would help in understanding what lowest means.
  + Note: One of p or q would be in the left subtree and the other in the right subtree of the LCA node.
  + Following cases are possible:
* **Algorithm**:
  + Start traversing the tree from the root node.
  + If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
  + If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
  + If both step 2 and step 3 are not true, this means we have found the node which is common to node \(p\)’s and \(q\)’s subtrees. and hence we return this common node as the LCA.

```
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        return root
```

##### Complexity

* Time: \(O(n)\), where \(n\) is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
* Space: \(O(n)\). This is because the maximum amount of space utilized by the recursion stack would be \(n\) since the height of a skewed BST could be \(n\).

#### Solution: DFS Iteration

* **Algorithm**:
  + The steps taken are also similar to approach 1. The only difference is instead of recursively calling the function, we traverse down the tree iteratively. This is possible without using a stack or recursion since we don’t need to backtrace to find the LCA node. In essence of it the problem is iterative, it just wants us to find the split point. The point from where \(p\) and \(q\) won’t be part of the same subtree or when one is the parent of the other.

```
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node
```

##### Complexity

* Time: \(O(n)\), where \(n\) is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
* Space: \(O(1)\).

### [Medium] Lowest Common Ancestor of a Binary Tree (without Root Node)

#### Problem

* Given two nodes of a binary tree (that has a parent node pointer in each node), find the lowest common ancestor (LCA) of two given nodes in the tree.
* According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes \(p\) and \(q\) as the lowest node in \(T\) that has both \(p\) and \(q\) as descendants (where we allow a node to be a descendant of itself).”
* Note that two nodes may have more than one common ancestor, however, they can have only one lowest common ancestor.
* Example 1:

```
Input: f, g
Output: The nodes  f  and  g  have  e  as their lowest common ancestor
```

#### Solution: Iteration

* In this method we will iterate from the node `a` to the root of the tree, while saving the ancestors of the node in a vector. Next, we will iterate from the node `b` to the root of the tree and determine whether the ancestors of `a` appear in the ancestors of `b`. The first ancestor of `b` which is also an ancestor of a will be the lowest common ancestor. This method will require a total of two traversals of the binary tree.

```
class Node:
    def __init__(self,val):
        self.val = val
        self.left_Node = None
        self.right_Node = None
        self.Parent = None

class BinaryTree:
    def __init__(self,val):
        self.root = Node(val)

def lowest_common_ancestor(node1, node2):
    ancestor_node1 = [] # use slice to store the ancestor of node1 
    
    curr = node1 
    while curr:
        curr = curr.Parent
        if curr:
            ancestor_node1.append(curr) # add ancestors of node1
          
    curr = node2
    while curr:
        curr = curr.Parent
        for i in range(0, len(ancestor_node1)): # find out if the most immediate ancestor of node1 is also the common ancestor of node2
            if ancestor_node1[i] == curr:
                print ("The nodes ", node1.val," and ", node2.val," have ", curr.val," as their lowest common ancestor")
                return curr 
         
    return None

def main():
    # making the Binary tree structure shown above.
    BST = BinaryTree('d')

    BST.root.left_Node = Node('c')
    BST.root.left_Node.Parent = BST.root
    BST.root.right_Node = Node('e')
    BST.root.right_Node.Parent = BST.root

    BST.root.left_Node.left_Node = Node('a')
    BST.root.left_Node.left_Node.Parent = BST.root.left_Node
    BST.root.left_Node.right_Node = Node('b')
    BST.root.left_Node.right_Node.Parent = BST.root.left_Node

    BST.root.right_Node.left_Node = Node('f')
    BST.root.right_Node.left_Node.Parent = BST.root.right_Node
    BST.root.right_Node.right_Node = Node('g')
    BST.root.right_Node.right_Node.Parent = BST.root.right_Node

    result = lowest_common_ancestor(BST.root.right_Node.left_Node,BST.root.right_Node.right_Node)

if __name__ == "__main__":
    main()
```

##### Complexity

* Time: This method will require a total of two traversals of the binary tree. So the Time-Complexity will be \(O(2h) ≈ O(h)\) where \(h\) is the height of the tree.
* Space: This method will store the ancestors of node a in a vector. So in the worst-case scenario, \(a\)is the leaf of the tree at the greatest depth. So a would have \(h\) ancestors. The Space-Complexity would hence be \(O(h)\).

#### Solution: Recursion

* In this method we will use recursion to reduce the time required to find the lowest common ancestor. We will start from the root and traverse the tree towards the leaves. This method uses four if conditions.
  + If the current node is NULL then we will return NULL since we have reached the end of the tree.
  + If the current node matches nodes `a` or `b`, we will return the current node.
  + If the current node has node `a` in its left subtree and b in its right subtree or vice versa then the current node will be the lowest common ancestor.
  + If the current node has nodes `a` and `b` exclusively in its left subtree or right subtree, then we will return the left or right subtree accordingly.

```
class Node:
    def __init__(self,val):
        self.val = val
        self.left_Node = None
        self.right_Node = None
        self.Parent = None

class BinaryTree:
    def __init__(self, val):
        self.root = Node(val)

def lowest_common_ancestor(curr, node1, node2):
    if curr == None:
        return None
    elif curr == node1 or curr == node2:
        return curr

    left_subtree = lowest_common_ancestor(curr.left_Node, node1, node2)
    right_subtree = lowest_common_ancestor(curr.right_Node, node1, node2)

    if left_subtree and right_subtree:
        return curr
    elif left_subtree:
        return left_subtree
    else:
        return right_subtree

def main():
    BST = BinaryTree('d')

    BST.root.left_Node = Node('c')
    BST.root.left_Node.Parent = BST.root
    BST.root.right_Node = Node('e')
    BST.root.right_Node.Parent = BST.root

    BST.root.left_Node.left_Node = Node('a')
    BST.root.left_Node.left_Node.Parent = BST.root.left_Node
    BST.root.left_Node.right_Node = Node('b')
    BST.root.left_Node.right_Node.Parent = BST.root.left_Node

    BST.root.right_Node.left_Node = Node('f')
    BST.root.right_Node.left_Node.Parent = BST.root.right_Node
    BST.root.right_Node.right_Node = Node('g')
    BST.root.right_Node.right_Node.Parent = BST.root.right_Node

    result = lowest_common_ancestor(BST.root,BST.root.right_Node.left_Node,BST.root.right_Node.right_Node)
    print ("The lowest common ancestor of nodes ", BST.root.right_Node.left_Node.val," and ", BST.root.right_Node.right_Node.val, " is : ", result.val)

if __name__ == "__main__":
    main()
```

##### Complexity

* Time: This method will require one traversal of the binary tree. So the Time-Complexity will be \(O(m+n) ≈ O(n)\) where \(m\) is the number of edges and \(n\) is the total number of nodes.
* Space: Another advantage of this method is that it does not use any data structure to store the ancestors of the nodes `a` and `b`. Hence, the space-complexity will be \(O(n)\).

#### Solution: DFS Iteration (Post-order Traversal with a Stack)

* Same algorithm as the [recursive solution](#solution-recursion-2), but iterative. Do a post-order traversal with a stack. Each stack element at first is a `[node, parent]` pair, where parent is the stack element of the node’s parent node.
* When the children of a parent get finished, their results are appended to their parent’s stack element. So when a parent gets finished, we have the results of its children/subtrees available (its stack element at that point is `[node, parent, resultForLeftSubtree, resultForRightSubtree]`).

```
def lowestCommonAncestor(self, root, p, q):
    answer = []
    stack = [[root, answer]]
    
    while stack:
        top = stack.pop()
        (node, parent), subs = top[:2], top[2:]
        
        if node in (None, p, q):
            parent += node,
        elif not subs:
            stack += top, [node.right, top], [node.left, top]
        else:
            parent += node if all(subs) else max(subs),
            
    return answer[0]
```

##### Complexity

* Time: TODO
* Space: TODO

#### Solution: Iteration (Path-building and finding the last node where the paths match)

* Here, we find the paths to `p` and `q` using a path-building technique and then find the last node where the paths match.

```
def lowestCommonAncestor(self, root, p, q):
    def path(root, goal):
        path, stack = [], [root]
        
        while True:
            node = stack.pop()
            
            if node:
                if node not in path[-1:]:
                    path += node,
                    if node == goal:
                        return path
                    stack += node, node.right, node.left
                else:
                    path.pop()
                    
    return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)
```

##### Complexity

* Time: TODO
* Space: TODO

### [236/Medium] Lowest Common Ancestor of a Binary Tree

#### Problem

* Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
* According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
* Example 1:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

* Example 2:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

* Example 3:

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

* Constraints:
  + `The number of nodes in the tree is in the range [2, 105].`
  + `-109 <= Node.val <= 109`
  + `All Node.val are unique.`
  + `p != q`
  + `p and q will exist in the tree.`
* See [problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) on LeetCode.

#### Solution: DFS Recursion One-liner

* If the current (sub)tree contains both `p` and `q`, then the function result is their LCA. If only one of them is in that subtree, then the result is that one of them. If neither are in that subtree, the result is `None`.

```
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right
```

* Or using that `None` is considered smaller than any node:

```
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    subs = [self.lowestCommonAncestor(kid, p, q)
            for kid in (root.left, root.right)]
    return root if all(subs) else max(subs)
```

##### Complexity

* Time: \(O(n)\), where \(n\) is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
* Space: \(O(n)\). This is because the maximum amount of space utilized by the recursion stack would be \(n\) since the height of a skewed BST could be \(n\).

#### Solution: DFS Iteration (Post-order Traversal with a Stack)

* Same algorithm as the [recursive solution](#solution-dfs-recursion), but iterative. Do a post-order traversal with a stack. Each stack element at first is a `[node, parent]` pair, where parent is the stack element of the node’s parent node.
* When the children of a parent get finished, their results are appended to their parent’s stack element. So when a parent gets finished, we have the results of its children/subtrees available (its stack element at that point is `[node, parent, resultForLeftSubtree, resultForRightSubtree]`).

```
def lowestCommonAncestor(self, root, p, q):
    answer = []
    stack = [[root, answer]]
    
    while stack:
        top = stack.pop()
        (node, parent), subs = top[:2], top[2:]
        
        if node in (None, p, q):
            parent += node,
        elif not subs:
            stack += top, [node.right, top], [node.left, top]
        else:
            parent += node if all(subs) else max(subs),
            
    return answer[0]
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\) for `stack`

#### Solution: DFS Iteration (Path-building and finding the last node where the paths match)

* Here, we find the paths to `p` and `q` using a path-building technique and then find the last node where the paths match.

```
def lowestCommonAncestor(self, root, p, q):
    def path(root, goal):
        path, stack = [], [root]
        
        while True:
            node = stack.pop()
            if node:
                if node not in path[-1:]:
                    path += node,
                    if node == goal:
                        return path
                    stack += node, node.right, node.left
                else:
                    path.pop()
                    
    return next(a for a, b in zip(path(root, p), path(root, q))[::-1] if a == b)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\) for `stack`

#### Solution: DFS Recursion

* The logic here is to check for every node, whether `p` or `q` belong to that root’s subtree.
* If the root is equal to either `p` or `q`, we know that the root is definitely one of it’s ancestors. We simply return it.
* One important point to note is that for a given root, if `p` or `q` are part of the current subtree, we return `root`, implying that that is an ancestor. If not, we return `None`. We do this recursively on the left and right subtrees of a given root.
* If both `left` and `right` return a non-`None` value, we know that’s the lowest common ancestor.
* If `left` returns `None` and right returns non-`None`, we know that the answer lies within the right subtree. Or if left returns non-`None` and `right` returns `None`, we know that the answer lies within the left subtree.

```
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
                
        # Find p/q in left subtree
        leftRes = self.lowestCommonAncestor(root.left, p, q)
        
        # Find p/q in right subtree
        rightRes = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in left and right subtree of this node, 
        # or root == p or root == q,
        # then this node is LCA
        if leftRes and rightRes or root in (p, q):
            return root
        
        # Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
        return leftRes or rightRes # or return leftRes if leftRes else rightRes
```

##### Complexity

* Time: \(O(n)\), where \(n\) is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
* Space: \(O(n)\). This is because the maximum amount of space utilized by the recursion stack would be \(n\) since the height of a skewed BST could be \(n\).

### [257/Easy] Binary Tree Paths

#### Problem

* Given the `root` of a binary tree, return all root-to-leaf paths in any order.
* A leaf is a node with no children.
* Example 1:

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

* Example 2:

```
Input: root = [1]
Output: ["1"]
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 100].`
  + `-100 <= Node.val <= 100`
* See [problem](https://leetcode.com/problems/binary-tree-paths/) on LeetCode.

#### Solution: Preorder traversal

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        
        result = []
        self.dfs(root, "", result)
        return result

    def dfs(self, root, path, result):
        if not root.left and not root.right:
            result.append(path + str(root.val))
        
        if root.left:
            self.dfs(root.left, path + str(root.val) + "->" , result)
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->", result)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

### [282/Hard] Expression Add Operators

#### Problem

* Given a string `num` that contains only digits and an integer target, return all possibilities to insert the binary operators ‘+’, ‘-‘, and/or ‘\*’ between the digits of `num` so that the resultant expression evaluates to the target value.
* Note that operands in the returned expressions should not contain leading zeros.
* Example 1:

```
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
```

* Example 2:

```
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
```

* Example 3:

```
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
```

* Constraints:
  + `1 <= num.length <= 10`
  + `num consists of only digits.`
  + `-2^31 <= target <= 2^31 - 1`
* See [problem](https://leetcode.com/problems/expression-add-operators/) on LeetCode.

#### Solution: Backtracking/DFS

```
class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        def dfs(idx=0, path='', value=0, prev=None):  
            if idx == len(num) and value == target:
                rtn.append(path)
                return
            
            for i in range(idx+1, len(num) + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
                    if prev is None :
                        dfs(i, num[idx: i], tmp, tmp)
                    else:
                        dfs(i, path+'+'+num[idx: i], value + tmp, tmp)
                        dfs(i, path+'-'+num[idx: i], value - tmp, -tmp)
                        dfs(i, path+'*'+num[idx: i], value - prev + prev*tmp, prev*tmp)
        
        rtn = []
        dfs()
        
        return rtn
```

#### Solution: Backtracking/DFS

* It’s the same idea as [Basic Calculator II](#227medium-basic-calculator-ii) using stack.
  + If the operator is `+` or `-`, push to stack as is.
  + If the operator is `*`, pop the stack and multiply it by the current number, then push the result to the stack.

```
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        size = len(num)
        
        def solve(index: int, stack: list = None, built: str = None) -> List[str]:
            if index >= size:
                if sum(stack) == target:
                    return [built]
                else:
                    return []
            
            res = []
            
            for i in range(index + 1, size + 1):
                ns = num[index: i]
                if ns[0] == '0' and i - index > 1:
                    break
                    
                n = int(ns)
                
                if index == 0:
                    res += solve(i, stack=[n], built=ns)
                else:
                    res += solve(i, stack=stack + [n], built=built + '+' + ns)
                    res += solve(i, stack=stack + [-n], built=built + '-' + ns)
                    res += solve(i, stack=stack[:-1] + [stack[-1] * n], built=built + '*' + ns)
                
            return res
        
        return solve(0)
```

### [297/Hard] Serialize and Deserialize Binary Tree

#### Problem

* Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
* Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
* Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
* Example 1:

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

* Example 2:

```
Input: root = []
Output: []
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 104].`
  + `-1000 <= Node.val <= 1000`
* See [problem](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) on LeetCode.

#### Solution: Recursive DFS preorder traversal

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # take care of base cases
        # if a node is empty, add 'x' to string
        # you can set 'x' to any mark as you want 
        if not root: 
            return 'x'
            
        # preorder(Root->left->right)
        # ex,
        #     1
        #    / \
        #   2   3
        #      / \
        #     4   5 
        # 
        # return (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
        # if you look at the return statement very closely, it is actually very intuitive
        # for value 1, you have 2 as left child and 3 as right child
        # for value 2, you have 'x'(None) as left child and 'x'(None) as right child which indicates it is a leaf node    
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])    
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #######################INTUITION#########################
        # The initial data string will be something like below:
        # (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
        # if you loop through string: 
        # 1                                 -> this is node value
        # (2, 'x', 'x')                     -> this is node left
        # (3, (4, 'x', 'x'), (5, 'x', 'x')) -> this is node right
        ######################################################## 
        # always take care of base case: if the node's value is 'x' then return None
        self.data = data
        
        if self.data[0] == 'x': 
            return None
        
        # create new treenode for node value
        node = TreeNode(self.data[:self.data.find(',')]) 

        # recursively unpack the string value
        node.left = self.deserialize(self.data[self.data.find(',')+1:])
        node.right = self.deserialize(self.data[self.data.find(',')+1:])

        # return the new TreeNode that we just created
        return node
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```

* Note that the reason `self.data` in used in `deserialize` is that data stream will be consumed as we build left side of Tree. By the time when the right side is building up, we need to hold what is left over. Therefore, self.data is a global value, right side will use what is left over after tree is partially built.

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

### [332/Hard] Reconstruct Itinerary

#### Problem

* You are given a list of airline tickets where `tickets[i] = [from_i, to_i]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
* All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

  + For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
* You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
* Example 1:

```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

* Example 2:

```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
```

* Constraints:
  + `1 <= tickets.length <= 300`
  + `tickets[i].length == 2`
  + `fromi.length == 3`
  + `toi.length == 3`
  + `fromi and toi consist of uppercase English letters.`
  + `fromi != toi`
* See [problem](https://leetcode.com/problems/reconstruct-itinerary/) on LeetCode.

#### Solution: Recursive DFS

* Just Eulerian path. Greedy DFS, building the route backwards when retreating.
* Algorithm:
  + First keep going forward until you get stuck. That’s a good main path already.
  + Remaining tickets form cycles which are found on the way back and get merged into that main path.
  + By writing down the path backwards when retreating from recursion, merging the cycles into the main path is easy - the end part of the path has already been written, the start part of the path hasn’t been written yet, so just write down the cycle now and then keep backwards-writing the path.
* Example:

* From JFK we first visit `JFK -> A -> C -> D -> A`. There we’re stuck, so we write down `A` as the end of the route and retreat back to `D`. There we see the unused ticket to `B` and follow it: `D -> B -> C -> JFK -> D`. Then we’re stuck again, retreat and write down the airports while doing so: Write down `D` before the already written `A`, then `JFK` before the `D`, etc. When we’re back from our cycle at `D`, the written route is `D -> B -> C -> JFK -> D -> A`. Then we retreat further along the original path, prepending `C`, `A` and finally `JFK` to the route, ending up with the route `JFK -> A -> C -> D -> B -> C -> JFK -> D -> A`.

```
def findItinerary(self, tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
        
    route = []
    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)
        
    visit('JFK')
    return route[::-1]
```

#### Solution: Iterative DFS + Stack

```
class Solution:
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = {}
    # Create a graph for each airport and keep list of airport reachable from it
    for src, dst in tickets:
        if src in graph:
            graph[src].append(dst)

    for src in graph.keys():
        graph[src].sort(reverse=True)
        # Sort children list in descending order so that we can pop last element 
        # instead of pop out first element which is costly operation

    res = []
    stack = ['JFK']
    
    # Start with JFK as starting airport and keep adding the next child to traverse 
    # for the last airport at the top of the stack. If we reach to an airport from where 
    # we can't go further then add it to the result. This airport should be the last to go 
    # since we can't go anywhere from here. That's why we return the reverse of the result
    # After this backtrack to the top airport in the stack and continue to traverse it's children
    while stack:
        elem = stack[-1]
        if elem in graph and len(graph[elem]) > 0: 
            # Check if elem in graph as there may be a case when there is no out edge from an airport 
            # In that case it won't be present as a key in graph
            stack.append(graph[elem].pop())
        else:
            res.append(stack.pop())
            # If there is no further children to traverse then add that airport to res
            # This airport should be the last to go since we can't anywhere from this
            # That's why we return the reverse of the result
    return res[::-1]
```

* Note that this approach guarantee both the conditions are met: a) using all tickets, b) going in most lexicographic-ally smallest possible route.

  + using all tickets: we can assume from the problem statement that all tickets (edges) are within the same connected component, since it states at least one valid itinerary can be formed. We won’t have any disjoint components such that we might miss out on visiting an edge if we start at the “JFK” node. In our DFS, we are removing edges from our adjacency list each time we traverse an edge. Thus, we will visit each edge exactly once, so every ticket will be used exactly once.
  + lexicographically smallest route: this is ensured by sorting each list of values in our adjacency list (`graph`). Our graph variable is an adjacency list with format {source\_city: [destination\_city1, destination\_city2, …]}. Since the list of values is sorted lexicographically in reverse, the last element will the lexicographically smallest one. When we are traversing edges in our DFS, we are popping the next city from our dictionary values, so we are greedily visiting the next city that is lexicographically lowest.
* Same approach; concise:

```
def findItinerary(self, tickets):
    targets = collections.defaultdict(list)
   
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    
    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
        route += stack.pop(),
   
    return route[::-1]
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

### [339/Medium] Nested List Weight Sum

#### Problem

* You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
* The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer’s value set to its depth.
* Return the sum of each integer in nestedList multiplied by its depth.
* Example 1:

```
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
```

* Example 2:

```
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
```

* Example 3:

```
Input: nestedList = [0]
Output: 0
```

* Constraints:
  + `1 <= nestedList.length <= 50`
  + `The values of the integers in the nested list is in the range [-100, 100].`
  + `The maximum depth of any integer is less than or equal to 50.`

#### Solution: BFS

```
class Solution(object):
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
    
        res, level, q = 0, 0, nestedList
        
        while q:
            level += 1
            next_q = []
            for ni in q:
                if ni.isInteger():
                    res += level * ni.getInteger()
                else:
                    next_q += ni.getList()
            q = next_q
        
        return res
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: One-liner

```
class Solution(object):
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def scanList(curr_list, depth):
            return sum(depth * x.getInteger() if x.isInteger() else scanList(x.getList(), depth + 1) for x in curr_list)
        
        return scanList(nestedList, 1)
```

##### Complexity

* Time: TODO
* Space: TODO

#### Solution: Recursive Backtracking/DFS

```
class Solution(object):
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def dfs(nestedList, depth):
            temp_sum = 0
            for member in nestedList:
                if member.isInteger():
                    temp_sum += member.getInteger() * depth
                else:
                    temp_sum += dfs(member.getList(), depth+1)
                    
            return temp_sum
            
        return dfs(nestedList, 1)
```

* Same approach; rehashed:

```
class Solution(object):
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(ni, depth):
            if ni.isInteger():
                return depth * ni.getInteger()
            return sum(dfs(n, depth + 1) for n in ni.getList())
        
        return sum(dfs(ni, 1) for ni in nestedList)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: Iterative Backtracking/DFS using Stack

```
class Solution(object):
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = [(ni, 1) for ni in nestedList]
        res = 0
        
        while stack:
            ni, depth = stack.pop()
            if ni.isInteger():
                res += depth * ni.getInteger()
            else:
                stack += [(n, depth + 1) for n in ni.getList()]
            
        return res
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\) for `stack`

### [366/Medium] Find Leaves of Binary Tree

* Given the `root` of a binary tree, collect a tree’s nodes as if you were doing this:
  + Collect all the leaf nodes.
  + Remove all the leaf nodes.
  + Repeat until the tree is empty.
* Example 1:

```
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
```

* Example 2:

```
Input: root = [1]
Output: [[1]]
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 100].`
  + `-100 <= Node.val <= 100`
* See [problem](https://leetcode.com/problems/find-leaves-of-binary-tree/) on LeetCode.

#### Solution: Backtracking/DFS using Post-order Traversal

* Post-order traversal, since we would like to add leaf nodes in subtrees first.
* After processing for both subtrees, we know that the current node is a leaf now.
  + We add it to the result list.
  + We use a level variable to denote which sublist (index) it should be in the res list.
  + `level` is 0 for original leaf nodes.
  + `level` will be `1 + the maximum level` of the children of the current node
  + When there aren’t enough sublists in the `res` list, we simply add enough empty lists to it.

```
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        res = []
        def dfs(root):
            level = 0
            
            if root.left:
                level = max(level, 1 + dfs(root.left))
                
            if root.right:
                level = max(level, 1 + dfs(root.right))
                
            for _ in range(level-len(res)+1):
                res.append([])
                
            res[level].append(root.val)
            return level
            
        dfs(root)
        return res
```

* Same approach; uses a `defaultdict`:

```
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, dic):
            
            if not root:
                return 0
                
            left = dfs(root.left, dic)
            right = dfs(root.right, dic)
            lev = max(left, right) + 1
            dic[lev] += root.val,
            
            return lev
            
        dic, ret = collections.defaultdict(list), []
        dfs(root, dic)
        
        for i in range(1, len(dic) + 1):
            ret.append(dic[i])
            
        return ret
```

* Same approach; uses a result list instead of a `defaultdict` as above:

```
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(root):
            if not root:
                return -1

            height = max(dfs(root.left), dfs(root.right)) + 1

            if height >= len(res):
                res.append([])

            res[height].append(root.val)
            return height

        dfs(root)
        return res
```

### [426/Medium] Convert Binary Search Tree to Sorted Doubly Linked List

#### Problem

* Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
* You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
* We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
* Example 1:

```
Input: root = [4,2,5,1,3]
```

```
Output: [1,2,3,4,5]
```

```
Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
```

* Example 2:

```
Input: root = [2,1,3]
Output: [1,2,3]
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 2000].`
  + `-1000 <= Node.val <= 1000`
  + `All the values of the tree are unique.`
* See [problem](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) on LeetCode.

#### Solution: DFS in-order traversal

* Use DFS in-order traversal finds the nodes in ascending order, and store the head and previous node in global variables. After the traversal is finished, prev is the “tail” of the double linked list so just connect it to the head.
* Because it’s binary search tree, from any node, as long as we’re using in-order (left - middle - right), the values of the nodes will be increasing, which will also be exactly how linkedList formed: smallest to largest. This author utilized the rule to visit nodes in-order.
* For example, `[4, 2, 5, 1, 3]`.
* Starting from root (4), the recursive function will go deep down to the left most node (1) as the 1st node to visit. it will do nothing but to define the head and prev = node(1). Then go up to the upper layer, node = (2), inside the function the purpose is to form the left and right relation between node and prev, which are (2) and (1). Then, move prev point to (2) and go ahead to visit node (3).
* In `treeToDoublyListHelper`, the node visiting will be left - middle - right all time, so we can safely assume prev to be the previous node visited, and build the doubly pointers to the current node.

```
class Solution(object):
    head = None
    prev = None

    def treeToDoublyList(self, root):
        if not root: return None
        self.treeToDoublyListHelper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def treeToDoublyListHelper(self, node):
        if not node: 
            return
        
        self.treeToDoublyListHelper(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else: # We are at the head.
            self.head = node
        
        self.prev = node
        self.treeToDoublyListHelper(node.right)
```

### [428/Hard] Serialize and Deserialize N-ary Tree

#### Problem

* Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
* Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.
* For example, you may serialize the following `3-ary` tree:

* as `[1 [3[5 6] 2 4]]`. Note that this is just an example, you do not necessarily need to follow this format.
* Or you can follow LeetCode’s level order traversal serialization format, where each group of children is separated by the null value.

* For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].
* You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.
* Example 1:

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
```

* Example 2:

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
```

* Example 3:

```
Input: root = []
Output: []
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 104].`
  + `0 <= Node.val <= 104`
  + `The height of the n-ary tree is less than or equal to 1000`
  + `Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.`
* See [problem](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/) on LeetCode.

#### Solution: Recursive DFS Pre-order Traversal

* **Serializer**:
  + The serializer uses recursion and gives us a result like:

  ```
    [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]
  ```
* **Deserializing**:
  + Our deserializer uses recursion similar to the serializer.
  + We get the root val (`k`) and then iterate through the nested items:

  ```
    At every call:
    eg: [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]

    k = 1
    for i in [[3, [[5, []], [6, []]]], [2, []], [4, []]]:
        node = Node(k)
        node.children = [helper(x) for x in i]
                                      1
                                    /   \ 
            [3, [[5, []], [6, []]]]       [2, []], [4, []]
                        3                    2        4
                      /   \
                [5,[]]    [6,[]]
                  5          6
  ```

```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        
        def helper(x):
            if x:
                return [[i.val, helper(i)] for i in x.children]
        return [root.val, helper(root)]
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
                
        def helper(vals):
            if not vals:
                return
            
            k = vals[0]
            for i in vals[1:]:
                node = Node(k)
                node.children = [helper(x) for x in i]
                return node
                    
        return helper(data)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [429/Medium] N-ary Tree Level Order Traversal

#### Problem

* Given the `root` of an n-ary tree, return the level order traversal of its nodes’ values.
* Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
* Example 1:

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
```

* Example 2:

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 104].`
  + `The height of the n-ary tree is less than or equal to 1000.`
* Follow up: Recursive solution is trivial, could you do it iteratively?
* See [problem](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) on LeetCode.

#### Solution: Recursion

```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        output = []
        self.dfs(root, 0, output)
        return output
    
    def dfs(self, root, level ,output):
        if root is None:
            return
        if len(output) < level+1:
            output.append([])
        
        output[level].append(root.val)
        for child in root.children:
            self.dfs(child, level+1, output)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: Iteration with Queue

```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
            
        queue = [root]
        ans = []
        
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                for child in node.children:
                    if child:
                        queue.append(child)
            
            ans.append(temp)
        return ans
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [472/Hard] Concatenated Words

#### Problem

* Given an array of strings `words` (without duplicates), return all the concatenated words in the given list of `words`.
* A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
* Example 1:

```
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
```

* Example 2:

```
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
```

* Constraints:
  + `1 <= words.length <= 104`
  + `0 <= words[i].length <= 30`
  + `words[i] consists of only lowercase English letters.`
  + `0 <= sum(words[i].length) <= 105`
* See [problem](https://leetcode.com/problems/concatenated-words/) on LeetCode.

#### Solution: DFS with Memoization

```
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        
        def find_words(word):
            #nonlocal wordset (not necessary)
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordset and suffix in wordset:
                    return True
                elif prefix in wordset and find_words(suffix):
                    return True
            
            return False
        
        output = []
        for word in words:
            if find_words(word):
                output.append(word)
                
        return output
```

##### Complexity

* Time: \(O(nm)\) where \(n\) are the number of words in the input and \(m\) are the average number of characters in each input word.
* Space: \(O(n)\) for `output`

### [489/Hard] Robot Room Cleaner

#### Problem

* You are controlling a robot that is located somewhere in a room. The room is modeled as an `m x n` binary grid where `0` represents a wall and `1` represents an empty slot.
* The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API `Robot`.
* You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.
* When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.
* Design an algorithm to clean the entire room using the following APIs:

```
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
```

* Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.
* Custom testing:

The input is only given to initialize the room and the robot’s position internally. You must solve this problem “blindfolded”. In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot’s position.

* Example 1:

```
Input: room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3
Output: Robot cleaned all rooms.
Explanation: All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
```

* Example 2:

```
Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms.
```

* Constraints:
  + `m == room.length`
  + `n == room[i].length`
  + `1 <= m <= 100`
  + `1 <= n <= 200`
  + `room[i][j] is either 0 or 1.`
  + `0 <= row < m`
  + `0 <= col < n`
  + `room[row][col] == 1`
  + `All the empty cells can be visited from the starting position.`
* See [problem](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) on LeetCode.

#### Solution: Recursive DFS

* Without the Robot API settings, it’s a kind of regular DFS problem. So we can build our solution based on DFS.
* The tricky things are, how to we make our robot object search all four directions without missing, and get back to original place after our recursive call. We can’t just input a coordinate `(i, j)` to our robot. We need to manually set the direction for it and move one step a time.
* An idea is search left side once first, and then search right side three times. In such way, after a DFS, robot will search all four directions and heads to the opposite direction against where it came from. Then, we have it move extra one unit and it can go back to where it came from, like a recursive DFS return.
* And we also need to pass current direction down to next DFS so we can calculate the direction sequence in next DFS. It’s like `(d+k) % 4 for k in (3,0,1,2)` where d is original direction and `k` is the turn. `k` iterates as `(3,0,1,2)` because we turn left first and then turn right 3 times.
* Another thing should be taken care is that after we DFS one path and get back to original place, we need to continue our DFS in current place. And since our direction has been reversed, we should turn left instead of right otherwise two direction would be missed.
* E.g. Robot reaches point X and heads N (so it comes from S). In current DFS, it turns left first and heads W to DFS. After that sub DFS, it gets back to X and heads E (not W). If it turns right, it will return to S and N and E will be missed. So it should turn left to visit N, then E and return to S.

```
    N
    
W   X   E

    S
```

* It will be clearer if you make a draft.
* So each time we have done a sub DFS, we reset the “turn left once first and then turn right” pattern.

```
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cleaned = set()
        
        def dfs(robot, x, y, direction):
            if (x, y) in cleaned:
                return
            robot.clean()
            cleaned.add((x, y))
            for i, (dx, dy) in enumerate(directions[direction:] + directions[:direction]):
                nx = x + dx
                ny = y + dy
                
                if robot.move():
                    dfs(robot, nx, ny, (direction + i) % 4)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                else:    
                    robot.turnRight()
                    
        dfs(robot, 0, 0, 0)
```

* Same approach; verbose:

```
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.robot = robot
        self.robot.clean()
        self.visited = {(0,0)}
        self.dfs(0, 0)
    
    def dfs(self, x, y):
        if (x-1, y) not in self.visited and self.up():
            self.robot.clean()
            self.visited.add((x-1, y))
            self.dfs(x-1, y)
            self.down()
        if (x, y-1) not in self.visited and self.left():
            self.robot.clean()
            self.visited.add((x, y-1))
            self.dfs(x, y-1)
            self.right()
        if (x+1, y) not in self.visited and self.down():
            self.robot.clean()
            self.visited.add((x+1, y))
            self.dfs(x+1, y)
            self.up()
        if (x, y+1) not in self.visited and self.right():
            self.robot.clean()
            self.visited.add((x, y+1))
            self.dfs(x, y+1)
            self.left()
        
    def up(self):
        return self.robot.move()
        
    def left(self):
        self.robot.turnLeft()
        result = self.robot.move()
        self.robot.turnRight()
        return result
        
    def right(self):
        self.robot.turnRight()
        result = self.robot.move()
        self.robot.turnLeft()
        return result
        
    def down(self):
        self.robot.turnLeft()
        self.robot.turnLeft()
        result = self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
        return result
```

### [515/Medium] Find Largest Value in Each Tree Row

#### Problem

* Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
* Example 1:

```
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
```

* Example 2:

```
Input: root = [1,2,3]
Output: [1,3]
```

* Constraints:
  + `The number of nodes in the tree will be in the range [0, 104].`
  + `-2^31 <= Node.val <= 2^31 - 1`
* See [problem](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) on LeetCode.

#### Solution: BFS/Level-order Traversal

* Traverse the tree level-by-level and record the max value seen at each level.

```
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        queue = deque([root])
        res = []
        
        while queue:
            max_ = float('-inf')
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node:
                    continue
                    
                max_ = max(max_, node.val)
                queue.extend([node.left, node.right])
                
            if max_ != float('-inf'):
                res.append(max_)
                
        return res
```

#### Solution: Recursive Backtracking/DFS with Pre-order Traversal

* Perform pre-order traversal on the tree.
* Initialize two variables `max_array` and `self.n.max_array` which contains the max value of each row. `self.n` keeps track of the current deepest row we travel so far.
* If the current row `cur_row`, is deeper than the deepest row we have visited at `self.n`, we update it. If not, we just compare the current value at this node with the max value of this row saved in the `max_array`.

```
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        max_array, self.n = [], 0

        def dfs(cur_node: Optional[TreeNode], cur_row: int):
            if not cur_node:
                return

            if cur_row == self.n:
                self.n += 1
                max_array.append(cur_node.val)

            max_array[cur_row] = max(max_array[cur_row], cur_node.val)

            dfs(cur_node.left, cur_row + 1)
            dfs(cur_node.right, cur_row + 1)

        dfs(root, 0)
        return max_array
```

##### Complexity

* Time: \(O(n)\) since we have to visit all the nodes once.
* Space: \(O(n)\) for `max_array`

#### Solution: Iterative Backtracking/DFS with Stack

```
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        max_array, self.n = [], 0

        def dfs(cur_node: Optional[TreeNode], cur_row: int):
            if not cur_node:
                return

            if cur_row == self.n:
                self.n += 1
                max_array.append(cur_node.val)

            max_array[cur_row] = max(max_array[cur_row], cur_node.val)

            dfs(cur_node.left, cur_row + 1)
            dfs(cur_node.right, cur_row + 1)

        dfs(root, 0)
        return max_array
```

* Same approach; rehashed:

```
def largestValues(self, root: TreeNode) -> List[int]:
    res = []
    
    def dfs(node=root, level=0):
        if not node:
            return
    
        if len(res)-1 < level:
            res.append(node.val)
        else:
            res[level] = max(node.val, res[level])
    
        dfs(node.left, level+1)
        dfs(node.right, level+1)
    
    dfs()
    return res
```

##### Complexity

* Time: \(O(n)\) since we have to visit all the nodes once.
* Space: \(O(n)\) for `max_array`

### [543/Easy] Diameter of Binary Tree

#### Problem

* Given the root of a binary tree, return the length of the diameter of the tree.
* The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
* The length of a path between two nodes is represented by the number of edges between them.
* Example 1:

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

* Example 2:

```
Input: root = [1,2]
Output: 1
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 104].`
  + `-100 <= Node.val <= 100`
* See [problem](https://leetcode.com/problems/diameter-of-binary-tree/) on LeetCode.

#### Solution: Backtracking/DFS

* The height of a node is the number of edges on the longest downward path between that node and a leaf. `dfs()` (in the first solution) and `height()` (in the second solution) calculates the height of the node, i.e, the longest downward path between the node and a leaf.
* For a node, the length of longest path going through the node is the sum of left child’s height plus right child’s height.
* The diameter of a binary tree is defined as the length of the longest path between any two nodes in a tree. For each node in the binary tree, we calculate the length of the longest path going through the node, the maximum length is the diameter of the binary tree according to the aforementioned definition.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
            
        def dfs(root):
            if not root: 
                return 0
                
            leftLongestPath = dfs(root.left)
            rightLongestPath = dfs(root.right)
            
            # keep track of the longest path that goes through the current
            # node i.e. the longest path from it's left child to leaf
            # through to its right child to a leaf and return that
            self.diameter = max(self.diameter, (leftLongestPath + rightLongestPath))
            
            # this is the standard recursive procedure
            # for calculating maximum height for a tree
            # i.e. longest path recursively from either 
            # left or right subtree + 1 for the current
            # level. 
            # For instance, if there's just one node
            # we'll check its left and right subtree, both of
            # which will return 0 from our base condition
            # and then max(0, 0) + 1 => 1 the correct height
            return max(leftLongestPath, rightLongestPath) + 1
        
        dfs(root)
        return self.diameter
```

* Using `nonlocal`:

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root):
            # The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
            # Use the keyword nonlocal to declare that the variable is not local.
            nonlocal diameter
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        
        diameter = 0
        height(root)
        return diameter
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [589/Easy] N-ary Tree Preorder Traversal

#### Problem

* Given the `root` of an n-ary tree, return the preorder traversal of its nodes’ values.
* Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
* Example 1:

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
```

* Example 2:

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 104].`
  + `0 <= Node.val <= 104`
  + `The height of the n-ary tree is less than or equal to 1000.`
* Follow up: Recursive solution is trivial, could you do it iteratively?
* See [problem](https://leetcode.com/problems/accounts-merge) on LeetCode.

#### Solution: Recursion

```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        output = []
        
        # perform dfs on the root and get the output stack
        self.dfs(root, output)
        
        # return the output of all the nodes.
        return output
    
    def dfs(self, root, output):
        
        # If root is none return 
        if root is None:
            return
        
        # for preorder we first add the root val
        output.append(root.val)
        
        # Then add all the children to the output
        for child in root.children:
            self.dfs(child, output)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: Iteration with Stack

```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack = [root]
        output = []
        
        # Till there is element in stack the loop runs.
        while stack:
            
            #pop the last element from the stack and store it into temp.
            temp = stack.pop()
            
            # append. the value of temp to output
            output.append(temp.val)
            
            #add the children of the temp into the stack in reverse order.
            # children of 1 = [3,2,4], if not reversed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(temp.children[::-1])
        
        #return the output
        return output
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [590/Easy] N-ary Tree Postorder Traversal

#### Problem

* Given the `root` of an n-ary tree, return the postorder traversal of its nodes’ values.
* Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
* Example 1:

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
```

* Example 2:

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
```

* Constraints:
  + `The number of nodes in the tree is in the range [0, 104].`
  + `0 <= Node.val <= 104`
  + `The height of the n-ary tree is less than or equal to 1000.`
* Follow up: Recursive solution is trivial, could you do it iteratively?
* See [problem](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) on LeetCode.

#### Solution: Recursion

```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output =[]
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
            
        for child in root.children:
            self.dfs(child, output)
        
        output.append(root.val)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: Iteration with Stack

```
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output =[]
        stack = [root]
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                stack += root.children
                
        return output[::-1]
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [695/Medium] Max Area of Island

* You are given an `m x n` binary matrix grid. An island is a group of 1’s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
* The area of an island is the number of cells with a value 1 in the island.
* Return the maximum area of an island in `grid`. If there is no island, return 0.
* Example 1:

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

* Example 2:

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

* Constraints:
  + `m == grid.length`
  + `n == grid[i].length`
  + `1 <= m, n <= 50`
  + `grid[i][j] is either 0 or 1.`
* See [problem](https://leetcode.com/problems/max-area-of-island/) on LeetCode.

#### Solution: Recursive DFS

* We want to know the area of each connected shape in the grid, then take the maximum of these.
* If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected to those squares, and so on), then the total number of squares explored will be the area of that connected shape.
* To ensure we don’t count squares in a shape more than once, let’s use seen to keep track of squares we haven’t visited before. It will also prevent us from counting the same shape more than once.

```
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
```

* Similar approach; doesn’t use `seen` and instead sets the grid entry to 0 after visiting it:

```
class Solution(object):
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0
```

* Note that the time complexity of the above solution is \(O(mn)\). If you maintain a list of visited cells (like the first solution), then you will execute one DFS per island. With the set of visited you ensure that you visited any one cell on the grid at most once. Which leads to the worst case time, when the grid is full of 1’s where you visit each cell of the grid, leading to \(O(mn)\). In the implementation above, the visited set is implemented in the form of setting the grid entry to 0 after visiting it, effectively preventing reaching that cell again after it’s been explored.

##### Complexity

* Time: \(O(R\*C)\), where \(R\) is the number of rows in the given grid, and \(C\) is the number of columns. We visit every square once.
* Space: \(O(R\*C)\), the space used by seen to keep track of visited squares, and the space used by the call stack during our recursion.

#### Solution: Iterative DFS

* We can try the same approach using a stack based, (or “iterative”) depth-first search.
* Here, seen will represent squares that have either been visited or are added to our list of squares to visit (stack). For every starting land square that hasn’t been visited, we will explore 4-directionally around it, adding land squares that haven’t been added to seen to our stack.
* On the side, we’ll keep a count shape of the total number of squares seen during the exploration of this shape. We’ll want the running max of these counts.

```
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
```

##### Complexity

* Time: \(O(R\*C)\), where \(R\) is the number of rows in the given grid, and \(C\) is the number of columns. We visit every square once.
* Space: \(O(R\*C)\), the space used by seen to keep track of visited squares, and the space used by stack.

### [721/Medium] Accounts Merge

#### Problem

* Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing emails of the account.
* Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
* After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
* Example 1:

```
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
```

* Example 2:

```
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
```

* Constraints:
  + `1 <= accounts.length <= 1000`
  + `2 <= accounts[i].length <= 10`
  + `1 <= accounts[i][j] <= 30`
  + `accounts[i][0] consists of English letters.`
  + `accounts[i][j] (for j > 0) is a valid email.`
* See [problem](https://leetcode.com/problems/accounts-merge) on LeetCode.

#### Solution: DFS Iterative

```
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        em_to_name = {}
        em_graph = defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            
            # making a graph of common connected gmail
            # all acc the gamil start with 1 index
            for email in acc[1:]:
                
                # connect 1st to 2nd email
                em_graph[acc[1]].add(email)
                
                #connect 2nd to 1st email
                em_graph[email].add(acc[1])
                
                # create a hashmap
                # it help us to find the email owners
                em_to_name[email] = name
                
        # print(em_graph)
        # print(em_to_name)
    
        seen = set()
        ans = []
        
        # here we use loop to traverse all unconnected
        # components of the graph
        for email in em_graph:
            if email not in seen:
                seen.add(email)
                st = [email]
                component = []
                
                # this loop give us the all conneted path as here
                # all common gmail as a list in comonent
                while st:
                    edge = st.pop()
                    component.append(edge)
                    for nei in em_graph[edge]:
                        if nei not in seen:
                            seen.add(nei)
                            st.append(nei)
                            
                # after geting all connect comonent
                # we sorted the as question
                # and search the owner of the starting email
                # append in the ans
                ans.append([em_to_name[email]] + sorted(component))
        return ans
```

#### Solution: DFS Recursion

```
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:        
        
        em_to_name = {}
        em_graph = defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            
            # making a graph of common connected gmail
            # all acc the gamil start with 1 index
            for email in acc[1:]:
                
                # connect 1st to 2nd email
                em_graph[acc[1]].add(email)
                
                #connect 2nd to 1st email
                em_graph[email].add(acc[1])
                
                # create a hashmap
                # it help us to find the email owners
                em_to_name[email] = name
                
        # print(em_graph)
        # print(em_to_name)
    
        seen = set()
        ans = []
        
        # dfs function
        def dfs(s,comp):
            if s in seen:
                return
            seen.add(s)
            comp.append(s)
            for nei in em_graph[s]:
                if nei not in seen:
                    dfs(nei,comp)    
            return comp  
        
        # here we use loop to traverse all unconnected
        # components of the graph
        for email in em_graph:
            if email not in seen:
                component = []
                dfs(email, component)
                ans.append([em_to_name[email]] + sorted(component))
                
        return ans
```

#### Solution: BFS

```
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        em_to_name = {}
        em_graph = defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            
            # making a graph of common connected gmail
            # all acc the gamil start with 1 index
            for email in acc[1:]:
                
                # connect 1st to 2nd email
                em_graph[acc[1]].add(email)
                
                #connect 2nd to 1st email
                em_graph[email].add(acc[1])
                
                # create a hashmap
                # it help us to find the email owners
                em_to_name[email] = name
                
        # print(em_graph)
        # print(em_to_name)
    
        seen = set()
        ans = []
        
        # here we use loop to traverse all unconnected
        # components of the graph
        for email in em_graph:
            if email not in seen:
                seen.add(email)
                 q = [email]
                component = []
                
                # this loop give us the all conneted path as here
                # all common gmail as a list in comonent
                while q:
                    edge = q.pop(0)
                    component.append(edge)
                    for nei in em_graph[edge]:
                        if nei not in seen:
                            seen.add(nei)
                           q.append(nei)
                            
                # after geting all connect comonent
                # we sorted the as question
                # and search the owner of the starting email
                # append in the ans
                ans.append([em_to_name[email]] + sorted(component))
        return ans
```

#### Solution: Union-Find

```
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Create unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
```

### [863/Medium] All Nodes Distance \(K\) in Binary Tree

#### Problem

* Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.
* You can return the answer in any order.
* Example 1:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
```

* Example 2:

```
Input: root = [1], target = 1, k = 3
Output: []
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 500].`
  + `0 <= Node.val <= 500`
  + `All the values Node.val are unique.`
  + `target is the value of one of the nodes in the tree.`
  + `0 <= k <= 1000`
* See [problem](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree) on LeetCode.

#### Solution: BFS by converting tree to a bidirected graph

* We want to do a BFS and return all the values at `K` distance from target.
* We hit a minor obstacle because we cannot traverse a tree backwards.
* So we ask ourselves, what do we know about a tree?
* A tree is a directed acyclic graph. If we could convert the tree to a undirected graph (or bidirected in the code below) we could simply run a BFS on the adjacency list of each node.

```
class Solution:
    def convert_into_graph(self, node, parent, graph):
        # To convert into graph we need to know who is the parent
        if not node:
            return
        
        if parent:
            graph[node].append(parent)
            
        if node.right:
            graph[node].append(node.right)
            self.convert_into_graph(node.right, node, graph)
        
        if node.left:
            graph[node].append(node.left)
            self.convert_into_graph(node.left, node, graph)
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(list)
        vis, q, res = set(), deque(), []
        # We have a graph, now we can use simply BFS to calculate K distance from node.
        self.convert_into_graph(root, None, graph)
        
        q.append((target, 0))
        
        while q:
            n, d = q.popleft()
            vis.add(n)
            
            if d == K:
                res.append(n.val)
            
            # adjacency list traversal
            for neighbor in graph[n]:
                if neighbor not in vis:
                    q.append((neighbor, d + 1)) 
                
        return res
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

#### Solution: BFS + HashMap

```
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.parent = {}
        self.getParents(root, None)
        return self.bfs(target, K)
    
    def getParents(self, node: TreeNode, parent: TreeNode) -> None: 
        if node == None: 
            return
        
        # Store parent nodes
        self.parent[node.val] = parent
        
        self.getParents(node.left, node)
        self.getParents(node.right, node)
        
    def bfs(self, start: TreeNode, K: int) -> List[int]:
        res, q, visited = [], [(start, 0)], set()
        
        while q:
            n, d = q.pop(0)
            
            if n not in visited:
                if d == K: 
                    res.append(n.val)
                
                visited.add(n)
                # you can improve it slightly by storing the memory address instead of the node itself in visited.
                # So, if id(n) not in visited: visited.add(id(n))
                
                if n.left: 
                    q.append((n.left, d+1))
                
                if n.right: 
                    q.append((n.right, d+1))
                
                if self.parent[n.val]: 
                    q.append((self.parent[n.val], d+1))
                                   
        return res
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

#### Solution: DFS

```
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # dfs preorder traversal to map each node to its parent
        def get_parent(node = root, parent = None):
            if not node: 
                return
            
            hashmap[node] = parent
            get_parent(node.left, node), get_parent(node.right, node)
        
        def search(node = target, distance = 0):
            if not node or node.val in visited: 
                return
            
            visited.add(node.val)
            if distance == K: 
                answer.append(node.val)
            
            for neighbor in (hashmap[node], node.left, node.right):
                search(neighbor, distance+1)
        
        hashmap, answer, visited = {}, [], set()
        get_parent(), search()
        return answer
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(n)\)

### [865/1123/Medium] Smallest Subtree with all the Deepest Nodes / Lowest Common Ancestor of Deepest Leaves

#### Problem

* Given the root of a binary tree, the depth of each node is the shortest distance to the root.
* Return the smallest subtree such that it contains all the deepest nodes in the original tree.
* A node is called the deepest if it has the largest depth possible among any node in the entire tree.
* The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
* Example 1:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
```

* Example 2:

```
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
```

* Example 3:

```
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
```

* Constraints:
  + `The number of nodes in the tree will be in the range [1, 500].`
  + `0 <= Node.val <= 500`
  + `The values of the nodes in the tree are unique.`
* Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
* See [problem](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) on LeetCode.

#### Solution: DFS/Post-order traversal

```
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deepestDepth(node, depth):
            if not node:
                return node, depth
            
            left, leftDepth = deepestDepth(node.left, depth + 1)
            right, rightDepth = deepestDepth(node.right, depth + 1)    

            # If the deepest node on the left subtree is deeper than the deepest node 
            # on the right subtree return the left subtree and the left deepest depth 
            if leftDepth > rightDepth:
                return left, leftDepth
            
            # If the deepest node on the right subtree is deeper than the deepest node 
            # on the left subtree return the right subtree and the right deepest depth 
            if rightDepth > leftDepth:
                return right, rightDepth
            
            # If the above two conditions isn't met, then leftDepth == rightDepth
            #
            # leftDepth equal rightDepth means that the deepest node
            # in the left subtree has the same depth as the deepest node 
            # in the right subtree, as such, we should return the current node 
            # as it is the root of the current subtree that contains the deepest 
            # nodes on the left and right subtree.
            #
            # return statement can also be `return node, rightDepth`
            return node, leftDepth
            
        return deepestDepth(root, 0)[0]
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [889/Medium] Construct Binary Tree from Preorder and Postorder Traversal

### Problem

* Given two integer arrays, `preorder` and `postorder` where `preorder` is the preorder traversal of a binary tree of distinct values and `postorder` is the postorder traversal of the same tree, reconstruct and return the binary tree.
* If there exist multiple answers, you can return any of them.
* Example 1:

```
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
```

* Example 2:

```
Input: preorder = [1], postorder = [1]
Output: [1]
```

* Constraints:
  + `1 <= preorder.length <= 30`
  + `1 <= preorder[i] <= preorder.length`
  + `All the values of preorder are unique.`
  + `postorder.length == preorder.length`
  + `1 <= postorder[i] <= postorder.length`
  + `All the values of postorder are unique.`
  + `It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.`
* See [problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal) on LeetCode.

#### Solution: Recursion

* Consider the following tree and its preorder and postorder sequence:

```
                   1
            2             3
          4  5           6  7
          
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
```

* We know that the `root` is the first element in the preorder sequence and the last element in the postorder sequence. Therefore, the root node is `1`. After we pop the root (`1`) from `postorder`, locate the new last element in the postorder sequence, `3`, which is the root of right subtree (or the right child of the root node). Now since `3` is the root node of the right subtree, all nodes before `3` in `preorder` (apart from the leftmost root node), i.e., `{2, 4, 5}`, correspond to the left subtree with `2` being the root of it while all nodes after (and including) `3` must be present in the right subtree, i.e., `{3, 6, 7}`.
* Now the problem is reduced to recursively building the left and right subtrees and linking them to the root node.

```
Left subtree:
 
Preorder  : {2, 4, 5}
Postorder : {4, 5, 2}
 
Right subtree:
 
Preorder  : {3, 6, 7}
Postorder : {6, 7, 3}
```

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        # root of the level
        root = TreeNode(postorder.pop())
        
        if len(preorder) == 1:
            return root
        
        # find the root of the right subtree at the level
        root_index = preorder.index(postorder[-1])                
        
        root.right = self.constructFromPrePost(preorder[root_index:], postorder)
        root.left = self.constructFromPrePost(preorder[1:root_index], postorder)
        
        return root
```

* Alternatively, if we `pop(0)` the root (`1`) from the preorder sequence, locate the next element in the postorder sequence, `2`, which is the root of left subtree (or the left child of the root node). Now since `2` is the root node of the left subtree, all nodes before (and including) `2` in the postorder sequence must be present in the left subtree of the root node, i.e., `{4, 5, 2}`, and all the nodes after `2` (except the last node which is the root node) must be present in the right subtree, i.e., `{6, 7, 3}`.

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

### [938/Easy] Range Sum of BST

#### Problem

* Given the `root` node of a binary search tree and two integers `low` and `high`, return the sum of values of all nodes with a value in the inclusive range `[low, high]`.
* Example 1:

```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
```

* Example 2:

```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 2 * 104].`
  + `1 <= Node.val <= 105`
  + `1 <= low <= high <= 105`
  + `All Node.val are unique.`
* See [problem](https://leetcode.com/problems/range-sum-of-bst) on LeetCode.

#### Solution: Recursion

```
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # Make sure to use an identity check using "is" (and not an equality check using "--") 
        # for singleton objects such as True, False and None. 
        # Check [Comparison to None should be 'cond is None:' (E711)](https://www.flake8rules.com/rules/E711.html) for more info.
        if root is None: 
            return 0
            
        if root.val > R: 
            return self.rangeSumBST(root.left, L, R)
            
        if root.val < L: 
            return self.rangeSumBST(root.right, L, R)
        
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(1)\)

#### Solution: Recursive Backtracking/DFS

```
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                    #print(node.val)
                    
                if node.val > L:
                    dfs(node.left)
                    
                if node.val < R:
                    dfs(node.right)
                    
        self.ans = 0
        dfs(root)
        return self.ans
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(h)\)

#### Solution: Recursive Backtracking/DFS

```
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                    
                if node.val > L:
                    dfs(node.left)
                    
                if node.val < R:
                    dfs(node.right)
                    
        self.ans = 0
        dfs(root)
        return self.ans
```

* Same approach; rehashed:

```
class Solution(object):
    def rangeSumBST(self, root, L, R):    
        def dfs(node):
            if not node: 
                return 0
                
            if node.val < L: 
                return dfs(node.right)
            elif node.val > R: 
                return dfs(node.left)
            else: 
                return dfs(node.left) + dfs(node.right) + node.val
                
        return dfs(root)
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(h)\)

#### Solution: Iterative Backtracking/DFS + Stack

```
class Solution(object):
    def rangeSumBST(self, root, L, R):    
        stack = [root]
        ans = 0
        
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R: 
                    ans += node.val
                    
                if L < node.val: 
                    stack.append(node.left)
                    
                if R > node.val: 
                    stack.append(node.right)
                    
        return ans
```

##### Complexity

* Time: \(O(n)\)
* Space: \(O(h)\)

### [987/Hard] Vertical Order Traversal of a Binary Tree

#### Problem

* Given the `root` of a binary tree, calculate the vertical order traversal of the binary tree.
* For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.
* The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
* Return the vertical order traversal of the binary tree.
* Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
```

* Example 2:

```
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
```

* Example 3:

```
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 1000].`
  + `0 <= Node.val <= 1000`
* See [problem](https://leetcode.com/problems/brace-expansion/) on LeetCode.

#### Solution: BFS/DFS with Global Sorting

* **Overview**:
  + This is yet another problem about Binary Tree traversals. As one would probably know, the common strategies to traverse a Tree data structure are Breadth-First Search (a.k.a. BFS) and Depth-First Search (a.k.a. DFS).
  + The DFS strategy can be further distinguished as preorder DFS, inorder DFS and postorder DFS, depending on the relative order of visit among the node itself and its child nodes.
  + If one is not familiar with the concepts of BFS and DFS, please go through BFS traversal as well as the DFS traversal at the beginning of this section. Hence, in this article, we won’t repeat ourselves on these concepts.
  + In this problem, we are asked to return the vertical order of a binary tree, which implies three sub-orders (denoted as `<column, row, value>`) as follows:
    - **column-wise order:**
      * First, we look at a binary tree horizontally. Each node would be aligned to a specific `column`, based on its relative offset to the root node of the tree.
      * Let us assume that the root node has a column index of 0, then its left child node would have a column index of -1, and its right child node would have a column index of +1, and so on.
    - **row-wise order:**
      * Secondly, we look at the binary tree vertically. Each node would be assigned to a specific `row`, based on its level (i.e. the vertical distance to the root node).
      * Let us assume that the root node has a row index of 0, then both its child nodes would have the row index of 1. Note that the convention we adopt here is slightly different from the one in the problem description where the row index of a parent node is larger than the one of its child nodes. This, though, would not jeopardize our solution. On the contrary, it would help us to simplify the solution, as one will see later.
    - **value-wise order:**
      * Finally, given the definitions of the above two sub-orders, there could be a case where two different nodes have the same `<column, row>` index. As a result, to resolve the draw situation, as stated in the problem description, the node that has a smaller `value` should come first.
        > Given the above definitions, we can now formulate the problem as a task to sort the nodes based on the 3-dimensional coordinates (i.e., `<column, row, value>`) that we defined above.
  + The priority of each coordinate is determined by its order. For example, the coordinate column comes first, therefore it has the highest priority. A node with the lowest column index would come up first, regardless the other two coordinates.
  + Before proceeding to the solutions, we would like to mention that there is another almost identical problem called [314. Binary Tree Vertical Order Traversal](../bfs/#314medium-binary-tree-vertical-order-traversal).
  + The only difference between these two problems lies in the third sub-order. When two nodes have the same `<column, row>` index, in this problem we would further order them based on their values, while in the problem of 314 we would order them based on the horizontal order from left to right. To illustrate the difference, we show an example in the following graph on how two nodes of the same `<column, row>` index should be ordered respectively in these two problems.
  + A subtle difference as it seems to be, yet it has a significant impact on the solutions. As a spoiler alert, one could solve the problem of 314 without resorting to the sorting operation, while for this problem the sorting is inevitable due to the third sub-order required in the problem.
* **Intuition**:
  + In the overview section, we’ve reduced the problem into a sorting problem, based on the order of 3-dimensional coordinates `<column, row, value>` as we defined.
    > As a result, the idea to solve the problem would be as intuitive as building a list where each element in the list corresponds to the 3-dimensional coordinates of each node in the tree, and then sorting the list based on the coordinates.
  + To build such a list, we would need to traverse all the nodes in the tree, which we could do with either Breadth-First Search (BFS) or Depth-First Search (DFS). Most of the time, facing the problems of binary tree traversal, we need to make a choice between them. However, in this case, both of the approaches would work. Because both of them would lead to a list that contains the coordinates of all nodes. Though the order of elements in the list would differ depending on the approach, it does not matter, since we would sort the list anyway.
* **Algorithm**:
  + Based on the above intuition, we could implement the solution in 3 simple steps:
    1. we traverse the input tree either by BFS or DFS, in order to generate a list that contains the 3-dimensional coordinates (i.e. `<column, row, value>`) of each node.
       - Note that, we assign a higher `row` index value to a node’s child node. This convention is at odds with the denotation given in the problem description. This is done intentionally, in order to keep the ordering of all coordinates consistent, i.e. a lower value in any specific coordinate represents a higher order. As a result, a sorting operation in ascending order would work for each coordinate consistently.
    2. Once we generate the desired list, we then sort the list.
    3. From the sorted list, we then extract the results, and group them by the `column` index.
  + In the following, we give some sample implementations with both the BFS traversal and the DFS traversal.
* **BFS Traversal**:

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def BFS(root):
            queue = deque([(root, 0, 0)])
            while queue:
                node, row, column = queue.popleft()
                if node is not None:
                    node_list.append((column, row, node.val))
                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). construct the global node list, with the coordinates
        BFS(root)

        # step 2). sort the global node list, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results partitioned by the column index
        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]

        return ret.values()
```

* **DFS Traversal**:

```
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def DFS(node, row, column):
            if node is not None:
                node_list.append((column, row, node.val))
                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). construct the node list, with the coordinates
        DFS(root, 0, 0)

        # step 2). sort the node list globally, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results grouped by the column index
        ret = []
        curr_column_index = node_list[0][0]
        curr_column = []
        for column, row, value in node_list:
            if column == curr_column_index:
                curr_column.append(value)
            else:
                # end of a column, and start the next column
                ret.append(curr_column)
                curr_column_index = column
                curr_column = [value]
        # add the last column
        ret.append(curr_column)

        return ret
```

##### Complexity

* Let \(N\) be the number of nodes in the input tree.
* Time: \(\mathcal{O}(N \log N)\), which applies to both the BFS and DFS approaches.
  + In the first step of the algorithm, we traverse the input tree with either BFS or DFS, which would take \(\mathcal{O}(N)\) time.
  + Secondly, we sort the obtained list of coordinates which contains \(N\) elements. The sorting operation would take \(\mathcal{O}(N \log N)\) time.
  + Finally, we extract the results from the sorted list, which would take another \mathcal{O}(N)O(N) time.
  + To summarize, the overall time complexity of the algorithm would be \(\mathcal{O}(N \log N)\), which is dominated by the sorting operation in the second step.
* Space: \(\mathcal{O}(N)\). Again this applies to both the BFS and DFS approaches.
  + In the first step of the algorithm, we build a list that contains the coordinates of all the nodes. Hence, we need \(\mathcal{O}(N)\) space for this list.
  + Additionally, for the BFS approach, we used a queue data structure to maintain the order of visits. At any given moment, the queue contains no more than two levels of nodes in the tree. The maximal number of nodes at one level is \(\frac{N}{2}\), which is the number of the leaf nodes in a balanced binary tree. As a result, the space needed for the queue would be \(\mathcal{O}(\frac{N}{2} \cdot 2)\) = \(\mathcal{O}(N)\).
  + Although we don’t need the queue data structure for the DFS approach, the recursion in the DFS approach incurs some additional memory consumption on the function call stack. In the worst case, the input tree might be completely imbalanced, e.g. each node has only the left child node. In this case, the recursion would occur up to \(N\) times, which in turn would consume \(\mathcal{O}(N)\) space in the function call stack.
  + To summarize, the space complexity for the BFS approach would be \(\mathcal{O}(N) + \mathcal{O}(N) = \mathcal{O}(N)\). And the same applies to the DFS approach.

#### Solution: BFS/DFS with Partition Sorting

* **Intuition**:
  + As we can see in the above approaches, the overall time complexity is dominated by the sorting operation on the list of coordinates. In order to further optimize the solution, we can try to do something with the sorting.
  + It would be hard, if not impossible, to eliminate the sorting operation, since we still need a means to resolve the draw situation when two nodes share the same `<column, row>` index.
  + One might argue that we could use the heap data structure (also known as `PriorityQueue` in Java) to maintain the list of coordinates. The elements in the heap data structure are ordered automatically, and this does eliminate the sorting operation. However, to maintain the elements in order, each insertion operation in heap would take \(\mathcal{O}(\log N)\) time complexity. In other words, one can consider the heap data structure as another form of sorting, which amortizes the cost of sorting operating over each insertion.
  + One could apply the head data structure to replace the sorting operation here, which could make the code more concise. But this is not the main point here.
    > That being said, one thing that we can do is to reduce the scope of sorting, by partitioning the list of coordinates into subgroups based on the `column` index.
  + Although we would still need to sort the subgroups respectively, it would be faster to sort a series of subgroups than sorting them all together in a single group. Here is a not-so-rigid proof.
  + Suppose that we have a list of \(N\) elements, it would then take \(\mathcal{O}(N \log N)\) time to sort this list.
  + Next, we divide the list into \(k\) sublists equally. Each list would contain \(\frac{N}{k}\) elements. Similarly, it would take \(\mathcal{O}(\frac{N}{k} \log \frac{N}{k})\) time to sort each sublist.
  + In total, to sort all the \(k\) sublists, it would take \(\mathcal{O}(k \cdot \frac{N}{k} \log \frac{N}{k}) = \mathcal{O}(N \log \frac{N}{k})\), which is less than the time complexity of sorting the original list (i.e. \(\mathcal{O}(N \log N)O(NlogN)\)).
    > More importantly, another rationale to partition the list into `column` based groups is that this is also the format of results that are asked in the problem.
  + Once we sort the column based groups, we can directly return the groups as results, without the need for extraction as we did in the previous approach.
  + This is also the reason why we would not recommend to further partition the list based on the combination of `<column, row>` index. Although theoretically, the more groups that we partition the list into, the faster the sorting operations would be.
  + If we partition the list into the groups lead by `<column row>` index, we would need some additional processing to extract the results. Hence, it would become an overkill.
* **Algorithm**:
  + We could implement the above intuition based on the previous approaches. Again, we could break it down into 3 steps:
    1. First of all, we create a hashmap called `columnTable` with the `column` index as key and the list of `<row, value>` tuples as value. This hashmap is used to hold the groups of coordinates.
       - We traverse the input tree by either BFS or DFS. During the traversal, we populate the hashmap that we created above.
       - Meanwhile, we also note down the minimal and maximal column index during the traversal. The minimal and maximal column index defines the range of column index. With this range, we could iterate through columns in order without the need for sorting, as one will see later.
    2. Once we populate the above hashmap, we then sort the value in each entry of the hashmap, i.e. we sort each group of coordinates led by the `column` index.
    3. From the sorted hashmap, we extract the results that are grouped by the `column` index.
  + In the following, we give some sample implementations with both the BFS traversal and the DFS traversal.
* **BFS Traversal**:

```
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def BFS(root):
            nonlocal min_column, max_column
            queue = deque([(root, 0, 0)])

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row, node.val))
                    min_column = min(min_column, column)
                    max_column = max(max_column, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). BFS traversal
        BFS(root)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret
```

* **DFS Traversal**:

```
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        # step 1). DFS traversal
        DFS(root, 0, 0)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret
```

##### Complexity

* Let \(N\) be the number of nodes in the tree.
  + Time: \(\mathcal{O}(N \log{\frac{N}{k}})\) where \(k\) is the width of the tree, i.e., \(k\) is also the number of columns in the result.
  + In the first step, it takes \(\mathcal{O}(N)\) time complexity for both the BFS and DFS traversal.
  + In the second step, we need to sort the hashmap entry by entry. As we shown in the intuition section, the time complexity of sorting \(k\) equal-sized subgroups of with total \(N\) elements would be \(\mathcal{O}(k \cdot \frac{N}{k} \log{\frac{N}{k}}) = \mathcal{O}(N \log{\frac{N}{k}})\). If we assume that the nodes are evenly aligned in the columns, then this would be the time complexity of sorting the obtained hashmap.
  + Finally, it takes another \(\mathcal{O}(N)\) time complexity to extract the results from the hashmap.
  + As a result, the overall time complexity is \(\mathcal{O}(N \log{\frac{N}{k}})\).
  + Although the sorting operation in the second step still dominates, it is more optimized compared to the previous approach of sorting the entire coordinates. Let us look at one particular example. In the case where the tree is complete imbalanced (e.g. a node has only left node), the tree would be partitioned into exactly \(N\) groups. Each group contains a single element. It would take no time to sort each group. As a result, the overall time complexity of this approach becomes \(N \cdot \mathcal{O}(1) = \mathcal{O}(N)\). While for the previous approach, its overall time complexity remains \(\mathcal{O}(N \log N)\).
* Space: \(\mathcal{O}(N)\). Again this applies to both the BFS and DFS approaches. The analysis is the same as the previous approach.

### [1087/Medium] Brace Expansion

#### Problem

* You are given a string `s` representing a list of words. Each letter in the word has one or more options.

  + If there is one option, the letter is represented as is.
  + If there is more than one option, then curly braces delimit the options. For example, `"{a,b,c}"` represents options `["a", "b", "c"]`.
* For example, if s = `"a{b,c}"`, the first character is always `'a'`, but the second character can be `'b'` or `'c'`. The original list is `["ab", "ac"]`.
* Return all words that can be formed in this manner, sorted in lexicographical order.
* Example 1:

```
Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
```

* Example 2:

```
Input: s = "abcd"
Output: ["abcd"]
```

* Constraints:
  + `1 <= s.length <= 50`
  + `s consists of curly brackets '{}', commas ',', and lowercase English letters.`
  + `s is guaranteed to be a valid input.`
  + `There are no nested curly brackets.`
  + `All characters inside a pair of consecutive opening and ending curly brackets are different.`
* See [problem](https://leetcode.com/problems/brace-expansion/) on LeetCode.

#### Solution: Backtracking/DFS

* **Intuition**:
  + We could have the list of words ready and use this list to create a new list containing the product of the current words and all of the next character options.
  + However, in this approach, rather than constructing all of the words at the same time, we will construct the list of words, one word at a time. We will sequentially choose one character from each of the character groups to build the string. We will be performing this process recursively, using backtracking. Suppose the words in the list have length \(k\), we will traverse the character options for a particular index in ascending order, add a character to the current string, and make a recursive call for the next index. Once we return from the recursive call, we will backtrack (remove the last added character), add the next character in the `options`, and repeat the process until the string length becomes equal to \(k\). Each time the string length becomes equal to \(k\), we add the current string to our list of expanded words.
* **Algorithm**:
  + Extract the character options for different indices and store them in the list `options` using the function `storeAllOptions`. Unlike the previous approaches, we find the options for all indices beforehand because if we find the options while backtracking, we will end up finding the options for the same index multiple times.
  + Call the function `backtrack` with the given string \(s\) and an empty string as the current string `tmpStr`.
  + If the string `tmpStr` is complete i.e., the length of the `tmpStr` becomes equal to the number of options in `options`, add the string to the list `res` and return.
  + Fetch the character options for the current index in `options`. Iterate over the characters in the list `options` and for each character:
    - Add the character to `tmpStr`.
    - Recursively call the function `backtrack` with the updated index (`index+1`) and string `tmpStr`.
    - Backtrack by removing the last added character.
  + Return `res`.

```
class Solution:        
    def expand(self, s: str) -> List[str]:
        options = [] 
        res = []
        
        def storeAllOptions(s: str) -> List:
            nonlocal options

            i = 0           
            # turn string into graph "{a, b}c{d, e}f" -> [[a, b], [c], [d, e], [f]]
            # creates the option list with: [[a, b], [c], [d, e], [f]]
            while i < len(s):
                if s[i] == '{':
                    tmpArr = []
                    while s[i] != '}':
                        if s[i].isalpha():
                            tmpArr.append(s[i])
                        i += 1
                    tmpArr.sort()
                    options.append(tmpArr)
                elif s[i].isalpha():
                    options.append([s[i]])
                i += 1
                
            return options            
        
        # classic backtracking template
        def backtrack(index, tmpStr) -> None:
            nonlocal res
                        
            # do we have as many characters as len(options)?
            if len(tmpStr) == len(options):
                res.append(tmpStr)
                return
            for s in options[index]:
                prev = tmpStr
                
                # append char
                tmpStr += s
                # go ahead with the next char
                backtrack(index + 1, tmpStr)
                
                # backtrack by removing the last added character
                tmpStr = prev
        
        storeAllOptions(s)
        backtrack(0, "")
        return res
```

##### Complexity

* Time: \(O(N \* K^N)\)
  + First of all, we can consider this as repeat-allowed permutation with \(K\) choices where \(K\) is length of nested array, and for \(N\) positions. So we have \(K^N\) choices.
    - Then we have to take N times to build each permutations.
    - So it is \(O(N \* K^N)\) where \(N\) is the length of the array and \(K\) is length of nested array.
  + Consider we have these possible cases => `[{a,b} x 10] vs [{a,b,c} x 7] vs [{a,b,c,d} x 5]` (since we know length of s <= 50).
    - We have \(2^10 vs. 3^7 vs. 4^5\) = \(1024 vs. 2187 vs. 1024\).
    - It seems the worst case we can have is where every list has 3 choices with 7 positions.
  + We can break down the time complexity into three parts. The time required to find all of the character options, the time required to store all of the words, and the time required to build all of the words. Let’s go over the parts in that order.
    - In the function storeAllOptions we traverse over the string and sort the individual list of options for each index. Hence, similar to the previous approaches, the complexity is bounded by \(O(N\log N)\), using the inequality \(x \log x + y \log y \leq (x+y) \log (x+y)\).
    - Also similar to the previous approaches, in the worst-case scenario, we will create \(3^{N/7}\) words. In this implementation, we use a mutable data structure to build each word at a time. Thus, once the word is of length KK we must make a deep copy of the word in order to store it. If we did not create a deep copy, then when we remove the last character from the mutable data structure, it would also affect the word in our result list. Creating each copy will take O(K)O(K) time. Thus, storing all of the words will require \(O(K \* 3 ^ {N / 7})\) time.
  + Finally, for this approach, adding a character to or removing a character from `tmpStr` requires only constant time. Since each word is built only once, building all of the strings will not require more than \(O(K \* 3 ^ {N / 7})\) time (which is the maximum number of characters in all of the words).
  + Therefore, the dominant term in the time complexity is \(O(K \* 3^K)\), and as shown in the previous approaches, in the worst-case scenario, \(K = N / 7\). Thus, the complexity can be written as \(O(N \* 3^{N/7})\).
* Space: \(O(N \* K)\). Since we are analyzing based on the structure of list from the input where \(K\) is number of choices for each position and \(N\) position (length of list). Space used to build the options array is \(O(N \cdot K)\). And recursive call can get stack upto \(O(N)\). Therefore \(O(N \* K)\).
  + OR `res` is only used to store the output and is not used for any intermediate operations, so it does not count towards the space complexity. This is different from the previous approaches where `res` temporarily stored strings shorter than length \(K\). Instead, the backtracking approach stores each intermediate string in `tmpStr`, which uses \(O(N)\) space. Likewise, stack space in the recursion equals the maximum number of active functions, and the maximum possible number of active functions is \(N\). Hence, the space complexity equals \(O(N)\).

### [1382/Medium] Balance a Binary Search Tree

#### Problem

* Given the `root` of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
* A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
* Example 1:

```
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
```

* Example 2:

```
Input: root = [2,1,3]
Output: [2,1,3]
```

* Constraints:
  + `The number of nodes in the tree is in the range [1, 104].`
  + `1 <= Node.val <= 105`
* See [problem](https://leetcode.com/problems/balance-a-binary-search-tree) on LeetCode.

#### Solution: Recursive in-order traversal + Rebuild

* Here is the procedure:
  + Recall that BST is a binary tree with ordered elements with inorder traversal. So, flatten original BST into a ascending sorted sequence.
  + Convert ascending sorted sequence into balanced BST by the algorithm in .

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nums = []
        
        def inorder(node,nums):
            '''
            Convert BST to ascending sequence
            '''    
            if node:
                inorder(node.left, nums)
                nums.append(node.val)
                inorder(node.right, nums)
                
        # ----------------------------------------
        
        def sequence_to_balanced_BST(left, right, nums):
            '''
            Convert ascending sequence to balanced BST
            '''
            if left > right:
                # Base case:
                return None
            
            else:
                # General case:
                mid = left + (right - left) // 2

                # start from the middle (since in a BBST, the root node holds the center sorted value)
                root = TreeNode(nums[mid])

                # assign all lower values than the middle to the left tree
                root.left = sequence_to_balanced_BST(left, mid-1, nums)
                # assign all higher values than the middle to the right tree
                root.right = sequence_to_balanced_BST(mid+1, right, nums)

                return root
        
        # ----------------------------------------
        # Flatten original BST into a ascending sorted sequence.
        inorder(root, nums)
        
        # Convert ascending sorted sequence into balanced BST
        return sequence_to_balanced_BST(left = 0, right = len(nums)-1, nums = nums)
```

* Same approach; concise:

```
class Solution(object):
    # We need to sort the distinct nodes of the BST by using inorder traversal
    def balanceBST(self, root):
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        nums = inorder(root) # Because the function returns a list, we assign that list to variable nums for later uses
        
        def constructBST(nums):
            if len(nums) == 0: # Our list is empty
                return None
            if len(nums) == 1: # Our list has only one element
                return TreeNode(nums[0])
                
            # Here is one illustration before the code:
            # Assuming that we already have a sorted list : [1, 2, 5, 7, 9, 12, 14]
            # The middle value is 7, which is also our very first root
            # root.left will apply the same thought recursively with a sorted list: [1, 2, 5]
            # root.right will apply the same thought recursively with a sorted list: [9, 12, 14]
            # Below is the final code:
            
            mid = len(nums) // 2
            new_node = TreeNode(nums[mid])
            new_node.left = constructBST(nums[:mid])
            new_node.right = constructBST(nums[mid+1:])
            return new_node
        
        return constructBST(nums)
```

##### Complexity

* Time: \(O(n + n) = O(n)\)
* Space: $$O(1)$

### [2002/Medium] Maximum Product of the Length of Two Palindromic Subsequences]

#### Problem

* Given a string `s`, find two disjoint palindromic subsequences of `s` such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.
* Return the maximum possible product of the lengths of the two palindromic subsequences.
* A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.
* Example 1:

```
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
```

* Example 2:

```
Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
```

* Example 3:

```
Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.
```

* Constraints:
  + `2 <= s.length <= 12`
  + `s consists of lowercase English letters only.`
* See [problem](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/) on LeetCode.

#### Solution: Recursive/Top-Down DP

* We have 3 possibilities:
  + Not considering the current char for either subsequence.
  + Considering it for first one.
  + Considering it for second subsequence.

```
class Solution:
    def maxProduct(self, s: str) -> int:
        self.answer = 0
        
        def dfs(i, word, word2):
            if i >= len(s):
                if word == word[::-1] and word2 == word2[::-1]:
                    self.answer = max(len(word) * len(word2), self.answer)
                return
            
            dfs(i + 1, word + s[i], word2) # 1st case
            dfs(i + 1, word, word2 + s[i]) # 2nd case
            dfs(i + 1, word, word2)        # 3rd case
            
        dfs(0, '', '')
        
        return self.answer
```

#### Solution: Recursive/Top-Down DP + Memoization

* Modified solution compared to the above, with an efficient palindrome function (only loop through till the middle) and memoization.
* We have 3 possibilities:
  + Not considering the current char for either subsequence.
  + Considering it for first one.
  + Considering it for second subsequence.

```
class Solution:
    def maxProduct(self, s: str) -> int:
        memo = {}
        
        def isPalindrome(word):
            l, r = 0, len(word)-1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(i, word1, word2):
            if i >= len(s):
                return len(word1) * len(word2) \
                if isPalindrome(word1) and isPalindrome(word2) \
                else float('-inf')

            key = (i, word1, word2)
            if key in memo: 
                return memo[key]            
            
            memo[key] = max([dfs(i + 1, word1, word2),         # 1st case 
                             dfs(i + 1, word1 + s[i], word2),  # 2nd case
                             dfs(i + 1, word1, word2 + s[i])]) # 3rd case
            
            return memo[key]
        
        return dfs(0, '', '')
```

#### Solution: Recursive/Top-Down DP + Memoization

* Modified solution compared to the above, with an efficient palindrome function (only loop through till the middle) and memoization.
* We have 3 possibilities:
  + Not considering the current char for either subsequence.
  + Considering it for first one.
  + Considering it for second subsequence.

```
from functools import lru_cache

class Solution:
    def maxProduct(self, s: str) -> int:
        self.res = 0
        def isPalindrome(word: str) -> bool:
            l, r = 0, len(word)-1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        # If maxsize is set to None, the LRU feature is disabled and the cache can grow without bound.
        @lru_cache(maxsize=None)
        def dfs(i, word1, word2):
            if i >= len(s):
                if isPalindrome(word1) and isPalindrome(word2):
                    self.res = max(self.res, len(word1) * len(word2))
                return
            dfs(i + 1, word1, word2)        # 1st case 
            dfs(i + 1, word1 + s[i], word2) # 2nd case
            dfs(i + 1, word1, word2 + s[i]) # 3rd case
            
        dfs(0, '', '')
        
        return self.res
```

##### Complexity

* Time Complexity: \(O(n\*3^n)\) where \(n\) is the length of the string and the number of options at each stage are 3 (corresponding to the three cases), essentially leading to a 3-ary tree.
* Space Complexity: \(O(n)\). The main consumption of the memory lies in the recursion callstack of the backtracking function. The maximum length of the call stack would be the length of the word. Therefore, the space complexity of the algorithm is \(O(n)\).
