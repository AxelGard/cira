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
    value = capital
    nr_of_asset = np.zeros([len(asset_prices.keys())], int)
    i = 0
    for t, cur_price in asset_prices.iterrows():
        if len(asset_prices) == i + 1: break
        if value > 0: 
            f_data = feature_data.iloc[: i + 1]
            p_data = asset_prices.iloc[: i + 1]
            allocation = strat.predict(f_data, p_data, capital)
            asking = np.matmul(cur_price.values.T, allocation) + use_fees*fees(cur_price.values, allocation)
            if capital - asking > 0: 
                capital -= asking
                nr_of_asset += allocation
                nr_of_asset = np.maximum(nr_of_asset, 0)
                value = np.matmul(cur_price.values.T, nr_of_asset) + capital
        
        portfolio_history["timestamp"].append(t)
        portfolio_history["value"].append(value)
 
    df = pd.DataFrame(portfolio_history)
    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index.get_level_values("timestamp"))
    df.rename(columns={'value': strat.name}, inplace=True)
    return df



def multi_strategy_backtest(strats:List[Strategy], 
    feature_data: pd.DataFrame,
    asset_prices: pd.DataFrame,
    capital=100_000.0,
    use_fees: bool = True
):
    result = pd.DataFrame()
    result.index = asset_prices.index
    for s in strats:
        s_result = back_test(
                        s, 
                        feature_data=feature_data,
                        asset_prices=asset_prices,
                        capital=capital,
                        use_fees=use_fees)
        result[s.name] = s_result[s.name]
    return result



def back_test_against_buy_and_hold(
    strat: Strategy,
    feature_data: pd.DataFrame,
    asset_prices: pd.DataFrame,
    capital=100_000.0,
    use_fees: bool = True
):
    return multi_strategy_backtest( strats=[strat, ByAndHold()],                         
                                    feature_data=feature_data,
                                    asset_prices=asset_prices,
                                    capital=capital,
                                    use_fees=use_fees)
