from typing import List
from datetime import datetime
import logging
import warnings

# Alpaca
import alpaca
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass, OrderType, AssetStatus
from alpaca.data.models import Bar
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.requests import LimitOrderRequest, StopLimitOrderRequest
from alpaca.trading.client import TradingClient

# stock
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.requests import StockBarsRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.data.live import StockDataStream

# crypto
from alpaca.data import CryptoHistoricalDataClient
from alpaca.data.live.crypto import CryptoDataStream
from alpaca.data.requests import CryptoLatestQuoteRequest
from alpaca.data.requests import CryptoBarsRequest

import pandas as pd

from . import auth
from . import config
from . import util
from . import log

from .asset import Asset


class Cryptocurrency(Asset):
    def __init__(self, symbol: str) -> None:
        """Exchange for trading cryptocurrencies"""
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.symbol = symbol
        self.live_client = CryptoDataStream(APCA_ID, APCA_SECRET)
        self.history: CryptoHistoricalDataClient = CryptoHistoricalDataClient()
        if APCA_ID != "":
            self.history = CryptoHistoricalDataClient(APCA_ID, APCA_SECRET)
            self.trade = TradingClient(APCA_ID, APCA_SECRET, paper=config.PAPER_TRADING)
        self.latest_quote_request = CryptoLatestQuoteRequest
        self.bars_request = CryptoBarsRequest

    def price(self) -> float:
        """gets the asking price of the symbol"""
        perms = self.latest_quote_request(symbol_or_symbols=self.symbol)
        return float(self.history.get_crypto_latest_quote(perms)[self.symbol].ask_price)

    def buy(self, qty: float) -> None:
        """Buy the asset,
        qty is the number of the asset that you buy"""
        market_order = MarketOrderRequest(
            symbol=self.symbol,
            qty=qty,
            side=OrderSide.BUY,
            type=OrderType.MARKET,
            time_in_force=TimeInForce.GTC,
        )
        if config.IS_LOGGING:
            log.log("BUY", self.symbol, qty)
        self.trade.submit_order(market_order)

    def buy_within(self, qty: float, buy_at: float, sell_at: float) -> None:
        req = StopLimitOrderRequest(
            symbol=self.symbol,
            qty=qty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.GTC,
            limit_price=buy_at,
            stop_price=sell_at,
        )
        self.trade.submit_order(req)

    def buy_at(self, qty: int, price: float) -> None:
        """Buy the asset at a given price,
        qty is the number of the asset that you buy"""
        limit_order_data = LimitOrderRequest(
            symbol=self.symbol,
            limit_price=price,
            qty=qty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.GTC,
        )
        if config.IS_LOGGING:
            log.log("BUY", self.symbol, qty)
        self.trade.submit_order(order_data=limit_order_data)

    def sell(self, qty: float) -> None:
        """Sell the asset,
        qty is the number of the asset that you sell"""
        market_order = MarketOrderRequest(
            symbol=self.symbol,
            qty=qty,
            side=OrderSide.SELL,
            type=OrderType.MARKET,
            time_in_force=TimeInForce.GTC,
        )
        logging.info(f"sell:{self.symbol}, qty:{qty}")
        if config.IS_LOGGING:
            log.log("SELL", self.symbol, qty)
        self.trade.submit_order(market_order)

    def sell_at(self, qty: int, price: float) -> None:
        """Sell the asset at a given price,
        qty is the number of the asset that you sell"""
        limit_order_data = LimitOrderRequest(
            symbol=self.symbol,
            limit_price=price,
            qty=qty,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.GTC,
        )
        if config.IS_LOGGING:
            log.log("SELL", self.symbol, qty)
        self.trade.submit_order(order_data=limit_order_data)

    def _get_bars(self, start_date: datetime, end_date: datetime):
        """returns aplc bars from the given dates"""
        params = self.bars_request(
            symbol_or_symbols=self.symbol,
            timeframe=TimeFrame.Day,
            start=start_date,
            end=end_date,
            adjustment="all",
        )
        return self.history.get_crypto_bars(params)

    @classmethod
    def get_all_assets(self):
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        trade = TradingClient(APCA_ID, APCA_SECRET, paper=config.PAPER_TRADING)
        search_params = GetAssetsRequest(
            asset_class=AssetClass.CRYPTO, status=AssetStatus.ACTIVE
        )
        return [a.symbol for a in trade.get_all_assets(search_params)]
