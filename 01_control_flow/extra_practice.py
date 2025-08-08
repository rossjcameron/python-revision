# =========================================================
# Enumerate – Extra Exercises
# =========================================================

# 🧠 1. Task: Print "1) Monday", "2) Tuesday", ... for all days in a list.
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for index, day in enumerate (days, start=1):
    print(f"{index}) {day}")

# 🧠 2. Task: Given a list of animals, print each one with its position number starting at 100.
animals = ["dog", "cat", "hamster", "parrot"]

for index, animal in enumerate(animals, start=100):
    print(f"{index}: {animal}")

# 🧠 3. Task: Print all book titles from a list with "Book #<number> → <title>" format.
books = ["1984", "Pride and Prejudice", "To Kill a Mockingbird"]

for index, book in enumerate(books, start=1001):
    print(f"Book number: {index} → {book}")

# 🧠 4. Task: Print student names with their index, but index should start at 0.
students = ["Alice", "Bob", "Charlie"]

for index, student in enumerate(students, start=0):
    print(f"{student}, Student No: {index}")

# 🧠 5. Task: Given a shopping list, print each item in the format "<index>. <item>  (position starts at 1)".
shopping = ["milk", "bread", "eggs", "cheese"]
for index, item in enumerate(shopping, start=1):
    print(f"Item {index}: {item}")

# 🧠 6. Task: Print a leaderboard in the format "Rank X: <player>" for a list of player names.
players = ["Ross", "Chloe", "Jamie", "Taylor"]

for rank, player in enumerate(players, start=1):
    print(f"Rank {rank}: {player}")

# 🧠 7. Task: Print each city in a list with its name in uppercase alongside its position.
cities = ["Glasgow", "Edinburgh", "London", "New York"]

for pos, city in enumerate(cities, start=1):
    print(f"{pos}: {city.upper()}")

# 🧠 8. Task: Given a list of favourite movies, print them in reverse order with numbering starting at 1.
movies = ["Inception", "The Matrix", "Interstellar", "Fight Club"]
for rank, movie in enumerate(reversed(movies), start=1):
    print(f"{rank}: {movie}")

# 🧠 9. Task: Print each colour in a list, but skip the index number for the first colour.
colours = ["red", "green", "blue", "yellow"]
for idx, colour in enumerate(colours, start=1):
    if idx == 1:
        print(colour)
    else:
        print(f"{idx}: {colour}")

# 🧠 10. Task: Given a list of countries, print them with a dash before the index like "-1: <country>".
countries = ["Scotland", "France", "Japan", "Canada"]
for idx, country in enumerate(countries, start=1):
    print(f"-{idx}: {country}")

# =========================================================
# Sentinel Values – Extra Exercises
# =========================================================

# 🧠 1. Task: Print each number from the list until you encounter -1 (sentinel), then stop.
nums = [5, 7, 9, -1, 12, 14]
i = 0

while i < len(nums) and nums[i] != -1:
    print(nums[i])
    i += 1

# 🧠 2. Task: Keep reading names from a list and printing them until you hit "STOP".
names = ["Alice", "Bob", "STOP", "Charlie", "Dana"]
i = 0

while i < len(names) and names[i] != "STOP":
    print(names[i])
    i += 1

# 🧠 3. Task: Loop through temperatures and stop when you hit None.
temperatures = [21.5, 20.0, 19.8, None, 22.1]
i = 0

while i < len(temperatures) and temperatures[i] is not None:
    print(temperatures[i])
    i += 1


# 🧠 4. Task: Print colours from the list until you see "end".
colours = ["red", "blue", "green", "end", "yellow"]

i = 0

while i < len(colours) and colours[i] != "end":
    print(colours[i])
    i += 1

# 🧠 5. Task: Read prices from a list and sum them until you hit 0, then print the total.
prices = [5.99, 3.49, 7.25, 0, 4.10]

i = 0
result = 0

while i < len(prices) and prices[i] != 0: 
    result += prices[i]
    i += 1

print(f"{result:.2f}")

# 🧠 6. Task: Go through a list of words and stop when you reach an empty string "".
words = ["Python", "Java", "", "C++", "Rust"]
i = 0

while i < len(words) and words[i] != "":
    print(words[i])
    i += 1

# 🧠 7. Task: Loop through exam scores until you reach a negative number.
scores = [88, 76, 92, -5, 85]
i = 0

while i < len(scores) and scores[i] >= 0:
    print(scores[i])
    i += 1

# 🧠 8. Task: Print all items in the shopping list until you see "done".
shopping = ["milk", "bread", "eggs", "done", "cheese"]
i = 0

while i < len(shopping) and shopping[i] != "done":
    print(shopping[i])
    i += 1

# 🧠 9. Task: Process transactions until you encounter None.
transactions = [150, 200, 50, None, 300]
i = 0

while i < len(transactions) and transactions[i] is not None:
    print(transactions[i])
    i += 1

# 🧠 10. Task: Loop through letters until you see the letter "X".
letters = ["A", "B", "C", "X", "D", "E"]
i = 0

while i < len(letters) and letters[i] != "X":
    print(letters[i])
    i += 1

