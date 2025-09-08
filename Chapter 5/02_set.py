# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)               # Output: {'banana', 'cherry', 'apple'} (no duplicates)

# Adding elements
fruits.add("mango")
print(fruits)               # Output: {'banana', 'cherry', 'apple', 'mango'}

# Removing elements
fruits.remove("banana")
print(fruits)               # Output: {'cherry', 'apple', 'mango'}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))           # Output: {1, 2, 3, 4, 5}
print(a.intersection(b))    # Output: {3}
print(a.difference(b))      # Output: {1, 2}