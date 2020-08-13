# cira
A simpler libray for alpaca-trade-api from Alpaca Markets. 
Cira is available [pip](https://pypi.org/project/cira/)

![a cira](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.allthingsclipart.com%2F03%2Falpaca.001.jpg&f=1&nofb=1)

![GitHub stars](https://img.shields.io/github/stars/AxelGard/Cira?style=social)
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="61" height="20" ><style>a:hover #llink{fill:url(#b);stroke:#ccc}a:hover #rlink{fill:#4183c4}</style><linearGradient id="a" x2="0" y2="100%"><stop offset="0" stop-color="#fcfcfc" stop-opacity="0"/><stop offset="1" stop-opacity=".1"/></linearGradient><linearGradient id="b" x2="0" y2="100%"><stop offset="0" stop-color="#ccc" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><g stroke="#d5d5d5"><rect stroke="none" fill="#fcfcfc" x="0.5" y="0.5" width="60" height="19" rx="2"/></g><image x="5" y="3" width="14" height="14" xlink:href="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMURBMUYyIiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+VHdpdHRlciBpY29uPC90aXRsZT48cGF0aCBkPSJNMjMuOTU0IDQuNTY5Yy0uODg1LjM4OS0xLjgzLjY1NC0yLjgyNS43NzUgMS4wMTQtLjYxMSAxLjc5NC0xLjU3NCAyLjE2My0yLjcyMy0uOTUxLjU1NS0yLjAwNS45NTktMy4xMjcgMS4xODQtLjg5Ni0uOTU5LTIuMTczLTEuNTU5LTMuNTkxLTEuNTU5LTIuNzE3IDAtNC45MiAyLjIwMy00LjkyIDQuOTE3IDAgLjM5LjA0NS43NjUuMTI3IDEuMTI0QzcuNjkxIDguMDk0IDQuMDY2IDYuMTMgMS42NCAzLjE2MWMtLjQyNy43MjItLjY2NiAxLjU2MS0uNjY2IDIuNDc1IDAgMS43MS44NyAzLjIxMyAyLjE4OCA0LjA5Ni0uODA3LS4wMjYtMS41NjYtLjI0OC0yLjIyOC0uNjE2di4wNjFjMCAyLjM4NSAxLjY5MyA0LjM3NCAzLjk0NiA0LjgyNy0uNDEzLjExMS0uODQ5LjE3MS0xLjI5Ni4xNzEtLjMxNCAwLS42MTUtLjAzLS45MTYtLjA4Ni42MzEgMS45NTMgMi40NDUgMy4zNzcgNC42MDQgMy40MTctMS42OCAxLjMxOS0zLjgwOSAyLjEwNS02LjEwMiAyLjEwNS0uMzkgMC0uNzc5LS4wMjMtMS4xNy0uMDY3IDIuMTg5IDEuMzk0IDQuNzY4IDIuMjA5IDcuNTU3IDIuMjA5IDkuMDU0IDAgMTMuOTk5LTcuNDk2IDEzLjk5OS0xMy45ODYgMC0uMjA5IDAtLjQyLS4wMTUtLjYzLjk2MS0uNjg5IDEuOC0xLjU2IDIuNDYtMi41NDhsLS4wNDctLjAyeiIvPjwvc3ZnPg=="/><g aria-hidden="false" fill="#333" text-anchor="middle" font-family="Helvetica Neue,Helvetica,Arial,sans-serif" text-rendering="geometricPrecision" font-weight="700" font-size="110px" line-height="14px"><a target="_blank" xlink:href="https://twitter.com/intent/tweet?text=Wow:&amp;url=https%3A%2F%2Ftwitter.com%2FAxel_Gard"><text aria-hidden="true" x="385" y="150" fill="#fff" transform="scale(.1)" textLength="330">Tweet</text><text x="385" y="140" transform="scale(.1)" textLength="330">Tweet</text><rect id="llink" stroke="#d5d5d5" fill="url(#a)" x=".5" y=".5" width="60" height="19" rx="2" /></a></g></svg>

![GitHub](https://img.shields.io/github/license/AxelGard/cira?style=plastic)
![PyPI](https://img.shields.io/pypi/v/cira)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cira)

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

## Versioning

still in some what of early stages. 
However I have been using this for alomst a year now.<br>
There will most likey be quite raped updates in the beging due to bug and what not that will ecure due to the move from my own project [paper-trader](https://github.com/AxelGard/paper-trader). 

if you find bug plz let me know with a issue or if you think you know what the problem is you can ofcourse make a pull request an I will take a look at it. :smiley:

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
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details


## Acknowledgments

* [alpaca API](https://alpaca.markets/)
* [paper-trader](https://github.com/AxelGard/paper-trader)