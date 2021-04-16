"""
Cira

A simpler libray for alpaca-trade-api from Alpaca Markets.
"""

import alpaca_trade_api as tradeapi

from . import alpaca
from . import config
from . import util
from . import logging
from .exchange import Exchange
from .stock import Stock
from .portfolio import Portfolio

__version__ = "2.1.1"
__author__ = "Axel Gard"
__credits__ = "alpaca.markets"
