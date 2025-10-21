# Numerical Comparisons
age = 18
print(f"is the person alteast 18 years old?: {age == 18}")

age = 19
print(f"is the person alteast below 21 years of age?: {age < 21}")
print(f"is the person alteast below 21 years old or younger?: {age <= 21}")
print(f"is the person alteast above 21 years old?: {age > 21}")
print(f"is the person alteast 21 years old?: {age >= 21}")

print("\n")

# Checking Multiple Conditions
# 1) Using and to Check Multiple Conditions
age_0 = 22
age_1 = 21

admission = age_0 >= 21 and age_1 >= 21
print(f"Are both patrons allowed to purchase?: {admission}")

# 2) Using or to Check Multiple Conditions
age_0 = 21
age_1 = 18

admission = age_0 >= 21 or age_1 >= 21
print(f"can they enter the movie theatre?: {admission}")

print("\n")

# Checking Whether a Value Is in a List
requested_toppings = ["mushrooms", "onions", "pineapple"]
print(f"Add Mushrooms for order?: {"mushrooms" in requested_toppings}")
print(f"Add Pepperoni's for order?: {"pepperoni" in requested_toppings}")

print("\n")

# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"{user.title()}, you are not Authorized to access the page")

# Boolean Expressions
game_active = True
can_edit = False