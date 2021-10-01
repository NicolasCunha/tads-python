import sys, inspect

from config import app, FLASK_PORT, db
from flask import Response, jsonify
from reflection_utils import is_avaiable_class, get_class_from_str
from data.pessoa import Pessoa

@app.route('/listar/<string:classe>')
def common_get(classe):
    if not is_avaiable_class(classe):
        return classe + ' is not a valid class.'

    cls = get_class_from_str(classe)
    result = db.session.query(cls).all()
    result_json = [iterator.to_json() for iterator in result]
    result_json = jsonify(result_json)
    result_json.headers.add('Access-Control-Allow-Origin', '*')

    return result_json
    

app.run(port = FLASK_PORT, debug = True)