"""
Cira 

A simpler libray for alpaca-trade-api from Alpaca Markets.
"""

from time import gmtime 
from time import strftime
import json
import csv
import alpaca_trade_api as tradeapi

__version__ = "0.0.2"
__author__ = 'Axel Gard'
__credits__ = 'alpacahq markets'


KEY_FILE = ""
LOGGING = False
LOG_FILE = ""


# Auth 

def authentication_header():
    """ get's key and returns key in json format """
    with open(KEY_FILE, 'r') as file:
        header = json.load(file)
    return header

def api():
    """ returns object for api """
    auth_header = authentication_header()
    APCA_API_KEY_ID = str(auth_header["APCA-API-KEY-ID"])
    APCA_API_SECRET_KEY = str(auth_header["APCA-API-SECRET-KEY"])
    # Open the API connection
    api = tradeapi.REST(
        APCA_API_KEY_ID,
        APCA_API_SECRET_KEY,
        'https://paper-api.alpaca.markets'
    )
    # Get account info
    api.get_account()
    return api

def exchange_open():
    """ returns if exchange is open """
    clock = api().get_clock()
    return clock.is_open


def order(sym, qty, beh):
    """ submit order and is a
    template for order """
    order = api().submit_order(
        symbol=sym,
        qty=qty,
        side=beh,
        type='market',
        time_in_force='gtc')

    return order


def buy(qty, sym):
    """ buys a stock.
    takes int qty and a string sym """
    order_ = order(sym, qty, 'buy')
    if LOGGING:
        log(format_log_action('buy', sym, qty))
    return order_


def sell(qty, sym):
    """ sells a stock.
    takes int qty and a string sym"""
    order_ = order(sym, qty, 'sell')
    if LOGGING:
        log(format_log_action('sell', sym, qty))
    return order_


def is_shortable(sym):
    """ checks if stock can be shorted """
    asset = api().get_asset(sym)
    return asset.shortable


def can_borrow(sym):
    """ check whether the name is currently
    available to short at Alpaca """
    asset = api().get_asset(sym)
    return asset.easy_to_borrow


def get_barset(sym, lim):
    """ get's barset for stock for time period lim """
    lim = int(lim)
    barset = api().get_barset(sym, 'day', limit=lim)
    return barset


def value_of_stock(sym):
    """ takes a string sym.
    Gets and returns the stock value at close """
    nr_days = 1
    barset = get_barset(sym, nr_days)
    if barset is None:
        return 0
    value = barset[sym][0].c  # get stock at close
    return value


def get_week_pl_change(sym):
    """ % change over a week """
    nr_days = 5
    bars = get_barset(sym, nr_days)
    week_open = bars[sym][0].o
    week_close = bars[sym][-1].c
    return (week_close - week_open) / week_open


def get_position():
    """ create a list of all owned position """
    portfolio = api().list_positions()
    portfolio_lst = []
    for position in portfolio:
        position_dict = reformat_position(position)
        position_dict['symbol'] = position.symbol
        portfolio_lst.append(position_dict)
    return portfolio_lst


def is_tradable(sym):
    """ return if the stock can be traded  """
    asset = api().get_asset(sym)
    return asset.tradable


def nasdaq_assets():
    """ creates a list of all avilabel assets on NASDAQ """
    active_assets = api().list_assets(status='active')
    # Filter the assets to NASDAQ
    return [a for a in active_assets if a.exchange == 'NASDAQ']


def exchange_lst():
    """ returns a list of stock exchanges
    that is supported by alpaca """
    lst = ['NASDAQ', 'NYSE', 'ARCA', 'BATS']
    return lst


def stock_position(sym):
    """ takes str sym (needs to stock symbol)
    returns position of stock """
    return api().get_position(sym)


def owned_stock_qty(sym):
    """ returns quantity of owned of a stock sym (str) """
    position = reformat_position(stock_position(sym))
    return position['qty']


def current_price(sym):
    """ returns the current price of given symbol (str) """
    price = stock_position(sym)['current_price']
    return price


def owned_stocks():
    """ returns a list of owned stocks """
    lst = get_position()
    stock_lst = []
    for dict_ in lst:
        stock_lst.append(dict_['symbol'])
    return stock_lst


def reformat_position(position):
    """ reformat position to be float values """
    raw_position = vars(position)['_raw']
    position_dict = {}
    for key in raw_position.keys():
        try:
            position_dict[key] = float(raw_position[key])
        except ValueError:
            continue
    return position_dict


def stock_today_plpc(sym):
    """ stock today's profit/loss percent """
    dict_ = reformat_position(stock_position(sym))
    return dict_['unrealized_intraday_plpc']


def stock_plpc(sym):
    """ stock sym (str) Unrealized profit/loss percentage """
    dict_ = reformat_position(stock_position(sym))
    return dict_['unrealized_plpc']


def sell_list(lst):
    """ takes a list of symbols (str) and
    sells all stocks in that list """
    for sym in lst:
        qty = int(owned_stock_qty(sym))
        #if not sym == 'GOOGL':  # google has problem selling, to few buyers??
        sell(qty, sym)
    return None

# LOG 

def format_log_action(act, sym, qty):
    """ formats info for logging """
    time_ = strftime("%Y-%m-%d %H:%M", gmtime())
    log_data = [act, sym, qty, time_]
    return log_data


def log(log_data):
    """ writes log data to file """
    file_path = "trader/log/log.csv"
    with open(file_path, 'a') as file:
        # fd.write(log_data)
        writer = csv.writer(file)
        writer.writerow(log_data)
    return None
