# Modifying a List in a Function

# EXAMPLE 1
# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#         print(completed_model)

# EXAMPLE 2
# def print_models(unprinted_designs, completed_models):
#       """Simulate printing each design, until none are left. Move each design to completed_models after print."""
      
#       while unprinted_designs:
#             current_design = unprinted_designs.pop()
#             print(f"Printing Model: {current_design}")
#             completed_models.append(current_design)

# def show_completed_models(completed_models):
#       """Show all the models that was printed."""
#       print("\nThe following models have been printed:")
#       for completed_model in completed_models:
#            print(completed_model)


# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# new_designs = ['x', 'y', 'z']
# print_models(new_designs, completed_models)
# show_completed_models(completed_models)

# EXAMPLE 3
# print(f"\n---EXAMPLE 3---\n")

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# copy_of_list = unprinted_designs[:]

# print_models(copy_of_list, completed_models) # Debugging
# show_completed_models(completed_models) # Debugging

# print(f"\nOriginal list: {unprinted_designs}")
# print(f"\nCopy of Original list: {copy_of_list}")

# CHAT GPT Summary

# This program simulates a 3D printing process using two functions:
# print_models() removes each design from the unprinted_designs list, simulates printing it, and moves it to completed_models.
# show_completed_models() displays all models that have been printed.
# In the examples, different sets of designs are printed and added to the same completed_models list.
# Finally, the code shows that:
# Passing the original list lets the function modify it directly (it becomes empty).
# Passing a copy of the list (unprinted_designs[:]) protects the original list from changes.

from printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)