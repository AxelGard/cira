import cira
from . import util
import os
import numpy as np


def test_iterate():
    feature_data = util.stock_data
    strat = cira.strategy.DollarCostAveraging(amount=1)
    prices = feature_data["close"].to_frame()
    change_in_portfolio = strat.iterate(feature_data, prices.iloc[-1], 10_000)
    assert change_in_portfolio.tolist() == [1]


def test_storing_strategy():
    CHECK = "this should be in the strategy"
    FILE = "./my_strat.pkl"

    strat = cira.strategy.Strategy("my_strat")
    strat.test_name = CHECK
    strat.save(FILE)
    new_strat = cira.strategy.Strategy.load(FILE)
    assert CHECK == new_strat.test_name

    os.system(f"rm {FILE}")


def test_backtest():
    feature_data = util.stock_data
    strat = cira.strategy.DollarCostAveraging(amount=1)
    prices = feature_data["close"].to_frame()
    prices["close"] = [10, 10, 5, 20, 10]

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 20, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [20, 20, 10, 40, 20]


def test_backtest_float():
    feature_data = util.stock_data
    strat = cira.strategy.DollarCostAveraging(amount=0.5)
    prices = feature_data["close"].to_frame()
    prices["close"] = [10, 10, 5, 20, 10]

    resutlt = cira.strategy.back_test(strat, feature_data, prices, 10, use_fees=False)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [10, 10, 5, 20, 10]


def test_backtest_fees():
    feature_data = util.stock_data
    strat = cira.strategy.DollarCostAveraging(amount=1)
    prices = feature_data["close"].to_frame()
    prices["close"] = [10, 10, 10, 10, 10]

    cira.strategy.FEE_RATE = 0.1
    resutlt = cira.strategy.back_test(strat, feature_data, prices, 100, use_fees=True)

    res = resutlt[strat.name].values.astype(int).tolist()
    assert res == [99, 98, 97, 96, 95]