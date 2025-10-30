# Large Files: One Million Digits
from pathlib import Path

path = Path('pi_ten_million.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(f"{pi_string[:52]}...") # print a slice of this file
print(len(pi_string))