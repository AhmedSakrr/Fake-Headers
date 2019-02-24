from bs4 import BeautifulSoup
from requests import get

versions = []
text = get('https://www.mozilla.org/en-US/firefox/releases/').text
bs = BeautifulSoup(text, 'html5lib')

div = bs.find('div', {'id': 'main-content'})
table = div.find('ol', {'reversed': ''})
rows = table.findAll('li')

for row in rows:
    try:
        first = row.find('strong')
        second = first.find('a').text
        versions.append(second)

        first = row.find('ol')
        second = first.findAll('li')

        for item in second:
            a = item.find('a').text
            versions.append(a)

    except Exception:
        pass

print(versions)
