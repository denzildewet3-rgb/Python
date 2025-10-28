# Creating and Using a Class

# Creating the Dog Class
class Dog: # this starts the calss definition
    """A simple attempt to model a dog."""

    # Construcor

    def __init__(self, name, age): #__init__() is a special method that runs automatically when you create a new dog
        """Initialize name and age attributes."""
        self.name = name # stores the dog's name
        self.age = age # stores the dog's age

    # Methods

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simluate rolling over in response to a command"""
        print(f"{self.name.title()} rolled over!")

# initiate dog object

my_dog = Dog('chico', 11)

print(f"My dog's name is {my_dog.name.title()}")
print(f"My dog is {my_dog.age} years old")

# Calling Method
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
my_dog = Dog('chico', 11)
your_dog = Dog('kloey', 14)

print(f"\nMy dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old")


print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"your dog is {your_dog.age} years old\n")

my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()