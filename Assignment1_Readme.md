Assignment 1: Python and NumPy Fundamentals

📌 Project Overview

This repository contains Assignment 1: Python and NumPy
Fundamentals, completed as a Jupyter Notebook.

The assignment is divided into three sections:

Section A --- Theory Questions: Python fundamentals, data types,
operators, conditionals, functions, loops, NumPy, slicing,
range(), and palindrome logic.

Section B --- Coding Questions: Practical Python programs
covering conditionals, functions, loops, palindrome checking, NumPy
array operations, star patterns, and list slicing.

Section C --- Brainstorming and Research Questions: Loop design,
NumPy efficiency, modularity, conditional limitations, and
programming logic.

🛠️ Technologies Used

Python 3.13.4

Jupyter Notebook

NumPy

🗂️ Project Structure

.
├── Assignment1.ipynb
└── README.md

📚 Section A --- Theory Questions

Python Fundamentals

The assignment covers Python's simple syntax, library ecosystem,
community support, and integration capabilities.

Mutable vs Immutable Data Types

The notebook explains mutable objects such as lists and dictionaries and
immutable objects such as strings, integers, and tuples. It also
compares lists and tuples.

Python Operators

Four operator categories are discussed:

Arithmetic

Assignment

Comparison

Logical

Conditional Statements

The notebook explains if, elif, and else statements and gives a
streaming-quality example based on internet speed.

Functions

Functions are presented as reusable blocks of code. The assignment
discusses code reuse, modularity, maintenance, and debugging.

For and While Loops

The notebook explains using for loops for known iteration patterns and
while loops when repetition depends on a condition.

NumPy Basics

The assignment explains why NumPy is useful for numerical operations,
focusing on efficient array storage and vectorized operations.

Slicing

Python list slicing and NumPy array slicing are introduced using the
form:

[start:stop:step]

range() Function

The notebook explains:

range(start, stop, step)

with examples such as:

range(4)
range(5, 10)
range(2, 11, 2)

Palindrome Logic

The assignment explains the idea of reversing a string or number and
comparing it with the original value.

💻 Section B --- Coding Questions

1. Sign Checker

Accepts a number and identifies whether it is positive, negative, or
zero.

Example:

-3
The number is negative.

2. Statistics Function

cal_stats() accepts a list and returns its sum and average.

Example:

[11, 22, 33, 12, 13, 10, 24]

Output:

sum: 125
Average: 17.857142857142858

3. First N Even Numbers

Uses a for loop and range() to generate the first n even numbers.

For n = 10:

0
2
4
6
8
10
12
14
16
18

4. Manual Palindrome Checker

Builds a reversed string manually using a loop instead of a built-in
reverse function.

Example:

wow
'wow' is a palindrome.

5. NumPy Array Operations

Creates:

arr = np.array([12, 11, 13, 14, 15, 66])

and demonstrates:

arr.max()
arr.min()
arr.sum()

Output:

original array: [12 11 13 14 15 66]
Max value: 66
Min value: 11
Sum of all elements: 131

6. Star Pattern

Uses nested loops to print:

*****
*****
*****
*****
*****

7. List Slicing

Uses:

og_list[::2]

to extract alternate elements.

Example:

original list: [12, 13, 44, 11, 22, 43]
sliced list : [12, 44, 22]

🧠 Section C --- Brainstorming and Research

The final section explores:

Why programming languages provide both for and while loops

How NumPy handles numerical data efficiently

Problems caused by avoiding functions in large programs

Why conditionals alone cannot solve every programming problem

Why logical problem solving is more important than memorizing syntax

🎯 Learning Objectives

This assignment provides practice with:

Python fundamentals

Data types

Lists and tuples

Operators

Conditional statements

Functions

Loops

range()

String manipulation

Palindrome logic

List slicing

NumPy arrays

Array aggregation

Nested loops

Programming problem solving

🚀 How to Run

1. Clone the repository

git clone <your-repository-url>
cd <your-repository-folder>

2. Install dependencies

pip install notebook numpy

3. Start Jupyter Notebook

jupyter notebook

Open Assignment1.ipynb and run the cells.

📦 Requirements

Python 3.x
Jupyter Notebook
NumPy

Optional requirements.txt:

numpy
notebook

📝 Notes

Some coding cells use input() and therefore require interactive input
when executed.

The notebook combines written explanations with executable Python
examples and NumPy exercises.

👩‍💻 Author

Sandhya Shakya

⭐ Conclusion

Assignment 1: Python and NumPy Fundamentals provides hands-on
practice with core Python programming concepts and introductory NumPy
operations. It establishes a foundation for further work in Python
programming, data analysis, and numerical computing.
