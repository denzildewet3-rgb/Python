# 10-4 Guest

from pathlib import Path

name = input("What is your name? ")

path = Path("guest.txt")

path.write_text(name.title())

print(f"Thanks, {name.title()}. Your name has been written to guest.txt")