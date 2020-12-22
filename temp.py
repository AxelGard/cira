import cira
import os

cira.alpaca.KEY_FILE = "../paper-trader/key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()
stock = cira.Stock("TSLA")

print(stock.buy(1))