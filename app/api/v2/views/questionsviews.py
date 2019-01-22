import os
import psycopg2
from flask import Blueprint, jsonify, request
import json

from app.api.v2.models.questionsmodel import Question
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.api.v2.models.db import Database

v2_questions = Blueprint('v2_uestions', __name__)

db = Database()
cur = db.cur

@v2_questions.route('', methods=['POST'])
@jwt_required
def create_question(current_user):
    data = request.get_json()
    title= data['title']
    body= data['body']
 
    query = "SELECT meetup_id from meetups;"
    cur.execute(query)
    meetups = cur.fetchall()
    questions_data = Question(
    	current_user["id"],
    	meetup_id["id"],
    	title,
    	body
    	)
    for m in meetups:
    	for topic in data['topic'].keys():
    		if meetups['topic'] == topic:
    			questions_data.ask_question()
    			return jsonify({'message': 'Question successfully posted!'}), 201
    		return jsonify({'message': '{} not available!'.format(meetups)}), 404

@v2_questions.route('', methods=['GET'])
def view_all_question():
	pass

@v2_questions.route('', methods=['GET'])
def fetch_specific_question():
	pass

@v2_questions.route('', methods=['DELETE'])
def delete_question():
	pass