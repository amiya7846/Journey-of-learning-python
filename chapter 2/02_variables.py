# Variable naming rules
# Valid: my_var, _var, var1
# Invalid: 1var, my-var, my var

# valid_variable = 10
# _var = 20 
# var1 = 30


# invalid-variable = 40  # This is invalid because there is - symbol in it
# 1var = 50               # This is invalid because it starts with 1
# my var = 60            # This is invalid because it has white spaces in it
# my.var = 80           # Uncommenting this line will cause a syntax error
# my@var = 90          # Uncommenting this line will cause a syntax error
# my#var = 100         # Uncommenting this line will cause a syntax error
# my$var = 110        # Uncommenting this line will cause a syntax error
# my%var = 120       # Uncommenting this line will cause a syntax error
# my^var = 130      # Uncommenting this line will cause a syntax error
# my&var = 140     # Uncommenting this line will cause a syntax error
# my*var = 150    # Uncommenting this line will cause a syntax error
# my(var) = 160   # Uncommenting this line will cause a syntax error

a = 1
b = 2
print(a + b)  # Output: 3

c = a + b
print(c)  # Output: 3
print("Type of c:", type(c)) # Output: <class 'int'>
#  Here a nad b are the variables and they also called as the identifiers.

