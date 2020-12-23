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

portfolio = cira.Portfolio() 
exchange = cira.Exchange() 

def test_setup():
    """ Ensure that position is predictable for testing """
    global exchange
    global portfolio
    if exchange.is_open:
        portfolio.sell_list(portfolio.owned_stocks) # clear portfolio
    
    assert exchange.owned_stocks() == []
    assert portfolio.orders == []

    

def test_stock():
    """ test relatied to the stock class """
    global exchange
    global portfolio
    stock = cira.Stock("TSLA")
    if exchange.is_open: 
        assert portfolio.owned_stocks == []
        stock.buy(1)
        assert portfolio.owned_stocks == ['TSLA']
        stock.sell(1)
        assert portfolio.owned_stocks == []

    assert stock.is_shortable == True 
    assert stock.can_borrow == True 
    assert stock.is_tradable == True 
    assert stock == stock
    assert int(stock) == int(stock.price)

