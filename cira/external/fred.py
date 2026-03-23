from fredapi import Fred
import pandas as pd 
from datetime import datetime


class FRED:
    def __init__(self, api_key:str):
        self.client = Fred(api_key=api_key)
    
    def get(self, series_id:str, start:datetime, end:datetime) -> pd.DataFrame:
        return pd.DataFrame({series_id:self.client.get_series(series_id, start, end)})
