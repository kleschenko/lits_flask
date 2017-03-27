import unittest

from main import app, db
from models import User


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_hello_world(self):
        expected_text = 'Hello world'
        self.assertEqual(expected_text, 'Hello world')

    def test_app_config(self):
        self.assertEqual(app.config['SQLALCHEMY_DATABASE_URI'],
                         'sqlite:///test.db')

    def test_user_model(self):
        u = User(username='user', email='email@example.com')
        db.session.add(u)
        db.session.commit()

        users = User.query.all()
        self.assertEqual(len(users), 1)

    def test_user_pretty_print(self):
        u = User(username='user', email='email@example.com')
        db.session.add(u)
        db.session.commit()

        pretty_printed_name = u.pretty_print_user()
        self.assertEqual(pretty_printed_name, 'Username: user, name: None')

    def test_user_upper_name(self):
        u = User(username='user', email='email@example.com', name='lower')
        db.session.add(u)
        db.session.commit()

        upper_name = u.upper_name()
        self.assertEqual(upper_name, 'LOWER')
