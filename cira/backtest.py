import pandas as pd
import numpy as np
from typing import List
from .strategy import Strategy

fees = lambda price, qty: .004 * price * qty

def buy_and_hold(data_set:pd.DataFrame, capital, entry_price_name:str="close", use_fees:bool = True) -> pd.DataFrame:
    _portfolio = {
        "capital":[],
        "timestamp":[],
        "allocation":[],
    }  
    init_price = data_set[entry_price_name].values[0]
    stk_q = capital // init_price 
    capital -= (use_fees * fees(init_price, stk_q))
    stk_q = capital // init_price 
    
    for t, row in data_set.iterrows():
        cur_price = row[entry_price_name]
        _portfolio["capital"].append(stk_q*cur_price)
        _portfolio["timestamp"].append(t)
        _portfolio["allocation"].append(stk_q)

    df = pd.DataFrame(_portfolio)
    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index.get_level_values('timestamp'))
    return df
    

def back_test(strategy:Strategy, data_set:pd.DataFrame, entry_price_name:str="close", capital=100_000.0, use_fees:bool = True):
    """
    
    usage: 
        back_test(model, position_sizer test_data, ["open", "high", "low"], "close")
    """
    #assert any(item  == False  for item in [f in data_set.keys().to_list() for f in strategy.get_features_names()]), "the given data set dose not have the features that the strategy needs"

    _portfolio = {
        "capital":[],
        "timestamp":[],
        "allocation":[],
    }  
    stk_q = 0
    i = 1

    for t, row in data_set.iterrows():
        if len(data_set) == i+1: break
        cur_price = row[entry_price_name]
        hist = data_set[strategy.get_features_names()].iloc[:i+1] 
        y_pred = strategy.predict(hist)
        pos = strategy.size(cur_price, y_pred, stk_q, capital)
        if stk_q + pos <= 0: 
            pos = -stk_q
        stk_q += pos
        capital -= pos * cur_price - use_fees * fees(cur_price, pos)
        _portfolio["capital"].append(capital + stk_q*cur_price)
        _portfolio["timestamp"].append(t)
        _portfolio["allocation"].append(stk_q)
        i += 1
        if capital + stk_q*cur_price <= 0: break # went bankrupt  

    df = pd.DataFrame(_portfolio)
    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index.get_level_values('timestamp'))
    return df
        

def model_vs_buy_and_hold(strategy:Strategy, data_set:pd.DataFrame, entry_price_name:str="close", capital=100_000.0, use_fees:bool = True):
    """
    
    usage: 
        bh_res, model_res = back_test(model, test_data, ["open", "high", "low"], "close")
        plt.plot(bh_res, label="by and hold")
        plt.plot(model_res, label="model")
        plt.legend()
        plt.show()
    """

    bh_res = buy_and_hold(data_set=data_set.copy(), entry_price_name=entry_price_name, capital=capital, use_fees=use_fees)
    model_res = back_test(strategy=strategy, data_set=data_set.copy(), entry_price_name=entry_price_name, capital=capital, use_fees=use_fees)
    return bh_res, model_res
