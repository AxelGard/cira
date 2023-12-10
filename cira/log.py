import csv
import time
import logging
from . import config

"""
This functions is logging trades
"""


def format_log_action(act: str, sym: str, qty: int) -> list:
    """formats info for logging"""
    time_ = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
    log_data = [act, sym, qty, time_]
    return log_data


def log(log_data: list) -> None:
    """writes log data to file"""
    with open(config.LOG_FILE, "a") as file:
        # fd.write(log_data)
        writer = csv.writer(file)
        writer.writerow(log_data)


def set_logging():
    if config.IS_LOGGING:
        logging.basicConfig(filename="./cira.log", level=config.LOGGING_LEVEL)
