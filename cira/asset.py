from typing import List
from datetime import datetime
import alpaca
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.requests import CryptoLatestQuoteRequest
from alpaca.data.requests import CryptoBarsRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.live import StockDataStream
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest
from alpaca.data.models import Bar

import pandas as pd

from . import auth
from . import config

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
        self.live_client = StockDataStream(APCA_ID,APCA_SECRET)
        self.history = StockHistoricalDataClient(APCA_ID, APCA_SECRET)
        self.trade = TradingClient(APCA_ID, APCA_SECRET, paper=config.PAPER_TRADING)
        self.symbol = symbol

    def current_price(self) -> float:
        """ gets the asking price of the symbol """
        perms = StockLatestQuoteRequest(symbol_or_symbols=self.symbol)
        return float(self.history.get_stock_latest_quote(perms)[self.symbol].ask_price)

    def live_data(self, async_function_to_resolve_to, run:bool=True) -> None:
        self.live_client.subscribe_quotes(async_function_to_resolve_to, self.symbol)
        if run: 
            self.live_client.run()

    def _get_bars(self, start_date:datetime, end_date:datetime):
        """ returns aplc bars from the given dates """
        params = StockBarsRequest(
            symbol_or_symbols=self.symbol,
            timeframe=TimeFrame.Day,
            start=start_date,
            end=end_date
        )
        return self.history.get_stock_bars(params)

    def historical_data_df(self, start_date:datetime, end_date:datetime)->pd.DataFrame:
        """ takes two dates, and returns a data frame with bars from the given dates """
        data = self._get_bars(start_date, end_date).df
        data = data.reset_index(level='symbol')
        data.index = pd.to_datetime(data.index.get_level_values('timestamp'))
        return data

    def historical_data(self, start_date:datetime, end_date:datetime)->List[dict]:
        """ takes two dates, and returns a list of dicts with bars from the given dates """
        return self._get_bars(start_date, end_date).dict()[self.symbol]

    def buy(self,qty:float) -> None:
        market_order = MarketOrderRequest(
                    symbol=self.symbol,
                    qty=qty,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )
        self.trade.submit_order(market_order)

    def sell(self,qty:float) -> None:
        market_order = MarketOrderRequest(
                    symbol=self.symbol,
                    qty=qty,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY
                    )
        self.trade.submit_order(market_order)

    def buy_at(self, qty:int, price:float) -> None:
        limit_order_data = LimitOrderRequest(
                            symbol=self.symbol,
                            limit_price=price,
                            notional=qty,
                            side=OrderSide.BUY,
                            time_in_force=TimeInForce.FOK
                        )
        self.trade.submit_order(
                        order_data=limit_order_data
                    )

    def buy_at(self, qty:int, price:float) -> None:
        limit_order_data = LimitOrderRequest(
                            symbol=self.symbol,
                            limit_price=price,
                            notional=qty,
                            side=OrderSide.SELL,
                            time_in_force=TimeInForce.FOK
                        )
        self.trade.submit_order(
                        order_data=limit_order_data
                    )


    
        

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

