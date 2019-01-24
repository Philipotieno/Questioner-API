from app.api.v2.models.db import Database

db = Database()
cur = db.cur

class Rsvp():

    """ Implements questions class"""

    def __init__ (self,user_id, meetup_id, response):
        self.user_id = user_id
        self.meetup_id = meetup_id
        self.response = response 

    def check_if_rsvp_exists(self, user_id, meetup_id):
        '''Method to check for existing comments'''
        query = "SELECT * FROM rsvps WHERE user_id = '{}' AND meetup_id = '{}'\
        ".format(user_id, meetup_id)
        cur.execute(query)
        the_rsvp = cur.fetchone()
        if the_rsvp:
            return True

    def post_rsvp(self):
        '''Method to post for comments'''
        if self.check_if_rsvp_exists(self.user_id, self.meetup_id):
            return False
        query = "INSERT INTO rsvps (user_id, meetup_id, response) values (%s, %s, %s) \
        RETURNING rsvp_id user_id, meetup_id, response;"
        cur.execute(
            query,
            (self.user_id,
             self.meetup_id,
             self.response))
        rsvp = cur.fetchone()
        db.conn.commit()
        return rsvp