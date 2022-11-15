# import alpaca_trade_api as tradeapi
from .asset import Asset

class Stock(Asset):
    """
    This is the class instence of a Stock.
    This class is for interaction of a Stock
    """
    def __init__(self, symbol="", alpaca_model_asset=None) -> None: 
        super().__init__(symbol, alpaca_model_asset)


