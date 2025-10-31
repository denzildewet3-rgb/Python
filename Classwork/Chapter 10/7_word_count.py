# Working with Multiple Files 
from pathlib import Path

def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


# Example 1  
# path = Path('alice.txt')
# count_words(path)

# print("==================================================")

# little_women = Path("text_files/little_women.txt") # Path into another folder
# count_words(little_women)

# print("==================================================")

# Example 2
filenames = ['alice.txt', 'siddhartha.txt', 'text_files/moby_dick.txt', 'text_files/little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)