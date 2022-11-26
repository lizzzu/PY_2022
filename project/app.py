import json
from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
@app.route('/countries/')
@app.route('/countries/all/')
def all_countries():
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    return db['data']

@app.route('/countries/<key>/')
def countries_key(key):
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    key = key.replace('-', ' ')
    db['data'] = [{key: j[key]} for j in db['data']]
    return db['data']

@app.route('/countries/area/top/')
@app.route('/countries/area/top/<k>/')
def top_by_area(k='207'):
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    db['data'] = [{'name': j['name'], 'area': j['area']} for j in db['data']]
    return sorted(db['data'], key=lambda d: d['area'], reverse=True)[:int(k)]

@app.route('/countries/population/top/')
@app.route('/countries/population/top/<k>/')
def top_by_population(k='207'):
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    db['data'] = [{'name': j['name'], 'population': j['population']} for j in db['data']]
    return sorted(db['data'], key=lambda d: d['population'], reverse=True)[:int(k)]

@app.route('/countries/density/top/')
@app.route('/countries/density/top/<k>')
def top_by_density(k='207'):
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    db['data'] = [{'name': j['name'], 'density': j['density']} for j in db['data']]
    return sorted(db['data'], key=lambda d: d['density'], reverse=True)[:int(k)]

@app.route('/countries/language/<language>')
def country_language(language):
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    language = language.replace('-', ' ')
    return [j for j in db['data'] if any(l for l in j['languages'].split(';') if language in l.lower())]

@app.route('/countries/religion/<religion>')
def country_religion(religion):
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    religion = religion.replace('-', ' ')
    return [j for j in db['data'] if any(r for r in j['religion'].split(';') if religion in r.lower())]

@app.route('/countries/government/<government>')
def country_government(government):
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    return [j for j in db['data'] if government in j['government'].lower()]

@app.route('/countries/time-zone/<time_zone>')
def country_time_zone(time_zone):
    db = json.load(open('db.json', 'r', encoding='utf-8'))
    return [{'name': j['name'], 'time zone': j['time zone']} for j in db['data'] if time_zone == j['time zone'].lower()]
