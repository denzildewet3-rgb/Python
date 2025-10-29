# 9-14 Lottery (Google helped me with this code)
from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

winning_ticket = []
for i in range(4):
    picked_item = choice(lottery)
    winning_ticket.append(picked_item)
    
print("-------------------------------------")
print("LOTTERY DRAW RESULTS")
print("Your winning ticket is:", winning_ticket)
print("Any ticket matching these 4 numbers or letters wins a prize!")
print("-------------------------------------")