Assignment 2: Logic Building with Python and NumPy

📌 Project Overview

This repository contains Assignment 2: Logic Building with Python and
NumPy, completed in a Jupyter Notebook.

The assignment focuses on strengthening Python problem-solving skills
through theory, practical programming exercises, and conceptual
questions about loops, slicing, functions, NumPy, and modular
programming.

The notebook is organized into:

Section A --- Theory Questions

Section B --- Coding Questions

Logic and Research Questions

🛠️ Technologies Used

Python 3

Jupyter Notebook

NumPy

🗂️ Project Structure

.
├── Assignment2.ipynb
└── README.md

📚 Section A --- Theory Questions

1. Flow of Execution

The assignment explains how Python normally executes code from top to
bottom and how functions, conditional statements, and loops change that
flow.

It covers:

Function definitions and function calls

if / elif / else decision paths

for and while loop repetition

Returning to the appropriate point after a function call

2. Importance of Data Types

The notebook explains why data types are important for interpreting and
processing values correctly.

It discusses how choosing an inappropriate data type can affect:

Program meaning

Operations performed on data

Precision

Program output

3. Role of Operators

Operators are discussed as the building blocks used to create
expressions for decision-making.

The assignment covers:

Relational operators: >, <, ==, !=

Logical operators: and, or, not

An automated banking/ATM example is used to demonstrate combining
conditions.

4. Internal Mechanics of for Loops and range()

The notebook explains how range() works with a for loop.

The discussion covers:

range() objects

Iterators

The current iteration state

Getting the next value

StopIteration when the sequence is exhausted

Example concept:

for i in range(3):
    print(i)

5. Efficiency Through Slicing

The assignment explains slicing using:

sequence[start:stop:step]

It identifies practical applications such as:

Data pagination

Reversing sequences

Selecting every nth element

Extracting portions of data

6. Loop Control Conditions

Loop conditions determine when a loop should continue and when it should
stop.

The notebook discusses problems caused by incorrect loop conditions,
including:

Infinite loops

Off-by-one errors

Premature termination

Incorrect or incomplete results

7. NumPy Arrays vs Python Lists

The assignment compares Python lists and NumPy arrays in terms of memory
and performance.

Python Lists

Store references to Python objects

Can contain heterogeneous data

Generally have more object-level overhead

NumPy Arrays

Store homogeneous numerical data

Use compact array storage

Support vectorized numerical operations

Are designed for efficient numerical computation

8. Problem Decomposition

The notebook explains why large problems should be divided into smaller
functions.

A sample e-commerce order-processing scenario is used, involving tasks
such as:

Validating items

Calculating taxes

Applying discounts

Processing payments

Sending receipts

Breaking these responsibilities into functions improves modularity,
readability, and debugging.

💻 Section B --- Coding Questions

9. Sum of Digits

A program accepts a number and uses a while loop to extract each digit
and calculate the total.

Core operations include:

last_digit = num % 10
num = num // 10

Example result:

the sum of digits is 9

10. Even Number Filter

The notebook defines a function:

filter_even_num(num)

The function loops through a list and creates a new list containing only
even numbers.

Example:

original list is [11, 22, 13, 67, 87, 23, 34, 43, 54, 56, 99, 76]
filtered even number list is [22, 34, 54, 56, 76]

11. Fibonacci Series

The program generates a Fibonacci sequence for a user-specified number
of terms.

It handles:

Non-positive input

A single requested term

Multiple Fibonacci terms

Example output:

fibonacci series:
0 1 1 2 3 5

12. List Reversal Using Slicing

The program accepts space-separated numbers from the user, converts them
to integers, and reverses the list using slicing.

The main slicing operation is:

original_list[::-1]

Example:

the original list is [2, 4, 5, 7, 8]
the reversed list is [8, 7, 5, 4, 2]

13. NumPy Slicing

A NumPy array containing 11 elements is created.

The program:

Calculates the midpoint

Extracts the first half using slicing

Calculates the sum of the extracted elements

Example:

the original numpy array is [10 22 12 33 21 34 56 54 57 98 87]
first half of the array is [10 22 12 33 21]
sum of the extracted elements is 98

The NumPy function used for the sum is:

np.sum(first_half)

14. Arithmetic Palindrome

The notebook checks whether a number is a palindrome without converting
it to a string.

It uses arithmetic operations to:

Extract the last digit

Build the reversed number

Compare the reversed number with the original

Core operations include:

last_digit = temp % 10
reversed_num = (reversed_num * 10) + last_digit
temp = temp // 10

Example:

original number is 22 a palindrome

15. Nested Loop Pattern

A nested loop is used to generate the following pattern:

1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

The exercise demonstrates:

Outer loops

Inner loops

Repeated output

print(..., end=" ")

🧠 Logic and Research Questions

16. Benefits of Pseudocode

The notebook explains pseudocode as a planning step before writing
actual code.

Benefits discussed include:

Focusing on logic instead of syntax

Acting as a blueprint

Identifying logic problems early

Saving implementation time

17. Limitations of Using Only Loops and Conditionals

The assignment explains that relying only on loops and conditional
statements can result in code that is:

Long

Repetitive

Difficult to read

Difficult to scale

It highlights the usefulness of additional programming structures such
as functions, recursion, and objects.

18. Modular Debugging

Breaking a problem into functions isolates different parts of a program.

This makes it easier to:

Test individual components

Locate errors

Fix specific functionality

Maintain the program

19. Slicing vs Looping

The notebook explains that slicing can be useful when a specific portion
of a sequence needs to be extracted.

Examples include:

Selecting the top items from a leaderboard

Extracting a specific range of data

Reversing a sequence

Selecting regularly spaced elements

20. Error Analysis

The final question emphasizes that errors and unexpected output are
useful during programming practice.

Debugging helps developers:

Understand why code behaves unexpectedly

Identify gaps in understanding

Improve problem-solving skills

Write more reliable programs

🎯 Learning Objectives

This assignment provides hands-on practice with:

Python execution flow

Data types

Operators

Conditional logic

for and while loops

range()

Functions

Problem decomposition

List processing

List slicing

Fibonacci sequences

Palindrome logic

Nested loops

NumPy arrays

NumPy slicing

Basic debugging and error analysis

Programming logic building

🚀 How to Run the Notebook

1. Clone the Repository

git clone <your-repository-url>
cd <your-repository-folder>

2. Install Dependencies

pip install notebook numpy

3. Start Jupyter Notebook

jupyter notebook

Open:

Assignment2.ipynb

and execute the cells.

📦 Requirements

Python 3.x
Jupyter Notebook
NumPy

An optional requirements.txt can contain:

numpy
notebook

📝 Notes

Several coding exercises use input(), so they require interactive
input when executed in Jupyter Notebook.

The README summarizes the structure and purpose of the notebook. The
original assignment notebook contains the complete theory answers,
source code, and executed examples.

👩‍💻 Author

Sandhya Shakya

⭐ Conclusion

Assignment 2: Logic Building with Python and NumPy focuses on
applying fundamental Python concepts to practical problem-solving.

Through loops, functions, slicing, arithmetic operations, NumPy arrays,
and modular programming concepts, the assignment provides continued
practice in building structured programming logic and understanding how
Python programs execute.
