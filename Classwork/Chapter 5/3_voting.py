# IF Statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

print("\n")

# if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("\n")

# The if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is R0.")
elif age < 18:
    print("Your admission cost is R25.")
else:
    print("Your admission cost is R40.")

# Using Multiple elif Blocks (SAME RESULT AS ABOVE)
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is R{price}.")

# Omitting the else Block
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is R{price}.")

print("\n")

# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

print("\n")

# Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

print("\n")

# Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\n")

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")