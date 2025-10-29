# Importing Multiple Classes from a Module
# from car_module import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# Importing an Entire Module into a Module
# import car_module as cm # cm Using Aliases - short for car_module

# my_mustang = cm.Car('ford', 'mustang', 2024) # .Car refers to the class in that module
# print(my_mustang.get_descriptive_name())

# my_leaf = cm.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# Importing All Classes from a Module
from car_module import *

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())