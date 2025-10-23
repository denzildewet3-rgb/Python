# Introducing while Loops 
# (while loop runs as long as, or while, a certain condition is true. )

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1 #once it is greater than 5 exit the loop

#------------------------------------------------------------------------------
# Letting the User Choose When to Quit
# prompt = "\nTell me something, and I will repeat it back to you: " # creating a prompt varaible
# prompt += "\nEnter 'quit' to end the program: " # 

# message = " " # Declare empty variable
# while message != "quit": # While message is not equal to quit stay in the loop
#     message = input(prompt) # Message is holding the value, if message is quit, break out of the while loop.
#     if message != "quit": # this does not print a message of quit
#         print(f"\nMessage = {message}")

#------------------------------------------------------------------------------
# Using a Flag
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True # Flag is called active
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(f"\nMessage = {message}")

#------------------------------------------------------------------------------
# Using break to Exit a Loop

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True: # While loop will run if the condition is true
#     city = input(prompt)

#     if city == 'quit':
#         break # the loop will break when user inputs 'quit'
#     else: # otherwise the message will print and return to the first prompt
#         print(f"\nI'd love to go to {city.title()}!")

#------------------------------------------------------------------------------
# Using continue in a Loop

current_number = 0 # current_number starts at 0.
while current_number < 10: # The while loop runs as long as current_number < 10.
    current_number += 1 # Inside the loop, current_number increases by 1 each time.
    if current_number % 2 == 0: # The if statement checks if the number is even (current_number % 2 == 0).
        continue # If it is even, the continue statement makes the program skip the rest of the loop and go straight to the next iteration.

    print(current_number)


