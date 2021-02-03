from . import alpaca
from . import util
from . import stock


class Portfolio:
    def __init__(self):
        self.equity = 0
        self._list_orders = []
        self._owned_stocks = []
        self._position = []

    @property
    def orders(self):
        """ returns a list of all open orders with all diffult args """
        self._list_orders = alpaca.api().list_orders()
        return self._list_orders

    @property
    def position(self):  # PREV: get_position
        """ create a list of all owned position """
        portfolio = alpaca.api().list_positions()
        self._position = []
        for position in portfolio:
            position_dict = util.reformat_position(position)
            position_dict["symbol"] = position.symbol
            self._position.append(position_dict)

        return self._position

    def owned_stock_qty(self, stock):  # maby shuld be in stock.Stock
        """ returns quantity of owned of a stock Stock (obj) """
        position = util.reformat_position(stock.position)
        return position["qty"]

    @property
    def owned_stocks(self):
        """ returns a list of owned stocks """
        lst = self.position
        self._owned_stocks = []
        for dict_ in lst:
            self._owned_stocks.append(stock.Stock(dict_["symbol"]))
        return self._owned_stocks

    
    def sell_list(self, lst):
        """ takes a list of Stocks and sells all stocks in that list """
        for stock_ in lst:
            qty = self.owned_stock_qty(stock_)
            # if not stock.symbol == 'GOOGL':
            # # BUG: fix, google has problem selling!
            stock_.sell(qty)

    def __repr__(self):
        return f"portfolio({self.equity})"

    def __str__(self):
        return f"{self.position}"
