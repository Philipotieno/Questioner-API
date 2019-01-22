import psycopg2
from flask import Blueprint, jsonify, request
import datetime

from app.api.v2.models.meetupsmodel import Meetup
from app.api.v2.models.usersmodels import User


from app.api.v2.views.validator import validate_meetup
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.api.v2.models.db import Database

v2_meetups = Blueprint('v2_meetups', __name__)


@v2_meetups.route('<user_id>', methods=['POST'])
@jwt_required
def create_meetup(user_id):
    user = User.get_user_by_id(user_id)
    current_user = get_jwt_identity()

    if current_user == 'wiseadmin':
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
    return jsonify({'message': 'You are not allowed to make changes'}), 409


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