# 8-3 T-Shirt
def make_shirt(size, message):
    """Display information about the shirt"""
    print(f"The shirt is {size.upper()} and it will have the message: '{message}' printed on it.")

make_shirt('medium', 'Code like a pro!')
make_shirt(size='large', message='Python is awesome!')

print("\n")

#8-4 Large shirts
def make_shirt(size='large', message='I love Python'):
    """Display information about the shirt with the default value"""
    print(f"The shirt is {size.upper()} and it will have the message: '{message}' printed on it.")

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='Keep Calm and Code On!')