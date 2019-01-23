import os
import datetime
from app.api.v2.models.db import Database
from app.api.v2.models.meetupsmodel import Meetup

now = datetime.datetime.now()
db = Database()
cur = db.cur

class Question():

    """ Implements questions class"""

    def __init__ (self,title, body, user_id, meetup_id):
        self.title = title
        self.body = body
        self.user_id = user_id
        self.meetup_id = meetup_id
        self.created_on = now

    def check_if_question_exists(self, title):
        query = "SELECT title from questions WHERE title=%s;"
        cur.execute(query, (title,))
        question = cur.fetchone()
        if question:
            return True

    def ask_question(self):
        if self.check_if_question_exists(self.title):
            return False
        query = "INSERT INTO questions (title, body, user_id, meetup_id, created_on) values (%s, %s, %s, %s, %s);"
        cur.execute(
            query,
            (self.title,
             self.body,
             self.user_id,
             self.meetup_id,
             self.created_on))
        db.conn.commit()
        return True

    def get_all_questions():
        '''Method to fetch all questions'''
        query = "SELECT * from questions;"
        cur.execute(query)
        questions = cur.fetchall()
        return questions

    @staticmethod
    def get_specific_question(self, question_id):
        """ Fetch a specific question using given id"""
        pass