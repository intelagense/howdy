import logging
from discord import utils as DiscordUtils
from discord import TextChannel, DMChannel, Forbidden

from .welcome_responses import get_welcome_message

logger = logging.getLogger('LogBot')


async def message_controller(message):
    if not message.content:
        return
    is_direct_message = isinstance(message.channel, DMChannel)
    is_text_channel = isinstance(message.channel, TextChannel)

    # Put the most common first!
    if  is_direct_message:
        await send_message_private(message)
    elif is_text_channel:
        pass
        #channel = message.channel
        #await message.channel.send(response)
    else:
        pass

async def send_message_private(message):
    username = str(message.author)
    try:
        await message.author.send(username + ": " + message.content)
    except Forbidden:
        logger.error(f"Cannot send messages to user {message.author}. They might have DMs disabled or the bot is blocked.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")



async def welcome_message(member):
    welcome_channel = DiscordUtils.get(member.guild.text_channels, name='welcome')
    if welcome_channel:
        await welcome_channel.send(get_welcome_message(member.mention))
