# Database Management Systems (DBMS) - Class 1

## What is a Database?
A database is an organized collection of digital information stored electronically in a computer system.

### Core Concepts
* **Data**: Raw facts or numbers that the database stores.
* **DBMS (Database Management System)**: The software program used to create, manage, secure, and access the database (such as MySQL or PostgreSQL).
* **CRUD**: The four basic operations performed on data: Create, Read, Update, and Delete.

---

## Types of Databases
Databases are organized collections of data stored electronically, categorized primarily by how they structure, store, and manage information.

### Main Types of Databases
1. **Relational Databases (SQL)**: Store data in structured tables with rows and columns, using SQL for querying. Examples include MySQL and PostgreSQL. Best for financial and inventory systems.
2. **NoSQL Databases (Non-Relational)**: Handle flexible, semi-structured, or unstructured data without fixed table schemas. Sub-types include:
   * **Document stores** (e.g., MongoDB)
   * **Key-value stores** (e.g., Redis)
   * **Column-family stores** (e.g., Apache Cassandra)

---

## What is an RDBMS?
An RDBMS (Relational Database Management System) is a software program used to store, organize, and manage data in a structured, tabular format consisting of rows and columns.

### Core Concepts
* **Tables**: Data is saved in flat, structured grids where columns represent attributes (fields) and rows represent individual records (tuples).


Absolutely. If you're setting up PostgreSQL for development, don't overcomplicate it. **Use the native package manager/official installer for each OS**, not a source build. PostgreSQL's own documentation recommends binary packages/installers for normal users. ([PostgreSQL][1])

As of August 2026, **PostgreSQL 18 is the current major release**, with 18.6 available. ([PostgreSQL][2])

# PostgreSQL Installation Guide

![Image](https://images.openai.com/static-rsc-4/pGCmA1G8ClC9-Qg5lBDT0rx5MnuKawCLADp9f-BohhaKhjq2DcpCw3n--Shb7QjDeSJK2hb7IAtiW3uYczkvP3QOu0xvdsx1mkBuF83SNrMyLK4Bcv4ajGIxKYdh3vi8CeL1Q_Ca9m0zbFFKfrYEZHNiALxvIhcJK3EwPbJ_gP2zV-z_PFKaVTrxcQx2IDkm?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/vlgNo_6zbipidf7bNU6uc_V0OuGYxaaej7XtjD5vXRQBceZy44NeJGYrXS4u8hkxcbpIoeRCTkpA2qzwhRnH6gEBcoSMgLgVfqrZC0jZnAxOMeuGkPO85g0SoZeSt4E4epZ3OmJF7YhuDDrYIgNt5fwJSQ1MiBcybg82XvDwJoVV_dDbXUSY2m6sH5RS60Rt?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/9fX3oWZZO6HqFhzahuZYd8F5q6GZN1mPnlN3wnLc67vXEW-7Jw2I5lg9qLPU_e1PnLA4rnDTZ6KY3QlsYKX8sG4KJyH7m10D_SMZLWbu7_pFCW9fORioaOG1NfgnQGQ0c_LBceGSGjcnQ362EHq_S8Xga7_Ib-PvCxsug0crTR2AF6OMZS7DO8U9qQq-hJQO?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/FE5_fhQ-2d4ZyyKfRA9N68L-5mOF7ApCAVctBso1CxcXDocOzvMZcPH9wc80ULpRQvj6C_rqWgj8BDkoOsf4fQ0bZkJfSoJis6j8hXM76dVL0Us0Qdq09RhFjW6gNAYpc_TV3mkIKaqdNVoo4fTSy0bHlpxp9KGFVpmCi954yWDVjPUSu3vI3u_1q0a3-zEJ?purpose=fullsize)

We'll cover:

1. 🍎 macOS
2. 🐧 Ubuntu Linux
3. 🪟 Windows
4. ✅ Verify installation
5. 🔑 Important PostgreSQL commands
6. 🗄️ Create your first database
7. 🧱 Create your first table
8. 🌐 PostgreSQL + pgAdmin
9. 📌 Connection information to remember
10. ⚡ Quick cheat sheet

---

# 1. 🍎 PostgreSQL on macOS

For macOS, I recommend **Homebrew** if you're a developer.

PostgreSQL officially supports installation through Homebrew, Postgres.app, and the EDB installer. ([PostgreSQL][3])

## Step 1 — Check Homebrew

Open Terminal:

```bash
brew --version
```

If you get something like:

```text
Homebrew 4.x.x
```

you're good.

If Homebrew isn't installed, install it from:

[Homebrew official website](https://brew.sh/?utm_source=chatgpt.com)

---

## Step 2 — Install PostgreSQL

```bash
brew update
brew install postgresql@18
```

Check:

```bash
psql --version
```

You should see something similar to:

```text
psql (PostgreSQL) 18.x
```

---

## Step 3 — Start PostgreSQL

```bash
brew services start postgresql@18
```

Check:

```bash
brew services list
```

You should see PostgreSQL running.

---

## Step 4 — Add PostgreSQL to PATH

Depending on your Homebrew setup, `psql` may not automatically be available.

Check:

```bash
which psql
```

If it doesn't find it:

### Apple Silicon Mac

For M1/M2/M3/M4:

```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@18/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Intel Mac

```bash
echo 'export PATH="/usr/local/opt/postgresql@18/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Then:

```bash
psql --version
```

---

## Step 5 — Connect

Try:

```bash
psql postgres
```

You may get:

```text
psql (18.x)
Type "help" for help.

postgres=#
```

Congratulations. PostgreSQL is running.

Exit:

```sql
\q
```

---

# 2. 🐧 PostgreSQL on Ubuntu

Ubuntu already includes PostgreSQL packages by default. PostgreSQL also maintains its own APT repository if you need a specific supported version. ([PostgreSQL][4])

For a normal college/development project, start with the Ubuntu package:

## Step 1 — Update packages

```bash
sudo apt update
```

## Step 2 — Install PostgreSQL

```bash
sudo apt install postgresql
```

PostgreSQL's official Ubuntu instructions use this installation method. ([PostgreSQL][4])

---

## Step 3 — Check version

```bash
psql --version
```

Example:

```text
psql (PostgreSQL) 16.x
```

The exact version depends on your Ubuntu release/package repositories.

---

## Step 4 — Check PostgreSQL service

```bash
sudo systemctl status postgresql
```

You want:

```text
Active: active (exited)
```

or a running PostgreSQL cluster/service depending on your Ubuntu packaging.

Start it if necessary:

```bash
sudo systemctl start postgresql
```

Enable it at boot:

```bash
sudo systemctl enable postgresql
```

---

## Step 5 — Switch to PostgreSQL user

Ubuntu typically creates a Linux user called `postgres`.

```bash
sudo -u postgres -i
```

Then:

```bash
psql
```

You'll get:

```text
postgres=#
```

Exit PostgreSQL:

```sql
\q
```

Exit the `postgres` Linux user:

```bash
exit
```

---

## Installing PostgreSQL 18 specifically on Ubuntu

If you specifically want PostgreSQL 18 instead of Ubuntu's default version, use the official PostgreSQL APT repository.

The official instructions currently support Ubuntu **22.04, 24.04, and 26.04 LTS**. ([PostgreSQL][4])

Run:

```bash
sudo apt install -y postgresql-common
```

Then:

```bash
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
```

Then:

```bash
sudo apt update
```

Install PostgreSQL 18:

```bash
sudo apt install postgresql-18
```

Verify:

```bash
psql --version
```

The PostgreSQL project documents this PGDG repository method officially. ([PostgreSQL][4])

---

# 3. 🪟 PostgreSQL on Windows

For Windows, don't mess around with compiling PostgreSQL.

Use the official PostgreSQL download page and the **EDB installer**. The official PostgreSQL site provides Windows installers through EDB, including PostgreSQL and pgAdmin. ([PostgreSQL][2])

[PostgreSQL Windows Downloads](https://www.postgresql.org/download/windows/?utm_source=chatgpt.com)

## Step 1 — Download installer

Go to the PostgreSQL Windows download page.

Download the Windows installer.

Choose the current stable PostgreSQL version, e.g.:

```text
PostgreSQL 18.x
```

---

## Step 2 — Run installer

The installer will ask which components you want.

You'll typically see:

```text
☑ PostgreSQL Server
☑ pgAdmin 4
☑ Stack Builder
☑ Command Line Tools
```

For development, keep:

```text
PostgreSQL Server
pgAdmin 4
Command Line Tools
```

Stack Builder is optional.

---

## Step 3 — Choose installation directory

Default is usually something similar to:

```text
C:\Program Files\PostgreSQL\18
```

Keep the default unless you have a reason to change it.

---

## Step 4 — Choose data directory

You'll see something like:

```text
C:\Program Files\PostgreSQL\18\data
```

Keep the default.

---

## Step 5 — Set PostgreSQL password

You'll be asked for a password for the PostgreSQL superuser:

```text
postgres
```

For example:

```text
Username: postgres
Password: ********
```

**Don't forget this password.**

You'll need it when connecting from applications.

---

## Step 6 — Port

Default:

```text
5432
```

Keep:

```text
5432
```

unless another PostgreSQL instance is already using it.

The standard PostgreSQL connection looks like:

```text
localhost:5432
```

---

## Step 7 — Locale

Usually:

```text
Default locale
```

is fine.

Click through the installer and complete installation.

---

## Step 8 — Verify Windows installation

Open:

```text
Command Prompt
```

or PowerShell.

Run:

```powershell
psql --version
```

If you get:

```text
psql is not recognized...
```

then PostgreSQL's `bin` directory isn't in your PATH.

Usually it is:

```text
C:\Program Files\PostgreSQL\18\bin
```

Add that directory to your Windows PATH.

Then restart your terminal and run:

```powershell
psql --version
```

---

# 4. Verify PostgreSQL on all systems

Once installed, run:

```bash
psql --version
```

Then connect:

```bash
psql -U postgres
```

Depending on the OS, you may be asked for a password.

If successful:

```text
psql (18.x)
Type "help" for help.

postgres=#
```

You're done.

---

# 5. Important PostgreSQL commands

Once you're inside:

```text
postgres=#
```

these commands are extremely useful.

### List databases

```sql
\l
```

### List users

```sql
\du
```

### Connect to a database

```sql
\c database_name
```

### List tables

```sql
\dt
```

### Describe a table

```sql
\d table_name
```

### Quit

```sql
\q
```

---

# 6. Create your first database

Inside PostgreSQL:

```sql
CREATE DATABASE myproject;
```

Check:

```sql
\l
```

Connect:

```sql
\c myproject
```

You should see:

```text
You are now connected to database "myproject".
```

---

# 7. Create your first table

Now:

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100)
);
```

Insert data:

```sql
INSERT INTO students (name, age, department)
VALUES
('Omer', 21, 'Computer Science'),
('Rahul', 22, 'Information Technology');
```

Check:

```sql
SELECT * FROM students;
```

Result:

```text
 id | name  | age |    department
----+-------+-----+-------------------
  1 | Omer  | 21  | Computer Science
  2 | Rahul | 22  | Information Technology
```

---

# 8. PostgreSQL + pgAdmin

If you don't want to use the terminal all the time, use **pgAdmin**.

The EDB installers for macOS and Windows include pgAdmin, while on Ubuntu you can install/use it separately. ([PostgreSQL][3])

pgAdmin gives you a GUI where you can manage:

```text
Servers
 └── PostgreSQL
      ├── Databases
      │    └── myproject
      │         ├── Schemas
      │         ├── Tables
      │         ├── Views
      │         └── Functions
      │
      └── Login/Group Roles
```

For learning SQL, though, **don't become dependent on pgAdmin**.

Learn:

```bash
psql
```

and SQL first.

---

# 9. Connection information you should remember

For local development, your configuration normally looks like:

```text
Host:     localhost
Port:     5432
Database: myproject
Username: postgres
Password: your_password
```

For example, a connection URL:

```text
postgresql://postgres:password@localhost:5432/myproject
```

You'll use this later with:
* **Python** (Django, FastAPI)
* **Node.js** (Express, NestJS)
* **Java** (Spring Boot)
* **Containers** (Docker, Kubernetes)

---

# 10. Quick cheat sheet

| OS                 | Recommended installation |
| ------------------ | ------------------------ |
| 🍎 macOS           | Homebrew                 |
| 🐧 Ubuntu          | `apt`                    |
| 🪟 Windows         | EDB Installer            |
| GUI                | pgAdmin                  |
| CLI                | `psql`                   |
| Default port       | `5432`                   |
| Default admin user | `postgres`               |

### macOS

```bash
brew install postgresql@18
brew services start postgresql@18
psql --version
psql postgres
```

### Ubuntu

```bash
sudo apt update
sudo apt install postgresql
sudo systemctl status postgresql
psql --version
```

### Windows

```powershell
psql --version
psql -U postgres
```

---

[1]: https://www.postgresql.org/docs/current/install-binaries.html?utm_source=chatgpt.com "PostgreSQL: Documentation: 18: Chapter 16. Installation from Binaries"
[2]: https://www.postgresql.org/download/?utm_source=chatgpt.com "PostgreSQL: Downloads"
[3]: https://www.postgresql.org/download/macosx/?from=20423&from_column=20423&utm_source=chatgpt.com "PostgreSQL: macOS packages"
[4]: https://www.postgresql.org/download/linux/ubuntu/?utm_source=chatgpt.com "PostgreSQL: Linux downloads (Ubuntu)"
