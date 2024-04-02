import cira
from . import util
import os


def test_iterate():
    feature_data = util.stock_data
    strat = cira.strategy.Randomness(seed=2**12)
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
