a = input("Enter number 1:")
b = input("Enter number 2:")
# We can use alt + shift + downarrow to replicate the same line
print("Number a is:",a)
print("Number a is:",b)

print("sum is :",a+b)
# Here in this example the compiler takes the number as string and concatinate the both numbers

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
print("Number a is:",a)
print("Number a is:",b)

print("sum is :",a+b)
# Here we specify that it is an integer type so it will now add both the Nos.


# Student Marks Details
sid = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")
branch = input("Enter Branch: ")

print("Enter Test1, Test2, and Test3 marks")
t1,t2,t3 = float(input()),float(input()),float(input())
avg = (t1 + t2 + t3) / 3
print ("----------------Student Marks Details---------------")
print("Student Id:",sid)
print("Name:",name)
print("Branch:",branch)
print("Marks:",t1,t2,t3)
print("Average Marks:",avg)
