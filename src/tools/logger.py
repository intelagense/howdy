import logging
import logging.config
import os

# Ensure the logs directory exists
os.makedirs('logs', exist_ok=True)

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s'
        },
        'standard': {
            'format': '%(levelname)-10s - %(name)-15s : %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'console2': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/infos.log',
            'mode': 'w',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'bot': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        'discord': {
            'handlers': ['console2', 'file'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

# Apply the logging configuration
logging.config.dictConfig(LOGGING_CONFIG)

# Define a helper to get loggers for other modules
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
