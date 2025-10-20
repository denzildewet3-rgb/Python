# Modifying elements on a list
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

motorcycles[0] = "Ducati"
print(motorcycles)

# Adding elements to a list
# Append method
motorcycles = ["Honda", "Yamaha", "Suzuki"]
motorcycles.append("Ducati")
print(motorcycles)


motorcycles = []
print(motorcycles)
motorcycles.append("Honda")
motorcycles.append("Yamaha")
motorcycles.append("Suzuki")
motorcycles.append("Ducati")
print(motorcycles)

# Inserting a element into a list
motorcycles = ["Honda", "Yamaha", "Suzuki"]
motorcycles.insert(0, "Ducati")
print(motorcycles)

print("\n")
# Removing elments from a list using the del statement
motorcycles = ["Honda", "Yamaha", "Suzuki"]
del motorcycles[1]
print(motorcycles)

print("\n")
# Removing an elmenent using the pop() method
motorcycles = ["Honda", "Yamaha", "Suzuki"]
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"Popped Motorcycle: {popped_motorcycle}\nNew List {motorcycles}")

print("\n")
# Popping Items from Any Position in a List
motorcycles = ["Honda", "Yamaha", "Suzuki"]
second_owned = motorcycles.pop(1)
print(f"The second motorcycle I owned was a {second_owned.title()}")

print("\n")
# Removing an intem by value
motorcycles = ["honda", "yamaha", "Suzuki"]
print(motorcycles)

motorcycles.remove("honda")
print(motorcycles)

# To expensive
motorcycles.append("Ducati")
print(motorcycles)

too_expensive = "Ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me. \nMy current wishlist is now a {motorcycles}")