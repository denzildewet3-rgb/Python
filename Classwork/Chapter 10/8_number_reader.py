from pathlib import Path
import json

path = Path('numbers.json') 
contents = path.read_text() # reads the text in the file and stores it in a varaible
numbers = json.loads(contents) # json.loads an existing json file

print(numbers)
print(type(numbers)) # when you ues json.loads it converts back to the original data type which is a list
print(type(contents)) # json.dumps method converts the data type into a string