# Using a Function with a while Loop

def get_formatted_name(first_name, last_name): # Defines a function named get_formatted_name that takes two parameters: first_name and last_name.
    """Return a full name, neatly formatted.""" # A docstring that describes what the function does.
    full_name = f"{first_name} {last_name}" # Uses an f-string to join the first and last names with a space between them, storing the result in full_name.
    return full_name.title() # Calls the string method,  The function returns this nicely formatted name to the caller.

while True: # Starts an infinite loop. The loop runs until a break statement stops it.
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ") # Shows First name: and waits for the user to type something and press Enter. The typed string is saved in f_name.
    if f_name == 'q': # If the user typed exactly 'q' for the first name, the break ends the while loop (program quits).
        break
    
    l_name = input("Last name: ") 
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name) # Calls the function defined earlier, passing the values the user entered. The returned nicely-formatted name is stored in formatted_name.
    print(f"\nHello, {formatted_name}!") # Prints a greeting that includes the formatted name. The \n inserts a blank line above the greeting.