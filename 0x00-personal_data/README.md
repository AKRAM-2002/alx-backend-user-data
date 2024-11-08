# 0x00. Personal Data

## Overview
This project focuses on handling personal data securely in a backend application. It involves implementing authentication, logging, and data filtering to protect Personally Identifiable Information (PII). Key skills covered include regex, logging, encryption, and secure database connections.

## Project Timeline
* **Start Date**: Nov 6, 2024, 4:00 AM
* **End Date**: Nov 8, 2024, 4:00 AM
* **QA Review**: Request manual QA upon completion; auto-review is launched at the deadline.

## Learning Objectives
By the end of this project, you should understand:
* Examples of PII and non-PII data
* How to implement a log filter to obfuscate PII fields
* Password encryption and validation
* Database authentication using environment variables

## Requirements
* Python 3.7 on Ubuntu 18.04 LTS
* Code should be compliant with `pycodestyle` (v2.5)
* Include documentation for all modules, classes, and functions
* Use type annotations for all functions
* Create a `README.md` file at the project root

## Tasks

### 1. Regex-ing (filter_datum)
Create a function `filter_datum` that obfuscates specific fields in a log message using regex.
* **Parameters**: `fields` (list), `redaction` (string), `message` (string), `separator` (string)
* **Expected Output**: Sensitive fields are replaced by the `redaction` string.

Example:
```python
filter_datum(["password", "date_of_birth"], "xxx", "name=Bob;password=secret;date_of_birth=01/01/1990;", ";")
```

### 2. Log Formatter (RedactingFormatter)
* Create a `RedactingFormatter` class extending `logging.Formatter`
* The `format` method should use `filter_datum` to obfuscate specified fields in log messages

### 3. Create Logger (get_logger)
* Define a `get_logger` function returning a `Logger` object named `user_data`
* Add a `StreamHandler` with a `RedactingFormatter` to filter PII
* Define `PII_FIELDS` containing the sensitive fields to obfuscate

### 4. Secure Database Connection (get_db)
* Create a `get_db` function to connect securely to a MySQL database
* Use environment variables for the database credentials (`PERSONAL_DATA_DB_*`)

### 5. Read and Filter Data (main)
* Implement a `main` function to read and filter data from a database
* Retrieve all rows from the `users` table and print filtered log messages using `RedactingFormatter`