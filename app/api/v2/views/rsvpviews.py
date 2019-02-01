from flask import Blueprint, jsonify, request

from app.api.v2.models.rsvpmodel import Rsvp
from app.api.v2.models.meetupsmodel import Meetup
from app.api.v2.models.usersmodels import User

from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.api.v2.models.db import Database

v2_rsvps = Blueprint('v2_rsvps', __name__)

db = Database()
cur = db.cur

@v2_rsvps.route('', methods=['POST'])
@jwt_required
def post_rsvp(meetup_id):
    """Function to view rsvp """
    meetup = Meetup.get_meetup_by_id(meetup_id)
    if not meetup:
        return jsonify({'message': 'Meetup not found!'}), 404

    username = get_jwt_identity()
    user = User.get_user_by_name(username)

    data = request.get_json()
    if not data:
        return jsonify({'message': 'Body should contain data in json format!'}), 401

    if not data or not data["response"]:
        return jsonify({'message': 'Response cannot be empty!'}), 400

    r = data['response']
    if (r != "maybe" and r != "yes" and r != "no"):
        return jsonify({'error' : 'Response must be yes no or maybe', "status":400}), 400


    query = "SELECT user_id, meetup_id FROM rsvps;"
    cur.execute(query)
    ids = cur.fetchall()
    for ids in ids:
        if ids['user_id'] == user['user_id'] and ids['meetup_id'] == meetup['meetup_id']:
            return jsonify({'message': 'You have already responded to this meetup'}), 409

    rsvp_details = Rsvp(
        user['user_id'],
        meetup['meetup_id'],
        data['response']
    )

    new_rsvp = rsvp_details.post_rsvp()
    return jsonify({'status':200, 'message': 'Rsvp posted successfully!', "data" : new_rsvp}), 201