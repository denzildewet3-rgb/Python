# 7-5
prompt = ("How old are you? ")

age = int(input(prompt))

if age <= 3:
    print("\nYour movie ticket will be free")
elif age <= 12:
    print("\nYour movie ticket price will be R 10")
else:
    print("\nyour movie ticket price will be R 15 ")