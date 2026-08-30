# PostgreSQL Basic Operations: Databases and Tables

This document covers the fundamental commands to create and manage databases, design tables, insert data, and query tables in **PostgreSQL**.

---

## 1. Database Operations

### A. Creating a Database
To create a new database:
```sql
CREATE DATABASE database_name;
```

**Example:**
```sql
CREATE DATABASE school_db;
```

### B. Connecting to a Database
If you are using the PostgreSQL interactive terminal (`psql`), use the meta-command `\c` (or `\connect`) to switch to a specific database:
```sql
\c database_name
```

**Example:**
```sql
\c school_db
```

### C. Deleting (Dropping) a Database
To delete a database:
1. First, make sure you are not connected to the database you want to delete. If you are, switch to another database (e.g., `\c postgres` or `\c template1`).
2. Run the `DROP DATABASE` command:
```sql
DROP DATABASE database_name;
```

**Example:**
```sql
DROP DATABASE school_db;
```

---

## 2. Table Operations

### A. Creating a Table
To create a table, use the `CREATE TABLE` statement followed by the table name and the list of columns with their respective data types.
```sql
CREATE TABLE table_name (
    column1 data_type,
    column2 data_type,
    ...
);
```

**Example:**
```sql
CREATE TABLE product (
    sno INT,
    name VARCHAR(50),
    quantity INT,
    price DECIMAL(8, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    approved BOOLEAN
);
```

> [!NOTE]
> Column names and table names in PostgreSQL are folded to lowercase by default unless enclosed in double quotes. It is standard practice to use lowercase snake_case for database identifiers.

### B. Viewing Tables and Schema (psql shortcuts)
When working in `psql`, you can inspect your database schema with these meta-commands:
- **List all tables:** `\dt`
- **Inspect table structure/columns:** `\d table_name`

---

## 3. Data Manipulation

### A. Inserting Data into a Table
There are two main methods to insert new rows into a table.

#### Method 1: Inserting values for all columns (in defined order)
If you provide values for all columns in the exact order they were defined in the table schema, you do not need to specify column names.
```sql
INSERT INTO table_name VALUES (value1, value2, value3, ...);
```

**Example:**
```sql
INSERT INTO product VALUES (
    1,
    'Omer',
    44,
    5.45,
    '2026-08-30 20:50:00',
    TRUE
);
```

#### Method 2: Inserting values for specific columns
If you only have values for certain columns, or want to make your SQL query robust against changes in column order, list the column names explicitly. Unlisted columns will be set to `NULL` (or their default values, if configured).
```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```

**Example:**
```sql
INSERT INTO product (sno, name) VALUES (1, 'Omer');
```

### B. Querying/Viewing Data from a Table
To retrieve and view the rows stored in a table, use the `SELECT` statement:
```sql
SELECT * FROM table_name;
```

**Example:**
```sql
SELECT * FROM product;
```

**Output Example:**
```text
 sno | name | quantity | price |     created_at      | approved 
-----+------+----------+-------+---------------------+----------
   1 | Omer |       44 |  5.45 | 2026-08-30 20:50:00 | t
(1 row)
```