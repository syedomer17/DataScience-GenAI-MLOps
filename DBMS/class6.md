# Modifying Table Structure with ALTER TABLE (DDL)

The `ALTER TABLE` statement in SQL (Data Definition Language - DDL) is used to modify the structure of an existing table **without losing the data already stored inside it**.

You use `ALTER TABLE` when you need to:
- Add new columns
- Delete (drop) unused columns
- Rename columns or the table itself
- Change a column's data type
- Add or remove constraints (like `UNIQUE`, `NOT NULL`, `DEFAULT`, or `CHECK`)

---

## Sample Table for Practice

To follow along with the examples, imagine we have an existing table named `customers`:

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    created_at DATE DEFAULT CURRENT_DATE
);

-- Sample Data
INSERT INTO customers (name, age) 
VALUES 
('Omer', 22),
('Ali', 25);
```

### Initial Table Data:
| id | name | age | created_at |
|:---|:---|:---|:---|
| 1 | Omer | 22 | 2026-09-03 |
| 2 | Ali | 25 | 2026-09-03 |

---

## 1. Adding New Columns (`ADD COLUMN`)

Adds one or more new columns to an existing table. New columns are automatically populated with `NULL` for existing rows unless a default value is specified.

### Syntax:
```sql
ALTER TABLE table_name 
ADD COLUMN column_name data_type [constraints];
```

### Examples:

**Example A: Add a simple text column**
```sql
ALTER TABLE customers 
ADD COLUMN phone VARCHAR(15);
```

**Example B: Add a boolean column with a default value**
```sql
ALTER TABLE customers 
ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
```

**Example C: Add a column with a default value and NOT NULL**
```sql
ALTER TABLE customers 
ADD COLUMN country VARCHAR(50) DEFAULT 'Pakistan' NOT NULL;
```

**Example D: Add multiple columns in a single statement**
```sql
ALTER TABLE customers 
ADD COLUMN email VARCHAR(100),
ADD COLUMN city VARCHAR(50) DEFAULT 'Karachi';
```

---

## 2. Dropping Columns (`DROP COLUMN`)

Deletes an existing column and all data stored in that column permanently.

### Syntax:
```sql
ALTER TABLE table_name 
DROP COLUMN column_name;
```

### Examples:

**Example A: Drop a column**
```sql
ALTER TABLE customers 
DROP COLUMN phone;
```

**Example B: Drop a column only if it exists (prevents errors)**
```sql
ALTER TABLE customers 
DROP COLUMN IF EXISTS phone;
```

**Example C: Drop a column that has dependencies (foreign keys, views)**
```sql
ALTER TABLE customers 
DROP COLUMN country CASCADE;
```

---

## 3. Renaming Columns (`RENAME COLUMN`)

Changes the name of an existing column while keeping its data type and values intact.

### Syntax:
```sql
ALTER TABLE table_name 
RENAME COLUMN old_column_name TO new_column_name;
```

### Examples:

**Example A: Rename a date column**
```sql
ALTER TABLE customers 
RENAME COLUMN created_at TO admission_date;
```

**Example B: Rename a contact column**
```sql
ALTER TABLE customers 
RENAME COLUMN name TO full_name;
```

---

## 4. Changing Column Data Type (`ALTER COLUMN ... TYPE`)

Modifies the data type of an existing column (e.g., changing from `INT` to `BIGINT`, or expanding `VARCHAR(50)` to `VARCHAR(100)`).

### Syntax:
```sql
ALTER TABLE table_name 
ALTER COLUMN column_name TYPE new_data_type;
```

### Examples:

**Example A: Expand character limit**
```sql
ALTER TABLE customers 
ALTER COLUMN full_name TYPE VARCHAR(100);
```

**Example B: Change numeric precision**
```sql
ALTER TABLE customers 
ALTER COLUMN age TYPE SMALLINT;
```

**Example C: Change type with automatic data conversion (`USING` clause)**
*If PostgreSQL cannot automatically convert the data, specify conversion using `USING`:*
```sql
-- Convert an integer column to text
ALTER TABLE customers 
ALTER COLUMN age TYPE VARCHAR(10) USING age::VARCHAR;
```

---

## 5. Setting and Removing Default Values

Controls the automatic fallback value when a new row is inserted without specifying that column.

### A. Set a Default Value:
```sql
ALTER TABLE table_name 
ALTER COLUMN column_name SET DEFAULT default_value;
```
**Example:**
```sql
ALTER TABLE customers 
ALTER COLUMN city SET DEFAULT 'Islamabad';
```

### B. Remove (Drop) a Default Value:
```sql
ALTER TABLE table_name 
ALTER COLUMN column_name DROP DEFAULT;
```
**Example:**
```sql
ALTER TABLE customers 
ALTER COLUMN city DROP DEFAULT;
```

---

## 6. Setting and Removing `NOT NULL` Constraints

Determines whether a column can accept empty (`NULL`) values.

### A. Add `NOT NULL` (Disallow NULL values):
> **Note:** Existing rows must not contain any `NULL` values in that column before adding this constraint.

```sql
ALTER TABLE table_name 
ALTER COLUMN column_name SET NOT NULL;
```
**Example:**
```sql
ALTER TABLE customers 
ALTER COLUMN email SET NOT NULL;
```

### B. Remove `NOT NULL` (Allow NULL values):
```sql
ALTER TABLE table_name 
ALTER COLUMN column_name DROP NOT NULL;
```
**Example:**
```sql
ALTER TABLE customers 
ALTER COLUMN email DROP NOT NULL;
```

---

## 7. Adding and Dropping Constraints

Constraints enforce business rules (like uniqueness or valid ranges).

### A. Add a `UNIQUE` Constraint
Ensures all values in the column are distinct:
```sql
ALTER TABLE customers 
ADD CONSTRAINT uq_customers_email UNIQUE (email);
```

### B. Add a `CHECK` Constraint
Ensures column values meet a condition:
```sql
ALTER TABLE customers 
ADD CONSTRAINT chk_customer_age CHECK (age >= 18);
```

### C. Add a `FOREIGN KEY` Constraint
Links a column to another table's primary key:
```sql
-- Assuming a table named 'cities' exists with primary key 'city_id'
ALTER TABLE customers 
ADD COLUMN city_id INT,
ADD CONSTRAINT fk_customers_city 
FOREIGN KEY (city_id) REFERENCES cities(city_id);
```

### D. Drop a Constraint
Removes a constraint using its assigned name:
```sql
ALTER TABLE customers 
DROP CONSTRAINT uq_customers_email;
```

---

## 8. Renaming the Entire Table (`RENAME TO`)

Renames the table to a new name.

### Syntax:
```sql
ALTER TABLE old_table_name 
RENAME TO new_table_name;
```

### Example:
```sql
ALTER TABLE customers 
RENAME TO client_accounts;
```

---

## Complete Hands-On Walkthrough

Here is a full sequence showing how a table evolves through `ALTER TABLE` commands:

```sql
-- Step 1: Create initial table
CREATE TABLE staff (
    emp_id INT PRIMARY KEY,
    name VARCHAR(30)
);

-- Step 2: Add salary and join_date columns
ALTER TABLE staff 
ADD COLUMN salary NUMERIC(10, 2) DEFAULT 30000.00,
ADD COLUMN join_date DATE DEFAULT CURRENT_DATE;

-- Step 3: Rename name column to full_name
ALTER TABLE staff 
RENAME COLUMN name TO full_name;

-- Step 4: Add a CHECK constraint for positive salary
ALTER TABLE staff 
ADD CONSTRAINT chk_positive_salary CHECK (salary > 0);

-- Step 5: Add unique constraint on an email column
ALTER TABLE staff 
ADD COLUMN email VARCHAR(100),
ADD CONSTRAINT uq_staff_email UNIQUE (email);

-- Step 6: Drop a column if it is no longer required
ALTER TABLE staff 
DROP COLUMN IF EXISTS join_date;

-- Step 7: Rename table to employees
ALTER TABLE staff 
RENAME TO employees;
```

---

## Quick Reference Summary Table

| Operation | SQL Command Example |
|:---|:---|
| **Add column** | `ALTER TABLE customers ADD COLUMN email VARCHAR(100);` |
| **Add column with default** | `ALTER TABLE customers ADD COLUMN is_active BOOLEAN DEFAULT TRUE;` |
| **Drop column** | `ALTER TABLE customers DROP COLUMN phone;` |
| **Rename column** | `ALTER TABLE customers RENAME COLUMN created_at TO admission_date;` |
| **Change data type** | `ALTER TABLE customers ALTER COLUMN age TYPE INT;` |
| **Set default value** | `ALTER TABLE customers ALTER COLUMN city SET DEFAULT 'Karachi';` |
| **Remove default value** | `ALTER TABLE customers ALTER COLUMN city DROP DEFAULT;` |
| **Add NOT NULL** | `ALTER TABLE customers ALTER COLUMN email SET NOT NULL;` |
| **Remove NOT NULL** | `ALTER TABLE customers ALTER COLUMN email DROP NOT NULL;` |
| **Add UNIQUE constraint** | `ALTER TABLE customers ADD CONSTRAINT uq_phone UNIQUE (phone);` |
| **Add CHECK constraint** | `ALTER TABLE customers ADD CONSTRAINT chk_age CHECK (age >= 18);` |
| **Drop constraint** | `ALTER TABLE customers DROP CONSTRAINT uq_phone;` |
| **Rename table** | `ALTER TABLE customers RENAME TO clients;` |
