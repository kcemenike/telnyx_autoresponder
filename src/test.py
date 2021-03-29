import unittest
import json
from app import app, parse_message
from constants import MAPPING, DEFAULT

# Test data
TEST_DATA = {
    "data": {
        "event_type": "message.received",
        "id": "3f13491e-0365-4498-9608-ae4b8ed4ca72",
        "occurred_at": "2021-03-27T13:59:28.773+00:00",
        "payload": {
            "cc": [],
            "completed_at": None,
            "cost": None,
            "direction": "inbound",
            "encoding": "GSM-7",
            "errors": [],
            "from": {
                "carrier": "",
                "line_type": "",
                "phone_number": "+2348034381517"
            }, "id": "f355574f-9d46-4e60-8487-b18127b265b9",
            "media": [],
            "messaging_profile_id": "40017873-eca0-451a-b060-0d84d941cda3",
            "organization_id": "03b16fde-e623-4b5e-b3bf-6ae853d2da85",
            "parts": 1,
            "received_at": "2021-03-27T13:59:28.652+00:00",
            "record_type": "message",
            "sent_at": None,
            "tags": [],
            "text": "This is a test SMS",
            "to": [
                {
                    "carrier": "Telnyx",
                    "line_type": "Wireless",
                    "phone_number": "+14192734689",
                    "status": "webhook_delivered"
                }
            ],
            "type": "SMS",
            "valid_until": None,
            "webhook_failover_url": "https://webhook.site/b1ca7a7d-3168-4983-8943-8fe72337d0b9",
            "webhook_url": "http://391e80463d1d.ngrok.io/webhooks"},
        "record_type": "event"},
    "meta": {
        "attempt": 1,
        "delivered_to": "http://391e80463d1d.ngrok.io/webhooks"
    }
}


class AutoResponderTestCase(unittest.TestCase):
    '''This test represents the AutoResponder test case'''

    def setUp(self):
        self.MAPPING = MAPPING
        self.DEFAULT = DEFAULT
        self.TEST_DATA = TEST_DATA
        self.from_ = self.TEST_DATA['data']['payload']['from']['phone_number']
        self.to = self.TEST_DATA['data']['payload']['to'][0]['phone_number']
        self.text = self.TEST_DATA['data']['payload']['text'].lower()
        self.app = app
        self.testing = True
        self.client = self.app.test_client

    def tearDown(self):
        pass

    # Test that service is up
    def test_working_server(self):
        res = self.client().get('/test')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    # Test message parser / converter
    def test_parse_correct_message(self):
        parsed_message = parse_message(self.TEST_DATA)
        from_ = parsed_message.get('from')
        to = parsed_message.get('to')
        message = parsed_message.get('reply')
        expected_message = "Please send either the word 'pizza' or 'ice cream' for a different response"
        self.assertEqual(from_, self.from_)
        self.assertEqual(to, self.to)
        self.assertEqual(message, expected_message)

    # Test when nothing/or blank is passed to message
    def test_parse_wrong_message(self):
        result = parse_message("")
        expected = None
        self.assertEqual(result, expected)

    # Test autoresponse
    def test_autoresponse(self):
        res = self.client().post('/webhooks',
                                 json=self.TEST_DATA,
                                 content_type="application/json"
                                 )
        data = json.loads(res.data)
        # print('data', self.TEST_DATA)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Autoresponder complete')

    # Test when users try to use GET for autoresponse endpoint
    def test_autoresponse_get(self):
        res = self.client().get('/webhooks')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'bad request')

    # Test when wrong data is passed to endpoint
    def test_bad_data_to_autoresponse(self):
        res = self.client().post('/webhooks',
                                 json=None,
                                 content_type="application/json"
                                 )
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'bad request')


# Run all tests
if __name__ == "__main__":
    unittest.main()
