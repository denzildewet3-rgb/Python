# Tests for equality and inequality with strings
fruit = "apple"
print('Is fruit == "apple"? I predict True.')
print(fruit == "apple")

print('\nIs fruit == "banana"? I predict False')
print(fruit == "banana")

# Tests using the lower() method
name = "Denzil"
print('\nIs name.lower() == "denzil"? I predict True.')
print(name.lower() == "denzil")

print('\nIs name.lower() == "DENZIL"? I predict False.')
print(name.lower() == "DENZIL")

# Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age != 30? I predict True.")
print(age != 30)

print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 25? I predict True.")
print(age >= 25)

print("\nIs age <= 24? I predict False.")
print(age <= 24)

# Tests using the and keyword and the or keyword
score = 85
grade = "B"

print('\nIs score > 80 and grade == "B"? I predict True.')
print(score > 80 and grade == "B")

print('\nIs score > 90 or grade == "A"? I predict False.')
print(score > 90 or grade == "A")

# Test whether an item is in a list
colors = ["red", "green", "blue"]
print('\nIs "green" in colors? I predict True.')
print("green" in colors)

print('\nIs "yellow" in colors? I predict False.')
print("yellow" in colors)

# Test whether an item is not in a list
print('\nIs "purple" not in colors? I predict True.')
print("purple" not in colors)

print('\nIs "red" not in colors? I predict False.')
print("red" not in colors)