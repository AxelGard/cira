"""
Cira

A simpler libray for alpaca-trade-api from Alpaca Markets.
"""

from cira import auth
from cira import config
from cira import util
from cira import log

from cira import strategy

from cira.asset.stock import Stock
from cira.asset.cryptocurrency import Cryptocurrency
from cira.asset.option import OptionContract

from cira.portfolio import Portfolio, Position
from cira.exchange import Exchange, DemoExchange

import alpaca

__version__ = "4.0.0"
__author__ = "Axel Gard"
__credits__ = "alpaca.markets"
