import cira
import random
import time
import operator

cira.alpaca.KEY_FILE = "./tests/test_key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()
print(exchange.is_open)


#for stk in exchange.stocks[:3]: 
#    print(stk.price)

stk = cira.Stock("TSLA")
print(stk.price)

for op in (operator.add, operator.sub, operator.mul, operator.truediv, operator.floordiv):
    assert op(stk, 2) == op(stk.price, 2)