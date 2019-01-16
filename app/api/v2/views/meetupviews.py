import os
import psycopg2
from flask import Blueprint, jsonify, request

from app.api.v2.models.meetupsmodel import Meetup

from app.api.v2.models.db import Database

v2_meetups = Blueprint('meetups', __name__)

db = Database()
cur = db.conn.cursor()

@v2_meetups.route('', methods=['POST'])
def create_meetup():
    pass

@v2_meetups.route('/upcoming', methods=['GET'])
def get_meetups():
    pass

@v2_meetups.route('<meetup_id>', methods=['GET'])
def get_specific_meetup(meetup_id):
    pass