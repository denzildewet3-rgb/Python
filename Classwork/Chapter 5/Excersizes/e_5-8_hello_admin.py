usernames = ["admin", "denzil", "jaco", "johan", "francois"]

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users")