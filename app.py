from flask import Flask, request, send_from_directory
import sqlite3, re, typing

app = Flask(__name__)

app.debug = True

DB = "./sets.db"

PRONOUN_RE = re.compile(r"\[[A-z ]+\]")

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
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        if endpoint == "set_names.json":
            return {
                "sets": [item[0] for item in cur.execute('select name from sets')]
            }
        elif endpoint.startswith('sentences/'):
            endpoint = str(endpoint)[len('sentences/'):]
            pronoun_set = cur.execute(
                "select name, subject, object, reflexive, \"possessive adjective\", \"possessive pronoun\" from sets where name =:name limit 1;", 
                {"name": endpoint[:-len(".json")] }
            ).fetchone()
            pronoun_set = dict(zip(pronoun_set.keys(), map(str, pronoun_set)))
            ammount = request.args.get("ammount", default=1, type=int)
            sentences = cur.execute(
                """select * from sentences
                order by random() asc
                LIMIT 2;"""#,
                # { "l": ammount }
            ).fetchmany(2) #ammount)
            def replace(s: str) -> str:
                index = 0
                out = ""
                for m in re.finditer(PRONOUN_RE, s):
                    replacement = pronoun_set[m[0].lower()[1:-1]]
                    if m[0][1:-1].isupper():
                        replacement = replacement.capitalize()
                    out += s[index:m.start()] + "[" + replacement + "]"
                    index = m.end()
                out += s[index:]
                return out
            return {
                    "sentences": list(map(lambda x: replace(x['sentence']), sentences))
                }
        elif endpoint.endswith('.json'):
            e = endpoint[:-len(".json")]
            result = cur.execute(
                "select name, subject, object, reflexive, \"possessive adjective\", \"possessive pronoun\" from sets where name =:name limit 1;", 
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
