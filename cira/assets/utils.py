from .asset import Asset
from .cryptocurrency import Cryptocurrency
from .stock import Stock
from alpaca.trading.enums import AssetClass

def cast_asset_class(alpc_asset_enum:AssetClass, symbol:str) -> Asset:
    if alpc_asset_enum == 'crypto':
        return Cryptocurrency(symbol)
    return Stock(symbol) 