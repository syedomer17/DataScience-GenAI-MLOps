# PostgreSQL Hands-on: Database Creation, Constraints, and CSV Import/Export

This document walks you through a complete example of creating a database, defining a table with constraints, inserting data, and importing/exporting data using CSV files in **PostgreSQL**.

---

## 1. Setup Database and Table

### A. Create and Connect to the Database
First, create a new database called `courses` and connect to it:

```sql
-- Create the database
CREATE DATABASE courses;

-- Connect to the database (psql meta-command)
\c courses
```

### B. Create a Table with Constraints
Next, create a `customers` table. We use constraints like `SERIAL`, `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, and `CHECK` to ensure data integrity:

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW(),
    age SMALLINT CHECK (age > 17)
);
```

### C. Inspect Table Schema
To check the description and columns of your table inside the `psql` shell:

```sql
\d customers
```

---

## 2. Managing Data

### A. Inserting Data
Insert sample rows into the `customers` table:

```sql
INSERT INTO customers (name, email, age) VALUES 
('omer', 'omer@gmail.com', 20),
('ali', 'ali123@gmail.com', 19);
```

### B. Querying Data
To see all the rows and data in the table:

```sql
SELECT * FROM customers;
```

---

## 3. Importing and Exporting Data (CSV)

### A. Importing Data from a CSV File
If you have data in a CSV/Excel file and want to load it into a PostgreSQL table:
1. Ensure the CSV columns match the database table structure.
2. Match the column names, datatypes, and formats exactly.
3. Run the `\copy` command in the `psql` terminal.

**Syntax:**
```sql
\copy table_name(column1, column2, ...) FROM '/path/to/file.csv' DELIMITER ',' CSV HEADER;
```

**Example:**
```sql
\copy customers(name, email, age) FROM '/Users/syedomerali/data.csv' DELIMITER ',' CSV HEADER;
```

> [!NOTE]
> `CSV HEADER` tells PostgreSQL to ignore the first row of the CSV file because it contains column headers (like `name`, `email`, `age`), rather than actual data.

### B. Exporting Data to a CSV File
You can also export your database tables or specific query results to a CSV file.

#### Option 1: Export an entire table
```sql
\copy table_name TO '/path/to/destination.csv' DELIMITER ',' CSV HEADER;
```

**Example:**
```sql
\copy customers TO '/Users/syedomerali/Dummy.csv' DELIMITER ',' CSV HEADER;
```

#### Option 2: Export results of a specific query
You can filter the data before exporting by using a `SELECT` query inside the `\copy` command:
```sql
\copy (SELECT * FROM customers WHERE age < 20) TO '/Users/syedomerali/Dummy.csv' DELIMITER ',' CSV HEADER;
```

---

## 4. SQL Clauses, Operators, and Filtering

SQL clauses and operators are built-in keywords used to filter, sort, limit, group, and summarize data from database tables.

---

### A. `WHERE` Clause
- **Explanation**: Used to filter rows that meet a specific condition. Only records where the condition evaluates to `TRUE` are returned.
- **Syntax**:
  ```sql
  SELECT column1, column2, ...
  FROM table_name
  WHERE condition;
  ```
- **Example**:
  ```sql
  -- Select all customers who are older than 18
  SELECT * FROM customers 
  WHERE age > 18;
  ```

---

### B. `ORDER BY` Clause
- **Explanation**: Sorts the query result set in ascending (`ASC`) or descending (`DESC`) order based on one or more columns.
- **Note**: By default, `ORDER BY` sorts in ascending (`ASC`) order if no direction is specified.
- **Syntax**:
  ```sql
  SELECT column1, column2, ...
  FROM table_name
  ORDER BY column_name [ASC | DESC];
  ```
- **Examples**:
  ```sql
  -- Sort customers by created_at in descending order (newest first)
  SELECT * FROM customers 
  ORDER BY created_at DESC;

  -- Sort by age ascending, and then by name ascending
  SELECT * FROM customers 
  ORDER BY age ASC, name ASC;
  ```

---

### C. `LIMIT` and `OFFSET` Clauses
- **Explanation**:
  - `LIMIT`: Restricts the maximum number of rows returned by a query (e.g., top 5 records).
  - `OFFSET`: Skips a specified number of rows before beginning to return results.
  - When used together, `LIMIT` and `OFFSET` enable pagination (e.g., displaying records page by page).
- **Syntax**:
  ```sql
  SELECT column1, column2, ...
  FROM table_name
  [ORDER BY column_name]
  LIMIT number_of_rows OFFSET number_to_skip;
  ```
- **Examples**:
  ```sql
  -- Get the top 5 newest customers
  SELECT * FROM customers 
  ORDER BY created_at DESC 
  LIMIT 5;

  -- Skip the first 5 records and return the next 5 records (Page 2)
  SELECT * FROM customers 
  ORDER BY id ASC 
  LIMIT 5 OFFSET 5;
  ```

---

### D. `DISTINCT` Keyword
- **Explanation**: Removes duplicate rows from the query results, returning only unique values or unique combinations of values.
- **Syntax**:
  ```sql
  SELECT DISTINCT column1, column2, ...
  FROM table_name;
  ```
- **Example**:
  ```sql
  -- Get all unique ages from the customers table sorted from oldest to youngest
  SELECT DISTINCT age 
  FROM customers 
  ORDER BY age DESC;
  ```

---

### E. `BETWEEN` Operator
- **Explanation**: A logical operator used within a `WHERE` clause to select values within a continuous, inclusive range (both start and end boundaries are included).
- **Syntax**:
  ```sql
  SELECT column1, column2, ...
  FROM table_name
  WHERE column_name BETWEEN value1 AND value2;
  ```
- **Example**:
  ```sql
  -- Select customers whose age is between 18 and 25 (inclusive)
  SELECT * FROM customers 
  WHERE age BETWEEN 18 AND 25;
  ```

---

### F. `IN` Operator
- **Explanation**: A logical operator used in a `WHERE` clause to check if a column's value matches any value in a specified list. It serves as a cleaner shorthand for multiple `OR` conditions.
- **Syntax**:
  ```sql
  SELECT column1, column2, ...
  FROM table_name
  WHERE column_name IN (value1, value2, ...);
  ```
- **Example**:
  ```sql
  -- Select customers whose age is either 18, 19, or 25
  SELECT * FROM customers 
  WHERE age IN (18, 19, 25);
  ```

---

### G. `LIKE` and `ILIKE` Operators
- **Explanation**:
  - `LIKE`: Searches for a specific text pattern within a column. It is **case-sensitive**.
  - `ILIKE`: A PostgreSQL-specific extension that performs **case-insensitive** pattern matching.
  - **Pattern Wildcards**:
    - `%` : Represents zero, one, or multiple characters.
    - `_` : Represents exactly one single character.
- **Syntax**:
  ```sql
  -- Case-sensitive search
  SELECT column1, column2, ...
  FROM table_name
  WHERE column_name LIKE 'pattern';

  -- Case-insensitive search (PostgreSQL)
  SELECT column1, column2, ...
  FROM table_name
  WHERE column_name ILIKE 'pattern';
  ```
- **Examples**:
  ```sql
  -- Match names starting with capital 'A' (e.g., 'Ali')
  SELECT * FROM customers 
  WHERE name LIKE 'A%';

  -- Match emails containing 'omer' regardless of uppercase or lowercase (e.g., 'omer@gmail.com', 'OMER@GMAIL.COM')
  SELECT * FROM customers 
  WHERE email ILIKE '%omer%';

  -- Match names where the second letter is 'a' (e.g., 'Sam', 'Dan')
  SELECT * FROM customers 
  WHERE name LIKE '_a%';
  ```

---

### H. `GROUP BY` Clause
- **Explanation**: Groups rows that share identical values in specified columns into summary rows. It is most commonly used with aggregate functions (such as `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`) to compute summary metrics per group.
- **Syntax**:
  ```sql
  SELECT column_name, AGGREGATE_FUNCTION(column_name)
  FROM table_name
  GROUP BY column_name;
  ```
- **Example**:
  ```sql
  -- Count how many customers exist for each age
  SELECT age, COUNT(*) AS total_customers 
  FROM customers 
  GROUP BY age 
  ORDER BY age DESC;
  ```

---

### I. `HAVING` Clause
- **Explanation**: Filters grouped records and aggregate function results. While `WHERE` filters individual rows *before* grouping, `HAVING` filters groups *after* the `GROUP BY` aggregation has been performed.
- **Syntax**:
  ```sql
  SELECT column_name, AGGREGATE_FUNCTION(column_name)
  FROM table_name
  GROUP BY column_name
  HAVING AGGREGATE_CONDITION;
  ```
- **Example**:
  ```sql
  -- Find only the age groups that have more than 4 customers
  SELECT age, COUNT(*) AS total_customers 
  FROM customers 
  GROUP BY age 
  HAVING COUNT(*) > 4;
  ```