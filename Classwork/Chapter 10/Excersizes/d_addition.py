# 10-6 Addition & 10-7 Addition Calculator
print("Give me 2 numbers, and I will add them together")
print("Enter 'q' to quit\n")

while True:
    first_number = input("First number: ")
    if first_number.lower() == 'q':
        print("Thank you for playing")
        break
    
    second_number = input("Second Number: ")
    if second_number.lower() == 'q':
        print("Thank you for playing")
        break
    
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Oops! you can only enter numbers. Please try again.\n")
        continue
    else:
        print(f"The sum of {first_number} and {second_number} is {result}.")