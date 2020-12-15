"""
Tests for cira pkg.
for dev
"""
import pytest
#import unittest
import cira
import os


if 'APCA_ID' in os.environ and 'APCA_KEY' in os.environ: # github action
    cira.APCA_API_KEY_ID = os.environ['APCA_ID']
    cira.APCA_API_SECRET_KEY = os.environ['APCA_KEY']
    cira.KEY_FILE = ""
else:
    cira.KEY_FILE = "./tests/test_key.json"


def test_set_up():
    """ Ensure that position is predictable for testing """
    if cira.exchange_open():
        cira.sell_list(cira.owned_stocks()) # clear portfolio
    assert cira.owned_stocks() == []


def test_portfolio():
    """ Testing function realating to portfolio """
    assert cira.owned_stocks() == []
    assert cira.get_position() == []


def test_trade():
    """ buy and sell testing """
    stock = 'AMZN'
    cira.logging.LOGGING = False
    assert cira.is_tradable(stock) == True
    if cira.exchange_open():
        cira.buy(1, stock)
        assert cira.owned_stocks() == [stock]
        cira.sell(1, stock)
    assert cira.owned_stocks() == []


def test_short():
    """ testing realating to shorting stocks """
    stock = 'TSLA'
    assert cira.is_shortable(stock) == True
    assert cira.can_borrow(stock) == True


def test_lists_orders():
    """ simple testy to ensure that no orders is till runing """
    assert cira.list_orders() == []
