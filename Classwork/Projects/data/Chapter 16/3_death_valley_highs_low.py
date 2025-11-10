from pathlib import Path
import csv
import matplotlib.pyplot as plt

from datetime import datetime

#=============================================================================
# Importing and reading simple data form a CSV
#=============================================================================

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# # Printing the headers and their positions
# for index, column_header in enumerate(header_row): 
#     print(index, column_header)
   
# print("\n")
 
# print(header_row)

# Extracting dates, high and low temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
# print(highs)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
# ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel(" ", fontsize=16)
fig.autofmt_xdate() # to prevent overlapping text in cases where txt is too long for the available space and updates the info from the file.
ax.set_ylabel("Temperature (f)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

# Chat GPT Summary
# It imports necessary libraries:
# pathlib to locate and read the CSV file.
# csv to process the file’s data.
# matplotlib.pyplot to create the graph.
# datetime to convert date strings into date objects.
# The program opens the CSV file containing weather data for Death Valley.
# It reads the header row to identify which columns contain the date, high, and low temperatures.
# It then loops through the remaining rows, converting the date strings into Python datetime objects and storing the high and low temperatures in separate lists.
# If any data is missing, it prints a warning message showing which date has missing information.
# Using Matplotlib, it plots the daily high temperatures in red and low temperatures in blue.
# It shades the area between the high and low lines to visually highlight the temperature range.
# The chart includes a title, axis labels, and formatted dates for readability.
# Finally, it displays the graph, showing how temperatures varied throughout the year in Death Valley.