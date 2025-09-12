# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, this is a file!\n")
    f.write("Second line.\n")
# This creates 'example.txt' and writes two lines to it.

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
# Output:
# Hello, this is a file!
# Second line.

# Appending to a file
with open("example.txt", "a") as f:
    f.write("Third line.\n")
# Adds a new line at the end of the file.

# Reading line by line
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())
# Output:
# Hello, this is a file!
# Second line.
# Third line.