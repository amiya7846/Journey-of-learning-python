#Q1:-
name = input("Enter your name: ")
print(f"Good Night, {name}") # Using f-string for formatted output

# Q2:-
letter = '''Dear <|NAME|>,
You are selected!
Have a great day ahead!
Date: <|DATE|>'''

letter = letter.replace("<|NAME|>", name).replace("<|DATE|>", "20th June 2023") #This is called chaining of methods
print(letter)

# Q3:-
name = "Amiya is a good boy  and  "
print(name.find("  ")) #Output: 16 (index of first occurrence of double space)
# The above program is used to find the index of the first occurrence of double spaces in the string.

# Q4:-
print(name.replace("  ", " ")) #Output: Amiya is
print (name) #Strings are immutable which means that you cannot change them by running functions on them.


