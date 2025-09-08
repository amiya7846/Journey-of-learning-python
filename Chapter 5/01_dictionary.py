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
# city : Bhubaneswar