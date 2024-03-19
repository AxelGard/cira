import csv
import time
import logging
from . import config

"""
This functions is logging trades
"""


def log(action: str, sym: str, qty: int) -> None:
    """writes log data to file"""
    time_ = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
    log_data = [action, sym, qty, time_]
    with open(config.LOG_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow(log_data)
