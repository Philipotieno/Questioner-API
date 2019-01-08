import unittest
import json

from app.tests.v1.base import TestSetup
from app.api.v1.models.usersmodels import User

user = User()

class TestUser(TestSetup):

    def test_register_new_user(self):
        """ Test new user register """

        # register a user
        res = self.client.post(
            '/auth/register',
            data=json.dumps(self.user_1),
            content_type='application/json')

        self.assertEqual(res.status_code, 401)
        # msg = json.loads(res.data.decode("UTF-8"))
        # self.assertIn('User succesfully created!', msg['message'])
        # self.assertTrue(res.content_type == 'application/json')
