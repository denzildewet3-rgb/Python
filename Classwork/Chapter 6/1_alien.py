# Simple Dictionary
alien_0 = {"color": "green", "points": 5} # creates a dcitionary with 2 key value pairs "colors" and "points"

print(alien_0["color"]) # Prints the values
print(alien_0["points"]) # Prints the values

new_points = alien_0["points"]
print(f"You just earned {new_points} points\n") # Prints the values an displays a message of points earned

# Adding New Key-Value Pairs
alien_0 = {"color": "green", "points": 5}
print(f"Original Dictionary: \n{alien_0}\n") # prints the dictionary before the update

alien_0["x_position"] = 0 # adds new keys x and y_position
alien_0["y_position"] = 25
print(f"Updated Dictionary:\n{alien_0}\n") # prints the dictionary after the update

# Starting with an Empty Dictionary
alien_0 = {}

alien_0["color"] = "green"
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary
# Example 1
alien_0 = {'color': 'green'}
print(f"\nThe alien is {alien_0['color']}.")

alien_0["color"] = "yellow" # Shows how to change an existing value (changes the alien’s color from green to yellow).
print(f"The alien is now {alien_0["color"]}.\n")

# Example 2
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0["x_position"]}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0["speed"] == "slow": # Demonstrates using dictionary data to calculate a new position based on the alien’s speed.
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New X position: {alien_0['x_position']}\n")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0["points"] # Deletes a specific key (points) from the dictionary and prints the result.
print(alien_0)