# -------------------------------
# 📘 PYTHON BASICS — REFERENCE NOTES
# -------------------------------

# 🟦 VARIABLES
# - No need to declare types
# - Use snake_case naming convention

name = "Ross"
age = 27
height_m = 1.82
is_coder = True

# 🟧 DATA TYPES
# - str, int, float, bool, list, tuple, set, dict, None

# Examples:
string_example = "Python"
int_example = 100
float_example = 99.9
bool_example = False
none_example = None

# 🟨 TYPE CHECKING & CASTING
# - Use type() to inspect types
# - Use int(), float(), str(), bool() to cast

print(type(name))  # <class 'str'>
num_as_string = str(123)
pi_as_int = int(3.14)

# 🟥 OPERATORS
# Arithmetic: + - * / // % **
# Comparison: == != > >= < <=
# Logical: and, or, not
# Assignment: = += -= *= /=

# Example:
a, b = 10, 3
print(a + b)     # 13
print(a ** b)    # 1000
print(a // b)    # 3

# Logical:
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 🟩 STRINGS
# - Immutable, iterable
# - Use single or double quotes

# String methods:
greeting = "  hello, Ross!  "
print(greeting.strip())
print(greeting.upper())
print("Ross".startswith("R"))
print("Ross".replace("s", "z"))

# String formatting:
name = "Ross"
age = 27
print(f"My name is {name} and I'm {age} years old.")
print("My name is {} and I'm {} years old.".format(name, age))

# Indexing & slicing:
text = "Programming"
print(text[0])        # P
print(text[-1])       # g
print(text[0:6])      # Progra
