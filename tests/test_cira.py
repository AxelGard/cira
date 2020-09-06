"""
Tests for cira pkg.
for dev
"""
import pytest
#import unittest
import cira

TEST_KEY_FILE = "./tests/test_key.json"
cira.KEY_FILE = TEST_KEY_FILE

def test_set_up():
    cira.sell_list(cira.owned_stocks()) # clear portfolio
    assert cira.owned_stocks() == []

def test_portfolio():
    """ Testing function realating to portfolio """
    assert cira.owned_stocks() == []


def test_trade():
    """ buy, sell and short testing """
    stock = 'TSLA'
    cira.logging.LOGGING = False
    """
    cira.buy(1, stock)
    assert cira.owned_stocks() == [stock]
    cira.sell(1, stock)
    """
    assert cira.owned_stocks() == []

    assert cira.is_shortable(stock) == True
    assert cira.can_borrow(stock) == True
    assert cira.is_tradable(stock) == True
