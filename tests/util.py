import pandas as pd
from pandas import Timestamp


stock_data = pd.DataFrame(
    {
        "symbol": {
            Timestamp("2016-01-04 05:00:00+0000", tz="UTC"): "MSFT",
            Timestamp("2016-01-05 05:00:00+0000", tz="UTC"): "MSFT",
            Timestamp("2016-01-06 05:00:00+0000", tz="UTC"): "MSFT",
            Timestamp("2016-01-07 05:00:00+0000", tz="UTC"): "MSFT",
            Timestamp("2016-01-08 05:00:00+0000", tz="UTC"): "MSFT",
        },
        "open": {
            Timestamp("2016-01-04 05:00:00+0000", tz="UTC"): 48.18,
            Timestamp("2016-01-05 05:00:00+0000", tz="UTC"): 48.72,
            Timestamp("2016-01-06 05:00:00+0000", tz="UTC"): 48.18,
            Timestamp("2016-01-07 05:00:00+0000", tz="UTC"): 46.75,
            Timestamp("2016-01-08 05:00:00+0000", tz="UTC"): 46.45,
        },
        "high": {
            Timestamp("2016-01-04 05:00:00+0000", tz="UTC"): 48.61,
            Timestamp("2016-01-05 05:00:00+0000", tz="UTC"): 49.13,
            Timestamp("2016-01-06 05:00:00+0000", tz="UTC"): 48.25,
            Timestamp("2016-01-07 05:00:00+0000", tz="UTC"): 47.44,
            Timestamp("2016-01-08 05:00:00+0000", tz="UTC"): 47.26,
        },
        "low": {
            Timestamp("2016-01-04 05:00:00+0000", tz="UTC"): 47.36,
            Timestamp("2016-01-05 05:00:00+0000", tz="UTC"): 48.38,
            Timestamp("2016-01-06 05:00:00+0000", tz="UTC"): 47.58,
            Timestamp("2016-01-07 05:00:00+0000", tz="UTC"): 46.19,
            Timestamp("2016-01-08 05:00:00+0000", tz="UTC"): 46.26,
        },
        "close": {
            Timestamp("2016-01-04 05:00:00+0000", tz="UTC"): 48.61,
            Timestamp("2016-01-05 05:00:00+0000", tz="UTC"): 48.83,
            Timestamp("2016-01-06 05:00:00+0000", tz="UTC"): 47.94,
            Timestamp("2016-01-07 05:00:00+0000", tz="UTC"): 46.28,
            Timestamp("2016-01-08 05:00:00+0000", tz="UTC"): 46.42,
        },
        "volume": {
            Timestamp("2016-01-04 05:00:00+0000", tz="UTC"): 59379610.0,
            Timestamp("2016-01-05 05:00:00+0000", tz="UTC"): 36457804.0,
            Timestamp("2016-01-06 05:00:00+0000", tz="UTC"): 41899187.0,
            Timestamp("2016-01-07 05:00:00+0000", tz="UTC"): 61897908.0,
            Timestamp("2016-01-08 05:00:00+0000", tz="UTC"): 52260304.0,
        },
        "trade_count": {
            Timestamp("2016-01-04 05:00:00+0000", tz="UTC"): 272783.0,
            Timestamp("2016-01-05 05:00:00+0000", tz="UTC"): 180639.0,
            Timestamp("2016-01-06 05:00:00+0000", tz="UTC"): 225858.0,
            Timestamp("2016-01-07 05:00:00+0000", tz="UTC"): 303273.0,
            Timestamp("2016-01-08 05:00:00+0000", tz="UTC"): 261924.0,
        },
        "vwap": {
            Timestamp("2016-01-04 05:00:00+0000", tz="UTC"): 48.05,
            Timestamp("2016-01-05 05:00:00+0000", tz="UTC"): 48.83,
            Timestamp("2016-01-06 05:00:00+0000", tz="UTC"): 47.99,
            Timestamp("2016-01-07 05:00:00+0000", tz="UTC"): 46.64,
            Timestamp("2016-01-08 05:00:00+0000", tz="UTC"): 46.74,
        },
    }
)
