from random import choice

# Define Welcome Messages
WELCOME_MESSAGES = [
    "Welcome {username} 🤗",
    "Hello {username} 👋🏻",
    "Howdy.. {username}!"
]

def get_welcome_message(username):
    return choice(WELCOME_MESSAGES).format(username=username)
