# cira
A simpler libray for alpaca-trade-api from Alpaca Markets. 
Cira is available [pip](https://pypi.org/project/cira/)

![a cira](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.allthingsclipart.com%2F03%2Falpaca.001.jpg&f=1&nofb=1)

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="78" height="20" role="img" aria-label="license: MIT"><title>license: MIT</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="78" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="47" height="20" fill="#555"/><rect x="47" width="31" height="20" fill="#4c1"/><rect width="78" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="245" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="370">license</text><text x="245" y="140" transform="scale(.1)" fill="#fff" textLength="370">license</text><text aria-hidden="true" x="615" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="210">MIT</text><text x="615" y="140" transform="scale(.1)" fill="#fff" textLength="210">MIT</text></g></svg>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="64" height="20" role="img" aria-label="pypi: cira"><title>pypi: cira</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="64" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="33" height="20" fill="#555"/><rect x="33" width="31" height="20" fill="#dfb317"/><rect width="64" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="175" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="230">pypi</text><text x="175" y="140" transform="scale(.1)" fill="#fff" textLength="230">pypi</text><text aria-hidden="true" x="475" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="210">cira</text><text x="475" y="140" transform="scale(.1)" fill="#fff" textLength="210">cira</text></g></svg>
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/Axel_Gard)

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