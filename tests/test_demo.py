import cira
from datetime import datetime
from pandas import Timestamp
import numpy as np
import pandas as pd

def test_demo():
    cira.auth.KEY_FILE = "" # NO KEY 
    assert not cira.auth.check_keys()

    SYMBOL = "BTC/USD"
    ast = cira.Cryptocurrency(SYMBOL)
    assert ast.price() > 0.0 # send requst to alpaca but small 

    data = pd.DataFrame({'symbol': {Timestamp('2023-07-01 05:00:00+0000', tz='UTC'): 'BTC/USD', Timestamp('2023-07-02 05:00:00+0000', tz='UTC'): 'BTC/USD', Timestamp('2023-07-03 05:00:00+0000', tz='UTC'): 'BTC/USD', Timestamp('2023-07-04 05:00:00+0000', tz='UTC'): 'BTC/USD', Timestamp('2023-07-05 05:00:00+0000', tz='UTC'): 'BTC/USD'}, 'open': {Timestamp('2023-07-01 05:00:00+0000', tz='UTC'): 30385.895956, Timestamp('2023-07-02 05:00:00+0000', tz='UTC'): 30528.37, Timestamp('2023-07-03 05:00:00+0000', tz='UTC'): 30697.0715105075, Timestamp('2023-07-04 05:00:00+0000', tz='UTC'): 31063.25735, Timestamp('2023-07-05 05:00:00+0000', tz='UTC'): 30841.5055}, 'high': {Timestamp('2023-07-01 05:00:00+0000', tz='UTC'): 30710.060945, Timestamp('2023-07-02 05:00:00+0000', tz='UTC'): 30813.870461679, Timestamp('2023-07-03 05:00:00+0000', tz='UTC'): 31390.039548221, Timestamp('2023-07-04 05:00:00+0000', tz='UTC'): 31123.8403, Timestamp('2023-07-05 05:00:00+0000', tz='UTC'): 30883.247817}, 'low': {Timestamp('2023-07-01 05:00:00+0000', tz='UTC'): 30374.97, Timestamp('2023-07-02 05:00:00+0000', tz='UTC'): 30231.36435, Timestamp('2023-07-03 05:00:00+0000', tz='UTC'): 30485.7, Timestamp('2023-07-04 05:00:00+0000', tz='UTC'): 30629.9067, Timestamp('2023-07-05 05:00:00+0000', tz='UTC'): 30204.959}, 'close': {Timestamp('2023-07-01 05:00:00+0000', tz='UTC'): 30529.743525, Timestamp('2023-07-02 05:00:00+0000', tz='UTC'): 30701.6205105075, Timestamp('2023-07-03 05:00:00+0000', tz='UTC'): 31056.9905094905, Timestamp('2023-07-04 05:00:00+0000', tz='UTC'): 30842.05240964, Timestamp('2023-07-05 05:00:00+0000', tz='UTC'): 30457.98348348}, 'volume': {Timestamp('2023-07-01 05:00:00+0000', tz='UTC'): 0.544617957, Timestamp('2023-07-02 05:00:00+0000', tz='UTC'): 1.010968445, Timestamp('2023-07-03 05:00:00+0000', tz='UTC'): 1.339711015, Timestamp('2023-07-04 05:00:00+0000', tz='UTC'): 0.421326377, Timestamp('2023-07-05 05:00:00+0000', tz='UTC'): 1.431555108}, 'trade_count': {Timestamp('2023-07-01 05:00:00+0000', tz='UTC'): 100.0, Timestamp('2023-07-02 05:00:00+0000', tz='UTC'): 104.0, Timestamp('2023-07-03 05:00:00+0000', tz='UTC'): 197.0, Timestamp('2023-07-04 05:00:00+0000', tz='UTC'): 79.0, Timestamp('2023-07-05 05:00:00+0000', tz='UTC'): 364.0}, 'vwap': {Timestamp('2023-07-01 05:00:00+0000', tz='UTC'): 30565.780444418, Timestamp('2023-07-02 05:00:00+0000', tz='UTC'): 30540.5968780593, Timestamp('2023-07-03 05:00:00+0000', tz='UTC'): 30950.9446485936, Timestamp('2023-07-04 05:00:00+0000', tz='UTC'): 30957.1352892724, Timestamp('2023-07-05 05:00:00+0000', tz='UTC'): 30443.6923107624}})
    #data = ast.historical_data_df(datetime(2023, 7, 1), datetime(2023, 7, 6)) # to not request data for each , but should be the same result 
    assert data.shape == (5, 8)
    assert data.keys().to_list() == ['symbol', 'open', 'high', 'low', 'close', 'volume', 'trade_count', 'vwap']

    strat = cira.strategy.Randomness()
    bt = cira.strategy.back_test_against_buy_and_hold(strat, data, data["open"].to_frame(), 100_000, True)
    assert np.allclose(bt[cira.strategy.ByAndHold().name].head(3).to_numpy(), np.array([99635.369248528, 100062.791380528, 100568.8959120505]))
