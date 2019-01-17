import os
import psycopg2
from app.api.v2.models.db import Database

db = Database()
cur = db.conn.cursor()

class Question(object):

    """ Implements questions class"""

    def __init__(self):
    	pass

    @staticmethod
    def ask_question(self, createdon, user, meetup, title, body):
    	pass

    @staticmethod
    def get_all_questions(self):
    	'''Method to fetch all questions'''
    	pass

    @staticmethod
    def get_specific_question(self, question_id):
    	""" Fetch a specific question using given id"""
    	pass