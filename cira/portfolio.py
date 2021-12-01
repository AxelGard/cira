from . import alpaca
from . import util
from . import stock


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


    @property
    def orders(self):
        """ returns a list of all open orders with all diffult args """
        self._list_orders = alpaca.api().list_orders()
        return self._list_orders


    @property
    def position(self):  # PREV: get_position # TODO: change to positions
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
        position = stock.position
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
        owned_stocks = self.owned_stocks
        for stock_ in lst:
            # if stock_ in owned_stocks:
            qty = self.owned_stock_qty(stock_)
            # if not stock.symbol == 'GOOGL':
            # # BUG: fix, google has problem selling!
            stock_.sell(qty)


    @property
    def account(self):
        """ returns the dict of user account details"""
        self._account = util.reformat_position(alpaca.api().get_account())
        return self._account


    @property
    def buying_power(self):
        """ returns the amount of current buying_power that the user have"""
        self._buying_power = self.account["buying_power"]
        return self._buying_power


    def is_blocked(self):
        """ checks if the users has been blocked from trading """
        return self.account["trading_blocked"]


    @property
    def cash(self):
        """ returns the amount of a available liquid chash in account """
        self._cash = self.account["cash"]
        return self._cash


    @property
    def equity(self):
        """ returns the amount of equity that users has """
        self._equity = self.account["equity"]
        return self._equity


    @property
    def equity_yesterday(self):
        """ returns the amount of equity that was
        available at market close yesterday """
        self._equity_yesterday = self.account["last_equity"]
        return self._equity_yesterday


    @property
    def equity_change(self):
        """ returns the change in equity from yesterday to now """
        self._equity_change = self.equity - self.equity_yesterday
        return self._equity


    def __repr__(self):
        return f"portfolio({self.equity})"


    def __str__(self):
        return f"{self.position}"
