import unittest
import json

from app.tests.v1.base import TestSetup

class TestUser(TestSetup):

    def test_register_new_user(self):
        """ Test new user register """

        # register a user
        res = self.client.post(
            '/v1/register/',
            data=json.dumps(self.user_2),
            content_type='application/json')

        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('User Registered successfully!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')


if __name__ == '__main__':
    unittest.main()