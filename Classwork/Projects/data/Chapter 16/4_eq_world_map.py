from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a python objects
path = Path('mapping_global_datasets/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('mapping_global_datasets/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents, encoding='utf-8')

# Examine all earthquakes in the dataseta.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
    
title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags, color_continuous_scale='Viridis', labels={'color':'Magnitutde'}, projection='natural earth', hover_name=eq_titles)
# fig.show()
fig.write_html("eq_world_map.html")
print("Figure saved as eq_world_map.html - open it in your browser")

# Chat GPT Summary
#  Earthquake Data Visualization Summary
# Imports & Setup:
# Uses pathlib and json to load data, datetime for timestamp conversion, and plotly.express for visualization.
# Data Loading:
# Reads a GeoJSON file (eq_data_30_day_m1.geojson) containing earthquake data and converts it from JSON text into a Python dictionary.
# Data Extraction:
# Loops through each earthquake entry under the "features" key to collect:
# Magnitude (mag)
# Longitude (lon)
# Latitude (lat)
# Title (eq_title)
# Readable time (converted from milliseconds to UTC format)
# Visualization:
# Uses Plotly Express to plot the earthquakes on a world map (scatter_geo):
# Circle size and color represent earthquake magnitude.
# Hover info shows the title and time of each quake.
# The map uses a Natural Earth projection with a “Viridis” color scale.
# Purpose:
# To create an interactive global visualization of recent earthquakes, showing their location, magnitude, and time.