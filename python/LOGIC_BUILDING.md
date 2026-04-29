# Python Logic Building Questions

A structured collection of **270 logic-building questions** in Python, organized by topic and difficulty.
Each topic has **3 levels** — Easy (10) → Medium (10) → Advanced (10).

> **Recommended learning order** (prerequisites first):
> 1. Operators → 2. Conditional Statements → 3. Loops → 4. Functions →
> 5. Data Structures (List, Tuple, Set, Dict) → 6. Map / Filter / Zip → 7. Comprehensions

> **How to use this file**
> - Try to solve **without running code** first — that is what "logic building" means.
> - Then verify by running it.
> - Re-attempt questions you got wrong after a week.

---

## Table of Contents

1. [Operators](#1-operators)
2. [Conditional Statements](#2-conditional-statements)
3. [Loops](#3-loops)
4. [Functions](#4-functions)
5. [Lists](#5-lists)
6. [Tuples](#6-tuples)
7. [Sets](#7-sets)
8. [Dictionaries](#8-dictionaries)
9. [Map, Filter, Zip](#9-map-filter-zip)
10. [Comprehensions (List / Set / Dict)](#10-comprehensions-list--set--dict)

---

## 1. Operators

### Level 1 — Easy (10)

1. Take two numbers from the user and print their sum, difference, product, and quotient.
   _Input:_ `10, 3` → _Output:_ `13, 7, 30, 3.33`
2. Check whether a given number is even or odd using the modulo (`%`) operator.
3. Swap two variables **without** using a third variable (use arithmetic operators).
4. Find the remainder when `n` is divided by `7`.
5. Convert a temperature from Celsius to Fahrenheit using `F = C * 9/5 + 32`.
6. Given two integers, print `True` if both are positive, otherwise `False` (use `and`).
7. Given a number, print `True` if it is divisible by **both** 3 and 5.
8. Find the floor division and true division of two numbers (`//` vs `/`).
9. Compute `2 ** 10` using the exponent operator and print the result.
10. Read a 3-digit number and find the sum of its digits using `//` and `%`.

### Level 2 — Medium (10)

1. Compare two numbers without using `if` — use only comparison/boolean operators to print the larger one (hint: `(a > b) * a + (b >= a) * b`).
2. Given a year, check if it is a leap year using only boolean operators in a single expression.
3. Convert a binary string to its decimal equivalent using bitwise operators only.
4. Given two integers `a` and `b`, swap them using **XOR** (`^`).
5. Check if a number is a power of 2 using `n & (n - 1) == 0`.
6. Set, clear, and toggle the `k`-th bit of a given number.
7. Count the number of set bits (1s) in the binary representation of `n`.
8. Given a float, extract the integer and fractional parts using only operators (no `math` module).
9. Check whether the signs of two integers are the same using the XOR operator.
10. Implement integer multiplication of `a * b` using only addition, comparison, and bit-shift operators.

### Level 3 — Advanced (10)

1. Given an integer `n`, find the lowest set bit using `n & -n`.
2. Without using `if/else`, return the absolute value of an integer using only bit operations.
3. Round a positive float to the nearest integer using only arithmetic operators.
4. Compute `a^b` (exponentiation) in `O(log b)` using bit operations (binary exponentiation).
5. Given two integers, find their average **without** overflow using `(a & b) + ((a ^ b) >> 1)`.
6. Convert a lowercase letter to uppercase (and vice versa) using only the XOR operator.
7. Reverse the bits of a 32-bit unsigned integer.
8. Multiply a number by 7 without using `*` (hint: `(n << 3) - n`).
9. Find the only non-repeating element in an array where every other element repeats twice (use XOR).
10. Given two numbers, compute their sum without using the `+` operator (use `^` and `&` with carry propagation).

---

## 2. Conditional Statements

### Level 1 — Easy (10)

1. Take a number and print whether it is positive, negative, or zero.
2. Check whether a character is a vowel or a consonant.
3. Find the largest of two numbers.
4. Find the largest of three numbers.
5. Check whether a person is eligible to vote (age ≥ 18).
6. Given a percentage, print the grade (A: ≥90, B: ≥75, C: ≥60, D: ≥40, F: otherwise).
7. Check whether a year is a leap year.
8. Given the length of three sides, check whether they form a triangle.
9. Given a number, check whether it is a multiple of 5 but not a multiple of 10.
10. Given the day number (1–7), print the day's name.

### Level 2 — Medium (10)

1. Classify a triangle as equilateral, isosceles, or scalene given three sides.
2. Find the roots of a quadratic equation `ax² + bx + c = 0` (handle real, equal, and complex roots).
3. Given a date `(d, m, y)`, find the next day's date (handle month-end and leap years).
4. Build a basic calculator that takes two numbers and an operator and returns the result.
5. Compute electricity bill: 0–100 units → ₹5/unit, 101–300 → ₹10/unit, 301+ → ₹15/unit.
6. Given an integer between 1 and 12, print the number of days in that month.
7. Given a character, classify it as digit, uppercase letter, lowercase letter, or special character.
8. Given hours and minutes for a movie's duration and start time, compute and print the end time in 24-hour format.
9. Determine whether a chess square (e.g., `e4`) is white or black.
10. Compute income tax using slabs: 0–2.5L → 0%, 2.5–5L → 5%, 5–10L → 20%, 10L+ → 30%.

### Level 3 — Advanced (10)

1. Find the median of three numbers without using a list (only conditionals).
2. Validate a credit card number using the Luhn algorithm.
3. Given a date `(d, m, y)`, compute the day of the week (Zeller's congruence).
4. Validate whether a string is a valid IPv4 address using only string and conditional logic.
5. Given the coordinates of three points, classify them as collinear, forming an acute / right / obtuse triangle.
6. Implement a `rock-paper-scissors-lizard-spock` decision system.
7. Given a person's age, gender, and ticket type, compute fare with multiple discount rules.
8. Given a string time like `"14:35"`, determine the smaller angle between the hour and minute hands of a clock.
9. Decide whether two given rectangles (by `(x1,y1,x2,y2)`) overlap.
10. Implement a state machine for a traffic light cycle that also handles a pedestrian-button override.

---

## 3. Loops

### Level 1 — Easy (10)

1. Print numbers from 1 to N.
2. Print all even numbers from 1 to 50.
3. Compute the sum of the first N natural numbers.
4. Compute the factorial of N.
5. Print the multiplication table of a given number.
6. Count the number of digits in an integer.
7. Reverse an integer (e.g., `1234 → 4321`).
8. Check whether a given number is a palindrome.
9. Find the sum of digits of a number.
10. Print the first N terms of the Fibonacci sequence.

### Level 2 — Medium (10)

1. Print all prime numbers between 1 and N.
2. Check whether a number is an Armstrong number (e.g., `153 = 1³ + 5³ + 3³`).
3. Find the GCD of two numbers using the Euclidean algorithm.
4. Find the LCM of two numbers.
5. Print a right-angled triangle pattern of `*` of height N.
6. Print Pascal's triangle with N rows.
7. Given an integer, find the largest digit in it.
8. Given an integer, count how many digits are even and how many are odd.
9. Print all numbers between 1 and 1000 whose digits sum to a perfect square.
10. Find all pairs `(a, b)` such that `a² + b² = N` for a given N.

### Level 3 — Advanced (10)

1. Print all prime numbers up to N using the Sieve of Eratosthenes.
2. Print the first N Kaprekar numbers (e.g., `45 → 45² = 2025 → 20 + 25 = 45`).
3. Find the smallest number that is divisible by every number from 1 to N.
4. Given N, print all "happy numbers" up to N (replace `n` by sum of squares of digits; eventually reaches 1).
5. Find all the prime factors of N along with their multiplicities.
6. Print a hollow diamond pattern of height N (only borders).
7. Given an integer N, generate the next permutation of its digits in lexicographic order.
8. Implement long division: divide two numbers without using the `/` or `//` operator.
9. Compute the digital root of a number iteratively (sum of digits until single digit).
10. Find the longest sequence of consecutive integers (e.g., `4,5,6`) hidden inside a number's digits.

---

## 4. Functions

### Level 1 — Easy (10)

1. Write a function `add(a, b)` that returns their sum.
2. Write a function `is_even(n)` that returns `True` / `False`.
3. Write a function `factorial(n)` using a loop.
4. Write a function `max_of_three(a, b, c)` that returns the maximum.
5. Write a function `area_of_circle(r)` (use `math.pi`).
6. Write a function `celsius_to_fahrenheit(c)` and its inverse.
7. Write a function `is_prime(n)`.
8. Write a function `reverse_string(s)`.
9. Write a function `count_vowels(s)`.
10. Write a function `power(base, exp)` without using `**`.

### Level 2 — Medium (10)

1. Write a recursive `factorial(n)`.
2. Write a recursive `fibonacci(n)` and analyze why it is slow.
3. Write `gcd(a, b)` recursively.
4. Write a function `is_palindrome(s)` that ignores case and spaces.
5. Write a function with **default arguments** that greets a user.
6. Write a function with `*args` that returns the sum of any number of arguments.
7. Write a function with `**kwargs` that prints key-value pairs nicely.
8. Write a higher-order function `apply(fn, x)` that applies `fn` to `x`.
9. Write a function that returns another function (closure) — e.g., `make_multiplier(n)`.
10. Write a decorator `@timer` that prints how long a function takes to run.

### Level 3 — Advanced (10)

1. Write a memoized `fibonacci(n)` using `functools.lru_cache`, then implement memoization manually.
2. Write a recursive function to compute the power set of a list.
3. Write a recursive function to print all permutations of a string.
4. Write a recursive function to solve the Tower of Hanoi for `n` disks.
5. Write a function `compose(*fns)` that returns the composition of all given functions.
6. Write a generator function `fib_gen()` that yields Fibonacci numbers infinitely.
7. Write a generator function `primes()` that yields prime numbers infinitely (use Sieve of Eratosthenes incrementally).
8. Write a decorator `@retry(times=3)` that re-runs a function on exception.
9. Write a function `curry(f)` that converts `f(a, b, c)` into `f(a)(b)(c)`.
10. Implement a trampoline so a deeply recursive function does not hit Python's recursion limit.

---

## 5. Lists

### Level 1 — Easy (10)

1. Create a list of the first 10 natural numbers and print it.
2. Find the length of a list **without** using `len()`.
3. Find the sum and average of a list of numbers.
4. Find the maximum and minimum of a list **without** using `max()` / `min()`.
5. Reverse a list **without** using `reverse()` or slicing.
6. Count how many times an element appears in a list.
7. Check whether an element exists in a list.
8. Concatenate two lists.
9. Remove duplicates from a list (preserve order).
10. Sort a list of numbers in ascending order without using `sort()` (bubble sort).

### Level 2 — Medium (10)

1. Find the second-largest element in a list (single pass).
2. Rotate a list to the right by `k` positions.
3. Move all zeros in a list to the end while preserving order of non-zeros.
4. Merge two sorted lists into a single sorted list.
5. Find the intersection of two lists (preserve order, no duplicates).
6. Find pairs in a list whose sum equals a given target.
7. Flatten a nested list one level deep.
8. Find the running (prefix) sum of a list.
9. Find the longest strictly-increasing subarray.
10. Given a list of integers, partition it into evens and odds while preserving order.

### Level 3 — Advanced (10)

1. Flatten an arbitrarily-nested list of any depth.
2. Find the majority element in a list (appears more than n/2 times) — Boyer–Moore.
3. Find the contiguous subarray with the maximum sum (Kadane's algorithm).
4. Find all triplets `(a, b, c)` in a list such that `a + b + c == 0`.
5. Implement a sliding-window maximum for window size `k` in `O(n)`.
6. Given two lists representing big integers (digit per cell, least-significant first), add them.
7. Implement quicksort in-place.
8. Given a list of intervals `(start, end)`, merge all overlapping intervals.
9. Given a list, find the next greater element for each element (use a stack — `O(n)`).
10. Find the median of two sorted lists in `O(log(min(m, n)))`.

---

## 6. Tuples

### Level 1 — Easy (10)

1. Create a tuple of 5 elements and print it.
2. Access the first and last elements of a tuple.
3. Find the length of a tuple.
4. Concatenate two tuples.
5. Repeat a tuple `n` times.
6. Check whether an element exists in a tuple.
7. Find the index of an element in a tuple.
8. Count how many times an element appears in a tuple.
9. Convert a list to a tuple and a tuple to a list.
10. Unpack a tuple into multiple variables.

### Level 2 — Medium (10)

1. Given a list of `(name, age)` tuples, sort by age.
2. Given a list of `(x, y)` coordinate tuples, find the one closest to the origin.
3. Swap two variables using tuple packing/unpacking (one line).
4. Use `*rest` unpacking to split `(a, b, c, d, e)` into `a, b, *rest`.
5. Given two tuples of equal length, return a tuple of element-wise sums.
6. Given a list of `(student, marks)` tuples, find the student with the highest marks.
7. Use a tuple as a dictionary key (e.g., `grid[(x, y)] = value`) and demonstrate why a list cannot.
8. Given a tuple of mixed types, separate it into tuples of `int`, `float`, `str`.
9. Implement a function that returns multiple values via a tuple (e.g., min and max).
10. Given a tuple of numbers, return a tuple of running averages.

### Level 3 — Advanced (10)

1. Implement an immutable `Point` class using `collections.namedtuple` and add a `distance` method.
2. Implement an immutable `Point` using `typing.NamedTuple` with type hints — compare with the previous.
3. Use a tuple as a memoization key for a recursive function (e.g., `lru_cache` on `(n, k)`).
4. Group a list of tuples by their first element using `itertools.groupby`.
5. Given a list of `(timestamp, value)` tuples, find the maximum value within any rolling window of `T` seconds.
6. Given two tuples of polynomial coefficients (highest degree first), multiply them.
7. Implement a priority queue using a list of `(priority, item)` tuples and `heapq`.
8. Given an iterable, return all consecutive pairs as tuples (`pairwise` from `itertools`).
9. Use tuples to represent intervals and compute their union/intersection.
10. Given a list of `(x, y, z)` tuples (3D points), find the convex-hull diameter (the two points farthest apart).

---

## 7. Sets

### Level 1 — Easy (10)

1. Create a set from a list and print it (notice duplicates removed).
2. Add an element to a set; try adding a duplicate.
3. Remove an element from a set safely (handle missing key).
4. Find the union of two sets.
5. Find the intersection of two sets.
6. Find the difference (`A - B`) of two sets.
7. Find the symmetric difference (`A ^ B`).
8. Check whether one set is a subset of another.
9. Check whether two sets are disjoint.
10. Convert a string to a set of unique characters.

### Level 2 — Medium (10)

1. Find unique elements common to **three** lists.
2. Given two strings, find characters that appear in either but not both.
3. Check whether two strings are anagrams using sets _and_ explain why a set alone is insufficient (counts matter).
4. Find duplicate elements in a list using a set in a single pass.
5. Given a list of words, find words that share **no** common letters with a given word.
6. Find missing numbers from `1..N` in a given list using sets.
7. Given two lists, return elements unique to each (symmetric difference).
8. Given a list of strings, group anagrams together using `frozenset` of letters as a key.
9. Build a phonebook lookup that returns numbers shared between two contact lists.
10. Find the Jaccard similarity (`|A ∩ B| / |A ∪ B|`) of two sets.

### Level 3 — Advanced (10)

1. Implement a basic spell-checker using a set of valid words and minimum edit distance ≤ 1.
2. Given an undirected graph as edges, count the number of connected components using sets.
3. Given a stream of integers, find the count of distinct elements seen so far in `O(1)` amortized per element.
4. Implement set operations (`union`, `intersection`, `difference`) **without** using built-ins, on top of a custom hash-table.
5. Find the smallest missing positive integer in a list using a set in `O(n)`.
6. Given a list of `frozenset`s representing transactions, find the most frequent itemset of size 2 (a tiny Apriori step).
7. Detect a cycle in a linked list using a set of seen nodes (then redo it without a set — Floyd's algorithm).
8. Given a list of words, find the longest chain `w1 → w2 → ...` where each next word is the previous word with one letter removed.
9. Implement a Bloom filter using bit operations and multiple hash functions; compare false-positive rate with a real `set`.
10. Find the union of `n` intervals `(start, end)` and report the total covered length.

---

## 8. Dictionaries

### Level 1 — Easy (10)

1. Create a dictionary mapping student names to marks and print it.
2. Add, update, and delete a key in a dictionary.
3. Check whether a key exists in a dictionary.
4. Iterate over keys, values, and items of a dictionary.
5. Get a value with a default if the key is missing (`dict.get`).
6. Find the length of a dictionary.
7. Merge two dictionaries (later values win).
8. Convert a list of tuples `[(k, v), ...]` into a dictionary.
9. Convert a dictionary into a list of `(k, v)` tuples.
10. Given a string, count the frequency of each character using a dictionary.

### Level 2 — Medium (10)

1. Count word frequencies in a sentence and return the top 3 most common.
2. Invert a dictionary (swap keys and values) — discuss what happens when values repeat.
3. Group a list of words by their first letter using a dictionary of lists.
4. Given two dictionaries, find keys present in both with different values.
5. Build a simple in-memory phonebook supporting add / search / delete / list.
6. Given a list of `(student, subject, marks)`, build `{student: {subject: marks}}`.
7. Implement `defaultdict` behavior manually (using `dict.setdefault`).
8. Find the key with the maximum value in a dictionary.
9. Sort a dictionary by value (ascending and descending).
10. Given two strings, check whether one is a permutation of the other using dictionaries (counts).

### Level 3 — Advanced (10)

1. Implement an LRU cache (least-recently-used) using `OrderedDict`.
2. Implement an LFU cache (least-frequently-used) using only dicts.
3. Given a list of dependencies `{task: [prereqs...]}`, perform a topological sort (Kahn's algorithm).
4. Implement a simple Trie using nested dictionaries; support `insert`, `search`, `starts_with`.
5. Given a dictionary of currency exchange rates `{(from, to): rate}`, find a path of conversions from `A` to `B` that maximizes the rate (BFS/DFS).
6. Implement a multiset (bag) using a dict `{element: count}` with proper `+`, `-`, and `&` operators.
7. Build an inverted index `{word: set(doc_ids)}` from a list of documents and run AND / OR queries on it.
8. Given a stream, maintain a top-K frequent items using a dict + a heap.
9. Given two trees represented as nested dicts, compute their structural diff.
10. Given an arbitrarily nested dict, flatten it into `{"a.b.c": value}` form and write the inverse function.

---

## 9. Map, Filter, Zip

### Level 1 — Easy (10)

1. Use `map` to square every number in a list.
2. Use `map` to convert a list of strings to uppercase.
3. Use `filter` to keep only even numbers from a list.
4. Use `filter` to keep only words longer than 4 characters.
5. Use `zip` to combine `[1, 2, 3]` and `['a', 'b', 'c']` into `[(1, 'a'), (2, 'b'), (3, 'c')]`.
6. Use `zip` to iterate over two lists in parallel and print pairs.
7. Use `map` with a `lambda` to add 10 to every element of a list.
8. Use `filter` with a `lambda` to keep only positive numbers.
9. Use `zip` with `dict()` to build a dictionary from `keys` and `values` lists.
10. Convert temperatures in Celsius to Fahrenheit using `map`.

### Level 2 — Medium (10)

1. Use `map` with multiple iterables: element-wise sum of two lists.
2. Use `filter` + `map` to get the squares of all even numbers in a list.
3. Use `zip` to transpose a 2D list (list of lists).
4. Given two lists `names` and `marks`, return a list of `(name, marks)` for students who passed (>= 40).
5. Use `map` to convert a list of `"YYYY-MM-DD"` strings to `datetime.date` objects.
6. Given a list of strings, use `filter` to remove empty / whitespace-only ones.
7. Use `zip(*matrix)` to rotate a 2D list 90° clockwise (combine with reversing rows).
8. Use `zip` with `enumerate` to create `[(idx, a, b), ...]` from two lists.
9. Use `map` to parse `"3+4"`, `"7-2"` etc. and return their numerical results.
10. Given two dicts, use `zip` over their `.items()` to find keys that have the same value in both.

### Level 3 — Advanced (10)

1. Implement your own version of `map`, `filter`, and `zip` using generators.
2. Use `zip_longest` from `itertools` to pair two unequal-length lists, filling with `None`.
3. Given many lists, find the element-wise maximum using `map` + `zip`.
4. Use `functools.reduce` together with `map` to compute the dot product of two vectors.
5. Given a list of `(name, score)` tuples, use `map` and `sorted` to rank students and return `(rank, name, score)` tuples.
6. Given a list of dicts (rows), use `map` to project specific columns (like a SQL `SELECT`).
7. Given a list of sentences, use `map` + `filter` to find sentences containing all of a given set of keywords.
8. Use `zip` and `*` unpacking to split a list of `(x, y, z)` tuples into three separate lists.
9. Given two sorted lists, lazily merge them using a generator (yield one element at a time).
10. Implement a pipeline DSL: `pipe(data, map_step(fn), filter_step(pred), reduce_step(op))` where each step is composable.

---

## 10. Comprehensions (List / Set / Dict)

> Mix of list, set, and dict comprehensions. Each must be solved in a **single comprehension expression**.

### Level 1 — Easy (10)

1. **List**: Build `[1, 4, 9, 16, 25]` (squares of 1–5).
2. **List**: Get all even numbers from 1 to 20.
3. **List**: Convert `["hello", "world"]` to uppercase.
4. **Set**: Get unique characters of `"mississippi"`.
5. **Set**: Get unique word lengths from a sentence.
6. **Dict**: Build `{1: 1, 2: 4, 3: 9, ..., 10: 100}`.
7. **Dict**: Build `{c: ord(c) for c in "abc"}`.
8. **List**: Get the first letters of every word in a sentence.
9. **List**: Build `[(x, y) for x, y ...]` of all pairs where `x ∈ [1,2,3]` and `y ∈ ['a','b']`.
10. **Dict**: Invert `{1: 'a', 2: 'b', 3: 'c'}` into `{'a': 1, 'b': 2, 'c': 3}`.

### Level 2 — Medium (10)

1. **List**: From `[1..100]`, build a list of numbers divisible by 3 or 5 but not both.
2. **List**: Flatten a 2D matrix into a 1D list using a nested comprehension.
3. **Dict**: Given a string, build `{char: count}` using a comprehension (and `str.count`).
4. **Set**: From a list of words, build a set of words that contain all 5 vowels.
5. **List**: Generate the first 10 rows of Pascal's triangle as a list of lists.
6. **Dict**: From a list of `(name, age)` tuples, build `{name: age}` keeping only adults (≥18).
7. **List**: Generate all prime numbers up to 50 using a comprehension (with a helper `is_prime`).
8. **Dict**: Given two lists `keys` and `values`, build the dict — but skip keys whose value is `None`.
9. **List**: Transpose a matrix (list of lists) using a nested comprehension.
10. **Set**: Given two strings, compute their common characters using a single comprehension.

### Level 3 — Advanced (10)

1. **Dict**: Given a paragraph, build `{word_length: [words_of_that_length]}` using a comprehension only.
2. **List**: Generate all Pythagorean triples `(a, b, c)` with `a, b, c ≤ 50` using a comprehension.
3. **List**: Implement matrix multiplication of two 2D lists using only nested comprehensions.
4. **Dict**: Given a list of dicts (rows), pivot them into `{column_name: [values...]}`.
5. **Generator**: Write a generator expression that lazily yields all primes (use `next` to get the first 100).
6. **Dict**: Build `{(i, j): i*j for i, j ...}` for a multiplication table — then convert to a 2D list via comprehension.
7. **Set**: Given a list of sentences, build the set of words that appear in **every** sentence (intersection via comprehension + `reduce`).
8. **List**: Sieve of Eratosthenes implemented via a single comprehension chain (helper variable allowed).
9. **Dict**: Given an arbitrarily nested dict, flatten it to `{"a.b.c": v}` form using a recursive comprehension helper.
10. **List**: Generate all valid IP addresses (4 octets of 0–255) that can be formed from a 12-digit string — solve with comprehensions and slicing.

---

## Tips for Logic Building

- **Trace by hand first.** For loops and recursion, simulate the first 2–3 iterations on paper before coding.
- **Draw the data structure.** A dict-of-lists is much clearer when sketched than when imagined.
- **Edge cases matter more than the happy path** — empty input, one element, all duplicates, negative numbers.
- **Time complexity is part of the answer.** For every advanced question, ask: "Can this be done in `O(n)` instead of `O(n²)`?"
- **`pdb` and `print`** are not cheating — they are how professionals debug.

---

_Last updated: 2026-04-29_
