# PostgreSQL Indexes, Views & Materialized Views

In this class, we cover three essential database performance and organization tools in PostgreSQL:
1. **Indexes** — Speeding up query lookups.
2. **Views** — Creating reusable, virtual tables from queries.
3. **Materialized Views** — Storing query results physically on disk for lightning-fast reporting.

---

## Part 1: PostgreSQL Indexes

### 1. What is an Index?

An **Index** is a specialized data structure that PostgreSQL creates to find rows in a table much faster.

- **The Textbook Analogy:**  
  Imagine you have a 1,000-page book and want to find the topic *"Indexing"*.
  - **Without an index:** You must flip through all 1,000 pages one by one until you find it. In database terms, this is called a **Full Table Scan (Sequential Scan / Seq Scan)**.
  - **With an index:** You look up *"Indexing"* in the book's index at the back, see that it is on page 425, and jump directly to page 425. In database terms, this is called an **Index Scan**.

### Why Not Index Every Column?
Indexes make reading (`SELECT`) faster, but they have trade-offs:
- **Disk Space:** Indexes take extra storage on disk.
- **Write Performance:** Every `INSERT`, `UPDATE`, and `DELETE` becomes slightly slower because PostgreSQL must update the table **and** every index on that table.

---

### 2. Practice Database & Dataset Setup

Let's create a database called `dummy` and populate a table named `users` with **1,000,000 rows** of random data to see the performance difference.

```sql
-- Step 1: Create a practice database
CREATE DATABASE dummy;

-- Step 2: Connect to the database
\c dummy

-- Step 3: Create a table with 1,000,000 records
CREATE TABLE users AS 
SELECT 
    generate_series(1, 1000000) AS id,
    md5(random()::text) AS email;
```

> **Explanation of the query:**
> - `generate_series(1, 1000000) AS id`: Generates numbers from 1 to 1,000,000.
> - `md5(random()::text) AS email`: Generates a random 32-character string to simulate random email hashes.

---

### 3. Measuring Query Performance: `EXPLAIN ANALYZE`

To see how long a query takes and whether PostgreSQL uses an index or a full table scan, use the `EXPLAIN (ANALYZE, BUFFERS)` command:

```sql
-- Check performance BEFORE adding an index
EXPLAIN (ANALYZE, BUFFERS) 
SELECT * FROM users WHERE email = 'abc123xyz';
```

**Output Breakdown:**
- **`Seq Scan on users`**: PostgreSQL scanned all 1,000,000 rows one by one.
- **`Execution Time`**: Usually takes **30 ms – 100 ms** (or more depending on hardware).
- **`Buffers: shared read=...`**: PostgreSQL had to read thousands of disk blocks into memory.

---

### 4. Index Types in PostgreSQL

PostgreSQL supports several types of indexes. The three most common are:

#### A. B-Tree Index (Default)
- **What it is:** A self-balancing search tree (Balanced Tree).
- **When to use:** It is the default index type and works best for most scenarios.
- **Supported operators:** `=`, `<`, `<=`, `>`, `>=`, `BETWEEN`, `IN`, `IS NULL`, and `ORDER BY`.

**Syntax:**
```sql
CREATE INDEX <index_name> ON <table_name>(<column_name>);
```

**Example:**
```sql
-- Create a B-Tree index on the email column
CREATE INDEX idx_users_email ON users(email);
```

**Test the Query Again:**
```sql
EXPLAIN (ANALYZE, BUFFERS) 
SELECT * FROM users WHERE email = 'abc123xyz';
```
> **Result:** The execution plan changes from `Seq Scan` to **`Index Scan using idx_users_email`**, and execution time drops from ~50 ms to **under 0.1 ms**!

---

#### B. Hash Index
- **What it is:** Uses a 32-bit hash code to look up keys quickly.
- **When to use:** Only when you do **exact equality comparisons (`=`)**.
- **Limitations:** Hash indexes do **not** support range queries (`<`, `>`, `BETWEEN`) or sorting (`ORDER BY`).

**Syntax:**
```sql
CREATE INDEX <index_name> ON <table_name> USING HASH (<column_name>);
```

**Example:**
```sql
-- Create a Hash index on the email column
CREATE INDEX idx_users_hash ON users USING HASH (email);
```

---

#### C. GIN Index (Generalized Inverted Index)
- **What it is:** An inverted index designed for values containing multiple elements (like a book index maps a word to multiple page numbers).
- **When to use:**
  1. **Arrays** (`text[]`, `int[]`) — finding elements inside an array.
  2. **JSONB** (`jsonb`) — searching keys or values inside nested JSON.
  3. **Full-Text Search** (`tsvector`) — searching words inside documents.
  4. **Pattern Matching (`LIKE '%text%'`)** — using the `pg_trgm` extension.

> **Note on Text Columns:** Standard PostgreSQL does not allow a GIN index on plain `text` columns directly. You must enable the `pg_trgm` (trigram) extension first.

**Example 1: Trigram Matching on Email with GIN:**
```sql
-- Enable the trigram extension
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Create GIN index for text search
CREATE INDEX idx_users_email_gin ON users USING GIN (email gin_trgm_ops);

-- This makes substring search very fast:
SELECT * FROM users WHERE email LIKE '%a1b2%';
```

**Example 2: GIN on an Array Column:**
```sql
-- Add an array column for tags
ALTER TABLE users ADD COLUMN tags text[];

-- Update some sample data
UPDATE users SET tags = ARRAY['admin', 'verified'] WHERE id = 1;

-- Create GIN index on the array column
CREATE INDEX idx_users_tags_gin ON users USING GIN (tags);

-- Fast lookup for rows containing a specific tag:
SELECT * FROM users WHERE tags @> ARRAY['admin'];
```

---

### 5. Dropping an Index

If an index is no longer needed, you can delete it with `DROP INDEX`:

**Syntax:**
```sql
DROP INDEX <index_name>;
```

**Example:**
```sql
-- Drop the B-Tree index
DROP INDEX idx_users_email;

-- Drop the Hash index
DROP INDEX idx_users_hash;

-- Drop the GIN index
DROP INDEX idx_users_email_gin;
```

---

### 6. Summary Comparison: Index Types

| Index Type | Best Used For | Supported Operators | Speed |
| :--- | :--- | :--- | :--- |
| **B-Tree** *(Default)* | Numbers, text, dates, ranges, sorting | `=`, `<`, `<=`, `>`, `>=`, `BETWEEN`, `IN`, `ORDER BY` | Fast and versatile |
| **Hash** | Exact equality lookup only | `=` | Extremely fast for `=` |
| **GIN** | Arrays, JSONB, full-text search, trigrams | `@>`, `?`, `@@`, `LIKE '%abc%'` (with `pg_trgm`) | Fast searches, slower writes |

---

## Part 2: PostgreSQL Views

### 1. What is a View?

A **View** is a **virtual table** defined by a saved SQL `SELECT` query.
- It **does not store data physically** on the hard drive.
- It only stores the **query definition**.
- Every time you query a view, PostgreSQL automatically runs the underlying query behind the scenes and returns fresh, up-to-date data.

### Why Use Views?
1. **Simplicity:** Hides complex joins and aggregate queries behind a simple table name.
2. **Security & Data Access Control:** Expose only specific columns to certain users without showing sensitive columns (like passwords or salaries).
3. **Consistency:** All developers and reports use the same standard query definition.

---

### 2. Practice Table Setup for Views

Let's create a table called `viewusers` with 2,000,000 rows and a `status` column:

```sql
-- Step 1: Create a table with 2,000,000 rows
CREATE TABLE viewusers AS 
SELECT 
    generate_series(1, 2000000) AS id,
    md5(random()::text) AS email;

-- Step 2: Add a status column
ALTER TABLE viewusers ADD COLUMN status INT;

-- Step 3: Assign status values in batches
UPDATE viewusers SET status = 1 WHERE id BETWEEN 1 AND 500000;
UPDATE viewusers SET status = 2 WHERE id BETWEEN 500001 AND 1000000;
UPDATE viewusers SET status = 3 WHERE id BETWEEN 1000001 AND 1500000;
UPDATE viewusers SET status = 4 WHERE id BETWEEN 1500001 AND 2000000;

-- Step 4: Verify count for each status
SELECT status, COUNT(email) 
FROM viewusers 
GROUP BY status;
```

---

### 3. Creating and Using a View

**Syntax:**
```sql
CREATE VIEW <view_name> AS 
<SELECT_QUERY>;
```

**Example:**
Create a view called `status1` that shows only users where `status = 1`:

```sql
-- Create the view
CREATE VIEW status1 AS 
SELECT id, email 
FROM viewusers 
WHERE status = 1;
```

#### Querying the View:
Treat the view just like a regular table:
```sql
-- Query the view
SELECT * FROM status1 LIMIT 10;

-- Filter the view further
SELECT * FROM status1 WHERE id < 100;
```

#### Dropping a View:
**Syntax:**
```sql
DROP VIEW <view_name>;
```

**Example:**
```sql
DROP VIEW status1;
```

---

## Part 3: PostgreSQL Materialized Views

### 1. What is a Materialized View?

A **Materialized View** is a database object that executes a query and **physically saves (caches) the result on disk** as a real table.

- **Unlike a regular View:** It does **not** re-run the underlying query every time you read from it.
- **Query Speed:** Reads are instant because data is precomputed and read directly from disk.
- **Trade-off (Stale Data):** When the base table changes (new rows inserted, updated, or deleted), the materialized view **does not update automatically**. You must refresh it explicitly.

---

### 2. Creating and Using a Materialized View

**Syntax:**
```sql
CREATE MATERIALIZED VIEW <mview_name> AS 
<SELECT_QUERY>;
```

**Example:**
```sql
-- Create a materialized view storing status = 1 records
CREATE MATERIALIZED VIEW mstatus1 AS 
SELECT id, email 
FROM viewusers 
WHERE status = 1;
```

#### Querying the Materialized View:
```sql
-- Read from the materialized view (instant response)
SELECT * FROM mstatus1 LIMIT 10;
```

---

### 3. Refreshing a Materialized View

When base table data changes, update the materialized view with `REFRESH MATERIALIZED VIEW`:

```sql
-- Standard refresh (locks the view for reads while refreshing)
REFRESH MATERIALIZED VIEW mstatus1;
```

#### Refreshing Without Locking Reads (`CONCURRENTLY`):
To allow users to continue querying the materialized view while it is refreshing in the background:
```sql
-- Step 1: Create a UNIQUE index on the materialized view (required for CONCURRENTLY)
CREATE UNIQUE INDEX idx_mstatus1_id ON mstatus1(id);

-- Step 2: Refresh concurrently without blocking reads
REFRESH MATERIALIZED VIEW CONCURRENTLY mstatus1;
```

---

### 4. Dropping a Materialized View

**Syntax:**
```sql
DROP MATERIALIZED VIEW <mview_name>;
```

**Example:**
```sql
DROP MATERIALIZED VIEW mstatus1;
```

---

## Part 4: Key Differences: View vs Materialized View

| Feature | Standard View (Regular View) | Materialized View |
| :--- | :--- | :--- |
| **Storage** | **Virtual** — No data stored on disk (stores only SQL query logic). | **Physical** — Query result is saved on disk like a table. |
| **Data Freshness** | **Always real-time** — Evaluates query on every read. | **Snapshot** — Can become stale until refreshed. |
| **Read Speed** | Same as executing the underlying query (can be slow for complex queries). | **Very fast** — Reads precomputed results directly from disk. |
| **Indexes** | Cannot create indexes directly on a regular view. | **Can create indexes** (B-Tree, Hash, Unique) on it. |
| **Refresh Mechanism** | Not needed (automatic on every query). | Manual or scheduled using `REFRESH MATERIALIZED VIEW`. |
| **Best Use Case** | - Simplifying queries<br>- Row/column access security<br>- Real-time data requirements | - Heavy aggregations (e.g., `SUM`, `AVG`, `COUNT`)<br>- Analytical dashboards and reports<br>- Slowly changing data |

---

## Quick Revision Summary

1. **Indexes** speed up searches:
   - `B-Tree` (default) for `=`, `>`, `<`, ranges, and ordering.
   - `HASH` for exact `=` lookup.
   - `GIN` for multi-value types (Arrays, JSONB, Full-Text, Trigrams).
   - Use `EXPLAIN (ANALYZE, BUFFERS)` to test query performance before and after indexing.
2. **Views** (`CREATE VIEW`) store the query logic without saving data. Always up-to-date, great for security and simplifying complex SQL.
3. **Materialized Views** (`CREATE MATERIALIZED VIEW`) store the query result on disk. Extremely fast for heavy reporting queries, but requires `REFRESH MATERIALIZED VIEW` to update stale data.