from typing import List
from datetime import datetime
import alpaca
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.requests import CryptoLatestQuoteRequest
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import pandas as pd

from . import auth

class Asset: 
    def __init__(self, symbol:str) -> None:
        """ Interface class """
        self.symbol = symbol 

    def historical_data_df(self, start_date:datetime, end_date:datetime)->pd.DataFrame:
        raise NotImplementedError
    
    def current_price(self)->float:
        raise NotImplementedError
    
    def __str__(self) -> str:
        return self.symbol
    
    def __repr__(self) -> str:
        return self.symbol



class Stock(Asset):
    def __init__(self, symbol:str) -> None:
        """ Exchange for trading stocks """ 
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.client = StockHistoricalDataClient(APCA_ID, APCA_SECRET)
        self.symbol = symbol

    def historical_data(self)->list:
        perms = StockLatestQuoteRequest(symbol_or_symbols=self.symbols)
        self.client.get_stock_bars

    def current_price(self) -> float:
        """ gets the asking price of the symbol """
        perms = StockLatestQuoteRequest(symbol_or_symbols=self.symbol)
        return float(self.client.get_stock_latest_quote(perms)[self.symbol].ask_price)


class Cryptocurrency(Asset):
    def __init__(self, symbol:str) -> None:
        """ Exchange for trading cryptocurrencies """
        self.client = CryptoHistoricalDataClient()
        self.symbol = symbol

    def _get_bars(self, start_date:datetime, end_date:datetime):
        params = CryptoBarsRequest(
            symbol_or_symbols=self.symbol,
            timeframe=TimeFrame.Day,
            start=start_date,
            end=end_date
        )
        return self.client.get_crypto_bars(params)

    def historical_data_df(self, start_date:datetime, end_date:datetime)->pd.DataFrame:
        return self._get_bars(start_date, end_date).df

    def current_price(self) -> float:
        """ gets the asking price of the symbol """
        perms = CryptoLatestQuoteRequest(symbol_or_symbols=self.symbol)
        return float(self.client.get_crypto_latest_quote(perms)[self.symbol].ask_price)

