import auth
from alpaca.trading.client import TradingClient
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from .config import PAPER_TRADING


_trading_client = None


def get_trading_client() -> TradingClient:
    """get the alpaca-sdk python trading class
    obj initalized with set config"""
    global _trading_client
    if _trading_client != None:
        return _trading_client
    apca_id, apca_key = auth.get_api_keys()
    assert apca_id != "" and apca_key != "", "The keys for alpaca are not set "
    _trading_client = TradingClient(apca_id, apca_key, paper=PAPER_TRADING)
    return _trading_client


_data_client_stocks = None


def get_historical_data_client_stocks() -> StockHistoricalDataClient:
    global _data_client_stocks
    if _data_client_stocks != None:
        return _data_client_stocks
    apca_id, apca_key = auth.get_api_keys()
    assert apca_id != "" and apca_key != "", "The keys for alpaca are not set "
    _data_client_stocks = StockHistoricalDataClient(apca_id, apca_key)
    return _data_client_stocks


_data_client_crypto = None


def get_historical_data_client_crypto() -> CryptoHistoricalDataClient:
    global _data_client_crypto
    if _data_client_crypto != None:
        return _data_client_crypto
    apca_id, apca_key = auth.get_api_keys()
    _data_client_crypto = CryptoHistoricalDataClient()
    if apca_id and apca_key:
        _data_client_crypto = CryptoHistoricalDataClient(apca_id, apca_key)
    return _data_client_crypto
