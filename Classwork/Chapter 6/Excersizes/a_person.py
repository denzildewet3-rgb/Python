# 6-1
person = {
    "first": "denzil",
    "last": "de wet",
    "age": 35,
    "city": "pretoria",
}

print(f"My name is {person["first"].title()}")
print(f"My last name is {person["last"].title()}")
print(f"My full name is {person["first"].title()} {person["last"].title()}")
print(f"My age is {person["age"]}")
print(f"I live in {person["city"].title()}")

print(f"\nHi, My name is {person["first"].title()} {person["last"].title()},I am {person["age"]} years old and I live in {person["city"].title()}!")