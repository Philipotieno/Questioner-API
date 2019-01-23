import os
import psycopg2
from flask import Blueprint, jsonify, request
import json

from app.api.v2.models.questionsmodel import Question
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.api.v2.views.validator import validate_questions
from app.api.v2.models.db import Database

v2_questions = Blueprint('v2_uestions', __name__)

db = Database()
cur = db.cur

@v2_questions.route('', methods=['POST'])
@jwt_required
def create_question():
    """ Creates a question """
    data = request.get_json()
    if validate_questions(data):
        return validate_questions(data)

    current_user = get_jwt_identity()
    if not data or not data["title"] or not data["body"] or not data["user_id"] or not data["meetup_id"]:
            return jsonify({'message': 'All fields are required!'}), 400
    
    questions_data = Question(
        data['title'],
        data['body'],
        data['user_id'],
        data['meetup_id']
    	)

    if questions_data.ask_question():
        return jsonify({'message': 'Question created!'}), 201
    return jsonify({'message': 'Question with the title \'{}\' already exists'.format(data['title'])}), 409
    

@v2_questions.route('', methods=['GET'])
def view_all_question():
	pass

@v2_questions.route('', methods=['GET'])
def fetch_specific_question():
	pass

@v2_questions.route('', methods=['DELETE'])
def delete_question():
	pass