import re
import time
import requests
from pysondb import db as DB
from bs4 import BeautifulSoup

start_time = time.time()

def get_info(country, link):
    """
    Builds and returns a dictionary for each country
    by crawling the wikipedia page at the received url.
    """
    country = ' '.join([c for _, c in reversed(list(enumerate(country.replace(',_', ',').split(','))))]).replace('_', ' ')
    m, s = divmod(int(time.time() - start_time), 60)
    print(f'[{m:02d}:{s:02d}] {country}')
    info = {
        'name': country,
        'link': link,
        'capital': '',
        'largest city': '',
        'languages': '',
        'religion': '',
        'government': '',
        'area': -1.0,
        'population': -1,
        'density': -1.0,
        'driving side': '',
        'currency': '',
        'time zone': '',
        'calling code': ''
    }
    html = BeautifulSoup(requests.get(link).content, 'html.parser')
    for row in html.find('table', attrs={'class': 'infobox'}).find_all('tr'):
        th = row.find('th', attrs={'class': 'infobox-label'})
        td = row.find('td', attrs={'class': 'infobox-data'})
        if th or td:
            title = re.search(r'\w+([.\[\]\s]*\w+)*', th.text)
            if title:
                title = title.group()
                if any(s in title for s in ['Capital', 'capital']):
                    data = td.find_all('a')
                    info['capital'] = data[1].text if data[0].text == 'de jure' else data[0].text
                if any(s in title for s in ['Largest city', 'largest city']):
                    info['largest city'] = td.find('a').text
                if any(s in title for s in ['Official', 'National language', 'Major language', 'Working language']):
                    languages = [d.text for d in td.find_all('a') if not re.search(r'[\d\[]', d.text) and d.text[0].isupper()]
                    if info['languages'] == '': info['languages'] = ';'.join(languages)
                    else: info['languages'] += ';' + ';'.join(languages)
                if 'Religion' in title:
                    info['religion'] = ';'.join([d.text for d in td.find_all('a') if not re.search(r'[\d\[]', d.text) and d.text.lower() not in ['official', 'see below']])
                if 'Government' in title:
                    info['government'] = ''.join([char for char in td.text.replace('−', '-').replace('–', '-') if not char.isdigit() and char not in ['[', ']']])
                if any(s in title for s in ['Total', 'Including', 'Land']) and 'km2' in td.text:
                    info['area'] = float(re.match(r'(\d+[.,]?)+', td.text).group().replace(',', ''))
                if any(s in title for s in ['estimate', 'census']) and info['population'] < 0:
                    info['population'] = int(re.search(r'(\d+[., ]?)+', td.text).group().replace(' ', '').replace(',', ''))
                    info['density'] = float('%.1f' % (info['population'] / info['area']))
                if 'Driving' in title:
                    info['driving side'] = re.match(r'\w+', td.text).group()
                if 'Currency' in title:
                    currency = re.search(r'\(([A-Z]{2,3}|¥)', td.text)
                    if currency: info['currency'] = currency.group()[1:]
                    else: info['currency'] = re.search(r'[A-Z][a-z]+( [a-z]+)', td.text).group()
                if 'Time zone' in title:
                    time_zone = re.search(r'UTC([+-−]\d{1,2})?', td.text).group().replace('−', '-').replace('–', '-')
                    if len(time_zone) == 6 and time_zone[-2] == '0': time_zone = time_zone[:-2] + time_zone[-1]
                    info['time zone'] = time_zone
                if 'Calling code' in title:
                    code = re.match(r'\+\d+', td.text)
                    if code: info['calling code'] = code.group()
                    else: info['calling code'] = td.find('li').find('a').text
    return info

def init_db():
    """
    Initializes the JSON database, iterating through
    all the countries and adding the corresponding info.
    """
    root = 'https://en.wikipedia.org'
    html = BeautifulSoup(requests.get(f'{root}/wiki/List_of_sovereign_states').content, 'html.parser')
    db = DB.getDb('db.json')
    for row in html.find('table', attrs={'class': 'sortable'}).find_all('tr'):
        cid = row.find('span')
        if cid and cid.get('id'):
            link = row.find('a')
            if link:
                db.add(get_info(cid.get('id'), f'{root}{link.get("href")}'))

init_db()
m, s = divmod(int(time.time() - start_time), 60)
print(f'TIME {m:02d}:{s:02d}')
