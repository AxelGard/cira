import pandas as pd
import numpy as np
from typing import List

fees = lambda price, qty: .004 * price * qty

def buy_and_hold(data_set:pd.DataFrame, capital, use_fees:bool = True) -> pd.DataFrame:
    _portfolio = {
        "capital":[],
        "timestamp":[]
    }  
    init_price = data_set["close"].values[0]
    stk_q = capital // init_price 
    capital -= (use_fees * fees(init_price, stk_q))
    stk_q = capital // init_price 
    
    for t, row in data_set.iterrows():
        cur_price = row["close"]
        _portfolio["capital"].append(stk_q*cur_price)
        _portfolio["timestamp"].append(t)

    df = pd.DataFrame(_portfolio)
    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index.get_level_values('timestamp'))
    return df
    

def back_test(model, position_sizer, data_set:pd.DataFrame, x_features_names:List[str], y_name:str, capital=100_000.0, threshold = 0.01, use_fees:bool = True):
    """
    
    usage: 
        back_test(model, position_sizer test_data, ["open", "high", "low"], "close")
    """
    _portfolio = {
        "capital":[],
        "timestamp":[],
        "allocation":[],
    }  
    stk_q = 0
    i = 1

    for t, row in data_set.iterrows():
        if len(data_set) == i+1: break
        cur_price = row["close"]
        hist = data_set[x_features_names].iloc[:i+1] 
        y_pred = model.predict(hist)
        diff = y_pred[-1] - data_set[y_name].iloc[1+i]
        buy_sig = diff > threshold
        pos = position_sizer.size(capital, cur_price, buy_sig, stk_q)
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
        

def model_vs_buy_and_hold(model, sizer, data_set:pd.DataFrame, x_features_names:List[str], y_name:str, capital=100_000.0, threshold = 0.01, use_fees:bool = True):
    """
    
    usage: 
        bh_res, model_res = back_test(model, test_data, ["open", "high", "low"], "close")
        plt.plot(bh_res, label="by and hold")
        plt.plot(model_res, label="model")
        plt.legend()
        plt.show()
    """

    bh_res = buy_and_hold(data_set.copy(), capital, use_fees)
    model_res = back_test(model, sizer, data_set.copy(), x_features_names, y_name, threshold=threshold, capital=capital, use_fees=use_fees)
    return bh_res, model_res
