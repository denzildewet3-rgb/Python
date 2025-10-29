# 9-10 Imported Restaurant
class Restaurant:
    """A class that models a Restaurant types"""

# Constructor

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes an instance of a restaurant class"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print description of restaurant incl name & cuisine type."""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} food")

    def open_restaurant(self):
        """Indicates that the restaurant is open"""
        print(f"{self.restaurant_name.title()} is now open for business")

# Instantiate instance of class
restaurant_1 = Restaurant("spur", "mexican grill")

print("\n\t---Accessing Attributes---")

print(f"The name of the restaurant is: {restaurant_1.restaurant_name.upper()}") 
print(f"They serve {restaurant_1.cuisine_type.upper()}")  

print("\n\t---Method Calls---")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

#=============================================================================
#=============================================================================

restaurant_2 = Restaurant("ocean basket", "seafood")
restaurant_3 = Restaurant("smoke house", "smoked meat")

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
