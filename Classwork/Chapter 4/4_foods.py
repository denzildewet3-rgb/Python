my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print(f"My favorite foods are: {my_foods}")
# print(my_foods)

print((f"\nMy friend's favourite foods are: {friends_foods}"))
# print(friends_foods)

my_foods.append('cannoli')
friends_foods.append('ice cream')

print(f"\nMy favorite foods are: {my_foods}")
print((f"\nMy friend's favourite foods are: {friends_foods}"))