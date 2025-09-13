# Object-Oriented Programming (OOPs) in Python

# 1. Defining a class
class Student:
    # Constructor (initializer)
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# 2. Creating objects (instances) of the class
student1 = Student("Amiya", 21)
student2 = Student("Riya", 20)

# 3. Accessing attributes and methods
print(student1.name)      # Output: Amiya
student1.greet()          # Output: Hello, my name is Amiya and I am 21 years old.
student2.greet()          # Output: Hello, my name is Riya and I am 20 years old.

# 4. Inheritance example
class GraduateStudent(Student):
    def __init__(self, name, age, degree):
        super().__init__(name, age)  # Call parent constructor
        self.degree = degree

    def show_degree(self):
        print(f"{self.name} has a degree in {self.degree}.")

grad = GraduateStudent("Amiya", 21, "Computer Science")
grad.greet()              # Output: Hello, my name is Amiya and I am 21 years old.
grad.show_degree()        # Output: Amiya has a degree in Computer Science.