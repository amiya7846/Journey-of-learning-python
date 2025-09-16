# Creating a dictionary
student = {
    "name": "Amiya",
    "age": 21,
    "branch": "DS"
}

# Accessing values
print(student["name"])      # Output: Amiya

# Adding or updating values
student["age"] = 22
student["city"] = "Bhubaneswar"
print(student)              # Output: {'name': 'Amiya', 'age': 22, 'branch': 'CSE', 'city': 'Bhubaneswar'}

# Removing a key-value pair
student.pop("branch")
print(student)              # Output: {'name': 'Amiya', 'age': 22, 'city': 'Bhubaneswar'}

# Iterating through keys and values
for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Amiya
# age : 22
# city : Bhubaneswar# ...existing code...

# 1. Creating a dictionary with different data types
info = {
    "id": 101,
    "marks": [85, 90, 92],
    "is_passed": True
}
print(info)  # Output: {'id': 101, 'marks': [85, 90, 92], 'is_passed': True}

# 2. Using get() to access values safely
print(student.get("name"))      # Output: Amiya
print(student.get("branch"))    # Output: None (since 'branch' was removed)

# 3. Checking if a key exists
if "city" in student:
    print("City is present")    # Output: City is present

# 4. Getting all keys and values
print(student.keys())           # Output: dict_keys(['name', 'age', 'city'])
print(student.values())         # Output: dict_values(['Amiya', 22, 'Bhubaneswar'])

# 5. Copying a dictionary
student_copy = student.copy()
print(student_copy)             # Output: {'name': 'Amiya', 'age': 22, 'city': 'Bhubaneswar'}

# 6. Removing all items
student_copy.clear()
print(student_copy)             # Output: {}

# 7. Nested dictionary
students = {
    "student1": {"name": "Amiya", "age": 21},
    "student2": {"name": "Riya", "age": 20}
}
print(students["student2"]["name"])  # Output: Riya

# 8. Using setdefault to add a key if not present
student.setdefault("email", "amiya@email.com")
print(student)  # Output: {'name': 'Amiya', 'age': 22, 'city': 'Bhubaneswar', 'email': 'amiya@email.com'}