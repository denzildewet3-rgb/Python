# 9-7 Admin
#-----------------------------------------------------------------------
#                              Parent Class/Super Class
#-----------------------------------------------------------------------
class User:
    "A simple attempt to model a user profile"

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize the user's profile attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        """Print asummary of the user's information"""
        print(f"User Profile:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
        print(f"Occupation: {self.occupation.title()}")

    def greet_user(self):
        """Print a personlized greeting to user"""
        print(f"\nHello, {self.first_name.title()}! Welcome back!")
        print("-------------------------------------------")

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attemps to 0"""
        self.login_attempts = 0
        
#-----------------------------------------------------------------------
#                              Child Class
#-----------------------------------------------------------------------
class Admin(User):
    """Represent an admin user with special privileges."""
    
    def __init__(self,first_name, last_name, age, location, occupation):
        """Initialize attributes of the parent class, then admin-specific ones"""
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = ["can add post", "can delete post", "can ban user", "can modify settings"]
        
    def show_privileges(self):
        """Display the admin's privileges."""
        print(f"\nAdmin Privilages for {self.first_name.title()}")
        for privilege in self.privileges:
            print(f"- {privilege}")   
    
    
#-----------------------------------------------------------------------
#                              
#-----------------------------------------------------------------------

user1 = User("denzil", "de wet", 35, "pretoria", "programmer")
user2 = User("jean-claude", "van damme", 48, "hollywood", "actor")
user3 = User("eben", "etsebeth", 30, "durban", "rugby player")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

print(f"Initial login attemps: {user1.login_attempts}")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()


print(f"Login attempts after incrementing: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")

print("-------------------------------------------")
admin_user = Admin("denzil", "de wet", 35, "cape town", "programmer")
admin_user.describe_user()
admin_user.show_privileges()
print("-------------------------------------------")