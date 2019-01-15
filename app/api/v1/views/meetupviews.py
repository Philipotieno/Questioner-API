import re
from flask import request, jsonify, Blueprint
from app.api.v1.models.meetupsmodel import Meetup
from datetime import datetime

v1_meetups = Blueprint('meetups', __name__)

meetups = Meetup() #meetup class instance

@v1_meetups.route('', methods=['POST'])
def create_meetup():
    data = request.get_json()
    topic = data['topic']
    location = data['location']
    tags = data['tags']
    happeningOn = data['happeningOn']

    data_format = re.compile(r"(^[A-Za-z\s]+$)")

    if not re.match(data_format, topic) or not re.match(data_format, location) or not re.match(data_format, tags):
        return jsonify({'message' : 'topic/locaion/tag should contain letters only'}), 400

    if not topic or not location or not tags or not happeningOn:
        return jsonify({'message': 'Please input all required fields!'}), 400

    if len(topic) < 4 or len(location) < 4 or len(tags) < 4:
        return jsonify({"message" : "length of topic, location and tag should not be less than 4"}), 400

    if happeningOn:
        try:
            datetime.strptime(happeningOn, '%d-%m-%Y')
        except ValueError as e:
            return jsonify({'message' : str(e)})

    return jsonify({'Message' : 'Meetup created successfully'}), 201

@v1_meetups.route('/upcoming', methods=['GET'])
def get_meetups():
    all_meetups = meetups.get_all_meetups()
    if not all_meetups:
        return jsonify({'message' : 'No meetups', "status": 200}), 200


    meetups.create_meetup(
        topic=topic,
        location=location,
        tags=tags,
        happeningOn=happeningOn
        )

    return jsonify({"meetups" : all_meetups, "status": 200}), 200

@v1_meetups.route('<meetup_id>', methods=['GET'])
def get_specific_meetup(meetup_id):
    a_meetup = meetups.get_specific_meetup(meetup_id)
    if not a_meetup:
        return jsonify({'message' : 'meetup does not exist', "status" : 404}), 404

    return jsonify({"meetups" : a_meetup, "status" : 200}), 200

@v1_meetups.route('<meetup_id>/rsvp', methods=['POST'])
def rsvp_meetup(meetup_id):
    data = request.get_json()

    all_meetup = meetups.get_all_meetups()
    if not all_meetup:
        return jsonify({'message' : 'meetup does not exist', "status" : 404}), 404
    
    new_status = data['attending']
    if not new_status:
        return jsonify({'message': 'Please input all required fields!'}), 400
    if (new_status != "maybe" and new_status != "yes" and new_status != "no"):
        return jsonify({'error' : 'response must be yes no or maybe', "status":400}), 400
    meetups.response(meetup_id, new_status)

    return jsonify({'message' : 'your response has been recorded'}), 200