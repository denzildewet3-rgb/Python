class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year,):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Set deafult value for attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"\nThis {self.make.title()} {self.model.title()} has {self.odometer_reading} miles on it.")


# Modify attribute value through a method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an Odometer")

# Incrementing an Attribute’s Value Through a Method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# Intitiate car object
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())


# Modifying attribute values directly
my_new_car.odometer_reading = 77856
my_new_car.read_odometer()

# Modify attribute value through a method

my_new_car.update_odometer(50)
my_new_car.read_odometer()


print("\n==============================")

# Incrementing an Attribute’s Value Through a Method
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

print("\n---Update Function---")
my_used_car.read_odometer()
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

print("\n---Increment Function---")
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# CHAT GPT SUMMARY
# The code defines a Car class that models a car with attributes like make, model, year, and odometer_reading.
# Key features:
# __init__() initializes each new car with its make, model, and year, and sets the odometer to 0 by default.
# get_descriptive_name() returns a formatted string describing the car (e.g., “2024 Audi A4”).
# read_odometer() prints the current mileage of the car.
# update_odometer() safely sets the odometer reading to a new value, preventing it from being rolled back.
# increment_odometer() adds a specified number of miles to the odometer.
# Example usage:
# A new Audi A4 (2024) car is created, its odometer is set and displayed.
# A Subaru Outback (2019) car is also created, its mileage is updated and then incremented by 100 miles.
# In short, this code demonstrates object-oriented programming by showing how to create and manipulate car objects with both direct attribute modification and class methods.