import requests
import re
import locale
from bs4 import BeautifulSoup as soap

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
results = {}


def main():
    url = 'https://www.borsaitaliana.it/borsa/azioni/' \
          'obbligazioni-convertibili/dati-completi.html?isin=IT0005256059&lang=en'

    isin = re.search(r'isin=(\w+)', url, re.I).group(1)
    resource = requests.get(url)
    if not resource.text:
        print('Page is not found: ' + url)
        return ''

    content = resource.text
    # f = open('D:/Documents/test.html', 'w')
    # f.write(resource.text)
    # f.close()
    # file = open('D:/Documents/test.html', 'r')
    # content = file.read()
    # file.close()

    doc = soap(content, 'html.parser')
    rows = doc.find_all(string=re.compile('Stream Prices'))[0].find_parent('table').find_all('tr')
    if not rows:
        print('Table is empty')
        return

    columns = {}
    columns_counter = 0
    patterns = {
        r'Stream\s+Prices': 'stream',
        r'No': 'number',
        r'Bid\s+Quantity': 'bid_quantity',
        r'Ask\s+Quantity': 'ask_quantity',
        r'Bid\s+Price': 'bid',
        r'Ask\s+Price': 'ask',
    }

    keys = results.keys()
    for row in rows:
        if columns_counter < 5:
            columns = get_columns(row, patterns.items())
            columns_counter = columns.__len__()
            continue

        for column, index in columns.items():
            value = row.find_all('td')[index].text.strip()
            if not value:
                continue

            value = locale.atof(value)
            if value:
                if isin in keys:
                    results[isin][column] = value
                else:
                    results[isin] = {column: value}

    print(results)


def get_columns(row, patterns, tag='th'):
    columns = {}
    index = 0
    for cell in row.find_all(tag):
        for pattern, column in patterns:
            if re.findall(pattern, cell.text, re.I):
                columns[column] = index
        index += 1

    return columns


if __name__ == '__main__':
    main()
