import psycopg2
from flask import Blueprint, jsonify, request
import datetime

from app.api.v2.models.meetupsmodel import Meetup
from app.api.v2.views.validator import validate_meetup

from app.api.v2.models.db import Database

v2_meetups = Blueprint('v2_meetups', __name__)


@v2_meetups.route('', methods=['POST'])
def create_meetup():
    data = request.get_json()
    if validate_meetup(data):
        return validate_meetup(data)

    if not data or not data["topic"] or not data["location"] or not data["happening_on"] or not data["tags"]:
        return jsonify({'message': 'All fields are required!'}), 400
    
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
    upcoming = Meetup.get_all_meetups()
    if upcoming:
        return jsonify({'Meetups': upcoming}), 200
    return jsonify({'message': 'No meetups available!'})

@v2_meetups.route('<meetup_id>', methods=['GET'])
def get_specific_meetup(meetup_id):
    meetup = Meetup.get_meetup_by_id(meetup_id)
    if meetup:
        return jsonify({'Meetup': meetup}), 200
    return jsonify({'message': 'Meetup not found!'}), 404