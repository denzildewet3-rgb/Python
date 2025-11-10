import matplotlib.pyplot as plt

from c_random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    # fig, ax = plt.subplots()
    # fig, ax = plt.subplots(figsize=(15, 9))
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.set_aspect('equal')
    
    # Emphasise the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input("Make another walk? (y/n) ")
    if keep_running == 'n':
        break
    

# Chat GPT Summary
# File 1: c_random_walk.py
# Purpose: Defines the RandomWalk class, which creates a series of random steps.
# Key points:
# Uses Random.choice() to determine both direction (+ or -) and distance (0–4 units) for each step.
# Starts every walk at the origin (0, 0) and continues until it reaches the specified number of points (num_points, default 5000).
# Ensures that no step results in no movement (both x and y = 0).
# Stores all x and y coordinates in self.x_values and self.y_values.
# File 2: rw_visual.py
# Purpose: Handles visualization and user interaction for random walks.
# Key points:
# Continuously generates new random walks while the program runs.
# Plots up to 50,000 points per walk using Matplotlib with the "classic" style.
# Colors points using a green gradient (cmap=plt.cm.Greens) to show progression through the walk.
# Highlights:
# Starting point in red.
# Ending point in blue.
# Removes axes for a cleaner visualization.
# Prompts the user (input("Make another walk? (y/n)")) to continue or quit after each walk.