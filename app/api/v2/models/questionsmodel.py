import os
import datetime
from app.api.v2.models.db import Database
from app.api.v2.models.meetupsmodel import Meetup

db = Database()
cur = db.conn.cursor()

class Question():

    """ Implements questions class"""

    def __init__ (self, user_id, meetup_id, title, body):
        self.user_id = user_id
        self.meetup_id = meetup_id
        self.title = title
        self.body = body

    @staticmethod
    def ask_question(self):
        query = "INSERT INTO questions (user_id, meetup_id, title, body) values (%s, %s, %s, %s);"
        cur.execute(
            query,
            (self.user_id,
             self.meetup_id,
             self.title,
             self.body,))
        db.conn.commit()
        return True

    @staticmethod
    def get_all_questions(self):
        '''Method to fetch all questions'''
        pass

    @staticmethod
    def get_specific_question(self, question_id):
        """ Fetch a specific question using given id"""
        pass