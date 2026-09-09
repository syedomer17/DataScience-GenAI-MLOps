# PostgreSQL JSON & JSONB: Semi-Structured Data, Operators & Indexing

PostgreSQL is renowned for being an **object-relational database**. One of its greatest strengths is native support for semi-structured **JSON** (JavaScript Object Notation) data alongside traditional relational tables. This allows developers to combine the speed, consistency, and ACID guarantees of a relational database with the flexibility of a document database (like MongoDB).

---

## 1. What is JSON vs. JSONB in PostgreSQL?

PostgreSQL offers two native data types for storing JSON data: **`json`** and **`jsonb`**.

| Feature | `json` (Plain Text) | `jsonb` (Binary / Decomposed) |
| :--- | :--- | :--- |
| **Storage Format** | Stored as an exact textual copy of the input string. | Parsed and stored in a specialized decomposed binary format. |
| **Whitespace & Formatting** | Preserves original whitespace, indentation, and newlines. | Strips unnecessary whitespace for compact binary storage. |
| **Key Ordering** | Preserves original order of keys in JSON objects. | Reorders keys internally for fast binary searching. |
| **Duplicate Keys** | Keeps duplicate keys as written in the text. | Keeps only the **last** duplicate key value. |
| **Write / Insert Speed** | **Faster** (No conversion or validation parsing overhead). | Slightly slower (Must validate, decompose, and index keys on insert). |
| **Read / Query Speed** | **Slower** (Must re-parse the raw text on every query). | **Significantly Faster** (Direct binary traversal without re-parsing). |
| **Indexing Support** | Only functional / expression B-Tree indexes. | **Full GIN Indexing support** for fast path and key lookups. |
| **Recommended Usage** | Raw audit log payloads where exact text layout matters. | **Standard choice for almost all real-world applications.** |

> **Best Practice Rule:**  
> Always use **`jsonb`** unless you have a specialized requirement to preserve the exact raw text formatting or duplicate keys.

---

## 2. JSON / JSONB Operator Reference

PostgreSQL provides a rich set of operators for querying, navigating, and modifying JSONB objects and arrays:

### Extraction Operators:
| Operator | Right-Hand Argument | Return Type | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| **`->`** | Key name (`text`) or Array Index (`int`) | **`jsonb`** | Extracts JSON object field or array element **as JSON/JSONB**. | `data -> 'address'` |
| **`->>`** | Key name (`text`) or Array Index (`int`) | **`text`** | Extracts JSON object field or array element **as plain TEXT**. | `data ->> 'email'` |
| **`#>`** | Path array (`text[]`) | **`jsonb`** | Extracts nested JSON object at specified path **as JSONB**. | `data #> '{user, address}'` |
| **`#>>`** | Path array (`text[]`) | **`text`** | Extracts nested JSON object at specified path **as plain TEXT**. | `data #>> '{user, email}'` |

> **Crucial Difference: `->` vs `->>`**
> - Use `->` when you want to continue chaining JSON operators (returns `jsonb`).
> - Use `->>` when you want to compare values in `WHERE`, `ORDER BY`, or display plain text (returns `text`).

---

### Existence & Containment Operators (JSONB only):
| Operator | Right-Hand Argument | Return Type | Description |
| :--- | :--- | :---: | :--- |
| **`@>`** | `jsonb` | `boolean` | **Contains**: Does the left JSONB contain the right JSONB structure? |
| **`<@`** | `jsonb` | `boolean` | **Contained by**: Is the left JSONB contained inside the right JSONB? |
| **`?`** | `text` | `boolean` | **Key Exists**: Does the specified string key exist at the top level? |
| **`?\|`** | `text[]` | `boolean` | **Any Key Exists**: Do *any* of the specified keys exist? |
| **`?&`** | `text[]` | `boolean` | **All Keys Exist**: Do *all* of the specified keys exist? |

---

### Modification Operators:
| Operator | Right-Hand Argument | Description | Example |
| :--- | :--- | :--- | :--- |
| **`\|\|`** | `jsonb` | Concatenates / merges two JSONB objects or arrays. | `data \|\| '{"tier": "gold"}'::jsonb` |
| **`-`** | `text` or `int` | Deletes a key from an object or an element from an array by index. | `data - 'language'` or `data - 0` |
| **`#-`** | `text[]` | Deletes a field or array element at a nested path. | `data #- '{hobbies, 1}'` |

---

## 3. Hands-On Practical Setup

Let's build a realistic e-commerce database with customers storing dynamic preferences, tags, and settings in a `JSONB` column.

```sql
-- Step 1: Create practice database
CREATE DATABASE ecommerce_db;

-- Step 2: Connect to the database
\c ecommerce_db

-- Step 3: Create customers table with a JSONB column
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    preferences JSONB DEFAULT '{}'::jsonb
);

-- Step 4: Insert sample records with nested JSONB data
INSERT INTO customers (first_name, last_name, email, preferences) VALUES
('Sara', 'Ahmed', 'sara.ahmed@example.com', '{
    "language": "Hindi",
    "theme": "dark",
    "newsletter": true,
    "hobbies": ["reading", "coding"],
    "address": {
        "city": "Hyderabad",
        "pincode": "500001"
    }
}'::jsonb),

('Omer', 'Ali', 'omer.ali@example.com', '{
    "language": "English",
    "theme": "light",
    "newsletter": false,
    "hobbies": ["gym", "coding", "gaming"],
    "address": {
        "city": "Bengaluru",
        "pincode": "560001"
    }
}'::jsonb),

('Rahul', 'Sharma', 'rahul.sharma@example.com', '{
    "language": "Hindi",
    "theme": "dark",
    "newsletter": true,
    "hobbies": ["photography", "travel"],
    "address": {
        "city": "Mumbai",
        "pincode": "400001"
    }
}'::jsonb),

('Priya', 'Reddy', 'priya.reddy@example.com', '{
    "language": "Telugu",
    "theme": "system",
    "newsletter": false,
    "hobbies": ["music"],
    "address": {
        "city": "Hyderabad",
        "pincode": "500081"
    }
}'::jsonb);

-- Step 5: Verify table contents
SELECT * FROM customers;
```

---

## 4. Querying & Extracting JSONB Data

### Practical 1: Extracting Fields as JSON vs. Text (`->` vs `->>`)

```sql
SELECT 
    first_name,
    -- -> returns jsonb (notice double quotes around value in output: "Hindi")
    preferences -> 'language' AS lang_json,
    -- ->> returns text (clean text without quotes: Hindi)
    preferences ->> 'language' AS lang_text
FROM customers;
```

### Practical 2: Extracting Array Elements by Index

JSON arrays are **0-indexed** in PostgreSQL:

```sql
SELECT 
    first_name,
    -- First hobby (index 0)
    preferences -> 'hobbies' ->> 0 AS first_hobby,
    -- Second hobby (index 1)
    preferences -> 'hobbies' ->> 1 AS second_hobby
FROM customers;
```

### Practical 3: Navigating Deeply Nested Objects (`#>` and `#>>`)

Use path arrays to extract nested fields in one clean operation:

```sql
SELECT 
    first_name,
    -- Extract nested city using path
    preferences #>> '{address, city}' AS city,
    -- Extract nested pincode using path
    preferences #>> '{address, pincode}' AS pincode
FROM customers;
```

### Practical 4: Filtering Rows in `WHERE` Clauses

Always use `->>` (text extraction) when comparing with standard SQL strings or numbers:

```sql
-- Filter by top-level text field
SELECT first_name, email 
FROM customers 
WHERE preferences ->> 'language' = 'Hindi';

-- Filter by nested object field
SELECT first_name, email, preferences #>> '{address, city}' AS city
FROM customers 
WHERE preferences #>> '{address, city}' = 'Hyderabad';

-- Filter boolean value (cast to boolean)
SELECT first_name, email 
FROM customers 
WHERE (preferences ->> 'newsletter')::boolean = true;
```

---

## 5. Containment & Existence Testing (`@>`, `?`, `?|`, `?&`)

These operators are among the fastest operations in PostgreSQL because they directly leverage GIN indexes.

### Practical 5: The `@>` (Contains) Operator
Find all customers who prefer **Hindi** and **dark theme**:

```sql
SELECT first_name, email 
FROM customers 
WHERE preferences @> '{"language": "Hindi", "theme": "dark"}';
```

Check if a JSON array contains a specific item (e.g., customers whose hobbies include `"coding"`):

```sql
SELECT first_name, email, preferences -> 'hobbies' AS hobbies
FROM customers 
WHERE preferences -> 'hobbies' @> '["coding"]'::jsonb;
```

### Practical 6: Key Existence (`?`, `?|`, `?&`)

```sql
-- Check if the 'theme' key exists at the top level
SELECT first_name 
FROM customers 
WHERE preferences ? 'theme';

-- Check if EITHER 'newsletter' OR 'loyalty_points' exists
SELECT first_name 
FROM customers 
WHERE preferences ?| array['newsletter', 'loyalty_points'];

-- Check if BOTH 'language' AND 'address' exist
SELECT first_name 
FROM customers 
WHERE preferences ?& array['language', 'address'];
```

---

## 6. Modifying & Updating JSONB Data

### Practical 7: Merging New Keys with `||` (Concatenation)
Add or overwrite fields without disturbing existing keys:

```sql
-- Add 'loyalty_member': true to Omer's preferences
UPDATE customers 
SET preferences = preferences || '{"loyalty_member": true, "tier": "Gold"}'::jsonb 
WHERE customer_id = 2;

-- Verify update
SELECT first_name, preferences FROM customers WHERE customer_id = 2;
```

### Practical 8: Updating Nested Fields with `jsonb_set`

**Syntax:**
```sql
jsonb_set(target_column, '{path, keys}', new_value_as_jsonb, create_if_missing)
```

Change Omer's language to `"French"`:
```sql
UPDATE customers 
SET preferences = jsonb_set(preferences, '{language}', '"French"'::jsonb) 
WHERE customer_id = 2;
```

Update a nested address property:
```sql
-- Change Sara's city to 'New Delhi'
UPDATE customers 
SET preferences = jsonb_set(preferences, '{address, city}', '"New Delhi"'::jsonb) 
WHERE customer_id = 1;
```

### Practical 9: Deleting Keys with `-` and `#-`

```sql
-- 1. Remove the 'theme' key from Sara's preferences
UPDATE customers 
SET preferences = preferences - 'theme' 
WHERE customer_id = 1;

-- 2. Remove the second hobby (index 1) from Omer's hobbies array
UPDATE customers 
SET preferences = preferences #- '{hobbies, 1}' 
WHERE customer_id = 2;
```

---

## 7. Transforming JSONB: Expanding & Aggregating

PostgreSQL provides powerful functions to convert JSON into tabular rows and vice versa:

### Practical 10: Unnesting Arrays with `jsonb_array_elements_text()`
Convert a JSON array of hobbies into separate relational rows:

```sql
SELECT 
    first_name,
    jsonb_array_elements_text(preferences -> 'hobbies') AS individual_hobby
FROM customers;
```

**Output:**
| first_name | individual_hobby |
| :--- | :--- |
| Sara | reading |
| Sara | coding |
| Omer | gym |
| Omer | gaming |
| Rahul | photography |
| Rahul | travel |
| Priya | music |

### Practical 11: Unnesting Key-Value Pairs with `jsonb_each_text()`

```sql
SELECT 
    first_name,
    key AS attribute_name,
    value AS attribute_value
FROM customers,
LATERAL jsonb_each_text(preferences)
WHERE customer_id = 1;
```

### Practical 12: Aggregating Relational Rows into JSON (`jsonb_agg` & `jsonb_build_object`)

Convert relational rows directly into a structured JSON payload for API responses:

```sql
SELECT jsonb_pretty(
    jsonb_agg(
        jsonb_build_object(
            'id', customer_id,
            'name', first_name || ' ' || last_name,
            'email', email,
            'city', preferences #>> '{address, city}'
        )
    )
) AS customer_api_payload
FROM customers;
```

---

## 8. Indexing JSONB for High Performance

Querying large JSONB columns without indexes leads to slow **Sequential Scans (`Seq Scan`)**. PostgreSQL provides two indexing strategies for JSONB:

### Strategy 1: GIN Index (Generalized Inverted Index)

A GIN index indexes all keys and values inside the JSONB document.

```sql
-- Default GIN index (Supports @>, ?, ?|, ?& operators)
CREATE INDEX idx_customers_preferences_gin ON customers USING GIN (preferences);

-- Path Ops GIN Index (Supports ONLY @>, but is smaller and up to 3x faster)
CREATE INDEX idx_customers_preferences_path_ops ON customers USING GIN (preferences jsonb_path_ops);
```

#### Verifying Index Usage with `EXPLAIN ANALYZE`:
```sql
EXPLAIN (ANALYZE, BUFFERS) 
SELECT * FROM customers WHERE preferences @> '{"language": "Hindi"}';
-- Output: Bitmap Index Scan on idx_customers_preferences_gin
```

---

### Strategy 2: B-Tree Expression Index on a Specific Field

If you frequently query or sort by a specific JSON key using standard comparisons (`=`, `>`, `<`, `ORDER BY`), create a **B-Tree index on the extracted expression**:

```sql
-- Create B-Tree index on the extracted text field
CREATE INDEX idx_customers_pref_lang ON customers ((preferences ->> 'language'));

-- Now equality, range, and ORDER BY queries on language are instant!
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM customers WHERE (preferences ->> 'language') = 'Hindi';
-- Output: Index Scan using idx_customers_pref_lang
```

---

## 9. Quick Revision Summary & Cheat Sheet

```sql
-- 1. Extract values
col -> 'key'          -- Returns JSONB (with quotes)
col ->> 'key'         -- Returns TEXT (clean string)
col #>> '{path, key}' -- Returns nested value as TEXT

-- 2. Containment & Search
col @> '{"status": "active"}'::jsonb  -- Contains check
col ? 'key_name'                      -- Top-level key exists

-- 3. Modify JSONB
col || '{"new_key": 123}'::jsonb                    -- Merge / append
jsonb_set(col, '{address, city}', '"Delhi"'::jsonb) -- Update path
col - 'key_name'                                    -- Delete key

-- 4. Indexing
CREATE INDEX idx_gin ON table USING GIN (jsonb_col);                      -- General GIN
CREATE INDEX idx_btree ON table (((jsonb_col ->> 'key')));                -- Specific field B-Tree
```