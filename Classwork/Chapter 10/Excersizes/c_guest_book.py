from pathlib import Path

path = Path("guest_book.txt")

guest_names = []

while True:
    name = input("Enter Your Name or Type 'q' to quit: ")
    if name.lower() == 'q':
        break
    guest_names.append(name.title())
    
path.write_text('\n'.join(guest_names))

print(f"\nThanks! {len(guest_names)} names have been added to guest_book.txt.")