import time
from . import auth
from .assets import stock
from alpaca.trading.client import TradingClient
from .assets import Cryptocurrency
import alpaca
from typing import List

class Exchange:
    """
    This is the class instence of the Exchange.
    This class is used for interaction with the exchanges,
    for exampel NYSE. The exchange returns data and list of Stocks.
    """
    def __init__(self):
        self._symbols = []
        self._cryptocurrencies = []
        self.stocks = []
        self.apca_id, self.apca_key = auth.get_api_keys()
        self.trading_client = TradingClient(self.apca_id, self.apca_key)
        
    def symbols(self):
        assets = self.trading_client.get_all_assets()
        self._symbols = []
        for asset in assets: 
            self._symbols.append(asset.symbol)
        return self._symbols
        
    def cryptocurrencies(self) -> List[Cryptocurrency]:
        assets = self.trading_client.get_all_assets()
        self._cryptocurrencies = []
        for asset in assets: 
            if asset.asset_class == alpaca.trading.enums.AssetClass.CRYPTO:
                self._cryptocurrencies.append(Cryptocurrency(alpaca_model_asset=asset))
        return self._cryptocurrencies
    

