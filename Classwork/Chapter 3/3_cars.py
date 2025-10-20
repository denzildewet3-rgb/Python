# Sorting the list permanently using the sort() method
# Alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

print("\n")

# Reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


print("\n")
# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Original list: {cars}")
print(f"1) Sorted list: {sorted(cars)}")
print(f"After sorted method: {cars}")

print("\n")
# Printing a List in Reverse aplhabetical Order
sorted_cars = sorted(cars, reverse=True)
print(f"2) Sorted list: {sorted_cars}")

# Printing a list in reverse order
print("\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Reversed list: {cars}")

cars.reverse()
print(f"Reversed list: {cars}")

# Finding the Length of a List
print(f"Length of cars list: = {len(cars)}")
