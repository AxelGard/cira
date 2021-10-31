import cira
import random
import time
import operator

cira.alpaca.KEY_FILE = "../paper-trader/key.json"


portfolio = cira.Portfolio()
exchange = cira.Exchange()
print(exchange.is_open)

"""
for stk in exchange.stocks[:3]:
    for op in (operator.add, operator.sub, operator.mul, operator.truediv, operator.floordiv):
        assert op(stk, 2) == op(stk.price, 2), f"test of op {op}"
"""


stk = cira.Stock("MMLP")
stks = [stk]

portfolio.sell_list(lst=stks)
