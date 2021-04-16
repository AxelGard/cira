# import alpaca_trade_api as tradeapi
from . import config
from . import alpaca
from . import logging
from . import util


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self._price = 0
        self._value = 0
        self._is_shortable = False
        self._can_borrow = False
        self._barset = None
        self._week_pl_change = 0
        self._is_tradable = False
        self._position = None
        self._today_plpc = 0
        self._plpc = 0
        self._is_open = False

    @property
    def price(self):  # PREV: current_price
        """ returns the current price of given symbol (str) """
        if not self.exchange_is_open:
            self._price = self.value
        else:
            # OBS: due to API change no diffrence btween price and value 
            self._price = self.barset(1)[self.symbol][0].c 
        return self._price

    @property
    def value(self):  # prev: value_of_stock
        """ takes a string sym. Gets and returns the stock value at close """
        nr_days = 1
        bars = self.barset(nr_days)
        if bars is None:
            self._value = 0
        else:
            self._value = bars[self.symbol][0].c  # get stock at close
        return self._value
        
    def buy(self, qty: int):
        """ buys a stock. Takes int qty and a string sym """
        order_ = self.order(qty, "buy")
        if config.IS_LOGGING:
            logging.log(logging.format_log_action("buy", self.symbol, qty))
        return order_

    def sell(self, qty: int):
        """ sells a stock. Takes int qty and a string sym"""
        order_ = self.order(qty, "sell")
        if config.IS_LOGGING:
            logging.log(logging.format_log_action("sell", self.symbol, qty))
        return order_

    def order(self, qty: int, beh: str):
        """ submit order and is a template for order """
        if not self.is_tradable:
            raise Exception(f"Sorry, {self.symbol} is currantly not tradable on https://alpaca.markets/")
        else: 
            order = alpaca.api().submit_order(
                symbol=self.symbol, qty=qty, side=beh,
                type="market", time_in_force="gtc"
            )
            return order

    @property
    def is_shortable(self):
        """ checks if stock can be shorted """
        self._is_shortable = alpaca.api().get_asset(self.symbol).shortable
        return self._is_shortable

    @property
    def can_borrow(self):
        """check whether the name is currently
        available to short at Alpaca"""
        self._can_borrow = alpaca.api().get_asset(self.symbol).easy_to_borrow
        return self._can_borrow

    def barset(self, limit):
        """ returns barset for stock for time period lim """
        self._barset = alpaca.api().get_barset(self.symbol, "minute", limit=int(limit))
        return self._barset

    def historical_data(self, nr_days=1000):
        """returns a list of the stocks closing value,
        range of 1 to 1000 days"""
        lst = []
        nr_days = max(1, min(nr_days, 1000))
        for bar in self.barset(nr_days)[self.symbol]:
            lst.append(bar.c)
        return lst

    @property
    def week_pl_change(self):
        """ Percentage change over a week """
        nr_days = 5
        bars = self.barset(nr_days)
        week_open = bars[self.symbol][0].o
        week_close = bars[self.symbol][-1].c
        self._week_pl_change = (week_close - week_open) / week_open
        return self._week_pl_change

    @property
    def is_tradable(self):
        """ return if the stock can be traded  """
        self._is_tradable = alpaca.api().get_asset(self.symbol).tradable
        return self._is_tradable

    @property
    def position(self):
        """ returns position of stock """
        pos = alpaca.api().get_position(self.symbol)
        self._position = util.reformat_position(pos)
        return self._position

    @property
    def today_plpc(self):
        """ stock today's profit/loss percent """
        self._today_plpc = util.reformat_position(self.position)[
            "unrealized_intraday_plpc"
        ]
        return self._today_plpc

    @property
    def plpc(self):
        """ stock sym (str) Unrealized profit/loss percentage """
        self._plpc = util.reformat_position(self.position)["unrealized_plpc"]
        return self._plpc

    @property
    def exchange_is_open(self):
        """ returns if exchange is open """
        self._is_open = alpaca.api().get_clock().is_open
        return self._is_open

    def __repr__(self):
        return f"{self.symbol}@(${self.price})"

    def __str__(self):
        return f"{self.symbol}"

    # Operators

    def __eq__(self, other):
        if isinstance(other,(int,float)):
            return self.price == other
        return self.price == other.price

    def __ne__(self, other):
        if isinstance(other,(int,float)):
            return self.price != other
        return self.price != other.price

    def __lt__(self, other):
        if isinstance(other,(int,float)):
            return self.price < other
        return self.price < other.price

    def __le__(self, other):
        if isinstance(other,(int,float)):
            return self.price <= other
        return self.price <= other.price

    def __gt__(self, other):
        if isinstance(other,(int,float)):
            return self.price > other
        return self.price > other.price

    def __ge__(self, other):
        if isinstance(other,(int,float)):
            return self.price >= other
        return self.price >= other.price

    # Arithmetic Operators

    def __add__(self, other):
        if isinstance(other,(int,float)):
            return self.price + other
        return self.price + other.price
    
    def __radd__(self, other):
        return self.price + other

    def __sub__(self, other):
        if isinstance(other,(int,float)):
            return self.price - other
        return self.price - other.price

    def __rsub__(self, other):
        return self.price - other

    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return self.price * other
        return self.price * other.price

    def __rmul__(self, other):
        return self.price * other
        
    def __truediv__(self, other):
        if isinstance(other,(int,float)):
            return self.price / other
        return self.price / other.price

    def __rdiv__(self, other):
        return self.price / other

    def __floordiv__(self, other):
        if isinstance(other,(int,float)):
            return self.price // other
        return self.price // other.price

    def __rfloordiv__(self, other):
        return self.price // other
        
    # Type Conversion

    def __abs__(self):
        # dose not rely makes sense should not be able to
        # be neg but might be good to have
        return abs(self.price)

    def __int__(self):
        return int(self.price)

    def __float__(self):
        return float(self.price)

    def __round__(self, nDigits):
        return round(self.price, nDigits)
