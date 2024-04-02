import logging

"""
 This files keeps the varibale that is used 
 for configuration cross cira. 
"""

# logging
IS_LOGGING = False
LOG_FILE = "./cira-log.csv"
LOGGING_LEVEL = logging.WARNING

# debugging
DEBUG = False

# paper trading
PAPER_TRADING = True

# data that will not very often change is cached
USE_CASHING = True
