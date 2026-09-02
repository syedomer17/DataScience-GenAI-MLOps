# PostgreSQL Comparison and Logical Operators

This document covers **Comparison Operators** and **Logical Operators** in **PostgreSQL**. These operators are used inside the `WHERE` clause to filter data and fetch only the exact rows you need from your database.

---

## Sample Table (For Examples)

To easily understand how each operator works, imagine we have a table called `customers`:

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50),
    balance NUMERIC(10, 2),
    is_active BOOLEAN
);

INSERT INTO customers (name, age, city, balance, is_active) VALUES
('Omer', 22, 'Karachi', 1500.00, TRUE),
('Ali', 17, 'Lahore', 500.00, TRUE),
('Sara', 25, 'Karachi', 2400.00, FALSE),
('Zain', 18, 'Islamabad', 0.00, TRUE),
('Ayesha', 30, 'Lahore', 3200.00, FALSE);
```

### Table Data View:
| id | name | age | city | balance | is_active |
|:---|:---|:---|:---|:---|:---|
| 1 | Omer | 22 | Karachi | 1500.00 | true |
| 2 | Ali | 17 | Lahore | 500.00 | true |
| 3 | Sara | 25 | Karachi | 2400.00 | false |
| 4 | Zain | 18 | Islamabad | 0.00 | true |
| 5 | Ayesha | 30 | Lahore | 3200.00 | false |

---

## 1. Comparison Operators

### What are Comparison Operators?
Comparison operators compare two values (such as a column value and a number, or two columns).
Every comparison returns one of three results:
- **`TRUE`**: The row matches the condition and will be included in the results.
- **`FALSE`**: The row does not match and will be skipped.
- **`NULL`**: One of the values is unknown/missing.

### Quick Reference Table

| Operator | Meaning | Example | Description |
|:---|:---|:---|:---|
| `=` | Equal to | `age = 22` | Matches if the value is exactly 22 |
| `!=` or `<>` | Not equal to | `city != 'Karachi'` | Matches if the value is anything except 'Karachi' |
| `>` | Greater than | `age > 18` | Matches if the value is strictly higher than 18 |
| `<` | Less than | `balance < 1000` | Matches if the value is strictly lower than 1000 |
| `>=` | Greater than or equal to | `age >= 18` | Matches if the value is 18 or higher |
| `<=` | Less than or equal to | `age <= 25` | Matches if the value is 25 or lower |

---

### A. Equal To (`=`)
- **Explanation**: Checks if the value on the left is exactly equal to the value on the right.
- **Syntax**:
  ```sql
  SELECT * FROM table_name WHERE column_name = value;
  ```
- **Example**: Find customers who live in `'Karachi'`:
  ```sql
  SELECT * FROM customers 
  WHERE city = 'Karachi';
  ```
- **Result**: Returns rows for `Omer` and `Sara`.

---

### B. Not Equal To (`!=` or `<>`)
- **Explanation**: Checks if the value is different from the given value. Both `!=` and `<>` do the same thing in PostgreSQL (`<>` is the official standard SQL keyword).
- **Syntax**:
  ```sql
  SELECT * FROM table_name WHERE column_name != value;
  -- OR
  SELECT * FROM table_name WHERE column_name <> value;
  ```
- **Example**: Find all customers who do **not** live in `'Karachi'`:
  ```sql
  SELECT * FROM customers 
  WHERE city != 'Karachi';
  ```
- **Result**: Returns rows for `Ali` (Lahore), `Zain` (Islamabad), and `Ayesha` (Lahore).

---

### C. Greater Than (`>`)
- **Explanation**: Checks if a value is strictly greater than (higher than) the specified value.
- **Syntax**:
  ```sql
  SELECT * FROM table_name WHERE column_name > value;
  ```
- **Example**: Find customers who are older than 18:
  ```sql
  SELECT * FROM customers 
  WHERE age > 18;
  ```
- **Result**: Returns `Omer` (22), `Sara` (25), and `Ayesha` (30).
- **Note**: `Zain` (age 18) is **not** included because 18 is not greater than 18.

---

### D. Less Than (`<`)
- **Explanation**: Checks if a value is strictly less than (lower than) the specified value.
- **Syntax**:
  ```sql
  SELECT * FROM table_name WHERE column_name < value;
  ```
- **Example**: Find customers who have a balance less than 1000:
  ```sql
  SELECT * FROM customers 
  WHERE balance < 1000.00;
  ```
- **Result**: Returns `Ali` (500.00) and `Zain` (0.00).

---

### E. Greater Than or Equal To (`>=`)
- **Explanation**: Checks if a value is either greater than OR equal to the specified number.
- **Syntax**:
  ```sql
  SELECT * FROM table_name WHERE column_name >= value;
  ```
- **Example**: Find all customers who are 18 years old or older:
  ```sql
  SELECT * FROM customers 
  WHERE age >= 18;
  ```
- **Result**: Returns `Omer` (22), `Sara` (25), `Zain` (18), and `Ayesha` (30).
- **Note**: `Zain` (age 18) **is** included this time because he is equal to 18.

---

### F. Less Than or Equal To (`<=`)
- **Explanation**: Checks if a value is either less than OR equal to the specified number.
- **Syntax**:
  ```sql
  SELECT * FROM table_name WHERE column_name <= value;
  ```
- **Example**: Find customers who are 22 years old or younger:
  ```sql
  SELECT * FROM customers 
  WHERE age <= 22;
  ```
- **Result**: Returns `Ali` (17), `Zain` (18), and `Omer` (22).

---

## 2. Logical Operators

### What are Logical Operators?
Logical operators are used to connect two or more conditions together in a `WHERE` clause, or to reverse a condition.

### Quick Reference Table

| Operator | Meaning | Condition Rule |
|:---|:---|:---|
| `AND` | Both must be true | Returns rows where **all** connected conditions are `TRUE` |
| `OR` | Either can be true | Returns rows where **at least one** condition is `TRUE` |
| `NOT` | Reverses condition | Turns `TRUE` into `FALSE`, and `FALSE` into `TRUE` |

---

### A. The `AND` Operator
- **Explanation**: All conditions separated by `AND` must be satisfied (true) for the row to be returned. If even one condition is false, the row is ignored.
- **Syntax**:
  ```sql
  SELECT * FROM table_name 
  WHERE condition1 AND condition2;
  ```
- **Example**: Find customers who are older than 18 **AND** live in `'Karachi'`:
  ```sql
  SELECT * FROM customers 
  WHERE age > 18 AND city = 'Karachi';
  ```
- **How PostgreSQL checks**:
  - `Omer` (age 22 > 18: TRUE, city 'Karachi': TRUE) -> **Included**
  - `Sara` (age 25 > 18: TRUE, city 'Karachi': TRUE) -> **Included**
  - `Ali` (age 17 > 18: FALSE, city 'Lahore': FALSE) -> **Skipped**
  - `Zain` (age 18 > 18: FALSE, city 'Islamabad': FALSE) -> **Skipped**
  - `Ayesha` (age 30 > 18: TRUE, city 'Lahore': FALSE) -> **Skipped** (fails city check)

---

### B. The `OR` Operator
- **Explanation**: At least one of the conditions separated by `OR` must be true. The row will be returned if the first condition is true, the second condition is true, or both are true.
- **Syntax**:
  ```sql
  SELECT * FROM table_name 
  WHERE condition1 OR condition2;
  ```
- **Example**: Find customers who live in `'Islamabad'` **OR** live in `'Lahore'`:
  ```sql
  SELECT * FROM customers 
  WHERE city = 'Islamabad' OR city = 'Lahore';
  ```
- **Result**: Returns `Ali` (Lahore), `Zain` (Islamabad), and `Ayesha` (Lahore).

---

### C. The `NOT` Operator
- **Explanation**: Reverses the meaning of a condition. If a condition evaluates to `TRUE`, `NOT` makes it `FALSE`. If it is `FALSE`, `NOT` makes it `TRUE`.
- **Syntax**:
  ```sql
  SELECT * FROM table_name 
  WHERE NOT condition;
  ```
- **Example 1**: Find customers whose account is **NOT** active:
  ```sql
  SELECT * FROM customers 
  WHERE NOT is_active;
  -- (Same as: WHERE is_active = FALSE)
  ```
- **Result**: Returns `Sara` and `Ayesha`.

- **Example 2**: Find customers who are **NOT** under 18:
  ```sql
  SELECT * FROM customers 
  WHERE NOT (age < 18);
  -- (Same as: WHERE age >= 18)
  ```
- **Result**: Returns `Omer` (22), `Sara` (25), `Zain` (18), and `Ayesha` (30).

---

## 3. Combining `AND`, `OR`, and `NOT` (Using Parentheses)

When combining multiple logical operators in a single query, PostgreSQL follows an **order of priority (precedence)**:
1. `NOT` is evaluated first.
2. `AND` is evaluated second.
3. `OR` is evaluated last.

> [!TIP]
> **Best Practice:** Always use parentheses `()` to make your conditions clear and ensure PostgreSQL executes them in the exact order you want.

### Example:

Suppose you want:
- Customers from `'Karachi'` who are older than 20, **OR**
- Any customer whose balance is greater than 3000.

```sql
SELECT * FROM customers 
WHERE (city = 'Karachi' AND age > 20) OR balance > 3000;
```

**How it works:**
1. First, it evaluates `(city = 'Karachi' AND age > 20)`. This matches `Omer` and `Sara`.
2. Second, it checks `balance > 3000`. This matches `Ayesha` (balance 3200.00).
3. The final result returns: `Omer`, `Sara`, and `Ayesha`.

---

## 4. Special Note: Comparing with `NULL` Values

In SQL, `NULL` means "unknown" or "no value".
Because `NULL` is unknown, you **cannot** use `= NULL` or `!= NULL`.

- ❌ `WHERE balance = NULL` (Will not work / returns nothing)
- ✅ `WHERE balance IS NULL` (Correct way to check for missing values)
- ✅ `WHERE balance IS NOT NULL` (Correct way to check for existing values)

**Example:**
```sql
-- Find customers who have an email address recorded
SELECT * FROM customers 
WHERE email IS NOT NULL;
```

---

## 5. Summary Cheat Sheet

| Task | Operator | Example Query |
|:---|:---|:---|
| Find exact match | `=` | `SELECT * FROM customers WHERE age = 18;` |
| Exclude specific value | `!=` or `<>` | `SELECT * FROM customers WHERE city <> 'Lahore';` |
| Greater than | `>` | `SELECT * FROM customers WHERE age > 21;` |
| Less than | `<` | `SELECT * FROM customers WHERE balance < 1000;` |
| Minimum value (inclusive) | `>=` | `SELECT * FROM customers WHERE age >= 18;` |
| Maximum value (inclusive) | `<=` | `SELECT * FROM customers WHERE age <= 60;` |
| All conditions must match | `AND` | `SELECT * FROM customers WHERE age >= 18 AND is_active = TRUE;` |
| Any condition can match | `OR` | `SELECT * FROM customers WHERE city = 'Karachi' OR city = 'Lahore';` |
| Opposite / Negation | `NOT` | `SELECT * FROM customers WHERE NOT is_active;` |
| Check for missing values | `IS NULL` | `SELECT * FROM customers WHERE city IS NULL;` |
| Check for non-missing values | `IS NOT NULL` | `SELECT * FROM customers WHERE city IS NOT NULL;` |
 
