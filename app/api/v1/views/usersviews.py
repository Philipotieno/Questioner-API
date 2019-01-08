from flask import Blueprint
from app.api.v1.models.usersmodels import User
import os

v1_user = Blueprint('users', __name__)

user_inst = User() #meetup class instance


@v1_user.route('/register', methods=['POST'])
def registered_user():
	pass