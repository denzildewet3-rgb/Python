cities = {
    "cape town": {
        "country": "South Africa",
        "population": "4.6 million",
        "fact": "It is home to Table Mountain.",
    },
    "paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Known as the 'City of Light'.",
    },
    "tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "It is the largest metropolitan area in the world.",
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info["country"]}")
    print(f"Population: {info["population"]}")
    print(f"Fact: {info["fact"]}")

# 6-12
cities = {
    "cape town": {
        "country": "South Africa",
        "population": "4.6 million",
        "fact": "It is home to Table Mountain.",
        "landmark": "Table Mountain Cableway",
    },
    "paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Known as the 'City of Light'.",
        "landmark": "Eiffel Tower",
    },
    "tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "It is the largest metropolitan area in the world.",
        "landmark": "Shibuya Crossing",
    },
}

print("\n")

print("\nCity Information:\n" + "-"*50)

for city, info in cities.items():
    print(f"City: {city.title()}")
    for key, value in info.items():
        print(f"{key.title()}: {value}")
    print("-"*50)