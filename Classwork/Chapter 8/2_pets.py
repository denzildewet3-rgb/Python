# Passing Arguments
# # 1) Positional Arguments

# def describe_pet(animal_type, pet_name): # order is important, when you call this as well.
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet("hamster", "harry") # Calling the function, hamster refers to animal_type and harry refers to pet_name

# # 2) Keyword Arguments
# describe_pet(animal_type="dog", pet_name="jack russel") # Identify the keywords, you can mix the order if you use this.
# describe_pet(pet_name="snowy", animal_type="cat")

# 3) Default Values
def describe_pet(pet_name, animal_type='dog'): # deafult values should always be at the end
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='willie') 
# describe_pet('willie')
# describe_pet(pet_name='harry', animal_type='hamster') #Override values that inserted in line 16.

# # 4)Equivalent Function Calls
describe_pet('willie')
describe_pet(pet_name='willie')

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# describe_pet() # This will give an error becuase no value was specified.