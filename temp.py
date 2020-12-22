import cira
import os

cira.alpaca.KEY_FILE = "../paper-trader/key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()

print(exchange.stocks)