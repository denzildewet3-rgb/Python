# Import the whole module
import greetings
greetings.say_hello('Pieter')

# Import the function directly
from greetings import say_hello
say_hello('Jaco')

# Import the function with an alias
from greetings import say_hello as greet
greet('Charlie')

# Import the module with an alias
import greetings as gr
gr.say_hello('Denzil')

# Import all functions from the module
from greetings import *
say_hello('Machiel')
