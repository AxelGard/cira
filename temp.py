import cira 
#import random
#import time

cira.auth.KEY_FILE = "../alpc_key.json"

print(cira.Exchange().is_open())
"""
portfolio = cira.Portfolio()
exchange = cira.Exchange()

qty = 1 # choose how many stocks should be handled in one session 
while exchange.is_open:
    for stock in random.choices(exchange.stocks, k=qty):
        stock.buy(1)
    for stock in random.choices(portfolio.owned_stocks, k=qty):
        stock.sell(1)
    time.sleep(3)     
""" 
