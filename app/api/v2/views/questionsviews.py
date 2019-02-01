import os
import psycopg2
from flask import Blueprint, jsonify, request
import json

from app.api.v2.models.questionsmodel import Question, Voters
from app.api.v2.models.meetupsmodel import Meetup
from app.api.v2.models.usersmodels import User
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.api.v2.models.db import Database

v2_questions = Blueprint('v2_uestions', __name__)

db = Database()
cur = db.cur

@v2_questions.route('<int:meetup_id>', methods=['POST'])
@jwt_required
def create_question(meetup_id):
    """ Creates a question """
    meetup = Meetup.get_meetup_by_id(meetup_id)

    username = get_jwt_identity()
    user = User.get_user_by_name(username)

    if not meetup:
        return jsonify({'message': 'Meetup does not exist!'}), 404
    
    data = request.get_json()

    if not data or not data["title"] or not data["body"]:
            return jsonify({'message': 'All fields are required!'}), 400
    
    questions_data = Question(
        data['title'],
        data['body'],
        user['user_id'],
        meetup['meetup_id']
        )
    new_qns = questions_data.ask_question()
    if new_qns:
        return jsonify({'status':201, 'message': 'Question created!', 'data':new_qns}), 201
    return jsonify({'message': 'Question with the title \'{}\' already exists'.format(data['title'])}), 409

@v2_questions.route('', methods=['GET'])
def view_all_question():
    """View all questions"""
    asked = Question.get_all_questions()
    if asked:
        return jsonify({'Questions': asked}), 200
    return jsonify({'message': 'No questions available!'})

@v2_questions.route('<question_id>', methods=['GET'])
def fetch_specific_question(question_id):
    """Fetch specific question"""
    question = Question.get_specific_question(question_id)
    if question:
        return jsonify({'Meetup': question}), 200
    return jsonify({'message': 'Question not found!'}), 404

@v2_questions.route('<int:question_id>/upvote', methods=['PATCH'])
@jwt_required
def upvote_question(question_id):
    """Upvote a question"""
    data = request.get_json()
    question = Question.get_specific_question(question_id)
    if not question:
        return jsonify({"status":404, 'message': 'question does not exist!'}), 404

    username = get_jwt_identity()
    user = User.get_user_by_name(username)

    if not data or not data["vote"]:
        return jsonify({'message': 'All fields are required!'}), 400


    if data['vote'].lower() != "upvote":
        return jsonify({'error' : 'Response must upvote', "status":400}), 400

    query = "SELECT user_id, question_id FROM votes;"
    cur.execute(query)
    votes = cur.fetchall()
    for votes in votes:
        if votes['user_id'] == user['user_id'] and votes['question_id'] == question['question_id']:
            return jsonify({'message': 'User has already voted'}), 409

    votes_data = Voters(
        user['user_id'],
        question['question_id'],
        data['vote']
        )

    new_vote = votes_data.add_vote()

    result = Question.upvote_question(question["question_id"])
    return jsonify({"status":400, 'message': 'Question upvoted succesfully!', "data": result, "new_vote": new_vote}), 400


@v2_questions.route('<int:question_id>/downvote', methods=['PATCH'])
@jwt_required
def downvote_question(question_id):
    """Downvote a question"""
    question = Question.get_specific_question(question_id)
    if not question:
        return jsonify({"status":404, 'message': 'question does not exist!'}), 404

    result = Question.downvote_question(question["question_id"])
    return jsonify({"status":400, 'message': 'Question upvoted succesfully!', "data": result}), 400