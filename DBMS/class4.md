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