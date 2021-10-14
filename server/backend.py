import sys, inspect

from config import app, FLASK_PORT, db
from flask import request, Response, jsonify
from reflection_utils import is_avaiable_class, get_class_from_str
from data.pessoa import Pessoa

@app.route('/listar/<string:classe>', methods=['get'])
def common_get(classe):
    if not is_avaiable_class(classe):
        return classe + ' is not a valid class.'

    cls = get_class_from_str(classe)
    result = db.session.query(cls).all()
    result_json = [iterator.to_json() for iterator in result]
    result_json = jsonify(result_json)

    return result_json

@app.route('/incluir/<string:classe>', methods=['post'])
def common_post(classe):
    if not is_avaiable_class(classe):
        return classe + ' is not a valid class.'

    response = jsonify({'resultado': 'ok', 'detalhes': 'ok'})
    request_json = request.get_json()

    try:
        obj = Pessoa(**request_json)
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        response = jsonify({'resultado':'erro', 'detalhes':str(e)})

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    
@app.route('/delete/<string:classe>', methods=['delete'])
def common_delete(classe):
    if not is_avaiable_class(classe):
        return classe + ' is not a valid class.'

    response = jsonify({'resultado': 'ok', 'detalhes': 'ok'})
    request_json = request.get_json()
    try:
        Pessoa.query.filter(Pessoa.id == request_json['id']).delete()
        db.session.commit()
    except Exception as e:
        response = jsonify({'resultado':'erro', 'detalhes':str(e)})

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

app.run(port = FLASK_PORT)