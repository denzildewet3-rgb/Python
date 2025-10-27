# 8-5
# def describe_city(city='new york', country='united states of america'):
#     """Display the information of a city and the country it is in"""
#     print(f"{city.title()} is in {country.title()}")

# describe_city()
# describe_city(city='paris', country='france')
# describe_city('cape town', 'south africa')

# 8-6 City Names
def city_country(city, country):
    """Return a city and country, neatly formatted"""
    return f"{city.title()}, {country.title()}"

city1 = city_country('california', 'united states of america')
city2 = city_country('cape town', 'south africa')
city3 = city_country('tokyo', 'japan')

print(city1)
print(city2)
print(city3)