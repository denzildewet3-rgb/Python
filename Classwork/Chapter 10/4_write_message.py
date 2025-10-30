# Writing to a File

from pathlib import Path

# Writing Multiple Lines
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt') # this created a txt file
# path.write_text("I love programming.") # Writing a Single Line # This text was added in the file

path.write_text(contents)