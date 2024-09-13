import cira
from . import util
import os
import numpy as np
import pandas as pd 


def test_iterate():
    feature_data = util.stock_data
    strat = cira.strategy.strategies.DollarCostAveraging(amount=1)
    prices = feature_data["close"].to_frame()
    change_in_portfolio = strat.iterate(feature_data, prices.iloc[-1], 10_000)
    assert change_in_portfolio.tolist() == [1]


def test_storing_strategy():
    CHECK = "this should be in the strategy"
    FILE = "./my_strat.pkl"

    strat = cira.strategy.strategy.Strategy("my_strat")
    strat.test_name = CHECK
    strat.save(FILE)
    new_strat = cira.strategy.strategy.Strategy.load(FILE)
    assert CHECK == new_strat.test_name

    os.system(f"rm {FILE}")


def test_backtest():
    feature_data = util.stock_data
    strat = cira.strategy.strategies.DollarCostAveraging(amount=1)
    prices = feature_data["close"].to_frame()
    prices["close"] = [10, 10, 5, 20, 10]

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 20, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [20, 20, 10, 40, 20]


def test_backtest_float():
    feature_data = util.stock_data
    strat = cira.strategy.strategies.DollarCostAveraging(amount=0.5)
    prices = feature_data["close"].to_frame()
    prices["close"] = [10, 10, 5, 20, 10]

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 10, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [10, 10, 5, 20, 10]


def test_backtest_fees():
    feature_data = util.stock_data
    strat = cira.strategy.strategies.DollarCostAveraging(amount=1)
    prices = feature_data["close"].to_frame()
    prices["close"] = [10, 10, 10, 10, 10]

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 100, use_fees=True, fee_rate=0.1)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [99, 98, 97, 96, 95]


def test_backtest_multi_asset_uniform_prices():
    feature_data = util.stock_data
    strat = cira.strategy.strategies.DollarCostAveraging(amount=1)

    prices = pd.DataFrame() 
    prices["ast_1"] = [10, 10, 5, 20, 10]
    prices["ast_2"] = [10, 10, 5, 20, 10]
    prices["ast_3"] = [10, 10, 5, 20, 10]
    prices["ast_4"] = [10, 10, 5, 20, 10]

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 40, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [40, 40, 20, 80, 40] 


def test_backtest_multi_asset():
    feature_data = util.stock_data
    strat = cira.strategy.strategies.DollarCostAveraging(amount=1)

    prices = pd.DataFrame()
    prices["ast_1"] = [10, 10, 1,  0, 0]
    prices["ast_2"] = [10, 11, 5,  0, 0]
    prices["ast_3"] = [10, 10, 1,  0, 0]
    prices["ast_4"] = [10, 14, 7, 99, 0]

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 40, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [40, 45, 14, 99, 0] 


def test_backtest_not_enugh_cash():
    feature_data = util.stock_data
    strat = cira.strategy.strategies.DollarCostAveraging(amount=1)
    prices = feature_data["close"].to_frame()
    prices["close"] = [10, 11, 12, 13, 14]

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 9, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [9, 9, 9, 9, 9]


def test_backtest_sell_no_allocation():
    feature_data = util.stock_data
    strat = cira.strategy.strategies.DollarCostAveraging(amount=-1)
    prices = feature_data["close"].to_frame()
    prices["close"] = [10, 11, 12, 13, 14]

    resutlt = cira.strategy.backtest.back_test(strat, feature_data, prices, 100, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [100, 100, 100, 100, 100]