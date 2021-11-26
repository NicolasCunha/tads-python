from config import app, db

from flask import request

from model.user import User

from utils.string_utils import str_empty
from utils.http_utils import create_response

from service.user_service import user_exists, create_user

HTTP_OK = 200
HTTP_ERR = 500

@app.route('/user/login', methods=['post'])
def login():
    request_data = request.get_json()

    user_login = str(request_data['login'])
    user_pwd = str(request_data['pwd'])

    response = {};
    response["login_ok"] = False
    
    if str_empty(user_login):
        response["msg"] = "User login can't be empty"
        return create_response(response, HTTP_ERR)
    
    if str_empty(user_pwd):
        response["msg"] = "User password can't be empty"
        return create_response(response, HTTP_ERR)

    user = db.session.query(User).filter(User.login == user_login).filter(User.pwd == user_pwd).all()

    response["login_ok"] = True if user else False

    return create_response(response, HTTP_OK)

@app.route('/user/signup', methods=['post'])
def signup():
    request_data = request.get_json()

    login = str(request_data['login'])
    pwd = str(request_data['pwd'])
    email = str(request_data['email'])
    name = str(request_data['name'])

    response = {}
    response["signup_ok"] = False

    result = user_exists(login, email)

    if not result["status"]:
        if result["msg"]:
            response["msg"] = result["msg"]
        else:
            response["msg"] = "Email {email} or user {user} already exists".format(user=login, email=email)
        
        print(result)
        return create_response(response, HTTP_OK)
    
    result = create_user(login, pwd, email, name)

    if result["status"]:
        response["signup_ok"] = True
    else:
        response["msg"] = result["msg"]

    return create_response(response, HTTP_OK)


    

