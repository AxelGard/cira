"""
Tests for cira pkg.
for dev
"""
import pytest
#import unittest
import cira
import os
import operator


if 'APCA_ID' in os.environ and 'APCA_KEY' in os.environ: # github action
    cira.alpaca.APCA_API_KEY_ID = os.environ['APCA_ID']
    cira.alpaca.APCA_API_SECRET_KEY = os.environ['APCA_KEY']
    cira.alpaca.KEY_FILE = ""
else:
    cira.alpaca.KEY_FILE = "../paper-trader/key.json"



def test_setup():
    """ Ensure that position is predictable for testing """
    portfolio = cira.Portfolio() 
    exchange = cira.Exchange() 
    if exchange.is_open:
        pass 
        # portfolio.sell_list(portfolio.owned_stocks) # clear portfolio
    #assert portfolio.owned_stocks == []
    
    

def test_stock():
    """ test relatied to the stock class """
    portfolio = cira.Portfolio() 
    exchange = cira.Exchange() 
    stk = cira.Stock("PYPL")

    assert stk.is_shortable == True 
    assert stk.can_borrow == True 
    assert stk.is_tradable == True 

    assert stk + 2 == stk.price + 2 
    assert stk - 2 == stk.price - 2 
    assert stk * 2 == stk.price * 2 
    for op in (operator.add, operator.sub, operator.mul, operator.truediv, operator.floordiv):
        assert op(stk, 2) == op(stk.price, 2)
