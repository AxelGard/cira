from typing import List
from . import asset



class Exchange: 
    def __init__(self) -> None:
        pass

    def get_assets(self, symbols:List[str])-> List[asset.Asset]:
        raise NotImplementedError

class StockExchange(Exchange):
    def __init__(self) -> None:
        pass 

    def get_assets(self, symbols: List[str]) -> List[asset.Stock]:
        return [asset.Stock(s) for s in symbols]

class CryptoExchange(Exchange):
    def __init__(self) -> None:
        pass 