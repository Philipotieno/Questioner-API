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
            "firstname" : "fname",
            "lastname" : "lname",
            "username" : "username",
            "email" : "email",
            "phone" : "phone",
            "password" : "password",
            "registered" : "registered"
        }

        self.register = self.client.post(
        	'/auth/register',
            data=json.dumps(self.user_1),
            content_type='application/json')


    def tearDown(self):
        self.users = user.users
        self.users.clear()