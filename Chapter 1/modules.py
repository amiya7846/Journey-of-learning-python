# module 1# with the help of pip we installed the modules in the system and used it like pyjokes
# And with the help of ctrl + / we comment out the line. 

import pyjokes
print ("printing jokes...")
joke =  pyjokes.get_joke()
print(joke)

"""
so thanks 
that was my program

"""
# The above is a multiline comment.

# module2# Another module is pyttsx3 that will speak what we are going to write in the program.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello amiya how are you and welcome to the journey.")
engine.runAndWait()



# module 3# we are using the OS module to print the contains of a directory.
# we have  generated the code using chat gpt.
import os

def list_directory_contents(path):
    if os.path.isdir(path):  # Check if it's a directory
        print(f"Contents of directory '{path}':")
        for item in os.listdir(path):
            print(item)
    else:
        print(f"'{path}' is not a valid directory.")

# Example usage
path = input("Enter the directory path: ")
list_directory_contents(path) # It will print the contents of the directory which we have given in the input..
