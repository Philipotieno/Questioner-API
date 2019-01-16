import os
import psycopg2
from flask import Blueprint, jsonify, request

from app.api.v2.models.questionssmodels import Question

from app.api.v2.models.db import Database

v2_user = Blueprint('users', __name__)

db = Database()
cur = db.conn.cursor()

@v2_questions.route('', methods=['POST'])
def create_question():
	pass

@v2_questions.route('', methods=['GET'])
def view_all_question():
	pass

@v2_questions.route('', methods=['GET'])
def fetch_specific_question():
	pass

@v2_questions.route('', methods=['DELETE'])
def delete_question():
	pass