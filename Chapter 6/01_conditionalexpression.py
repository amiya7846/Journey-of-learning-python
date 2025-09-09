# 1. Simple if-else conditional expression (ternary operator)
a = 10
b = 20
max_value = a if a > b else b
print("Max value is:", max_value)  # Output: Max value is: 20

# 2. Nested conditional expression
x = 5
result = "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
print(result)  # Output: Positive

# 3. Using conditional expression in a function
def is_even(num):
    return "Even" if num % 2 == 0 else "Odd"

print(is_even(7))  # Output: Odd

# 4. Conditional expression with list comprehension
numbers = [1, 2, 3, 4, 5]
parity = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(parity)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# 5. Assigning values based on a condition
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# 6. Conditional expression with multiple variables
a, b = 15, 25
min_value = a if a < b else b
print("Min value is:", min_value)  # Output: Min value is: 15