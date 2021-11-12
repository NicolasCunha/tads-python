from config import app, db

from flask import request, Response, jsonify

from model.user import User

HTTP_OK = 200
HTTP_ERR = 500

@app.route('/user/login', methods=['post'])
def login():
    request_data = request.get_json()

    user_login = str(request_data['login'])
    user_pwd = str(request_data['pwd'])
    
    if str_empty(user_login):
        return create_response("User login can't be empty", HTTP_ERR)
    
    if str_empty(user_pwd):
        return create_response("User password can't be empty", HTTP_ERR)

    return create_response('OK', HTTP_OK)

@app.route('/user/signup', methods=['post'])
def signup():
    request_data = request.get_json()

    login = str(request_data['login'])
    pwd = str(request_data['pwd'])
    email = str(request_data['email'])
    name = str(request_data['name'])

    user = User(login, pwd, email, person_name=name)

    db.session.add(user)
    db.session.commit()

    return create_response('OK', HTTP_OK)

def create_response(msg, status):
    response = jsonify({'msg':msg})
    response.status = status
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def str_empty(arg):
    try:
        if arg and arg.strip():
            #is not None AND myString is not empty or blank
            return False
        return True
    except Exception as e:
        return True
    

