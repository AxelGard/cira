from typing import List
from . import asset
from . import auth
from . import config
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.trading.enums import AssetClass
import warnings


class Exchange:
    def __init__(self) -> None:
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.alpc_client = TradingClient(APCA_ID, APCA_SECRET)
        self.alpc_historical = StockHistoricalDataClient(APCA_ID, APCA_SECRET)
        self.stock_cache: List[asset.Stock] = []

    def is_open(self) -> bool:
        """Checks if the exchange is open and able to trade"""
        return auth.api().get_clock().is_open

    def to_assets(self, symbols: List[str]) -> List[asset.Asset]:
        """Takes a list of symbols and returns
        them in a list of cira Assets objects"""
        return [self.to_asset(s) for s in symbols]

    def to_asset(self, symbol: str) -> asset.Asset:
        """Takes a symbols and returns
        it as a cira Assets objects"""
        return asset.Stock(symbol)

    def get_all_stocks(
        self, is_tradeable: bool = True, force_reload: bool = False
    ) -> List[asset.Stock]:
        """Returns a list of all stocks as cira asset,
        objects will be cached, can be turn off in config."""
        if config.USE_CASHING and self.stock_cache != [] and not force_reload:
            return self.stock_cache
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        alpc_assets = self.alpc_client.get_all_assets(search_params)
        self.stock_cache = [
            asset.Stock(a.symbol) for a in alpc_assets if a.tradable == is_tradeable
        ]
        return self.stock_cache


class DemoExchange(Exchange):
    def __init__(self) -> None:
        """uses crypto client, so no need for keys, has limited usage"""
        warnings.warn("Warning: demo exchange has limited usage ")
        self.alpc_historical = CryptoHistoricalDataClient()
