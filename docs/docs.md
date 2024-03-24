# cira/
## cira/alpaca_utils.py
**def get_trading_client() -> TradingClient** \
`get the alpaca-sdk python trading class` \
`obj initalized with set config` 


## cira/portfolio.py
### class Position()
`None` 

> **def \_\_init\_\_(self, symbol) -> None** \
> `None` 
>
> **def quantity(self) -> int** \
> `returns the number of the assets that is owned` 
>
> **def market_value(self) -> float** \
> `Returns market value of symbol in portfolio` 
>
> **def to_dict(self) -> dict** \
> `Returns a dict of the position` 
>
> **def \_\_str\_\_(self) -> str** \
> `None` 
>
> **def \_\_repr\_\_(self) -> str** \
> `None` 
>
### class Portfolio()
`None` 

> **def \_\_init\_\_(self) -> None** \
> `None` 
>
> **def total_value(self) -> float** \
> `None` 
>
> **def is_blocked(self) -> bool** \
> `None` 
>
> **def buying_power(self) -> float** \
> `gets the amount of cash currently available` 
>
> **def cash(self) -> float** \
> `gets the amount of cash currently available` 
>
> **def equity(self) -> float** \
> `returns the amount of equity that users has` 
>
> **def equity_yesterday(self) -> float** \
> `returns the amount of equity that was` \
`available at market close yesterday` 
>
> **def equity_change(self)** \
> `returns the change in equity from yesterday to now` 
>
> **def all_positions(self) -> List[Position]** \
> `Returns all positions of portfolio` 
>
> **def close_all_positions(self) -> None** \
> `WARNING: This closes all your open positions` 
>
> **def position_in(self, symbol: str) -> Position** \
> `None` 
>
> **def get_allocation(self, symbol: str) -> int** \
> `None` 
>
> **def cancel_all_orders(self) -> None** \
> `None` 
>
> **def sell_list(self, symbols: List[str]) -> None** \
> `takes a list of Stocks and sells all stocks in that list` 
>
> **def owned_stock_qty(self, symbol: str) -> int** \
> `returns quantity of owned of a stock Stock (obj)` 
>
> **def owned_stocks_qty(self) -> Dict[(str, int)]** \
> `None` 
>
> **def owned_stocks(self) -> List[Stock]** \
> `returns a list of owned stocks` 
>
> **def \_\_repr\_\_(self)** \
> `None` 
>
> **def \_\_str\_\_(self)** \
> `None` 
>

## cira/asset.py
### class Asset()
`None` 

> **def \_\_init\_\_(self, symbol: str) -> None** \
> `Interface class` 
>
> **def historical_data_df(self, start_date: datetime, end_date: datetime) -> pd.DataFrame** \
> `None` 
>
> **def price(self) -> float** \
> `None` 
>
> **def \_\_str\_\_(self) -> str** \
> `None` 
>
> **def \_\_repr\_\_(self) -> str** \
> `None` 
>
> **def \_\_eq\_\_(self, other)** \
> `None` 
>
> **def \_\_ne\_\_(self, other)** \
> `None` 
>
### class Stock(Asset)
`None` 

> **def \_\_init\_\_(self, symbol: str) -> None** \
> `Exchange for trading stocks` 
>
> **def price(self) -> float** \
> `gets the asking price of the symbol` 
>
> **def live_data(self, async_function_to_resolve_to, run: bool=True) -> None** \
> `None` 
>
> **def _get_bars(self, start_date: datetime, end_date: datetime)** \
> `returns aplc bars from the given dates` 
>
> **def historical_data_df(self, start_date: datetime, end_date: datetime) -> pd.DataFrame** \
> `takes two dates, and returns a data frame with bars from the given dates` 
>
> **def historical_data(self, start_date: datetime, end_date: datetime) -> List[dict]** \
> `takes two dates, and returns a list of dicts with bars from the given dates` 
>
> **def buy(self, qty: float) -> None** \
> `Buy the asset,` \
`qty is the number of the asset that you buy` 
>
> **def sell(self, qty: float) -> None** \
> `Sell the asset,` \
`qty is the number of the asset that you sell` 
>
> **def buy_at(self, qty: int, price: float) -> None** \
> `Buy the asset at a given price,` \
`qty is the number of the asset that you buy` 
>
> **def sell_at(self, qty: int, price: float) -> None** \
> `Sell the asset at a given price,` \
`qty is the number of the asset that you sell` 
>
> **def save_historical_data(self, file_path, start_date: datetime, end_date: datetime) -> None** \
> `None` 
>
> **@classmethod \
def load_historical_data(cls, file_path) -> pd.DataFrame** \
> `Load in model from pickle file` \
`usage:` \
`    model = Strategy.load('./model.pkl')` \
`    predictions = model.predict(X_test)` 
>
> **def value(self) -> float** \
> `takes a string sym. Gets and returns the stock value at close` 
>
> **def order(self, qty: int, beh: str) -> float** \
> `submit order and is a template for order` 
>
> **def is_sortable(self) -> bool** \
> `checks if stock can be shorted` 
>
> **def can_borrow(self) -> bool** \
> `check whether the name is currently` \
`available to short at Alpaca` 
>
> **def barset(self, limit: int)** \
> `returns barset for stock for time period lim` 
>
> **def is_tradable(self) -> bool** \
> `return if the stock can be traded` 
>
> **def position(self)** \
> `returns position of stock` 
>
> **def today_plpc(self) -> float** \
> `stock today's profit/loss percent` 
>
> **def plpc(self) -> float** \
> `stock sym (str) Unrealized profit/loss percentage` 
>
> **def \_\_eq\_\_(self, other)** \
> `None` 
>
> **def \_\_ne\_\_(self, other)** \
> `None` 
>
> **def \_\_lt\_\_(self, other)** \
> `None` 
>
> **def \_\_le\_\_(self, other)** \
> `None` 
>
> **def \_\_gt\_\_(self, other)** \
> `None` 
>
> **def \_\_ge\_\_(self, other)** \
> `None` 
>
> **def \_\_add\_\_(self, other)** \
> `None` 
>
> **def \_\_radd\_\_(self, other)** \
> `None` 
>
> **def \_\_sub\_\_(self, other)** \
> `None` 
>
> **def \_\_rsub\_\_(self, other)** \
> `None` 
>
> **def \_\_mul\_\_(self, other)** \
> `None` 
>
> **def \_\_rmul\_\_(self, other)** \
> `None` 
>
> **def \_\_truediv\_\_(self, other)** \
> `None` 
>
> **def \_\_rdiv\_\_(self, other)** \
> `None` 
>
> **def \_\_floordiv\_\_(self, other)** \
> `None` 
>
> **def \_\_rfloordiv\_\_(self, other)** \
> `None` 
>
> **def \_\_abs\_\_(self)** \
> `None` 
>
> **def \_\_int\_\_(self)** \
> `None` 
>
> **def \_\_float\_\_(self)** \
> `None` 
>
> **def \_\_round\_\_(self, nDigits)** \
> `None` 
>
### class Cryptocurrency(Asset)
`None` 

> **def \_\_init\_\_(self, symbol: str) -> None** \
> `Exchange for trading cryptocurrencies` 
>
> **def _get_bars(self, start_date: datetime, end_date: datetime)** \
> `None` 
>
> **def historical_data_df(self, start_date: datetime, end_date: datetime) -> pd.DataFrame** \
> `None` 
>
> **def price(self) -> float** \
> `gets the asking price of the symbol` 
>

## cira/util.py
**def reformat_position(position)** \
`reformat position to be float values` 

**def bars_to_dict(bars)** \
`None` 

**def date_to_days_back(date: str)** \
`None` 


## cira/__init__.py

## cira/config.py

## cira/log.py
**def format_log_action(act: str, sym: str, qty: int) -> list** \
`formats info for logging` 

**def log(log_data: list) -> None** \
`writes log data to file` 

**def set_logging()** \
`None` 


## cira/auth.py
**def get_api_keys()** \
`None` 

**def check_keys() -> bool** \
`None` 

**def authentication_header()** \
`get's key and returns key in json format` 

**def api(version='v2')** \
`returns object for api` 


## cira/exchange.py
### class Exchange()
`None` 

> **def \_\_init\_\_(self) -> None** \
> `None` 
>
> **def is_open(self) -> bool** \
> `Checks if the exchange is open and able to trade` 
>
> **def to_assets(self, symbols: List[str]) -> List[asset.Asset]** \
> `Takes a list of symbols and returns` \
`them in a list of cira Assets objects` 
>
> **def to_asset(self, symbol: str) -> asset.Asset** \
> `Takes a symbols and returns` \
`it as a cira Assets objects` 
>
> **def get_all_stocks(self, is_tradeable: bool=True, force_reload: bool=False) -> List[asset.Stock]** \
> `Returns a list of all stocks as cira asset,` \
`objects will be cached, can be turn off in config.` 
>
> **def calendar(self, start='2018-12-01', end='2018-12-01')** \
> `None` 
>
> **def assets_raw(self)** \
> `(legacy, should not be used)` \
`returns a list of all avilabel stocks in exchanges list` 
>
> **def symbols(self)** \
> `returns a list of all symbols` 
>
### class DemoExchange(Exchange)
`None` 

> **def \_\_init\_\_(self) -> None** \
> `uses crypto client, so no need for keys, has limited usage` 
>

## cira/strategy/strategy.py
### class Strategy()
`None` 

> **def \_\_init\_\_(self, name) -> None** \
> `None` 
>
> **def iterate(self, feature_data: pd.DataFrame, prices: pd.DataFrame, portfolio: np.ndarray, cash=float) -> np.ndarray** \
> `Takes in feature data, then returns allocation prediction.` 
>
> **def save(self, file_path)** \
> `Save strategy to pickle file` \
`usage:` \
`    strategy.fit(train_data)` \
`    strategy.save('./model.pkl')` 
>
> **@classmethod \
def load(cls, file_path)** \
> `Load in strategy from pickle file` \
`usage:` \
`    strategy = Strategy.load('./model.pkl')` \
`    predictions = strategy.predict(test_data)` 
>
### class Randomness(Strategy)
`None` 

> **def \_\_init\_\_(self, lower: int=(- 1), upper: int=1, seed=0) -> None** \
> `None` 
>
> **def iterate(self, feature_data: pd.DataFrame, prices: pd.DataFrame, portfolio: np.ndarray, cash=float) -> np.ndarray** \
> `None` 
>
### class ByAndHold(Strategy)
`None` 

> **def \_\_init\_\_(self) -> None** \
> `None` 
>
> **def iterate(self, feature_data: pd.DataFrame, prices: pd.DataFrame, portfolio: np.ndarray, cash=float) -> np.ndarray** \
> `None` 
>

## cira/strategy/backtest.py
**def back_test(strat: Strategy, feature_data: pd.DataFrame, asset_prices: pd.DataFrame, capital=100000.0, use_fees: bool=True) -> pd.DataFrame** \
`DISCLAIMER: ` \
`The results of this backtest are based on historical data and do not guarantee future performance. ` \
`The financial markets are inherently uncertain, and various factors can influence actual trading results. ` \
`This backtest is provided for educational and informational purposes only. ` \
`Users should exercise caution and conduct additional research before applying any trading strategy in live markets. ` 

**def multi_strategy_backtest(strats: List[Strategy], feature_data: pd.DataFrame, asset_prices: pd.DataFrame, capital=100000.0, use_fees: bool=True)** \
`None` 

**def back_test_against_buy_and_hold(strat: Strategy, feature_data: pd.DataFrame, asset_prices: pd.DataFrame, capital=100000.0, use_fees: bool=True)** \
`None` 


## cira/strategy/__init__.py

## cira/strategy/scheduler.py
### class Scheduler()
`None` 

> **def \_\_init\_\_(self) -> None** \
> `None` 
>
> **def add_daily_job(self, func_name) -> None** \
> `None` 
>
> **def add_daily_job_at(self, func_name, time_HM: str='12:00') -> None** \
> `None` 
>
> **def add_hour_job(self, func_name) -> None** \
> `None` 
>
> **def add_minute_job(self, func_name) -> None** \
> `None` 
>
> **def add_daily_job_at_time_EDT(self, func_name, time_HM: str='12:00') -> None** \
> `None` 
>
> **def get_all_jobs(self)** \
> `None` 
>
> **def clear_all_jobs(self) -> None** \
> `None` 
>
> **def run(self)** \
> `runs the scheduler for ever` 
>

