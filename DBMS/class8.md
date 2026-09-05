# PostgreSQL Table Relationships & Joins

In relational databases (RDBMS) like PostgreSQL, data is divided across multiple specialized tables to reduce redundancy, prevent anomalies, and ensure consistency—a process known as **Database Normalization**. 

To connect this distributed data back together, we define **Relationships** using Primary Keys (PK) and Foreign Keys (FK), and use **JOINs** to query across multiple tables in a single cohesive result set.

---

## 1. Database Relationships Overview

A **relationship** defines how records in one table relate to records in another table. In PostgreSQL, relationships are enforced using **Foreign Key constraints**.

### The 4 Relationship Types:
1. **One-to-One (1:1)**: A record in Table A is linked to at most one record in Table B, and vice versa (e.g., a Customer and their User Profile).
2. **One-to-Many (1:N)**: A single record in Table A can relate to multiple records in Table B, but each record in Table B links back to exactly one record in Table A (e.g., one Customer can place many Orders).
3. **Many-to-One (N:1)**: The reverse perspective of One-to-Many. Multiple records in the child table link to a single record in the parent table.
4. **Many-to-Many (M:N)**: Multiple records in Table A relate to multiple records in Table B (e.g., Customers and Products). In relational databases, this is implemented using a **Junction Table** (bridge table) containing foreign keys pointing to both tables.

---

## 2. Database & Schema Setup

Let's build a realistic e-commerce database called `sales` to demonstrate relationships and joins.

### A. Create and Connect to the Database

```sql
-- Create the database
CREATE DATABASE sales;

-- Connect to the database
\c sales
```

---

### B. Create Tables with Primary and Foreign Keys

```sql
-- 1. Customers Table (Parent)
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
);

-- 2. Products Table (Parent)
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    unit_price NUMERIC(10, 2) NOT NULL
);

-- 3. Locations Table (Parent)
CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50) NOT NULL
);

-- 4. Sales Report Table (Child / Junction Table)
CREATE TABLE salesreport (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    location_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    discount NUMERIC(5, 2) DEFAULT 0 CHECK (discount >= 0),
    total_amount NUMERIC(12, 2) NOT NULL,

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON DELETE RESTRICT,

    CONSTRAINT fk_location
        FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
        ON DELETE RESTRICT
);
```

---

### C. Insert Sample Data

```sql
-- Insert Customers
INSERT INTO customers (first_name, last_name, email, phone)
VALUES
    ('Omer', 'Ali', 'omer.ali@gmail.com', '9876543210'),
    ('Rahul', 'Sharma', 'rahul.sharma@gmail.com', '9876543211'),
    ('Priya', 'Reddy', 'priya.reddy@gmail.com', '9876543212'),
    ('Arjun', 'Kumar', 'arjun.kumar@gmail.com', '9876543213'),
    ('Sneha', 'Patel', 'sneha.patel@gmail.com', '9876543214'),
    ('Vikram', 'Singh', 'vikram.singh@gmail.com', '9876543215'); -- Customer with no sales yet

-- Insert Products
INSERT INTO products (product_name, category, unit_price)
VALUES
    ('Laptop', 'Electronics', 65000.00),
    ('Wireless Mouse', 'Accessories', 1200.00),
    ('Mechanical Keyboard', 'Accessories', 3500.00),
    ('Monitor 24 Inch', 'Electronics', 15000.00),
    ('USB-C Hub', 'Accessories', 2500.00),
    ('4K Webcam', 'Electronics', 4500.00); -- Product with no sales yet

-- Insert Locations
INSERT INTO locations (city, state, country)
VALUES
    ('Hyderabad', 'Telangana', 'India'),
    ('Bengaluru', 'Karnataka', 'India'),
    ('Mumbai', 'Maharashtra', 'India'),
    ('Delhi', 'Delhi', 'India'),
    ('Chennai', 'Tamil Nadu', 'India');

-- Insert Sales Records
INSERT INTO salesreport
    (sale_date, customer_id, product_id, location_id, quantity, discount, total_amount)
VALUES
    ('2026-09-01', 1, 1, 1, 2, 1000.00, 129000.00),
    ('2026-09-02', 2, 2, 2, 3, 100.00, 3500.00),
    ('2026-09-03', 3, 3, 3, 1, 200.00, 3300.00),
    ('2026-09-04', 4, 4, 4, 2, 500.00, 29500.00),
    ('2026-09-05', 5, 5, 5, 4, 300.00, 9700.00);
```

---

### D. Table Previews

#### `customers`
| customer_id | first_name | last_name | email | phone |
|:---|:---|:---|:---|:---|
| 1 | Omer | Ali | omer.ali@gmail.com | 9876543210 |
| 2 | Rahul | Sharma | rahul.sharma@gmail.com | 9876543211 |
| 3 | Priya | Reddy | priya.reddy@gmail.com | 9876543212 |
| 4 | Arjun | Kumar | arjun.kumar@gmail.com | 9876543213 |
| 5 | Sneha | Patel | sneha.patel@gmail.com | 9876543214 |
| 6 | Vikram | Singh | vikram.singh@gmail.com | 9876543215 |

#### `products`
| product_id | product_name | category | unit_price |
|:---|:---|:---|:---|
| 1 | Laptop | Electronics | 65000.00 |
| 2 | Wireless Mouse | Accessories | 1200.00 |
| 3 | Mechanical Keyboard | Accessories | 3500.00 |
| 4 | Monitor 24 Inch | Electronics | 15000.00 |
| 5 | USB-C Hub | Accessories | 2500.00 |
| 6 | 4K Webcam | Electronics | 4500.00 |

#### `locations`
| location_id | city | state | country |
|:---|:---|:---|:---|
| 1 | Hyderabad | Telangana | India |
| 2 | Bengaluru | Karnataka | India |
| 3 | Mumbai | Maharashtra | India |
| 4 | Delhi | Delhi | India |
| 5 | Chennai | Tamil Nadu | India |

#### `salesreport`
| sale_id | sale_date | customer_id | product_id | location_id | quantity | discount | total_amount |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 2026-09-01 | 1 | 1 | 1 | 2 | 1000.00 | 129000.00 |
| 2 | 2026-09-02 | 2 | 2 | 2 | 3 | 100.00 | 3500.00 |
| 3 | 2026-09-03 | 3 | 3 | 3 | 1 | 200.00 | 3300.00 |
| 4 | 2026-09-04 | 4 | 4 | 4 | 2 | 500.00 | 29500.00 |
| 5 | 2026-09-05 | 5 | 5 | 5 | 4 | 300.00 | 9700.00 |

---

## 3. The 4 Relationship Types in Action

### 3.1 One-to-Many (1:N) Relationship

- **Concept**: A single customer can place many sales orders, but each sales order is attributed to only one customer.
- **Parent Table**: `customers` (`customer_id` is Primary Key)
- **Child Table**: `salesreport` (`customer_id` is Foreign Key)

#### Query:
```sql
SELECT 
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS customer_name,
    s.sale_id,
    s.sale_date,
    s.total_amount
FROM customers c 
JOIN salesreport s 
    ON c.customer_id = s.customer_id
ORDER BY c.customer_id, s.sale_date;
```

#### Output:
| customer_id | customer_name | sale_id | sale_date | total_amount |
|:---|:---|:---|:---|:---|
| 1 | Omer Ali | 1 | 2026-09-01 | 129000.00 |
| 2 | Rahul Sharma | 2 | 2026-09-02 | 3500.00 |
| 3 | Priya Reddy | 3 | 2026-09-03 | 3300.00 |
| 4 | Arjun Kumar | 4 | 2026-09-04 | 29500.00 |
| 5 | Sneha Patel | 5 | 2026-09-05 | 9700.00 |

---

### 3.2 Many-to-One (N:1) Relationship

- **Concept**: Looking from the child table's perspective. Multiple sales records refer back to a single parent customer.
- **Example**: Finding which customer is associated with a specific sale (e.g., `sale_id = 3`).

#### Query:
```sql
SELECT 
    s.sale_id,
    s.sale_date,
    s.total_amount,
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS customer_name,
    c.email
FROM salesreport s
JOIN customers c 
    ON s.customer_id = c.customer_id
WHERE s.sale_id = 3;
```

#### Output:
| sale_id | sale_date | total_amount | customer_id | customer_name | email |
|:---|:---|:---|:---|:---|:---|
| 3 | 2026-09-03 | 3300.00 | 3 | Priya Reddy | priya.reddy@gmail.com |

---

### 3.3 Many-to-Many (M:N) Relationship

- **Concept**: A customer can purchase many different products, and a product can be purchased by many different customers.
- **Junction Table Solution**: We cannot directly link `customers` and `products`. Instead, the `salesreport` table acts as the **bridge/junction table** holding both `customer_id` and `product_id`.

#### Query:
```sql
SELECT 
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS full_name,
    p.product_name,
    s.quantity,
    s.total_amount
FROM salesreport s
JOIN customers c 
    ON s.customer_id = c.customer_id
JOIN products p 
    ON s.product_id = p.product_id
ORDER BY c.customer_id;
```

#### Output:
| customer_id | full_name | product_name | quantity | total_amount |
|:---|:---|:---|:---|:---|
| 1 | Omer Ali | Laptop | 2 | 129000.00 |
| 2 | Rahul Sharma | Wireless Mouse | 3 | 3500.00 |
| 3 | Priya Reddy | Mechanical Keyboard | 1 | 3300.00 |
| 4 | Arjun Kumar | Monitor 24 Inch | 2 | 29500.00 |
| 5 | Sneha Patel | USB-C Hub | 4 | 9700.00 |

---

### 3.4 One-to-One (1:1) Relationship

- **Concept**: Exactly one record in Table A matches at most one record in Table B.
- **Implementation**: The primary key of the child table (`customer_profiles`) is also defined as the foreign key referencing `customers(customer_id)`.

#### Create Table & Insert Data:
```sql
CREATE TABLE customer_profiles (
    customer_id INT PRIMARY KEY,
    date_of_birth DATE,
    gender VARCHAR(10),

    CONSTRAINT fk_customer_profile
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE
);

-- Insert profiles for existing customers (IDs 1 through 5)
INSERT INTO customer_profiles (customer_id, date_of_birth, gender)
VALUES
    (1, '1998-04-12', 'Male'),
    (2, '2001-08-25', 'Female'),
    (3, '1995-11-03', 'Male'),
    (4, '2000-02-17', 'Female'),
    (5, '1992-06-30', 'Male');
```

#### Query:
```sql
SELECT 
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS full_name,
    c.email,
    p.date_of_birth,
    p.gender
FROM customers c
LEFT JOIN customer_profiles p 
    ON c.customer_id = p.customer_id
ORDER BY c.customer_id;
```

#### Output:
| customer_id | full_name | email | date_of_birth | gender |
|:---|:---|:---|:---|:---|
| 1 | Omer Ali | omer.ali@gmail.com | 1998-04-12 | Male |
| 2 | Rahul Sharma | rahul.sharma@gmail.com | 2001-08-25 | Female |
| 3 | Priya Reddy | priya.reddy@gmail.com | 1995-11-03 | Male |
| 4 | Arjun Kumar | arjun.kumar@gmail.com | 2000-02-17 | Female |
| 5 | Sneha Patel | sneha.patel@gmail.com | 1992-06-30 | Male |
| 6 | Vikram Singh | vikram.singh@gmail.com | NULL | NULL |

*(Notice that Customer 6 appears with `NULL` profile data because no profile was created for him yet).*

---

### 3.5 Adding Foreign Keys to Existing Tables (`ALTER TABLE`)

In production environments, tables are frequently created first and relationships are added later using `ALTER TABLE ... ADD CONSTRAINT`.

#### Step 1: Create Table and Insert Data
```sql
CREATE TABLE cus_profiles (
    id INT PRIMARY KEY,
    city VARCHAR(50),
    fees NUMERIC(10, 2)
);

INSERT INTO cus_profiles (id, city, fees)
VALUES
    (1, 'Hyderabad', 5000.00),
    (2, 'Mumbai', 7500.50),
    (3, 'Delhi', 6200.00),
    (4, 'Bangalore', 8500.75),
    (5, 'Chennai', 4500.25);
```

#### Step 2: Add Foreign Key Constraint via `ALTER TABLE`
```sql
-- Correct syntax: ADD CONSTRAINT (singular) and REFERENCES (spelled correctly)
ALTER TABLE cus_profiles 
ADD CONSTRAINT fk_cus_id
FOREIGN KEY (id)
REFERENCES customers(customer_id)
ON DELETE CASCADE;
```

#### Step 3: Query the Joined Tables
```sql
SELECT 
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS full_name,
    c.email,
    cp.city,
    cp.fees
FROM customers c 
JOIN cus_profiles cp
    ON c.customer_id = cp.id
ORDER BY c.customer_id;
```

#### Output:
| customer_id | full_name | email | city | fees |
|:---|:---|:---|:---|:---|
| 1 | Omer Ali | omer.ali@gmail.com | Hyderabad | 5000.00 |
| 2 | Rahul Sharma | rahul.sharma@gmail.com | Mumbai | 7500.50 |
| 3 | Priya Reddy | priya.reddy@gmail.com | Delhi | 6200.00 |
| 4 | Arjun Kumar | arjun.kumar@gmail.com | Bangalore | 8500.75 |
| 5 | Sneha Patel | sneha.patel@gmail.com | Chennai | 4500.25 |

---

## 4. SQL Joins In-Depth (All 6 Types)

A `JOIN` clause in SQL combines rows from two or more tables based on a related column between them.

```
       TABLE A                TABLE B
    +-----------+          +-----------+
    |           |  MATCH   |           |
    | LEFT ONLY | [BOTH A] | RIGHT ONLY|
    |           | [& B  ]  |           |
    +-----------+          +-----------+
```

### The 6 Types of Joins in PostgreSQL:
1. **INNER JOIN**: Returns only rows that match in both tables.
2. **LEFT JOIN**: Returns all rows from the left table, plus matched rows from the right table.
3. **RIGHT JOIN**: Returns all rows from the right table, plus matched rows from the left table.
4. **FULL JOIN**: Returns all rows from both tables, filling missing matches with `NULL`.
5. **SELF JOIN**: Joins a table with itself using aliases (ideal for hierarchies).
6. **CROSS JOIN**: Produces the Cartesian product (all possible combinations of rows).

---

### 4.1 INNER JOIN

- **How it Works**: Returns records only when there is a match in **both** the left and right tables. If a row in the left table does not match a row in the right table, it is omitted.

#### Syntax:
```sql
SELECT columns
FROM table_a a
INNER JOIN table_b b
    ON a.matching_column = b.matching_column;
```

#### Practical Query:
Join `customers`, `salesreport`, `products`, and `locations`:
```sql
SELECT 
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS customer_name,
    p.product_name,
    s.quantity,
    s.total_amount,
    l.city AS store_location
FROM customers c 
INNER JOIN salesreport s 
    ON c.customer_id = s.customer_id
INNER JOIN products p 
    ON s.product_id = p.product_id
INNER JOIN locations l
    ON s.location_id = l.location_id
ORDER BY s.sale_id;
```

#### Output:
| customer_id | customer_name | product_name | quantity | total_amount | store_location |
|:---|:---|:---|:---|:---|:---|
| 1 | Omer Ali | Laptop | 2 | 129000.00 | Hyderabad |
| 2 | Rahul Sharma | Wireless Mouse | 3 | 3500.00 | Bengaluru |
| 3 | Priya Reddy | Mechanical Keyboard | 1 | 3300.00 | Mumbai |
| 4 | Arjun Kumar | Monitor 24 Inch | 2 | 29500.00 | Delhi |
| 5 | Sneha Patel | USB-C Hub | 4 | 9700.00 | Chennai |

*(Note: Customer 6 Vikram Singh does not appear because he has not made any purchase).*

---

### 4.2 LEFT JOIN (LEFT OUTER JOIN)

- **How it Works**: Returns **all** records from the left table, along with matching records from the right table. If there is no match on the right, PostgreSQL fills those columns with `NULL`.

#### Syntax:
```sql
SELECT columns
FROM table_a a
LEFT JOIN table_b b
    ON a.matching_column = b.matching_column;
```

#### Practical Query:
Retrieve all customers and their sales (including customers who have never bought anything):
```sql
SELECT 
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS customer_name,
    c.email,
    s.sale_id,
    s.sale_date,
    s.total_amount
FROM customers c
LEFT JOIN salesreport s 
    ON c.customer_id = s.customer_id
ORDER BY c.customer_id;
```

#### Output:
| customer_id | customer_name | email | sale_id | sale_date | total_amount |
|:---|:---|:---|:---|:---|:---|
| 1 | Omer Ali | omer.ali@gmail.com | 1 | 2026-09-01 | 129000.00 |
| 2 | Rahul Sharma | rahul.sharma@gmail.com | 2 | 2026-09-02 | 3500.00 |
| 3 | Priya Reddy | priya.reddy@gmail.com | 3 | 2026-09-03 | 3300.00 |
| 4 | Arjun Kumar | arjun.kumar@gmail.com | 4 | 2026-09-04 | 29500.00 |
| 5 | Sneha Patel | sneha.patel@gmail.com | 5 | 2026-09-05 | 9700.00 |
| 6 | Vikram Singh | vikram.singh@gmail.com | NULL | NULL | NULL |

*(Key takeaway: Vikram Singh is preserved in the output with `NULL` sales values).*

---

### 4.3 RIGHT JOIN (RIGHT OUTER JOIN)

- **How it Works**: Returns **all** records from the right table, and matching records from the left table. If no match exists on the left, PostgreSQL returns `NULL` for the left table's columns.

#### Syntax:
```sql
SELECT columns
FROM table_a a
RIGHT JOIN table_b b
    ON a.matching_column = b.matching_column;
```

#### Practical Query:
List all products and their sales details (including products that have never been sold):
```sql
SELECT 
    p.product_id,
    p.product_name,
    p.unit_price,
    s.sale_id,
    s.quantity,
    s.total_amount
FROM salesreport s
RIGHT JOIN products p 
    ON s.product_id = p.product_id
ORDER BY p.product_id;
```

#### Output:
| product_id | product_name | unit_price | sale_id | quantity | total_amount |
|:---|:---|:---|:---|:---|:---|
| 1 | Laptop | 65000.00 | 1 | 2 | 129000.00 |
| 2 | Wireless Mouse | 1200.00 | 2 | 3 | 3500.00 |
| 3 | Mechanical Keyboard | 3500.00 | 3 | 1 | 3300.00 |
| 4 | Monitor 24 Inch | 15000.00 | 4 | 2 | 29500.00 |
| 5 | USB-C Hub | 2500.00 | 5 | 4 | 9700.00 |
| 6 | 4K Webcam | 4500.00 | NULL | NULL | NULL |

*(Key takeaway: Product 6 '4K Webcam' is preserved even though it has no entries in `salesreport`).*

---

### 4.4 FULL JOIN (FULL OUTER JOIN)

- **How it Works**: Combines the results of both `LEFT JOIN` and `RIGHT JOIN`. It returns all rows from both tables. When rows match, they are joined; when there is no match on either side, `NULL` values are returned.

#### Syntax:
```sql
SELECT columns
FROM table_a a
FULL OUTER JOIN table_b b
    ON a.matching_column = b.matching_column;
```

#### Practical Query:
Join `customers` with `salesreport` using `FULL OUTER JOIN`:
```sql
SELECT 
    c.customer_id,
    CONCAT_WS(' ', c.first_name, c.last_name) AS customer_name,
    s.sale_id,
    s.product_id,
    s.total_amount
FROM customers c
FULL OUTER JOIN salesreport s 
    ON c.customer_id = s.customer_id
ORDER BY c.customer_id;
```

#### Output:
| customer_id | customer_name | sale_id | product_id | total_amount |
|:---|:---|:---|:---|:---|
| 1 | Omer Ali | 1 | 1 | 129000.00 |
| 2 | Rahul Sharma | 2 | 2 | 3500.00 |
| 3 | Priya Reddy | 3 | 3 | 3300.00 |
| 4 | Arjun Kumar | 4 | 4 | 29500.00 |
| 5 | Sneha Patel | 5 | 5 | 9700.00 |
| 6 | Vikram Singh | NULL | NULL | NULL |

---

### 4.5 SELF JOIN

- **How it Works**: A `SELF JOIN` joins a table **to itself**. It is typically used when rows inside the same table have hierarchical relationships (e.g., an employee report-to manager hierarchy).

#### Sample Organizational Hierarchy Table:
```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    manager_id INT
);

INSERT INTO employees (emp_id, emp_name, job_title, manager_id) 
VALUES
    (1, 'Sara Ahmed', 'Regional Director', NULL),
    (2, 'Omer Ali', 'Engineering Lead', 1),
    (3, 'Rahul Sharma', 'Senior Developer', 2),
    (4, 'Priya Reddy', 'Data Analyst', 1),
    (5, 'Arjun Kumar', 'Backend Developer', 2);
```

#### Syntax:
```sql
SELECT 
    e.column_name AS employee_info,
    m.column_name AS manager_info
FROM table_name e
LEFT JOIN table_name m
    ON e.manager_id = m.primary_id;
```

#### Practical Query:
Retrieve every employee alongside their respective manager's name:
```sql
SELECT 
    e.emp_id,
    e.emp_name AS employee_name,
    e.job_title AS designation,
    COALESCE(m.emp_name, 'Top Executive (No Manager)') AS manager_name
FROM employees e
LEFT JOIN employees m 
    ON e.manager_id = m.emp_id
ORDER BY e.emp_id;
```

#### Output:
| emp_id | employee_name | designation | manager_name |
|:---|:---|:---|:---|
| 1 | Sara Ahmed | Regional Director | Top Executive (No Manager) |
| 2 | Omer Ali | Engineering Lead | Sara Ahmed |
| 3 | Rahul Sharma | Senior Developer | Omer Ali |
| 4 | Priya Reddy | Data Analyst | Sara Ahmed |
| 5 | Arjun Kumar | Backend Developer | Omer Ali |

---

### 4.6 CROSS JOIN (Cartesian Product)

- **How it Works**: Matches **every single row** of the first table with **every single row** of the second table. 
- If Table A has $M$ rows and Table B has $N$ rows, the result contains $M \times N$ rows.
- No `ON` condition is required.

#### Syntax:
```sql
-- Explicit syntax (Recommended)
SELECT columns
FROM table_a
CROSS JOIN table_b;

-- Comma syntax (Older SQL standard)
SELECT columns
FROM table_a, table_b;
```

#### Practical Query:
Generate all potential product deployment combinations across store locations (pairing 3 products with 2 locations = $3 \times 2 = 6$ rows):
```sql
SELECT 
    p.product_name,
    p.category,
    l.city,
    l.country
FROM (
    SELECT product_name, category 
    FROM products 
    WHERE product_id <= 3
) p
CROSS JOIN (
    SELECT city, country 
    FROM locations 
    WHERE location_id <= 2
) l
ORDER BY p.product_name, l.city;
```

#### Output:
| product_name | category | city | country |
|:---|:---|:---|:---|
| Laptop | Electronics | Bengaluru | India |
| Laptop | Electronics | Hyderabad | India |
| Mechanical Keyboard | Accessories | Bengaluru | India |
| Mechanical Keyboard | Accessories | Hyderabad | India |
| Wireless Mouse | Accessories | Bengaluru | India |
| Wireless Mouse | Accessories | Hyderabad | India |

---

## 5. Joins Comparison Cheat Sheet

| Join Type | Returns Matching Rows? | Returns Unmatched Left Rows? | Returns Unmatched Right Rows? | Typical Use Case |
|:---|:---:|:---:|:---:|:---|
| **`INNER JOIN`** | Yes | No | No | Fetching only records that exist simultaneously in both tables (e.g., active orders with valid customers). |
| **`LEFT JOIN`** | Yes | Yes (with `NULL` right cols) | No | Preserving all master records (e.g., all customers, showing `NULL` if no orders placed). |
| **`RIGHT JOIN`** | Yes | No | Yes (with `NULL` left cols) | Auditing all reference records (e.g., all catalog products, showing `NULL` if never sold). |
| **`FULL JOIN`** | Yes | Yes (with `NULL` right cols) | Yes (with `NULL` left cols) | Reconciliation reports, identifying orphan records across both sides. |
| **`SELF JOIN`** | Yes | Optional (`LEFT JOIN`) | Optional | Recursive hierarchies, employee-to-manager links, category trees. |
| **`CROSS JOIN`** | All combinations | All combinations | All combinations | Matrix generation, price simulations, testing combinations. |