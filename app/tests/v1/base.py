import unittest
import json

from app import create_app

from app.api.v1.models.usersmodels import User

user = User()

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

        self.register = self.client.post(
        	'/v1/register/',
            data=json.dumps(self.user_1),
            content_type='application/json')


    def tearDown(self):
        self.users = user.users
        self.users.clear()