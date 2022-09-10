import cira
import random
import time
import operator
import datetime
cira.alpaca.KEY_FILE = "../alpc_key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()
#print(exchange.is_open)



"""
for stk in exchange.stocks[:3]:
    for op in (operator.add, operator.sub, operator.mul, operator.truediv, operator.floordiv):
        assert op(stk, 2) == op(stk.price, 2), f"test of op {op}"
"""

stk = cira.Stock("TSLA")
print(stk.barset(10))
hist = stk.historical_data_range()
print([d["date"] for d in hist])

#print(str(datetime.datetime.utcfromtimestamp(stk.barset(1).__dict__['_raw'][0]['t']).strftime("%Y-%m-%d")))

#str(datetime.datetime.utcfromtimestamp(bar.__dict__['_raw'][0]['t']).strftime("%Y-%m-%d"))
