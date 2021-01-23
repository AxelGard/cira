"""
Tests for cira pkg.
for dev
"""
import pytest
#import unittest
import cira
import os


if 'APCA_ID' in os.environ and 'APCA_KEY' in os.environ: # github action
    cira.alpaca.APCA_API_KEY_ID = os.environ['APCA_ID']
    cira.alpaca.APCA_API_SECRET_KEY = os.environ['APCA_KEY']
    cira.alpaca.KEY_FILE = ""
else:
    cira.alpaca.KEY_FILE = "./tests/test_key.json"



def test_setup():
    """ Ensure that position is predictable for testing """
    portfolio = cira.Portfolio() 
    exchange = cira.Exchange() 
    if exchange.is_open:
        portfolio.sell_list(portfolio.owned_stocks) # clear portfolio
    
    print(portfolio)
    #assert portfolio.owned_stocks == []
    #assert portfolio.orders == []

    

def test_stock():
    """ test relatied to the stock class """
    portfolio = cira.Portfolio() 
    exchange = cira.Exchange() 
    stock = cira.Stock("TSLA")
    print(exchange.is_open)
    if exchange.is_open: 
        assert portfolio.owned_stocks == []
        stock.buy(1)
        assert portfolio.owned_stocks == ['TSLA']
        stock.sell(1)
        assert portfolio.owned_stocks == []

    assert stock.is_shortable == True 
    assert stock.can_borrow == True 
    assert stock.is_tradable == True 
    # assert int(stock) == int(stock.price)

