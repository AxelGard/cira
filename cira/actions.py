from .strategy import Strategy
from .asset import Asset, Stock

def threshold_buy_sell(ast:Stock, strategy:Strategy, buy=0.01, sell=0.01, qty = 1):
    """
    Use given thresholds movement for buy and sell action.
    Similar to back test.
    """
    cur = ast.current_price()
    y_pred = strategy.predict([cur])
    diff = y_pred[-1] - cur 
    if diff > buy: # Buy
        ast.buy(qty)
    elif diff < sell: # Sell
        ast.sell(qty)
    else: # Hold 
        pass