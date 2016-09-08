#!.venv/bin/python
import os
import unittest

from app import app
from app import db
from app.models import User


class TestLogin(unittest.TestCase):
    def setUp(self):
        # import ipdb
        # ipdb.set_trace()
        app.config.from_object('config.TestConfig')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_login(self):
        url = '/'
        data = {'username': 'testuser', 'password': 'python'}
        response = self.app.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(User.query.all()), 1)

if __name__ == '__main__':
    unittest.main()
