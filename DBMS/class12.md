# PostgreSQL User Management, Roles & Access Control (DCL)

User management is a critical aspect of database administration. It ensures that only authorized users can connect to the database, access specific tables, and execute designated operations (such as reading, inserting, updating, or deleting data).

In SQL, user management and permission handling is governed by **Data Control Language (DCL)**, primarily using the `GRANT` and `REVOKE` statements.

---

## 1. Core Concepts: Roles vs. Users

In PostgreSQL, **users** and **groups** are unified under a single concept called a **Role**:

- **Role:** An entity that can own database objects and hold access privileges.
- **User:** A role that has the `LOGIN` privilege enabled (allowing it to connect as a database client).
- **Group:** A role created without `LOGIN` (used to bundle multiple users together for permission management).

> **Note:** In PostgreSQL:
> ```sql
> CREATE USER john WITH PASSWORD 'pass123';
> ```
> is identical to:
> ```sql
> CREATE ROLE john WITH LOGIN PASSWORD 'pass123';
> ```

---

## 2. Common Role Attributes

When creating or modifying roles, you can assign specific flags and privileges:

| Attribute | Opposite | Description |
| :--- | :--- | :--- |
| `LOGIN` | `NOLOGIN` | Determines whether the role can log in and establish a database connection. |
| `SUPERUSER` | `NOSUPERUSER` | Grants unrestricted, root-like powers over the database cluster (bypasses all permission checks). |
| `CREATEDB` | `NOCREATEDB` | Allows the role to create new databases. |
| `CREATEROLE` | `NOCREATEROLE` | Allows the role to create, modify, and drop other roles. |
| `INHERIT` | `NOINHERIT` | Allows the role to automatically inherit privileges from parent group roles. (Default is `INHERIT`). |
| `PASSWORD 'secret'` | | Sets an encrypted password for database authentication. |
| `VALID UNTIL 'timestamp'` | | Sets an expiration date and time for the user's password/account. |

---

## 3. User Hierarchy in Organizations

In enterprise applications, users are categorized into tiers according to the **Principle of Least Privilege (PoLP)**:

```text
    ┌─────────────────────────────────────────────────────────┐
    │  1. Super Admin (SUPERUSER)                             │
    │     Full cluster control, system maintenance            │
    └───────────────────────────┬─────────────────────────────┘
                                │
    ┌───────────────────────────▼─────────────────────────────┐
    │  2. Database Admin (CREATEDB, CREATEROLE, NOLOGIN)      │
    │     Manages schemas, databases, and users               │
    └───────────────────────────┬─────────────────────────────┘
                                │
    ┌───────────────────────────▼─────────────────────────────┐
    │  3. Power User / Developer (LOGIN)                      │
    │     Read & write access (SELECT, INSERT, UPDATE, DELETE)│
    └───────────────────────────┬─────────────────────────────┘
                                │
    ┌───────────────────────────▼─────────────────────────────┐
    │  4. Normal / Read-Only User (LOGIN)                     │
    │     Read-only access (SELECT only, no modifications)    │
    └─────────────────────────────────────────────────────────┘
```

---

## 4. Understanding PostgreSQL Permission Hierarchy (The 3 Keys)

In PostgreSQL, permissions work like a 3-door security checkpoint. For a user to read a table, they must be granted 3 permissions in order:

```text
  Door 1: CONNECT on DATABASE  ──▶  Door 2: USAGE on SCHEMA  ──▶  Door 3: SELECT on TABLE
```

1. **Database Level:** Permission to connect to the database (`GRANT CONNECT ON DATABASE`).
2. **Schema Level:** Permission to look inside the schema (`GRANT USAGE ON SCHEMA public`).
3. **Table Level:** Permission to perform operations on the table (`GRANT SELECT, INSERT ON TABLE`).

If any of these 3 keys is missing, the query will fail with `permission denied`.

---

## 5. Hands-On Practical Lab

Let's go step-by-step through a complete, production-grade practical scenario.

### Step 1: Database & Sample Schema Setup

Log in as the default administrative user (`postgres`):

```sql
-- 1. Create a practice company database
CREATE DATABASE company_db;

-- 2. Connect to company_db
\c company_db

-- 3. Create sample tables
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL
);

CREATE TABLE audit_logs (
    log_id SERIAL PRIMARY KEY,
    action_description TEXT NOT NULL,
    performed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Insert sample data
INSERT INTO employees (full_name, department, salary) VALUES
('Sara Ahmed', 'Engineering', 95000.00),
('Omer Ali', 'Data Science', 88000.00),
('Rahul Sharma', 'Marketing', 62000.00),
('Priya Reddy', 'Finance', 74000.00);

-- 5. Verify records
SELECT * FROM employees;
```

---

### Step 2: Creating Users with Different Roles

Now let's create our four types of users with secure passwords:

```sql
-- 1. Super Admin: Has full cluster authority
CREATE ROLE super_admin WITH LOGIN PASSWORD 'SuperAdmin123' SUPERUSER CREATEDB CREATEROLE;

-- 2. Database Admin: Can manage DBs and roles, but not superuser
CREATE ROLE db_admin WITH LOGIN PASSWORD 'AdminPass123' CREATEDB CREATEROLE;

-- 3. Power User (Backend App / Developer): Can read and modify data
CREATE ROLE power_user WITH LOGIN PASSWORD 'PowerDev123';

-- 4. Read-Only User (Data Analyst / Reporting): Can only view data
CREATE ROLE analyst_user WITH LOGIN PASSWORD 'Analyst123';

-- 5. Intern User (Restricted access, temporary account expiring in 2026)
CREATE ROLE intern_user WITH LOGIN PASSWORD 'Intern123' VALID UNTIL '2026-12-31 23:59:59';
```

---

### Step 3: Granting Permissions (`GRANT`)

#### A. Granting Permissions to `power_user` (Read + Write)

The `power_user` needs to connect to the database, use the `public` schema, and execute `SELECT`, `INSERT`, `UPDATE`, and `DELETE`:

```sql
-- 1. Allow connecting to company_db
GRANT CONNECT ON DATABASE company_db TO power_user;

-- 2. Allow viewing objects in the public schema
GRANT USAGE ON SCHEMA public TO power_user;

-- 3. Grant Read and Write privileges on all existing tables
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO power_user;

-- 4. Grant permission on auto-increment sequence IDs (Required for INSERT!)
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO power_user;
```

> **Why grant on SEQUENCES?**  
> When a table uses `SERIAL` or `IDENTITY` columns, inserting a new row requires updating the internal counter sequence. Without sequence permissions, an `INSERT` statement will fail!

---

#### B. Granting Permissions to `analyst_user` (Read-Only)

The analyst should only be allowed to view records, never modify or delete them:

```sql
-- 1. Allow connection
GRANT CONNECT ON DATABASE company_db TO analyst_user;

-- 2. Allow schema lookup
GRANT USAGE ON SCHEMA public TO analyst_user;

-- 3. Grant SELECT ONLY
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analyst_user;
```

---

#### C. Granting Column-Level Permissions (Sensitive Data Protection)

Suppose the `intern_user` is allowed to see employee names and departments, but **must not see employee salaries**:

```sql
-- 1. Allow connection and schema usage
GRANT CONNECT ON DATABASE company_db TO intern_user;
GRANT USAGE ON SCHEMA public TO intern_user;

-- 2. Grant SELECT only on specific columns
GRANT SELECT (emp_id, full_name, department) ON employees TO intern_user;
```

Now, if `intern_user` queries:
- `SELECT emp_id, full_name FROM employees;` $\rightarrow$ **Success!**
- `SELECT salary FROM employees;` $\rightarrow$ **Permission denied for column salary!**

---

#### D. Automatically Granting Permissions on Future Tables

By default, permissions granted on `ALL TABLES` only apply to tables that **already exist**. To ensure future tables automatically receive permissions:

```sql
-- Future tables created in schema public will automatically allow power_user to read and write
ALTER DEFAULT PRIVILEGES IN SCHEMA public 
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO power_user;

-- Future tables will automatically allow analyst_user to read
ALTER DEFAULT PRIVILEGES IN SCHEMA public 
GRANT SELECT ON TABLES TO analyst_user;
```

---

### Step 4: Role-Based Access Control (RBAC) Using Groups

Instead of granting permissions to 50 individual users one by one, enterprise systems create a **Group Role** (with `NOLOGIN`), grant permissions to the group, and assign users to the group.

```sql
-- 1. Create a Group Role without login permission
CREATE ROLE dev_team NOLOGIN;

-- 2. Grant permissions to the group
GRANT CONNECT ON DATABASE company_db TO dev_team;
GRANT USAGE ON SCHEMA public TO dev_team;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO dev_team;

-- 3. Create individual developers
CREATE ROLE dev_omar WITH LOGIN PASSWORD 'OmarPass1';
CREATE ROLE dev_sara WITH LOGIN PASSWORD 'SaraPass2';

-- 4. Assign developers into the group
GRANT dev_team TO dev_omar;
GRANT dev_team TO dev_sara;
```

> Because `dev_team` has `INHERIT` by default, `dev_omar` and `dev_sara` automatically inherit all permissions granted to `dev_team`.

---

### Step 5: User Management Operations (`ALTER ROLE / USER`)

Administrators frequently need to update passwords, change permissions, or lock accounts.

#### 1. Changing a User's Password:
```sql
ALTER ROLE power_user WITH PASSWORD 'NewSecurePass2026!';
```

#### 2. Locking / Disabling a User Account:
Prevent a user from logging in without deleting their account:
```sql
-- Lock account (cannot log in)
ALTER ROLE intern_user WITH NOLOGIN;

-- Unlock account (allow login again)
ALTER ROLE intern_user WITH LOGIN;
```

#### 3. Modifying User Privileges:
```sql
-- Give db_admin permission to create databases
ALTER ROLE db_admin WITH CREATEDB;

-- Revoke superuser rights from an account
ALTER ROLE db_admin WITH NOSUPERUSER;
```

#### 4. Setting or Extending Account Expiration:
```sql
-- Set password to expire on a specific date
ALTER ROLE intern_user VALID UNTIL '2026-06-30 18:00:00';

-- Remove expiration (valid indefinitely)
ALTER ROLE intern_user VALID UNTIL 'infinity';
```

#### 5. Renaming a User:
```sql
ALTER ROLE analyst_user RENAME TO reporting_user;
```

---

### Step 6: Revoking Permissions (`REVOKE`)

When a user changes roles or a security policy changes, use `REVOKE` to withdraw privileges.

#### A. Revoke Specific Operations:
Revoke `DELETE` permission from `power_user` so they cannot permanently erase records:
```sql
REVOKE DELETE ON ALL TABLES IN SCHEMA public FROM power_user;
```

#### B. Revoke Table-Level Access:
Remove all permissions on `audit_logs` from `power_user`:
```sql
REVOKE ALL PRIVILEGES ON TABLE audit_logs FROM power_user;
```

#### C. Revoke Database Connection:
Prevent a user from connecting to the database:
```sql
REVOKE CONNECT ON DATABASE company_db FROM intern_user;
```

#### D. Revoke Group Membership:
Remove a developer from the group:
```sql
REVOKE dev_team FROM dev_omar;
```

---

### Step 7: How to Safely Drop a User (`DROP ROLE / DROP USER`)

If you attempt to run `DROP ROLE power_user;` while the user owns objects or has granted permissions, PostgreSQL will throw an error:
```text
ERROR: role "power_user" cannot be dropped because some objects depend on it
```

#### The Safe 3-Step Procedure to Drop a User:

```sql
-- Step 1: Reassign any objects owned by power_user to the postgres superuser
REASSIGN OWNED BY power_user TO postgres;

-- Step 2: Drop all privileges and dependencies granted to power_user
DROP OWNED BY power_user;

-- Step 3: Safely drop the role
DROP ROLE power_user;
```

---

## 6. Inspecting Users and Permissions

You can check existing roles and permissions using `psql` meta-commands or SQL queries:

### Useful `psql` Shortcut Commands:
- `\du` — List all roles, their attributes (Superuser, Create DB), and group memberships.
- `\du+` — List all roles with descriptions.
- `\l` — List all databases and access privileges.
- `\dp <table_name>` or `\z <table_name>` — View table-level access permissions.

### Inspecting via SQL Queries:
```sql
-- 1. View all database users and their attributes
SELECT rolname, rolsuper, rolcreaterole, rolcreatedb, rolcanlogin 
FROM pg_roles;

-- 2. View table privileges granted in public schema
SELECT grantee, table_name, privilege_type 
FROM information_schema.role_table_grants 
WHERE table_schema = 'public' 
ORDER BY table_name, grantee;
```

---

## 7. Security Best Practices Checklist

1. **Principle of Least Privilege:** Never give `SUPERUSER` or `CREATEDB` to application users.
2. **Never connect apps as `postgres`:** Create a dedicated application user (e.g., `app_backend`) with only necessary CRUD privileges.
3. **Use Group Roles (RBAC):** Manage permissions by department or team groups, not individual user accounts.
4. **Always Protect Sequences:** Always run `GRANT USAGE ON ALL SEQUENCES` when granting `INSERT` rights.
5. **Set Password Expiry:** Use `VALID UNTIL` for interns, contractors, and temporary team members.
6. **Column-Level Restriction:** Restrict sensitive columns (passwords, salary, SSN) using column-level `GRANT SELECT (col1, col2)`.

---

## 8. Quick Revision Summary & Cheat Sheet

```sql
-- 1. Create a user
CREATE ROLE <username> WITH LOGIN PASSWORD '<password>';

-- 2. Grant access (3 keys)
GRANT CONNECT ON DATABASE <dbname> TO <username>;
GRANT USAGE ON SCHEMA public TO <username>;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO <username>;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO <username>;

-- 3. Revoke access
REVOKE DELETE ON ALL TABLES IN SCHEMA public FROM <username>;
REVOKE CONNECT ON DATABASE <dbname> FROM <username>;

-- 4. Alter user
ALTER ROLE <username> WITH PASSWORD '<new_password>';
ALTER ROLE <username> WITH NOLOGIN;  -- Lock account
ALTER ROLE <username> WITH LOGIN;    -- Unlock account

-- 5. Drop user safely
REASSIGN OWNED BY <username> TO postgres;
DROP OWNED BY <username>;
DROP ROLE <username>;
```