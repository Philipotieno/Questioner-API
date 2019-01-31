from flask import Blueprint, jsonify, request
import datetime

from app.api.v2.models.meetupsmodel import Meetup
from app.api.v2.models.usersmodels import User


from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.api.v2.models.db import Database

v2_meetups = Blueprint('v2_meetups', __name__)


@v2_meetups.route('', methods=['POST'])
@jwt_required
def create_meetup():
    current_user = get_jwt_identity()
    if current_user == 'wiseadmin':
        data = request.get_json()

        if not data or not data["topic"] or not data["location"] or not data["happening_on"] or not data["tags"]:
            return jsonify({'message': 'All fields are required!'}), 400

        meetup_details = Meetup(
            data['topic'],
            data['location'],
            data['tags'],
            data['happening_on']
            )
        new_meetup =meetup_details.create_meetup()
        if new_meetup:
            return jsonify({'status': 201,'message': 'Meetup created!', "Meetup":new_meetup}), 201
        return jsonify({'status': 409,'message': 'Topic {} already exists choose another topic'.format(data['topic'])}), 409
    return jsonify({'status': 409,'message': 'You are not allowed to make changes'}), 409

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


@v2_meetups.route('<meetup_id>', methods=['DELETE'])
def remove_meetup(meetup_id):
    """delete one meetup"""
    meetup = Meetup.get_meetup_by_id(meetup_id)
    if not meetup:
        return (jsonify({'status': 404, 'message': "Meetup does not exist"}), 404)

    Meetup.delete_meetup(meetup_id)

    return (jsonify({"status": 200, "message": "meetup removed" }), 200)
