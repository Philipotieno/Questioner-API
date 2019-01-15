import unittest
import json

from app.tests.v1.base import TestSetup

class TestMeetup(TestSetup):

    def test_created_meetup(self):
        """ Test new meetup can be created """
        res = self.client.post(
            '/api/v1/meetups',
            data=json.dumps(self.meetup_2),
            content_type='application/json')
        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Meetup created successfully", msg["Message"])


    def test_get_all_meetup(self):

        self.client.post(
            '/api/v1/meetups',
            data=json.dumps(self.add_meetup),
            content_type='application/json')

        res = self.client.get(
            '/api/v1/meetups/upcoming',
            content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_specific_meetup(self):

        res = self.client.post(
            '/api/v1/meetups',
            data=json.dumps(self.add_meetup),
            content_type='application/json')

        res = self.client.get(
            '/api/v1/meetups/1',
            content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_non_exixting_meetup(self):

        res = self.client.get(
            '/api/v1/meetups/12',
            data=json.dumps(self.meetup_1),
            content_type='application/json')
        self.assertEqual(res.status_code, 404)


    def test_rsvp_meetup(self):

        self.client.post(
            '/api/v1/meetups/1',
            data=json.dumps(self.add_meetup),
            content_type='application/json')

        res = self.client.post(
            '/api/v1/meetups/1/rsvp',
            data=json.dumps(dict(attending="maybe")),
            content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_rsvp_non_existent_status(self):

        res = self.client.post(
            '/api/v1/meetups/44/rsvp',
            data=json.dumps(dict(attending="nono")),
            content_type='application/json')
        self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()
