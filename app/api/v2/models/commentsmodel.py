import os
import datetime
from app.api.v2.models.db import Database

now = datetime.datetime.now()
db = Database()
cur = db.cur

class Comment():

    """ Implements questions class"""

    def __init__ (self,body, user_id, question_id):
        self.body = body
        self.user_id = user_id
        self.question_id = question_id
        self.created_on = now

    def check_if_comment_exists(self, body):
        '''Method to check for existing comments'''
        query = "SELECT body from comments WHERE body=%s;"
        cur.execute(query, (body,))
        the_comment = cur.fetchone()
        if the_comment:
            return True

    def post_comment(self):
        '''Method to post for comments'''
        if self.check_if_comment_exists(self.body):
            return False
        query = "INSERT INTO comments (body, user_id, question_id, created_on) values (%s, %s, %s, %s) \
        RETURNING body, user_id, question_id, created_on;"
        cur.execute(
            query,
            (self.body,
             self.user_id,
             self.question_id,
             self.created_on))
        comment = cur.fetchone()
        db.conn.commit()
        return comment

    def get_all_comments():
        '''Method to fetch all comments'''
        query = "SELECT * from comments;"
        cur.execute(query)
        comments = cur.fetchall()
        return comments