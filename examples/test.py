import cira
import pandas as pd 
import numpy as np
from typing import List, Dict

from datetime import datetime

cira.auth.KEY_FILE = "../alpc_key.json"
import os
assert cira.auth.check_keys(), "the set keys dose not work"


portfolio = cira.Portfolio()

assets_symbols = ["MSFT", "TSLA", "AMZN"]
stk_hist_data = {}
IS_CACHED = True

for SYMBOL in assets_symbols:
    SYM_HIST_FILE = f"./examples/{SYMBOL}.csv"
    stk = cira.Stock(SYMBOL)

    if not IS_CACHED:
        start = datetime(2015, 7, 1)
        end = datetime(2023, 7, 1)
        stk.save_historical_data(SYM_HIST_FILE, start, end)
    
    data = stk.load_historical_data(SYM_HIST_FILE)
    stk_hist_data[SYMBOL] = data



df = pd.DataFrame()

for sym, hist in stk_hist_data.items():
    df[sym] = hist["close"]

df["CASH"] = 1.0


import pandas as pd
import numpy as np
from typing import List
from cira.strategy.strategy import Strategy, ByAndHold

fees = lambda prices, allocation: 0.004 * np.matmul(prices.T, allocation)

def back_test(
    strat: Strategy,
    feature_data: pd.DataFrame,
    asset_prices: pd.DataFrame,
    capital=100_000.0,
    use_fees: bool = True
):
    portfolio_history = {
        "value": [],
        "timestamp": [],
    }
    assert len(feature_data) == len(asset_prices)
    total_value = capital
    nr_of_asset = np.zeros([len(asset_prices.keys())], int)
    nr_of_asset[-1] = capital
    i = 0
    for t, cur_price in asset_prices.iterrows():
        if len(asset_prices) == i + 1: break
        if total_value > 0: 
            f_data = feature_data.iloc[: i + 1]
            p_data = asset_prices.iloc[: i + 1]
            allocation = strat.iterate(f_data, p_data, nr_of_asset.copy())
            allocation = np.maximum(nr_of_asset, allocation)
            asking = np.matmul(cur_price.values.T, allocation) + use_fees*fees(cur_price.values, allocation) - allocation[-1]
            if capital - asking > 0: 
                capital -= asking
                nr_of_asset += allocation
                nr_of_asset[-1] = capital
                nr_of_asset = np.maximum(nr_of_asset, np.zeros_like(nr_of_asset))
                total_value = np.matmul(cur_price.values.T, nr_of_asset) #+ capital 
        portfolio_history["timestamp"].append(t)
        portfolio_history["value"].append(total_value)
        i+= 1
 
    df = pd.DataFrame(portfolio_history)
    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index.get_level_values("timestamp"))
    df.rename(columns={'value': strat.name}, inplace=True)
    return df


from cira.strategy.strategy import Randomness

back_test(Randomness(-8,8), df, df, 100_000, True).plot()
import matplotlib as plt


#for _ in range(4):
    #back_test_against_buy_and_hold(Randomness(-8,8), df, df, 100_000, True).plot()
