

class PositionSizer:
    def __init__(self, risk_percentage, stop_loss_price, max_position_size:int=100):
        assert risk_percentage <= 1.0 and risk_percentage >= 0.0, "risk percentage needs to be between 0 and 1"
        self.risk_percentage = risk_percentage 
        self.stop_loss_price = stop_loss_price
        self.max_position_size = max_position_size

    def size(self, capital, entry_price, is_buy_signal, current_position):
        available_capital = capital - (current_position * entry_price) if is_buy_signal else capital
        risk_per_trade = available_capital * self.risk_percentage
        position_size = risk_per_trade / (entry_price - self.stop_loss_price)
        position_size = min(int(position_size), self.max_position_size)
        return int(position_size) if is_buy_signal else -int(position_size)