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