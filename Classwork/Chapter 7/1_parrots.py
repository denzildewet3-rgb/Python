# How the input() Function Works

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# -----------------------------------------------------------------------------

# Writing Clear Prompts

# name = input("Please enter your name: ")
# print(f"\nHello, {name.title()}")

# -----------------------------------------------------------------------------

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? " # += append at the end

# name = input(prompt)
# print(f"\nHello, {name.title()}!")

# -----------------------------------------------------------------------------

# Using int() to Accept Numerical Input

# age = input("How old are you? ")
# print(age) # Data type is not a number
# print(type(age)) # type this if you want to see what data type it is

# age = int(age) #type this to change data type from a string to number
# print(type(age))

# if age >= 18: #this will run if the data type is the same
#     print("Access Granted")

# -----------------------------------------------------------------------------
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nSorry, You will be able to ride if you are a little bit older")