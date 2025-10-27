# Return Values
# 1) Returning a Simple Value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}" # created a variable and combined the first and last name.
#     return full_name.title() #Return the full name varaible

# musician = get_formatted_name('jimi', 'hendrix') #took the value and stored it in a variable
# print(musician) # print the variable of musician

# 2) Making an Argument Optional
# def get_formatted_name(first_name, middle_name, last_name): # specidfies 3 arguments

#     """Return a full name, neatly formatted."""
    
#     full_name = f"{first_name} {middle_name} {last_name}"

#     return full_name.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

def get_formatted_name(first_name, last_name, middle_name=''): #allways put the default value at the end
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('denzil', 'de wet', 'ignatius')
print(musician) 