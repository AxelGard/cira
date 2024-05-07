"""
Cira

A simpler libray for alpaca-trade-api from Alpaca Markets.
"""

from . import auth
from . import config
from . import util
from . import log
from . import strategy

# Assets
from .asset import Asset
from .assset_cryptocurrency import Cryptocurrency
from .asset_stock import Stock
from .asset_option import OptionContract

from .portfolio import Portfolio, Position
from .exchange import Exchange, DemoExchange

import alpaca

__version__ = "3.1.0"
__author__ = "Axel Gard"
__credits__ = "alpaca.markets"
