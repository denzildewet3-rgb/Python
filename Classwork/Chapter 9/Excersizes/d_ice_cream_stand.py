# 9-6 Ice Cream Stand
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

# Child Class
class IceCreamStand(Restaurant):
    """Represents the ice cream stand, a specific kind of restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        """Initialize attributes of the parent class. Then initialize attributes to an ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "mint"]

    def display_flavours(self):
        """Display the list of available ice cream flavours"""
        print(f"\n{self.restaurant_name} offers the following ice cream flavors:")
        for flavour in self.flavors:
                print(f"\t- {flavour.title()}")
                
                
# Instantiate instance of class
restaurant_1 = Restaurant("spur", "mexican grill")

print("\n\t---Accessing Attributes---")

print(f"The name of the restaurant is: {restaurant_1.restaurant_name.upper()}") 
print(f"They serve {restaurant_1.cuisine_type.upper()}")  

print("\n\t---Method Calls---")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

print("--------------------------------------------")
my_ice_cream_stand = IceCreamStand("Frosty delights")

my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavours()
print("--------------------------------------------")

#=============================================================================
#=============================================================================

#9-3 Three restaurants

restaurant_2 = Restaurant("ocean basket", "seafood")
restaurant_3 = Restaurant("smoke house", "smoked meat")

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()