import discord
import settings
from discord.ext import commands
import asyncio  # Import asyncio for adding delays

# No need to worry about this for now. It was just a way to have clean teminal logs.
logger = settings.logging.getLogger('bot')

# Emojis required for the Welcome channel in Codédex
emojis = {
    'Codédex Club': '<:codedex_club:1120725369381736590>',
    'Python': '<:python:1081697059272413244>',
    'HTML': '<:html:1081697119385157673>',
    'CSS': '<:css:1088318087905955850>',
    'JavaScript': '<:javascript:1116791242521583706>',
    'React': '<:react:1133083387633082478>',
    'SQL': '<:sql:1236748185800540273>',
    'Command Line': '<:command_line:1177615909427359835>',
    'Git & GitHub': '<:github:995770422077431809>',
    'GitHub Student Developer Pack': '<:github_student:1211046146558926878>',
    '#30NitesOfCode Reminder': '<:30nitesofcode:1242335055792046210>'
}


# Defining the run function
def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

# setting the bot command to list to $ and setting the intents to the declared intents above.
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f'User:{bot.user} (ID:{bot.user.id})')

# This function watched the welcome channel and when the welcome message is sent when a new user joins
# it looks for the roles that the user has and if the role is in the emojis dictionary it adds the emoji.
# The emojis hThe emojis have been delcared to match the role names and are stored in a dictionarave been delcared to match the role names and are stored in a dictionary.

        @bot.event
        async def on_message(message):
            if message.type == discord.MessageType.default:
                return

            if message.type == discord.MessageType.new_member:
                member = message.author
                roles = [
                    role.name for role in member.roles if role.name != '@everyone']

                for role in reversed(roles):
                    if role in emojis:
                        await message.add_reaction(emojis.get(role))
                        # Add a 1 second delay to avoid 429 rate limit with custom emojis
                        await asyncio.sleep(1)

            await bot.process_commands(message)

    bot.run(settings.DISCORD_BOT_TOKEN, root_logger=True)


if __name__ == "__main__":
    run()
