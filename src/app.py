import discord
from discord.ext import commands
import asyncio
from config import Emojis  # import emojis dictionary from config.py
from tools.logger import get_logger  # Import the new logger
import tools.settings as settings # Import Settings

# Initialize logger using the new get_logger function
logger = get_logger('bot')

# Define the bot's configuration and behavior
def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True  # Required for tracking member joins

    # Set the bot command prefix and intents
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Event handler for when the bot becomes ready
    @bot.event
    async def on_ready():
        logger.info(f'Logged in as {bot.user} (ID: {bot.user.id})')

    # Event handler for message events
    @bot.event
    async def on_message(message):
        # Ignore messages that are not from new members
        if message.type != discord.MessageType.new_member:
            return

        # Handle welcome message reactions based on member roles
        await handle_welcome_reactions(message)

        # Process commands if any
        await bot.process_commands(message)

    # Function to add reactions based on member roles
    async def handle_welcome_reactions(message):
        member = message.author
        roles = [role.name for role in member.roles if role.name != '@everyone']
        
        # Add reactions based on roles in the Emojis dictionary
        for role in reversed(roles):
            emoji = Emojis.get(role)
            if emoji:
                try:
                    await message.add_reaction(emoji)
                    await asyncio.sleep(1)  # Delay to avoid hitting the rate limit
                except discord.HTTPException as e:
                    logger.warning(f"Failed to add reaction for role '{role}': {e}")

    return bot

# Run the bot with the specified token from settings
def run():
    bot = create_bot()
    bot.run(settings.DISCORD_BOT_TOKEN, root_logger=True)

# Entry point
if __name__ == "__main__":
    run()
