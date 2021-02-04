import cira
import random
import time

cira.alpaca.KEY_FILE = "../paper-trader/key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()
print(exchange.is_open)


for stk in exchange.stocks: 
    print(f"{stk}@{stk.price }")


stk = cira.Stock("TSLA")
print(stk.barset)