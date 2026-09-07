# PostgreSQL Subqueries & Nested Queries

A **subquery** (also known as an **inner query**, **nested query**, or **subselect**) is a SQL query embedded within another SQL statement (the **outer query** or enclosing query). The outer query depends on the result of the inner query to filter, project, calculate, or manipulate data.

Subqueries can be embedded across almost all major SQL clauses (`SELECT`, `FROM`, `WHERE`, `HAVING`) and DML statements (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).

---

## 1. Fundamentals & Core Rules

### Why Use Subqueries?
- **Step-by-step problem breakdown**: Subqueries allow you to compute an intermediate result (e.g., finding the maximum value, average, or an ID list) and feed it directly into an enclosing query in a single execution step.
- **Dynamic filtering**: Avoids hardcoding IDs or static values that change as data updates.
- **Data modification conditions**: Allows `INSERT`, `UPDATE`, and `DELETE` statements to target rows based on criteria evaluated from other tables.

### Key Rules for Subqueries:
1. **Parentheses**: A subquery **must always** be enclosed in parentheses `(...)`.
2. **Order of Evaluation**: In standard (non-correlated) subqueries, the inner subquery executes **first**, and its output is passed to the outer query. In correlated subqueries, the inner query executes repeatedly for each candidate row of the outer query.
3. **Column Compatibility**:
   - Subqueries used with standard comparison operators (`=`, `>`, `<`, `!=`) must return a **single scalar value** (1 row, 1 column).
   - Subqueries used with `IN`, `ANY`, `ALL` must return a **single column**, but can return **multiple rows**.
   - Subqueries used in the `FROM` clause act as virtual tables (derived tables) and **must be given an explicit table alias**.
4. **Ordering**: An `ORDER BY` clause inside a subquery is generally unnecessary unless used alongside `LIMIT` / `OFFSET`.

---

## 2. Practice Database & Schema Setup

To test and execute all examples and exercises, we will use the following relational schema (`customers`, `customer_profiles`, `products`, `locations`, and `sales`).

```sql
-- Connect to your database
-- \c sales;

-- 1. Customers Table (Master)
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
);

-- 2. Customer Profiles Table (1:1 Relationship with customers)
CREATE TABLE IF NOT EXISTS customer_profiles (
    customer_id INT PRIMARY KEY REFERENCES customers(customer_id) ON DELETE CASCADE,
    date_of_birth DATE,
    gender VARCHAR(10)
);

-- 3. Products Table
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL
);

-- 4. Locations Table
CREATE TABLE IF NOT EXISTS locations (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL
);

-- 5. Sales Transactions Table
CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    location_id INT NOT NULL REFERENCES locations(location_id) ON DELETE RESTRICT,
    quantity INT NOT NULL CHECK (quantity > 0),
    discount NUMERIC(5, 2) DEFAULT 0 CHECK (discount >= 0),
    total_amount NUMERIC(12, 2) NOT NULL
);
```

### Sample Data Insertion

```sql
-- Insert Customers
INSERT INTO customers (customer_id, first_name, last_name, email, phone) VALUES
(1, 'Sara', 'Ahmed', 'sara.ahmed@example.com', '9876543210'),
(2, 'Omer', 'Ali', 'omer.ali@example.com', '9876543211'),
(3, 'Rahul', 'Sharma', 'rahul.sharma@example.com', '9876543212'),
(4, 'Priya', 'Reddy', 'priya.reddy@example.com', '9876543213'),
(5, 'Arjun', 'Kumar', 'arjun.kumar@example.com', '9876543214'),
(6, 'Fatima', 'Noor', 'fatima.noor@example.com', '9876543215')
ON CONFLICT (customer_id) DO NOTHING;

-- Insert Customer Profiles (Notice customer 5 and 6 do NOT have profiles yet)
INSERT INTO customer_profiles (customer_id, date_of_birth, gender) VALUES
(1, '1995-04-12', 'Female'),
(2, '1992-08-23', 'Male'),
(3, '1988-11-05', 'Male'),
(4, '1997-01-30', 'Female')
ON CONFLICT (customer_id) DO NOTHING;

-- Insert Products
INSERT INTO products (product_id, product_name, category, unit_price) VALUES
(1, 'Laptop', 'Electronics', 65000.00),
(2, 'Mechanical Keyboard', 'Accessories', 3500.00),
(3, 'Wireless Mouse', 'Accessories', 1200.00),
(4, 'Smart TV 55-inch', 'Electronics', 48000.00),
(5, 'Desk Chair', 'Furniture', 8500.00),
(6, 'USB-C Cable', 'Accessories', 99.00)
ON CONFLICT (product_id) DO NOTHING;

-- Insert Locations
INSERT INTO locations (location_id, city, state, country) VALUES
(1, 'Bengaluru', 'Karnataka', 'India'),
(2, 'Hyderabad', 'Telangana', 'India'),
(3, 'New Delhi', 'Delhi', 'India'),
(4, 'Mumbai', 'Maharashtra', 'India')
ON CONFLICT (location_id) DO NOTHING;

-- Insert Sales Transactions
INSERT INTO sales (sale_id, sale_date, customer_id, product_id, location_id, quantity, discount, total_amount) VALUES
(1, '2024-01-10', 1, 1, 1, 1, 0.00, 65000.00),
(2, '2024-01-12', 2, 2, 2, 2, 500.00, 6500.00),
(3, '2024-01-15', 3, 3, 3, 1, 0.00, 1200.00),
(4, '2024-01-20', 1, 4, 1, 1, 2000.00, 46000.00),
(5, '2024-01-22', 4, 5, 4, 2, 1000.00, 16000.00),
(6, '2024-01-25', 2, 6, 2, 3, 0.00, 297.00),
(7, '2024-02-01', 3, 1, 3, 1, 1000.00, 64000.00)
ON CONFLICT (sale_id) DO NOTHING;
```

---

## 3. Classification of Subqueries by Returned Result

Subqueries can be categorized according to the dimensionality and format of the result set they produce:

```
                          Subquery Types
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
  Scalar Subquery      Single-Column Multi-Row   Multi-Column Subquery
(1 row, 1 column)         (N rows, 1 column)       (N rows, M columns)
  e.g., MAX(price)       e.g., IN (SELECT id)    e.g., (id, cat) IN (...)
```

### 3.1 Scalar Subquery (Single Row, Single Column)
A scalar subquery produces exactly **one single value** (one row and one column). Because it evaluates to a scalar primitive, it can be used anywhere a literal constant or column value is accepted, using standard comparison operators (`=`, `>`, `<`, `>=`, `<=`, `<>`).

```sql
-- Find all sales where the total amount is greater than the average sale amount
SELECT 
    sale_id, 
    customer_id, 
    total_amount
FROM sales
WHERE total_amount > (
    SELECT AVG(total_amount) 
    FROM sales
);
```

> [!WARNING]
> If a scalar subquery returns more than 1 row, PostgreSQL raises an error:
> `ERROR: more than one row returned by a subquery used as an expression`.

---

### 3.2 Single-Column, Multiple-Row Subquery
Returns a list of values (multiple rows, exactly 1 column). It cannot be compared using `=` or `>` directly; instead, it requires multi-row operators:
- `IN` / `NOT IN`
- `ANY` / `SOME`
- `ALL`

```sql
-- Find sales made for products belonging to the 'Electronics' category
SELECT 
    sale_id,
    customer_id,
    product_id,
    total_amount
FROM sales
WHERE product_id IN (
    SELECT product_id 
    FROM products 
    WHERE category = 'Electronics'
);
```

---

### 3.3 Multi-Column Subquery (Row / Tuple Subquery)
Evaluates multiple columns simultaneously using row constructors `(col1, col2)`.

```sql
-- Find products that have the maximum unit price within their category
SELECT 
    product_id, 
    product_name, 
    category, 
    unit_price
FROM products
WHERE (category, unit_price) IN (
    SELECT category, MAX(unit_price)
    FROM products
    GROUP BY category
);
```

---

## 4. Correlated vs. Non-Correlated Subqueries

Understanding correlation is critical for writing correct queries and diagnosing SQL performance.

| Attribute | Non-Correlated Subquery (Independent) | Correlated Subquery (Dependent) |
| :--- | :--- | :--- |
| **Dependency** | Completely independent of the outer query. | References columns from the outer query via aliases. |
| **Execution** | Executes **once**; the result is cached and reused by the outer query. | Executes **once per outer row candidate**. |
| **Can Run Alone?** | **Yes**; you can copy-paste the inner query and run it independently. | **No**; running the inner query alone yields an `unknown column` error. |
| **Performance** | Typically fast ($O(1)$ subquery execution). | Can be slow on large tables ($O(N \times M)$) unless properly indexed. |

### 4.1 Non-Correlated Subquery Example
The subquery runs once, evaluates to `65000.00`, and the outer query evaluates `WHERE total_amount = 65000.00`:

```sql
SELECT sale_id, customer_id, total_amount
FROM sales
WHERE total_amount = (
    SELECT MAX(total_amount) 
    FROM sales
);
```

### 4.2 Correlated Subquery Example
Notice the inner query references `s_outer.customer_id`. For every row evaluated in `customers`, PostgreSQL runs the inner query to compute that customer's personal average:

```sql
-- Find sales where the amount exceeds the customer's personal average purchase
SELECT 
    s_outer.sale_id,
    s_outer.customer_id,
    s_outer.total_amount
FROM sales s_outer
WHERE s_outer.total_amount > (
    SELECT AVG(s_inner.total_amount)
    FROM sales s_inner
    WHERE s_inner.customer_id = s_outer.customer_id
);
```

---

## 5. Subquery Predicates & Operators

### 5.1 `IN` and `NOT IN`
Checks whether a value is present or absent in the result list of the subquery.

```sql
-- Get all sales that occurred in Delhi locations
SELECT *
FROM sales
WHERE location_id IN (
    SELECT location_id 
    FROM locations 
    WHERE state = 'Delhi'
);
```

> [!CAUTION]
> **The `NOT IN` with `NULL` Trap!**
> If a subquery used with `NOT IN` returns even a single `NULL` value, the entire `NOT IN` condition evaluates to `UNKNOWN`/`NULL`, resulting in **zero rows returned**!
> 
> ```sql
> -- If subquery contains NULL:
> x NOT IN (1, 2, NULL) 
> -- Expands to:
> (x <> 1) AND (x <> 2) AND (x <> NULL)
> -- Since (x <> NULL) is UNKNOWN, the entire condition evaluates to FALSE/UNKNOWN!
> ```
> **Best Practice**: Use `NOT EXISTS` instead of `NOT IN`, or explicitly filter `WHERE column IS NOT NULL` inside the subquery.

---

### 5.2 `EXISTS` and `NOT EXISTS`
Checks for the **existence** of rows meeting a condition. Returns a Boolean (`TRUE` or `FALSE`). It terminates scanning as soon as the first matching row is found (**short-circuit evaluation**).

```sql
-- Find customers who have made at least one purchase
SELECT c.customer_id, c.first_name, c.last_name
FROM customers c
WHERE EXISTS (
    SELECT 1 
    FROM sales s 
    WHERE s.customer_id = c.customer_id
);

-- Find customers who have NEVER made a purchase
SELECT c.customer_id, c.first_name, c.last_name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 
    FROM sales s 
    WHERE s.customer_id = c.customer_id
);
```

> [!TIP]
> Inside `EXISTS (SELECT ...)`, the projected column does not matter (`SELECT 1`, `SELECT *`, or `SELECT NULL`). PostgreSQL only checks for row presence.

---

### 5.3 `ANY` (or `SOME`) and `ALL`
- `ANY` / `SOME`: Returns `TRUE` if the comparison is true for **at least one** value returned by the subquery.
- `ALL`: Returns `TRUE` only if the comparison is true for **every single** value returned by the subquery.

```sql
-- Find products whose unit price is greater than ANY product in the 'Accessories' category
-- (i.e., greater than the minimum price in Accessories)
SELECT product_id, product_name, unit_price
FROM products
WHERE unit_price > ANY (
    SELECT unit_price 
    FROM products 
    WHERE category = 'Accessories'
);

-- Find products whose unit price is greater than ALL products in the 'Accessories' category
-- (i.e., greater than the maximum price in Accessories)
SELECT product_id, product_name, unit_price
FROM products
WHERE unit_price > ALL (
    SELECT unit_price 
    FROM products 
    WHERE category = 'Accessories'
);
```

---

## 6. Placement of Subqueries Across SQL Clauses

Subqueries can be placed in various clauses of a SQL statement:

### 6.1 Subquery in the `WHERE` Clause
The most common usage: filtering rows based on dynamic calculations or lookup lists.

```sql
SELECT product_name, unit_price
FROM products
WHERE unit_price < (
    SELECT AVG(unit_price) 
    FROM products
);
```

---

### 6.2 Subquery in the `SELECT` Clause (Scalar Subquery as a Column)
Computes an individual metric for each row in the output. Must return a single scalar value.

```sql
-- Show each customer along with the total count of orders they placed
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    (
        SELECT COUNT(*) 
        FROM sales s 
        WHERE s.customer_id = c.customer_id
    ) AS total_orders
FROM customers c;
```

---

### 6.3 Subquery in the `FROM` Clause (Derived Table / Inline View)
Treats the output of the subquery as a temporary table. **In PostgreSQL, any subquery in the `FROM` clause MUST have an alias**.

```sql
-- Calculate overall statistics from aggregated customer spending
SELECT 
    ROUND(AVG(cust_summary.lifetime_spend), 2) AS avg_customer_spend,
    MAX(cust_summary.lifetime_spend) AS max_customer_spend
FROM (
    SELECT 
        customer_id, 
        SUM(total_amount) AS lifetime_spend
    FROM sales
    GROUP BY customer_id
) AS cust_summary;
```

---

### 6.4 Subquery in the `HAVING` Clause
Filters aggregated groups by comparing group aggregates against a subquery result.

```sql
-- Find product categories whose average product price is higher than the overall average price of all products
SELECT 
    category, 
    ROUND(AVG(unit_price), 2) AS avg_category_price
FROM products
GROUP BY category
HAVING AVG(unit_price) > (
    SELECT AVG(unit_price) 
    FROM products
);
```

---

## 7. Subqueries in Data Modification Language (DML)

Subqueries are essential when inserting, updating, or deleting records dynamically based on conditions in other tables.

### 7.1 `INSERT INTO ... SELECT` with Subquery
Create profile placeholders for all customers who do not yet have a record in `customer_profiles`:

```sql
INSERT INTO customer_profiles (customer_id, date_of_birth, gender)
SELECT 
    c.customer_id, 
    NULL, 
    NULL
FROM customers c
WHERE c.customer_id NOT IN (
    SELECT customer_id 
    FROM customer_profiles
);
```

---

### 7.2 `UPDATE` with Subquery
Add a promotional discount of $5.00$ to all sales originating from locations in the state of `Delhi`:

```sql
UPDATE sales
SET discount = discount + 5.00
WHERE location_id IN (
    SELECT location_id 
    FROM locations 
    WHERE state = 'Delhi'
);
```

---

### 7.3 `DELETE` with Subquery
Delete sales transactions associated with budget items (e.g., products with a unit price under $100$):

```sql
DELETE FROM sales
WHERE product_id IN (
    SELECT product_id 
    FROM products 
    WHERE unit_price <= 100.00
);
```

---

## 8. Multi-Level Nested Subqueries

A subquery can be nested inside another subquery (nesting depth can go multiple levels deep).

```sql
-- Find customer details for customers who purchased the most expensive product in the store
SELECT first_name, last_name, email
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM sales
    WHERE product_id = (
        -- Deepest level: Finds product with maximum unit price
        SELECT product_id
        FROM products
        ORDER BY unit_price DESC
        LIMIT 1
    )
);
```

---

## 9. Subquery vs. JOIN vs. CTE (Common Table Expression)

In PostgreSQL, complex operations can often be implemented using Subqueries, JOINs, or CTEs (`WITH` clauses).

### Comparison Matrix

| Feature | Subquery | JOIN | CTE (`WITH` clause) |
| :--- | :--- | :--- | :--- |
| **Readability** | Good for simple scalar lookups; hard to read when deeply nested. | Clean for connecting related tables. | Highly readable; modular top-to-bottom pipeline. |
| **Reusability** | Subquery must be duplicated if needed multiple times. | Re-joined as needed. | Can be referenced multiple times in the same query. |
| **PostgreSQL Optimizer** | Modern planner often rewrites subqueries into joins automatically. | Direct hash / merge / nested loop joins. | In PG 12+, CTEs are inlined by default unless marked `MATERIALIZED`. |
| **Best For** | One-off filters (`WHERE val > (SELECT ...)`), existence checks (`EXISTS`). | Combining columns from multiple tables. | Multi-step transformations, data warehousing, recursive queries. |

### Refactoring Comparison Example

**Problem**: Retrieve customer names who bought products in the `'Electronics'` category.

#### Approach A: Subquery with `IN`
```sql
SELECT first_name, last_name 
FROM customers
WHERE customer_id IN (
    SELECT customer_id 
    FROM sales 
    WHERE product_id IN (
        SELECT product_id 
        FROM products 
        WHERE category = 'Electronics'
    )
);
```

#### Approach B: `INNER JOIN` with `DISTINCT`
```sql
SELECT DISTINCT c.first_name, c.last_name
FROM customers c
INNER JOIN sales s ON c.customer_id = s.customer_id
INNER JOIN products p ON s.product_id = p.product_id
WHERE p.category = 'Electronics';
```

#### Approach C: Common Table Expression (`WITH`)
```sql
WITH electronic_products AS (
    SELECT product_id 
    FROM products 
    WHERE category = 'Electronics'
),
electronic_sales AS (
    SELECT DISTINCT customer_id 
    FROM sales 
    WHERE product_id IN (SELECT product_id FROM electronic_products)
)
SELECT c.first_name, c.last_name
FROM customers c
INNER JOIN electronic_sales es ON c.customer_id = es.customer_id;
```

---

## 10. Practice Exercises & Solutions

### Question 1: Find the Customer Who Made the Highest Total Amount Sale

#### Query:
```sql
SELECT 
    s.sale_id,
    s.customer_id,
    c.first_name,
    c.last_name,
    s.total_amount
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
WHERE s.total_amount = (
    SELECT MAX(total_amount) 
    FROM sales
);
```

#### Output:
| sale_id | customer_id | first_name | last_name | total_amount |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | Sara | Ahmed | 65000.00 |

---

### Question 2: Get All Sales of Products in the 'Electronics' Category

#### Query:
```sql
SELECT 
    s.sale_id,
    s.sale_date,
    s.product_id,
    s.quantity,
    s.total_amount
FROM sales s
WHERE s.product_id IN (
    SELECT p.product_id
    FROM products p
    WHERE p.category = 'Electronics'
);
```

#### Output:
| sale_id | sale_date | product_id | quantity | total_amount |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 2024-01-10 | 1 | 1 | 65000.00 |
| 4 | 2024-01-20 | 4 | 1 | 46000.00 |
| 7 | 2024-02-01 | 1 | 1 | 64000.00 |

---

### Question 3: Find Customers Who Have Never Made Any Purchases

#### Query (Using `NOT EXISTS` - Recommended):
```sql
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 
    FROM sales s 
    WHERE s.customer_id = c.customer_id
);
```

#### Output:
| customer_id | first_name | last_name | email |
| :--- | :--- | :--- | :--- |
| 5 | Arjun | Kumar | arjun.kumar@example.com |
| 6 | Fatima | Noor | fatima.noor@example.com |

---

### Question 4: Find Products Priced Above the Average Price of Their Own Category

#### Query (Correlated Subquery):
```sql
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    p.unit_price
FROM products p
WHERE p.unit_price > (
    SELECT AVG(p_sub.unit_price)
    FROM products p_sub
    WHERE p_sub.category = p.category
);
```

#### Output:
| product_id | product_name | category | unit_price |
| :--- | :--- | :--- | :--- |
| 1 | Laptop | Electronics | 65000.00 |
| 2 | Mechanical Keyboard | Accessories | 3500.00 |

---

### Question 5: Find the 2nd Highest Sale Amount Without Using `LIMIT` or `OFFSET`

#### Query (Subquery Pattern):
```sql
SELECT MAX(total_amount) AS second_highest_sale
FROM sales
WHERE total_amount < (
    SELECT MAX(total_amount) 
    FROM sales
);
```

#### Output:
| second_highest_sale |
| :--- |
| 64000.00 |

---

## 11. Performance Optimization & Best Practices

1. **Avoid Subqueries in `SELECT` for Large Datasets**:
   - A scalar subquery in the `SELECT` clause runs once per row. On 100,000 rows, that means 100,000 queries! Replace with a `LEFT JOIN` and `GROUP BY`.
2. **Prefer `EXISTS` over `IN` for Subqueries**:
   - `EXISTS` halts scanning as soon as the first match is encountered (early exit).
   - `IN` may collect all matching IDs into memory before evaluating.
3. **Beware of `NOT IN` with Nullable Columns**:
   - Always prefer `NOT EXISTS` over `NOT IN` to prevent silent logic errors caused by `NULL` values.
4. **Index Subquery Join Columns**:
   - Ensure foreign keys and columns used inside the inner query's `WHERE` clause (e.g. `customer_id`, `category`, `location_id`) have B-Tree indexes.
5. **Inspect Execution Plans**:
   - Use `EXPLAIN ANALYZE` before and after refactoring a subquery into a `JOIN` or `CTE` to verify PostgreSQL's cost and execution time.