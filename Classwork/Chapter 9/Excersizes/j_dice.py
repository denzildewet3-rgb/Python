from random import randint
randint(1, 6)

class Die:
    """A class representing a die witha variable numbner of sides"""
    
    def __init__(self, sides=6):
        """Initialize the die with a default of 6 sides"""
        self.sides = sides
        
    def roll_die(self):
        """Return a random number between 1 and the number of sides"""
        return randint(1, self.sides)

print("--------------------------------------")    

print("Rolling a 6-sided die:")
six_sided = Die()
for roll in range(10):
    print(f"Roll {roll + 1}: {six_sided.roll_die()}")
    
print("--------------------------------------")

print("Rolling a 10-sided die:")
ten_sided = Die(10)
for roll in range(10):
    print(f"Roll {roll + 1}: {ten_sided.roll_die()}")
    
print("--------------------------------------")

print("Rolling a 20-sided die:")
twenty_sided = Die(20)
for roll in range(10):
    print(f"Roll {roll + 1}: {twenty_sided.roll_die()}")
    
print("--------------------------------------")