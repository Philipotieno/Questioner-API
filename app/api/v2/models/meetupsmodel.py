import os
import psycopg2
from app.api.v2.models.db import Database

db = Database()
cur = db.conn.cursor()

class Meetup():
	def __init__(self):
		pass

	def create_meetup(self, topic, location, happeningOn, tags):
		pass

	staticmethod
	def get_all_meetups(self):
		'''Method to fetch all meetups'''
		pass

	@staticmethod
	def get_specific_meetup(self, meetup_id):
		""" Fetch a specific meet using meetup_id"""
		pass
