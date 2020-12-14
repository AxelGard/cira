# cira
A simpler library for alpaca-trade-api from Alpaca Markets.
Cira is available on [pip](https://pypi.org/project/cira/). **Plz give it a star if you like it!**

![a cira](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.allthingsclipart.com%2F03%2Falpaca.001.jpg&f=1&nofb=1)

![GitHub stars](https://img.shields.io/github/stars/AxelGard/Cira?style=social)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/Axel_Gard)

![GitHub](https://img.shields.io/github/license/AxelGard/cira?style=plastic)
![PyPI](https://img.shields.io/pypi/v/cira)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cira)

I was interested in using the Alpaca trade API for building a quantitative paper trader.
The project is available [here](https://github.com/AxelGard/paper-trader).<br>
However after working on this for alomst a year (off and on) I realized that I had alomst build a small library for using the Alpaca API.
So I thought that I would make this into a real library so that you can get started with quantitative paper trading as well.

The name [cira](https://en.wikipedia.org/wiki/Cria) is the word for a baby alpaca and because this is a simple and small lib I thought it would be a perfect fit.


## Getting Started

### Installation
You can install it using [pip](https://pypi.org/project/cira/).
```bash
pip install cira
```

### Usage
Since the Alpaca trade API need a key, you need to generate your own and keep it in a **JSON file** which cira needs the **path** to.
You can also set the variables directly or use an environment variable. However, it is recommended that you store it in a file.<br>
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
cira.KEY_FILE = "../mypath/key.json"
cira.buy(1, "TSLA")
print(cira.get_postion())
cira.sell(1, "TSLA")
```

## [Wiki](https://github.com/AxelGard/cira/wiki) and docs 

To see what more you can do check out the [wiki](https://github.com/AxelGard/cira/wiki).

I also have an example of how to build a [index fund trader with cira](https://axelgard.github.io/blog/cira/2020/08/20/cira-index-fund.html) or check out [paper-trader](https://github.com/AxelGard/paper-trader) for my usage of cira.

## Versioning & News 

cira still has some things that need be implemented in order to be enter a v0.1.0, for exampel stock shorting and support for more stock markets than NASDAQ. 

if you find bug plz let me know with a issue. If you know how to solve the problem then you can of course make a pull request and I will take a look at it.

## Development 
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
pip install -e .[dev]
```
Run tests using pytest. Ensure that you are in the cira dir.
But you will need a new key. This key should not only be used for testing or if you don't mind if all of the assets in the portfolio being sold.   
```bash
touch tests/test_key.json
pytest
```


### Coding style
I have been building this in a very [functional programming style](https://en.wikipedia.org/wiki/Functional_programming). I'm also trying to follow the [pep8](https://pep8.org/) standard notation.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details


## Acknowledgments

* [Alpaca API](https://alpaca.markets/)
* [paper-trader](https://github.com/AxelGard/paper-trader)
