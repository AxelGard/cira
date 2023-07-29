from typing import List
from alpaca.trading.client import TradingClient
from . import auth
from . import config

class Position:
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.client = TradingClient(APCA_ID, APCA_SECRET, paper=config.PAPER_TRADING)
    
    def quantity(self) -> int:
        """ returns the number of the assets that is owned """
        qty:int = 0
        try:
            qty = int(self.client.get_open_position(self.symbol).qty)
        except:
            qty = 0
        return qty

    
    def market_value(self,symbol:str) -> float:
        return float(self.client.get_open_position(symbol).market_value)

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return self.symbol


class Portfolio:
    def __init__(self) -> None:
        APCA_ID, APCA_SECRET = auth.get_api_keys()
        self.client = TradingClient(APCA_ID, APCA_SECRET, paper=config.PAPER_TRADING)
        self.account = self.client.get_account()
        self.positions:List[Position] = []

    def cash(self)->float: 
        """ gets the amount of cash currently available """
        return float(self.account.cash)
    
    def all_positions(self)->List[Position]:
        positions = self.client.get_all_positions() 
        for p in positions:
            self.positions.append(Position(p.symbol))
        return self.positions
        
    def close_all_positions(self)->None:
        """ WARNING: This closes all your open positions """
        self.client.close_all_positions(cancel_orders=True)

    def position_in(self, symbol:str) -> Position:
        return Position(symbol)

