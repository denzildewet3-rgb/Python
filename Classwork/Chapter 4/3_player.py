# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])

print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
print(players[:4])

# Last Index position
print(players[2:])

print(players[-3:])

print("\n")

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())