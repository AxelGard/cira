from . import alpaca
from . import stock


class Exchange:
    def __init__(self):
        self.name = ""
        self.exchanges = [
            "NASDAQ",
            "NYSE",
            "ARCA",
            "BATS",
        ]  # list of stock exchanges that is supported by alpaca
        self._is_open = False
        self._assets = []
        self._symbols = []  # ["sym", ... ]
        self._stocks = []  # [Stock(sym), ... ] obj
        self._historical_data = {}

    @property
    def is_open(self):
        """ returns if exchange is open """
        self._is_open = alpaca.api().get_clock().is_open
        return self._is_open

    def assets_raw(self):
        """ returns a list of all avilabel stocks in exchanges list """
        all_assets = []
        active_assets = alpaca.api().list_assets(status="active")
        for exchange in self.exchanges:
            all_assets += [a for a in active_assets if a.exchange == exchange]
        self._assets = all_assets
        return self._assets

    @property
    def symbols(self):
        """ returns a list of all symbols """
        self._symbols = []
        for asset in self.assets_raw():
            self._symbols.append(asset.__dict__["_raw"]["symbol"])
        return self._symbols

    @property
    def stocks(self):
        """ returns a list of objects Stocks """
        self._stocks = []
        for sym in self.symbols:
            self._stocks.append(stock.Stock(sym))
        return self._stocks

    @property
    def historical_data(self):
        """ gathers all historical data on all stocks, {"sym":[data]} """
        self._historical_data = {}
        for stk in self.stocks:
            self._historical_data[stk.symbol] = stk.historical_data()
        return self._historical_data