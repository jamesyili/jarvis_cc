# Primers • Python Tips and Tricks

**Source:** https://aman.ai/code/python-tips/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** algorithms

---

* [Python Built-in Methods](#python-built-in-methods)
  + [Strings](#strings)
  + [Using `isinstance()` vs. `type()` for type-checking](#using-isinstance-vs-type-for-type-checking)
    - [Index of a Substring using `str.find()` or `str.index()`](#index-of-a-substring-using-strfind-or-strindex)
    - [Replace a String with Another String Using Regular Expressions](#replace-a-string-with-another-string-using-regular-expressions)
  + [Lists](#lists)
    - [Create a copy of a list using `=` vs. `<list>.copy()`](#create-a-copy-of-a-list-using--vs-listcopy)
    - [Get counter and value while looping using `enumerate()`](#get-counter-and-value-while-looping-using-enumerate)
    - [`list.append()` vs. `list.extend()` vs. `+=`](#listappend-vs-listextend-vs-)
    - [Get Elements](#get-elements)
      * [`random.choice()`: Get a Randomly Selected Element from a List](#randomchoice-get-a-randomly-selected-element-from-a-list)
      * [`random.sample()`: Get Multiple Random Elements from a List](#randomsample-get-multiple-random-elements-from-a-list)
      * [`heapq`: Find `n` Max Values of a List](#heapq-find-n-max-values-of-a-list)
    - [Unpacking](#unpacking)
      * [How to Unpack Iterables](#how-to-unpack-iterables)
      * [Extended Iterable Unpacking: Ignore Multiple Values when Unpacking](#extended-iterable-unpacking-ignore-multiple-values-when-unpacking)
    - [Join Iterables](#join-iterables)
      * [`join()`: Turn an Iterable into a String](#join-turn-an-iterable-into-a-string)
      * [`zip()`: Create Pairs of Elements from Two Iterators](#zip-create-pairs-of-elements-from-two-iterators)
    - [Interaction Between Two Lists](#interaction-between-two-lists)
      * [`set.intersection()`: Find the Intersection Between Two Sets](#setintersection-find-the-intersection-between-two-sets)
      * [`<set>.difference()`: Find the Difference Between Two Sets](#setdifference-find-the-difference-between-two-sets)
      * [`set.union()`: Find the Union Between Two Sets](#setunion-find-the-union-between-two-sets)
    - [Apply Functions to Elements in a List](#apply-functions-to-elements-in-a-list)
      * [`any()`: Check if Any Element of an Iterable is True](#any-check-if-any-element-of-an-iterable-is-true)
      * [`all()`: Check if All Elements of an Iterable Are Strings](#all-check-if-all-elements-of-an-iterable-are-strings)
      * [`filter()`: Get the Elements of an Iterable that a Function Evaluates True](#filter-get-the-elements-of-an-iterable-that-a-function-evaluates-true)
      * [`map()`: Apply a Function to Each Item of an Iterable](#map-apply-a-function-to-each-item-of-an-iterable)
      * [`sort()`: Sort a List of Tuples by the First or Second Item](#sort-sort-a-list-of-tuples-by-the-first-or-second-item)
  + [Tuple](#tuple)
    - [`slice`: Make Your Indices More Readable by Naming Your Slice](#slice-make-your-indices-more-readable-by-naming-your-slice)
  + [Dictionaries](#dictionaries)
    - [Merge two dictionaries](#merge-two-dictionaries)
    - [`max(dict)`](#maxdict)
    - [`dict.get()`: Get the Default Value of a Dictionary if a Key Doesn’t Exist](#dictget-get-the-default-value-of-a-dictionary-if-a-key-doesnt-exist)
    - [`dict.fromkeys()`](#dictfromkeys)
  + [Function](#function)
    - [`**kwargs`: Pass Multiple Arguments to a Function](#kwargs-pass-multiple-arguments-to-a-function)
    - [Decorator in Python](#decorator-in-python)
  + [Classes](#classes)
    - [Abstract Classes: Declare Methods without Implementation](#abstract-classes-declare-methods-without-implementation)
    - [`classmethod`: What is it and When to Use it](#classmethod-what-is-it-and-when-to-use-it)
    - [`getattr`: a Better Way to Get the Attribute of a Class](#getattr-a-better-way-to-get-the-attribute-of-a-class)
    - [`__call__`: Call your Class Instance like a Function](#__call__-call-your-class-instance-like-a-function)
    - [`@staticmethod`: use the function without adding the attributes required for a new instance](#staticmethod-use-the-function-without-adding-the-attributes-required-for-a-new-instance)
    - [Property Decorator: A Pythonic Way to Use Getters and Setters](#property-decorator-a-pythonic-way-to-use-getters-and-setters)
    - [`__str__` and `__repr__`: Create a String Representation of a Python Object¶](#__str__-and-__repr__-create-a-string-representation-of-a-python-object)
    - [`attrs`: Bring Back the Joy of Writing Classes!](#attrs-bring-back-the-joy-of-writing-classes)
  + [Datetime](#datetime)
    - [`datetime` + `timedelta`: Calculate End DateTime Based on Start DateTime and Duration](#datetime--timedelta-calculate-end-datetime-based-on-start-datetime-and-duration)
    - [Use Dates in a Month as the Feature](#use-dates-in-a-month-as-the-feature)
  + [Best Practices](#best-practices)
    - [Use `_` to Ignore Values](#use-_-to-ignore-values)
    - [Python Pass Statement](#python-pass-statement)
  + [Code Speed](#code-speed)
    - [Concurrently Execute Tasks on Separate CPUs](#concurrently-execute-tasks-on-separate-cpus)
    - [Compare The Execution Time Between Two Functions](#compare-the-execution-time-between-two-functions)
* [Python Built-in Libraries](#python-built-in-libraries)
  + [Collections](#collections)
    - [`collections.Counter`: Count The Occurrences of Items in a List](#collectionscounter-count-the-occurrences-of-items-in-a-list)
    - [`namedtuple`: Tuple with Named Fields](#namedtuple-tuple-with-named-fields)
    - [Defaultdict: Return a Default Value When a Key is Not Available](#defaultdict-return-a-default-value-when-a-key-is-not-available)
  + [Itertools](#itertools)
* [Sort the elements in the list by the key](#sort-the-elements-in-the-list-by-the-key)
* [Group elements in the list by the key](#group-elements-in-the-list-by-the-key)
  + [References](#references)
  + [Citation](#citation)

## Python Built-in Methods

* This section covers some useful Python built-in methods and libraries.

### Strings

### Using `isinstance()` vs. `type()` for type-checking

* `isinstance()` caters for inheritance (an instance of a derived class is an instance of a base class, too), while checking for equality of type does not (it demands identity of types and rejects instances of subtypes, a.k.a. subclasses).
* For your code to support inheritance, `isinstance()` is less bad than checking identity of types because it seamlessly supports inheritance. It’s not that `isinstance` is good, mind you—it’s just less bad than checking equality of types. The normal, Pythonic, preferred solution is almost invariably “duck typing”: try using the argument as if it was of a certain desired type, do it in a try/except statement catching all exceptions that could arise if the argument was not in fact of that type (or any other type nicely duck-mimicking it, and in the except clause, try something else (using the argument “as if” it was of some other type).
* `basestring` is, however, quite a special case—a builtin type that exists only to let you use `isinstance()` (both `str` and `unicode` subclass `basestring`). Strings are sequences (you could loop over them, index them, slice them, …), but you generally want to treat them as “scalar” types—it’s somewhat inconvenient (but a reasonably frequent use case) to treat all kinds of strings (and maybe other scalar types, i.e., ones you can’t loop on) one way, all containers (lists, sets, dicts, …) in another way, and `basestring` plus `isinstance()` helps you do that—the overall structure of this idiom is something like:

```
s1 = unicode("test")
s2 = "test"
isinstance(s1, basestring) ## Returns True
isinstance(s2, basestring) ## Returns True
```

* A gotcha with `isinstance()` is that the `bool` datatype is a subclass of the `int` datatype:

```
issubclass(bool, int) ## Returns True
```

#### Index of a Substring using `str.find()` or `str.index()`

* To find the index of a substring in a string, use the `str.find()` method which returns the index of the first occurrence of the substring if found and `-1` otherwise.

```
sentence = "Today is Saturaday"
```

* Find the index of first occurrence of the substring:

```
sentence.find("day") ## Returns 2
sentence.find("nice") ## Returns -1
```

* You can also provide the starting and stopping position of the search:

```
## Start searching for the substring at index 3
sentence.find("day", 3) ## Returns 15
```

* Note that you can also use `str.index()` to accomplish the same result.

#### Replace a String with Another String Using Regular Expressions

* To either replace one string with another string or to change the order of characters in a string, use `re.sub()`.
* `re.sub()` allows you to use a regular expression to specify the pattern of the string you want to swap.
* In the code below, we replace 3/7/2021 with Sunday and replace 3/7/2021 with 2021/3/7.

```
import re

text = "Today is 3/7/2021"
match_pattern = r"(\d+)/(\d+)/(\d+)"

re.sub(match_pattern, "Sunday", text) ## Returns 'Today is Sunday'
re.sub(match_pattern, r"\3-\1-\2", text) ## Returns 'Today is 2021-3-7'
```

### Lists

#### Create a copy of a list using `=` vs. `<list>.copy()`

* When you create a copy of a list using the `=` operator, a change in the second list will lead to the change in the first list. It is because both lists point to the same object.

```
l1 = [1, 2, 3]
l2 = l1 
l2.append(4)
l2 ## Returns [1, 2, 3, 4]
l1 ## Returns [1, 2, 3, 4]

l1 is l2 ## Returns True since they are the same object
```

* Instead of using the `=` operator, use the `copy()` method. Now any changes to the second list will not reflect in the first list.

```
l1 = [1, 2, 3]
l2 = l1.copy()
l2.append(4)
l2 ## Returns [1, 2, 3, 4]
l1 ## Returns [1, 2, 3]
```

#### Get counter and value while looping using `enumerate()`

* Rather than using `for i in range(len(array))` to access both the index and the value of the array, use `enumerate()` instead. It produces the same result but it is much cleaner.

```
arr = ['a', 'b', 'c', 'd', 'e']

## Instead of this
for i in range(len(arr)):
    print(i, arr[i])
## Prints 
## 0 a
## 1 b
## 2 c
## 3 d
## 4 e

## Use this
for i, val in enumerate(arr):
    print(i, val)
## Prints 
## 0 a
## 1 b
## 2 c
## 3 d
## 4 e
```

#### `list.append()` vs. `list.extend()` vs. `+=`

* To add a list to another list, use the `list.append()` method or `+=`. To add elements of a list to another list, use the `list.extend()` method.

```
a = [1, 2, 3]
a.append([4, 5])
a ## Returns [1, 2, 3, [4, 5]]

a = [1, 2, 3]
a.extend([4, 5])
a ## Returns [1, 2, 3, 4, 5]

a = [1, 2, 3]
a += [4, 5]
a ## Returns [1, 2, 3, 4, 5]
```

#### Get Elements

##### `random.choice()`: Get a Randomly Selected Element from a List

* Besides getting a random number, you can also get a random element from a Python list using random. In the code below, “stay at home” was picked randomly from a list of options.

```
import random 

to_do_tonight = ['stay at home', 'attend party', 'do exercise']
random.choice(to_do_tonight) ## Returns 'attend party'
```

##### `random.sample()`: Get Multiple Random Elements from a List

* To get `n` random elements from a list, use `random.sample`.

```
import random

random.seed(1)
nums = [1, 2, 3, 4, 5]
random_nums = random.sample(nums, 2)
random_nums ## Returns [2, 1]
```

##### `heapq`: Find `n` Max Values of a List

* To extract `n` max values from a large Python list, using `heapq` will speed up the code.
* In the code below, using `heapq` is >2x faster than using sorting and indexing. Both methods try to find the max values of a list of 10000 items.

```
import heapq
import random
from timeit import timeit

random.seed(0)
l = random.sample(range(0, 10000), 10000)

def get_n_max_sorting(l: list, n: int):
    l = sorted(l, reverse=True)
    return l[:n]

def get_n_max_heapq(l: list, n: int):
    return heapq.nlargest(n, l)

expSize = 1000
n = 100

time_sorting = timeit("get_n_max_sorting(l, n)", number=expSize,
                        globals=globals())
time_heapq = timeit('get_n_max_heapq(l, n)', number=expSize,
                    globals=globals())

ratio = round(time_sorting/time_heapq, 3)
print(f'Run {expSize} experiments. Using heapq is {ratio} times'
' faster than using sorting')
## Prints Run 1000 experiments. Using heapq is 2.827 times faster than using sorting
```

#### Unpacking

##### How to Unpack Iterables

* To assign items of a Python iterables (such as list, tuple, string) to different variables, you can unpack the iterable like below.

```
nested_arr = [[1, 2, 3], ["a", "b"], 4]
num_arr, char_arr, num = nested_arr
num_arr
## Prints [1, 2, 3]

char_arr
## Prints ['a', 'b']
```

##### Extended Iterable Unpacking: Ignore Multiple Values when Unpacking

* To ignore multiple values when unpacking a Python iterable, add \* to \_ as shown below.
* This is called “Extended Iterable Unpacking” and is available in Python 3.x.

```
a, *_, b = [1, 2, 3, 4]
print(a)
## Prints 1

b
## Prints 4

_
## Prints [2, 3]
```

#### Join Iterables

##### `join()`: Turn an Iterable into a String

* To turn an iterable into a string, use `join()`.
* In the code below, elements are joined in the list fruits using `,` .

```
fruits = ['apples', 'oranges', 'grapes']

fruits_str = ', '.join(fruits)
print(f"Today, I need to get some {fruits_str} in the grocery store")
## Prints "Today, I need to get some apples, oranges, grapes in the grocery store"
```

##### `zip()`: Create Pairs of Elements from Two Iterators

* To to create pairs of elements from two lists use the `zip()` method which aggregates them in a list of tuples.

```
nums = [1, 2, 3, 4]
string = "abcd"
combinations = zip(nums, string)
combinations ## Prints [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

nums = [1, 2, 3, 4]
chars = ['a', 'b', 'c', 'd']

comb = zip(nums, chars)
comb ## Returns [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
```

* You can also unzip the list of tuples back to it’s original form by using `zip(*list_of_tuples)`:

```
nums_2, chars_2 = zip(*comb)
nums_2, chars_2 ## Returns ((1, 2, 3, 4), ('a', 'b', 'c', 'd'))
```

#### Interaction Between Two Lists

##### `set.intersection()`: Find the Intersection Between Two Sets

* To get the common elements between two iterators, convert them to sets then use `set.intersection()` (Python 2) or the `&` operator (Python 3).

```
requirement1 = ['pandas', 'numpy', 'statsmodel']
requirement2 = ['numpy', 'statsmodel', 'sympy', 'matplotlib']

## Python 2
intersection = set.intersection(set(requirement1), set(requirement2))
list(intersection) ## Returns ['statsmodel', 'numpy']

## Python 3
intersection = set(requirement1) & set(requirement2)
list(intersection) ## Returns ['statsmodel', 'numpy']
```

##### `<set>.difference()`: Find the Difference Between Two Sets

* To find the difference between two iterators, convert them to sets then apply `<set>.difference()` (Python 2) or the `-` operator (Python 3) to the sets.

```
a = [1, 2, 3, 4]
b = [1, 3, 4, 5, 6]

## Python 2
## Find elements in a but not in b
diff = set(a).difference(set(b))
list(diff) ## Returns [2]

## Find elements in b but not in a
diff = set(b).difference(set(a))
list(diff) ## Returns [5, 6]

## Python 3
## Find elements in a but not in b
diff = set(a) - set(b)
list(diff) ## Returns [2]

## Find elements in b but not in a
diff = set(b) - set(a)
list(diff) ## Returns [5, 6]
```

##### `set.union()`: Find the Union Between Two Sets

* To get the union of elements from two sets, use `set.union()` (Python 2) or the `|` operator (Python 3).

```
requirement1 = ['pandas', 'numpy', 'statsmodel']
requirement2 = ['numpy', 'statsmodel', 'sympy', 'matplotlib']

## Python 2
union = set.union(set(requirement1), set(requirement2))
list(union) ## Returns ['sympy', 'statsmodel', 'numpy', 'pandas', 'matplotlib']

## Python 3
union = set(requirement1) | set(requirement2)
list(union) ## Returns ['sympy', 'statsmodel', 'numpy', 'pandas', 'matplotlib']
```

#### Apply Functions to Elements in a List

##### `any()`: Check if Any Element of an Iterable is True

* To check if any element of an iterable is True, use `any()`. In the code below, `any()` find if any element in the text is in uppercase.

```
text = "abcdE"
any(c.isupper() for c in text) ## Returns True
```

##### `all()`: Check if All Elements of an Iterable Are Strings

* To check if all elements of an iterable are strings, use `all()` and `isinstance()`.

```
l = ['a', 'b', 1, 2]
all(isinstance(item, str) for item in l) ## Returns False
```

##### `filter()`: Get the Elements of an Iterable that a Function Evaluates True

* To get the elements of an iterable that a function returns true, use `filter()`.
* In the code below, the filter method gets items that are fruits:

```
def get_fruit(val: str):
    fruits = ['apple', 'orange', 'grape']
    return val in fruits

items = ['chair', 'apple', 'water', 'table', 'orange']
fruits = filter(get_fruit, items)
print(list(fruits)) ## Returns ['apple', 'orange']
```

##### `map()`: Apply a Function to Each Item of an Iterable

* To apply the given function to each item of a given iterable, use map.

```
nums = [1, 2, 3]
list(map(str, nums))             ## Returns ['1', '2', '3']

multiply_by_two = lambda num: num * 2
list(map(multiply_by_two, nums)) ## Returns [2, 4, 6]
```

##### `sort()`: Sort a List of Tuples by the First or Second Item

* To sort a list of tuples by the first or second item in a tuple, use the `sort()` method. To specify which item to sort by, use the `key` parameter.

```
prices = [('apple', 3), ('orange', 1), ('grape', 3), ('banana', 2)]

## Sort by the first item
by_letter = lambda x: x[0]
prices.sort(key=by_letter)
prices ## Returns [('apple', 3), ('banana', 2), ('grape', 3), ('orange', 1)]

## Sort by the second item in reversed order
by_price = lambda x: x[1]
prices.sort(key=by_price, reverse=True)
prices ## Returns [('apple', 3), ('grape', 3), ('banana', 2), ('orange', 1)]
```

### Tuple

##### `slice`: Make Your Indices More Readable by Naming Your Slice

* Have you ever been confused when looking into code that contains hardcoded slice indices? Even if you understand it now, you might forget why you choose specific indices in the future.

```
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

some_sum = sum(data[:8]) * sum(data[8:])
```

* If so, name your `slice`. Python provides a nice built-in function for that purpose called `slice`. By using names, your code is much easier to understand.

```
JANUARY = slice(0, 8)
FEBRUARY = slice(8, len(data))
some_sum = sum(data[JANUARY] * sum(data[FEBRUARY]))
print(some_sum) ## Prints 684
```

### Dictionaries

#### Merge two dictionaries

* Starting Python 3.5, you can use dictionary unpacking options:

```
{'a': 1, **{'b': 2}} ## Returns {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}} ## Returns {'a': 2}
```

* Note that if there are overlapping keys in the input dictionaries, the value in the last dictionary for the common key will be stored.
* You can use this idea to merge two dictionaries:

```
d1 = {'a': 1}
d2 = {'b': 2}
{**d1, **d2} ## Returns {'a': 1, 'b': 2}
```

* However, Python 3.9 or greater provides the simplest method to merge two dictionaries:

```
d1 = {'a': 1}
d2 = {'b': 2}
d3 = d1 | d2 ## Returns {'a': 1, 'b': 2}
```

* To merge two dictionaries in Python 3.4 or lower:

```
d1 = {'a': 1}
d2 = {'b': 2}
d2.update(d1) ## Returns {'a': 1, 'b': 2}
```

#### `max(dict)`

* Applying `max` on a Python dictionary will give you the largest key. To find the key with the largest value in a dictionary, utilize the `key` parameter (similar to [`sort`](#sort-key)) in the `max` method in conjunction with [lambda functions](#lambda-functions) or `itemgetter`.

```
from operator import itemgetter

birth_year = {"Ben": 1997, "Alex": 2000, "Oliver": 1995}
max(birth_year) ## Returns "Oliver"

max_val = max(birth_year, key=lambda k: birth_year[k])
max_val         ## Returns "Alex"

max_val = max(birth_year.items(), key=itemgetter(1))
max_val         ## Returns ('Alex', 2000)
max_val[0]      ## Returns "Alex"
```

#### `dict.get()`: Get the Default Value of a Dictionary if a Key Doesn’t Exist

* Refer the [Python 3 Primer](../python3) for examples and use-cases on this topic.

#### `dict.fromkeys()`

* To create a dictionary from a list and a value, use `dict.fromkeys()`. For instance, we can use `dict.fromkeys()` to create a dictionary of furnitures’ locations:

```
furnitures = ['bed', 'table', 'chair']
loc1 = 'IKEA'

furniture_loc = dict.fromkeys(furnitures, loc1)
furniture_loc ## Returns {'bed': 'IKEA', 'table': 'IKEA', 'chair': 'IKEA'}
```

… or create a dictionary of food’s locations:

```
food = ['apple', 'pepper', 'onion']
loc2 = 'ALDI'

food_loc = dict.fromkeys(food, loc2)
food_loc ## Returns {'apple': 'ALDI', 'pepper': 'ALDI', 'onion': 'ALDI'}
```

* These results can be combined into a location dictionary like below:

```
locations = {**food_loc, **furniture_loc}
locations
{'apple': 'ALDI',
 'pepper': 'ALDI',
 'onion': 'ALDI',
 'bed': 'IKEA',
 'table': 'IKEA',
 'chair': 'IKEA'}
```

### Function

#### `**kwargs`: Pass Multiple Arguments to a Function

* Sometimes you might not know the arguments you will pass to a function. If so, use `**kwargs`.
* `**kwargs` allow you to pass multiple arguments to a function using a dictionary. In the example below, passing `**{'a':1, 'b':2}` to the function is similar to passing `a=1, b=1` to the function.
* Once `**kwargs` argument is passed, you can treat it like a Python dictionary.

```
parameters = {'a': 1, 'b': 2}

def example(c, **kwargs):
    print(kwargs)
    for val in kwargs.values():
        print(c + val)

example(c=3, **parameters) 
## Prints 
## {'a': 1, 'b': 2}
## 4
## 5
```

#### Decorator in Python

* Do you want to add the same block of code to different functions in Python? If so, use a decorator!
* In the code below, the decorator tracks the time of the function `say_hello`:

```
import time 

def time_func(func):
    def wrapper():
        print("This happens before the function is called")
        start = time.time()
        func()
        print('This happens after the funciton is called')
        end = time.time()
        print('The duration is', end - start, 's')

    return wrapper
```

* Now all we need to do is to add @time\_func before the function say\_hello.

```
@time_func
def say_hello():
    print("hello")

say_hello()
```

```
- which outputs:
    
```
This happens before the function is called
hello
This happens after the function is called
The duration is 0.0002987384796142578 s
```
```

* Decorator makes the code clean and shortens repetitive code. If we want to track the time of another function, for example, func2(), I can just use:

```
@time_func
def func2():
    pass
func2()
```

```
- which outputs:
    
```
This happens before the function is called
This happens after the funciton is called
The duration is 4.38690185546875e-05 s
from typing import List, Dict
```
```

### Classes

#### Abstract Classes: Declare Methods without Implementation

* Sometimes you might want different classes to use the same attributes and methods. But the implementation of those methods can be slightly different in each class.
* A good way to implement this is to use abstract classes. An abstract class contains one or more abstract methods.
* An abstract method is a method that is declared but contains no implementation. The abstract method requires subclasses to provide implementations.

```
from abc import ABC, abstractmethod 

class Animal(ABC):

    def __init__(self, name: str):
        self.name = name 
        super().__init__()

    @abstractmethod 
    def make_sound(self):
        pass 

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} says: Woof')

class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} says: Meows')

Dog('Pepper').make_sound()
Cat('Bella').make_sound()
## Prints 
## "Pepper says: Woof
## Bella says: Meows"
```

#### `classmethod`: What is it and When to Use it

* When working with a Python class, To create a method that returns that class with new attributes, use `classmethod`.
* Classmethod doesn’t depend on the creation of a class instance. In the code below, `classmethod` instantiates a new object whose attribute is a list of even numbers.

```
class Solver:
    def __init__(self, nums: list):
        self.nums = nums
    
    @classmethod
    def get_even(cls, nums: list):
        return cls([num for num in nums if num % 2 == 0])
    
    def print_output(self):
        print("Result:", self.nums)

## Not using class method       
nums = [1, 2, 3, 4, 5, 6, 7]
solver = Solver(nums).print_output()
## Prints Result: [1, 2, 3, 4, 5, 6, 7]

solver2 = Solver.get_even(nums)
solver2.print_output()
## Prints Result: [2, 4, 6]
```

#### `getattr`: a Better Way to Get the Attribute of a Class

* To get a default value when calling an attribute that is not in a class, use `getattr()` method.
* The `getattr(class, attribute_name)` method simply gets the value of an attribute of a class. However, if the attribute is not found in a class, it returns the default value provided to the function.

```
class Food:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

apple = Food("apple", "red")

print("The color of apple is", getattr(apple, "color", "yellow"))
## Prints "The color of apple is red"

print("The flavor of apple is", getattr(apple, "flavor", "sweet"))
## Prints "The flavor of apple is sweet"

print("The flavor of apple is", apple.sweet)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/tmp/ipykernel_337430/3178150741.py in <module>
----> 1 print("The flavor of apple is", apple.sweet)

AttributeError: 'Food' object has no attribute 'sweet'
```

#### `__call__`: Call your Class Instance like a Function

* To call your class instance like a function, add the `__call__()` method to your class.

```
class DataLoader:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        print("Instance is created")

    def __call__(self):
        print("Instance is called")

data_loader = DataLoader("my_data_dir")
## Instance is created

data_loader()
## Instance is called

Instance is created
Instance is called
```

#### `@staticmethod`: use the function without adding the attributes required for a new instance

* Have you ever had a function in your class that doesn’t access any properties of a class but fits well in a class? You might find it redundant to instantiate the class to use that function. That is when you can turn your function into a static method.

All you need to turn your function into a static method is the decorator `@staticmethod`. Now you can use the function without adding the attributes required for a new instance.

```
import re

class ProcessText:
    def __init__(self, text_column: str):
        self.text_column = text_column

    @staticmethod
    def remove_URL(sample: str) -> str:
        """Replace url with empty space"""
        return re.sub(r"http\S+", "", sample)

text = ProcessText.remove_URL("My favorite page is https://www.google.com")
print(text) ## Prints "My favorite page is "
```

#### Property Decorator: A Pythonic Way to Use Getters and Setters

* If you want users to use the right data type for a class attribute or prevent them from changing that attribute, use the property decorator.
* In the code below, the first color method is used to get the attribute color and the second color method is used to set the value for the attribute color.

```
class Fruit:
    def __init__(self, name: str, color: str):
        self._name = name
        self._color = color

    @property
    def color(self):
        print("The color of the fruit is:")
        return self._color

    @color.setter
    def color(self, value):
        print("Setting value of color...")
        if self._color is None:
            if not isinstance(value, str):
                raise ValueError("color must be of type string")
            self.color = value
        else:
            raise AttributeError("Sorry, you cannot change a fruit's color!")

fruit = Fruit("apple", "red")
fruit.color

## Prints The color of the fruit is:
#'red'

fruit.color = "yellow"
Setting value of color...

## ---------------------------------------------------------------------------
## AttributeError                            Traceback (most recent call last)
## /tmp/ipykernel_337430/2513783301.py in <module>
## ----> 1 fruit.color = "yellow"
## 
## /tmp/ipykernel_337430/2891187161.py in color(self, value)
##      17             self.color = value
##      18         else:
## ---> 19             raise AttributeError("Sorry, you cannot change a fruit's color!")
##      20 
##      21 
## AttributeError: Sorry, you cannot change a fruit's color!
```

#### `__str__` and `__repr__`: Create a String Representation of a Python Object¶

* To create a string representation of an object, add `__str__` and `__repr__`.
* `__str__` shows readable outputs when printing the object. `__repr__` shows outputs that are useful for displaying and debugging the object.

```
class Food:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.color} {self.name}"

    def __repr__(self):
        return f"Food({self.color}, {self.name})"

food = Food("apple", "red")

## Invokes __str__()
print(food) ## Prints "red apple"

## Invokes __repr__()
food ## Prints Food(red, apple)
```

#### `attrs`: Bring Back the Joy of Writing Classes!

* Do you find it annoying to write an `__init__()` method every time you want to create a class in Python?

```
class Dog:
    def __init__(self, age: int, name: str, type_: str = 'Labrador Retriever'):
        self.age = age 
        self.name = name
        self.type_ = type_
        
    def describe(self):
        print(f"{self.name} is a {self.type_}.")
```

* If so, try `attrs`. With `attrs`, you can declaratively define the attributes of a class.

```
import attr

@attr.s(auto_attribs=True)
class Dog:
    age: int
    name: str
    type_: str = "Labrador Retriever"

    def describe(self):
        print(f"{self.name} is a {self.type_}.")

pepper = Dog(7, "Pepper", "Labrador Retriever")
```

* The instance created using `attrs` has a nice human-readable `__repr__()`.

```
pepper ## Returns Dog(age=7, name='Pepper', type_='Labrador Retriever')
pepper.describe() Pepper is a Labrador Retriever.
```

* You can also turn the attributes of that instance into a dictionary.

```
attr.asdict(pepper)
{'age': 7, 'name': 'Pepper', 'type_': 'Labrador Retriever'}
```

* You can also compare two instances of the same class using the first attribute of that class.

```
bim = Dog(8, 'Bim Bim', 'Dachshund')

pepper < bim ## Returns True
```

* Find other benefits of `attrs` [here](https://www.attrs.org/en/stable/overview.html).

### Datetime

#### `datetime` + `timedelta`: Calculate End DateTime Based on Start DateTime and Duration

* Provided an event starts at a certain time and takes a certain number of minutes to finish, how do you determine when it ends?
* Taking the sum of `datetime` and `timedelta` (minutes) does the trick!

```
from datetime import date, datetime, timedelta

beginning = '2020/01/03 23:59:00'
duration_in_minutes = 2500

## Find the beginning time
beginning = datetime.strptime(beginning, '%Y/%m/%d %H:%M:%S')

## Find duration in days
days = timedelta(minutes=duration_in_minutes)

## Find end time
end = beginning + days 
end ## Returns datetime.datetime(2020, 1, 5, 17, 39)
```

#### Use Dates in a Month as the Feature

* Have you ever wanted to use dates in a month as the feature in your time series data? You can find the days in a month by using calendar.monthrange(year, month)[1] like below.

```
import calendar 

calendar.monthrange(2020, 11)[1] ## Returns 30
```

### Best Practices

* This section includes some best practices to write Python code.

#### Use `_` to Ignore Values

* When assigning the values returned from a function, you might want to ignore some values that are not used in future code. If so, assign those values to underscores `_`.

```
def return_two():
    return 1, 2

_, var = return_two()
var ## Returns 2
```

* If you want to repeat a loop a specific number of times but don’t care about the index, you can also use `_`.

```
for _ in range(5):
    print('Hello')
## Prints 
## Hello
## Hello
## Hello
## Hello
## Hello
```

#### Python Pass Statement

* If you want to create code that does a particular thing but don’t know how to write that code yet, put that code in a function then use pass.
* Once you have finished writing the code in a high level, start to go back to the functions and replace pass with the code for that function. This will prevent your thoughts from being disrupted.

```
def say_hello():
    pass 

def ask_to_sign_in():
    pass 

def main(is_user: bool):
    if is_user:
        say_hello()
    else:
        ask_to_sign_in()

main(is_user=True)
```

### Code Speed

* This section will show you some ways to speed up or track the performance of your Python code.

#### Concurrently Execute Tasks on Separate CPUs

* If you want to concurrently execute tasks on separate CPUs to run faster, consider using `joblib.Parallel`. It allows you to easily execute several tasks at once, with each task using its own processor.

```
from joblib import Parallel, delayed
import multiprocessing

def add_three(num: int):
    return num + 3

num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(add_three)(i) for i in range(10))
results ## Returns [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

#### Compare The Execution Time Between Two Functions

* If you want to compare the execution time between two functions, try `timeit.timeit()`. You can also specify the number of times you want to rerun your function to get a better estimation of the time.

```
import time 
import timeit 

def func():
    """comprehension"""
    l = [i for i in range(10_000)]

def func2():
    """list range"""
    l = list(range(10_000))

expSize = 1000
time1 = timeit.timeit(func, number=expSize)
time2 = timeit.timeit(func2, number=expSize)

print(time1/time2) ## Prints 2.6299518653018685
```

* From the result, we can see that it is faster to use list range than to use list comprehension on average.

## Python Built-in Libraries

* This section covers Python Built-in libraries such as `collections`, `functools`, and `itertools`.

### Collections

* `collections` is a built-in Python library to deal with Python dictionary efficiently. This section will show you some useful methods of this module.

#### `collections.Counter`: Count The Occurrences of Items in a List

* Counting the occurrences of each item in a list using a for-loop is slow and inefficient.

```
char_list = ['a', 'b', 'c', 'a', 'd', 'b', 'b']
def custom_counter(list_: list):
    char_counter = {}
    for char in list_:
        if char not in char_counter:
            char_counter[char] = 1
        else: 
            char_counter[char] += 1

    return char_counter
custom_counter(char_list) ## Returns {'a': 2, 'b': 3, 'c': 1, 'd': 1}
```

* Using `collections.Counter` is more efficient, and all it takes is one line of code!

```
from collections import Counter

Counter(char_list) ## Returns Counter({'a': 2, 'b': 3, 'c': 1, 'd': 1})
```

* In my experiment, using Counter is >2x times faster than using a custom counter.

```
from timeit import timeit
import random 

random.seed(0)
num_list = [random.randint(0, 22) for _ in range(1000)]

numExp = 100
custom_time = timeit("custom_counter(num_list)", globals=globals())
counter_time = timeit("Counter(num_list)", globals=globals())
print(custom_time/counter_time) ## Returns 2.6199148843686806
```

* To get the most frequently occurring element in the list:

```
from collections import Counter

a = [1, 2, 3, 5, 4, 2, 3, 1, 5, 4, 5]
print(Counter(a).most_common(1)[0][0]) ## Returns 5
print(max(set(a), key = a.count))      1## Another way; also returns 5
```

#### `namedtuple`: Tuple with Named Fields

* If you need to create creating a tuple with named fields, consider using `namedtuple`:

```
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22) ## Instantiate with positional or keyword arguments
p[0] + p[1]         ## Returns 33; indexable like the plain tuple (11, 22)
x, y = p            ## Unpack like a regular tuple
x, y                ## Returns (11, 22)
p.x + p.y           ## Returns 33; Fields also accessible by name
p                   ## Returns Point(x=11, y=22); readable __repr__ with a name=value style
```

#### Defaultdict: Return a Default Value When a Key is Not Available

* If you want to create a Python dictionary with default value, use `defaultdict`. When calling a key that is not in the dictionary, the default value is returned.

```
from collections import defaultdict

classes = defaultdict(lambda: 'Outside')
classes['Math'] = 'B23'
classes['Physics'] = 'D24'
classes['Math'] ## Returns 'B23'
classes['English'] ## Returns 'Outside'
```

* Note that the first argument to `defaultdict` which is `default_factory`, requires a callable, which implies either a class or a function.
* You could also achieve similar functionality using `dict.get()`](), however note that this requires specifying the default value at every fetch-item call rather than once when defining the dictionary.

```
classes = {}
classes.get("English", "Outside") ## Returns 'Outside'
```

### Itertools

* `itertools`[https://docs.python.org/3/library/itertools.html] is a built-in Python library that creates iterators for efficient looping. This section will show you some useful methods of itertools.

3.2.1. itertools.combinations: A Better Way to Iterate Through a Pair of Values in a Python List¶
If you want to iterate through a pair of values in a list and the order does not matter ((a,b) is the same as (b, a)), a naive approach is to use two for-loops.

num\_list = [1, 2, 3]
for i in num\_list:
for j in num\_list:
if i < j:
print((i, j))
(1, 2)
(1, 3)
(2, 3)
However, using two for-loops is lengthy and inefficient. Use itertools.combinations instead:

from itertools import combinations

comb = combinations(num\_list, 2) ## use this
for pair in list(comb):
print(pair)
(1, 2)
(1, 3)
(2, 3)
3.2.2. itertools.product: Nested For-Loops in a Generator Expression¶
Are you using nested for-loops to experiment with different combinations of parameters? If so, use itertools.product instead.

itertools.product is more efficient than nested loop because product(A, B) returns the same as ((x,y) for x in A for y in B).

from itertools import product

params = {
“learning\_rate”: [1e-1, 1e-2, 1e-3],
“batch\_size”: [16, 32, 64],
}

for vals in product(\*params.values()):
combination = dict(zip(params.keys(), vals))
print(combination)
{‘learning\_rate’: 0.1, ‘batch\_size’: 16}
{‘learning\_rate’: 0.1, ‘batch\_size’: 32}
{‘learning\_rate’: 0.1, ‘batch\_size’: 64}
{‘learning\_rate’: 0.01, ‘batch\_size’: 16}
{‘learning\_rate’: 0.01, ‘batch\_size’: 32}
{‘learning\_rate’: 0.01, ‘batch\_size’: 64}
{‘learning\_rate’: 0.001, ‘batch\_size’: 16}
{‘learning\_rate’: 0.001, ‘batch\_size’: 32}
{‘learning\_rate’: 0.001, ‘batch\_size’: 64}
3.2.3. itertools.starmap: Apply a Function With More Than 2 Arguments to Elements in a List¶
map is a useful method that allows you to apply a function to elements in a list. However, it can’t apply a function with more than one argument to a list.

def multiply(x: float, y: float):
return x \* y
nums = [(1, 2), (4, 2), (2, 5)]
list(map(multiply, nums))
—————————————————————————
TypeError Traceback (most recent call last)
/tmp/ipykernel\_38110/240000324.py in 
1 nums = [(1, 2), (4, 2), (2, 5)]
----> 2 list(map(multiply, nums))

TypeError: multiply() missing 1 required positional argument: ‘y’
To apply a function with more than 2 arguments to elements in a list, use itertools.starmap. With starmap, elements in each tuple of the list nums are used as arguments for the function multiply.

from itertools import starmap

list(starmap(multiply, nums))
[2, 8, 10]
3.2.4. itertools.compress: Filter a List Using Booleans¶
Normally, you cannot filter a list using a list.

fruits = [‘apple’, ‘orange’, ‘banana’, ‘grape’, ‘lemon’]
chosen = [1, 0, 0, 1, 1]
fruits[chosen]
—————————————————————————
TypeError Traceback (most recent call last)
/tmp/ipykernel\_40588/2755098589.py in 
1 fruits = ['apple', 'orange', 'banana', 'grape', 'lemon']
2 chosen = [1, 0, 0, 1, 1]
----> 3 fruits[chosen]

TypeError: list indices must be integers or slices, not list
To filter a list using a list of booleans, use itertools.compress instead

from itertools import compress

list(compress(fruits, chosen))
[‘apple’, ‘grape’, ‘lemon’]
3.2.5. itertools.groupby: Group Elements in an Iterable by a Key¶
If you want to group elements in a list by a key, use itertools.groupby. In the example below, I grouped elements in the list by the first element in each tuple.

from itertools import groupby

prices = [(‘apple’, 3), (‘orange’, 2), (‘apple’, 4), (‘orange’, 1), (‘grape’, 3)]

key\_func = lambda x: x[0]

## Sort the elements in the list by the key

prices.sort(key=key\_func)

## Group elements in the list by the key

for key, group in groupby(prices, key\_func):
print(key, ‘:’, list(group))
apple : [(‘apple’, 3), (‘apple’, 4)]
grape : [(‘grape’, 3)]
orange : [(‘orange’, 2), (‘orange’, 1)]
3.2.6. itertools.zip\_longest: Zip Iterables of Different Lengths¶
zip allows you to aggregate elements from each of the iterables. However, zip doesn’t show all pairs of elements when iterables have different lengths.

fruits = [‘apple’, ‘orange’, ‘grape’]
prices = [1, 2]
list(zip(fruits, prices))
[(‘apple’, 1), (‘orange’, 2)]
To aggregate iterables of different lengths, use itertools.zip\_longest. This method will fill missing values with fillvalue.

from itertools import zip\_longest
list(zip\_longest(fruits, prices, fillvalue=’-‘))
[(‘apple’, 1), (‘orange’, 2), (‘grape’, ‘-‘)]

### References

* [Python Dictionary Tips](https://colab.research.google.com/github/khuyentran1401/Efficient_Python_tricks_and_tools_for_data_scientists/blob/master/Chapter1/dictionary.ipynb#scrollTo=e1d8987b)
* [Python Implementations of Data Structures](https://betterprogramming.pub/python-implementation-of-data-structures-bfcfa37bfaf1)
* [What are the differences between type() and isinstance()?](https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance)
* [Quora: What is the height, size, and depth of a binary tree?](https://www.quora.com/What-is-the-height-size-and-depth-of-a-binary-tree)
* [What is the time complexity of collections.Counter() in Python?](https://stackoverflow.com/questions/42461840/what-is-the-time-complexity-of-collections-counter-in-python#:~:text=As%20the%20source%20code%20shows,elements%20remain%20O(1).)
* [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
* [Big-O of list slicing](https://stackoverflow.com/questions/13203601/big-o-of-list-slicing)
* [What is the time complexity of slicing a list?](https://www.reddit.com/r/learnpython/comments/kqhcys/what_is_the_time_complexity_of_slicing_a_list/)

### Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledPython3Tips,
  title   = {Python 3 Tips},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
