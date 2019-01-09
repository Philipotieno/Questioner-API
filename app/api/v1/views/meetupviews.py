from flask import request, jsonify, Blueprint
from app.api.v1.models.meetupsmodel import Meetup


v1_meetups = Blueprint('meetups', __name__)

meetups = Meetup()

@v1_meetups.route('', methods=['POST'])
def create_meetup():
	data = request.get_json()
	topic = data['topic']
	location = data['location']
	tags = data['tags']

	# if not title or not content:
	# 	return jsonify({'message': 'Please input all required fields!'}), 400
	return jsonify({'Message' : 'You have succesfully posted your question'}), 201