from flask import Flask
from pysondb import db as DB

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
@app.route('/countries/')
@app.route('/countries/all/')
def all_countries():
    db = DB.getDb('db.json').getAll()
    for j in db:
        for key in j.keys():
            j[key] = j[key].split(';') if key in ['languages', 'religion'] else j[key]
    return db

@app.route('/countries/by/<key>/')
def countries_by_key(key):
    db = DB.getDb('db.json').getAll()
    key = key.lower().replace('-', ' ')
    if key not in db[0].keys():
        return "[400] ERROR: wrong key"
    if key == 'name':
        return [{key: j[key]} for j in db]
    if key in ['languages', 'religion']:
        return [{'name': j['name'], key: j[key].split(';')} for j in db]
    return [{'name': j['name'], key: j[key]} for j in db]

@app.route('/countries/by/<key>/top/')
@app.route('/countries/by/<key>/top/<k>/')
def top_by_key(key, k='207'):
    if key not in ['area', 'population', 'density']:
        return "[400] ERROR: wrong key"
    db = [{'name': j['name'], key: j[key]} for j in DB.getDb('db.json').getAll()]
    return sorted(db, key=lambda d: d[key], reverse=True)[:int(k)]

@app.route('/countries/by/<key>/<value>/')
def countries_by_key_value(key, value):
    db = DB.getDb('db.json').getAll()
    key = key.replace('-', ' ')
    value = value.lower()
    if key == 'name':
        value = value.replace('-', '_').replace(' ', '_')
        return [{key: j[key]} for j in db if value == j[key].lower()]
    if key in ['capital', 'largest city', 'driving side']:
        value = value.replace('+', ' ')
        return [{'name': j['name'], key: j[key]} for j in db if value == j[key].lower()]
    if key in ['languages', 'religion']:
        value = value.replace('-', ' ').replace('+', ' ')
        return [{'name': j['name'], key: j[key].split(';')} for j in db if any(v for v in j[key].split(';') if value in v.lower())]
    if key == 'government':
        value = value.replace('+', ' ')
        return [{'name': j['name'], key: j[key]} for j in db if value in j[key].lower()]
    if key in ['area', 'population', 'density']:
        return [{'name': j['name'], key: j[key]} for j in db if value == str(j[key])]
    if key in ['time zone', 'currency', 'calling code']:
        return [{'name': j['name'], key: j[key]} for j in db if value == j[key].lower()]
    return "[400] ERROR: wrong key"
