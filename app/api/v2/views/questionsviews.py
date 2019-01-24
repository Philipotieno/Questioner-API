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

    # current_user = get_jwt_identity()
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
    asked = Question.get_all_questions()
    if asked:
        return jsonify({'Questions': asked}), 200
    return jsonify({'message': 'No questions available!'})

@v2_questions.route('<question_id>', methods=['GET'])
def fetch_specific_question(question_id):
    question = Question.get_specific_question(question_id)
    if question:
        return jsonify({'Meetup': question}), 200
    return jsonify({'message': 'Question not found!'}), 404

@v2_questions.route('<question_id>/upvote', methods=['PATCH'])
def upvote_question(question_id):
    question = Question.get_specific_question(question_id)
    if not question:
        return jsonify({"status":404, 'message': 'question does not exist!'}), 404

    result = Question.upvote_question(question["question_id"])
    return jsonify({"status":404, 'message': 'Question upvoted succesfully!', "data": result}), 400


@v2_questions.route('<question_id>/downvote', methods=['PATCH'])
def downvote_question(question_id):
    question = Question.get_specific_question(question_id)
    if not question:
        return jsonify({"status":404, 'message': 'question does not exist!'}), 404

    result = Question.downvote_question(question["question_id"])
    return jsonify({"status":400, 'message': 'Question upvoted succesfully!', "data": result}), 400