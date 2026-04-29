# Python Logic Building Questions (Beginner-Friendly)

A collection of **270 logic-building questions** in Python.
Every question is written in **simple English**, has a **clear example**, and includes a **detailed hint** so beginners can understand what to do step by step.

> **Best learning order** (simple things first, then harder things):
> 1. Operators → 2. Conditional Statements (`if/else`) → 3. Loops →
> 4. Functions → 5. Data Structures (List, Tuple, Set, Dict) →
> 6. Map / Filter / Zip → 7. Comprehensions

> **How to use this file**
> 1. Read the question and example carefully.
> 2. Try to solve it **on paper first** (trace each step yourself).
> 3. If you are stuck, read the **Hint**.
> 4. Then write the code in Python and run it.
> 5. Compare your output with the example.
> 6. Come back after a week and try again — that is how logic gets strong.

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

> **What are operators?** Symbols like `+`, `-`, `*`, `/`, `%`, `==`, `and`, `or`, `&`, `|` that take values and give a new value.

### Level 1 — Easy

1. **Add, subtract, multiply, divide two numbers.**
   Take two numbers from the user and print their sum, difference, product, and quotient.
   _Example:_ Input `10, 3` → Output `Sum=13, Diff=7, Product=30, Quotient=3.33`.
   _Hint:_ Use `input()` to read numbers (it gives a string, so wrap with `int()` or `float()`). Then use `+`, `-`, `*`, `/`.

2. **Even or Odd.**
   Read one number and print whether it is even or odd.
   _Example:_ Input `7` → `Odd`. Input `8` → `Even`.
   _Hint:_ A number is even if `n % 2 == 0`. The `%` operator gives the remainder after division.

3. **Swap two numbers without a third variable.**
   Take two numbers `a` and `b`. After swapping, `a` should hold the old `b` and `b` should hold the old `a`.
   _Example:_ `a=5, b=8` → after swap `a=8, b=5`.
   _Hint:_ Do `a = a + b`, then `b = a - b`, then `a = a - b`. Trace it on paper to feel the magic.

4. **Find the remainder.**
   Read a number `n` and print the remainder when it is divided by 7.
   _Example:_ Input `25` → Output `4` (because 25 = 7×3 + 4).
   _Hint:_ Use `n % 7`. The `%` operator is called the "modulo" operator.

5. **Celsius to Fahrenheit.**
   Read a temperature in Celsius and convert it to Fahrenheit.
   _Example:_ Input `0` → Output `32`. Input `100` → Output `212`.
   _Hint:_ The formula is `F = C * 9 / 5 + 32`. Order of operations: `*` and `/` happen before `+`.

6. **Both numbers positive?**
   Read two numbers. Print `True` if both are positive (greater than 0), else `False`.
   _Example:_ Input `5, 3` → `True`. Input `5, -1` → `False`.
   _Hint:_ Use the `and` operator: `a > 0 and b > 0`.

7. **Divisible by both 3 and 5?**
   Read a number. Print `True` if it is divisible by both 3 **and** 5, else `False`.
   _Example:_ Input `15` → `True`. Input `9` → `False`.
   _Hint:_ A number is divisible by `x` when `n % x == 0`. Combine two checks with `and`.

8. **Floor division vs true division.**
   For two numbers, print the result of `/` (true division) and `//` (floor division).
   _Example:_ Input `7, 2` → `3.5` and `3`.
   _Hint:_ `/` always returns a float. `//` throws away the decimal part and returns an integer (or float if inputs are floats).

9. **Power of a number.**
   Print `2` raised to the power `10`.
   _Example:_ Output `1024`.
   _Hint:_ Use the `**` operator: `2 ** 10`.

10. **Sum of digits of a 3-digit number.**
    Read a 3-digit number (like `345`) and print the sum of its three digits (`3 + 4 + 5 = 12`).
    _Example:_ Input `345` → Output `12`.
    _Hint:_ Hundreds digit = `n // 100`. Tens digit = `(n // 10) % 10`. Units digit = `n % 10`.

### Level 2 — Medium

1. **Bigger number without `if`.**
   Print the larger of two numbers using **only** comparison and arithmetic operators (no `if/else`).
   _Example:_ Input `5, 8` → Output `8`.
   _Hint:_ In Python, `True` is `1` and `False` is `0`. So `(a > b) * a + (a <= b) * b` gives the bigger one.

2. **Leap year in one line.**
   Read a year. Print `True` if it is a leap year, else `False`. Solve in **one boolean expression**.
   _Example:_ `2020 → True`, `1900 → False`, `2000 → True`.
   _Hint:_ A leap year is divisible by 4 **and** (not divisible by 100 **or** divisible by 400). Translate that English to `and / or`.

3. **Binary string → decimal (using bit operations).**
   Read a binary string like `"1011"` and print its decimal value (`11`).
   _Example:_ `"1011" → 11`.
   _Hint:_ Walk through each character. For every bit, do `result = (result << 1) | int(bit)`. The `<<` shifts left (multiplies by 2) and `|` adds the bit.

4. **Swap using XOR.**
   Swap two numbers `a` and `b` using only the `^` operator (no `+`, no third variable).
   _Hint:_ `a = a ^ b`, then `b = a ^ b`, then `a = a ^ b`. The XOR of a number with itself is 0; with 0 it returns itself.

5. **Power of 2 check.**
   Read a positive number. Print `True` if it is a power of 2 (1, 2, 4, 8, 16, ...).
   _Example:_ `8 → True`, `12 → False`.
   _Hint:_ A power of 2 has exactly **one** `1` bit. The trick is `n > 0 and (n & (n - 1)) == 0`.

6. **Set, clear, and toggle the k-th bit.**
   Given a number `n` and a position `k`, print `n` after (a) setting bit `k` to 1, (b) clearing it to 0, (c) flipping it.
   _Example:_ `n=10 (1010), k=0` → set: `1011=11`, clear: `1010=10`, toggle: `1011=11`.
   _Hint:_ Set: `n | (1 << k)`. Clear: `n & ~(1 << k)`. Toggle: `n ^ (1 << k)`.

7. **Count the 1s in binary.**
   Read a number. Print how many `1` bits it has in its binary form.
   _Example:_ `13 (1101) → 3`.
   _Hint:_ Loop while `n > 0`: add `n & 1` to a counter, then do `n = n >> 1` (shift right).

8. **Integer and fractional part of a float.**
   Read a float like `3.75`. Print the integer part `3` and the fractional part `0.75`.
   _Hint:_ `int_part = int(x)`. `frac_part = x - int_part`. Watch out for negative numbers.

9. **Same sign or not?**
   Read two integers. Print `True` if both have the same sign (both positive or both negative).
   _Example:_ `(5, 3) → True`, `(-2, 7) → False`.
   _Hint:_ `(a ^ b) >= 0` works because XOR of two numbers with the same sign keeps the sign bit at 0.

10. **Multiply using only `+` and shifts.**
    Multiply two positive integers without using `*`. Use addition and bit-shifts.
    _Example:_ `13 * 5 → 65`.
    _Hint:_ For each bit of `b`, if it is `1`, add `a` (after shifting) to the result. This is how computers multiply at the hardware level.

### Level 3 — Advanced

1. **Lowest set bit.**
   For a number `n`, find the value of its lowest `1` bit.
   _Example:_ `n = 12 (1100) → 4 (0100)`.
   _Hint:_ The trick is `n & -n`. Negative numbers in Python use two's complement, which makes this work.

2. **Absolute value without `if`.**
   Return `|n|` using only bit operations.
   _Hint:_ For 32-bit integers: `mask = n >> 31`, then `(n + mask) ^ mask`. The `mask` is all 1s if negative, all 0s if positive.

3. **Round a positive float without `round()`.**
   Round `x` to the nearest integer using only `+`, `-`, `int()`.
   _Hint:_ `int(x + 0.5)` works for positive numbers. Think why this is true.

4. **Fast exponentiation (`a^b` in O(log b)).**
   Compute `a` raised to `b` faster than the loop method.
   _Hint:_ If `b` is even: `a^b = (a^(b/2))^2`. If odd: `a^b = a * a^(b-1)`. Use the `&1` and `>>1` operators.

5. **Average of two numbers without overflow.**
   Compute `(a+b)/2` in a way that does not overflow even for very big numbers.
   _Hint:_ `(a & b) + ((a ^ b) >> 1)`. The `&` part captures common bits, the `^` shifted right captures different bits.

6. **Toggle letter case using XOR.**
   Convert `'a'` to `'A'` or `'A'` to `'a'` using only XOR.
   _Hint:_ `chr(ord(c) ^ 32)`. The 6th bit (`32`) is the only difference between upper and lower in ASCII.

7. **Reverse all bits of a 32-bit number.**
   Given a 32-bit unsigned integer, reverse the order of its bits.
   _Example:_ `00000010100101000001111010011100 → 00111001011110000010100101000000`.
   _Hint:_ Loop 32 times: pull the lowest bit using `n & 1`, push it onto the result via `result = (result << 1) | bit`, then `n >>= 1`.

8. **Multiply by 7 without `*`.**
   _Hint:_ `7 * n = (n << 3) - n`. Multiplying by 8 is just a shift, then subtract one `n`.

9. **Find the lonely number.**
   Every number in a list appears twice except one. Find that one number.
   _Example:_ `[2, 3, 5, 3, 2] → 5`.
   _Hint:_ XOR everything together. Pairs cancel because `x ^ x = 0`, leaving only the unique number.

10. **Add two numbers without `+`.**
    Use only `^` and `&` and `<<`.
    _Hint:_ `a ^ b` is the sum without carry. `(a & b) << 1` is the carry. Repeat until carry is 0.

---

## 2. Conditional Statements

> **What are conditional statements?** They let your program **decide** what to do based on a condition. The keywords are `if`, `elif`, and `else`.

### Level 1 — Easy

1. **Positive, negative, or zero?**
   Read a number. Print `Positive` if greater than 0, `Negative` if less than 0, or `Zero`.
   _Example:_ `Input: -5 → Negative`.
   _Hint:_ Use `if n > 0: ... elif n < 0: ... else: ...`.

2. **Vowel or consonant.**
   Read a single letter. Print whether it is a vowel (a, e, i, o, u) or a consonant.
   _Example:_ `Input: e → Vowel`.
   _Hint:_ Use `in` operator: `if ch.lower() in "aeiou":`. Lowercase first to handle uppercase input too.

3. **Largest of two numbers.**
   Read two numbers and print the bigger one.
   _Hint:_ One `if` and one `else` is enough. Or use `max(a, b)`.

4. **Largest of three numbers.**
   Read three numbers and print the biggest.
   _Hint:_ Compare `a` with `b` first, then compare the winner with `c`. Three `if` checks are also fine.

5. **Voting eligibility.**
   Read age. Print `Eligible to vote` if age ≥ 18, else `Not eligible`.
   _Hint:_ Just one `if/else`.

6. **Grade calculator.**
   Read percentage. Print grade: `A` if ≥ 90, `B` if ≥ 75, `C` if ≥ 60, `D` if ≥ 40, else `F`.
   _Hint:_ Use `if/elif/elif/elif/else` from highest to lowest. Order matters!

7. **Leap year check.**
   Read a year. Print `Leap` or `Not Leap`.
   _Hint:_ Year is leap if (`year % 4 == 0` AND `year % 100 != 0`) OR `year % 400 == 0`.

8. **Triangle possible?**
   Read three side lengths. Print whether they can form a triangle.
   _Hint:_ Triangle is valid if every side is less than the sum of the other two: `a + b > c and b + c > a and a + c > b`.

9. **Multiple of 5 but not 10.**
   Read a number. Print `True` only if it is divisible by 5 but **not** by 10.
   _Example:_ `15 → True`, `20 → False`.
   _Hint:_ `n % 5 == 0 and n % 10 != 0`.

10. **Day name from day number.**
    Read 1–7 and print the day (1=Monday, ..., 7=Sunday).
    _Hint:_ A long `if/elif` chain works. A list `["Monday", "Tuesday", ..., "Sunday"]` and `days[n-1]` is much shorter.

### Level 2 — Medium

1. **Triangle type.**
   Given three sides, classify the triangle as `Equilateral` (all sides equal), `Isosceles` (two sides equal), or `Scalene` (all different). First check that it is a valid triangle.
   _Hint:_ Compare `a == b`, `b == c`, `a == c`. Use `if`, `elif`, `else`.

2. **Quadratic equation roots.**
   Given `a`, `b`, `c`, find the roots of `ax² + bx + c = 0`. Handle: real and different, real and equal, complex.
   _Hint:_ Calculate the discriminant `D = b*b - 4*a*c`. If `D > 0`: two real roots. `D == 0`: one repeated root. `D < 0`: complex roots. Use `cmath.sqrt` for complex.

3. **Next day's date.**
   Given a date `(d, m, y)`, print the next day's date. Be careful: end of month, end of year, and February in leap years.
   _Example:_ `28-02-2020 → 29-02-2020` (leap year). `31-12-2024 → 01-01-2025`.
   _Hint:_ First make a list of days per month. If today is the last day of the month, reset day to 1 and add 1 to month. If month overflows, reset to 1 and add 1 to year.

4. **Mini calculator.**
   Read two numbers and an operator (`+`, `-`, `*`, `/`). Print the result. Handle division by zero.
   _Hint:_ Use `if op == "+": ... elif ...`. For `/`, check if `b == 0` first and print an error.

5. **Electricity bill.**
   Read units consumed. Calculate bill: 0–100 units → ₹5/unit, 101–300 → ₹10/unit, 301+ → ₹15/unit. Bill is **slab-based** (each slab uses its own rate).
   _Example:_ 250 units → 100×5 + 150×10 = ₹2000.
   _Hint:_ Break units into slabs and add up. Use `if/elif/else`.

6. **Days in a month.**
   Read a month number (1–12) and a year. Print days in that month. Remember February depends on leap year.
   _Hint:_ Months 1, 3, 5, 7, 8, 10, 12 have 31 days. Months 4, 6, 9, 11 have 30. Feb has 28 or 29.

7. **Character classifier.**
   Read one character. Classify it as `Digit`, `Uppercase`, `Lowercase`, or `Special`.
   _Hint:_ Use `c.isdigit()`, `c.isupper()`, `c.islower()`. Or compare ASCII ranges with `ord(c)`.

8. **Movie end time.**
   Given the start time `HH:MM` and the duration in minutes, print the end time in 24-hour format.
   _Example:_ Start `22:30`, duration `90` → End `00:00` (next day).
   _Hint:_ Convert everything to total minutes, add, then convert back. Use `% (24*60)` to wrap around at midnight.

9. **Chess square color.**
   Given a chess position like `"e4"`, print whether the square is `White` or `Black`.
   _Hint:_ Convert the file letter (`a`–`h`) to a number 1–8. If `(file + rank) % 2 == 0`, the square is dark.

10. **Income tax slabs.**
    Given annual income, calculate tax: 0–2.5L → 0%, 2.5–5L → 5%, 5–10L → 20%, above 10L → 30%. Slab-based.
    _Hint:_ Same idea as the electricity bill — split income into chunks and tax each chunk separately.

### Level 3 — Advanced

1. **Median of three numbers (no list).**
   Find the middle value of three numbers using only `if/else`. No `sort`, no list.
   _Hint:_ The median is the one that is **not** the max and **not** the min. Compare pairs to figure out which one.

2. **Luhn check (credit card validation).**
   Given a card number as a string of digits, return `True` if it passes the Luhn check.
   _Hint:_ Starting from the right, double every second digit. If a doubled digit is over 9, subtract 9 from it. Sum all digits. Valid if the total is divisible by 10.

3. **Day of week from a date (Zeller's congruence).**
   Given `(d, m, y)`, compute which day of the week it is.
   _Hint:_ Use the formula: if month is Jan or Feb, treat them as month 13 and 14 of the previous year. Then plug into Zeller's formula. Search "Zeller congruence Python" if you need help.

4. **Validate IPv4 address.**
   Given a string like `"192.168.1.1"`, print whether it is a valid IPv4 address.
   _Hint:_ Split by `.`. Must have exactly 4 parts. Each part must be a number from 0 to 255 with no leading zeros (except `"0"` itself).

5. **Triangle type from points.**
   Given three points `(x1,y1), (x2,y2), (x3,y3)`, classify them as collinear, right-angled, acute, or obtuse triangle.
   _Hint:_ Calculate the squared lengths of all three sides. If they are collinear, area is 0. Use the law of cosines: compare `a² + b²` with `c²` where `c` is the longest side.

6. **Rock-Paper-Scissors-Lizard-Spock.**
   Two players choose. Decide the winner using the rules from Big Bang Theory.
   _Hint:_ Make a dict of what beats what: `{"rock": ["scissors", "lizard"], ...}`. Then check if `p1` is in `wins[p2]` or vice versa.

7. **Discounted ticket fare.**
   Given age, gender, and ticket type (Adult / Senior / Child / Student), compute the fare with multiple discount rules. Define your own rules.
   _Hint:_ Start with a base fare. Apply discounts step by step. Make rules clear in comments.

8. **Clock hand angle.**
   Given a string time like `"03:30"`, find the smaller angle between the hour and minute hands.
   _Example:_ `03:30 → 75°`.
   _Hint:_ Minute hand moves 6° per minute. Hour hand moves 0.5° per minute (30° per hour + extra for the minutes). Take the absolute difference, then `min(angle, 360 - angle)`.

9. **Rectangle overlap.**
   Given two rectangles by `(x1, y1, x2, y2)`, decide if they overlap.
   _Hint:_ They do **not** overlap if one is completely left, right, above, or below the other. So overlap is `not (any of those)`.

10. **Traffic light state machine with pedestrian button.**
    Build a system: lights cycle Green → Yellow → Red. If a pedestrian presses a button while green, the next state should be Yellow (then Red).
    _Hint:_ Keep a state variable. Use `if/elif` to decide the next state. The button is just a flag that overrides the normal flow.

---

## 3. Loops

> **What are loops?** Loops repeat a block of code many times. Python has `for` (when you know how many) and `while` (when you stop on a condition).

### Level 1 — Easy

1. **Print 1 to N.**
   Read N and print numbers from 1 to N each on a new line.
   _Hint:_ `for i in range(1, n + 1): print(i)`. `range(1, n+1)` because the end is **excluded**.

2. **Even numbers from 1 to 50.**
   Print only even numbers from 1 to 50.
   _Hint:_ Two ways: `for i in range(2, 51, 2)` (step of 2), or loop normally and `if i % 2 == 0`.

3. **Sum of first N natural numbers.**
   Read N and print `1 + 2 + ... + N`.
   _Example:_ N=5 → 15.
   _Hint:_ Make a variable `total = 0`, add `i` to it inside the loop.

4. **Factorial of N.**
   `5! = 5 × 4 × 3 × 2 × 1 = 120`.
   _Hint:_ Start with `result = 1` and multiply each `i` from 1 to N.

5. **Multiplication table.**
   Read N. Print its table from N×1 to N×10.
   _Example:_ N=3 → `3 6 9 12 15 18 21 24 27 30`.
   _Hint:_ `for i in range(1, 11): print(n * i)`.

6. **Count digits in a number.**
   Given `12345`, print `5`.
   _Hint:_ Use a `while` loop. Repeatedly divide by 10 (`n = n // 10`) and count until `n == 0`.

7. **Reverse an integer.**
   `1234 → 4321`.
   _Hint:_ `rev = 0`. While `n > 0`: `rev = rev * 10 + n % 10`, then `n = n // 10`.

8. **Palindrome number.**
   A palindrome reads the same forwards and backwards (`121`, `1221`).
   _Hint:_ Reverse the number using the previous question's logic. Compare with the original.

9. **Sum of digits.**
   `123 → 1 + 2 + 3 = 6`.
   _Hint:_ Same `while` loop pattern. `total += n % 10`, then `n //= 10`.

10. **First N Fibonacci numbers.**
    Print: `0, 1, 1, 2, 3, 5, 8, 13, ...`.
    _Hint:_ Keep two variables `a, b = 0, 1`. In each loop print `a`, then update `a, b = b, a + b`.

### Level 2 — Medium

1. **All primes from 1 to N.**
   _Hint:_ For each `i` from 2 to N, check if it has any divisor between 2 and `√i`. If not, it is prime.

2. **Armstrong number.**
   `153 = 1³ + 5³ + 3³`. Check if a number equals the sum of its digits each raised to the count of digits.
   _Hint:_ First count digits. Then sum each digit raised to that count. Compare with the original.

3. **GCD using Euclidean algorithm.**
   _Hint:_ Repeat: `a, b = b, a % b`. When `b == 0`, the GCD is `a`. Trace `gcd(48, 18)` by hand to feel it.

4. **LCM of two numbers.**
   _Hint:_ `LCM(a, b) = (a * b) // GCD(a, b)`. Reuse the GCD function from above.

5. **Triangle pattern of stars.**
   Print a right triangle of `*` of height N.
   _Example:_ N=4
   ```
   *
   **
   ***
   ****
   ```
   _Hint:_ Outer loop for rows. Inner loop prints `i` stars. Or just use string multiplication: `print("*" * i)`.

6. **Pascal's triangle.**
   Print N rows of Pascal's triangle.
   _Hint:_ Each row starts with 1. Each next number is the sum of two numbers above it. Start with `row = [1]`, then build the next row.

7. **Largest digit in a number.**
   `7283 → 8`.
   _Hint:_ Loop through digits using `% 10` and `// 10`. Track the maximum.

8. **Count even and odd digits.**
   `12345 → Even: 2, Odd: 3`.
   _Hint:_ For each digit, check `digit % 2`.

9. **Numbers whose digit sum is a perfect square.**
   Between 1 and 1000, print numbers whose digit sum is a perfect square (1, 4, 9, 16, 25...).
   _Hint:_ Sum digits using `while` loop. Check if `int(s ** 0.5) ** 2 == s`.

10. **All `(a, b)` such that `a² + b² = N`.**
    _Hint:_ Loop `a` from 1 to `√N`. For each `a`, check if `N - a*a` is a perfect square. If yes, print `(a, b)`.

### Level 3 — Advanced

1. **Sieve of Eratosthenes.**
   A faster way to find all primes up to N.
   _Hint:_ Make a boolean list of size N+1, all `True`. Set 0 and 1 to `False`. For each `i` starting at 2, if `i` is still `True`, mark all multiples of `i` (starting at `i*i`) as `False`.

2. **First N Kaprekar numbers.**
   `45² = 2025`, split into `20` and `25`, `20 + 25 = 45`. So 45 is Kaprekar.
   _Hint:_ Square the number. Convert to string. Try all ways to split into two parts. If any sum equals the original, it is Kaprekar.

3. **Smallest number divisible by 1 to N.**
   For N=10, the answer is 2520.
   _Hint:_ Take LCM repeatedly. `result = 1`. For each `i` from 2 to N: `result = LCM(result, i)`.

4. **Happy numbers up to N.**
   Replace `n` with the sum of squares of its digits. Repeat. If you reach `1`, the number is happy. If you cycle, it is not.
   _Hint:_ Use a `set` to remember numbers you have seen. Stop when you see one again or hit 1.

5. **Prime factorization.**
   `60 → 2² × 3 × 5`. Print factors and their counts.
   _Hint:_ For each `i` from 2 upwards, while `n % i == 0`: count `i` and divide `n` by `i`. Stop when `n == 1`.

6. **Hollow diamond pattern.**
   Print a diamond of `*` but only the outer border.
   _Hint:_ Two parts: top half (growing) and bottom half (shrinking). Inside each row, print `*` only at the first and last position; spaces in between.

7. **Next permutation of digits.**
   `1234 → 1243`. Find the next bigger arrangement of the same digits.
   _Hint:_ Walk from the right and find the first digit that is smaller than the digit to its right. Swap it with the smallest digit on its right that is bigger than it. Then sort the part to the right.

8. **Long division.**
   Divide `a` by `b` without using `/` or `//`.
   _Hint:_ Repeatedly subtract `b` from `a` and count how many times you subtracted. That count is the quotient.

9. **Digital root.**
   Keep summing digits until one digit remains. `9999 → 36 → 9`.
   _Hint:_ Use a `while` loop: while `n >= 10`, sum the digits and replace `n`.

10. **Longest run of consecutive digits.**
    In `123459` the longest run is `12345`.
    _Hint:_ Convert to a string. Walk through pairs of neighbors. Track the current run length and the best so far.

---

## 4. Functions

> **What is a function?** A reusable block of code with a name. You **define** it once with `def`, then **call** it many times.

### Level 1 — Easy

1. **`add(a, b)` returns the sum.**
   _Hint:_ `def add(a, b): return a + b`.

2. **`is_even(n)` returns True/False.**
   _Hint:_ `return n % 2 == 0`. The result of a comparison is already a bool.

3. **`factorial(n)` using a `for` loop.**
   _Hint:_ `result = 1`, then loop and multiply.

4. **`max_of_three(a, b, c)`.**
   _Hint:_ Either chain `if/elif`, or just `return max(a, b, c)`.

5. **`area_of_circle(r)`.**
   _Hint:_ `import math` and use `math.pi`. Formula is `π × r²`.

6. **Celsius ↔ Fahrenheit converter.**
   Write two functions, one for each direction.
   _Hint:_ `F = C * 9/5 + 32` and `C = (F - 32) * 5/9`.

7. **`is_prime(n)`.**
   _Hint:_ Handle `n < 2` (return False). Loop from 2 up to `int(n**0.5) + 1`. If any divides `n`, return False.

8. **`reverse_string(s)`.**
   _Hint:_ Easiest: `return s[::-1]`. To practice loops: build a new string char by char.

9. **`count_vowels(s)`.**
   _Hint:_ Loop through chars, increase counter if `c.lower() in "aeiou"`.

10. **`power(base, exp)` without `**`.**
    _Hint:_ Loop `exp` times and multiply.

### Level 2 — Medium

1. **Recursive `factorial(n)`.**
   _Hint:_ Base case: `n == 0 or n == 1 → return 1`. Recursive: `return n * factorial(n - 1)`.

2. **Recursive Fibonacci (and explain why slow).**
   _Hint:_ `fib(n) = fib(n-1) + fib(n-2)`. It is slow because it recomputes the same values many times — try printing inside.

3. **Recursive `gcd(a, b)`.**
   _Hint:_ Base case: `b == 0 → return a`. Recursive: `return gcd(b, a % b)`.

4. **`is_palindrome(s)` ignoring case and spaces.**
   _Hint:_ First clean: `s = s.replace(" ", "").lower()`. Then `return s == s[::-1]`.

5. **Greeting with default arguments.**
   _Hint:_ `def greet(name, msg="Hello"): print(msg, name)`. Calling `greet("Sam")` uses the default.

6. **`*args` to sum any number of inputs.**
   _Hint:_ `def total(*nums): return sum(nums)`. `*args` packs many arguments into a tuple.

7. **`**kwargs` to print keyword arguments.**
   _Hint:_ `def show(**info): for k, v in info.items(): print(k, "=", v)`.

8. **Higher-order `apply(fn, x)`.**
   _Hint:_ `return fn(x)`. Functions are values in Python — you can pass them around.

9. **Closure: `make_multiplier(n)`.**
   _Hint:_ Inside, define another function that uses `n` and return that function. `times3 = make_multiplier(3); times3(10) → 30`.

10. **`@timer` decorator.**
    _Hint:_ A decorator is a function that takes a function and returns a new one. Use `time.time()` before and after to measure.

### Level 3 — Advanced

1. **Memoized Fibonacci.**
   First use `@functools.lru_cache`. Then write your own version using a dictionary.
   _Hint:_ Manual version: keep `cache = {}`. Before computing `fib(n)`, check `if n in cache`. After computing, store it.

2. **Power set of a list (recursive).**
   For `[1, 2]`, return `[[], [1], [2], [1, 2]]`.
   _Hint:_ Power set of `[]` is `[[]]`. For each new element, double the existing list by adding the element to every subset.

3. **All permutations of a string.**
   `"abc" → abc, acb, bac, bca, cab, cba`.
   _Hint:_ For each character, fix it as the first, then recurse on the remaining string.

4. **Tower of Hanoi.**
   Move `n` disks from peg A to peg C using B as helper.
   _Hint:_ Move `n-1` from A to B, move 1 from A to C, move `n-1` from B to C. The recursion writes itself.

5. **`compose(*fns)` returns the composition.**
   _Hint:_ `compose(f, g)(x) = f(g(x))`. Use `functools.reduce` or a small loop to apply all functions right to left.

6. **Generator `fib_gen()`.**
   Use the `yield` keyword to return Fibonacci numbers one at a time forever.
   _Hint:_ `def fib_gen(): a, b = 0, 1\n  while True: yield a; a, b = b, a + b`.

7. **Generator `primes()` (infinite).**
   _Hint:_ Loop forever from 2. For each `n`, check primality (or use an incremental sieve). Yield primes one by one.

8. **`@retry(times=3)` decorator.**
   If the function raises an exception, retry up to N times.
   _Hint:_ Wrap the call in a `try/except` inside a loop. After N failures, re-raise the last exception.

9. **`curry(f)` so `f(a, b, c)` becomes `f(a)(b)(c)`.**
   _Hint:_ Each call should return a new function that remembers the previous arguments. Use closures.

10. **Trampoline for deep recursion.**
    A trick to make deeply recursive functions work without stack overflow.
    _Hint:_ Instead of recursing, return a "thunk" (a function with no args). The trampoline calls the thunk in a loop until it gets a final value.

---

## 5. Lists

> **What is a list?** An ordered, changeable collection of items. Written with `[ ]`. Items can repeat.

### Level 1 — Easy

1. **Build a list of 1–10 and print it.**
   _Hint:_ `list(range(1, 11))`.

2. **Length of a list without `len()`.**
   _Hint:_ Use a `for` loop with a counter variable.

3. **Sum and average.**
   _Hint:_ `total = sum(lst); avg = total / len(lst)`.

4. **Max and min without `max()` / `min()`.**
   _Hint:_ Initialize `mx = lst[0]`. Loop and update if you find a bigger one.

5. **Reverse a list without `reverse()` or `[::-1]`.**
   _Hint:_ Use two pointers (start and end). Swap them and move inwards.

6. **Count occurrences of an element.**
   _Hint:_ Loop through the list, count matches. Or `lst.count(x)`.

7. **Check if an element exists.**
   _Hint:_ `if x in lst:`.

8. **Concatenate two lists.**
   _Hint:_ `a + b` makes a new list. `a.extend(b)` modifies `a`.

9. **Remove duplicates while keeping order.**
   _Hint:_ Make a `seen` set. Loop through; if not in `seen`, add to result and to `seen`.

10. **Bubble sort.**
    _Hint:_ Repeatedly walk the list. If a neighbor is bigger than the next, swap them. Stop when one full pass made no swaps.

### Level 2 — Medium

1. **Second largest in one pass.**
   _Hint:_ Track two variables: `first` and `second`. Update both as you walk through.

2. **Rotate list right by k.**
   `[1,2,3,4,5], k=2 → [4,5,1,2,3]`.
   _Hint:_ Easy way: `lst[-k:] + lst[:-k]`. Use `k = k % len(lst)` to handle big k.

3. **Move zeros to the end.**
   _Hint:_ Walk through. Keep a write-pointer. If element is non-zero, place it at the write-pointer and advance. After loop, fill the rest with zeros.

4. **Merge two sorted lists.**
   _Hint:_ Use two pointers `i` and `j`. Compare `a[i]` and `b[j]`, pick the smaller, advance that pointer.

5. **Intersection (no duplicates, preserve order).**
   _Hint:_ For each item in A, if it is in B and not yet added, add it to result.

6. **Pairs that sum to target.**
   _Hint:_ Use a `set` of seen numbers. For each `x`, check if `target - x` is in the set.

7. **Flatten a one-level nested list.**
   `[[1,2],[3,4]] → [1,2,3,4]`.
   _Hint:_ Use a nested loop, or `[item for sub in lst for item in sub]`.

8. **Running sum.**
   `[1,2,3,4] → [1,3,6,10]`.
   _Hint:_ Keep a `total` variable. Append `total` after each addition.

9. **Longest strictly increasing subarray.**
   _Hint:_ Walk through pairs. Track current run length. When the next element is not greater, reset.

10. **Partition into evens and odds, preserve order.**
    _Hint:_ Two empty lists. Walk through, append to whichever based on `% 2`. Then concatenate.

### Level 3 — Advanced

1. **Flatten any depth nested list.**
   _Hint:_ Recursion. If element is a list, recurse and extend; else append.

2. **Majority element (Boyer–Moore).**
   _Hint:_ Track a candidate and a count. If count is 0, set the candidate. If next equals candidate, increase count, else decrease. The survivor is the majority.

3. **Maximum subarray sum (Kadane).**
   _Hint:_ Walk through. Keep `current_sum = max(x, current_sum + x)`. Track the best `current_sum` seen.

4. **All triplets that sum to zero.**
   _Hint:_ Sort the list. Fix one element. Use two pointers from both ends to find pairs that sum to its negative. Skip duplicates.

5. **Sliding window maximum.**
   For each window of size `k`, find the max in O(n) total.
   _Hint:_ Use a `deque` to keep indices of useful elements in decreasing order. The front is always the current max.

6. **Big integer addition (digit lists).**
   _Hint:_ Walk both lists from the front (least significant). Add digits with a carry.

7. **In-place quicksort.**
   _Hint:_ Pick a pivot. Partition the array so smaller elements are left, larger right. Recurse on both halves.

8. **Merge overlapping intervals.**
   `[(1,3),(2,6),(8,10)] → [(1,6),(8,10)]`.
   _Hint:_ Sort by start. Walk through. If current overlaps with the last in result, merge; else append.

9. **Next greater element using a stack.**
   _Hint:_ Walk from right. Pop the stack while top is ≤ current. The new top (if any) is the answer; push current.

10. **Median of two sorted lists in O(log).**
    _Hint:_ Use binary search to find the partition where the left halves' max is ≤ the right halves' min. This is a hard one — read up on it carefully.

---

## 6. Tuples

> **What is a tuple?** Like a list, but **cannot be changed** after creation. Written with `( )`. Used for fixed groups (like coordinates or records).

### Level 1 — Easy

1. **Make a tuple of 5 items.**
   _Hint:_ `t = (1, 2, 3, 4, 5)`. Or even `t = 1, 2, 3, 4, 5`.

2. **First and last elements.**
   _Hint:_ `t[0]` and `t[-1]`. Negative indices count from the end.

3. **Tuple length.**
   _Hint:_ `len(t)`.

4. **Concatenate two tuples.**
   _Hint:_ `t1 + t2` makes a new tuple.

5. **Repeat tuple n times.**
   _Hint:_ `t * 3`.

6. **Element exists?**
   _Hint:_ `if x in t:`.

7. **Find index of an element.**
   _Hint:_ `t.index(x)`. Throws `ValueError` if not found.

8. **Count occurrences.**
   _Hint:_ `t.count(x)`.

9. **Convert list ↔ tuple.**
   _Hint:_ `tuple(lst)` and `list(t)`.

10. **Unpack a tuple.**
    _Hint:_ `a, b, c = (1, 2, 3)`. Number of variables must match.

### Level 2 — Medium

1. **Sort `(name, age)` tuples by age.**
   _Hint:_ `sorted(lst, key=lambda x: x[1])`. The `key` function tells `sorted` what to compare.

2. **Closest point to origin.**
   _Hint:_ Distance is `√(x² + y²)`. Use `min(points, key=lambda p: p[0]**2 + p[1]**2)`.

3. **One-line swap with tuples.**
   _Hint:_ `a, b = b, a`. Python builds a tuple `(b, a)` and unpacks it.

4. **Star unpacking.**
   _Hint:_ `a, b, *rest = (1, 2, 3, 4, 5)` gives `a=1, b=2, rest=[3,4,5]`.

5. **Element-wise sum of two tuples.**
   _Hint:_ `tuple(x + y for x, y in zip(t1, t2))`.

6. **Student with highest marks.**
   _Hint:_ `max(students, key=lambda s: s[1])`.

7. **Tuple as dict key.**
   _Hint:_ `grid = {}; grid[(2, 3)] = "treasure"`. Lists cannot be keys because they can change; tuples are fine because they cannot.

8. **Separate by type.**
   _Hint:_ Loop through. Use `isinstance(x, int)`, `isinstance(x, float)`, `isinstance(x, str)`.

9. **Function returns multiple values via tuple.**
   _Hint:_ `def min_max(lst): return min(lst), max(lst)`. Caller does `lo, hi = min_max(lst)`.

10. **Running averages.**
    _Hint:_ Keep a running sum and a count. After each element, append `total / count`.

### Level 3 — Advanced

1. **`namedtuple` Point.**
   _Hint:_ `from collections import namedtuple; Point = namedtuple("Point", "x y")`. Then `p = Point(3, 4); p.x`. Add a method using a class that subclasses it.

2. **`typing.NamedTuple` with type hints.**
   _Hint:_ `class Point(NamedTuple): x: int; y: int`. Cleaner than the function form, and supports default values + methods.

3. **Tuple as memoization key.**
   _Hint:_ `@lru_cache(maxsize=None)` works only if all arguments are hashable. Tuples are; lists are not.

4. **Group by first element.**
   _Hint:_ `from itertools import groupby`. **First sort** by the same key, then `groupby`. Without sorting, `groupby` only groups consecutive equal items.

5. **Max value in any T-second window.**
   _Hint:_ Use a deque or two pointers. Slide a window where `right - left ≤ T`. Track the max as you go.

6. **Polynomial multiplication.**
   `(1 + 2x) * (1 + x) = 1 + 3x + 2x²`.
   _Hint:_ Make a new array of size `len(a) + len(b) - 1`. For every `i`, `j`: `result[i + j] += a[i] * b[j]`.

7. **Priority queue with `heapq`.**
   _Hint:_ Push `(priority, item)` tuples. `heappush`, `heappop`. Heap orders by the first tuple element.

8. **Pairwise iterator.**
   `[1,2,3,4] → [(1,2),(2,3),(3,4)]`.
   _Hint:_ `zip(it, it[1:])`. Or use `itertools.pairwise` if Python ≥ 3.10.

9. **Interval union & intersection.**
   _Hint:_ Sort by start. For union, merge as in lists Q8. For intersection, take `max(start)` and `min(end)`; valid if `max(start) ≤ min(end)`.

10. **Convex hull diameter.**
    Find the two points farthest apart in 3D.
    _Hint:_ Brute force is O(n²). Compute squared distance for every pair to avoid `sqrt`. Smarter algorithms exist (rotating calipers) but are advanced.

---

## 7. Sets

> **What is a set?** An **unordered** collection of **unique** items. Written with `{ }`. Great for "is this in there?" and removing duplicates.

### Level 1 — Easy

1. **Set from a list.**
   `[1, 1, 2, 3] → {1, 2, 3}`.
   _Hint:_ `set(lst)`. Duplicates disappear automatically.

2. **Add an element.**
   _Hint:_ `s.add(x)`. Adding a duplicate does nothing.

3. **Remove safely.**
   _Hint:_ `s.discard(x)` does nothing if missing. `s.remove(x)` raises an error if missing.

4. **Union.**
   _Hint:_ `a | b` or `a.union(b)`.

5. **Intersection.**
   _Hint:_ `a & b` or `a.intersection(b)`.

6. **Difference.**
   `A - B` means in A but not in B.
   _Hint:_ `a - b` or `a.difference(b)`.

7. **Symmetric difference.**
   In one set or the other, but not both.
   _Hint:_ `a ^ b`.

8. **Subset check.**
   _Hint:_ `a.issubset(b)` or `a <= b`.

9. **Disjoint sets?**
   No common elements.
   _Hint:_ `a.isdisjoint(b)` or `len(a & b) == 0`.

10. **Unique chars of a string.**
    _Hint:_ `set("hello")`. A string is iterable, so this iterates characters.

### Level 2 — Medium

1. **Common elements in three lists.**
   _Hint:_ `set(a) & set(b) & set(c)`.

2. **Characters in either string but not both.**
   _Hint:_ `set(s1) ^ set(s2)`.

3. **Anagram check (and why a set is not enough).**
   _Hint:_ `set("aab") == set("ab")` is True but they are not anagrams. So compare **sorted strings** or character **counts**, not sets.

4. **Find duplicates in a list (single pass).**
   _Hint:_ Walk through. Use a `seen` set. If element is already in it, mark it as duplicate; else add.

5. **Words sharing no letter with a given word.**
   _Hint:_ `target = set(given)`. Keep words `w` where `set(w).isdisjoint(target)`.

6. **Missing numbers from 1..N.**
   _Hint:_ `set(range(1, n+1)) - set(lst)`.

7. **Symmetric difference of two lists.**
   _Hint:_ `set(a) ^ set(b)`.

8. **Group anagrams using `frozenset` keys.**
   _Hint:_ A `frozenset` is a hashable set, so it can be a dict key. But **`frozenset("aab") == frozenset("ab")`** — for anagrams, prefer a `tuple` of sorted letters or a `tuple` of letter counts as the key.

9. **Common phone numbers between contact lists.**
   _Hint:_ Build sets of phone numbers, take their intersection.

10. **Jaccard similarity.**
    `|A ∩ B| / |A ∪ B|`. A score between 0 and 1.
    _Hint:_ `len(a & b) / len(a | b)`. Watch out for the empty case.

### Level 3 — Advanced

1. **Spell checker (edit distance ≤ 1).**
   _Hint:_ For a word, generate all words obtainable by 1 deletion, 1 insertion, 1 substitution. Check which ones are in the dictionary set.

2. **Connected components in an undirected graph.**
   _Hint:_ Build an adjacency dict. Walk through nodes; if a node is not yet visited, BFS/DFS from it and mark all reachable nodes. Each walk is one component.

3. **Distinct count of a stream.**
   _Hint:_ Just keep a `set` and add each new element. The size is the answer. (For huge streams, use HyperLogLog — beyond beginner.)

4. **Custom set operations on a hash table.**
   _Hint:_ Implement a hash table with chaining. Then `union/intersection/difference` are loops over bucket entries.

5. **Smallest missing positive integer in O(n).**
   _Hint:_ Put all positives in a set. Then loop from 1 upwards until you find one not in the set.

6. **Most frequent itemset of size 2 (Apriori step).**
   _Hint:_ For each transaction, generate all 2-element combinations using `itertools.combinations`. Count them in a dict. Find the max.

7. **Cycle detection in a linked list.**
   _Hint:_ With a set: walk through, store nodes in a set. If you see one again, cycle. Without a set: Floyd's algorithm — slow and fast pointers; if they meet, cycle exists.

8. **Word ladder by removing one letter.**
   _Hint:_ Build a dictionary set. BFS: from each word, remove one letter at every position; if the result is a valid word, follow the chain.

9. **Bloom filter.**
   _Hint:_ A bit array + several hash functions. To add: hash with each function, set those bits. To test: hash, check all bits are set. False positives possible, false negatives not.

10. **Total covered length of intervals.**
    _Hint:_ Same as merging intervals (List Q8). After merging, sum `(end - start)` of each merged interval.

---

## 8. Dictionaries

> **What is a dictionary?** A collection of `key: value` pairs. Written with `{ }`. Lookups are very fast.

### Level 1 — Easy

1. **Create a `name: marks` dict.**
   _Hint:_ `marks = {"Alice": 90, "Bob": 75}`.

2. **Add, update, delete a key.**
   _Hint:_ `d[k] = v` adds/updates. `del d[k]` deletes. `d.pop(k)` deletes and returns the value.

3. **Key exists?**
   _Hint:_ `if k in d:`. Do not use `d.has_key(k)` — that is removed in Python 3.

4. **Iterate keys, values, items.**
   _Hint:_ `for k in d:`, `for v in d.values():`, `for k, v in d.items():`.

5. **Get with default.**
   _Hint:_ `d.get(k, default_value)`. Never raises an error.

6. **Length of dict.**
   _Hint:_ `len(d)` gives the number of keys.

7. **Merge two dicts.**
   _Hint:_ `{**a, **b}` or `a | b` (Python ≥ 3.9). Later values overwrite earlier ones.

8. **List of tuples → dict.**
   _Hint:_ `dict([("a", 1), ("b", 2)])`.

9. **Dict → list of tuples.**
   _Hint:_ `list(d.items())`.

10. **Character frequency.**
    _Hint:_ Loop through chars. `d[c] = d.get(c, 0) + 1`.

### Level 2 — Medium

1. **Top 3 most common words.**
   _Hint:_ Build a frequency dict. Use `sorted(d.items(), key=lambda x: -x[1])[:3]`. Or `Counter(words).most_common(3)`.

2. **Invert a dict.**
   _Hint:_ `{v: k for k, v in d.items()}`. If two keys have the same value, only the last one survives — so this is lossy.

3. **Group words by first letter.**
   _Hint:_ Use `dict.setdefault(first, []).append(word)`. Or `defaultdict(list)`.

4. **Keys with different values in two dicts.**
   _Hint:_ For each shared key, compare values. `{k for k in d1 if k in d2 and d1[k] != d2[k]}`.

5. **In-memory phonebook with add/search/delete/list.**
   _Hint:_ Wrap a dict inside a class. Each operation is one or two lines.

6. **Build `{student: {subject: marks}}` from triples.**
   _Hint:_ Use nested `setdefault`. `result.setdefault(student, {})[subject] = marks`.

7. **Manual `defaultdict`.**
   _Hint:_ `d.setdefault(k, []).append(value)` is the same idea — creates an empty list only if the key is missing.

8. **Key with the maximum value.**
   _Hint:_ `max(d, key=d.get)`. The `key=d.get` tells `max` to compare by values.

9. **Sort a dict by value.**
   _Hint:_ `dict(sorted(d.items(), key=lambda x: x[1]))`. Add `reverse=True` for descending.

10. **Permutation check using counts.**
    _Hint:_ Count each character in both strings. Compare the two count dicts. If equal, they are permutations.

### Level 3 — Advanced

1. **LRU cache with `OrderedDict`.**
   _Hint:_ On every `get`, `move_to_end(key)`. On `put`, if the cache is full, `popitem(last=False)` to remove the oldest.

2. **LFU cache with dicts only.**
   _Hint:_ Keep `value`, `freq`, and a dict-of-OrderedDicts mapping `freq → keys at that freq`. On access, move the key to the next freq bucket.

3. **Topological sort (Kahn's algorithm).**
   _Hint:_ Count incoming edges (`in_degree`) for every task. Start with tasks having `in_degree == 0`. Pop one, output it, decrease the `in_degree` of its neighbors, push neighbors that hit 0.

4. **Trie using nested dicts.**
   _Hint:_ Each node is a dict. Insert: walk char by char, create empty dicts as needed. Search: walk char by char; if any step is missing, return False. Use a special sentinel like `"#"` to mark word ends.

5. **Best currency conversion path.**
   _Hint:_ Build a graph where nodes are currencies and edges are rates. Use BFS/DFS, multiplying rates along the path. Track the best product.

6. **Multiset (bag) class.**
   _Hint:_ Wrap a `Counter`. Implement `__add__` (sum counts), `__sub__` (subtract), `__and__` (min of counts).

7. **Inverted index for AND/OR queries.**
   _Hint:_ For each word, store the set of doc IDs containing it. AND query → intersection. OR query → union.

8. **Top-K frequent items in a stream.**
   _Hint:_ Increment counts in a dict. Maintain a min-heap of size K. When the count of a key exceeds the smallest in the heap, replace.

9. **Diff two trees stored as nested dicts.**
   _Hint:_ Recursive function. For each key in either: missing on one side → "added"/"removed". Both dicts → recurse. Different values → "changed".

10. **Flatten nested dict to dotted keys.**
    `{"a": {"b": 1}} → {"a.b": 1}`. Also write the inverse.
    _Hint:_ Recursion. Carry a `prefix` string. For each key, recurse with `prefix + "." + k`. Inverse: split by `.`, walk into nested dicts creating as you go.

---

## 9. Map, Filter, Zip

> **`map`** applies a function to every item.
> **`filter`** keeps only items where the function returns True.
> **`zip`** pairs items from multiple lists together.

### Level 1 — Easy

1. **Square every number with `map`.**
   _Hint:_ `list(map(lambda x: x*x, nums))`. Wrap with `list()` because `map` returns a special iterator.

2. **Uppercase strings with `map`.**
   _Hint:_ `list(map(str.upper, words))`. You can pass `str.upper` directly — no lambda needed.

3. **Even numbers with `filter`.**
   _Hint:_ `list(filter(lambda x: x % 2 == 0, nums))`.

4. **Words longer than 4 letters.**
   _Hint:_ `list(filter(lambda w: len(w) > 4, words))`.

5. **Zip two lists into pairs.**
   _Hint:_ `list(zip([1,2,3], ['a','b','c']))` → `[(1,'a'), (2,'b'), (3,'c')]`.

6. **Iterate two lists in parallel.**
   _Hint:_ `for a, b in zip(list1, list2): print(a, b)`.

7. **Add 10 to every element with `map` + `lambda`.**
   _Hint:_ `list(map(lambda x: x + 10, nums))`.

8. **Keep positives with `filter`.**
   _Hint:_ `list(filter(lambda x: x > 0, nums))`.

9. **Build dict from two lists.**
   _Hint:_ `dict(zip(keys, values))`.

10. **Celsius to Fahrenheit list.**
    _Hint:_ `list(map(lambda c: c*9/5 + 32, celsius))`.

### Level 2 — Medium

1. **Element-wise sum of two lists with `map`.**
   _Hint:_ `list(map(lambda x, y: x + y, a, b))`. `map` accepts multiple iterables.

2. **Squares of even numbers (filter then map).**
   _Hint:_ `list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))`.

3. **Transpose 2D list using `zip`.**
   `[[1,2],[3,4]] → [[1,3],[2,4]]`.
   _Hint:_ `list(zip(*matrix))`. The `*` unpacks rows as separate arguments.

4. **Pairs of `(name, marks)` for those who passed.**
   _Hint:_ `[(n, m) for n, m in zip(names, marks) if m >= 40]`.

5. **Parse date strings to `date` objects.**
   _Hint:_ `from datetime import date; list(map(date.fromisoformat, strs))`.

6. **Remove empty/whitespace strings.**
   _Hint:_ `list(filter(lambda s: s.strip(), lst))`. An empty string is falsy.

7. **Rotate a 2D list 90° clockwise.**
   _Hint:_ Transpose with `zip(*matrix)`, then reverse each row. Or simpler: `[list(row)[::-1] for row in zip(*matrix)]`.

8. **Indexed pairs from two lists.**
   _Hint:_ `list(enumerate(zip(a, b)))` gives `(index, (a_i, b_i))`. Flatten with a comprehension if needed.

9. **Evaluate simple expressions like "3+4".**
   _Hint:_ Parse each string into two numbers and an operator. Avoid `eval()` for security.

10. **Common keys with same value in two dicts.**
    _Hint:_ `[k for k in d1 if k in d2 and d1[k] == d2[k]]`. `zip` over `.items()` is one way, but a comprehension is simpler.

### Level 3 — Advanced

1. **Re-implement `map`, `filter`, `zip` as generators.**
   _Hint:_ `def my_map(fn, it): yield from (fn(x) for x in it)`. Similar for `filter`. For `zip`, use multiple iterators with `next()`; stop when one runs out.

2. **`zip_longest` for unequal lists.**
   _Hint:_ `from itertools import zip_longest; zip_longest(a, b, fillvalue=None)`.

3. **Element-wise max across many lists.**
   _Hint:_ `list(map(max, zip(*lists)))`. `zip(*lists)` groups all elements at the same index.

4. **Dot product with `reduce` + `map`.**
   _Hint:_ `from functools import reduce; reduce(lambda acc, p: acc + p[0]*p[1], zip(a, b), 0)`. Or just `sum(x*y for x, y in zip(a, b))`.

5. **Rank students.**
   _Hint:_ Sort by score descending. Then `[(rank+1, name, score) for rank, (name, score) in enumerate(sorted_list)]`.

6. **Project columns from list of dicts.**
   _Hint:_ `list(map(lambda row: {k: row[k] for k in cols}, rows))`.

7. **Sentences containing all keywords.**
   _Hint:_ `list(filter(lambda s: all(k in s for k in keywords), sentences))`.

8. **Split list of `(x,y,z)` into three lists.**
   _Hint:_ `xs, ys, zs = zip(*points)`. Then convert to lists if needed.

9. **Lazy merge two sorted lists.**
   _Hint:_ Write a generator. Keep two iterators and a `current` value from each. Yield the smaller, advance that iterator.

10. **Pipeline DSL: `pipe(data, step1, step2, ...)`.**
    _Hint:_ Each step is a function `iterable -> iterable`. `pipe` just calls each step in order. `map_step(fn)` returns a function that does the mapping.

---

## 10. Comprehensions (List / Set / Dict)

> **What is a comprehension?** A short, single-line way to build a list, set, or dict.
> Form: `[expression for item in iterable if condition]`.

### Level 1 — Easy

1. **List**: Squares of 1–5.
   _Expected:_ `[1, 4, 9, 16, 25]`.
   _Hint:_ `[i*i for i in range(1, 6)]`.

2. **List**: Even numbers from 1 to 20.
   _Hint:_ `[i for i in range(1, 21) if i % 2 == 0]`.

3. **List**: Uppercase a list of strings.
   _Hint:_ `[w.upper() for w in words]`.

4. **Set**: Unique chars of `"mississippi"`.
   _Hint:_ `{c for c in "mississippi"}`. Curly braces with no `:` make a set.

5. **Set**: Unique word lengths in a sentence.
   _Hint:_ `{len(w) for w in sentence.split()}`.

6. **Dict**: `{1:1, 2:4, ..., 10:100}`.
   _Hint:_ `{i: i*i for i in range(1, 11)}`.

7. **Dict**: `{c: ord(c) for c in "abc"}`.
   _Hint:_ Just write that expression.

8. **List**: First letter of every word in a sentence.
   _Hint:_ `[w[0] for w in sentence.split()]`.

9. **List**: All `(x, y)` pairs from two lists (cross product).
   _Hint:_ `[(x, y) for x in [1,2,3] for y in ['a','b']]`. Two `for` clauses = nested loop.

10. **Dict**: Invert a small dict.
    _Hint:_ `{v: k for k, v in d.items()}`.

### Level 2 — Medium

1. **List**: Numbers 1–100 divisible by 3 or 5 but not both.
   _Hint:_ Use XOR-like logic: `(i % 3 == 0) != (i % 5 == 0)`.

2. **List**: Flatten a 2D matrix.
   _Hint:_ `[x for row in matrix for x in row]`. Read it as nested loops left to right.

3. **Dict**: Char count using `str.count`.
   _Hint:_ `{c: s.count(c) for c in set(s)}`. Use `set(s)` to avoid recomputing.

4. **Set**: Words that contain all 5 vowels.
   _Hint:_ `{w for w in words if set("aeiou") <= set(w.lower())}`. `<=` is subset.

5. **List**: First 10 rows of Pascal's triangle.
   _Hint:_ Build row by row. A pure comprehension is hard; one helper variable is fine: each new row = `[1] + [a+b for a,b in zip(prev, prev[1:])] + [1]`.

6. **Dict**: Adults from `(name, age)` list.
   _Hint:_ `{n: a for n, a in people if a >= 18}`.

7. **List**: Primes up to 50.
   _Hint:_ `[n for n in range(2, 51) if all(n % d != 0 for d in range(2, int(n**0.5)+1))]`.

8. **Dict**: Skip None values.
   _Hint:_ `{k: v for k, v in zip(keys, values) if v is not None}`.

9. **List**: Transpose a matrix with comprehension.
   _Hint:_ `[[row[c] for row in matrix] for c in range(len(matrix[0]))]`.

10. **Set**: Common chars of two strings.
    _Hint:_ `{c for c in s1 if c in s2}`. Or just `set(s1) & set(s2)`.

### Level 3 — Advanced

1. **Dict**: `{word_length: [words_of_that_length]}` from a paragraph.
   _Hint:_ `{L: [w for w in words if len(w) == L] for L in {len(w) for w in words}}`. Inefficient but clean.

2. **List**: Pythagorean triples up to 50.
   _Hint:_ `[(a,b,c) for a in range(1,51) for b in range(a,51) for c in range(b,51) if a*a+b*b==c*c]`. Notice the `a ≤ b ≤ c` ordering removes duplicates.

3. **List**: Matrix multiplication.
   _Hint:_ `[[sum(a*b for a, b in zip(row, col)) for col in zip(*B)] for row in A]`. `zip(*B)` gives B's columns.

4. **Dict**: Pivot rows to columns.
   `[{a:1, b:2}, {a:3, b:4}] → {a:[1,3], b:[2,4]}`.
   _Hint:_ `{k: [r[k] for r in rows] for k in rows[0]}`.

5. **Generator**: Lazy primes.
   _Hint:_ `def primes_lazy(): ...` is easier than a one-line comprehension. The generator-expression form: `(n for n in itertools.count(2) if is_prime(n))`.

6. **Dict**: Multiplication table as dict, then as 2D list.
   _Hint:_ `{(i,j): i*j for i in range(1,11) for j in range(1,11)}`. To convert: `[[d[(i,j)] for j in range(1,11)] for i in range(1,11)]`.

7. **Set**: Words appearing in every sentence.
   _Hint:_ `from functools import reduce; reduce(lambda a, b: a & b, [set(s.split()) for s in sentences])`.

8. **List**: Sieve of Eratosthenes via comprehension chain.
   _Hint:_ Helper variable allowed. Build the boolean list normally. Then `[i for i, is_p in enumerate(sieve) if is_p]`.

9. **Dict**: Flatten nested dict to `"a.b.c": v`.
   _Hint:_ Recursion needed. Define a helper that returns a list of `(path, value)`. Then `dict(helper(d, ""))`.

10. **List**: All valid IPs from a 12-digit string.
    _Hint:_ `[".".join(parts) for i in range(1,4) for j in range(i+1,i+4) for k in range(j+1,j+4) if all(0<=int(p)<=255 and (p=="0" or not p.startswith("0")) for p in (parts := [s[:i], s[i:j], s[j:k], s[k:]]))]`. Heavy! In real life, write it as a normal nested loop.

---

## Tips for Logic Building (Beginner Friendly)

- **Trace by hand first.** Take a small example, write the variables on paper, and watch them change line by line. This is the single best habit.
- **Draw the data structure.** A list of dicts becomes much clearer when you draw boxes for each.
- **Edge cases matter.** Always ask: what if the input is empty? Has only one element? All duplicates? Negative numbers? Already sorted? Reversed?
- **Time complexity is part of the answer.** For every advanced question, ask: "Can I do this in `O(n)` instead of `O(n²)`?"
- **`print()` is your friend.** Drop print statements anywhere to see what is happening — there is no shame in it.
- **Read the error message.** Python tells you exactly which line and what kind of error. Read it slowly.
- **Same problem, different solutions.** After solving once, try a completely different approach. That is how skill grows.

---

_Last updated: 2026-04-29_
