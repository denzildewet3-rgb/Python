# 10-1 - Learning Python.
from pathlib import Path

path = Path('learning_python.txt')

print("-------------Reading entire file----------------------")

contents = path.read_text()
print (contents.strip())


print("\n-------------Reading lines----------------------")

# lines = contents.splitlines()

for line in contents.splitlines():
    modified_line = line.replace("Python", "C")
    print(line.strip())
        
    print(modified_line)