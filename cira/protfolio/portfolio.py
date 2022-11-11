from .. import auth
from .. import util
from ..assets import stock
from .position import Position

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

        from alpaca.trading.client import TradingClient
        self.apca_id, self.apca_key = auth.get_api_keys()
        self.trading_client = TradingClient(self.apca_id, self.apca_key)

        self.account = self.trading_client.get_account()

    def cash(self) -> float:
        return self._cash

    def positions(self) -> list:
        """ returns a list of all the portfolios positions """
        positions = self.trading_client.get_all_positions()
        #for position in positions:
        print(positions[0].dict)
        
    def close_all_positions(self) -> list[Position]:
        """ will close all open positions """
        closed_positions = self.trading_client.close_all_positions()
        positions = []
        for position in closed_positions:
            positions.append(Position(position))
        return positions 

        
    def to_dict(self)->dict:
        """ returns attributes of portfolio in a dict """
        return {
            
        }
    
    def __repr__(self):
        return f"portfolio({self.equity})"


    def __str__(self):
        return f"{self.position}"
