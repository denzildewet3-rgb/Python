name = "denzil ignatius de wet"
# Print the first letter in capital letters
print(name.title())

print(name.upper())
print(name.lower())

first_name = "denzil"
last_name = "de wet"
full_name = f"{first_name} {last_name}"
print(f"Hello, my name is {full_name.title()}, how are you doing?")

print("Python")
# Print with a tab
print("\tPython")

# print in different lines and tabs
print("Languages:\n\tPython\n\tC\n\tJavaScript\n\tHTMX")

# Stripping Whitespace
print("\n")
favorite_language = " python    "
favorite_language
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

# Removing prefixes

nostarch_url = "https://nostarch.com"
print(nostarch_url)
nostarch_url.removeprefix("https://")
print(nostarch_url)