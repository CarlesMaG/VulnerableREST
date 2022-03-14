import jwt
import datetime
from functools import wraps
from flask import request
from apiflask import APIFlask, Schema, input, output, abort
from sampleData import users

secret_key = 'd7d8c4b3-3f24-4dfd-b858-03846de91101'


def get_user_from_jwt():
    token = None
    if 'x-access-tokens' in request.headers:
        token = request.headers['x-access-tokens']
    elif 'Authorization' in request.headers:
        token = request.headers['Authorization'].replace("Bearer", "").strip()
    if not token:
        print(':( No token provided')
        return None
    try:
        data = jwt.decode(token, secret_key, algorithms=["HS256"])
        user_id = data['user_id']
        for u in users:
            if u['id'] == user_id:
                return u['id']
        print(':( User [' + user_id + '] not found')
        return None
    except Exception as e:
        print(e)
        print(':( Token is invalid')
        return None


def user_in_role(user_id, roles):
    for r in roles:
        for u in users:
            if u['id'] == user_id:
                if u['role'] == r:
                    print(':) User [' + user_id + '] belongs to required role [' + r + ']')
                    return True
    print(':( User [' + user_id + '] does not belong to required roles ' + str(roles))
    return False


def require_role(roles, message=None, status_code=401):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = get_user_from_jwt()
            if user is None or not user_in_role(user, roles):
                abort(message=message, status_code=status_code)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def generate_token(username):
    return jwt.encode({'user_id': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60000)},
               secret_key, "HS256")