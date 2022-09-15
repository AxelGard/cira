from alpaca.trading import TradingClient
import alpaca
from ..auth import get_api_keys

class Asset: 
    
    def __init__(self, symbol="", alpaca_model_asset=None) -> None:  
        self.alpaca_model_asset = alpaca_model_asset
        assert symbol != "" or type(alpaca_model_asset) == alpaca.trading.models.Asset, "An asset needs a symbol or a alpaca "
        _id, _key = get_api_keys()
        self.trade_client = TradingClient(_id, _key)
        
        self.symbol=None
        if type(alpaca_model_asset) == alpaca.trading.models.Asset: 
            self.symbol = alpaca_model_asset.symbol
        else: 
            self.symbol = symbol 
            self.alpaca_model_asset = self.trade_client.get_asset(symbol) 
        
        self._price = 0.0
        self.asset_class = str(self.alpaca_model_asset.asset_class)
        self.exchange = str(self.alpaca_model_asset.exchange)
        self.name = str(self.alpaca_model_asset.name)
        
    def price(self) -> float:
        raise NotImplementedError("Please Implement a price function")

    def submit(self, order): 
        market_order = self.trading_client.submit_order(
                order_data=order
                )
        return market_order
        
        
    def buy(self, qty:int):
        from alpaca.trading.requests import MarketOrderRequest
        from alpaca.trading.enums import OrderSide, TimeInForce

        market_order_data = MarketOrderRequest(
                    symbol=self.symbol,
                    qty=qty,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )
        self.submit(market_order_data)

    def sell(self, qty:int): 
        from alpaca.trading.requests import MarketOrderRequest
        from alpaca.trading.enums import OrderSide, TimeInForce

        market_order_data = MarketOrderRequest(
                    symbol=self.symbol,
                    qty=qty,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY
                    )
        self.submit(market_order_data)
   
    
    def to_dict(self):
        return {
            "symbol":self.symbol,
            "name":self.name,
            "price":self.price(),
        }

    def __str__(self) -> str:
        return str(self.symbol)