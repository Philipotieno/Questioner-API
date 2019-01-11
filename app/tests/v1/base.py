import unittest
import json

from app import create_app

from app.api.v1.models.usersmodels import User
from app.api.v1.models.meetupsmodel import Meetup

user = User()
meetup = Meetup()

class TestSetup(unittest.TestCase):
    """Base test class for all test classes"""

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.user_1 = {
            "firstname" : "tfirstname",
            "lastname" : "lastname",
            "username" : "testuser",
            "email" : "email@gmail.com",
            "phone" : "07034744",
            "password" : "password"
        }

        """not registered"""
        self.user_2 = {
            "firstname" : "testuser",
            "lastname" : "lastname",
            "username" : "testuserame",
            "email" : "emailwe3@gmail.com",
            "phone" : "07034744",
            "password" : "password"
        }

        self.add_meetup = {
            "topic" : "pytest",
            "location" : "kisumu",
            "tags" : "test tag",
            "happeningOn" : "1/1/2019",
        }

        self.register = self.client.post(
        	'/api/v1/users/register',
            data=json.dumps(self.user_1),
            content_type='application/json')

        self.login = self.client.post(
            '/api/v1/users/login',
            data=json.dumps(self.user_1),
            content_type='application/json')
        # self.data = json.loads(self.login.data.decode("UTF-8"))


        self.meetup_1 = {
            "topic" : "testtopic",
            "location" : "testlocation",
            "tags" : "tagfour, tagfive",
            "happeningOn" : "11/12/2019"
        }

        self.meetup_2 = {
            "topic" : "testtopics",
            "location" : "testlocations",
            "tags" : "tagtwo, tagone",
            "happeningOn" : "11/12/2019"
        }

        self.create_meetup = self.client.post(
            '/v1/meetups',
            data=json.dumps(self.meetup_1),
            content_type='application/json')

    def tearDown(self):
        self.users = user.users
        self.users.clear()