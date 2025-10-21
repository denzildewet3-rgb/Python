# TRY IT YOURSELF

# 4-1. Pizzas:
pizzas = ["bbq chicken", "spare rib", "tangy russian"]

for pizza in pizzas:
    print(f"I like an extra large {pizza.title()} pizza.")

print(f"\nI really like pizza!")

print("\n")

# 4-2. Animals
animals = ["dog", "cat", "lizzard"]

for animal in animals:
    print(f"this {animal.upper()} would make a great pet")

print("\nAll of these animals would make great pets")

print("\n")

# 4-3 Counting to 20
for value in range(1, 21):
    print(value)

# 4-3 One Million
# for value in range(1, 1000001):
#     print(value)

print("\n")

# 4-5 Summing a million
numbers = list(range(1, 1000001))
print(f"Min = {min(numbers)}")
print(f"Max = {max(numbers)}")
print(f"Sum = {sum(numbers)}")

print("\n")

# 4-6 Odd Numbers
odd_numbers = list(range(1, 20, 2))
for odd_number in odd_numbers:
    print(f"Number is: {odd_number}")

print("\n")

# 4-8 Cubes
cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

print("\n")

# 4-9 Cube Comprehension
cubes = [number **3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

print("\n")

# 4-10 Slices
print(f"The first 3 items in the list are {cubes[:3]}")
print(f"The middle 3 items in the list are {cubes[3:6]}")
print(f"The last 3 items in the list are {cubes[-3:]}")

print("\n")

# 4-11
pizzas = ["bbq chicken", "spare rib", "tangy russian"]

friend_pizzas = pizzas[:]

pizzas.append("regina")
friend_pizzas.append("hawaian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())

print("\n")

# 4-13 Buffet
foods = ("rice", "chicken", "salad", "fish", "fruit")

print("Original buffet menu:")
for food in foods:
    print(food.title())

# foods[0] = "pasta"

foods = ('pasta', 'chicken', 'salad', 'beef', 'dessert')
print("\nRevised buffet menu:")
for food in foods:
    print(food.title())