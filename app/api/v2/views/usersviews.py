from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

#local imports
from app.api.v2.models.usersmodels import User
from app.api.v2.views.validator import validate_register
from app.api.v2.models.db import Database
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, get_jwt_identity,
                                jwt_refresh_token_required)

db = Database()
cur = db.cur

v2_user = Blueprint('v2_users', __name__)


@v2_user.route('/register', methods=['POST'])
def registered_user():
    '''function to log in users'''
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Body should contaib json data!'}), 500
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

        new_user = user_details.register_user()
        return jsonify({'message': 'User Registered successfully!', "data" : new_user}), 201

    except Exception:
        return jsonify({'status':400, 'message': "data field cannot be empty"}), 400

    
@v2_user.route('/login', methods=['POST'])
def login():
    '''View function to log in'''
    try:
        data = request.get_json()
        if not data or not data["username"] or not data["password"]:
            return jsonify({'message': 'Username or password field cannot be empty!'}), 400

        query = "SELECT username, password from users WHERE username=%s;"
        cur.execute(query, (data['username'],))
        user = cur.fetchone()

        if not user:
            return jsonify({'message': 'Incorrect username'}), 401

        if check_password_hash(user['password'], data["password"]):
            access_token = create_access_token(identity=data['username'])
            return jsonify({'message': 'You are now logged in', 
                            'access_token': access_token}), 200

        return jsonify({'message': 'Incorrect password'}), 401

    except Exception:
        return jsonify({'message': "data field cannot be empty"}), 400