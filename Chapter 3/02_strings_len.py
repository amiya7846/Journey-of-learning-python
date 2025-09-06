name = "Amiya"

# Length of the string
print(len(name))            # 5

# Case conversion
print(name.upper())         # 'AMIYA'
print(name.lower())         # 'amiya'
print(name.capitalize())    # 'Amiya'

# Start/end checks
print(name.startswith('A')) # True
print(name.endswith('a'))   # True

# Find and replace
print(name.find('i'))       # 2 (index of first 'i')
print(name.replace('A', 'E')) # 'Emiya'

# Count occurrences
print(name.count('a'))      # 1

# Alphanumeric checks
print(name.isalpha())       # True
print(name.isdigit())       # False

# Splitting and joining (for demonstration)
full_name = "Amiya Ranjan"
parts = full_name.split()   # ['Amiya', 'Ranjan']
print(parts)
print('-'.join(parts))      # 'Amiya-Ranjan'