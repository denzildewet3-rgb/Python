# Version 1 - Conditional test in while statement

prompt = "\nEnter a pizza topping (type 'quit' to stop): "

topping = ""
while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza!")

print("\nYour pizza will be ready soon!")

# Version 2 - Using an active variable

prompt = "\nEnter a pizza topping (type 'quit' to stop): "

active = True  # flag variable
toppings = []

while active:
    topping = input(prompt)
    
    if topping.lower() == 'quit':
        active = False  # change flag to stop the loop
    else:
        toppings.append(topping)
        print(f"I'll add {topping} to your pizza!")

print("\nYou've added these toppings:")
for t in toppings:
    print(f"- {t}")

print("\nYour pizza will be ready soon!")

# Version 3 - Using a break statement

prompt = "\nEnter a pizza topping (type 'quit' to stop): "

toppings = []

while True:
    topping = input(prompt)
    
    if topping.lower() == 'quit':
        break  # immediately exit the loop
    else:
        toppings.append(topping)
        print(f"I'll add {topping} to your pizza!")

print("\nYou've added these toppings:")
for t in toppings:
    print(f"- {t}")

print("\nYour pizza will be ready soon!")
