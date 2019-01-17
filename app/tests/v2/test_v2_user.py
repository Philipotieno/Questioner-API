import unittest
import json

from app.tests.v2.base_v2 import TestSetup

class TestUser(TestSetup):

    def test_register_new_user(self):
        """ Test new user register """

        # register a user
        res = self.client.post(
            '/api/v2/auth/register',
            data=json.dumps(self.user_1),
            content_type='application/json')

        self.assertEqual(res.status_code, 201)
        # msg = json.loads(res.data.decode("UTF-8"))
        # self.assertIn('User Registered successfully!', msg['message'])
        # self.assertTrue(res.content_type == 'application/json')


    def test_registered_user_login(self):
        self.client.post(
            '/api/v2/auth/register',
            data=json.dumps(self.user_1),
            content_type='application/json')

        res = self.client.post(
            '/api/v2/auth/login',
            data=json.dumps(self.user_1),
            content_type='application/json')
        msg = json.loads(res.data.decode('UTF-8'))
        self.assertIn('You are now logged in', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
