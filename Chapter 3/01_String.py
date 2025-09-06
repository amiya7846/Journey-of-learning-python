# String is immutable 
# Creating strings
name = "Amiya"
greeting = 'Hello, World!'

# String concatenation
full_greeting = greeting + " My name is " + name

# String length
length = len(full_greeting)

# Accessing characters
first_char = name[0]      # 'A'
last_char = name[-1]      # 'a'

# Slicing strings
first_three = name[:3]    # 'Ami'
print(name[1: ])  # 'miya'
print(name[ :4])  # 'Amiya'

# Changing case
upper_name = name.upper() # 'AMIYA'
lower_greeting = greeting.lower() # 'hello, world!'

# Finding substrings
index = greeting.find('World')    # 7

# Replacing substrings
new_greeting = greeting.replace('World', 'Python') # 'Hello, Python!'

# Splitting strings
words = greeting.split(', ')     # ['Hello', 'World!']

# Stripping whitespace
spaced = "   hello   "
stripped = spaced.strip()        # 'hello'

# Print examples
print(full_greeting)
print("Length:", length)
print("First char:", first_char)
print("Last char:", last_char)
print("First three:", first_three)
print("Uppercase:", upper_name)
print("Lowercase:", lower_greeting)
print("Index of 'World':", index)
print("Replaced:", new_greeting)
print("Words:", words)
print("Stripped:", stripped)


