from flask import Flask, Response
from pysondb import db as DB

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def bad_request_page():
    return '<head><title>400 Bad Request</title></head>\
        <body><h1 style="margin-top: 1.5rem">Bad Request</h1><p>Wrong key</p></body>'

@app.route('/')
@app.route('/countries/')
@app.route('/countries/all/')
def all_countries():
    """
    Returns an array of JSON objects, each one corresponding to
    a specific country and containing all the data found about it.
    """
    db = DB.getDb('db.json').getAll()
    for j in db:
        for key in j.keys():
            j[key] = j[key].split(';') if key in ['languages', 'religion'] else j[key]
    return db

@app.route('/countries/by/<string:key>/')
def countries_by_key(key):
    """
    Returns an array of JSON objects that contain only the name
    and the value corresponding to the given key for each country.
    If the given key is `name`, the JSON objects contain only
    the name of the countries.
    """
    db = DB.getDb('db.json').getAll()
    key = key.lower().replace('-', ' ')
    if key not in db[0].keys():
        return Response(bad_request_page(), status=400)
    if key == 'name':
        return [{key: j[key]} for j in db]
    if key in ['languages', 'religion']:
        return [{'name': j['name'], key: j[key].split(';')} for j in db]
    return [{'name': j['name'], key: j[key]} for j in db]

@app.route('/countries/by/<string:key>/top/')
@app.route('/countries/by/<string:key>/top/<int:k>/')
def top_by_key(key, k=207):
    """
    If the given key is `area`, `population` or `density`, the API
    endpoint returns an array of JSON objects containing the name
    and the value corresponding to the given key for each country
    sorted descending by this value. If `k` is specified, only
    the first `k` objects will be returned.
    """
    if key not in ['area', 'population', 'density']:
        return Response(bad_request_page(), status=400)
    db = [{'name': j['name'], key: j[key]} for j in DB.getDb('db.json').getAll()]
    return sorted(db, key=lambda d: d[key], reverse=True)[:k]

@app.route('/countries/by/<string:key>/<string:value>/')
def countries_by_key_value(key, value):
    """
    Returns an array of JSON objects containing the name and the pair
    `(key, value)` for each country that matches the given pair.
    """
    db = DB.getDb('db.json').getAll()
    key = key.replace('+', ' ').replace('-', ' ')
    if key in ['name', 'capital', 'largest city', 'languages', 'religion', 'government']:
        value = value.lower().replace('+', ' ')
        if key == 'name':
            return [{key: j[key]} for j in db if value == j[key].lower()]
        if key in ['capital', 'largest city']:
            return [{'name': j['name'], key: j[key]} for j in db if value == j[key].lower()]
        if key in ['languages', 'religion']:
            return [{'name': j['name'], key: j[key].split(';')} for j in db if any(v for v in j[key].split(';') if value in v.lower())]
        if key == 'government':
            return [{'name': j['name'], key: j[key]} for j in db if value in j[key].lower()]
    if key in ['area', 'population', 'density', 'driving side', 'currency', 'time zone', 'calling code', 'id']:
        return [{'name': j['name'], key: j[key]} for j in db if value.lower() == str(j[key]).lower()]
    return Response(bad_request_page(), status=400)
