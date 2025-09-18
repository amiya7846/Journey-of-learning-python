# 1. Function: A block of code that performs a specific task and can be reused.

def greet(name):
    print("Hello,", name)

greet("Amiya")  # Output: Hello, Amiya

# 2. Function with return value

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)  # Output: Sum is: 8

# 3. Recursion: A function calling itself to solve a smaller problem.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))  # Output: Factorial of 5 is: 120

# 4. Another recursion example: Fibonacci sequence

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci(6):", fibonacci(6))  # Output: Fibonacci(6): 8

# 5. Function with default arguments

def power(base, exponent=2):
    return base ** exponent

print(power(3))        # Output: 9 (3^2)
print(power(2, 3))     # Output: 8 (2^3)

# 6. Function with variable number of arguments (*args)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(4, 5, 6, 7, 8))  # Output: 30

# 7. Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Amiya", age=21)
# Output:
# name: Amiya
# age: 21

# 8. Recursive function to sum a list
def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

print("Sum of [1,2,3,4]:", recursive_sum([1,2,3,4]))  # Output: 10

# 9. Recursive function to reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print("Reverse of 'python':", reverse_string("python"))  # Output: nohtyp