from flask import jsonify

def create_response(dict, status):
    response = jsonify(dict, status)
    response.status = status
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response