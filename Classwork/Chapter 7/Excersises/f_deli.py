# 7-8 Deli
# sandwich_orders = ["chicken mayo", "tuna", "bacon & cheese", "egg", "cheese", "cheese & tomato"]

# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop(0)
#     print(f"I made your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\nAll sandwiches have been made:")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich.title()} sandwich")
# ----------------------------------------------------------------------------
# 7-9 No Pastrami
sandwich_orders = ["chicken mayo", "tuna", "pastrami", "bacon & cheese", "egg", "pastrami", "cheese", "cheese & tomato", "pastrami"]

finished_sandwiches = []

print("Sorry, the deli has run out of pastrami sandwiches\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"\t- {sandwich.title()} sandwich")