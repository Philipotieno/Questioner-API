from flask import Blueprint, jsonify, request
from app.api.v1.models.usersmodels import User
import os

v1_user = Blueprint('users', __name__)

user_inst = User() #user class instance


@v1_user.route('/', methods=['POST'])
def registered_user():
	data = request.get_json()
	firstname = data["firstname"]
	lastname = data["lastname"]
	username = data["username"]
	email = data["email"]
	phone = data["phone"]
	password = data["password"]

	return jsonify({'message': 'User Registered successfully!'}), 201