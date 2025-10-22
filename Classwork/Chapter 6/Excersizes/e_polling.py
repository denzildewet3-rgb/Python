# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'denzil', 'michelle', 'phil']

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for taking the poll")
    else:
        print(f"{person.title()}, please take our poll.")