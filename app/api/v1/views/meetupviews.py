from flask import request, jsonify, Blueprint
from app.api.v1.models.meetupsmodel import Meetup


v1_meetups = Blueprint('meetups', __name__)

meetup_inst = Meetup() #meetup class instance

@v1_meetups.route('', methods=['POST'])
def create_meetup():
	data = request.get_json()
	topic = data['topic']
	location = data['location']
	tags = data['tags']
	happeningOn = data['happeningOn']

	if not topic or not location or not tags or not happeningOn:
		return jsonify({'message': 'Please input all required fields!'}), 400
		
	return jsonify({'Message' : 'Meetup created successfully'}), 201