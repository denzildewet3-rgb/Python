# 8-14
def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    
    car = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }

    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('ford', 'ranger', color='white', capabilities='4x4', tow_package=True)

print(car)