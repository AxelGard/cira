import cira
import random
import time

cira.alpaca.KEY_FILE = "./tests/test_key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()

print(portfolio.owned_stocks)
