import time
import requests
from re import match, search
from pysondb import db as DB
from bs4 import BeautifulSoup

start_time = time.time()

def get_info(country, link):
    """
    Builds and returns a dictionary for each country by crawling 
    the wikipedia page at the received url.
    """
    country = ' '.join([c for c in country.replace(',_', ',').split(',')[::-1]]).replace('_', ' ')
    m, s = divmod(int(time.time() - start_time), 60)
    print(f'[{m:02d}:{s:02d}] {country}')
    info = {
        'name': country,
        'link': link,
        'capital': '',
        'largest city': '',
        'languages': [],
        'religions': [],
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
            title = search(r'\w+([.\[\]\s]*\w+)*', th.text)
            if title:
                title = title.group()
                if any(s in title for s in ['Capital', 'capital']):
                    data = [d.text for d in td.find_all('a')]
                    info['capital'] = data[1] if data[0] == 'de jure' else data[0]
                if any(s in title for s in ['Largest city', 'largest city']):
                    info['largest city'] = td.find('a').text
                if any(s in title for s in ['Official', 'National lang', 'Major lang', 'Working lang']):
                    data = [d.text for d in td.find_all('a')]
                    lang = [d for d in data if not search(r'[\d\[]', d) and d[0].isupper()]
                    if not data:
                        lang = [d.text for d in td.find_all('li')]
                        if lang == []: lang = [td.text]
                    info['languages'] += lang
                if 'Religion' in title:
                    data = [d.text for d in td.find_all('a')]
                    relg = [d for d in data if not search(r'[\d\[]', d) and d.lower() not in ['official', 'see below']]
                    info['religions'] += relg
                if 'Government' in title:
                    data = td.text.replace('−', '-').replace('–', '-').replace(' ', ' ')
                    govt = [d for d in data if not d.isdigit() and d not in ['[', ']']]
                    info['government'] = ''.join(govt)
                if any(s in title for s in ['Total', 'Including', 'Land']) and 'km2' in td.text:
                    info['area'] = float(match(r'(\d+[.,]?)+', td.text).group().replace(',', ''))
                if any(s in title for s in ['estimate', 'census']) and info['population'] < 0:
                    info['population'] = int(search(r'(\d+[., ]?)+', td.text).group().replace(' ', '').replace(',', ''))
                    info['density'] = float('%.1f' % (info['population'] / info['area']))
                if 'Driving' in title:
                    info['driving side'] = match(r'\w+', td.text).group()
                if 'Currency' in title:
                    curr = search(r'\(([A-Z]{2,3}|¥)', td.text)
                    if curr: info['currency'] = curr.group()[1:]
                    else: info['currency'] = search(r'[A-Z][a-z]+( [a-z]+)', td.text).group()
                if 'Time zone' in title:
                    tz = search(r'UTC([+-−]\d{1,2})?', td.text).group().replace('−', '-').replace('–', '-')
                    if len(tz) == 6 and tz[-2] == '0': tz = tz[:-2] + tz[-1]
                    if len(tz) == 5 and tz[-1] == '0': tz = tz[:-2]
                    info['time zone'] = tz
                if 'Calling code' in title:
                    code = match(r'\+\d+', td.text)
                    if code: info['calling code'] = code.group()
                    else: info['calling code'] = td.find('li').find('a').text
    return info

def init_db():
    """
    Initializes the JSON database, iterating through all countries 
    and adding the corresponding info.
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
