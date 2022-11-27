from flask import Flask
from pysondb import db as DB

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
@app.route('/countries/')
@app.route('/countries/all/')
def all_countries():
    return DB.getDb('db.json').getAll()

@app.route('/countries/by/<key>/')
def countries_by_key(key):
    db = DB.getDb('db.json').getAll()
    key = key.lower().replace('-', ' ')
    if key not in db[0].keys():
        return "ERROR: wrong key"
    return [{key: j[key]} for j in db]

@app.route('/countries/by/<key>/top/')
@app.route('/countries/by/<key>/top/<k>/')
def top_by_key(key, k='207'):
    if key not in ['area', 'population', 'density']:
        return "ERROR: wrong key"
    db = [{'name': j['name'], key: j[key]} for j in DB.getDb('db.json').getAll()]
    return sorted(db, key=lambda d: d[key], reverse=True)[:int(k)]

@app.route('/countries/by/<key>/<value>')
def countries_by_key_value(key, value):
    db = DB.getDb('db.json').getAll()
    key = key.replace('-', ' ')
    value = value.lower()
    if key == 'name':
        value = value.replace('-', '_').replace(' ', '_')
        return [{key: j[key]} for j in db if value == j[key].lower()]
    elif key in ['capital', 'largest city', 'driving side']:
        value = value.replace('+', ' ')
        return [{'name': j['name'], key: j[key]} for j in db if value == j[key].lower()]
    elif key in ['language', 'religion']:
        value = value.replace('-', ' ').replace('+', ' ')
        return [{'name': j['name'], key: j[key]} for j in db if any(v for v in j[key].split(';') if value in v.lower())]
    elif key == 'government':
        value = value.replace('+', ' ')
        return [{'name': j['name'], key: j[key]} for j in db if value in j[key].lower()]
    elif key in ['area', 'population', 'density']:
        return [{'name': j['name'], key: j[key]} for j in db if value == str(j[key])]
    elif key in ['time zone', 'currency', 'calling code']:
        return [{'name': j['name'], key: j[key]} for j in db if value == j[key].lower()]
    else:
        return "ERROR: wrong key"
