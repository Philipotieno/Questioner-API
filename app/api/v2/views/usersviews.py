import os
import psycopg2
from flask import Blueprint, jsonify, request

from app.api.v2.models.usersmodels import User

from app.api.v2.models.db import Database

v2_user = Blueprint('users', __name__)

db = Database()
cur = db.conn.cursor()

@v2_user.route('/register', methods=['POST'])
def registered_user():
	pass
	
@v2_user.route('/login', methods=['POST'])
def login():
	pass