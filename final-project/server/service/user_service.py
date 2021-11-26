from config import db
from sqlalchemy import or_
from model.user import User

def user_exists(login, email):

    result = {}
    result["status"] = False

    try:
        user = db.session.query(User).filter(or_(User.login == login, User.email == email)).all()
        result["status"] = True if user else False
    except Exception as ex:
        result["msg"] = str(ex)
    
    return result

def create_user(login, pwd, email, name):
    result = {}
    result["status"] = False
    try:
        user = User(login=login, pwd=pwd, email=email, person_name=name)
        db.session.add(user)
        db.session.commit()
        result["status"] = True
    except Exception as ex:
        result["msg"] = str(ex)

    return result