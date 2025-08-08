# 01_control_flow/control_flow.py
# ------------------------------
# 🎯 Control Flow – Practice Exercises
# Focus: if/elif/else, loops, logical ops, truthy/falsy, break/continue/pass, loop-else
# Format: commented tasks with room to work + repetition for retention + realistic challenges.

# ==============================================================================
# SECTION A — If / Elif / Else (fundamentals)
# ==============================================================================

# A1) Basic conditions
# Task: Use if/elif/else to assign a risk_label based on `credit_score`.
#  - 800+ → "Excellent"
#  - 740–799 → "Very Good"
#  - 670–739 → "Good"
#  - 580–669 → "Fair"
#  - below 580 → "Poor"
credit_score = 680

if credit_score >= 800:
    risk_label = "Excellent"
elif 740 <= credit_score <= 799:
    risk_label = "Very Good"
elif 670 <= credit_score <= 739:
    risk_label = "Good"
elif 580 <= credit_score <= 669:
    risk_label = "Fair"
else:
    risk_label = "Poor"


print(risk_label)

# A2) Conditional expression (one-liner)
# Task: Set `status` to "adult" if age >= 18 else "minor".
age = 17

if age >= 18:
    status = "adult"
else:
    status = "minor"

print(status)

# A3) Guard clauses
# Task: Write a function `safe_ratio(a, b)` that:
#  - returns "undefined" if b == 0 (guard clause)
#  - otherwise returns a / b

def safe_ratio(a, b):
    if b == 0:
        return "undefined"
    return a / b
    
result = safe_ratio(5,0)

print(result)

# A4) Comparison chaining
# Task: Set `within_range` to True if n is strictly between 10 and 20.
n = 15

within_range = 10 < n < 20

print(within_range)

# A5) Identity vs equality
# Task: For the two lists below, demonstrate:
# - equality check with ==, and identity check with is
# - assign `same_value`, `same_object`, then print both
l1 = [1, 2, 3]
l2 = [1, 2, 3]

same_value = l1 == l2
same_object = l1 is l2
print(same_value, same_object)

# Repetition variant:
# A6) Repeat A1–A5 with different values to reinforce muscle memory.
credit_score_2 = 835
age_2 = 22
n_2 = 21
l3 = ["a"]
l4 = l3
# Do the same checks again with *_2 / l3 / l4.

credit_score2 = 780

if credit_score2 > 800:
    risk_label = "Excellent"
elif 740 <= credit_score2 <= 799:
    risk_label = "Very Good"
elif 670 <= credit_score2 <= 739:
    risk_label = "Good"
elif 580 <= credit_score2 <= 669:
    risk_label = "Fair"
else:
    risk_label = "Poor"


print(risk_label)

#---

if age_2 >= 18:
    status = "adult"
else:
    status = "minor"

print(status)

#--- 

same_value = l3 == l4
same_object = l3 is l4
print(same_value, same_object)

# ==============================================================================
# SECTION B — Logical Operators & Truthy/Falsy
# ==============================================================================

# B1) Short-circuiting practice
# Task: Create two functions:
# - left() prints "left" and returns False
# - right() prints "right" and returns True
# Use them in expressions to show when the second part does/doesn't run.
def left():
    print("left")
    return False

def right():
    print("right")
    return True

print(left() and right())   # Which functions run?
print(right() or left())    # Which functions run?

# B2) Truthiness checks
# Task: Given containers, print whether each is truthy or falsy WITHOUT using len().
values = ["", "hi", [], [0], {}, {"k": 1}, 0, 1, None, range(0)]
for v in values:
    if v:
        print("Truthy")
    else:
        print("Falsy")

# B3) Practical truthiness
# Task: Implement function `first_non_empty(*strings)` that returns the first
# non-empty string, or "" if all are empty.
def first_non_empty(*strings):
    for s in strings:       # loop through all provided strings
        if s:               # truthy check → skips empty strings ""
            return s        # return the first non-empty one
    return ""     
    
# # # Example:
print(first_non_empty("", "Ross", "", "Chloe"))  # "Ross"

# B4) De Morgan refactor
# Task: Re-express `not (a and b)` using `not a` / `not b` with or, and vice versa.
a, b = True, False
expr1 = not (a and b)
expr1_refactor = not a or not b
expr2 = not (a or b)
expr2_refactor = not a and not b

print(expr1, expr1_refactor, expr2, expr2_refactor)

# ==============================================================================
# SECTION C — For-Loops
# ==============================================================================

# C1) Range basics
# Task: Print numbers 1..10 inclusive using range.
for i in range(1, 11):
    print(i)

# C2) Summation & counting
# Task: Given numbers, compute:
#  - total sum
#  - count of even numbers
nums = [3, 8, 11, 14, 17, 22]
total = sum(nums)

evens = 0

for i in nums:
    if i % 2 == 0:
        evens += 1

print(total, evens)

# C3) Enumerate
# Task: Print "1: apple", "2: banana", ... using enumerate start=1.
fruits = ["apple", "banana", "cherry"]

for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}: {fruit}")


# C4) Zip
# Task: Combine names & balances; print "Ross → £<balance>".
names = ["Ross", "Chloe", "Sam"]
balances = [250.50, 90.00, 1200.00]
for name, balance in zip(names, balances):
    print(f"{name} → £{balance:.2f}")


# C5) Dict iteration
# Task: For each key-value, print "key=value".
profile = {"name": "Ross", "role": "Software Engineer", "city": "New Jersey"}
for key, value in profile.items():
    print(f"{key}: {value}")

# ==============================================================================
# SECTION D — While-Loops
# ==============================================================================

# D1) Basic while-loop
# Task: Print down from 5 to 1, then "Lift-off!".
start = 5
while start >= 1:
    print(start)
    start -= 1

print("Lift-off!")

# D2) Sentinel loop
# Task: Process items until None is reached; collect non-None into `cleaned`.
data = [10, 9, 8, None, 100, 200]
cleaned = []

i = 0

while i < len(data) and data[i] is not None:
    cleaned.append(data[i])
    i += 1

print(cleaned)

# D3) Simple input-like loop (no real input for testing)
# Task: Simulate attempts up to `max_attempts` to match `target`.
# If matched, print "Success in X tries" and stop early.
# Otherwise print "Failed after N tries" using else on the loop.
guesses = [12, 14, 17, 19, 21]
target = 19
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    if guesses[attempts] == target:
        print(f"Success in {attempts + 1} tries!")
        break
    attempts += 1
else: 
    print(f"Failed after {max_attempts} tries!")

# ==============================================================================
# SECTION E — break / continue / pass
# ==============================================================================

# E1) continue
# Task: Print numbers 0..9 except multiples of 3 (skip them).
for n in range(10):
    if n % 3 == 0:
        continue
    print(n)



# E2) break
# Task: Iterate 0..99 and stop once you hit the first square number > 50.
# Print that number and break.
for n in range(100):
    root = int(n ** 0.5)
    if root * root == n and n > 50:
        print(n)
        break
 

# E3) pass
# Task: Create stub functions validate_user, save_user that do nothing (yet).
def validate_user(u):
    pass
def save_user(u):
     pass

# Repetition variant:
# E4) Re-run E1–E2 with different ranges/conditions.

# ==============================================================================
# SECTION F — Loop else (search patterns)
# ==============================================================================

# F1) Search for a prime and use else
# Task: Given `candidates`, print the first prime found; if none, print "No primes".
candidates = [12, 15, 18, 21, 22, 23, 24]

for n in candidates:
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            print(n)
            break
else:
    print("No primes")

# F2) Find missing number (1..n) using loop-else confirmation
# Task: Confirm all numbers 1..n appear in `bag`. If all present, print "complete",
# else print the first missing number then stop.
bag = [1, 2, 4, 5]
nmax = 5

for num in range(1, nmax + 1): 
    if num not in bag:
        print(f"Missing: {num}")
        break
else:
    print("Check Complete")

# ==============================================================================
# SECTION G — Realistic mini-challenges (banking/data vibes)
# ==============================================================================

# G1) Transaction filter
# Task: Given transactions (amounts in £), create:
#  - high_risk: values >= 1000
#  - review_needed: values between 500 and 999 (inclusive)
#  - ok: the rest
transactions = [25, 1200, 999, 501, 500, 75, 3000, 12]

high_risk = []
review_needed = []
ok = []

for i in transactions:
    if i >= 1000:
        high_risk.append(i)
    elif 500 <= i <= 999:
        review_needed.append(i)
    else:
        ok.append(i)

print(high_risk)
print(review_needed)
print(ok)

# G2) Rolling sum until threshold (while)
# Task: Keep summing from `stream` until `threshold` reached; print count of items used.
stream = [120, 150, 90, 300, 450, 30]
threshold = 500

total = 0
used = 0
i = 0 

while total < threshold and i < len(stream):
    total += stream[i]
    used += 1
    i += 1

print(f"Used {used} numbers to reach {total}")

# G3) Password rule checker (if/elif/else + logical ops)
# Rules:
#  - at least 8 chars
#  - contains a digit
#  - contains a special from set("!@#$%^&*")
# Print "Strong" if all pass, "Weak" otherwise.
pwd = "Abcdef!2"
specials = ("!@#$%^&*")

has_len = len(pwd) >= 8
has_digit = any(character.isdigit() for character in pwd)
has_special = any(character in specials for character in pwd)


if has_len and has_digit and has_special:
    print("Strong")
else:
    print("Weak")

# ==============================================================================
# SECTION H — Classic exercises (build fluency)
# ==============================================================================

# H1) FizzBuzz (control flow staple)
# Print numbers 1..100 with:
# - "Fizz" for multiples of 3,
# - "Buzz" for multiples of 5,
# - "FizzBuzz" for multiples of both,
# - number otherwise.

if i % 15 == 0:
    print(f"{i}: FizzBuzz")
elif i % 3 == 0:
    print(f"{i}: Fizz")
elif i % 5 == 0:
    print(f"{i}: Buzz")
else:
    print(i)

# H2) Count vowels in a string (for-loop, conditionals)
s = "This is a practice string for CONTROL FLOW."
vowels = "aeiou"
vowel_count = 0

for letter in s.lower():
    if letter in vowels:
        vowel_count += 1

print(vowel_count)

# ==============================================================================
# SECTION I — Output-focused: "What will this print?"
# ==============================================================================

# I1) Predict the output and THEN run it to check. Write the predicted output in a comment.
# Tip: consider short-circuiting and loop-else.

# Snippet A
# ---------
total = 0
for n in [2, 4, 6, 8]:
    if n % 3 == 0:
       break
    total += n
else:
    total = -1
print(total)

# # Your prediction: 6

# Snippet B
# ---------
def f():
     print("f")
     return False
def g():
     print("g")
     return True
print(f() and g())
print(g() or f())

# Your prediction: f False, g True

# Snippet C
# ---------
x = 5
print(1 < x < 5)
print(1 < x <= 5)
# # Your prediction: False, True

# ==============================================================================
# SECTION J — Debug this code (spot and fix common mistakes)
# ==============================================================================

# J1) Buggy: uses `is` for numeric equality; has off-by-one; wrong branch.
# Fix it.
count = 0
for i in range(1, 11):  
   if i == 5:          
      count = count + 2
   elif i % 2 == 0:     
      count = count + 1
print(count)

# J2) Buggy: infinite loop risk; condition never changes.
# Fix it to stop after printing 3, 2, 1.
n = 3
while n > 0:
    print(n)
    n -= 1
print("Done")

# J3) Buggy: modifies list while iterating directly over it.
# Fix by iterating over a copy or building a new list.
vals = [1, 2, 3, 4]
evens = []

for v in vals:
    if v % 2 == 0:
        vals.remove(v)
        evens.append(v)
    
print(vals)
print(evens)

# ==============================================================================
# SECTION K — Refactor for readability (guard clauses & boolean clarity)
# ==============================================================================

# K1) From nested ifs to guard clauses:
# Original:
# def withdraw(balance, amount, daily_limit):
#     if amount <= balance:
#         if amount <= daily_limit:
#             return balance - amount
#         else:
#             return "Over daily limit"
#     else:
#         return "Insufficient funds"
#
# Refactor to:
def withdraw(balance, amount, daily_limit):
    if balance <= amount:
        return "Insufficient funds"
    elif amount <= daily_limit:
        return balance - amount
    else:
        return "Over daily limit"

print(withdraw(100,123,70))

# K2) Boolean clarity:
# Original:
# if not (user_is_active == False or has_penalty == True):
#     grant_access()
#
# Refactor with clear booleans, no double negatives.

#if user_is_active == True and has_penalty == False:
#   grant_access()


