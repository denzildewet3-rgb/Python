# Looping Through a Dictionary

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items(): # goes through each KEY and VALUE in a dictionary and then print each users information
    print(f"\nKey: {key}")
    print(f"Value: {value}\n")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

print("\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("\n")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take your poll")

print("\n")

# Looping Through a Dictionary’s Keys in a Particular Order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

print("\n")

# Looping Through All Values in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages that have been mentoined")
for language in favorite_languages.values():
    print(language.title())

print("\nUnique values")

for language in set(favorite_languages.values()):  # set removes doubles in a list (only take unique values)
    print(language.title())