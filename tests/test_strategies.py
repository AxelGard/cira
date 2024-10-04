import cira
import numpy as np
import pandas as pd 

def test_strategy_buy_and_hold():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.strategies.BuyAndHold(fee_rate=0.0)
    prices = pd.DataFrame({"close":[10, 10, 15, 20, 10]})

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 10, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [10, 10, 15, 20, 10]

def test_strategy_buy_and_hold_fee_rate():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 

    FEE_RATE = 0.5

    strat = cira.strategy.strategies.BuyAndHold(fee_rate=FEE_RATE)
    prices = pd.DataFrame({"close":[10, 10, 15, 20, 10]})

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 20, use_fees=True, fee_rate=FEE_RATE)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [15, 15, 20, 25, 15]