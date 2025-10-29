# 9-1 Restaurant & 9-4 Number served
class Restaurant:
    """A class that models a Restaurant types"""

# Constructor

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes an instance of a restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print description of restaurant incl name & cuisine type."""
        print(f"- {self.restaurant_name.title()} serves {self.cuisine_type.title()} food")

    def open_restaurant(self):
        """Indicates that the restaurant is open"""
        print(f"- {self.restaurant_name.title()} is now open for business")

    def set_number_served(self, number):
        """Set the number of customers that have been served"""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Add to the total number of customers served."""
        self.number_served += additional_customers

# Instantiate instance of class
restaurant_1 = Restaurant("spur", "mexican grill")

print("\n\t---Accessing Attributes---")

print(f"- The name of the restaurant is: {restaurant_1.restaurant_name.upper()}") 
print(f"- They serve {restaurant_1.cuisine_type.upper()}")  

print("\n\t---Method Calls---")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

#=============================================================================
#=============================================================================

#9-3 Three restaurants

restaurant_2 = Restaurant("ocean basket", "seafood")
restaurant_3 = Restaurant("smoke house", "smoked meat")

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print("----------------------------------------------------------------")
print(f"Number of customers served: {restaurant_1.number_served} (Original value)")

restaurant_1.number_served = 25
print(f"Number of customers served: {restaurant_1.number_served} (Updated directly)")

restaurant_1.set_number_served(100)
print(f"Number of customers served: {restaurant_1.number_served} (After using set_number_served)")

restaurant_1.increment_number_served(50)
print(f"Number of customers served: {restaurant_1.number_served} (afer incrementing)")

print("----------------------------------------------------------------")