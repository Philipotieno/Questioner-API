import unittest
import json

from flask_jwt_extended import (create_access_token)
from app.tests.v2.base_v2 import TestSetup

class TestQuestion(TestSetup):

    def test_asked_question(self):
        """ Test post a question without authentication"""
        token = create_access_token(identity="username")

        res = self.client.post(
            '/api/v2/questions/1',
            data=json.dumps(self.question_1),
            content_type='application/json')
        self.assertEqual(res.status_code, 401)
        msg = json.loads(res.data.decode("UTF-8"))
        print(msg)
        self.assertIn('Missing Authorization Header', msg['msg'])
        self.assertTrue(res.content_type == 'application/json')