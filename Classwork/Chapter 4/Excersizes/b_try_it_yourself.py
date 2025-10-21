# Tuples - Python refers to values that cannot change as TUPLE
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250,
print("\n")

# Looping Through All Values in a Tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

# Override tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Numerical Lists
# Using range() functions
for value in range(1, 5):
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

print("\n")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print("\n")
squares = []
for value in range (1, 12):
    # square = value **2
    squares.append(value ** 2)
print(squares)

print("\n")
# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Min = {min(digits)}")
print(f"Max = {max(digits)}")
print(f"Sum = {sum(digits)}")

print("\n")
# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your slice
# at the beginning of the list:
print(players[:4])

# Last Index position
print(players[2:])
print(players[-3:])

print("\n")
# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())