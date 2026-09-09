# PostgreSQL Window Functions, JOINs & CTEs

Window functions are among the most powerful analytical features in SQL. They allow you to perform calculations across a set of table rows that are related to the current row, **without collapsing them into a single summary row** (unlike `GROUP BY`).

---

## 1. Core Concept: `GROUP BY` vs. Window Functions

| Feature | `GROUP BY` Aggregation | Window Function (`OVER`) |
| :--- | :--- | :--- |
| **Row Output** | Collapses multiple rows into a **single summary row**. | Retains **all individual rows** while appending the calculated aggregate as a new column. |
| **Detail Visibility** | Loses access to individual row details (e.g., individual customer IDs or timestamps). | Keeps all raw row details intact alongside the aggregated calculation. |
| **SQL Keyword** | `GROUP BY column_name` | `OVER (PARTITION BY ... ORDER BY ...)` |

### Visual Representation:
```text
Raw Rows:
  Dept A, John,  $5,000
  Dept A, Sara,  $7,000
  Dept B, Bob,   $4,000

GROUP BY dept:
  Dept A, Total: $12,000   <-- Collapsed (John and Sara individual details are lost)
  Dept B, Total: $4,000

Window Function SUM() OVER (PARTITION BY dept):
  Dept A, John,  $5,000, Dept_Total: $12,000   <-- Retained!
  Dept A, Sara,  $7,000, Dept_Total: $12,000   <-- Retained!
  Dept B, Bob,   $4,000, Dept_Total: $4,000    <-- Retained!
```

---

## 2. Anatomy of a Window Function

Every window function relies on the **`OVER()`** clause:

```sql
SELECT 
    column_name,
    WINDOW_FUNCTION() OVER (
        PARTITION BY partition_column
        ORDER BY sort_column [ASC | DESC]
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS calculated_column
FROM table_name;
```

### Breakdown of the 3 Clauses:
1. **`PARTITION BY` (Optional):** Divides the result set into subsets or "windows" (like a virtual `GROUP BY`). If omitted, the entire table is treated as one single partition.
2. **`ORDER BY` (Optional):** Defines the logical order of rows inside each partition. Crucial for running totals, ranks, and offsets (`LAG`/`LEAD`).
3. **Frame Specification (`ROWS / RANGE`) (Optional):** Defines which subset of rows relative to the current row should be included in the window calculation (e.g., running sum vs. entire partition sum).

---

## 3. Categories of Window Functions

PostgreSQL window functions fall into three major families:

```text
                        Window Functions
    ┌───────────────────────────┼───────────────────────────┐
    ▼                           ▼                           ▼
Aggregate Functions         Ranking Functions         Value / Offset Functions
- SUM()                     - ROW_NUMBER()            - LAG()
- AVG()                     - RANK()                  - LEAD()
- MIN() / MAX()             - DENSE_RANK()            - FIRST_VALUE()
- COUNT()                   - NTILE()                 - LAST_VALUE()
```

---

## 4. Hands-On Practical Setup

Let's build a realistic corporate dataset with departments, employees, and regional sales transactions.

```sql
-- Step 1: Create practice database
CREATE DATABASE company_analytics;

-- Step 2: Connect to the database
\c company_analytics

-- Step 3: Create Departments Table
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

-- Step 4: Create Employees Table
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    dept_id INT REFERENCES departments(dept_id),
    salary NUMERIC(10, 2) NOT NULL,
    hire_date DATE NOT NULL
);

-- Step 5: Create Sales Table
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES employees(emp_id),
    sale_date DATE NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    region VARCHAR(20) NOT NULL
);

-- Step 6: Insert Sample Data
INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'Technology'),
(2, 'Sales'),
(3, 'Finance');

INSERT INTO employees (emp_id, emp_name, dept_id, salary, hire_date) VALUES
(1, 'Alice',   1, 95000.00, '2021-03-15'),
(2, 'Bob',     1, 85000.00, '2022-06-01'),
(3, 'Charlie', 1, 85000.00, '2023-01-10'),
(4, 'Diana',   2, 70000.00, '2020-11-20'),
(5, 'Evan',    2, 70000.00, '2021-08-14'),
(6, 'Fiona',   2, 60000.00, '2022-09-05'),
(7, 'George',  3, 80000.00, '2019-04-12'),
(8, 'Hannah',  3, 75000.00, '2021-12-01');

INSERT INTO sales (emp_id, sale_date, amount, region) VALUES
(4, '2026-01-05', 1200.00, 'North'),
(4, '2026-01-15', 1800.00, 'North'),
(5, '2026-01-10', 2500.00, 'South'),
(5, '2026-01-22', 1500.00, 'South'),
(6, '2026-01-08',  900.00, 'North'),
(6, '2026-01-19', 3100.00, 'East'),
(4, '2026-02-02', 2100.00, 'North'),
(5, '2026-02-14', 1900.00, 'South');
```

---

## 5. Aggregate Window Functions (`SUM`, `AVG`, `MIN`, `MAX`, `COUNT`)

### Practical 1: Department Total vs. Overall Total
Display each employee's salary along with:
1. The total salary budget of their department.
2. The overall company salary budget.
3. The employee's percentage contribution to their department budget.

```sql
SELECT 
    emp_name,
    dept_id,
    salary,
    -- Department salary total
    SUM(salary) OVER(PARTITION BY dept_id) AS dept_total_salary,
    -- Company-wide total
    SUM(salary) OVER() AS company_total_salary,
    -- Percentage contribution to department
    ROUND((salary / SUM(salary) OVER(PARTITION BY dept_id)) * 100, 2) AS dept_pct_share
FROM employees;
```

---

### Practical 2: Running Totals (Cumulative Sum)
When you add `ORDER BY` inside `OVER()`, PostgreSQL computes a **running/cumulative** calculation:

```sql
SELECT 
    sale_id,
    emp_id,
    sale_date,
    amount,
    region,
    -- Running total across the entire table by date
    SUM(amount) OVER(ORDER BY sale_date) AS overall_running_total,
    -- Running total within each region
    SUM(amount) OVER(PARTITION BY region ORDER BY sale_date) AS regional_running_total
FROM sales;
```

> **How it works:**  
> - For row 1, `regional_running_total` = row 1 amount.  
> - For row 2 (same region), it adds row 1 + row 2.  
> - When the region changes, the counter restarts because of `PARTITION BY region`.

---

## 6. Ranking Window Functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`)

Understanding the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` is a classic SQL interview favorite.

| Function | How Ties are Handled | Leaves Gaps in Numbers? | Example Sequence |
| :--- | :--- | :---: | :--- |
| `ROW_NUMBER()` | Assigns consecutive unique integers arbitrarily for ties. | ❌ No | 1, 2, 3, 4, 5 |
| `RANK()` | Tied values receive the same rank, next rank skips. | ✅ Yes | 1, **2, 2, 4**, 5 |
| `DENSE_RANK()` | Tied values receive the same rank, next rank is consecutive. | ❌ No | 1, **2, 2, 3**, 4 |
| `NTILE(n)` | Divides rows into `n` approximately equal buckets/quartiles. | ❌ No | Bucket 1, 2, ... |

### Practical 3: Side-by-Side Comparison of Ranking Functions

Notice that in Department 1, Bob and Charlie both earn **$85,000** (a tie):

```sql
SELECT 
    emp_name,
    dept_id,
    salary,
    ROW_NUMBER() OVER(PARTITION BY dept_id ORDER BY salary DESC) AS row_num,
    RANK()       OVER(PARTITION BY dept_id ORDER BY salary DESC) AS rnk,
    DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY salary DESC) AS dense_rnk
FROM employees;
```

**Output for Department 1:**
| emp_name | dept_id | salary | row_num | rnk | dense_rnk | Explanation |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| Alice | 1 | 95000 | 1 | 1 | 1 | Highest salary |
| Bob | 1 | 85000 | 2 | **2** | **2** | Tied salary |
| Charlie | 1 | 85000 | 3 | **2** | **2** | Tied salary |
| *(hypothetical next)* | 1 | 70000 | 4 | **4** (Gap!) | **3** (No Gap!) | Notice `RANK` jumped to 4, but `DENSE_RANK` continued to 3 |

---

### Practical 4: Bucketing Rows with `NTILE(n)`
Divide employees into 2 salary tiers (high earners vs. standard earners):

```sql
SELECT 
    emp_name,
    salary,
    NTILE(2) OVER(ORDER BY salary DESC) AS salary_tier
FROM employees;
```

---

## 7. Value & Offset Window Functions (`LAG`, `LEAD`)

- **`LAG(col, offset, default)`**: Fetches a value from a **previous row**.
- **`LEAD(col, offset, default)`**: Fetches a value from a **subsequent row**.

### Practical 5: Period-Over-Period Sales Growth
Compare each sale with the previous sale made by the same employee:

```sql
SELECT 
    emp_id,
    sale_date,
    amount,
    -- Previous sale amount by same employee
    LAG(amount, 1, 0.00) OVER(PARTITION BY emp_id ORDER BY sale_date) AS prev_sale_amount,
    -- Difference from previous sale
    amount - LAG(amount, 1, amount) OVER(PARTITION BY emp_id ORDER BY sale_date) AS change_from_last_sale,
    -- Next sale amount
    LEAD(amount, 1, 0.00) OVER(PARTITION BY emp_id ORDER BY sale_date) AS next_sale_amount
FROM sales;
```

---

## 8. Window Functions with `JOIN`s

In real business applications, your data is distributed across multiple tables. You often need to join tables first, and then evaluate window functions across the joined result.

### Practical 6: Department Names with Salary Percentages
Join `employees` and `departments`, then calculate:
1. Average department salary.
2. Difference between employee's salary and department average.

```sql
SELECT 
    e.emp_name,
    d.dept_name,
    e.salary,
    -- Average salary in their department
    ROUND(AVG(e.salary) OVER(PARTITION BY d.dept_name), 2) AS dept_avg_salary,
    -- Difference from department average
    ROUND(e.salary - AVG(e.salary) OVER(PARTITION BY d.dept_name), 2) AS diff_from_avg
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.salary DESC;
```

---

### Practical 7: Multi-Table Sales Leaderboard with Joins
Join `sales`, `employees`, and `departments` to see total sales per employee, department running total, and rank across the company:

```sql
SELECT 
    s.sale_id,
    e.emp_name,
    d.dept_name,
    s.amount,
    s.sale_date,
    -- Cumulative sales per department over time
    SUM(s.amount) OVER(PARTITION BY d.dept_name ORDER BY s.sale_date) AS dept_running_sales,
    -- Company-wide sale rank
    RANK() OVER(ORDER BY s.amount DESC) AS company_sale_rank
FROM sales s
INNER JOIN employees e ON s.emp_id = e.emp_id
INNER JOIN departments d ON e.dept_id = d.dept_id;
```

---

## 9. Window Functions with Common Table Expressions (CTEs)

### The Golden Rule of Window Functions:
> **Window functions CANNOT be used inside `WHERE` or `HAVING` clauses!**
>
> The following query will throw an error in PostgreSQL:
> ```sql
> -- ❌ SYNTAX ERROR!
> SELECT emp_name, salary 
> FROM employees 
> WHERE RANK() OVER (ORDER BY salary DESC) <= 2;
> ```
> **Why?** Because SQL evaluates the `WHERE` clause **before** window functions are calculated.

### The Solution: Use a CTE (`WITH` clause)
To filter by the result of a window function, calculate the window function inside a **CTE** (or subquery) first, and filter it in the outer query.

---

### Practical 8: Top-N Analysis (Top 2 Earners Per Department)

Find the **top 2 highest-earning employees in every department**:

```sql
WITH RankedEmployees AS (
    SELECT 
        e.emp_name,
        d.dept_name,
        e.salary,
        DENSE_RANK() OVER(PARTITION BY e.dept_id ORDER BY e.salary DESC) AS salary_rank
    FROM employees e
    INNER JOIN departments d ON e.dept_id = d.dept_id
)
SELECT 
    dept_name,
    salary_rank,
    emp_name,
    salary
FROM RankedEmployees
WHERE salary_rank <= 2
ORDER BY dept_name, salary_rank;
```

**Output:**
| dept_name | salary_rank | emp_name | salary |
| :--- | :---: | :--- | :---: |
| Finance | 1 | George | 80000.00 |
| Finance | 2 | Hannah | 75000.00 |
| Sales | 1 | Diana | 70000.00 |
| Sales | 1 | Evan | 70000.00 |
| Sales | 2 | Fiona | 60000.00 |
| Technology | 1 | Alice | 95000.00 |
| Technology | 2 | Bob | 85000.00 |
| Technology | 2 | Charlie | 85000.00 |

*(Notice Diana and Evan both tied for Rank 1 in Sales, and Fiona accurately got Rank 2 thanks to `DENSE_RANK`!)*

---

### Practical 9: Removing Duplicate Records Using CTE & `ROW_NUMBER()`

A very popular real-world data cleaning technique using `ROW_NUMBER()`:

```sql
-- Step 1: Create a table with duplicate entries
CREATE TABLE customer_leads (
    lead_id SERIAL PRIMARY KEY,
    email VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customer_leads (email, phone) VALUES
('test@gmail.com', '9999999991'),
('test@gmail.com', '9999999991'), -- Duplicate
('user@yahoo.com', '8888888882'),
('user@yahoo.com', '8888888882'); -- Duplicate

-- Step 2: Identify unique vs duplicate rows using a CTE
WITH DeduplicatedLeads AS (
    SELECT 
        lead_id,
        email,
        phone,
        ROW_NUMBER() OVER(PARTITION BY email, phone ORDER BY lead_id ASC) AS row_occurrence
    FROM customer_leads
)
-- Row occurrence 1 = Original record; > 1 = Duplicates!
SELECT * 
FROM DeduplicatedLeads 
WHERE row_occurrence = 1;
```

---

### Practical 10: Multi-Step Sales Performance Pipeline (Chained CTEs)

Combine multiple CTEs with window functions to produce an executive sales report:

```sql
-- CTE 1: Calculate total sales per employee
WITH EmployeeSalesSummary AS (
    SELECT 
        e.emp_id,
        e.emp_name,
        d.dept_name,
        SUM(s.amount) AS total_sales
    FROM sales s
    INNER JOIN employees e ON s.emp_id = e.emp_id
    INNER JOIN departments d ON e.dept_id = d.dept_id
    GROUP BY e.emp_id, e.emp_name, d.dept_name
),
-- CTE 2: Apply Window Functions on the summarized sales
RankedSalesTeam AS (
    SELECT 
        emp_name,
        dept_name,
        total_sales,
        -- Department rank
        RANK() OVER(PARTITION BY dept_name ORDER BY total_sales DESC) AS dept_rank,
        -- Company-wide rank
        RANK() OVER(ORDER BY total_sales DESC) AS overall_rank,
        -- Company average sales
        ROUND(AVG(total_sales) OVER(), 2) AS company_avg_sales
    FROM EmployeeSalesSummary
)
-- Final Query: Select top performers exceeding company average
SELECT 
    emp_name,
    dept_name,
    total_sales,
    dept_rank,
    overall_rank,
    company_avg_sales
FROM RankedSalesTeam
ORDER BY overall_rank;
```

---

## 10. Reusable Named Windows (`WINDOW` Clause)

If multiple window functions share the exact same `PARTITION BY` and `ORDER BY` specification, you can define a **named window** at the end of the query using the `WINDOW` clause to avoid repeating code (DRY Principle):

```sql
SELECT 
    emp_name,
    dept_id,
    salary,
    SUM(salary)  OVER w AS dept_running_sum,
    AVG(salary)  OVER w AS dept_running_avg,
    COUNT(*)     OVER w AS dept_running_count
FROM employees
WINDOW w AS (PARTITION BY dept_id ORDER BY salary DESC);
```

---

## 11. SQL Query Processing Order (Execution Lifecycle)

To master window functions, remember where they execute in the SQL query lifecycle:

```text
  1. FROM & JOIN
  2. WHERE
  3. GROUP BY
  4. HAVING
  5. WINDOW FUNCTIONS  ──▶ (Executed here! That's why WHERE cannot see them)
  6. SELECT
  7. DISTINCT
  8. ORDER BY
  9. LIMIT & OFFSET
```

---

## 12. Quick Revision Summary & Cheat Sheet

### Function Quick Lookup:
```sql
-- 1. Running Total
SUM(amount) OVER (PARTITION BY group_col ORDER BY date_col)

-- 2. Ranking without gaps
DENSE_RANK() OVER (PARTITION BY group_col ORDER BY metric_col DESC)

-- 3. Previous row value
LAG(col, 1) OVER (PARTITION BY group_col ORDER BY order_col)

-- 4. Next row value
LEAD(col, 1) OVER (PARTITION BY group_col ORDER BY order_col)

-- 5. Top-N Filtering Pattern with CTE
WITH cte AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY dept ORDER BY score DESC) AS rnk
    FROM students
)
SELECT * FROM cte WHERE rnk <= 3;
```
