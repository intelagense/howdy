import os
import logging
from dotenv import load_dotenv
from logging.config import dictConfig

load_dotenv()

# Needs to be replace the the codedex club discord token
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")  

# This is the logging configuration. No need to worry about it but feel free to take a look.
LOGGING_CONFIG = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose':{
      'format':'%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s'
    },
    "standard":{
      'format':'%(levelname)-10s - %(name)-15s : %(message)s'
    }
  },
  'handlers':{
    'console':{
      'level':'DEBUG',
      'class':'logging.StreamHandler',
      'formatter':'standard'
    },
    'console2':{
      'level':'WARNING',
      'class':'logging.StreamHandler',
      'formatter':'standard'
    },
    'file':{
      'level':'INFO',
      'class':'logging.FileHandler',
      'filename':'logs/infos.log',
      'mode':'w',
      'formatter':'verbose'
    },
    
  },
  'loggers':{
      'bot':{
        'handlers':['console'],
        'level':'INFO',
        'propagate':False
      },
      'discord':{
        'handlers':['console2','file'],
        'level':'INFO',
        'propagate':False
        }
        

    }
}

dictConfig(LOGGING_CONFIG)