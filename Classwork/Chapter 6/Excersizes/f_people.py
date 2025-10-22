# 6-7
person_1 = {
    "first_name": "john",
    "last_name": "doe",
    "age": 30,
    "city": "cape Town",
}

person_2 = {
    "first_name": "alice",
    "last_name": "smith",
    "age": 25,
    "city": "durban",
}

person_3 = {
    "first_name": "michael",
    "last_name": "brown",
    "age": 40,
    "city": "johannesburg",
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"Full Name: {person["first_name"].title()} {person["last_name"].title()}")
    print(f"Age: {person["age"]}")
    print(f"City: {person["city"].title()}\n")

print("\n")

# 6-8
pet_1 = {
    'animal': 'dog',
    'owner': 'Sarah',
}

pet_2 = {
    'animal': 'cat',
    'owner': 'James',
}

pet_3 = {
    'animal': 'parrot',
    'owner': 'Lerato',
}

pet_4 = {
    'animal': 'rabbit',
    'owner': 'Emily',
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"\nOwner: {pet["owner"].title()}")
    print(f"Animal: {pet["animal"].title()}")

# 6-9
favorite_places = {
    'Alice': ['Paris', 'Rome', 'Cape Town'],
    'Brian': ['New York', 'Tokyo'],
    'Lerato': ['Durban', 'Kruger National Park', 'London'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t- {place}")

