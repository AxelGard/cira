# cira
A simpler libray for alpaca-trade-api from Alpaca Markets. 
Cira is available [pip](https://pypi.org/project/cira/)

![a cira](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.allthingsclipart.com%2F03%2Falpaca.001.jpg&f=1&nofb=1)

I was intrested in using the alpaca trade api for building quantitative paper trading. 
The project [paper-trader](https://github.com/AxelGard/paper-trader).<br>
However after working on this for alomst a year (of and ond agian) I relized that I had alomst build a small libray for using the alpca api.
So I thought that shuld make this in to a real lib so that you also can get started with quantitative paper trading.

The name [Cira](https://en.wikipedia.org/wiki/Cria) is the word for a baby alpca and becose this is a simpel and small lib I thoght it would be a prefect fit. 


## Getting Started

### Installation
You can install by [pip](https://pypi.org/project/cira/)
```bash
pip install cira
```

### Usage
Becose the alpca trade API need a key. <br> 
You need to keep your api key in a **json file**. Cira needs the **path** to the file.

```python
import cira
cira.KEY_FILE = "../mypath/key.json"
cira.buy(1, "TSLA")
print(cira.get_postion())
cira.sell(1, "TSLA")

```

## Versioning

### [v.0.0.1]()

## Development 
To install cira with all the dev req.
```bash
git clone git@github.com:AxelGard/cira.git
cd cira/
git checkout develop 
```
and know 
```bash
python3 -m venv env 
source env/bin/activate
pip install -e .[dev]
```


### Coding style
I have been building this i a vary [functional programming style](https://en.wikipedia.org/wiki/Functional_programming). I'm also trying to follow the [pep8](https://pep8.org/) std notation. 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


## Acknowledgments

* [alpaca API](https://alpaca.markets/)
* [paper-trader](https://github.com/AxelGard/paper-trader)