# Import Entire Module
# all imports should go on to the top.
# import pizza_module

# pizza_module.make_pizza(16, 'pepperoni', 'mushroom', 'pineapple')
# pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# pizza_module.make_pizza(45, 'mushrooms', 'garlic', 'BBQ ribs', 'fresh green chillies')

# # Importing Specific Functions
# from pizza_module import make_pizza

# make_pizza(22, "black peppers")

# Using as to Give a Function an Alias
from pizza_module import make_pizza as mp

mp(16, "green pepper")

# Using as to Give a Module an Alias
import pizza_module as p

p.make_pizza(100, 'pepperoni', 'cheese')

#Importing All Functions in a Module
from pizza_module import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
