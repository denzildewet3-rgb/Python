# Creating a list
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# Accessing elements in a list
print(f"First element in the list: {bicycles[0].title()}")
print(f"Fourth element in the list: {bicycles[3].title()}")

print(f"Last element in the list: {bicycles[-1].title()}")
print(f"Second last element in the list: {bicycles[-2].title()}")

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)