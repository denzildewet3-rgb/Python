places = ["USA", "Canada", "ZAR", "Phuket", "Indonesia"]
print("original order")
print(places)

print("\nAlphabetical Order")
print(sorted(places))

print("\nStill in orignal order:")
print(places)

places.reverse()
print("\nReversed order")
print(places)

places.reverse()
print("\nBack to original order")
print(places)

places.sort()
print("\nSorted in Alphabetical order")
print(places)

places.sort(reverse=True)
print("\nSorted in reverse alphabetical order")
print(places)