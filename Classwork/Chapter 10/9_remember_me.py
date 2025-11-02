from pathlib import Path
import json

# Exapmle 1
# username = input("What is your name? ")

# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We'll remember you when you come back, {username}!")

# Example 2
# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")
    
# Example 3 Refactoring
# def greet_user():
#     """Greet the user by name."""
   
#     path = Path('username.json')
   
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

# Example 4
# def get_stored_username(path):
#     """Get stored username if available."""
    
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None

# def greet_user():
#     """Greet the user by name."""

#     path = Path('username.json')
#     username = get_stored_username(path)
    
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

# Example 5
def get_stored_username(path):
    """Get stored username if available."""
    
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""

    name = input("What is your name? ")
    age = input("How old are you? ")
    location = input("Where do you live? ")
    
    username = {"name": name,
                "age": age,
                "location": location}
    
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        print(f"Is this you, {username["name"]}? yes/no")
        answer = input("> ").lower()
        
        if answer == "yes":
            print(f"Welcome back, {username["name"]}!")
            print(f"I remember you're {username["age"]} years old and live in {username["location"]}")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username["name"]}!")

    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username["name"]}!")

greet_user()