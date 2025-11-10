import plotly.express as px
from e_die import Die

# Create two D6 dice.
die1 = Die()
die2 = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
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
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

fig.write_html("dice_results.html")
print("Figure saved as dice_results.html, open this file in the browser to view")
        
# print(frequencies)