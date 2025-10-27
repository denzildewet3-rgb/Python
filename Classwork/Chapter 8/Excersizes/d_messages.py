# # 8-9 Messages
# def show_messages(messages):
#     """Print each message in the list."""
#     for message in messages:
#         print(message)

# text_messages = [
#     "Hey, how are you?",
#     "Don’t forget the meeting at 10!",
#     "Lunch is on me today!",
#     "Call me when you're free.", 
#     "Tell me what do you want to eat for lunch",
#     "Hello, are you there", 
#     "Please pick up the phone"
# ]

# show_messages(text_messages)

# 8-10 Sending messages
# def show_messages(messages):
#     """Print each message in the list."""
#     for message in messages:
#         print(message)

# def send_messages(messages, sent_messages):
#     """Print each message and it will move it to sent_messages list. The original list will be empty after sending"""
#     while messages:
#         current_message = messages.pop(0)
#         print(current_message)
#         sent_messages.append(current_message)

# text_messages = [
#     "Hey, how are you?",
#     "Don’t forget the meeting at 10!",
#     "Lunch is on me today!",
#     "Call me when you're free.", 
#     "Tell me what do you want to eat for lunch",
#     "Hello, are you there", 
#     "Please pick up the phone"
# ]

# sent_messages = []

# send_messages(text_messages, sent_messages)

# print("\nOriginal list after sending message: ", text_messages)
# print("\nSent messages list: ", sent_messages)

# 8-11 Archived Messages
def show_messages(messages):
    """Print each message in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and it will move it to sent_messages list. The original list will be empty after sending"""
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

text_messages = [
    "Hey, how are you?",
    "Don’t forget the meeting at 10!",
    "Lunch is on me today!",
    "Call me when you're free.", 
    "Tell me what do you want to eat for lunch",
    "Hello, are you there", 
    "Please pick up the phone"
]

sent_messages = []

send_messages(text_messages[:], sent_messages)

print("\nOriginal list after (Unchanged): ", text_messages)
print("\nSent messages list: ", sent_messages)