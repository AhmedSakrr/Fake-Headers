# Or use my header parser:
# https://raw.githubusercontent.com/TheDevFromKer/Headers-Parser

from bs4 import BeautifulSoup
from requests import get

versions = []
text = get('https://en.wikipedia.org/wiki/Google_Chrome_version_history').text
bs = BeautifulSoup(text, 'html5lib')

table = bs.find('table', {'style': 'font-size:95%;'})
body = table.find('tbody')
rows = body.findAll('tr')

for row in rows:
    try:
        ver = row.find('td').text
        versions.append(ver.strip())
    except Exception:
        pass

print(versions)
