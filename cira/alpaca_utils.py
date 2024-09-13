import auth
from alpaca.trading.client import TradingClient
from cira import config


def get_trading_client() -> TradingClient:
    """get the alpaca-sdk python trading class
    obj initalized with set config"""
    apca_id, apca_key = auth.get_api_keys()
    assert apca_id != "" and apca_key != "", "The keys for alpaca are not set "
    return TradingClient(apca_id, apca_key, paper=config.PAPER_TRADING)
