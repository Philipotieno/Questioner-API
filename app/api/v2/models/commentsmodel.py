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
        query = "SELECT body from comments WHERE body=%s;"
        cur.execute(query, (body,))
        the_comment = cur.fetchone()
        if the_comment:
            return True

    def post_comment(self):
        if self.check_if_comment_exists(self.body):
            return False
        query = "INSERT INTO questions (body, user_id, question_id, created_on) values (%s, %s, %s, %s) \
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