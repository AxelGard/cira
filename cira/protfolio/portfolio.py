from .position import Position
from ..alpaca_utils import get_trading_client
from typing import List


class Portfolio:
    """
    The class Portfolio, is for
    interacting with your own protfolio.
    """

    def __init__(self):
        self._equity = 0.0
        self._equity_yesterday = 0.0
        self._equity_change = 0.0
        self._cash = 0.0
        self._buying_power = 0.0
        self._list_orders = []
        self._owned_stocks = []
        self._position = []
        self._account = {}

        self.trading_client = get_trading_client()

        self.account = self.trading_client.get_account()

    def cash(self) -> float:
        return self._cash

    def positions(self) -> List[Position]:
        """returns a list of all the portfolios positions"""
        positions = self.trading_client.get_all_positions()
        self._position = []
        for position in positions:
            pass
        print(positions[0].dict)
        return self._positions

    def close_all_positions(self) -> list[Position]:
        """will close all open positions"""
        closed_positions = self.trading_client.close_all_positions()
        positions = []
        for position in closed_positions:
            positions.append(Position(position))
        return positions

    @property
    def equity(self) -> float:
        self._equity = float(self.account.equity)
        return self._equity

    def to_dict(self) -> dict:
        """returns attributes of portfolio in a dict"""
        return {}

    def __repr__(self):
        return f"portfolio({self.equity})"

    def __str__(self):
        return f"{self.position}"
