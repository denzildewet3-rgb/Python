# Looping through entire list

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)

# Doing more work within a loop
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"\n{magician.title()}, that was a great trick!!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great show")

# Avoiding Indentation Errors
# NOTE: ERROR: Indentation Error
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)

# Forgetting to Indent Additional Lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Indenting Unnecessarily
# RESULTS in indentation error
message = "Hello Python world!"
print(message)

# Indenting Unnecessarily After the Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone, that was a great magic show!")

# Forgetting the Colon
# Results in Syntax error
magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)