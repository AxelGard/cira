from typing import List, Dict
import warnings
from alpaca.trading.client import TradingClient
from . import auth
from . import config
from .asset_stock import Stock


class Position:
    def __init__(self, symbol) -> None:
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.client = TradingClient(APCA_ID, APCA_SECRET, paper=config.PAPER_TRADING)
        self.symbol = symbol

    def quantity(self) -> int:
        """returns the number of the assets that is owned"""
        qty: int = 0
        try:
            qty = int(self.client.get_open_position(self.symbol).qty)
        except:
            qty = 0
        return qty

    def market_value(self) -> float:
        """Returns market value of symbol in portfolio"""
        return float(self.client.get_open_position(self.symbol).market_value)

    def to_dict(self) -> dict:
        """Returns a dict of the position"""
        return {
            "symbol": self.symbol,
            "market_value": self.market_value(),
            "quantity": self.quantity(),
        }

    def __str__(self) -> str:
        return f"({self.symbol}, {self.quantity()})"

    def __repr__(self) -> str:
        return f"({self.symbol}, {self.quantity()})"


class Portfolio:
    def __init__(self) -> None:
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.trading = TradingClient(APCA_ID, APCA_SECRET, paper=config.PAPER_TRADING)
        self.account = self.trading.get_account()
        self.positions: List[Position] = []
        self.account.portfolio_value

    def total_value(self) -> float:
        return float(self.account.portfolio_value)

    def is_blocked(self) -> bool:
        return self.account.account_blocked

    def buying_power(self) -> float:
        """gets the amount of cash currently available"""
        return float(self.account.buying_power)

    def cash(self) -> float:
        """gets the amount of cash currently available"""
        return float(self.account.cash)

    def equity(self) -> float:
        """returns the amount of equity that users has"""
        return float(self.account.equity)

    def equity_yesterday(self) -> float:
        """returns the amount of equity that was
        available at market close yesterday"""
        return float(self.account.last_equity)

    def equity_change(self):
        """returns the change in equity from yesterday to now"""
        return self.equity() - self.equity_yesterday()

    def all_positions(self) -> List[Position]:
        """Returns all positions of portfolio"""
        positions = self.trading.get_all_positions()
        self.positions = []
        for p in positions:
            self.positions.append(Position(p.symbol))
        return self.positions

    def close_all_positions(self) -> None:
        """WARNING: This closes all your open positions"""
        warnings.warn("Warning: will close all open positions ")
        self.trading.close_all_positions(cancel_orders=True)

    def position_in(self, symbol: str) -> Position:
        return Position(symbol)

    def get_allocation(self, symbol: str) -> int:
        return Position(symbol).quantity()

    def cancel_all_orders(self) -> None:
        self.trading.cancel_orders()

    def sell_list(self, symbols: List[str]) -> None:
        """takes a list of Stocks and sells all stocks in that list"""
        for symbol in symbols:
            q = self.position_in(symbol).quantity()
            if q == 0:
                continue
            stk = Stock(symbol=symbol)
            stk.sell(q)

    def owned_stock_qty(self, symbol: str) -> int:  # maby shuld be in stock.Stock
        """returns quantity of owned of a stock Stock (obj)"""
        assert isinstance(symbol, str), "symbol needs to be string"
        return Position(symbol).quantity()

    def owned_stocks_qty(self) -> Dict[str, int]:
        positions = self.trading.get_all_positions()
        result = {}
        for p in positions:
            result[p.symbol] = Position(p.symbol).quantity()
        return result

    def owned_stocks(self) -> List[Stock]:
        """returns a list of owned stocks"""
        return [Stock(p.symbol) for p in self.all_positions()]

    def __repr__(self):
        return f"portfolio({self.equity()})"

    def __str__(self):
        return f"{self.all_positions()}"
