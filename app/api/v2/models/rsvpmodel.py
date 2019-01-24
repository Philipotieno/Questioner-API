from app.api.v2.models.db import Database
import datetime

now = datetime.datetime.now()
db = Database()
cur = db.cur

class Rsvp():

    """ Implements questions class"""

    def __init__ (self,user_id, meetup_id, response):
        self.user_id = user_id
        self.meetup_id = meetup_id
        self.response = response
        self.created_on = now


    def post_rsvp(self):
        query = "INSERT INTO rsvps (user_id, meetup_id, response, created_on) values (%s, %s, %s, %s) \
        RETURNING rsvp_id, user_id, meetup_id, response;"
        cur.execute(
            query,
            (self.user_id,
             self.meetup_id,
             self.response,
             self.created_on))
        rsvp = cur.fetchone()
        db.conn.commit()
        return rsvp