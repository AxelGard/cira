import pandas as pd
import numpy as np
from typing import List

fees = lambda price, qty: .004 * price * qty
buy_and_hold = lambda data_ser, initial_capital: data_ser * initial_capital - data_ser[0]*initial_capital

def back_test(model, data_set:pd.Series, x_features_names:List[str], y_name:str, capital=100_000.0, threshold = 0.01, use_fees:bool = True):
    """
    
    usage: 
        back_test(model, test_data, ["open", "high", "low"], "close")
    """
    _portfolio = {
        "capital":[],
        "timestamp":[]
    }  
    stk_q = 0  
    for i, _ in enumerate(data_set[y_name]):
        if len(data_set) == i+1: break
        y_pred = model.predict(data_set[x_features_names][:1+i])
        close_price = data_set[y_name][1+i] 
        for i in range(len(y_pred)):
            diff = y_pred[-1] - data_set[y_name][i]
            if diff > threshold: # Buy
                capital -= close_price - fees(close_price, 1) * use_fees
                stk_q += 1 
            elif diff < -threshold and stk_q > 0: # Sell
                capital += close_price - fees(close_price, 1) * use_fees
                stk_q -= 1 
            else: # Hold 
                pass
        _portfolio["capital"].append(capital + stk_q*close_price)
        _portfolio["timestamp"].append(data_set.index[i])

    df = pd.DataFrame(_portfolio)
    df = df.set_index("timestamp")
    df.index = pd.to_datetime(df.index.get_level_values('timestamp'))
    return df
        

def model_vs_buy_and_hold(model, data_set:pd.Series, x_features_names:List[str], y_name:str, capital=100_000.0, threshold = 0.01, use_fees:bool = True):
    """
    
    usage: 
        bh_res, model_res = back_test(model, test_data, ["open", "high", "low"], "close")
        plt.plot(bh_res, label="by and hold")
        plt.plot(model_res, label="model")
        plt.legend()
        plt.show()
    """

    bh_res = buy_and_hold(data_set[y_name][1:], capital) 
    model_res = back_test(model, data_set, x_features_names, y_name, threshold=threshold, capital=capital, use_fees=use_fees)
    return bh_res, model_res
