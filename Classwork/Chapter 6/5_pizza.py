# A List in a Dictionary
# Example 1
# Store information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']} - crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t- {topping}")

# Example 2 - loop through lists in a dictionary
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

# Print the entire dictionary inside a for loop.
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t- {language.title()}")