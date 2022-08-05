# cira

Cira algorithmic trading made easy. A [Façade library](https://refactoring.guru/design-patterns/facade) for simpler interaction with alpaca-trade-API from Alpaca Markets.

Cira is available on [pip](https://pypi.org/project/cira/). **Please give it a star if you like it!**

![a cira](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F236x%2Fb6%2F42%2F3c%2Fb6423cfea7f6fcfeceeb9f852fa52ced--llama-drawing-drawing-art.jpg&f=1&nofb=1)

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

You can get started fast by using the **[cira-group boilerplate](https://github.com/cira-group/cira-boilerplate)**.
If you are new to cira checkout the [tutorial](https://github.com/AxelGard/cira/wiki/Tutorial).

### Installation
You can install it using [pip](https://pypi.org/project/cira/).
```bash
pip install cira
```

### Usage
Since the Alpaca trade API need a API key, you need to generate your own key at [alpaca markets website](https://app.alpaca.markets/signup). If you want to play around with it you can try paper trading (recommended for beginners). I recommend keep it in a **JSON file** which cira needs the **path** to.
You can also set the variables directly or use an environment variable, see the [wiki](https://github.com/AxelGard/cira/wiki/Storing-the-Alpaca-API-key) for diffrent the ways. However, it is recommended that you store it in a file just make sure not to upload that file on any public repositories. <br>
**key.json**
```json
{
  "APCA-API-KEY-ID":"your_pub_key",
  "APCA-API-SECRET-KEY":"your_private_key"
}
```
then you can start using the lib
```python
import cira
cira.alpaca.KEY_FILE = "../mypath/key.json"
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

## Things to checkout

* [News](https://github.com/AxelGard/cira/discussions/categories/news)
* [Wiki](https://github.com/AxelGard/cira/wiki/)
* [Tutorial](https://github.com/AxelGard/cira/wiki/Tutorial)
* [Storing the Alpaca API key](https://github.com/AxelGard/cira/wiki/Storing-the-Alpaca-API-key)
* [Examples of how to use cira](https://github.com/AxelGard/cira/wiki/Examples)
* [Discussions](https://github.com/AxelGard/cira/discussions)
* [Cira-group](https://github.com/cira-group)

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
