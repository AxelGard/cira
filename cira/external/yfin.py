import yfinance as yf
from datetime import datetime

class YFinacne:
    def __init__(self) -> None:
        pass

    def get(self, ticker:str, start_date:datetime, end_date:datetime=datetime.now()):
        start_date = start_date.date().strftime("%Y-%m-%d")
        end_date = end_date.date().strftime("%Y-%m-%d")
        return yf.download(ticker, start=start_date, end=end_date, progress=False)
