# 6-3 & 6-4

glossary = {
    "variable": "A name that stores a value in memory.",
    "loop": "A structure that repeats a block of code while a condition is true.",
    "dictionary": "A collection of key-value pairs in Python.",
    "function": "A block of code that performs a specific task when called.",
    "boolean": "A data type that can have one of two values: True or False.",
    "list": "An ordered collection of items that can be changed (mutable).",
    "tuple": "An ordered collection of items that cannot be changed (immutable).",
    "string": "A sequence of characters enclosed in quotes.",
    "if statement": "A control structure used to make decisions in code.",
    "module": "A file containing Python code that can be imported into other programs.",
}

print("Python Glossary:\n")

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t- {meaning}\n")