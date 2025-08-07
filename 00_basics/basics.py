# 00_basics/basics.py
# -------------------
# 🎯 Python Basics – Practice Exercises
# ➕ Variables, Data Types, Operators, Strings

# 🧠 1. Create variables to store your:
# - Name (string)
# - Age (integer)
# - Height in metres (float)
# - Whether you’re a student (boolean)

name = "Ross"
age = 24
height = 1.88
is_student = False

# 🧠 2. Print each variable along with its type using the `type()` function.
print(type(name), name)
print(type(age), age)
print(type(height), height)
print(type(is_student), is_student)

# 🧠 3. Convert the following string to an integer and multiply it by 5
num_str = "15"
# Your code here
print(int(num_str)*5)

# 🧠 4. Calculate the area of a rectangle (width × height)
width = 5.5
height = 3.2
# Your code here
area = width * height
print(f"{area:.2f}")

# 🧠 5. Test these comparisons and print the results:
a = 10
b = 20

# Is a equal to b?
is_equal = a == b
print(is_equal)

# Is a not equal to b?
is_not_equal = a != b
print(is_not_equal)

# Is b greater than or equal to a?
is_greater_than_equal_to = b >= a
print(is_greater_than_equal_to)

# 🧠 6. Use logical operators:
# Check if a number is between 10 and 50 using `and`
number = 25
# Your code here
is_between = number >= 10 and number <= 50
print(is_between)

# 🧠 7. String tasks:
# - Make the string uppercase
# - Replace "Python" with "Programming"
# - Check if the string ends with "fun"

message = "Python is fun"
#Your code here
print(message.upper())
print(message.replace("Python", "Programming"))
print(message.endswith("fun"))

# 🧠 8. Use f-strings to print:
# "Hello, my name is ___ and I am ___ years old."
# Use the variables you defined earlier.
print(f"My name is {name} and my age is {age}")

# 🧠 9. Bonus: Create a complex expression using arithmetic and logical operators:
# Example goal: Is the remainder of 25 divided by 4 greater than 1 and less than 3?
# Your code here
result = (25 % 4) > 1 and (25 % 4) < 3
print(result)

# 🧠 10. CHALLENGE: Reverse a string using slicing
word = "Python"
# Expected: "nohtyP"
# Your code here
print(word[::-1])

# 🧠 11. CHALLENGE: Get the middle character(s) of a string
# - If odd length → return middle character
# - If even length → return the two middle characters
# Try with: "racecar" and "coding"
# Your code here
word = "coding"

if len(word) % 2 == 0:
    mid_char = word[len(word)//2 - 1 : len(word)//2 + 1]
else:
    mid_char = word[len(word)//2]
print(mid_char)

# 🧠 12. EXTRA CHALLENGE (Repetition for mastery):
# Create variables for two people (name, age), and print:
# - Who is older?
# - The age difference
# - Format a sentence: "___ is ___ years older than ___."

# Example values:
name1, age1 = "Alice", 30
name2, age2 = "Bob", 26
# Your code here

if age1 > age2:
    print(f"{name1} is older than {name2}")
else:
    print(f"{name2} is older than {name1}")

print(f"The age difference is {age1 - age2}")
