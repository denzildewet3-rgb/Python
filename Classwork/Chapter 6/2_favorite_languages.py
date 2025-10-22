# A Dictionary of Similar Objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

language = favorite_languages["sarah"].title() 
print(f"Sarah's favorite language is {language}.\n") # The code retrieves Sarah’s favorite language using favorite_languages["sarah"] and prints it in title case

# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # The code tries to access a non-existent key 'points'.

point_value = alien_0.get("points", "No Point Value Assigned.") # Instead of causing an error, get() safely returns a default message: "No Point value exists" (or whatever message you specify).

print(alien_0.get("points", "No Point value exists\n")) #example of how to print without creating a variable.