"""
Tests for cira class Stock.
"""
import pytest
import cira
import os
import operator


def test_stock_oprators():
    """ test  operators relatied to the stock class """
    stk = cira.Stock("PYPL")
    assert stk + 2 == stk.price + 2
    assert stk - 2 == stk.price - 2
    assert stk * 2 == stk.price * 2
    for op in (operator.add, operator.sub, operator.mul, operator.truediv, operator.floordiv):
        assert op(stk, 2) == op(stk.price, 2), f"test of op {op}"

def test_shortable():
    """ test if a stock is able to be shorted """
    stk = cira.Stock("PYPL")
    assert stk.is_shortable == True

def test_tradable():
    """ test if a stock is able to be shorted """
    stk = cira.Stock("PYPL")
    assert stk.is_tradable == True

def test_stock_borrow():
    """ test if a stock is able to be shorted """
    stk = cira.Stock("PYPL")
    assert stk.can_borrow == True

def test_historical_data():
    """ Test that we historical data can be collected """
    stk = cira.Stock("PYPL")
    days = 10
    assert len(stk.historical_data(days)) == days
