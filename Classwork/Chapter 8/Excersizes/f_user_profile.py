# 8.13 User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""

    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile(
    'denzil',
    'de wet',
    location='South Africa',
    occupation='Skills Development Facilitator',
    hobbies=['coding', 'sports', 'camping']
)

print(my_profile)