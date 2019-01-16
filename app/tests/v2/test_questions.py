import unittest
import json

from app.tests.v1.base import TestSetup

class TestQuestion(TestSetup):

    def test_asked_question(self):
        """ Test ask a question """
        res = self.client.post(
            '/api/v1/questions',
            data=json.dumps(self.question_2),
            content_type='application/json')
        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Question created successfully", msg["Message"])