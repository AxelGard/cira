from typing import List
from . import asset
from . import auth
from . import config
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

class Exchange:
    def __init__(self) -> None:
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.client = TradingClient(APCA_ID, APCA_SECRET)
        self.stock_cache:List[asset.Stock] = []


    def get_assets(self, symbols: List[str]) -> List[asset.Asset]:
        return [asset.Stock(s) for s in symbols]
    
    def get_all_stocks(self, is_tradeable:bool=True) -> List[asset.Stock]:
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        alpc_assets = self.client.get_all_assets(search_params)
        return [asset.Stock(a.symbol) for a in alpc_assets if a.tradable == is_tradeable]

    def to_asset(symbols:List[str])->List[asset.Asset]:
        pass  

class DemoExchange(Exchange):
    def __init__(self) -> None:
        print("Warning: demo exchange has limited usage ")
        self.client = None

