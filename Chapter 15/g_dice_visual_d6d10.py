import plotly.express as px
from e_die import Die

# Create a D6 an D10 dice.
die1 = Die()
die2 = Die(10)

# Make some rolls, and store results in a list
results = []
for roll_num in range(50_000):
    result = die1.roll() + die2.roll()
    results.append(result)
    
# Analize the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results
title = "Results of Rolling a D6 and D10 Dice 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.write_html("D6_D10_dice_results.html")
print("Figure saved as dice_results.html, open this file in the browser to view")
        
# print(frequencies)


# Chat GPT Summary
# The program simulates rolling two dice: one with 6 sides and another with 10 sides.
# It rolls both dice 50,000 times to collect a large sample of results.
# For each roll, it adds the two dice values together and stores the total.
# After all rolls, it counts how many times each possible total (from 2 to 16) appears.
# It then creates a bar chart using Plotly Express to show the frequency of each total.
# The x-axis of the chart shows the possible dice totals, and the y-axis shows how often each total occurred.
# The chart visually demonstrates that some totals are more common because there are more combinations that can produce them.
# Finally, the chart is saved as an HTML file, which can be opened in a browser for interactive viewing.