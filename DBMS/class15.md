# PostgreSQL Backup, Disaster Recovery & Performance Optimization

This class covers the two most critical responsibilities of a PostgreSQL Database Administrator (DBA) and Backend Engineer:
1. **Backup & Disaster Recovery** — Safeguarding data against hardware failure, corruption, human error, and ransomware.
2. **Database Performance Optimization & Maintenance** — Query tuning, indexing strategies, memory configuration, and database housekeeping.

---

## Part 1: PostgreSQL Backup & Restore

A database without tested backups is an active disaster waiting to happen. In PostgreSQL, backups fall into two main categories:

- **Logical Backups:** Exports database schema and data as SQL statements or compressed binary archives (`pg_dump`, `pg_dumpall`).
- **Physical Backups:** Copies the raw underlying data files from disk at the block level (`pg_basebackup` with WAL archiving for Point-in-Time Recovery).

---

### 1. The `pg_dump` Tool (Single Database Backup)

`pg_dump` is a command-line client utility that creates consistent, non-blocking backups of a single database—even while other users are reading and writing to it.

> **Important:** `pg_dump` is executed from your **operating system terminal (bash/zsh)**, NOT inside the `psql` prompt!

#### The 4 Output Formats of `pg_dump`:

| Flag | Format Name | File Extension | Pros & Cons | Best Used For |
| :--- | :--- | :---: | :--- | :--- |
| `-F p` *(Default)* | **Plain Text SQL** | `.sql` | Human-readable; editable with text editor; slower to restore. | Small databases, version control, quick inspection. |
| `-F c` | **Custom Archive** | `.dump` or `.backup` | Compressed binary; fastest to restore; supports selective table restores; used with `pg_restore`. | **Industry standard for production backups.** |
| `-F d` | **Directory** | directory | Compressed directory; supports parallel dumping/restoring (`-j`); very fast for multi-GB databases. | Very large enterprise databases. |
| `-F t` | **Tar Archive** | `.tar` | Simple tarball; supports selective restores; cannot use parallel threads. | Archival storage. |

---

### 2. Practical Backup Commands

Let's assume we have a database named `sales` and user `postgres`.

#### A. Backing Up to Plain Text SQL:
```bash
# General Syntax:
# pg_dump -U <username> -d <dbname> -f <output_file.sql>

# Example: Backup sales database to a plain SQL file
pg_dump -U postgres -d sales -f ~/Desktop/sales_backup.sql

# Alternative using shell redirection:
pg_dump -U postgres sales > ~/Desktop/sales_backup.sql
```

#### B. Backing Up to Compressed Custom Format (`-F c`):
```bash
# Recommended for production!
pg_dump -U postgres -F c -d sales -f ~/Desktop/sales_backup.dump
```

#### C. Backing Up Specific Tables Only (`-t`):
```bash
# Backup only the 'customers' and 'orders' tables
pg_dump -U postgres -d sales -t customers -t orders -F c -f ~/Desktop/customers_orders.dump
```

#### D. Schema-Only Backup (`-s` / `--schema-only`):
Back up table definitions, indexes, and constraints **without any row data**:
```bash
pg_dump -U postgres -d sales -s -f ~/Desktop/sales_schema_only.sql
```

#### E. Data-Only Backup (`-a` / `--data-only`):
Back up only table row data **without re-creating tables or indexes**:
```bash
pg_dump -U postgres -d sales -a -f ~/Desktop/sales_data_only.sql
```

#### F. Excluding Heavy or Log Tables (`-T`):
```bash
# Exclude heavy audit logs from the backup
pg_dump -U postgres -d sales -T audit_logs -F c -f ~/Desktop/sales_no_logs.dump
```

---

### 3. The `pg_dumpall` Tool (Entire Cluster Backup)

While `pg_dump` only backs up one database at a time, **`pg_dumpall`** backs up the **entire PostgreSQL cluster**, including:
1. All databases.
2. Global database roles and users.
3. Tablespaces and server-wide permissions.

```bash
# 1. Back up all databases, users, and passwords into a single SQL script
pg_dumpall -U postgres -f ~/Desktop/all_databases_backup.sql

# 2. Back up ONLY global objects (Roles, Users, and Tablespaces)
pg_dumpall -U postgres --globals-only -f ~/Desktop/cluster_globals.sql
```

---

### 4. Restoring Databases

How you restore a database depends on the format used during backup.

#### Case A: Restoring Plain Text SQL Files (`psql`)
Plain `.sql` files are restored using the standard `psql` command:

```bash
# Step 1: Create an empty target database if it does not exist
createdb -U postgres sales_restored

# Step 2: Restore data using the -f flag
psql -U postgres -d sales_restored -f ~/Desktop/sales_backup.sql

# Alternative using shell redirection:
psql -U postgres -d sales_restored < ~/Desktop/sales_backup.sql
```

#### Case B: Restoring Custom/Directory Archives (`pg_restore`)
Binary formats (`-F c` or `-F d`) must be restored using **`pg_restore`**:

```bash
# 1. Standard restore to an existing database:
createdb -U postgres sales_restored
pg_restore -U postgres -d sales_restored -v ~/Desktop/sales_backup.dump

# 2. Auto-create database during restore (-C / --create):
pg_restore -U postgres -C -d postgres -v ~/Desktop/sales_backup.dump

# 3. Clean restore (-c / --clean: drops existing tables before recreating them):
pg_restore -U postgres -c -d sales_restored -v ~/Desktop/sales_backup.dump

# 4. Multi-threaded Parallel Restore (-j for high speed on multi-core CPUs):
pg_restore -U postgres -d sales_restored -j 4 -v ~/Desktop/sales_backup.dump

# 5. Selective Restore: Restore ONLY the 'customers' table from a full backup:
pg_restore -U postgres -d sales_restored -t customers -v ~/Desktop/sales_backup.dump
```

---

### 5. Production Automation: Automated Backup Script

In production, you schedule backups using a shell script triggered by a `cron` job.

#### Step 1: Configure Passwordless Authentication (`~/.pgpass`)
Avoid hardcoding passwords in scripts. Create a `~/.pgpass` file:
```bash
# Format: hostname:port:database:username:password
localhost:5432:*:postgres:MySecurePassword123
```
Set permissions (PostgreSQL requires strict 600 permissions):
```bash
chmod 600 ~/.pgpass
```

#### Step 2: Automated Backup Script (`backup.sh`)
```bash
#!/bin/bash
# Backup Configuration
BACKUP_DIR="/var/backups/postgres"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="sales"
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_$DATE.dump"

# Ensure backup directory exists
mkdir -p $BACKUP_DIR

# Run compressed backup
pg_dump -U postgres -h localhost -F c -d $DB_NAME -f $BACKUP_FILE

# Delete backups older than 7 days (Retention Policy)
find $BACKUP_DIR -name "${DB_NAME}_*.dump" -mtime +7 -delete

echo "Backup completed successfully: $BACKUP_FILE"
```

#### Step 3: Add to Crontab
Run every night at 2:00 AM:
```bash
# Open crontab editor
crontab -e

# Add cron rule:
0 2 * * * /bin/bash /path/to/backup.sh >> /var/log/pg_backup.log 2>&1
```

---

## Part 2: Database Performance Optimization

Database performance optimization is divided into 5 core pillars:

```text
               Database Performance Optimization
    ┌─────────────┬─────────────┬─────────────┬─────────────┐
    ▼             ▼             ▼             ▼             ▼
Query Tuning  Indexing Strategy  Schema Design  Memory Config  Maintenance
(EXPLAIN)      (B-Tree/GIN/Partial) (Data types) (work_mem)     (VACUUM/ANALYZE)
```

---

### Pillar 1: Query Tuning & Execution Plans (`EXPLAIN ANALYZE`)

Before optimizing any slow query, you must inspect **how PostgreSQL executes it**.

#### The `EXPLAIN (ANALYZE, BUFFERS)` Command:
- `EXPLAIN`: Shows the planned execution strategy generated by the query planner.
- `ANALYZE`: **Actually executes the query** and outputs real measured runtimes.
- `BUFFERS`: Displays how many memory blocks (pages) were read from cache vs. disk.

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM orders WHERE customer_id = 45000;
```

#### Key Execution Plan Scan Types to Look For:
1. **`Seq Scan` (Sequential Scan):** Reads all table rows one by one. Slow on large tables; fine on small tables.
2. **`Index Scan`:** Traverses an index and fetches corresponding rows from the table heap. Fast for fetching a small percentage of rows.
3. **`Index Only Scan`:** All requested columns are found directly inside the index. The database never touches the main table file! **(Fastest read possible)**.
4. **`Bitmap Index Scan / Bitmap Heap Scan`:** Combines index pointers into an in-memory bitmap before fetching rows from disk. Optimal when fetching moderate volumes of rows.

#### SARGable Queries (Search Argument Able):
Writing non-SARGable queries prevents PostgreSQL from using indexes:

```sql
-- ❌ BAD: Function wraps the indexed column (Forces a slow Seq Scan!)
SELECT * FROM users WHERE LOWER(email) = 'sara@example.com';
SELECT * FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2026;

-- ✅ GOOD: Expression index or clean range condition allows Index Scan!
-- Solution 1: Use an exact match or range
SELECT * FROM orders WHERE order_date >= '2026-01-01' AND order_date < '2027-01-01';

-- Solution 2: Create a functional/expression index for LOWER:
CREATE INDEX idx_users_lower_email ON users (LOWER(email));
```

#### Avoid `SELECT *`:
- `SELECT *` reads unnecessary columns, bloating network bandwidth and memory cache.
- Prevents PostgreSQL from utilizing **Index Only Scans**.

---

### Pillar 2: Strategic Indexing

#### 1. High Cardinality vs. Low Cardinality:
- **Index High-Cardinality Columns:** Columns with many distinct values (e.g., `user_id`, `email`, `order_number`).
- **Avoid Indexing Low-Cardinality Columns:** Columns with very few distinct values (e.g., `gender`, `is_active = true/false`). PostgreSQL will usually ignore indexes on these columns and use a `Seq Scan` anyway.

#### 2. Partial Indexes (Save Disk Space & Write Overhead):
If you only query active records or unread messages, index only those rows using a `WHERE` condition:

```sql
-- Creates an index ONLY for active users (much smaller and faster!)
CREATE INDEX idx_active_users ON users (email) WHERE is_active = true;

-- The planner uses this partial index for matching queries:
SELECT * FROM users WHERE email = 'test@example.com' AND is_active = true;
```

#### 3. Covering Indexes (`INCLUDE` Clause):
Enable **Index Only Scans** by bundling non-search columns into the index payload:

```sql
-- Store total_amount inside the index leaf nodes alongside customer_id
CREATE INDEX idx_orders_cust_inc_amount ON orders (customer_id) INCLUDE (total_amount);

-- This query reads ONLY the index; never touches the main orders table heap!
SELECT customer_id, total_amount FROM orders WHERE customer_id = 101;
```

#### 4. Always Index Foreign Key Columns:
PostgreSQL creates indexes automatically for `PRIMARY KEY` and `UNIQUE` constraints, but **does NOT automatically index `FOREIGN KEY` columns**. Always manually index foreign keys to prevent slow join lookups and full table locks during cascades:

```sql
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

---

### Pillar 3: Schema Design & Datatype Optimization

1. **Pick the Right Sized Integer:**
   - Use `INT` (4 bytes, up to 2.1 billion) for standard counts and foreign keys.
   - Use `BIGINT` (8 bytes) only for high-volume IDs (e.g., transaction IDs, sensor telemetry).
   - Use `SMALLINT` (2 bytes) for small lookup IDs (e.g., status codes, days of week).
2. **Text Fields:**
   - `TEXT` and `VARCHAR(n)` have identical performance in PostgreSQL. Use `VARCHAR(n)` when business validation is needed (e.g. state code `VARCHAR(2)`), and `TEXT` for open fields.
3. **Dates and Timestamps:**
   - Always prefer `TIMESTAMPTZ` (timestamp with time zone) over `TIMESTAMP`. It normalizes dates internally to UTC, preventing DST and timezone conversion bugs.

---

### Pillar 4: Server Memory Configuration (`postgresql.conf`)

PostgreSQL's default installation settings are intentionally very conservative to run on minimal hardware. For production servers, tune these core parameters in `postgresql.conf`:

| Parameter | Recommended Setting | Purpose |
| :--- | :--- | :--- |
| **`shared_buffers`** | **25% of total server RAM** | Primary database memory cache for reading/writing table and index pages. |
| **`work_mem`** | **16MB – 64MB** *(per operation)* | Memory allocated for in-memory sorting (`ORDER BY`, `DISTINCT`) and hash joins before spilling to slow temporary disk files. |
| **`maintenance_work_mem`** | **10% of RAM** (up to 1GB–2GB) | Memory used by maintenance tasks like `VACUUM`, `CREATE INDEX`, and `ALTER TABLE`. |
| **`effective_cache_size`** | **50% – 75% of total server RAM** | Guideline for the query planner estimating how much memory is available for caching in PostgreSQL + OS buffer cache combined. |
| **`wal_buffers`** | **16MB** | Buffer space in memory for WAL data before writing to disk. |

To check current settings:
```sql
SHOW shared_buffers;
SHOW work_mem;
SHOW maintenance_work_mem;
```

---

### Pillar 5: Routine Database Maintenance (Housekeeping)

#### 1. Why `VACUUM` is Essential (MVCC & Dead Tuples)
PostgreSQL uses **Multi-Version Concurrency Control (MVCC)**:
- When you `UPDATE` a row, PostgreSQL does **not** overwrite the old row. It writes a **new version** of the row and marks the old version as dead.
- When you `DELETE` a row, PostgreSQL merely marks it as dead.
- Over time, these dead rows accumulate into **Table Bloat**, wasting disk space and slowing down queries.

```sql
-- Standard VACUUM: Marks dead tuples as reusable space (Doesn't lock table)
VACUUM users;

-- VACUUM ANALYZE: Vacuums dead rows AND updates query planner statistics
VACUUM ANALYZE users;

-- VACUUM FULL: Reclaims physical disk space back to the OS by rewriting the table
-- ⚠️ CAUTION: Takes an EXCLUSIVE TABLE LOCK (Blocks all reads and writes!)
VACUUM FULL users;
```

#### 2. Tracking Dead Tuples & Bloat:
Inspect the ratio of live vs. dead rows across your tables:

```sql
SELECT 
    relname AS table_name,
    n_live_tup AS live_rows,
    n_dead_tup AS dead_rows,
    ROUND((n_dead_tup::numeric / NULLIF(n_live_tup + n_dead_tup, 0)) * 100, 2) AS dead_row_percentage,
    last_vacuum,
    last_autovacuum
FROM pg_stat_user_tables
ORDER BY dead_rows DESC;
```

#### 3. Rebuilding Bloated Indexes (`REINDEX`):
Over time, frequent `INSERT`, `UPDATE`, and `DELETE` operations bloat B-Tree index pages:

```sql
-- Rebuild a specific index without blocking reads or writes:
REINDEX INDEX CONCURRENTLY idx_users_email;

-- Rebuild all indexes on a table:
REINDEX TABLE CONCURRENTLY users;
```

#### 4. Monitoring Slow & Runaway Queries:
Find long-running queries currently executing on your database:

```sql
SELECT 
    pid,
    now() - pg_stat_activity.query_start AS duration,
    query,
    state,
    client_addr
FROM pg_stat_activity
WHERE state != 'idle' 
  AND (now() - pg_stat_activity.query_start) > interval '5 seconds'
ORDER BY duration DESC;
```

**Terminating a Stuck or Runaway Query:**
```sql
-- Gracefully cancel a running query (sends SIGINT):
SELECT pg_cancel_backend(<pid>);

-- Force terminate connection if query doesn't stop (sends SIGTERM):
SELECT pg_terminate_backend(<pid>);
```

---

## Part 3: Quick Revision Summary & Command Cheat Sheet

```bash
# ---------------- BACKUP CHEAT SHEET ----------------
# Plain SQL Backup
pg_dump -U postgres -d sales -f backup.sql

# Production Compressed Custom Backup
pg_dump -U postgres -F c -d sales -f backup.dump

# Entire PostgreSQL Cluster (All DBs + Users)
pg_dumpall -U postgres -f full_cluster.sql

# ---------------- RESTORE CHEAT SHEET ---------------
# Restore Plain SQL file
psql -U postgres -d target_db -f backup.sql

# Restore Custom Backup with 4 parallel threads
pg_restore -U postgres -d target_db -j 4 -v backup.dump

# Restore ONLY one table from backup
pg_restore -U postgres -d target_db -t customers -v backup.dump
```

```sql
-- ------------- PERFORMANCE & MAINTENANCE CHEAT SHEET -------------
-- 1. Inspect execution plan and memory buffers
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM orders WHERE customer_id = 1;

-- 2. Routine vacuum and stats update
VACUUM ANALYZE table_name;

-- 3. Rebuild bloated index concurrently
REINDEX TABLE CONCURRENTLY table_name;

-- 4. Check dead rows (table bloat)
SELECT relname, n_live_tup, n_dead_tup FROM pg_stat_user_tables;

-- 5. Terminate slow runaway query by PID
SELECT pg_terminate_backend(12345);
```