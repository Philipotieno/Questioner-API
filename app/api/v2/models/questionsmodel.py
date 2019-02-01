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
        self.votes = 0
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


        query = "INSERT INTO questions (title, body, user_id, meetup_id, created_on) values (%s, %s, %s, %s, %s) \
        RETURNING user_id, meetup_id, question_id, title, body, created_on;"
        cur.execute(
            query,
            (self.title,
             self.body,
             self.user_id,
             self.meetup_id,
             self.created_on))
        qns = cur.fetchone()
        db.conn.commit()
        return qns

    @staticmethod
    def get_all_questions():
        '''Method to fetch all questions'''
        query = "SELECT * from questions;"
        cur.execute(query)
        questions = cur.fetchall()
        return questions

    @staticmethod
    def get_specific_question(question_id):
        """ Fetch a specific question using given id"""
        query = "SELECT * from questions where question_id=%s;"
        cur.execute(query, (question_id,))
        question = cur.fetchone()
        return question

    @staticmethod
    def upvote_question(question_id):
        ''''Method to upvote a question'''
        query = "SELECT * FROM questions WHERE question_id= '{}';".format(question_id)
        cur.execute(query)
        qns = cur.fetchone()

        if qns:
            question = qns
        else:
            return None

        current_vote = int(question['votes']) + 1
        query = "UPDATE questions SET votes= '{}' WHERE question_id = '{}';".format(current_vote, question_id)
        cur.execute(query)
        db.conn.commit()

        cur.execute("SELECT * FROM questions WHERE question_id= '{}';".format(question_id))
        new_data = cur.fetchone()

        result = {
            "question_id" : new_data['question_id'],
            "votes": new_data['votes']
        }

        return result
    @staticmethod
    def downvote_question(question_id):
        ''''Method to dowpvote a question'''
        query = "SELECT * FROM questions WHERE question_id= '{}';".format(question_id)
        cur.execute(query)
        question = cur.fetchone()

        current_vote = int(question['votes']) - 1
        query = "UPDATE questions SET votes= '{}' WHERE question_id = '{}';".format(current_vote, question_id)
        cur.execute(query)
        db.conn.commit()

        cur.execute("SELECT * FROM questions WHERE question_id= '{}';".format(question_id))
        new_data = cur.fetchone()

        result = {
            "question_id" : new_data['question_id'],
            "votes": new_data['votes']
        }

        return result

class Voters():
    """ Implements voters class"""
    def __init__ (self, user_id, question_id, vote):
        self.user_id = user_id
        self.question_id = question_id
        self.vote = vote

    def add_vote(self):
        query = "INSERT INTO votes (user_id, question_id, vote) values (%s, %s, %s) \
        RETURNING user_id, question_id, vote;"
        cur.execute(
            query,
            (self.user_id,
            self.question_id,
            self.vote))
        vot = cur.fetchone()
        db.conn.commit()
        return vot