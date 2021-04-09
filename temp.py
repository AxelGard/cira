import cira
import random
import time

cira.alpaca.KEY_FILE = "../paper-trader/key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()
print(exchange.is_open)


for stk in exchange.stocks[:3]: 
    print(f"{stk.price} // 2 = {stk // 2}")


stk = cira.Stock("TSLA")
print(stk.barset)