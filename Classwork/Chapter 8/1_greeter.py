# Defining a simple Function
def greet_user():  # use the brackets so there can be arguments inserted later.
    """Display a simple greeting.""" # theis a called a "DOCSTRING"
    print("Hello!")

greet_user() # hover over greet_user to display docstring. Call the function.

# Passing Information to a Function

def greet_user(username): # Here we created a username varaible.
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user("denzil")