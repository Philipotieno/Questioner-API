import unittest
import json
from flask_jwt_extended import (create_access_token)

from app.tests.v2.base_v2 import TestSetup

class TestMeetup(TestSetup):

    def test_created_meetup(self):
        """ Test new meetup can be created """
        token = create_access_token(identity="wiseadmin")

        res = self.client.post(
            '/api/v2/meetups',
            data=json.dumps(self.meetup_3),
            content_type='application/json',
            headers={'Authorization': 'Bearer {}'.format(token)})
        self.assertEqual(res.status_code, 201)

    def test_meetup_with_no_auth(self):
        """ Test new meetup with no authorisation"""
        
        res = self.client.post(
            '/api/v2/meetups',
            data=json.dumps(self.meetup_3),
            content_type='application/json')
        self.assertEqual(res.status_code, 401)
