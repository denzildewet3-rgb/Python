# Inheritance

#PARENT CLASS/SUPERCLASS
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Simulate fillling up gas tanks."""
        print("Filling up a gas tank")

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"- Inside Battery class\n\t- This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"\t- This car can go about {range} miles on a full charge.")

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------

# CHILD CLASS/SUBCLASS
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. Then initialize attributes specific to an electrica car"""
        super().__init__(make, model, year)
        self.battery = Battery()
        self.battery_size = 40 # Defining attributes and methods for child class

# Defining Attributes and Methods for the Child Class
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"- Inside ElectricCar Class\n\t- This car has a {self.battery_size}-kWh battery.\n")

# Overiding methods from parent class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("\n- Inside ElectricCar class\n\t- This car doesn't have a gas tank!")

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Create instance of childclass/subclass
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

# Defining attributes and methods for child class
my_leaf.describe_battery()
my_leaf.battery.describe_battery()

# Overiding methods from parent class
my_leaf.fill_gas_tank()

# instances as attributes
my_leaf.battery.get_range()

# --------------------------------------------------------------------
#                       Chat GPT Summary
# --------------------------------------------------------------------

# Classes
    # Car (Parent Class / Superclass)
        # Represents a generic car.
        # Attributes:
            # make, model, year, odometer_reading
        
        # Methods:
            # get_descriptive_name(): Returns a formatted car name.
            # read_odometer(), update_odometer(), increment_odometer(): Manage odometer readings.
            #fill_gas_tank(): Simulates refueling.

# Battery
    # Represents a battery for electric cars.
    # Attributes:
        # battery_size (default 40 kWh)
        
        # Methods:
            # describe_battery(): Prints battery size.
            # get_range(): Prints the estimated driving range based on battery size.
            
# ElectricCar (Child Class / Subclass of Car)
    # Represents an electric car with additional features.
    # Inherits all attributes and methods from Car.
    # Adds:
        # battery attribute (instance of Battery)
        # battery_size attribute
        # describe_battery() method (overrides or supplements functionality)
    # Overrides:
        # fill_gas_tank() because electric cars don’t use gas.

# Usage
# Creates an ElectricCar instance (my_leaf) with make, model, and year.
# Demonstrates:
    # Inherited methods (get_descriptive_name())
    # Child class methods (describe_battery())
    # Using Battery class methods (my_leaf.battery.describe_battery(), my_leaf.battery.get_range())
    # Overridden methods (fill_gas_tank())