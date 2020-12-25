import cira
import os
import random
import time

cira.alpaca.KEY_FILE = "../paper-trader/key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()

stock = cira.Stock("TSLA")
print(stock.historical_data())

"""qty = 1
print(exchange.is_open)
while exchange.is_open:
    for stock in random.choices(exchange.stocks, k=qty):
        stock.buy(1)
        print(stock)
    for stock in random.choices(portfolio.owned_stocks, k=qty):
        stock.sell(1)
        print(stock)
    time.sleep(2)

"""
    