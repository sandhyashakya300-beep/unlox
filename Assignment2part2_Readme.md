Assignment 2 – Part 2: SQL & MySQL Database Fundamentals

📌 Overview

This repository contains Part 2 of Assignment 2, focused on fundamental concepts of SQL, MySQL, and relational database management.

The assignment consists of 10 conceptual questions covering important database topics such as primary keys, SQL commands, normalization, foreign keys, relationships, data types, NULL values, joins, and constraints.

This work is designed to build a strong foundation in relational database concepts and MySQL database design.

🎯 Objectives

The main objectives of this assignment are to:

Understand the purpose and characteristics of Primary Keys.

Differentiate between DDL and DML in SQL.

Understand database normalization and data redundancy.

Learn how Foreign Keys maintain referential integrity.

Understand One-to-Many relationships.

Identify the characteristics of a relational database.

Understand the importance of choosing appropriate data types.

Distinguish NULL values from 0 and empty strings.

Understand the purpose of INNER JOIN and LEFT JOIN.

Learn how UNIQUE and NOT NULL constraints improve data quality.

📚 Topics Covered

1. Primary Keys

A Primary Key uniquely identifies each record in a database table.

The assignment discusses three important characteristics of a Primary Key:

Uniqueness – Every value must be unique.

NOT NULL – A Primary Key cannot contain missing values.

Immutability – Values should rarely change over time.

Primary Keys make it easier to reliably identify, retrieve, and update individual records.

2. DDL vs DML

The assignment explains the difference between two major categories of SQL commands.

Category

Purpose

Example

DDL (Data Definition Language)

Defines, changes, or removes database structures

CREATE TABLE

DML (Data Manipulation Language)

Manages and modifies data stored in tables

INSERT INTO

DDL focuses mainly on the database structure, while DML works with the data inside that structure.

3. Database Normalization

Normalization organizes database information logically and aims to reduce unnecessary duplication.

The assignment explains data redundancy as storing the same information in multiple places.

Excessive redundancy can:

Waste storage space.

Create inconsistent information.

Cause update anomalies.

Make database maintenance more difficult.

4. Foreign Keys & Referential Integrity

A Foreign Key creates a relationship between tables by referencing a key in another table.

It helps maintain referential integrity by ensuring that referenced values correspond to valid records in the related table.

For example:

Authors
   |
   | Author_ID
   ↓
Books

The Author_ID in the Books table can reference the corresponding ID in the Authors table.

5. One-to-Many Relationships

The assignment uses an Author–Books example:

One author can write many books.

Each book has one author.

Therefore, the Foreign Key belongs on the many side of the relationship.

Example:

Authors
----------------
Author_ID (PK)
Name

        1
        |
        | 
        | 
        ∞
Books
----------------
Book_ID (PK)
Title
Author_ID (FK)

This design avoids storing multiple book IDs in a single author record.

6. Relational Databases

A database is considered relational when information is organized into related tables connected through common fields or keys.

Instead of keeping all information in one large, repetitive spreadsheet, a relational database can separate information into logical tables such as:

Customers

Products

Orders

These tables can then be connected using keys and relationships.

7. Data Types

The assignment highlights the importance of selecting appropriate data types such as:

INT

VARCHAR

DECIMAL

Correct data types help maintain:

Data accuracy

Appropriate storage usage

Correct database operations

The assignment also explains why storing a phone number as an INT can be problematic. Leading zeros can be lost, and standard integer types may not be suitable for values containing country codes or formatting characters.

8. NULL Values

In MySQL, NULL represents missing, unknown, or inapplicable data.

It is different from:

0       → A numerical value
""      → An empty string
NULL    → Absence of a value

Understanding this distinction is important when designing tables and writing SQL queries.

9. SQL Joins

The assignment explains why databases separate information into multiple tables and later combine it using JOINs.

INNER JOIN

Returns only records that have matching values in both tables.

SELECT *
FROM table1
INNER JOIN table2
ON table1.id = table2.id;

LEFT JOIN

Returns all records from the left table and matching records from the right table. If there is no match, the right-side columns contain NULL.

SELECT *
FROM table1
LEFT JOIN table2
ON table1.id = table2.id;

10. Database Constraints

Constraints are rules applied to database columns to help prevent invalid or unreliable data.

The assignment focuses on:

UNIQUE

Ensures that values in a column are distinct.

Example:

email VARCHAR(255) UNIQUE

This can help prevent duplicate email addresses.

NOT NULL

Requires a column to contain a value.

Example:

username VARCHAR(100) NOT NULL

Together, these constraints improve data quality, accuracy, and reliability.

🛠️ Technologies & Concepts

MySQL

SQL

Relational Database Management Systems (RDBMS)

Database Design

Primary Keys

Foreign Keys

Normalization

Referential Integrity

SQL Joins

Database Constraints

Data Types

📂 Project Structure

Assignment2part2/
│
├── Assignment2part2.ipynb
└── README.md

The Jupyter Notebook contains the complete assignment questions and their corresponding answers.

🎓 Key Learning Outcomes

After completing this assignment, the learner gains an understanding of:

How Primary Keys identify records.

The difference between DDL and DML.

Why normalization is important.

How Foreign Keys connect tables.

How One-to-Many relationships are designed.

What makes a database relational.

Why appropriate data types matter.

How NULL differs from 0 and empty strings.

How INNER JOIN and LEFT JOIN work.

How constraints help maintain database quality.

💡 Conclusion

This assignment provides a conceptual foundation for working with SQL and MySQL relational databases. The topics covered are essential for understanding database design, writing effective SQL queries, maintaining data integrity, and building reliable database-driven applications.

It serves as a useful starting point for progressing toward more advanced topics such as complex SQL queries, aggregate functions, subqueries, indexing, transactions, stored procedures, and database optimization.

👩‍💻 Author

Sandhya Shakya

Computer Engineering Student | BTech

Interested in Python, SQL, Data Analytics, Machine Learning, and Software Development.

⭐ Repository

If you find this assignment useful for learning SQL and database fundamentals, feel free to explore the repository and use it as a reference for your own learning journey.
