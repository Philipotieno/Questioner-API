import psycopg2
from flask import Blueprint, jsonify, request
import datetime

from app.api.v2.models.meetupsmodel import Meetup

from app.api.v2.models.db import Database

v2_meetups = Blueprint('v2_meetups', __name__)


@v2_meetups.route('', methods=['POST'])
def create_meetup():
    data = request.get_json()

    meetup_details = Meetup(
        data['topic'],
        data['location'],
        data['tags'],
        data['happening_on']
    )
    if meetup_details.create_meetup():
    	return jsonify({'message': 'Meetup created!'}), 201
    return jsonify({'message': 'Topic {} already exists choose another topic'.format(data['topic'])}), 409

@v2_meetups.route('/upcoming', methods=['GET'])
def get_meetups():
    pass

@v2_meetups.route('<meetup_id>', methods=['GET'])
def get_specific_meetup(meetup_id):
    pass