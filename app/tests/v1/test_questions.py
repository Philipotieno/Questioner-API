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

    def test_upvote_a_question(self):
        """ Test upvote a question """
        self.client.post(
            '/api/v1/questions',
            data=json.dumps(self.question_2),
            content_type='application/json')

        res = self.client.put(
            '/api/v1/questions/1/upvote',
            data=json.dumps(self.upvote),
            content_type='application/json')
        self.assertEqual(res.status_code, 200)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("you have upvoted a question", msg["message"])

    def test_downvote_a_question(self):
        """ Test upvote a question """
        self.client.post(
            '/api/v1/questions',
            data=json.dumps(self.question_2),
            content_type='application/json')

        res = self.client.put(
            '/api/v1/questions/1/downvote',
            data=json.dumps(self.downvote),
            content_type='application/json')
        self.assertEqual(res.status_code, 200)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("you have downvoted a question", msg["message"])


if __name__ == '__main__':
    unittest.main()
