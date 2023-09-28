from typing import List
import warnings
from alpaca.trading.client import TradingClient
from . import auth
from . import config


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
        return self.symbol

    def __repr__(self) -> str:
        return self.symbol


class Portfolio:
    def __init__(self) -> None:
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.trading = TradingClient(APCA_ID, APCA_SECRET, paper=config.PAPER_TRADING)
        self.account = self.trading.get_account()
        self.positions: List[Position] = []
        self.account.crypto_status

        assert not self.is_blocked(), "Account is blocked"

    def is_blocked(self) -> bool:
        return self.account.account_blocked()

    def buying_power(self) -> float:
        """gets the amount of cash currently available"""
        return float(self.account.buying_power)

    def cash(self) -> float:
        """gets the amount of cash currently available"""
        return float(self.account.cash)

    def all_positions(self) -> List[Position]:
        """Returns all positions of portfolio"""
        positions = self.trading.get_all_positions()
        for p in positions:
            self.positions.append(Position(p.symbol))
        return self.positions

    def close_all_positions(self) -> None:
        """WARNING: This closes all your open positions"""
        warnings.warn("Warning: will close all open positions ")
        self.trading.close_all_positions(cancel_orders=True)

    def position_in(self, symbol: str) -> Position:
        return Position(symbol)

    def cancel_all_orders(self) -> None:
        self.trading.cancel_orders()
