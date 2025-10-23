# 7-10 - Dream Vacation

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit on place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/n) ").lower()
    if repeat == 'n':
        polling_active = False

print("\n\t------- POLL RESULTS -------")
for name, response in responses.items():
    print(f"\t- {name.title()} would like to visit {response}.")