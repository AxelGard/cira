# cira
A simpler libray for alpaca-trade-api from Alpaca Markets. 
Cira is available [pip](https://pypi.org/project/cira/). Plz give it a star if you like it!

![a cira](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.allthingsclipart.com%2F03%2Falpaca.001.jpg&f=1&nofb=1)

![GitHub stars](https://img.shields.io/github/stars/AxelGard/Cira?style=social)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/Axel_Gard)

![GitHub](https://img.shields.io/github/license/AxelGard/cira?style=plastic)
![PyPI](https://img.shields.io/pypi/v/cira)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cira)

I was intrested in using the alpaca trade api for building quantitative paper trading. 
The project [paper-trader](https://github.com/AxelGard/paper-trader).<br>
However after working on this for alomst a year (of and ond agian) I relized that I had alomst build a small libray for using the alpca api.
So I thought that shuld make this in to a real lib so that you also can get started with quantitative paper trading.

The name [Cira](https://en.wikipedia.org/wiki/Cria) is the word for a baby alpca and becose this is a simpel and small lib I thoght it would be a prefect fit. 


## Getting Started

### Installation :arrow_down:
You can install by [pip](https://pypi.org/project/cira/)
```bash
pip install cira
```

### Usage
Becose the alpca trade API need a key. <br> 
You need to keep your api key in a **json file**. Cira needs the **path** to the file.

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

To se more you can what you can do check out the [wiki](https://github.com/AxelGard/cira/wiki)

I also have an exampel of how to build a [index fund with Cira](https://axelgard.github.io/blog/cira/2020/08/20/cira-index-fund.html)

## Versioning :page_with_curl:

still in some what of early stages. 
However I have been using this for alomst a year now.<br>
There will most likey be quite raped updates in the beging due to bug and what not that will ecure due to the move from my own project [paper-trader](https://github.com/AxelGard/paper-trader). 

if you find bug plz let me know with a issue or if you think you know what the problem is you can ofcourse make a pull request an I will take a look at it. :smiley:

## Development :wrench:
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

### Coding style
I have been building this i a vary [functional programming style](https://en.wikipedia.org/wiki/Functional_programming). I'm also trying to follow the [pep8](https://pep8.org/) std notation. 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details


## Acknowledgments

* [alpaca API](https://alpaca.markets/)
* [paper-trader](https://github.com/AxelGard/paper-trader)