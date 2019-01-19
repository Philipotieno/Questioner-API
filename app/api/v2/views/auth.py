import jwt
from functools import wraps
from flask import jsonify, request
import os


from app.api.v2.models.usersmodels import User
from app.api.v2.models.db import Database

db = Database()
cur = db.cur


def authentication(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'access-token' in request.headers:
            token = request.headers['access-token']

        if not token:
            return jsonify({'message': 'Token not found'}), 401

        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'))
            query = "SELECT * from users WHERE username=%s;"
            cur.execute(query, (data['username'],))
            current_user = cur.fetchone()

        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
