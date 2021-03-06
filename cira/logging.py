import csv
from . import config
import time


def format_log_action(act, sym, qty):
    """ formats info for logging """
    time_ = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
    log_data = [act, sym, qty, time_]
    return log_data


def log(log_data):
    """ writes log data to file """
    with open(config.LOG_FILE, "a") as file:
        # fd.write(log_data)
        writer = csv.writer(file)
        writer.writerow(log_data)
    return None
