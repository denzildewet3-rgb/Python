# A Dictionary in a Dictionary
users = {
    "aeinstein" : {
        "first" : "albert",
        "last" : "einstein",
        "location" : "princeton", 
        },

    "mcurie" : {
        "first" : "marie",
        "last" : "curie",
        "location" : "paris",
        },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]

    print(f"\t- Full name: {full_name.title()}")
    print(f"\t- Location: {location.title()}")

# - This code stores information about multiple users in a nested dictionary 
#   and then prints each user’s details.
# - Each username (like "aeinstein" or "mcurie") maps to another dictionary 
#   containing that person’s first name, last name, and location.
# - The program loops through all users, combines their first and last names, 
#   and prints the formatted full name and location.
# - In short: It displays each user’s username, full name, and location in a 
#   neat, readable format.