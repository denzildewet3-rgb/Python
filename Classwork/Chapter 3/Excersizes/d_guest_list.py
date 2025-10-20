guest_list = ["Francois", "Dwayne", "Bob"]

print(f"Dear {guest_list[0]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[1]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[2]}, You are invited to a special dinner at my house!")

print(f"\nUnfortunatly, {guest_list[0]}, can't make dinner tonight")

guest_list[0] = "Solly"

print(f"\nHere are the new Invitations")

print(f"\nDear {guest_list[0]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[1]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[2]}, You are invited to a special dinner at my house!")

# More Guests
print("\nGood News! I have found a bigger dinner table, so I can invite more guests")

guest_list.insert(0, "Williams")
guest_list.insert(2, "Kramer")
guest_list.append("Sylvia")

print("\nHere are the new invitations")

print(f"\nDear {guest_list[0]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[1]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[2]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[3]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[4]}, You are invited to a special dinner at my house!")
print(f"Dear {guest_list[5]}, You are invited to a special dinner at my house!")

print("\n")
# Shrinking the guest List
print("\nUnfortunately, the table did not arrive in time and I have to uninvite a few people")

popped_guest = guest_list.pop()
print("\n")
print(f"Sorry {popped_guest}, I can't invite you to dinner")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner")

print(f"\nDear {guest_list[0]}, You are still invited to the special dinner at my house!")
print(f"Dear {guest_list[1]}, You are still invited to the special dinner at my house!")

del guest_list[0]
del guest_list[0]
del guest_list[0]


print("\nMy Guest list is now empty")
print(guest_list)