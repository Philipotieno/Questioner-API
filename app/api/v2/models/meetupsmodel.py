import datetime
from app.api.v2.models.db import Database

now = datetime.datetime.now()
db = Database()
cur = db.cur

class Meetup():

    #meetup constructor
    def __init__(self, topic, location, tags, happening_on):
        self.topic = topic
        self.location = location
        self.tags = tags
        self.happening_on = happening_on
        self.created_on = now

    def check_if_meetup_exists(self, topic):
        query = "SELECT topic from meetups WHERE topic=%s;"
        cur.execute(query, (topic,))
        meetup = cur.fetchone()
        if meetup:
            return True

    def create_meetup(self):
        if self.check_if_meetup_exists(self.topic):
            return False
        query = "INSERT INTO meetups (topic, location, tags, happening_on, created_on) values (%s, %s, %s, %s, %s) \
        RETURNING meetup_id, topic, location, tags, happening_on, created_on;"
        cur.execute(
            query,
            (self.topic,
             self.location,
             self.tags,
             self.happening_on,
             self.created_on))
        meetup = cur.fetchone()
        db.conn.commit()
        return meetup

    def delete_meetup(meetup_id):
        """Delete a single Meetup"""
        query = "DELETE FROM meetups WHERE meetup_id= '{}';".format(meetup_id)
        cur.execute(query)
        db.conn.commit()

    @staticmethod
    def get_all_meetups():
        '''Method to fetch all meetups'''
        query = "SELECT * from meetups;"
        cur.execute(query)
        meetups = cur.fetchall()
        return meetups

    @staticmethod
    def get_meetup_by_id(meetup_id):
        """ Fetch a specific meetup using meetup_id"""
        query = "SELECT * from meetups where meetup_id=%s;"
        cur.execute(query, (meetup_id,))
        meetup = cur.fetchone()
        return meetup

