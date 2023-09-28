"""
Cira

A simpler libray for alpaca-trade-api from Alpaca Markets.
"""

from . import auth
from . import config
from . import util
from . import logging

from .exchange import Exchange, DemoExchange
from .asset import Asset, Stock, Cryptocurrency
from .portfolio import Portfolio, Position

import alpaca

__version__ = "3.0.0"
__author__ = "Axel Gard"
__credits__ = "alpaca.markets"
