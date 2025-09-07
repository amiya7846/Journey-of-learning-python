# Creating a list with mixed data types
my_list = [1, "hello", 3.14, True]
print(my_list)  # Output: [1, 'hello', 3.14, True]

# Slicing a list
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # Output: [20, 30, 40]
print(numbers[:3])    # Output: [10, 20, 30]
print(numbers[::2])   # Output: [10, 30, 50]

# Concatenating and repeating lists
a = [1, 2, 3]
b = [4, 5]
print(a + b)          # Output: [1, 2, 3, 4, 5]
print(a * 2)          # Output: [1, 2, 3, 1, 2, 3]

# Checking if an item exists in a list
print(20 in numbers)  # Output: True
print(100 in numbers) # Output: False

# Sorting a list
unsorted = [3, 1, 4, 2]
unsorted.sort()
print(unsorted)       # Output: [1, 2, 3, 4]

# Reversing a list
unsorted.reverse()
print(unsorted)       # Output: [4, 3, 2, 1]

# Copying a list
copy_list = numbers.copy()
print(copy_list)      # Output: [10, 20, 30, 40, 50]

# Clearing a list
copy_list.clear()
print(copy_list)      # Output: []

# Nested lists (list inside a list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])   # Output: 6 (row 2, column 3)