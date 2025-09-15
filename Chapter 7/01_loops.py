# Demonstrating various types of loops in Python

# 1. For loop: Repeats a block for each item in a sequence
print("For loop:")
for i in range(3):
    print("  i =", i)
# Output:
#   i = 0
#   i = 1
#   i = 2

# 2. While loop: Repeats as long as a condition is True
print("\nWhile loop:")
j = 0
while j < 3:
    print("  j =", j)
    j += 1
# Output:
#   j = 0
#   j = 1
#   j = 2

# 3. Nested loop: Loop inside another loop
print("\nNested loop:")
for x in range(2):
    for y in range(2):
        print(f"  x={x}, y={y}")
# Output:
#   x=0, y=0
#   x=0, y=1
#   x=1, y=0
#   x=1, y=1

# 4. Loop with else: 'else' runs after loop finishes (not by break)
print("\nFor loop with else:")
for k in range(2):
    print("  k =", k)
else:
    print("  Loop finished!")
# Output:
#   k = 0
#   k = 1
#   Loop finished!

# 5. Looping through a list
print("\nLooping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("  fruit =", fruit)
# Output:
#   fruit = apple
#   fruit = banana
#   fruit = cherry

# 6. Using break and continue
print("\nUsing break and continue:")
for n in range(5):
    if n == 3:
        break  # Exit the loop when n is 3
    if n == 1:
        continue  # Skip the rest of the loop when n is 1
    print("  n =", n)
# Output:
#   n = 0
#   n = 2

# 7. Looping with enumerate (get index and value)
print("\nUsing enumerate:")
colors = ["red", "green", "blue"]
for idx, color in enumerate(colors):
    print(f"  Index: {idx}, Color: {color}")
# Output:
#   Index: 0, Color: red
#   Index: 1, Color: green
#   Index: 2, Color: blue

# 8. Looping through a dictionary
print("\nLooping through a dictionary:")
student = {"name": "Amiya", "age": 21, "branch": "CSE"}
for key, value in student.items():
    print(f"  {key}: {value}")
# Output:
#   name: Amiya
#   age: 21
#   branch: CSE

# 9. List comprehension with loop
print("\nList comprehension:")
squares = [x**2 for x in range(5)]
print("  Squares:", squares)
# Output:
#   Squares: [0, 1, 4, 9, 16]

# 10. While loop with break and continue
print("\nWhile loop with break and continue:")
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue  # Skip when count is 2
    if count == 4:
        break    # Stop loop when count is 4
    print("  count =", count)
# Output:
#   count = 1
#   count = 3

# 11. Looping over a string
print("\nLooping over a string:")
for char in "Python":
    print(" ", char)
# Output:
#   P
#   y
#   t
#   h
#   o
#   n