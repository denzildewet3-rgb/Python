# 8-12 Sandwhiches
def make_sandwich(*items):
    """Print summary of the sandwiches being ordered"""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"\t- {item}")

make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'tomato')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')