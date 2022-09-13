"""
Tests for cira pkg.
for dev
"""
import pytest
import cira
import os
import operator

if 'APCA_ID' in os.environ and 'APCA_KEY' in os.environ: # github action
    cira.auth.APCA_API_KEY_ID = os.environ['APCA_ID']
    cira.auth.APCA_API_SECRET_KEY = os.environ['APCA_KEY']
    cira.auth.KEY_FILE = ""
else:
    cira.auth.KEY_FILE = "../paper-trader/key.json"


def test_setup():
    """ Ensure that position is predictable for testing """
    portfolio = cira.Portfolio() 
    exchange = cira.Exchange() 
    if exchange.is_open:
        pass 
        # portfolio.sell_list(portfolio.owned_stocks) # clear portfolio
    #assert portfolio.owned_stocks == []
    
    
