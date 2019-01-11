import unittest
import json

from app.tests.v1.base import TestSetup

class TestMeetup(TestSetup):

    def test_created_meetup(self):
        """ Test new meetup can be created """

        # place an order
        res = self.client.post(
            '/api/v1/meetups',
            data=json.dumps(self.meetup_2),
            content_type='application/json')
        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Meetup created successfully", msg["Message"])