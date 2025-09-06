# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Accessing elements
print(fruits[0])      # Output: apple
print(fruits[-1])     # Output: mango

# Modifying elements
fruits[1] = "orange"
print(fruits)         # Output: ['apple', 'orange', 'cherry', 'mango']

# Adding elements
fruits.append("grape")
print(fruits)         # Output: ['apple', 'orange', 'cherry', 'mango', 'grape']

# Inserting at a specific position
fruits.insert(2, "kiwi")
print(fruits)         # Output: ['apple', 'orange', 'kiwi', 'cherry', 'mango', 'grape']

# Removing elements
fruits.remove("orange")
print(fruits)         # Output: ['apple', 'kiwi', 'cherry', 'mango', 'grape']

# Popping the last element
last_fruit = fruits.pop()
print(last_fruit)     # Output: grape
print(fruits)         # Output: ['apple', 'kiwi', 'cherry', 'mango']

# List length
print(len(fruits))    # Output: 4

# Iterating through a list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# kiwi