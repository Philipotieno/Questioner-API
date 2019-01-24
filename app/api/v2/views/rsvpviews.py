from flask import Blueprint, jsonify, request

from app.api.v2.models.rsvpmodel import Rsvp
from app.api.v2.models.meetupsmodel import Meetup
from app.api.v2.models.model import Meetup
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
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Body should contain data in json format!'}), 401

        if not data or not data["user_id"] or not data["meetup_id"] or not data["response"]:
            return jsonify({'message': 'User_id, meetup_id or response cannot be empty!'}), 400

        r = data['response']
        if (r != "maybe" and r != "yes" and r != "no"):
            return jsonify({'error' : 'response must be yes no or maybe', "status":400}), 400


        query = "SELECT user_id, meetup_id FROM rsvps;"
        cur.execute(query)
        ids = cur.fetchall()
        for ids in ids:
            if ids['user_id'] == data['user_id'] and ids['meetup_id'] == data['meetup_id']:
                return jsonify({'message': 'user already responded to that meetup'}), 409

        rsvp_details = Rsvp(
            data['user_id'],
            data['meetup_id'],
            data['response'],
        )

        new_rsvp = rsvp_details.post_rsvp()
        return jsonify({'message': 'Rsvp posted successfully!', "data" : new_rsvp}), 201

    except Exception as e:
        return jsonify({'message': 'All fields are required'}), 400