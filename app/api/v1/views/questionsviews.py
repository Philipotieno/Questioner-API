from flask import request, jsonify, Blueprint
from app.api.v1.models.questionsmodel import Question
import datetime

now = datetime.datetime.now()
v1_questions = Blueprint('questions', __name__)

questions_inst = Question() #question class instance

@v1_questions.route('', methods=['POST'])
def create_question():
	data = request.get_json()
	user = data["user"]
	meetup = data['meetup']
	title = data['title']
	body = data['body']

	questions_inst.ask_question(
			user=user,
			meetup=meetup,
			title=title,
			body=body,
			createdon=now
		)

	if not user or not meetup or not title or not body:
		return jsonify({'message': 'Please input all required fields!', "status":400}), 400
		
	return jsonify({'Message' : 'Question created successfully', 'Question' : questions_inst.questions, "status":201}), 201

