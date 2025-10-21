# Simple IF Statements
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


print("\n")
# Checking for Equality
car = "bmw"
print(f"Is the car a bmw? {car == "bmw"}")
car = "audi"
print(f"Is the car a bmw? {car == "bmw"}")

# CASE sensistivity
car = "Audi"
print(f"Is the car a audi? {car == "audi"}")
print(f"Is the car a audi? {car.lower() == "audi"}")

print("\n")

# Checking for Inequality
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")