# 9-10 Imported Restaurant

from restaurant_module import Restaurant

restaurant_1 = Restaurant("spur", "mexican grill")

print("--------------------------------------------------")

print("\t---Accessing Attributes---")

print(f"Thr name of the restaurant is: {restaurant_1.restaurant_name.upper()}")
print(f"They serve {restaurant_1.cuisine_type.upper()}")

print("\n\t---Method calls---")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()