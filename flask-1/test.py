from unittest import TestCase
from app import app
from flask import session

class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client
        app.config["TESTING"] = True

    def valid_from(self):
        response = self.client.get('/currency-check')
        # self.assertEqual(response.json[])


    def test_homepage(self):
        with self.client:
            res = self.client.get('/')
            self.assertIn(b"<h1>Currency Converter", res.data)