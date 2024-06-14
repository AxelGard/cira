# cira

Cira algorithmic trading made easy. A [Façade library](https://refactoring.guru/design-patterns/facade) for simpler interaction with alpaca-trade-API from Alpaca Markets.

Cira is available on [pip](https://pypi.org/project/cira/). **Please give it a star if you like it!**

<img src="https://raw.githubusercontent.com/AxelGard/cira/master/docs/img/cira.jpeg" alt="drawing" style="width:300px;"/>

![GitHub stars](https://img.shields.io/github/stars/AxelGard/Cira?style=social)
![GitHub forks](https://img.shields.io/github/forks/AxelGard/cira?style=social)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/Axel_Gard)

![GitHub](https://img.shields.io/github/license/AxelGard/cira?style=plastic)
![PyPI](https://img.shields.io/pypi/v/cira)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cira)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cira)

The name **cira** is a miss spelling of the word for a [baby alpaca cria](https://en.wikipedia.org/wiki/Cria) and because this is a simple and small lib I thought it would be a perfect fit.

[Axel Gard](https://github.com/AxelGard) is main developer for cira.

## Getting Started

If you are new to cira checkout the [tutorial](https://github.com/AxelGard/cira/wiki/Tutorial).
Or checkout an [example](https://github.com/AxelGard/cira/blob/master/examples/linear.ipynb). 

### Installation
You can install it using [pip](https://pypi.org/project/cira/).
```bash
pip install cira
```

### Usage
Since the Alpaca trade API need a API key, you need to generate your own key at [alpaca markets website](https://app.alpaca.markets/signup). If you want to play around with it you can try paper trading (recommended for beginners). I recommend keep it in a **JSON file** which cira needs the **path** to.
You can also set the variables directly or use an environment variable, see the **[wiki](https://github.com/AxelGard/cira/wiki/Storing-the-Alpaca-API-key)** for diffrent the ways. However, it is **recommended** that you store it in a file just make sure not to upload that file on any public repositories. 

You can set the Alpaca keys directly 

```python
import cira

cira.auth.APCA_API_KEY_ID = "my key" 
cira.auth.APCA_API_SECRET_KEY = "my secret key"

stock = cira.Stock("TSLA")
stock.buy(1) # buy 1 TSLA stock on alpaca 
stock.sell(1) # sell 1 TSLA stock on alpaca 
```

For interactons with alpaca you can:  
```python
portfolio = cira.Portfolio() # methods for your portfolio
exchange = cira.Exchange() # methods for exchange
stock = cira.Stock("TSLA") # a class for one stock
crypto = cira.Cryptocurrency("BTC/USD") # method for one cryptocurrency 
```

### DEMO, no keys needed 

Crypto market data can be accessed [without any alpaca keys](https://alpaca.markets/sdks/python/market_data.html#api-keys).
So there for you can try cira out with out needing to get alpaca keys. 
To put you model in production where you buy and sell you will need alpaca keys. 

Needs `cira>=3.2.2`.

```python
import cira
from datetime import datetime
import matplotlib.pyplot as plt

assert not cira.auth.check_keys() # No keys are needed

SYMBOL = "BTC/USD"
ast = cira.Cryptocurrency(SYMBOL)

print(f"The current asking price for {SYMBOL} is {ast.price()}")


# alpaca only have BTC data from 2021 and forward 
data = ast.historical_data_df(datetime(2021, 1, 1), datetime.now().date())
print(data.head())

# All of strategies and backtesting works with out keys as well. 
strat = cira.strategy.Randomness()
cira.strategy.back_test_against_buy_and_hold(strat, data, data["open"].to_frame(), 100_000).plot()
plt.savefig('./result.png')
```

you can find more examples on the **[examples repo](https://github.com/AxelGard/cira-examples)** and the **[wiki/tutorial](https://github.com/AxelGard/cira/wiki/Tutorial)** for even more information. 

### Cira Stratergies

Cira have also support for strategies.  
An **full example** of how to use the strategy is [example/linear](../../examples/linear.ipynb). 

With strategies you can run a cira backtests.

```python
from cira.strategy import Strategy
import numpy as np
import pandas as pd

class MyStrat(Strategy):
    def __init__(self) -> None:
        super().__init__(name="MyStrat")

    def iterate(self, feature_data: pd.DataFrame, prices: pd.DataFrame, portfolio: np.ndarray, cash:float) -> np.ndarray:
        # this mehod will be called for each row of data in the backtest 
        # the function should return the change of your portfolio. 
        # -1 means sell one stock, 0 means hold, 1 means buy one stock
        return np.array([ portfolio_change_as_int_or_float ]) 
```

#### Backtest

If your model is put into a strategy you can run a backtest on you own data.
This is a backtest using some of the included strategy in cira.
You can run a backtest aginst multiple strategies using the same data, this requires however that all features for all models are in the given data to the backtest.
You should of course add your own strategy, but as an example.

```python
import cira
from datetime import datetime
import matplotlib.pyplot as plt

assert not cira.auth.check_keys() # back testing against crypto do not need keys 

SYMBOL = "ETH/USD"
ast = cira.Cryptocurrency(SYMBOL)

data = ast.historical_data_df(datetime(2021, 1, 1), datetime.now().date())

strats = [
            cira.strategy.ByAndHold(),
            cira.strategy.DollarCostAveraging(0.8),
            cira.strategy.Randomness(-100, 100, seed=None, use_float=True),
            # add your own strategy and compare your model against other models
        ]
cira.strategy.multi_strategy_backtest(strats, data, data["open"].to_frame(), 100_000).plot()
plt.savefig("./result.png")
```

If you want more full example of how to use the backtest checkout 
[multiassets](../../examples/multi_assets.ipynb) and 
[linear](../../examples/linear.ipynb).



## Things to checkout

* [News](https://github.com/AxelGard/cira/discussions/categories/news)
* [Wiki](https://github.com/AxelGard/cira/wiki/)
* [Tutorial](https://github.com/AxelGard/cira/wiki/Tutorial)
* [Storing the Alpaca API key](https://github.com/AxelGard/cira/wiki/Storing-the-Alpaca-API-key)
* [Examples of how to use cira](https://github.com/AxelGard/cira-examples)
* [Discussions](https://github.com/AxelGard/cira/discussions)

### [Wiki](https://github.com/AxelGard/cira/wiki) and docs

To see what more you can do check out the [wiki](https://github.com/AxelGard/cira/wiki).

### Want the old version?

For backwards compatibility I made sure to fork cira in to [cira-classic](https://github.com/AxelGard/cira-classic) and cira-classic is also available on [pypi with pip](https://pypi.org/project/cira-classic/).

**If you find bug plz let me know with a issue.** If you know how to solve the problem then you can of course make a pull request and I will take a look at it.

### Have a question?

If you have a question about cira, want to share what you built with cira or want to talk to others using cira,
you can checkout the [discussions page](https://github.com/AxelGard/cira/discussions) or make issue if that is more fitting.

### History of cira 

I was interested in using the Alpaca trade API for building a quantitative paper trader.
The project is available [here](https://github.com/AxelGard/paper-trader).<br>
However after working on this for alomst a year (off and on) I realized that I had alomst build a small library for using the Alpaca API.
So I thought that I would make this into a real library so that you can get started with quantitative paper trading as well.

## Development
If you want to help develop cira you are more then welcome to do so.
Feel free to make a pull request or issue.
To install cira with all the dev req.
```bash
git clone git@github.com:AxelGard/cira.git
cd cira/
git checkout develop
```
and know you need to  
```bash
python3 -m venv env
source env/bin/activate
pip install -e .
pip install -r requirements.txt
```
Run tests using pytest. Ensure that you are in the cira dir.
But you will need a new key. This key should not only be used for testing or if you don't mind if all of the assets in the portfolio being sold.   
```bash
pytest -rP
```

### Coding style
I'm trying to follow the [pep8](https://pep8.org/) standard notation.
I try to make the library to be so intuitive as possible for easy of use.

I enforce [black formater](https://github.com/psf/black) when you commit code, by [pre-commit githooks](https://git-scm.com/docs/githooks#_pre_commit) to keep it some what well formated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details. 


## Acknowledgments

* [Alpaca API](https://alpaca.markets/)
* [paper-trader](https://github.com/AxelGard/paper-trader)
* [cira-classic](https://github.com/AxelGard/cira-classic)
