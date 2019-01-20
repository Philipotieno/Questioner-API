import os
import psycopg2
from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

#local imports
from app.api.v2.models.usersmodels import User
from app.api.v2.views.validator import validate_register
from app.api.v2.views.auth import authentication
from app.api.v2.models.db import Database

db = Database()
cur = db.cur

v2_user = Blueprint('v2_users', __name__)

@v2_user.route('/register', methods=['POST'])
def registered_user():
    data = request.get_json()
    if validate_register(data):
    	return validate_register(data)

    query = "SELECT username from users;"
    cur.execute(query)
    usernames = cur.fetchall()
    for name in usernames:
        if name['username'] == data['username']:
            return jsonify({'message': 'User already exists!'}), 409
            
    hashed_password = generate_password_hash(data['password'], method='sha256')
    user_details = User(
        data['firstname'],
        data['lastname'],
        data['username'],
        data['phone_number'],
        data['email'],
        hashed_password
    )

    if user_details.register_user():
        return jsonify({'message': 'User Registered successfully!'}), 201
    return jsonify({'message': 'User already exists!'}), 409

@v2_user.route('/users/<user_id>', methods=['PUT'])
@authentication
def add_admin(current_user, user_id):
    user = User.get_user_by_id(user_id)
    if current_user['username'] == 'superUser':
        if user:
            query = "UPDATE users SET admin='true' WHERE user_id=%s"
            cur.execute(query, (user_id, ))
            db.conn.commit()
            return jsonify({'message': 'Admin added successfully'}), 200
        return jsonify({'message': 'User does not exist!'}), 404
    return jsonify({'message': 'You are not authorized to perform this function!'}),
    
@v2_user.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data["username"] or not data["password"]:
        return jsonify({'message': 'Username and password required!'}), 400

    query = "SELECT username, password from users WHERE username=%s;"
    cur.execute(query, (data['username'],))
    user = cur.fetchone()

    if not user:
        return jsonify({'message': 'Incorrect username'}), 401

    if check_password_hash(user['password'], data["password"]):
        token = jwt.encode(
            {"username" : user["username"],
            "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=720)},
            os.getenv('SECRET_KEY'), 'HS256').decode('UTF-8')
        return jsonify({'message': 'You are now logged in', 
                        'token': token}), 200

    return jsonify({'message': 'Incorrect password'}), 401
