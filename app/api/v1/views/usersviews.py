from flask import Blueprint, jsonify, request
from app.api.v1.models.usersmodels import User
import datetime
import os

import re

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

	email_format = re.compile(
		r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z-]+$)")
	name_format = re.compile(r"(^[A-Za-z]+$)")

	if not (re.match(name_format, firstname)):
		return jsonify({'message' : 'Invalid first name'}), 400

	if not (re.match(name_format, lastname)):
		return jsonify({'message' : 'Invalid last name'}), 400

	if not (re.match(name_format, username)):
		return jsonify({'message' : 'Invalid username'}), 400

	if len(firstname) < 4 or len(lastname) < 4 or len(username) < 4:
		return jsonify({"message" : "length of first name, last name or username is too short"}), 400

	if not password:
		return jsonify({'message' : 'password cannot be left blank'}), 400

	if len(password) < 8:
		return jsonify({'message' : 'password should be atleast 8 characters'}), 400

	if not (re.match(email_format, email)):
		return jsonify({'message' : 'Invalid email, ensure email is of the form example1@mail.com'}), 400
	
	if data['username'] in user_inst.users:
		return jsonify({"message" : "username already exists"}), 400
	
	user_inst.register_user(
		firstname=firstname,
		lastname=lastname,
		username=username,
		email=email,
		phone =phone,
		password=password,
		registered=datetime.datetime.now()
		)


	return jsonify({'message': 'User Registered successfully!', 'Users' : user_inst.users}), 201