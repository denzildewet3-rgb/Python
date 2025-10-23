# Moving Items from One List to Another

# Start with users that need to be verified, and an empty list to hold confirmed users.
# unconfirmed_users = ["alice", "brian", "candace"]
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(f"\t- {confirmed_user.title()}")

# -----------------------------------------------------------------------------
# Removing All Instances of Specific Values from a List
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(f"\nOriginal list: {pets}")

# while 'cat' in pets:
#     pets.remove('cat')
#     print(f"\t- {pets}")

# print(f"\nUpdated list: {pets}\n")

# -----------------------------------------------------------------------------
# Filling a Dictionary with User Input

responses = {} # creating a empty dictionary
polling_active = True # set a flag to indicate that polling is active

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/n) ")
    if repeat == 'n':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"\t- {name.title()} would like to climb {response}.\n")

# Chat GPT Summary
# This program conducts a simple poll asking users which mountain they would like to climb.
# It starts with an empty dictionary (responses) to store names and their answers.
# The while loop keeps running as long as polling_active is True.

# Inside the loop:
# The program asks for the user’s name and their desired mountain.
# It then stores this information in the dictionary (responses[name] = response).
# The user is asked if another person wants to respond; if they type 'n', polling stops.
# After polling ends, the program prints all the collected responses, showing which mountain each person wants to climb.