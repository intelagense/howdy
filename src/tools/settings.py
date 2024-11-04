import os
import logging
from dotenv import load_dotenv
from logging.config import dictConfig

load_dotenv()

# Needs to be replace the the codedex club discord token
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")  