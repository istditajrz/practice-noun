# I hate this syntax btw VVVVVVV
from flask import Flask, request, send_from_directory
import sqlite3

app = Flask(__name__)

app.debug = True

DB = "./sets.db"

@app.route('/public/<path:path>')
def public(path):
    return send_from_directory('public', path)

@app.route('/', methods=['GET'])
def index():
    with open('./public/index.html') as f:
        return f.read()

@app.route('/sets')
def sets():
    with open('./public/second.html') as f:
        return f.read()

@app.route('/data/<path:endpoint>')
def data(endpoint):
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        if endpoint == "set_names.json":
            return {
                "sets": [item[0] for item in cur.execute('select name from sets')]
            }
        elif endpoint.startswith('sentences/'):
            stripped_endpoint = str(endpoint)[len('sentences/'):]
            return "Not Implemented", 501
        elif endpoint.endswith('.json'):
            e = endpoint[:-len(".json")]
            result = cur.execute(
                "select name, subject, object, reflexive, \"possessive adjective\", \"possessive pronoun\" from sets where name =:name ;", 
                {"name": e }
            ).fetchone()
            if result == None:
                return 'null', 404
            else:
                return {
                    "name":                 result[0],
                    "subject":              result[1],
                    "object":               result[2],
                    "reflexive":            result[3],
                    "possessive adjective": result[4],
                    "possessive pronoun":   result[5]
                }
