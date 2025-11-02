# 10-11 Favorite number # 10-12 Favorite Number remembered
from pathlib import Path
import json

path = Path('favorite_number.json')

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number is {favorite_number}.")
else:
    favorite_number = input("what is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print("Your favorite number has been saved")