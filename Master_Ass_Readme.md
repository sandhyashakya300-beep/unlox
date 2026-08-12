Python Fundamentals + NumPy Foundation --- Interview Calibrated

A structured Python practice project built as a Jupyter Notebook tostrengthen Python fundamentals, problem-solving, programming logic,and NumPy foundations through interview-style questions and codingexercises.

📌 Project Overview

This repository contains the notebook masterAssignment.ipynb,which combines:

Python theory and conceptual questions

Output prediction exercises

Practical coding problems

String and collection manipulation

Mathematical and logical problem solving

Input validation and edge-case handling

Basic NumPy concepts

The notebook is organized to move from fundamentals → outputprediction → hands-on coding practice.

📚 Topics Covered

1. Python Fundamentals

The project covers important Python concepts such as:

== vs is

Mutable vs immutable data types

Floating-point precision

Lists vs tuples

Dictionary lookup and time complexity

range() vs numpy.arange()

append(), extend(), and insert()

Extended iterable unpacking

/, //, %, and **

Python memory and object behavior

NumPy performance fundamentals

2. Output Prediction

The notebook includes exercises involving:

Nested list creation

List references and copying behavior

x = x + [...] vs x += [...]

Loop-variable behavior

String and integer operations

Boolean short-circuit evaluation

These problems are useful for understanding how Python actually executescode rather than only memorizing syntax.

3. Coding Practice

The coding section contains practical programs including:

Swapping two numbers using multiple techniques

Swiggy-style order and GST calculation

Temperature conversion

Sum of digits without string conversion

Smart input type detection

Indian income tax slab calculation

Indian PAN format validation without regex

Bengaluru BESCOM electricity bill calculation

Cricket strike-rate classification

BMI calculation using Indian BMI ranges

Number and character patterns

Pascal's Triangle

Armstrong numbers

Fibonacci series and sum

Prime-number checking and prime sum

Number palindrome checking

HCF and LCM using the Euclidean algorithm

Single-pass string analysis

Student marks analysis

Word-frequency analysis

Indian states and capitals CRUD operations

Set operations

Stock-price analysis

Duplicate and unique number detection

Smart sentence palindrome checking

Manual title casing

Caesar Cipher encryption

GST calculation using a reusable function

🧠 Skills Demonstrated

This project demonstrates practical understanding of:

Python syntax and control flow

Conditional statements

for and while loops

Functions

Exception handling

Strings

Lists

Tuples

Sets

Dictionaries

Mathematical operations

Input validation

Algorithmic thinking

Time-complexity concepts

Basic data processing

Pattern generation

Financial calculations

String algorithms

Problem decomposition

🛠️ Technologies Used

Python 3

Jupyter Notebook

NumPy concepts and exercises

No external datasets are required for the exercises contained in thenotebook.

📂 Project Structure

Python-Fundamentals-NumPy/
│
├── masterAssignment.ipynb
└── README.md

▶️ How to Run

Option 1 --- Jupyter Notebook

Install Jupyter Notebook if required:

pip install notebook

Start Jupyter:

jupyter notebook

Then open:

masterAssignment.ipynb

Option 2 --- VS Code

Open the project folder in VS Code.

Install the Python extension.

Install the Jupyter extension.

Open masterAssignment.ipynb.

Select a Python kernel.

Run the cells individually or use Run All.

💡 Example Problems

Swiggy Order Calculator

The notebook calculates:

Subtotal = Price × Quantity
GST = 18% of Subtotal
Delivery = ₹40 when subtotal < ₹500
Delivery = FREE when subtotal >= ₹500

Cricket Strike Rate

Strike Rate = (Runs / Balls) × 100

The result is classified into:

Explosive

Aggressive

Steady

Defensive

The program also handles the balls = 0 edge case.

GST Calculator

A reusable function is implemented:

calculate_gst(amount, gst_rate=18, gst_inclusive=False)

It returns:

(base_amount, gst_amount, total_amount)

and supports both GST-inclusive and GST-exclusive amounts.

🎯 Learning Objectives

The main objective of this project is to build a strong foundation inPython by solving problems that require both conceptual understandingand implementation.

By completing these exercises, you can practice:

Writing clean Python logic

Understanding Python behavior

Handling edge cases

Working with built-in data structures

Breaking larger problems into smaller steps

Improving problem-solving skills for interviews and codingassessments

📈 Future Improvements

Possible improvements for this repository include:

Add the remaining assignment questions if applicable

Separate theory and coding exercises into individual notebooks

Add automated test cases

Add expected-output examples

Refactor repeated logic into reusable functions

Add a dedicated NumPy practical section

Add beginner-friendly explanations for each solution

Add unit testing with pytest

👩‍💻 Author

Sandhya Shakya

BTech Computer Engineering Student

Interested in:

Python

Data Science

Machine Learning

Data Analytics

Problem Solving

Artificial Intelligence

⭐ Support

If you find this project useful for learning Python or interviewpreparation, consider giving the repository a star ⭐ and sharingfeedback.
