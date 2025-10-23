# 7-1 Rental Car
# car = input("What kinf of rental car would you like? ")
# print(f"\nLet me see if I can find a {car.title()}.")

# 7.2 Restaurant Seating
# seating = input("How many people are you in your dinner group? ")
# seating = int(seating)

# if seating >= 8:
#     print(f"\nYou will have to wait for a table for {seating} seats.")
# else:
#     print(f"\nYou're table with {seating} seats is ready")

# 7.3 Multiples of 10
number = input("Enter a number between 1 and 1000 ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nThe number {number} is not a multiple of 10.")