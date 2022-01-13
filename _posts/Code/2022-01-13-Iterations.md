---
layout:	default
title:	"Iterations"
category:	code
date:	2022-01-13 08:00:00 -0000
permalink:	/code/Python/Iterations
---

## Iterator and Iterable objects
- Iterator is created using the function `iterator_x = iter(range(4))`, which creates an iterator variable whose next value can be used using the function call, `next(iterator_x)`. Everytime `next()` is called it will go to the next value in the iterator
- An Iterable object in Python could be a List, String, range of integers, Dictionaries and many other objects, directly written in for loop as an iterable object. Dictionaries which has a key and a value can be written as `for key,value in my_dictionary.items()` to iterate through each key and corresponding value.

## `enumerate()` and `zip()`

- `enumerate()` function assigns indices, starting from 0, to the list of iterable object passed as the parameter. Adding a `*` before printing, prints all the list of tuples created by `enumerate()`  

```
enum_obj = enumerate(range(4))
print(*enum_obj)
```

prints out: `(0, 0) (1, 1) (2, 2) (3, 3)`

Instead, individual values can be iterated over using a for loop:

```
for x1,x2 in enum_obj:
	print(x1,x2)
```

which prints out:

```
0 0
1 1
2 2
3 3
```
Note that the default index to begin with is zero, but the initial index can be set using the parameter `start=10` (For example)

- `zip()` function zips two iterable objects of same size together, mapping first item of the iterable object to the first ittem of the second iterable object. Unzipping can be done by adding a `*` before the zip object. 
  - Similar to `enumerate()`, `zip()` object also can be unzipped entirely using a `*` before the zip object, or accessed individually using the for loop.

## List comprehensions
- Using a single line of code for running for loop

For example:
```
arms = [1,1.04,0.9]
heights = [arm_length*1.8 for arm_length in arms]
print(heights)
```

has the same output, `heights = [1.8, 1.872, 1.62]` as:
```
arms = [1,1.04,0.9]
heights=[]
for arm_length in arms:
	heights.append(arm_length*1.8)
print(heights)
```
- Dictionary comprehensions work similarly but requires use of curle brackets, and the key and value are separated by a colon, such as `{value:value**2 for value in range(10)}`, creates `value` as keys and square of the `value` as the corresponding values for the keys.
- Conditional formatting can be combined with list comprehensions such as, `heights = [arm_length*1.8 for arm_length in arms if arm_length>=1]` will do the multiplication only when the `arm_length` is greater than 1. Likewise, `[arm_length*1.8 if arm_length>=1 else 0 for arm_length in arms]` have an added else statement if the `arm_length` is not greater than or equal to 1.

## Generators
- For list comprehensions, if we use parenthesis (or rounded brackets), it creates a generator object, which does not create the list until it is called in a for loop or in a `next()` function call.
- They can also be used in functions by using `yield` instead of `return`
