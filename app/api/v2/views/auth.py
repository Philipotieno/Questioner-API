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

        if 'Authorization' in request.headers:
            token = request.headers.get("Authorization")

        if not token:
            return jsonify({'message': 'Token not found'}), 401

        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY' algoriths='HS256'))
            query = "SELECT * from users WHERE username=%s;"
            cur.execute(query, (data['username'],))
            current_user = cur.fetchone()

        except Exception as e:
            return jsonify({'message': 'An error occured while decoding token.', 'error':str(e)}), 400

        return f(current_user, *args, **kwargs)

    return decorated
