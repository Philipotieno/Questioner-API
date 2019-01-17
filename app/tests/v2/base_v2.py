import unittest
import json

from app import create_app

from app.api.v2.models.usersmodels import User
from app.api.v2.models.meetupsmodel import Meetup
from app.api.v2.models.questionsmodel import Question

from app.api.v2.models.db import Database

db = Database()
cur = db.cur

class TestSetup(unittest.TestCase):
    """Base test class for all test classes"""

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.user_1 = {
            "firstname" : "testfirstname",
            "lastname" : "testlastname",
            "username" : "testuser",
            "email" : "email@gmail.com",
            "phone_number" : "0703473377",
            "password" : "password"
        }

        self.user_2 = {
            "firstname" : "testuser",
            "lastname" : "lastname",
            "username" : "testuserame",
            "email" : "emailwe3@gmail.com",
            "phone_number" : "070347446",
            "password" : "password"
        }

        self.add_meetup = {
            "topic" : "pytest",
            "location" : "kisumu",
            "tags" : "test tags",
            "happeningOn" : "1-1-2019",
        }

      

        self.meetup_1 = {
            "topic" : "testtopic",
            "location" : "testlocation",
            "tags" : "tagfour tagfive",
            "happeningOn" : "11-12-2019"
        }

        self.meetup_2 = {
            "topic" : "testtopics",
            "location" : "testlocations",
            "tags" : "tagtwo tagone",
            "happeningOn" : "11-12-2019"
        }
        
        self.meetup_3 = {
            "topic" : "tes",
            "location" : "testlocations",
            "tags" : "tagtwo tagone",
            "happeningOn" : "11-12-2019"
        }


        self.question_1 = {
            "user" : 1,
            "meetup" : 2,
            "title" : "testtitle",
            "body" : "this is a test body"
        }

        self.question_2 = {
            "user" : 2,
            "meetup" : 4,
            "title" : "testtitle_3",
            "body" : "this is a test body_3"
        }

    def tearDown(self):
        user = "DELETE FROM users WHERE username='testuser';"
        meetup = "DELETE FROM meetups WHERE topic='test_topic';"
        queries = [user, meetup]
        for query in queries:
            cur.execute(query)
            db.conn.commit()