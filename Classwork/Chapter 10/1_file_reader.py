# Reading the Contents of a File
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

contents = contents.rstrip()
print(contents)
print("--------------------------------------")

lines = contents.splitlines() # Accessing a files lines
for line in lines:
    print(f"- {line}")
print("--------------------------------------")

# Working with a File’s Contents
lines = contents.splitlines()
pi_string = '' 
for line in lines:
    pi_string += line.lstrip()
    
print(pi_string)
print(len(pi_string))