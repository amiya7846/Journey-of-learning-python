# Q1 Add two numbers
a = 1
b = 2
print(a+b)

# Q2 Write a python program to find remainder when a number is divided by another.

a = 15
b = 4
print("Remainder when a is divided by b is :", a%b)

# Q3 Check the type of variables assigned using Input() Function.

a = input("Enter the value of a: ")
print(type(a))

# Q4 show that a is greater than b or not 

a = int(input("Enter the number 1:"))
b = int(input("Enter the number 2:"))

print("a is greater than b is:",a>b)

# Q5 write a program to find the Average of two numbers.

a = int(input("Enter the Number:"))
b = int(input("Enter the Number:"))
print("Average of two numbers is:",(a+b)/2)

# Q6 write a python program to calculate the square of a number entered by the user.

a = int(input("Enter the Number:"))
print("The square of a Number is:",a**a)

# Employee Salary Details

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
designation = input("Enter Designation: ")

basic_salary = float(input("Enter Basic Salary: "))

# Typically, HRA and DA are calculated as a percentage of basic salary
hra = 0.20 * basic_salary   # 20% of basic salary
da = 0.15 * basic_salary    # 15% of basic salary

gross_salary = basic_salary + hra + da

print("\n------ Employee Salary Details ------")
print("Employee ID:", emp_id)
print("Name:", name)
print("Designation:", designation)
print("Basic Salary:", basic_salary)
print("House Rent Allowance (HRA):", hra)
print("Dearness Allowance (DA):", da)
print("Gross Salary:", gross_salary)


# ...existing code...


# Enhanced Employee Salary Details

print("\n" + "="*40)
print("        EMPLOYEE SALARY DETAILS")
print("="*40)

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
designation = input("Enter Designation: ")
department = input("Enter Department: ")
email = input("Enter Email: ")

basic_salary = float(input("Enter Basic Salary: "))

# Allow user to enter HRA and DA percentages, or use defaults
hra_percent = input("Enter HRA % (default 20): ")
hra_percent = float(hra_percent) if hra_percent else 20.0

da_percent = input("Enter DA % (default 15): ")
da_percent = float(da_percent) if da_percent else 15.0

hra = (hra_percent / 100) * basic_salary
da = (da_percent / 100) * basic_salary

# Additional Allowances
ta = 0.10 * basic_salary  # Travel Allowance (10%)
ma = 0.05 * basic_salary  # Medical Allowance (5%)

gross_salary = basic_salary + hra + da + ta + ma

# Deductions
pf = 0.12 * basic_salary  # Provident Fund (12%)
tax = 0.05 * gross_salary # Income Tax (5%)

net_salary = gross_salary - (pf + tax)

print("\n" + "-"*40)
print(f"Employee ID      : {emp_id}")
print(f"Name            : {name}")
print(f"Designation     : {designation}")
print(f"Department      : {department}")
print(f"Email           : {email}")
print("-"*40)
print(f"Basic Salary    : ₹{basic_salary:,.2f}")
print(f"HRA ({hra_percent}%)        : ₹{hra:,.2f}")
print(f"DA ({da_percent}%)         : ₹{da:,.2f}")
print(f"Travel Allowance : ₹{ta:,.2f}")
print(f"Medical Allowance: ₹{ma:,.2f}")
print("-"*40)
print(f"Gross Salary    : ₹{gross_salary:,.2f}")
print(f"Provident Fund  : ₹{pf:,.2f}")
print(f"Income Tax      : ₹{tax:,.2f}")
print("-"*40)
print(f"Net Salary      : ₹{net_salary:,.2f}")
print("="*40)
