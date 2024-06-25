import os
import logging

from dotenv import load_dotenv
from discord import Intents, Client

from messages.responses import welcome_message, message_controller

# Load env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Bot 
intents = Intents.default()
intents.message_content = True
intents.members = True
client= Client(intents=intents)

# Create a logger
logger = logging.getLogger('LogBot')


# Startup of the bot
@client.event
async def on_ready():
    print(f'{client.user} is now running!')


# Manage the messages
@client.event
async def on_message(message):
    # Check that the message is not for the same bot
    await message_controller(message)

# New Member on the server
@client.event
async def on_member_join(member):
   await welcome_message(member)

# Start
def main():
    client.run(token=DISCORD_TOKEN)

if __name__ == '__main__':
    main()