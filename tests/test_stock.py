"""
Tests for cira class Stock.
"""
import pytest
import cira
import os
import operator


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
        assert op(stk, 2) == op(stk.price, 2), f"test of op {op}"

