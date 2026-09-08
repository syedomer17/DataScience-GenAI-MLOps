# PostgreSQL Transactions & ACID Properties

A **Transaction** is a fundamental concept in database management. It ensures that data remains reliable, accurate, and protected against system crashes, network failures, and concurrent user modifications.

---

## 1. What is a Transaction?

A **Transaction** is a group of one or more SQL operations executed together as a **single, indivisible unit of work**.

### The Rule of a Transaction:
> **Either all operations succeed, or none of them happen.**

### The Classic Real-World Scenario: Bank Fund Transfer
Imagine **Alice** wants to transfer **₹2,000** to **Bob**.

This single transfer actually requires multiple database steps:
1. Check if Alice has at least ₹2,000.
2. Deduct ₹2,000 from Alice's account.
3. Add ₹2,000 to Bob's account.
4. Record the transfer receipt in a transaction history table.

```text
               Bank Transfer: Alice → Bob (₹2,000)
    ┌────────────────────────────────────────────────────────┐
    │  Step 1: Deduct ₹2,000 from Alice (Balance: ₹8,000)   │
    │  Step 2: Add ₹2,000 to Bob       (Balance: ₹7,000)   │
    └────────────────────────────────────────────────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
      Both Succeed                          Any Step Fails
         COMMIT                                ROLLBACK
  (Changes saved permanently)             (All changes undone)
```

If the database or power crashes after **Step 1** but before **Step 2**:
- Alice's money would be gone.
- Bob would never receive the money.

Without a transaction, this causes severe data corruption. With a database transaction, PostgreSQL guarantees that if step 2 fails, step 1 is automatically **rolled back (undone)**.

---

## 2. The ACID Properties Explained

Every relational database management system (RDBMS) like PostgreSQL adheres to **ACID** properties:

| Letter | Property | Simple Meaning | Real-Life Bank Analogy |
| :---: | :--- | :--- | :--- |
| **A** | **Atomicity** | **All or Nothing** | Money is deducted from Alice **AND** added to Bob. If Bob doesn't get it, Alice gets her money back. |
| **C** | **Consistency** | **Preserve All Rules** | Account balance cannot become negative if a `CHECK (balance >= 0)` constraint exists. |
| **I** | **Isolation** | **Transactions Don't Interfere** | If Alice sends money while Charlie also sends money to Bob, both transfers process safely without overriding each other. |
| **D** | **Durability** | **Once Committed, It Stays** | Once the screen says "Transfer Successful", the data is permanently saved to disk, even if the power goes out a second later. |

---

### Deep Dive into Each Property

#### 1. Atomicity (All or Nothing) 🧩
A transaction cannot be partially completed. 
- If 5 statements are inside a transaction and 4 succeed but the 5th fails, **all 5 statements are undone**.
- Handled by: `COMMIT` (save everything) or `ROLLBACK` (undo everything).

#### 2. Consistency (Rules & Invariants Intact) ✅
The database moves from one valid state to another valid state:
- All constraints (Primary Key, Foreign Key, `CHECK`, `NOT NULL`, `UNIQUE`) must remain satisfied before and after the transaction.
- If any rule is broken during the transaction, the entire transaction is cancelled.

#### 3. Isolation (Independent Execution) 🔒
Even if thousands of users execute queries at the exact same moment:
- Each user feels like they are the only person using the database.
- Uncommitted changes made by User 1 are hidden from User 2 to prevent reading "dirty" or temporary data.

#### 4. Durability (Permanent Storage) 💾
Once a transaction is committed:
- The changes are permanently recorded in non-volatile memory / disk storage.
- PostgreSQL achieves this using the **WAL (Write-Ahead Logging)** mechanism. If the server abruptly loses power, PostgreSQL recovers the committed data upon restart by replaying the log.

---

## 3. Transaction Control Language (TCL) Commands

PostgreSQL provides specific commands to control transactions:

| Command | Description |
| :--- | :--- |
| `BEGIN` or `START TRANSACTION` | Starts a new transaction block. |
| `COMMIT` | Saves all changes made in the transaction permanently. |
| `ROLLBACK` | Discards and undoes all changes made in the transaction. |
| `SAVEPOINT <name>` | Sets a checkpoint within a transaction to allow partial rollbacks. |
| `ROLLBACK TO <name>` | Reverts changes back to a specific checkpoint without cancelling the whole transaction. |
| `RELEASE SAVEPOINT <name>` | Removes an established savepoint. |

---

## 4. Hands-On Practical Lab

Let's implement complete, step-by-step practical examples in PostgreSQL.

### Step 1: Create Database & Setup Schema

Open your terminal or `psql` and run:

```sql
-- 1. Create a practice database
CREATE DATABASE bank_db;

-- 2. Connect to the practice database
\c bank_db

-- 3. Create the accounts table with a balance constraint
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    holder_name VARCHAR(50) NOT NULL,
    balance NUMERIC(12, 2) NOT NULL CHECK (balance >= 0)
);

-- 4. Insert initial sample accounts
INSERT INTO accounts (holder_name, balance) VALUES
('Alice', 10000.00),
('Bob', 5000.00),
('Charlie', 1500.00);

-- 5. Verify initial records
SELECT * FROM accounts;
```

**Initial Data:**
| account_id | holder_name | balance |
| :---: | :--- | :---: |
| 1 | Alice | 10000.00 |
| 2 | Bob | 5000.00 |
| 3 | Charlie | 1500.00 |

---

### Practical 1: Successful Transaction (`BEGIN` & `COMMIT`)

Let's simulate a successful transfer of **₹2,000** from Alice (id 1) to Bob (id 2).

```sql
-- Step 1: Start the transaction
BEGIN;

-- Step 2: Deduct ₹2,000 from Alice
UPDATE accounts 
SET balance = balance - 2000.00 
WHERE account_id = 1;

-- Step 3: Add ₹2,000 to Bob
UPDATE accounts 
SET balance = balance + 2000.00 
WHERE account_id = 2;

-- Step 4: Save all changes permanently
COMMIT;
```

**Verify the Result:**
```sql
SELECT * FROM accounts;
```

**Output:**
- Alice: `8000.00` (₹2,000 deducted)
- Bob: `7000.00` (₹2,000 added)
- Charlie: `1500.00` (untouched)

Both updates succeeded together!

---

### Practical 2: Atomicity in Action (`ROLLBACK`)

What happens if an error occurs mid-way or the user cancels the transfer?

Let's simulate Alice attempting to send **₹3,000** to Bob, but an issue occurs before Bob's balance can be updated:

```sql
-- Step 1: Start the transaction
BEGIN;

-- Step 2: Deduct ₹3,000 from Alice
UPDATE accounts 
SET balance = balance - 3000.00 
WHERE account_id = 1;

-- At this moment inside the transaction, Alice's balance appears as 5000.00.
-- But imagine an application error, network cutoff, or user cancellation happens here:

-- Step 3: Rollback the transaction
ROLLBACK;
```

**Verify the Result:**
```sql
SELECT * FROM accounts WHERE account_id = 1;
```

**Output:**
- Alice's balance is **still 8000.00**!
- The ₹3,000 deduction was completely erased as if it never happened. This is **Atomicity (All or Nothing)**.

---

### Practical 3: Consistency via Constraints (Automatic Abort)

What happens if a transaction violates a business rule, such as overdrafting an account?

Our table has `CHECK (balance >= 0)`. Let's test what happens if Charlie (balance = 1500.00) tries to transfer **₹5,000** to Bob:

```sql
BEGIN;

-- Try to deduct ₹5,000 from Charlie (who only has ₹1,500)
UPDATE accounts 
SET balance = balance - 5000.00 
WHERE account_id = 3;
```

**PostgreSQL Console Output:**
```text
ERROR: new row for relation "accounts" violates check constraint "accounts_balance_check"
DETAIL: Failing row contains (3, Charlie, -3500.00).
```

Now, even if you try to `COMMIT`:
```sql
COMMIT;
```

**PostgreSQL Response:**
```text
ROLLBACK
```

> **Why did PostgreSQL output `ROLLBACK`?**  
> Because once a constraint is broken inside a transaction block, PostgreSQL flags the transaction as **aborted**. It will automatically reject any subsequent `COMMIT` and rollback the entire unit to protect database **Consistency**.

---

### Practical 4: Partial Rollbacks Using `SAVEPOINT`

Sometimes you have a long, multi-step transaction and you don't want to discard everything if just one optional sub-task fails. You can use **`SAVEPOINT`** as a checkpoint.

#### Scenario:
Alice wants to:
1. Pay Bob ₹500 (Mandatory bill).
2. Pay Charlie ₹10,000 (Risky / optional operation that might fail).

```sql
-- Step 1: Start transaction
BEGIN;

-- Step 2: Pay Bob ₹500
UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 2;

-- Step 3: Create a checkpoint
SAVEPOINT bill_paid;

-- Step 4: Attempt a risky transfer to Charlie that violates balance constraint
UPDATE accounts SET balance = balance - 100000.00 WHERE account_id = 1;
-- ERROR: violates check constraint!

-- Step 5: Rollback ONLY to the checkpoint
ROLLBACK TO bill_paid;

-- Step 6: Commit the valid portion
COMMIT;
```

**Verify the Result:**
```sql
SELECT * FROM accounts;
```

**Output:**
- Alice: `7500.00` (Deducted ₹500 for Bob, but the ₹100,000 failed attempt was undone).
- Bob: `7500.00` (Received ₹500).
- Charlie: `1500.00` (Unchanged).

The payment to Bob was saved, while the failed operation was safely reverted!

---

### Practical 5: Isolation & Concurrency Control

To see **Isolation** with your own eyes, open **two separate terminal windows** (Session 1 and Session 2) connected to `bank_db`.

```text
Session 1 (Terminal A)                 Session 2 (Terminal B)
---------------------                 ---------------------
\c bank_db                            \c bank_db
```

#### Step-by-Step Test:

1. **In Session 1:** Start a transaction and update Alice's balance, but **do not commit yet**:
   ```sql
   -- Session 1
   BEGIN;
   UPDATE accounts SET balance = 9999.00 WHERE account_id = 1;
   ```

2. **In Session 2:** Check Alice's balance immediately:
   ```sql
   -- Session 2
   SELECT balance FROM accounts WHERE account_id = 1;
   ```
   > **Result:** Session 2 still sees **`7500.00`**!  
   > It **cannot** see the uncommitted value `9999.00`. This prevents "Dirty Reads" and keeps transactions isolated.

3. **In Session 1:** Now commit the transaction:
   ```sql
   -- Session 1
   COMMIT;
   ```

4. **In Session 2:** Check Alice's balance again:
   ```sql
   -- Session 2
   SELECT balance FROM accounts WHERE account_id = 1;
   ```
   > **Result:** Now Session 2 sees the updated balance **`9999.00`**!

---

### Practical 6: Row-Level Locking (`SELECT ... FOR UPDATE`)

When multiple users try to withdraw or modify the same row at the exact same moment (Race Condition), use `FOR UPDATE` to lock that specific row until the transaction finishes.

```sql
BEGIN;

-- Lock Alice's row exclusively for this transaction
SELECT * FROM accounts 
WHERE account_id = 1 
FOR UPDATE;

-- Perform calculation safely
UPDATE accounts 
SET balance = balance - 1000.00 
WHERE account_id = 1;

COMMIT;
```

> While Alice's row is locked by `FOR UPDATE`, any other transaction trying to modify or lock Alice's row will **wait** until this transaction finishes `COMMIT` or `ROLLBACK`.

---

## 5. PostgreSQL Transaction Isolation Levels

PostgreSQL provides different levels of isolation depending on your application's strictness requirements:

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Serialization Anomaly |
| :--- | :---: | :---: | :---: | :---: |
| **Read Committed** *(Default)* | ❌ Not possible | Allowed | Allowed | Allowed |
| **Repeatable Read** | ❌ Not possible | ❌ Not possible | Allowed (Prevented in PG) | Allowed |
| **Serializable** *(Strict)* | ❌ Not possible | ❌ Not possible | ❌ Not possible | ❌ Not possible |

> **Definitions:**
> - **Dirty Read:** Reading data that has been modified by another transaction but not yet committed.
> - **Non-Repeatable Read:** Re-reading the same row within a transaction and finding that another committed transaction changed its values.
> - **Phantom Read:** Re-running a query with a `WHERE` range condition and finding new rows inserted by another committed transaction.

### How to Set Isolation Level in PostgreSQL:

```sql
-- Set isolation level for the current transaction
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Or set it for the entire session
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

## 6. Durability: How PostgreSQL Guarantees Permanent Data

PostgreSQL ensures Durability using **WAL (Write-Ahead Logging)**:
1. When changes occur, PostgreSQL writes the change records to a sequential log file on disk (WAL) **before** modifying the actual table data blocks.
2. Even if power cuts out during a write to the table files, on startup PostgreSQL reads the WAL log and replays all committed transactions.

You can inspect WAL settings in PostgreSQL:
```sql
-- Check current WAL level
SHOW wal_level;

-- Check if PostgreSQL is currently in crash recovery mode
SELECT pg_is_in_recovery();
```

---

## 7. Quick Revision Summary & Cheat Sheet

```sql
-- 1. Standard Transaction Template
BEGIN;
    -- SQL Operation 1
    UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
    -- SQL Operation 2
    UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT; -- Or ROLLBACK; if anything goes wrong

-- 2. Checkpoints Template
BEGIN;
    INSERT INTO accounts (holder_name, balance) VALUES ('Test', 1000);
    SAVEPOINT sp1;
    
    DELETE FROM accounts WHERE account_id = 1; -- Risky/Mistake
    ROLLBACK TO sp1; -- Reverts only the DELETE statement
COMMIT; -- Saves the INSERT
```

### Memory Aid for Exams and Interviews:
- **A (Atomicity):** All or Nothing (`COMMIT` / `ROLLBACK`).
- **C (Consistency):** Obey all schema constraints (`CHECK`, `FOREIGN KEY`, `NOT NULL`).
- **I (Isolation):** Transactions execute independently without seeing intermediate dirty states.
- **D (Durability):** Committed data survives crashes and power outages via WAL.
