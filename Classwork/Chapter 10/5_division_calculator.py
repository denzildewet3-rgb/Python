# Handling the ZeroDivisionError Exception
# Using try-except Blocks

# try:
#     print(5/0)
# except ZeroDivisionError: # handling the ZeroDivisionError exception looks like:
#     print("You can't divide by zero!")
    
# print("\nExceptions are interesting")

# Using Exceptions to Prevent Crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
# The else Block
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
        
    else:
        print(answer)