from typing import List
from . import asset
from . import auth
from . import config
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.trading.enums import AssetClass

class Exchange:
    def __init__(self) -> None:
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.alpc_client = TradingClient(APCA_ID, APCA_SECRET)
        self.alpc_historical = StockHistoricalDataClient(APCA_ID,APCA_SECRET)
        self.stock_cache:List[asset.Stock] = []

    def to_assets(self, symbols: List[str]) -> List[asset.Asset]:
        return [self.to_asset(s) for s in symbols]

    def to_asset(symbol:str)->asset.Asset:
        return asset.Stock(symbol) 
    
    def get_all_stocks(self, is_tradeable:bool=True, force_reload:bool=False) -> List[asset.Stock]:
        if config.USE_CASHING and self.stock_cache != [] and not force_reload: 
            return self.stock_cache
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        alpc_assets = self.alpc_client.get_all_assets(search_params)
        self.stock_cache = [asset.Stock(a.symbol) for a in alpc_assets if a.tradable == is_tradeable]
        return self.stock_cache


class DemoExchange(Exchange):
    def __init__(self) -> None:
        print("Warning: demo exchange has limited usage ")
        self.alpc_historical = CryptoHistoricalDataClient()
