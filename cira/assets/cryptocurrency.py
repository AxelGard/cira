from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoLatestQuoteRequest
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import alpaca
import datetime
from .. import util
from .asset import Asset


class Cryptocurrency(Asset):
    def __init__(self, symbol="", alpaca_model_asset=None) -> None:
        super().__init__(symbol, alpaca_model_asset)
        self.historical_data_client = CryptoHistoricalDataClient()

    def price(self) -> float:
        """returns the asking price of the cryptocurrency"""
        req_pram = CryptoLatestQuoteRequest(symbol_or_symbols=self.symbol)
        lat_quo = self.historical_data_client.get_crypto_latest_quote(
            request_params=req_pram
        )
        self._price = float(lat_quo[self.symbol].ask_price)
        return self._price

    def historical_data(self, start="2022-01-01", end=""):
        """
        returns bars (formatted as dicts), in the given dates.
        The bars are one day bars.
        """
        if end == "":
            end = datetime.datetime.now().__format__("%Y-%m-%d")
        req_pram = CryptoBarsRequest(
            symbol_or_symbols=self.symbol, timeframe=TimeFrame.Day, start=start, end=end
        )
        bars = self.client.get_crypto_bars(request_params=req_pram)
        return util.bars_to_dict(bars[self.symbol])
