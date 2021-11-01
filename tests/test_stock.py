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


def test_is_shortable():
    pass

def test_historical_data():
    """ Test that we historical data can be collected """
    portfolio = cira.Portfolio()
    exchange = cira.Exchange()
    stk = cira.Stock("PYPL")
    days = 10
    assert len(stk.historical_data(days)) == days
