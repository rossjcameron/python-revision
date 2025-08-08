# 00_basics/notes.py
# ------------------
# 📚 SECTION: Python Basics
# Topics Covered:
# - Variables
# - Data Types
# - Type Conversion
# - Arithmetic & Comparison Operators
# - Logical Operators
# - Strings (creation, methods, formatting)

# ─────────────────────────────────────────────
# 🔸 VARIABLES
# Variables are containers for storing data values.

# Syntax:
name = "Ross"  # string
age = 26       # integer
height = 1.82  # float
is_student = True  # boolean

# Python is dynamically typed, so you don’t need to declare the type beforehand.
# You can reassign different types to the same variable name:
x = 10
x = "ten"  # This is valid, though not always recommended

# ─────────────────────────────────────────────
# 🔸 DATA TYPES
# Common types:
# - str: text (e.g., "hello")
# - int: whole numbers (e.g., 42)
# - float: decimal numbers (e.g., 3.14)
# - bool: True or False
# - None: represents the absence of a value

# You can check the type using `type()`:
print(type(42))        # <class 'int'>
print(type("hello"))   # <class 'str'>

# ─────────────────────────────────────────────
# 🔸 TYPE CONVERSION
# Converting one type to another using built-in functions

a = "123"
b = int(a)  # string to int
c = float(b)  # int to float
d = str(c)  # float to string

# Watch out: converting non-numeric strings to int will cause an error.
# int("abc")  # ValueError!

# ─────────────────────────────────────────────
# 🔸 ARITHMETIC OPERATORS
# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division (always returns float)
# // Floor Division (rounds down to nearest int)
# %  Modulus (remainder)
# ** Exponentiation (power)

# Examples:
print(5 + 2)     # 7
print(5 / 2)     # 2.5
print(5 // 2)    # 2
print(2 ** 3)    # 8

# ─────────────────────────────────────────────
# 🔸 COMPARISON OPERATORS
# Used for comparison; return a boolean (True/False)
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

# Example:
print(5 == 5)    # True
print(5 != 3)    # True
print(7 < 2)     # False

# ─────────────────────────────────────────────
# 🔸 LOGICAL OPERATORS
# Used to combine multiple boolean expressions:
# and  → True if both conditions are true
# or   → True if at least one condition is true
# not  → Inverts the condition

# Example:
x = 10
print(x > 5 and x < 20)  # True
print(not x == 10)       # False

# ─────────────────────────────────────────────
# 🔸 STRINGS
# Strings are text enclosed in quotes (" or ')

# Creation:
greeting = "Hello"
name = 'Ross'
combined = greeting + ", " + name  # String concatenation
print(combined)  # Hello, Ross

# Indexing (0-based):
print(name[0])  # 'R'

# Slicing:
print(name[1:3])  # 'os'

# Useful string methods:
text = "python is awesome"

print(text.upper())     # 'PYTHON IS AWESOME'
print(text.capitalize())  # 'Python is awesome'
print(text.replace("awesome", "powerful"))  # 'python is powerful'
print(text.startswith("py"))  # True
print(text.endswith("some"))  # True
print(len(text))        # 17 (length of string)

# ─────────────────────────────────────────────
# 🔸 STRING FORMATTING

# f-strings (modern and clean):
age = 24
print(f"My name is {name} and I am {age} years old.")

# old style:
print("My name is %s and I am %d years old." % (name, age))

# str.format():
print("My name is {} and I am {} years old.".format(name, age))

# ─────────────────────────────────────────────
# ✅ Summary:
# - Python is dynamically typed.
# - Variables can hold many types: strings, numbers, booleans.
# - Operators let you perform math and logic.
# - Strings are super powerful — learn to manipulate and format them.

