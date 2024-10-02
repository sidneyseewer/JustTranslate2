import logging
from enum import Enum

# Define an Enum for logging levels
class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

# Setup a standard logger
def get_logger(name: str, log_level: LogLevel = LogLevel.INFO):
    logger = logging.getLogger(name)
    
    # Set the log level from the enum
    logger.setLevel(log_level.value)
    
    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level.value)
    
    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    # Add the handler to the logger
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
    
    return logger
