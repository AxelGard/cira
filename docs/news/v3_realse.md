
# cira v3.0.0 is out!

After a long time of almost no updates v3 is finaly out. 
V3 brings some much needed features to the cira library. 

Sadly there are some breaking changes. 
But they should be easly fixed. 

## cira v2 vs v3 

most code from cira v2 will still work the only change that might be needed is that some things that was prevusaly a class `@property` such as price is 
now a accessed through a function call to make it more clear when the api is called. This also makes the docutmention easyer to read. 

So in cira **v2**

```python
import cira
stock = cira.Stock("TSLA")
print(stock.price)
```
Now in cira **v3** 
```python
import cira
stock = cira.Stock("TSLA")
print(stock.price())
```

### Alpaca file is now in auth 

there is now also a function for checking that you key is working. 

In **v2** 
```python
import cira
cira.alpaca.KEY_FILE = "../mypath/key.json"
stock = cira.Stock("TSLA")
```

but now in **v3**:

```python 
import cira
cira.auth.KEY_FILE = "../mypath/key.json"
assert cira.auth.check_keys(), "the set keys dose not work"
```


## Cira Strategies

A new module for cira v3 is strategies.
The cira strategies lets you backtest the models and set them into production in a simple way. 

the strategies have some sub modules. 

* [strategy class](../../cira/strategy/strategy.py), for you model
* [backtest](../../cira/strategy/backtest.py), for checking how your model preformce on historical data. 
* [scheduler](../../cira/strategy/scheduler.py), for scheduling of execution.


An **full example** of how to use the strategy is [example/linear](../../examples/linear.ipynb). 


```python
from cira.strategy import Strategy

class MyStrat(Strategy):
    def __init__(self) -> None:
        super().__init__(name="MyStrat")

    def iterate(self, feature_data: DataFrame, prices: DataFrame, portfolio: np.ndarray, cash:float) -> np.ndarray:
        # this mehod will be called for each row of data in the backtest 
        # the function should return the change of your portfolio. 
        # -1 means sell one stock, 0 means hold, 1 means buy one stock
        return np.array([ portfolio_change_as_int ]) 
```

cira comes with two strategies: 

* Randomness, which is will just return random values for each iteration
* BuyAndHold, which will buy as much as possible in the frist iteration then hold.

more might be added later on. 

### backtest

with cira v3 there is a new backtest function. 
there are some in v3.0.0 three types of backtests:
 
* backtest 
* backtest against buy and hold strategi 
* multi strategy backtest 

a example of how to use them is: 

```python
import cira
from cira.strategy.strategy import Randomness
from cira.strategy.backtest import back_test
from datetime import datetime
import pandas as pd

cira.auth.KEY_FILE = "../../alpc_key.json"
assert cira.auth.check_keys(), "the set keys dose not work"

stock = cira.Stock("AAPL")
df = stock.historical_data_df(datetime(2022, 1, 1), datetime(2024, 1, 1))
prices = pd.DataFrame()
prices["AAPL"] = df["close"]

strat = Randomness(-10,10, seed=23323)
bt = back_test(strat, df.copy(), prices.copy(), 10_000, True)
bt.plot()
```

If you want more full example of how to use the backtest checkout 
[multiassets](../../examples/multi_assets.ipynb) and 
[linear](../../examples/linear.ipynb).


## cryptocurncies 

Alpaca.py have support for cryptob but in cira v3.0.0 the crypto support is very minmal. 

More suppor is comming... 

## Assets class / Stock class 

There are new methods in the assets classes such as: 

```python
import cira
from datetime import datetime

stock = cira.Stock("TSLA")
df = stock.historical_data_df(datetime(2019, 1, 1), datetime(2024, 1, 1))
df # df will be a pandas data frame, were he index is a timestamp  
```