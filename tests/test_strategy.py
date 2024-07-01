import cira
import os
import numpy as np
import pandas as pd 



def test_save_strategy():
    CHECK = "this should be in the strategy"
    FILE = "./my_strat.pkl"

    strat = cira.strategy.Strategy("my_strat")
    strat.test_name = CHECK
    strat.save(FILE)
    new_strat = cira.strategy.Strategy.load(FILE)
    assert CHECK == new_strat.test_name

    os.system(f"rm {FILE}")


def test_backtest():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=1)
    prices = pd.DataFrame({"close":[10, 10, 5, 20, 10]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 20, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [20, 20, 10, 40, 20]


def test_backtest_float():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=0.5)
    prices = pd.DataFrame({"close":[10, 10, 5, 20, 10]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 10, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [10, 10, 5, 20, 10]


def test_backtest_fees():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=1)
    prices = pd.DataFrame({"close":[10, 10, 10, 10, 10]}) 

    cira.strategy.FEE_RATE = 0.1
    resutlt = cira.strategy.back_test(strat, feature_data, prices, 100, use_fees=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [99, 98, 97, 96, 95]


def test_backtest_multi_asset_uniform_prices():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=1)

    prices = pd.DataFrame() 
    prices["ast_1"] = [10, 10, 5, 20, 10]
    prices["ast_2"] = [10, 10, 5, 20, 10]
    prices["ast_3"] = [10, 10, 5, 20, 10]
    prices["ast_4"] = [10, 10, 5, 20, 10]

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 40, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [40, 40, 20, 80, 40] 


def test_backtest_multi_asset():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=1)

    prices = pd.DataFrame()
    prices["ast_1"] = [10, 10, 1,  0, 0]
    prices["ast_2"] = [10, 11, 5,  0, 0]
    prices["ast_3"] = [10, 10, 1,  0, 0]
    prices["ast_4"] = [10, 14, 7, 99, 0]

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 40, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [40, 45, 14, 99, 0] 


def test_backtest_not_enugh_cash():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=1)
    prices = pd.DataFrame({"close":[10, 11, 12, 13, 14]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 9, use_fees=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [9, 9, 9, 9, 9]


def test_backtest_sell_no_allocation():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=-1)
    prices = pd.DataFrame({"close":[10, 11, 12, 13, 14]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 100, use_fees=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [100, 100, 100, 100, 100]


def test_backtest_short_position_posetive_ROI():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=-1)
    prices = pd.DataFrame({"close":[10, 10, 9, 9, 9]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 10, use_fees=False, allow_short_position=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [10, 10, 12, 12, 12]


def test_backtest_short_position_negativ_ROI():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=-1)
    prices = pd.DataFrame({"close":[10, 10, 11, 11, 11]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 10, use_fees=False, allow_short_position=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [10, 10, 8, 8, 8]


def test_backtest_short_position_posetive_ROI_with_fees():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=-1)
    prices = pd.DataFrame({"close":[10, 10, 8, 8, 8]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 100, use_fees=True, allow_short_position=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [99, 98, 100 - 2 + 2*(10-8) - 1, 100, 99]


def test_backtest_short_position_negativ_ROI_with_fees():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=-1)
    prices = pd.DataFrame({"close":[10, 10, 20, 20, 20]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 100, use_fees=True, allow_short_position=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [99, 98, 100 - 2 - 2*10 - 2, 74, 72]



def test_backtest_short_position_margin_call():
    feature_data = pd.DataFrame({"my_featrue":[1,2,3,4,5]}) 
    strat = cira.strategy.DollarCostAveraging(amount=-1)
    prices = pd.DataFrame({"close":[10, 100, 100, 100, 100]})

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 100, use_fees=True, allow_short_position=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [99, -1, -1, -1, -1]