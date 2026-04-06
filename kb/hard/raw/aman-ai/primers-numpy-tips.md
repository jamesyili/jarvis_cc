# Primers • NumPy Tips

**Source:** https://aman.ai/primers/numpy-tips/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Swap rows/columns](#swap-rowscolumns)
* [Reverse rows](#reverse-rows)
* [Reverse columns](#reverse-columns)
* [Filter array based on two or more conditions](#filter-array-based-on-two-or-more-conditions)
* [Find if a given array has any null values](#find-if-a-given-array-has-any-null-values)
* [Count number of 1s in a NumPy array](#count-number-of-1s-in-a-numpy-array)
* [Get indicies of 1s in a NumPy array](#get-indicies-of-1s-in-a-numpy-array)
* [Count number of odd/even numbers in a NumPy array](#count-number-of-oddeven-numbers-in-a-numpy-array)
* [References and credits](#references-and-credits)
* [Citation](#citation)

## Swap rows/columns

```
import numpy as np

a = np.arange(9).reshape(3, 3)

# Create a view of "a" with column 1 and 2 swapped
print(a[:, [1, 0, 2]])
# Prints [[3, 4, 5],
#         [0, 1, 2],
#         [6, 7, 8]]

# Create a view of "a" with rows 1 and 2 swapped
print(a[[1, 0, 2], :])
# Prints [[3, 4, 5],
#         [0, 1, 2],
#         [6, 7, 8]]
# or simply, a[[1, 0, 2]]
# If you're confused about the notation a[[1, 0, 2]] 
# is shorthand for a[[1, 0, 2], :] 

# Swap rows in-place
a[[0, 1]] = a[[1, 0]]
# Again, a[[0, 2]] is shorthand for a[[0, 2], :] 
# so this selects the submatrix consisting of 
# rows 0 and 2. 

# Swap columns in-place
a[:, [0, 1]] = a[:, [1, 0]]
```

## Reverse rows

```
import numpy as np

a = np.arange(9).reshape(3, 3)

print(a[::-1])
# Prints [[6, 7, 8],
#         [3, 4, 5],
#         [0, 1, 2]]
```

## Reverse columns

```
import numpy as np

a = np.arange(9).reshape(3, 3)

print(a[:, ::-1])
# Prints [[2, 1, 0],
#         [5, 4, 3],
#         [8, 7, 6]]
```

## Filter array based on two or more conditions

```
import numpy as np

a = np.arange(9).reshape(3, 3)

a[(a > 1) & (a < 5)] = 0
print(a)
# Prints [[0 1 0]
# 		    [0 0 5]
# 		    [6 7 8]]
```

## Find if a given array has any null values

```
import numpy as np

a = np.arange(9).reshape(3, 3)
print(np.isnan(a))
# Prints [[False False False]
#		  [False False False]
#		  [False False False]]
print(np.isnan(a).any())

a[0, 0] = np.nan
print(np.isnan(a).any())
```

## Count number of 1s in a NumPy array

```
import numpy as np

a = np.array([0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4])

# Method 1: Using a conditional 
print(np.sum(a == 1))                  # 4

# Method 2: using np.unique
unique, counts = np.unique(a, return_counts=True)

# Counter dict
count_dict = dict(zip(unique, counts)) # {0: 7, 1: 4, 2: 1, 3: 2, 4: 1}
count_dict[1]                          # 4
# or print(np.sum(np.where(a % 2 == 1)))
```

## Get indicies of 1s in a NumPy array

```
import numpy as np

a = np.array([0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4])
print(np.where(a == 1)) # (array([ 3,  5,  7, 12]),)
```

## Count number of odd/even numbers in a NumPy array

```
import numpy as np

# Method 1: Using a conditional 
a = np.array([0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4])
# Odd
print(np.sum(a % 2 == 1)) # 6
# Even
print(np.sum(a % 2 == 0)) # 9
```

## References and credits

* [Swap two rows in a NumPy array in Python](https://stackoverflow.com/questions/54069863/swap-two-rows-in-a-numpy-array-in-python/54069951)
* [note.nkmk.me: NumPy](https://note.nkmk.me/en/numpy/)
* [Efficient Python Tricks and Tools for Data Scientists: NumPy](https://khuyentran1401.github.io/Efficient_Python_tricks_and_tools_for_data_scientists/Chapter4/Numpy.html)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledNumPyTips,
  title   = {NumPy Tips},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
