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
        query = "INSERT INTO meetups (topic, location, tags, happening_on, created_on) values (%s, %s, %s, %s, %s);"
        cur.execute(
            query,
            (self.topic,
             self.location,
             self.tags,
             self.happening_on,
             self.created_on))
        db.conn.commit()
        return True

    staticmethod
    def get_all_meetups():
        '''Method to fetch all meetups'''
        query = "SELECT * from meetups;"
        cur.execute(query)
        meetups = cur.fetchall()
        return meetups

    @staticmethod
    def get_specific_meetup(self, meetup_id):
        """ Fetch a specific meet using meetup_id"""
        pass
