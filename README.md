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

## News 

**cira v3.0.0 is now out!!**

If you want to know more about v3 check, the details are [here](./docs/news/v3_realse.md). 

If you find an issue with the new relase, open an [issue](https://github.com/AxelGard/cira/issues/new/choose). 

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
stock.buy(1)
stock.sell(1)
```

New classes with cira v.2!
```python
portfolio = cira.Portfolio() # methods for your portfolio
exchange = cira.Exchange() # methods for exchange
stock = cira.Stock("TSLA") # a class for one stock
```

### Sci-kit learn + cira 

> only for v3

I have made a simple example on how to use cira together with Sci-kit learn, using linear regression.
This model is just a toy example. 

**Checkout it out [./examples/linear.ipynb](./examples/linear.ipynb)**

### A simple algorithm  

In just a couple of lines you are up and running, with a super simple algorithm. 

```python 
import cira
import random
import time

cira.alpaca.KEY_FILE = "../mypath/key.json"

portfolio = cira.Portfolio()
exchange = cira.Exchange()

qty = 1 # choose how many stocks should be handled in one session 
while True:
    while exchange.is_open:
        for stock in random.choices(exchange.stocks, k=qty):
            stock.buy(1)
        for stock in random.choices(portfolio.owned_stocks, k=qty):
            stock.sell(1)
        time.sleep(60*30) # 30 min timer    
```

you can find more examples on the **[wiki/examples](https://github.com/AxelGard/cira/wiki/Examples)** and the **[wiki/tutorial](https://github.com/AxelGard/cira/wiki/Tutorial)** for even more information. 

### Cira Stratergies

Cira have also now (v3) support for strategies.  
An **full example** of how to use the strategy is [example/linear](../../examples/linear.ipynb). 

With strategies you can run a cira backtests.

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

#### Backtest

If your model is put into a strategy you can run a backtest on you own data.
This is a minimal setup for a backtest using the Randomness strategy included in cira.
You should of course use your own strategy, but as an example.

```python
import cira
from cira.strategy import Randomness
from cira.strategy import back_test
from datetime import datetime
import pandas as pd

cira.auth.KEY_FILE = "../../alpc_key.json"
assert cira.auth.check_keys(), "the set keys dose not work"

stock = cira.Stock("AAPL")
df = stock.historical_data_df(datetime(2022, 1, 1), datetime(2024, 1, 1))
prices = pd.DataFrame()
prices["AAPL"] = df["close"]

strat = Randomness(-10,10, seed=23323)
bt = back_test(strat, df.copy(), prices.copy(), 10_000, use_fees=True)
bt.plot()
```

If you want more full example of how to use the backtest checkout 
[multiassets](../../examples/multi_assets.ipynb) and 
[linear](../../examples/linear.ipynb).



## Things to checkout

* [News](https://github.com/AxelGard/cira/discussions/categories/news)
* [Wiki](https://github.com/AxelGard/cira/wiki/)
* [Tutorial](https://github.com/AxelGard/cira/wiki/Tutorial)
* [Storing the Alpaca API key](https://github.com/AxelGard/cira/wiki/Storing-the-Alpaca-API-key)
* [Examples of how to use cira](https://github.com/AxelGard/cira/wiki/Examples)
* [Discussions](https://github.com/AxelGard/cira/discussions)

## [Wiki](https://github.com/AxelGard/cira/wiki) and docs

To see what more you can do check out the [wiki](https://github.com/AxelGard/cira/wiki).

I also have an example of how to build a [index fund trader with cira](https://github.com/AxelGard/cira/wiki/Examples#simple-index-fund).

### Want the old version?

For backwards compatibility I made sure to fork cira in to [cira-classic](https://github.com/AxelGard/cira-classic) and cira-classic is also available on [pypi with pip](https://pypi.org/project/cira-classic/).

if you find bug plz let me know with a issue. If you know how to solve the problem then you can of course make a pull request and I will take a look at it.

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
```
Run tests using pytest. Ensure that you are in the cira dir.
But you will need a new key. This key should not only be used for testing or if you don't mind if all of the assets in the portfolio being sold.   
```bash
touch tests/test_key.json
pytest
```

### Coding style
I'm trying to follow the [pep8](https://pep8.org/) standard notation.
I try to make the library to be so intuitive as possible for easy of use.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details


## Acknowledgments

* [Alpaca API](https://alpaca.markets/)
* [paper-trader](https://github.com/AxelGard/paper-trader)
* [cira-classic](https://github.com/AxelGard/cira-classic)
