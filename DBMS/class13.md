# PostgreSQL Advanced SQL: Window Functions, JOINs, CTEs, Triggers & Extensions

This class covers advanced PostgreSQL topics that transform your SQL queries from basic CRUD operations into enterprise-grade analytics, automation, and modular database architectures:

1. **Window Functions** — Advanced analytics and calculations without collapsing rows.
2. **Window Functions with JOINs** — Multi-table analytical reporting.
3. **Common Table Expressions (CTEs)** — Clean, modular queries, Top-N filtering, and deduplication.
4. **Trigger Functions & Triggers** — Event-driven database automation and audit logging.
5. **PostgreSQL Extensions** — Extending database capabilities with UUIDs, cryptography, fuzzy text search, and case-insensitive data types.

---

## Part 1: PostgreSQL Window Functions

### 1. Core Concept: `GROUP BY` vs. Window Functions

| Feature | `GROUP BY` Aggregation | Window Function (`OVER`) |
| :--- | :--- | :--- |
| **Row Output** | Collapses multiple rows into a **single summary row**. | Retains **all individual rows** while appending the calculated aggregate as a new column. |
| **Detail Visibility** | Loses access to individual row details (e.g., individual customer IDs or timestamps). | Keeps all raw row details intact alongside the aggregated calculation. |
| **SQL Keyword** | `GROUP BY column_name` | `OVER (PARTITION BY ... ORDER BY ...)` |

#### Visual Representation:
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

### 2. Anatomy of a Window Function

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

#### Breakdown of the 3 Clauses:
1. **`PARTITION BY` (Optional):** Divides the result set into subsets or "windows" (like a virtual `GROUP BY`). If omitted, the entire table is treated as one single partition.
2. **`ORDER BY` (Optional):** Defines the logical order of rows inside each partition. Crucial for running totals, ranks, and offsets (`LAG`/`LEAD`).
3. **Frame Specification (`ROWS / RANGE`) (Optional):** Defines which subset of rows relative to the current row should be included in the window calculation (e.g., running sum vs. entire partition sum).

---

### 3. Categories of Window Functions

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

### 4. Hands-On Dataset Setup for Window Functions

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

### 5. Aggregate Window Functions (`SUM`, `AVG`, `COUNT`)

#### Practical 1: Department Total vs. Overall Total
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

#### Practical 2: Running Totals (Cumulative Sum)
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

---

### 6. Ranking Window Functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`)

| Function | How Ties are Handled | Leaves Gaps in Numbers? | Example Sequence |
| :--- | :--- | :---: | :--- |
| `ROW_NUMBER()` | Assigns consecutive unique integers arbitrarily for ties. | ❌ No | 1, 2, 3, 4, 5 |
| `RANK()` | Tied values receive the same rank, next rank skips. | ✅ Yes | 1, **2, 2, 4**, 5 |
| `DENSE_RANK()` | Tied values receive the same rank, next rank is consecutive. | ❌ No | 1, **2, 2, 3**, 4 |
| `NTILE(n)` | Divides rows into `n` approximately equal buckets/quartiles. | ❌ No | Bucket 1, 2, ... |

#### Practical 3: Ranking Comparison on Tied Salaries
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

---

### 7. Value & Offset Window Functions (`LAG`, `LEAD`)

#### Practical 4: Period-Over-Period Sales Growth
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

## Part 2: Window Functions with `JOIN`s

### Practical 5: Department Names with Salary Deviations
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

### Practical 6: Multi-Table Sales Leaderboard with Joins
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

## Part 3: Window Functions with Common Table Expressions (CTEs)

> **The Golden Rule:** Window functions **CANNOT** be used inside `WHERE` or `HAVING` clauses because SQL processes `WHERE` **before** computing window functions.  
> **The Solution:** Calculate the window function inside a **CTE (`WITH`)** and filter in the outer query.

### Practical 7: Top-N Analysis (Top 2 Earners Per Department)
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

### Practical 8: Deduplicating Records Using CTE & `ROW_NUMBER()`
```sql
-- Create leads table with duplicates
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

-- Filter out duplicates
WITH DeduplicatedLeads AS (
    SELECT 
        lead_id,
        email,
        phone,
        ROW_NUMBER() OVER(PARTITION BY email, phone ORDER BY lead_id ASC) AS row_occurrence
    FROM customer_leads
)
SELECT * 
FROM DeduplicatedLeads 
WHERE row_occurrence = 1;
```

---

## Part 4: PostgreSQL Triggers & Trigger Functions

### 1. What is a Trigger and a Trigger Function?

- **Trigger:** A database event listener that monitors tables for specific DML events (`INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`). When the event occurs, PostgreSQL automatically fires an associated function.
- **Trigger Function:** A specialized function defined using `PL/pgSQL` that:
  1. Takes **no arguments** in its function signature.
  2. Returns the special type **`TRIGGER`**.
  3. Uses built-in special variables (`NEW`, `OLD`, `TG_OP`, `TG_TABLE_NAME`).

```text
       SQL Operation (INSERT / UPDATE / DELETE)
                          │
                          ▼
                  ┌───────────────┐
                  │ Trigger Event │
                  └───────┬───────┘
                          │ (Fires automatically)
                          ▼
              ┌───────────────────────┐
              │ Trigger Function      │
              │ (Validates, Audits,   │
              │  or Modifies Data)    │
              └───────────────────────┘
```

---

### 2. Special Trigger Variables in PostgreSQL

Inside any trigger function, PostgreSQL gives you access to special contextual variables:

| Variable | Type | Description | Available In |
| :--- | :--- | :--- | :--- |
| **`NEW`** | `RECORD` | The new row data being inserted or updated. | `INSERT`, `UPDATE` |
| **`OLD`** | `RECORD` | The existing row data before modification or deletion. | `UPDATE`, `DELETE` |
| **`TG_OP`** | `TEXT` | String indicating operation: `'INSERT'`, `'UPDATE'`, or `'DELETE'`. | All triggers |
| **`TG_TABLE_NAME`** | `NAME` | Name of the table that invoked the trigger. | All triggers |
| **`TG_WHEN`** | `TEXT` | `'BEFORE'`, `'AFTER'`, or `'INSTEAD OF'`. | All triggers |

---

### 3. Trigger Timing & Execution Types

1. **`BEFORE` Triggers:** Run **before** row changes are committed to the table file on disk.
   - Ideal for: Validating business rules, cleaning/formatting inputs, auto-updating timestamps (`updated_at`).
   - Must return `NEW` (to save the modified row) or `NULL` (to cancel the operation).
2. **`AFTER` Triggers:** Run **after** row changes are committed to the table.
   - Ideal for: Writing audit logs to a separate table, sending notifications, aggregating summary stats.
   - Returns `NULL` (return value is ignored).
3. **`FOR EACH ROW` vs. `FOR EACH STATEMENT`:**
   - `FOR EACH ROW`: Executes once for every affected row.
   - `FOR EACH STATEMENT`: Executes once per SQL command regardless of how many rows are touched.

---

### 4. Hands-On Trigger Practicals

#### Practical 9: Automatic `updated_at` Timestamp Trigger (`BEFORE UPDATE`)

In production, you never want developers to manually pass `updated_at = NOW()` on every update query. A `BEFORE UPDATE` trigger guarantees timestamps are always up to date:

```sql
-- Step 1: Add updated_at column to employees
ALTER TABLE employees ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Step 2: Create the Trigger Function
CREATE OR REPLACE FUNCTION set_updated_at_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    -- Update the updated_at field on the incoming row
    NEW.updated_at = CURRENT_TIMESTAMP;
    -- In BEFORE triggers, returning NEW allows the modified row to be written
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Step 3: Attach the Trigger to the employees table
CREATE TRIGGER trg_employees_updated_at
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION set_updated_at_timestamp();
```

**Testing the Trigger:**
```sql
-- Update an employee's salary
UPDATE employees SET salary = 98000.00 WHERE emp_id = 1;

-- Check if updated_at changed automatically
SELECT emp_id, emp_name, salary, updated_at FROM employees WHERE emp_id = 1;
```

---

#### Practical 10: Complete Audit Logging Trigger (`AFTER INSERT, UPDATE, DELETE`)

An audit log records who made what change and when. This is mandatory in financial and healthcare systems:

```sql
-- Step 1: Create an Audit Log table
CREATE TABLE employee_audit_logs (
    audit_id SERIAL PRIMARY KEY,
    emp_id INT,
    action_type VARCHAR(10) NOT NULL, -- INSERT, UPDATE, DELETE
    changed_by VARCHAR(50) DEFAULT CURRENT_USER,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    old_data JSONB,
    new_data JSONB
);

-- Step 2: Create the Audit Trigger Function
CREATE OR REPLACE FUNCTION log_employee_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO employee_audit_logs (emp_id, action_type, new_data)
        VALUES (NEW.emp_id, TG_OP, to_jsonb(NEW));
        RETURN NEW;

    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO employee_audit_logs (emp_id, action_type, old_data, new_data)
        VALUES (NEW.emp_id, TG_OP, to_jsonb(OLD), to_jsonb(NEW));
        RETURN NEW;

    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO employee_audit_logs (emp_id, action_type, old_data)
        VALUES (OLD.emp_id, TG_OP, to_jsonb(OLD));
        RETURN OLD;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Step 3: Attach the Trigger
CREATE TRIGGER trg_employee_audit
AFTER INSERT OR UPDATE OR DELETE ON employees
FOR EACH ROW
EXECUTE FUNCTION log_employee_changes();
```

**Testing the Audit Log:**
```sql
-- 1. Insert a new employee
INSERT INTO employees (emp_name, dept_id, salary, hire_date) 
VALUES ('Iris Vance', 1, 88000.00, '2026-03-01');

-- 2. Update their salary
UPDATE employees SET salary = 92000.00 WHERE emp_name = 'Iris Vance';

-- 3. Delete the employee
DELETE FROM employees WHERE emp_name = 'Iris Vance';

-- 4. Inspect the audit log trail!
SELECT audit_id, action_type, changed_by, changed_at, old_data, new_data 
FROM employee_audit_logs;
```

---

#### Practical 11: Business Validation Trigger (`RAISE EXCEPTION`)

Prevent salary reductions: In company policy, an employee's salary can never be decreased.

```sql
CREATE OR REPLACE FUNCTION validate_salary_increase()
RETURNS TRIGGER AS $$
BEGIN
    -- Check if the new salary is lower than existing salary
    IF NEW.salary < OLD.salary THEN
        RAISE EXCEPTION 'Salary cannot be reduced! Previous: %, Attempted: %', OLD.salary, NEW.salary;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_prevent_salary_cut
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION validate_salary_increase();
```

**Testing the Constraint:**
```sql
-- Attempt to decrease Alice's salary (Will fail!)
UPDATE employees SET salary = 50000.00 WHERE emp_id = 1;
-- Output: ERROR: Salary cannot be reduced! Previous: 98000.00, Attempted: 50000.00
```

---

### 5. Managing and Removing Triggers

```sql
-- Temporarily disable a trigger
ALTER TABLE employees DISABLE TRIGGER trg_prevent_salary_cut;

-- Re-enable a disabled trigger
ALTER TABLE employees ENABLE TRIGGER trg_prevent_salary_cut;

-- Permanently drop a trigger
DROP TRIGGER IF EXISTS trg_prevent_salary_cut ON employees;

-- Permanently drop a trigger function
DROP FUNCTION IF EXISTS validate_salary_increase();
```

---

## Part 5: PostgreSQL Extensions

### 1. What is an Extension?

PostgreSQL has a modular plug-and-play architecture. An **Extension** bundles together new SQL functions, custom data types, index operators, and procedural languages into a single installable package.

#### Extension Management Commands:
```sql
-- Install an extension
CREATE EXTENSION IF NOT EXISTS <extension_name>;

-- View installed extensions
SELECT * FROM pg_extension;

-- View all available extensions on the server
SELECT name, default_version, comment 
FROM pg_available_extensions 
ORDER BY name;

-- Remove an extension
DROP EXTENSION IF EXISTS <extension_name>;
```

---

### 2. Top Essential PostgreSQL Extensions & Practicals

#### A. Extension 1: `pgcrypto` (Hashing, Encryption & UUIDs)

Used for secure password hashing with **Bcrypt** and generating cryptographic tokens.

```sql
-- Enable pgcrypto
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- 1. Generate secure random UUID v4
SELECT gen_random_uuid();
-- Output: e.g. 7f83b2a5-4876-4d43-98fe-891dc45763b0

-- 2. Create users table with UUID primary key and Bcrypt password hashing
CREATE TABLE app_users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Insert user with salted Bcrypt password
INSERT INTO app_users (username, password_hash)
VALUES ('alice_admin', crypt('SuperSecretPassword123', gen_salt('bf')));

-- 4. Authenticate user during login
SELECT user_id, username 
FROM app_users 
WHERE username = 'alice_admin' 
  AND password_hash = crypt('SuperSecretPassword123', password_hash);
-- If credentials match, the user row is returned!
```

---

#### B. Extension 2: `pg_trgm` (Fuzzy Search & Substring Matching)

Standard `LIKE '%search%'` cannot use regular B-Tree indexes and requires full table scans. The `pg_trgm` (trigram) extension breaks text into sets of 3 consecutive characters and enables fuzzy matching and fast GIN indexing.

```sql
-- Enable pg_trgm
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- 1. Check similarity score between two words (0.0 to 1.0)
SELECT similarity('PostgreSQL', 'Postgres');
-- Output: ~0.73 (73% similar)

-- 2. Find words with typos using the % (similarity) operator
SELECT 'database' % 'datbase'; -- Returns TRUE!

-- 3. Fast Substring Search with GIN Trigram Index
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL
);

INSERT INTO products (product_name) VALUES
('Apple iPhone 15 Pro Max'),
('Samsung Galaxy S24 Ultra'),
('Google Pixel 9 Pro'),
('Apple MacBook Pro 16');

-- Create GIN index for lightning-fast wildcard search
CREATE INDEX idx_products_name_trgm ON products USING GIN (product_name gin_trgm_ops);

-- Lightning fast substring query utilizing the GIN index
SELECT * FROM products WHERE product_name ILIKE '%pixel%';
```

---

#### C. Extension 3: `citext` (Case-Insensitive Text Data Type)

In standard SQL, `'John@gmail.com' != 'john@gmail.com'`. The `citext` extension provides a string data type that compares values case-insensitively without having to constantly write `LOWER()`:

```sql
-- Enable citext
CREATE EXTENSION IF NOT EXISTS citext;

-- Create table with citext email column
CREATE TABLE user_accounts (
    account_id SERIAL PRIMARY KEY,
    email CITEXT UNIQUE NOT NULL
);

INSERT INTO user_accounts (email) VALUES ('User.Test@Example.COM');

-- Query using all lowercase (Matches automatically!)
SELECT * FROM user_accounts WHERE email = 'user.test@example.com';

-- Unique constraint prevents duplicate casing!
-- INSERT INTO user_accounts (email) VALUES ('user.test@example.com');
-- ERROR: duplicate key value violates unique constraint "user_accounts_email_key"
```

---

#### D. Extension 4: `uuid-ossp` (Standard UUID Generation)

Alternative UUID generator providing UUID version 1 (MAC-address & time based) and version 4 (fully random):

```sql
-- Enable uuid-ossp
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Generate version 1 UUID
SELECT uuid_generate_v1();

-- Generate version 4 UUID
SELECT uuid_generate_v4();
```

---

## Part 6: Quick Revision Summary & Cheat Sheet

### 1. Window Functions Cheat Sheet:
```sql
-- Running Total
SUM(amount) OVER (PARTITION BY region ORDER BY sale_date)

-- Ranking without gaps
DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC)

-- Compare with previous row
LAG(amount, 1) OVER (PARTITION BY emp_id ORDER BY sale_date)

-- Top-N Filter using CTE
WITH ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT * FROM ranked WHERE rnk <= 2;
```

### 2. Triggers Cheat Sheet:
```sql
-- 1. Create function returning TRIGGER
CREATE OR REPLACE FUNCTION func_name() RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW(); -- In BEFORE triggers, modify NEW
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 2. Create trigger
CREATE TRIGGER trg_name
BEFORE UPDATE ON table_name
FOR EACH ROW
EXECUTE FUNCTION func_name();
```

### 3. Extensions Cheat Sheet:
```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;  -- UUIDs & Bcrypt passwords
CREATE EXTENSION IF NOT EXISTS pg_trgm;    -- Fuzzy text search & GIN substring index
CREATE EXTENSION IF NOT EXISTS citext;     -- Case-insensitive string type
```
