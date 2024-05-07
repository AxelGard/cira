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
    ) -> List[asset.Asset]:
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

    def calendar(self, start="2018-12-01", end="2018-12-01"):
        self._calendar = (
            auth.api().get_calendar(start=start, end=end)[0].__dict__["_raw"]
        )
        return self._calendar

    def assets_raw(self):
        """(legacy, should not be used)
        returns a list of all avilabel stocks in exchanges list"""
        all_assets = []
        active_assets = auth.api().list_assets(status="active")
        for exchange in self.exchanges:
            all_assets += [a for a in active_assets if a.exchange == exchange]
        self._assets = all_assets
        return self._assets

    def symbols(self):
        """returns a list of all symbols"""
        self._symbols = []
        for asset in self.assets_raw():
            self._symbols.append(asset.__dict__["_raw"]["symbol"])
        return self._symbols


class DemoExchange(Exchange):
    def __init__(self) -> None:
        """uses crypto client, so no need for keys, has limited usage"""
        warnings.warn("Warning: demo exchange has limited usage ")
        self.alpc_historical = CryptoHistoricalDataClient()
