# 01_control_flow/notes.py
# ------------------------
# 📚 SECTION: Control Flow
# Topics Covered (with plain-English explanations):
# 1) Booleans & comparisons
# 2) Logical operators (and, or, not) + short-circuiting
# 3) Truthy & falsy values
# 4) if / elif / else (including conditional expressions)
# 5) Comparison chaining & identity vs equality
# 6) for-loops (range, enumerate, zip, dict iteration)
# 7) while-loops (sentinel patterns)
# 8) break, continue, pass
# 9) Loop else-clauses
# 10) Common pitfalls & best practices

# ───────────────────────────────────────────────────────────────────────────────
# 1) BOOLEANS & COMPARISONS
# Booleans are True or False. Comparisons return booleans.

# Comparison operators:
# == equal, != not equal, > greater, < less, >= greater-or-equal, <= less-or-equal
print(5 == 5)      # True
print(7 != 3)      # True
print(10 > 20)     # False
print(3 <= 3)      # True

# In plain terms: comparisons ask a yes/no question about values.

# ───────────────────────────────────────────────────────────────────────────────
# 2) LOGICAL OPERATORS (+ SHORT-CIRCUITING)
# and  → True if BOTH sides are True
# or   → True if AT LEAST ONE side is True
# not  → flips True to False and vice-versa

age = 24
has_id = True

print(age >= 18 and has_id)  # True only if both checks pass
print(age < 18 or has_id)    # True if either condition passes
print(not has_id)            # Invert a condition

# Short-circuiting: Python stops early if the result is already decided.
# - For `and`, if the left side is False, it doesn't evaluate the right side.
# - For `or`, if the left side is True, it doesn't evaluate the right side.

def side_effect():
    print("I ran!")  # Side effect we can see
    return True

print(False and side_effect())  # False, function never runs due to short-circuit
print(True or side_effect())    # True, function never runs due to short-circuit

# De Morgan’s laws (handy for refactoring):
# not (A and B) == (not A) or (not B)
# not (A or B)  == (not A) and (not B)

# ───────────────────────────────────────────────────────────────────────────────
# 3) TRUTHY & FALSY VALUES
# In if-statements and logical expressions, non-boolean values can act like True/False.
# FALSY (act like False): 0, 0.0, 0j, "", [], {}, set(), range(0), None, and custom objects with __bool__ returning False.
# TRUTHY (act like True): almost everything else (non-empty strings/lists/etc., non-zero numbers).

print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool("Hi"))     # True
print(bool([1, 2]))   # True

# Practical: check if a list has items
nums = []
if nums:  # Empty list is falsy
    print("Has numbers")
else:
    print("No numbers")

# ───────────────────────────────────────────────────────────────────────────────
# 4) IF / ELIF / ELSE + CONDITIONAL EXPRESSIONS
# Syntax:
# if condition:
#     block
# elif another_condition:
#     block
# else:
#     block

score = 78
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D or below"
print(grade)

# Conditional expression (a compact one-liner):
# <value_if_true> if <condition> else <value_if_false>
is_weekend = False
plan = "Rest" if is_weekend else "Work"
print(plan)

# Guard clauses: exit early to keep code flatter (fewer nested blocks).
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

result = divide(10, 0)
print(result)

# ───────────────────────────────────────────────────────────────────────────────
# 5) COMPARISON CHAINING & IDENTITY VS EQUALITY
# Chaining: a < b < c means (a < b) and (b < c)
x = 5
print(1 < x < 10)  # True

# Equality vs identity:
# == checks values are equal.
# is checks if two names point to the same object in memory (identity).
a = [1, 2]
b = [1, 2]
c = a
print(a == b)  # True (same contents)
print(a is b)  # False (different lists in memory)
print(a is c)  # True (same list object)

# DO NOT use `is` to compare strings or numbers for equality. Use `==`.

# ───────────────────────────────────────────────────────────────────────────────
# 6) FOR-LOOPS
# Loop over items of an iterable (string, list, tuple, dict, set, etc.)

for ch in "AB":
    print(ch)  # A then B

# range(start, stop[, step]) generates numbers (stop is exclusive).
for i in range(3):
    print("i =", i)  # 0, 1, 2

# enumerate gives (index, item).
items = ["a", "b", "c"]
for index, item in enumerate(items, start=1):
    print(index, item)

# zip pairs items from multiple iterables.
names = ["Ross", "Chloe"]
scores = [95, 88]
for name, sc in zip(names, scores):
    print(name, sc)

# Iterating dictionaries:
person = {"name": "Ross", "role": "Engineer"}
for key in person:  # keys by default
    print("key:", key)
for key, value in person.items():
    print(key, "→", value)

# Key–Value List Pairs:
# Sometimes you have a list of key–value pairs (like tuples or lists of length 2).
# You can unpack them directly in the for-loop just like with dict.items().

pairs = [
    ("name", "Ross"),
    ("role", "Engineer"),
    ("location", "Scotland")
]

for key, value in pairs:
    print(f"{key}: {value}")

# This works with:
# - Lists of tuples: [("a", 1), ("b", 2)]
# - Lists of lists: [["a", 1], ["b", 2]]
# - Any iterable of 2-item iterables
# Python will unpack each pair into 'key' and 'value' variables automatically.


# ───────────────────────────────────────────────────────────────────────────────
# 7) WHILE-LOOPS
# A while loop repeats WHILE a given condition remains True.
# Be careful to update/change something inside the loop to avoid an infinite loop.

count = 0
while count < 3:                 # Condition is checked BEFORE each iteration
    print("count =", count)      # Loop body runs if condition is True
    count += 1                   # Progress towards making the condition False

# ───────────────────────────────────────────────────────────────────────────────
# SENTINEL LOOP
# A "sentinel" is a special value that signals "stop processing".
# This type of loop continues until it encounters that sentinel value.

data = [5, 4, 3, None, 100]  # 'None' here is the sentinel value → when found, stop
i = 0                        # Starting index

# while CONDITION:
# - 'i < len(data)' ensures we stay inside the list bounds (no IndexError)
# - 'and' combines conditions → BOTH must be True for the loop to continue
# - 'data[i] is not None' checks if the current element is NOT the sentinel value
while i < len(data) and data[i] is not None:
    print("val:", data[i])   # Process the current value
    i += 1                   # Move to the next index


# ───────────────────────────────────────────────────────────────────────────────
# 8) break, continue, pass
# break    → stop the loop entirely
# continue → skip to the next iteration
# pass     → do nothing (placeholder to satisfy syntax)

for n in range(10):
    if n == 3:
        continue  # skip 3
    if n == 7:
        break     # stop at 7
    print(n)

def todo():
    pass  # We'll implement later

# ───────────────────────────────────────────────────────────────────────────────
# 9) LOOP ELSE-CLAUSES
# The `else` on a loop runs only if the loop DID NOT end via `break`.

target = 13
for n in [2, 4, 6, 8]:
    if n == target:
        print("Found it!")
        break
else:
    print("Not found (loop finished normally without break).")

# Great for "search" patterns:
nums = [2, 3, 5, 7, 11]
needle = 5
for n in nums:
    if n == needle:
        print("Found", needle)
        break
else:
    print("Not found")

# ───────────────────────────────────────────────────────────────────────────────
# 10) COMMON PITFALLS & BEST PRACTICES
# - Using `is` instead of `==` for string/number comparison → use `==`.
# - Off-by-one errors with range: remember stop is exclusive.
# - Modifying a list while iterating over it: iterate over a copy if needed.
# - Infinite while-loops: ensure the loop condition will eventually be False.
# - Over-nesting if/else: prefer guard clauses to reduce indentation.
# - Relying on truthiness without being explicit can hide bugs; be intentional.
# - Prefer descriptive variable names to make conditions readable.
# - For clarity, use parentheses to group complex boolean logic.


