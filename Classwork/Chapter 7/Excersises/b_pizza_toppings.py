# 7-4 Pizza topping

prompt = "\nWhich toppings would you like on your pizza? "
prompt += "\n(Type 'quit' when you are done.) "

toppings = []
topping = " "

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        toppings.append(topping)
        print(f"I will add {topping.upper()} to your pizza!")

print("\nThank you for ordering at Denzil's pizzeria!")
print("\nYour pizza will include the following toppings: ")

for t in toppings:
    print(f"\t- {t.title()}")

print("\nYour pizza will be ready soon")