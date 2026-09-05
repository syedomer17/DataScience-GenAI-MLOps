# PostgreSQL Built-in Functions & Expressions

Functions in PostgreSQL are built-in operations that take input values, process them, and return a result. They help you manipulate text, perform mathematical calculations, work with dates, summarize data, and execute conditional logic directly inside your queries.

In this class, we cover 5 core categories:
1. **String Functions** (Text manipulation & formatting)
2. **Numeric & Math Functions** (Calculations, rounding, absolute values)
3. **Date & Time Functions** (Current timestamps, extracting parts, date differences)
4. **Aggregate Functions** (Summarizing rows into a single scalar value)
5. **Conditional Expressions (`CASE`)** (If-Else decision making in SQL)

---

## Sample Table for Practice

To easily run and understand all the examples, imagine we have a `customers` table with sample data:

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    city VARCHAR(50),
    balance NUMERIC(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert Sample Data
INSERT INTO customers (name, age, city, balance, created_at) VALUES
('Syed Omer Ali', 22, 'Karachi', 1450.75, '2024-01-15 10:30:00'),
('Ayesha Khan', 17, 'Lahore', -250.50, '2024-03-20 14:15:00'),
('Bilal Ahmed', 35, 'Karachi', 3200.00, '2023-11-05 09:00:00'),
('Sara Smith', 28, 'Islamabad', 0.00, '2024-06-10 18:45:00'),
('   Zain Malik   ', 45, 'Lahore', 875.20, '2022-08-01 12:00:00'),
('Fatima Noor', 22, 'Karachi', 2100.50, '2023-05-12 11:20:00');
```

### Table Preview:
| id | name | age | city | balance | created_at |
|:---|:---|:---|:---|:---|:---|
| 1 | Syed Omer Ali | 22 | Karachi | 1450.75 | 2024-01-15 10:30:00 |
| 2 | Ayesha Khan | 17 | Lahore | -250.50 | 2024-03-20 14:15:00 |
| 3 | Bilal Ahmed | 35 | Karachi | 3200.00 | 2023-11-05 09:00:00 |
| 4 | Sara Smith | 28 | Islamabad | 0.00 | 2024-06-10 18:45:00 |
| 5 | &nbsp;&nbsp;&nbsp;Zain Malik&nbsp;&nbsp;&nbsp; | 45 | Lahore | 875.20 | 2022-08-01 12:00:00 |
| 6 | Fatima Noor | 22 | Karachi | 2100.50 | 2023-05-12 11:20:00 |

---

## 1. String Functions

String functions are built-in operations used to clean, modify, extract, and format text data stored in database tables.

### 1.1 `UPPER()` and `LOWER()`
- `UPPER(text)`: Converts all letters in a string to uppercase.
- `LOWER(text)`: Converts all letters in a string to lowercase.

```sql
SELECT 
    name, 
    UPPER(name) AS name_uppercase, 
    LOWER(name) AS name_lowercase 
FROM customers;
```

### 1.2 `LENGTH()`
Counts and returns the total number of characters in a string (including spaces).

```sql
SELECT 
    name, 
    LENGTH(name) AS name_length 
FROM customers;
```

### 1.3 `CONCAT()` and the Concatenation Operator (`||`)
Combines two or more text values into a single string.

```sql
-- Using CONCAT()
SELECT CONCAT('Customer: ', name, ' | Age: ', age) AS customer_bio 
FROM customers;

-- Using || operator (standard SQL)
SELECT name || ' (ID: ' || id || ')' AS customer_tag 
FROM customers;
```

### 1.4 `LEFT()` and `RIGHT()`
- `LEFT(text, n)`: Extracts the first `n` characters from the left side of the string.
- `RIGHT(text, n)`: Extracts the last `n` characters from the right side of the string.

```sql
SELECT 
    name,
    LEFT(name, 4) AS first_4_letters,
    RIGHT(name, 4) AS last_4_letters
FROM customers;
```

### 1.5 `SUBSTRING()`
Extracts a portion of a string starting at a specific position for a specified length.

**Syntax:** `SUBSTRING(string, start_position, length)` *(Note: PostgreSQL is 1-indexed, starting from position 1)*

```sql
-- Extracts 4 characters starting at position 1
SELECT name, SUBSTRING(name, 1, 4) AS short_name 
FROM customers;

-- Generate an account code by combining pieces of name and id
SELECT 
    name, 
    CONCAT(LEFT(name, 3), '-', SUBSTRING(id::text, 1, 3)) AS account_code 
FROM customers;
```

### 1.6 `TRIM()`, `LTRIM()`, and `RTRIM()`
Removes unwanted leading and trailing whitespace (or specific characters) from text.
- `TRIM(text)`: Removes whitespace from both sides.
- `LTRIM(text)`: Removes whitespace only from the left (beginning).
- `RTRIM(text)`: Removes whitespace only from the right (end).

```sql
SELECT 
    name AS raw_name,
    TRIM(name) AS cleaned_name,
    LENGTH(name) AS raw_length,
    LENGTH(TRIM(name)) AS cleaned_length
FROM customers;
```

### 1.7 `REPLACE()`
Searches for a specific substring and replaces every occurrence with a replacement string.

**Syntax:** `REPLACE(original_string, 'target_text', 'new_text')`

```sql
-- Replace spaces with underscores
SELECT name, REPLACE(name, ' ', '_') AS underscore_name 
FROM customers;

-- Replace a specific word or character
SELECT REPLACE('Database Management', 'Management', 'System') AS updated_text;
```

---

## 2. Numeric & Math Functions

PostgreSQL provides a rich set of built-in mathematical functions to perform arithmetic calculations, rounding, and number transformations.

### 2.1 Basic Arithmetic Operators
- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `%` (Modulo / Remainder)

```sql
SELECT 
    name, 
    age, 
    age + 5 AS age_in_5_years,
    balance / 2 AS half_balance
FROM customers;
```

### 2.2 `ABS()` (Absolute Value)
Returns the positive value of any number, removing negative signs.

```sql
SELECT 
    name,
    balance, 
    ABS(balance) AS absolute_balance 
FROM customers;
-- e.g., -250.50 becomes 250.50
```

### 2.3 `ROUND()`
Rounds a number to the nearest integer, or to a specified number of decimal places.

**Syntax:** `ROUND(numeric_value, decimal_places)`

```sql
-- Round to whole number
SELECT ROUND(1450.75);       -- Result: 1451

-- Round to 1 decimal place
SELECT ROUND(1450.75, 1);    -- Result: 1450.8
```

### 2.4 `CEIL()` (or `CEILING()`) and `FLOOR()`
- `CEIL(x)`: Rounds a number **up** to the nearest whole integer.
- `FLOOR(x)`: Rounds a number **down** to the nearest whole integer.

```sql
SELECT 
    balance,
    CEIL(balance) AS rounded_up,
    FLOOR(balance) AS rounded_down
FROM customers;
-- For 1450.75: CEIL -> 1451, FLOOR -> 1450
```

### 2.5 `TRUNC()` (Truncate)
Discards decimal digits without rounding.

**Syntax:** `TRUNC(numeric_value, decimal_places)`

```sql
SELECT 
    TRUNC(123.456, 1) AS trunc_one_decimal,  -- Result: 123.4
    TRUNC(123.456, 0) AS trunc_whole_number; -- Result: 123
```

### 2.6 `POWER()` and `SQRT()`
- `POWER(base, exponent)`: Multiplies a base number by itself `exponent` times.
- `SQRT(number)`: Calculates the square root of a positive number.

```sql
SELECT 
    POWER(2, 3) AS two_cubed,     -- Result: 8 (2 * 2 * 2)
    SQRT(64) AS square_root_64;   -- Result: 8
```

### 2.7 `MOD()` (Modulo / Remainder)
Returns the remainder of dividing one number by another.

```sql
SELECT 
    name,
    age, 
    MOD(age, 2) AS remainder_div_by_2 -- 0 = Even number, 1 = Odd number
FROM customers;
```

---

## 3. Date & Time Functions

PostgreSQL handles dates, timestamps, and time intervals through convenient functions for tracking timestamps, date arithmetic, and calendar parsing.

### 3.1 `CURRENT_DATE`, `CURRENT_TIME`, and `NOW()`
- `CURRENT_DATE`: Returns today's date (`YYYY-MM-DD`).
- `CURRENT_TIME`: Returns the current time with time zone.
- `NOW()` or `CURRENT_TIMESTAMP`: Returns the current date, time, and timezone down to fractional seconds.

```sql
SELECT 
    CURRENT_DATE AS today_date,
    CURRENT_TIME AS time_now,
    NOW() AS full_timestamp;
```

### 3.2 `EXTRACT()`
Extracts a specific subfield (such as `YEAR`, `MONTH`, `DAY`, `HOUR`, `DOW` [Day of Week]) from a date or timestamp.

**Syntax:** `EXTRACT(field FROM source)`

```sql
SELECT 
    name,
    created_at,
    EXTRACT(YEAR FROM created_at) AS account_year,
    EXTRACT(MONTH FROM created_at) AS account_month,
    EXTRACT(DAY FROM created_at) AS account_day
FROM customers;
```

### 3.3 `AGE()`
Calculates the interval difference between two dates/timestamps, or between a timestamp and today's date.

**Syntax:**
- `AGE(timestamp)`: Difference between current date and the given timestamp.
- `AGE(end_timestamp, start_timestamp)`: Difference between two specified timestamps.

```sql
-- Account age for each customer
SELECT 
    name, 
    created_at, 
    AGE(NOW(), created_at) AS time_since_created 
FROM customers;

-- Age between two specific dates
SELECT AGE('2026-09-05'::DATE, '2000-01-01'::DATE) AS age_difference;
-- Result: 26 years 8 mons 4 days
```

### 3.4 `DATE_TRUNC()`
Truncates a timestamp to a specified unit of precision (such as `'day'`, `'month'`, `'year'`), rounding down all smaller time components to zero.

**Syntax:** `DATE_TRUNC('precision_unit', timestamp)`

```sql
-- Truncate to start of the day (resets hours, minutes, seconds to 00:00:00)
SELECT DATE_TRUNC('day', NOW()) AS start_of_today;

-- Truncate to start of the month (resets to 1st of the month at 00:00:00)
SELECT 
    name,
    created_at, 
    DATE_TRUNC('month', created_at) AS month_registered 
FROM customers;
```

---

## 4. Aggregate Functions & `GROUP BY`

An aggregate function performs a calculation on a set of rows and collapses them into a single summary scalar value.

### 4.1 Summary of Common Aggregate Functions
| Function | Description |
|:---|:---|
| `COUNT(*)` | Counts total rows returned by query |
| `COUNT(column)` | Counts total non-null values in the specified column |
| `SUM(column)` | Calculates the total sum of all numeric values |
| `AVG(column)` | Calculates the average value |
| `MIN(column)` | Returns the minimum (smallest) value |
| `MAX(column)` | Returns the maximum (largest) value |

### 4.2 Aggregates on the Entire Table
When aggregate functions are run without a `GROUP BY` clause, they calculate statistics across every row in the table, returning exactly one summary row:

```sql
SELECT 
    COUNT(*) AS total_customers,
    SUM(balance) AS total_balance,
    ROUND(AVG(age), 2) AS average_age,
    MIN(age) AS youngest_age,
    MAX(age) AS oldest_age
FROM customers;
```

---

### 4.3 The `GROUP BY` Clause

#### What is `GROUP BY`?
`GROUP BY` divides rows into groups based on matching values in one or more columns. It allows aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) to be calculated separately **for each group** rather than across the whole table.

#### The Golden Rule of `GROUP BY`:
> Every column in your `SELECT` statement that is **not** wrapped inside an aggregate function **must** be included in the `GROUP BY` clause. If you select a raw column without grouping by it, PostgreSQL will return a syntax error.

#### Example A: Basic `GROUP BY` (Count customers by City)
```sql
SELECT 
    city, 
    COUNT(*) AS total_customers
FROM customers
GROUP BY city;
```

**Output Result:**
| city | total_customers |
|:---|:---|
| Karachi | 3 |
| Lahore | 2 |
| Islamabad | 1 |

#### Example B: Multiple Aggregates per Group
You can apply multiple aggregate functions in the same query to inspect each group:

```sql
SELECT 
    city,
    COUNT(*) AS total_customers,
    SUM(balance) AS city_total_balance,
    ROUND(AVG(balance), 2) AS avg_balance,
    MAX(balance) AS highest_balance
FROM customers
GROUP BY city
ORDER BY total_customers DESC;
```

**Output Result:**
| city | total_customers | city_total_balance | avg_balance | highest_balance |
|:---|:---|:---|:---|:---|
| Karachi | 3 | 6751.25 | 2250.42 | 3200.00 |
| Lahore | 2 | 624.70 | 312.35 | 875.20 |
| Islamabad | 1 | 0.00 | 0.00 | 0.00 |

#### Example C: Filtering Groups with `HAVING`
- Use **`WHERE`** to filter raw rows **before** groups are formed (cannot use aggregate functions in `WHERE`).
- Use **`HAVING`** to filter groups **after** aggregation has been calculated.

```sql
-- Show only cities that have 2 or more customers
SELECT 
    city, 
    COUNT(*) AS customer_count,
    ROUND(AVG(balance), 2) AS avg_balance
FROM customers
GROUP BY city
HAVING COUNT(*) >= 2;
```

**Output Result:**
| city | customer_count | avg_balance |
|:---|:---|:---|
| Karachi | 3 | 2250.42 |
| Lahore | 2 | 312.35 |
*(Islamabad is excluded because its count is less than 2)*

#### Example D: Complete Pipeline (`WHERE` + `GROUP BY` + `HAVING` + `ORDER BY`)
This example shows how all the clauses work together step-by-step:

```sql
SELECT 
    city,
    COUNT(*) AS positive_balance_customers,
    ROUND(AVG(balance), 2) AS avg_positive_balance
FROM customers
WHERE balance >= 0                  -- Step 1: Filter individual rows first
GROUP BY city                       -- Step 2: Group surviving rows by city
HAVING COUNT(*) >= 2                -- Step 3: Keep only groups with 2+ rows
ORDER BY avg_positive_balance DESC; -- Step 4: Sort the final grouped result
```

#### Example E: `GROUP BY` with Expressions (`CASE`)
You can also group rows by calculated logical categories:

```sql
SELECT 
    CASE 
        WHEN age < 18 THEN 'Minor' 
        ELSE 'Adult' 
    END AS age_category,
    COUNT(*) AS total_count,
    ROUND(AVG(balance), 2) AS avg_balance
FROM customers
GROUP BY 
    CASE 
        WHEN age < 18 THEN 'Minor' 
        ELSE 'Adult' 
    END;
```

---

## 5. Conditional Expressions (`CASE`)

The `CASE` statement in PostgreSQL is the SQL equivalent of an `if-else` statement in programming languages. It checks conditions sequentially and returns a specified result when the first condition evaluates to `TRUE`.

### Syntax:
```sql
CASE 
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    ...
    ELSE default_result
END
```

> **Rules to remember:**
> - `CASE` statements evaluate conditions from top to bottom.
> - As soon as a condition is `TRUE`, it returns the matching result and stops evaluating further.
> - The `ELSE` clause is optional; if omitted and no conditions match, `CASE` returns `NULL`.
> - Always finish the expression with `END`.

### Examples:

**Example A: Classifying Customers by Age**
```sql
SELECT 
    name,
    age,
    CASE 
        WHEN age < 18 THEN 'Teenager'
        WHEN age BETWEEN 18 AND 29 THEN 'Young Adult'
        WHEN age BETWEEN 30 AND 49 THEN 'Adult'
        ELSE 'Senior'
    END AS age_group
FROM customers;
```

**Example B: Financial Account Status Based on Balance**
```sql
SELECT 
    name,
    balance,
    CASE 
        WHEN balance > 1000 THEN 'Premium Balance'
        WHEN balance > 0 THEN 'Standard Balance'
        WHEN balance = 0 THEN 'Zero Balance'
        ELSE 'Negative Balance (Debt)'
    END AS account_status
FROM customers;
```

---

## Quick Reference Summary Table

| Category | Function / Syntax | Example | Output / Purpose |
|:---|:---|:---|:---|
| **String** | `UPPER(str)` | `UPPER('omer')` | `'OMER'` (converts to uppercase) |
| **String** | `LOWER(str)` | `LOWER('OMER')` | `'omer'` (converts to lowercase) |
| **String** | `LENGTH(str)` | `LENGTH('apple')` | `5` (character count) |
| **String** | `CONCAT(a, b)` | `CONCAT('Hello', ' ', 'World')` | `'Hello World'` (combines strings) |
| **String** | `LEFT(str, n)` | `LEFT('Database', 4)` | `'Data'` (first n characters) |
| **String** | `RIGHT(str, n)` | `RIGHT('Database', 4)` | `'base'` (last n characters) |
| **String** | `SUBSTRING(str, s, len)`| `SUBSTRING('Database', 1, 4)` | `'Data'` (extracts slice) |
| **String** | `TRIM(str)` | `TRIM('  text  ')` | `'text'` (strips outer whitespace) |
| **String** | `REPLACE(str, from, to)`| `REPLACE('Cat', 'C', 'B')` | `'Bat'` (substitutes substrings) |
| **Numeric** | `ABS(n)` | `ABS(-50.5)` | `50.5` (removes negative sign) |
| **Numeric** | `ROUND(n, d)` | `ROUND(4.567, 2)` | `4.57` (rounds to d decimals) |
| **Numeric** | `CEIL(n)` | `CEIL(4.1)` | `5` (rounds up to integer) |
| **Numeric** | `FLOOR(n)` | `FLOOR(4.9)` | `4` (rounds down to integer) |
| **Numeric** | `TRUNC(n, d)` | `TRUNC(4.567, 1)` | `4.5` (cuts off decimals) |
| **Numeric** | `POWER(a, b)` | `POWER(3, 2)` | `9` ($3^2$) |
| **Numeric** | `SQRT(n)` | `SQRT(25)` | `5` ($\sqrt{25}$) |
| **Numeric** | `MOD(a, b)` | `MOD(10, 3)` | `1` (remainder of division) |
| **Date/Time**| `CURRENT_DATE` | `CURRENT_DATE` | Current date (`YYYY-MM-DD`) |
| **Date/Time**| `NOW()` | `NOW()` | Full current timestamp |
| **Date/Time**| `EXTRACT(unit FROM dt)` | `EXTRACT(YEAR FROM NOW())` | Single unit (e.g. `2026`) |
| **Date/Time**| `AGE(dt1, dt2)` | `AGE(NOW(), created_at)` | Interval difference |
| **Date/Time**| `DATE_TRUNC(unit, dt)` | `DATE_TRUNC('month', NOW())`| Floor timestamp to unit |
| **Aggregate**| `COUNT(col)` | `COUNT(*)` | Total number of rows |
| **Aggregate**| `SUM(col)` | `SUM(balance)` | Sum of column values |
| **Aggregate**| `AVG(col)` | `AVG(age)` | Average of column values |
| **Aggregate**| `MIN(col)` / `MAX(col)` | `MIN(age)`, `MAX(age)` | Minimum and maximum values |
| **Grouping** | `GROUP BY col` | `GROUP BY city` | Groups rows by distinct column values |
| **Grouping** | `HAVING condition` | `HAVING COUNT(*) > 1` | Filters groups after aggregation |
| **Conditional**| `CASE WHEN ... END` | `CASE WHEN age >= 18 THEN 'Adult' ELSE 'Minor' END` | If-Else decision logic |

 