# 9-15 - Lottery Analysis (Google helped me with this excersize)
from random import choice, sample

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

my_ticket = [1, "B", 5, "E"]

draws = 0
winning_ticket = []

while winning_ticket != my_ticket:
    winning_ticket = sample(lottery, 4)
    draws += 1

print("-------------------------------------")
print("LOTTERY ANALYSIS RESULTS")
print(f"Your ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {draws:,} draws to get a winning ticket!")
print("-------------------------------------")
