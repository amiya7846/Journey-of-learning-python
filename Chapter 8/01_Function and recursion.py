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