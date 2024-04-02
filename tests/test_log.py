import cira
import csv
import os


def test_logging():
    """simple test for checking logging format"""

    cira.config.LOG_FILE = "./cira-test-log.csv"
    cira.config.IS_LOGGING = True
    cira.log.log("BUY", "SYM", 1)
    cira.log.log("SELL", "SYM", 2)
    with open(cira.config.LOG_FILE) as f:
        reader = csv.reader(f, delimiter=",")
        rows = [r for r in reader]

    assert len(rows) == 2
    assert len(rows[0]) == 4 and len(rows[1]) == 4
    assert rows[0][0] == "BUY" and rows[1][0] == "SELL"
    assert rows[0][1] == "SYM" and rows[1][1] == "SYM"
    assert rows[0][2] == "1" and rows[1][2] == "2"

    os.system(f"rm {cira.config.LOG_FILE}")
