# Storing Data
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13] # converts data type into a string when using json.dumps

path = Path('numers.json')
contents = json.dumps(numbers) # json.dumps creates a new json file
path.write_text(contents)