import os
from dotenv import load_dotenv
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db


load_dotenv()
db_path = os.getenv('DATABASE_URL')


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        setup_db(self.app, db_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie = {
            'title': 'Test Test',
            'release_date': '3 / 3 / 2020'
        }

        self.new_actor = {
            'name': 'Test Test',
            'birth_date': '11/11/1991',
            'gender': 'M'
        }

        self.edited_movie = {
            'release_date': '4 / 4 / 2020'
        }

        self.edited_actor = {
            'gender': 'O'
        }

        # all tests ran for Executive Director Role. RBAC tests for all the roles are in Postman collection
        self.payload = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImllWm9CYzM5a3g1cU5MeTNxSTJnUCJ9.eyJpc3MiOiJodHRwczovL2Rldi05NHYzZmJ3OC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjZDFlYzU3YzQ1Y2YwMDY5YWFhNzdlIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTYwODY0MzgwNiwiZXhwIjoxNjA4NzMwMjA2LCJhenAiOiJkS2xOOWRIY0FUd0NJR3VWSm9WT25HRVlvZ3psRDJ3WSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.kesDjAwTHmPsnMhuYR6M4-KoiwJrK2PzBOGA0PB2J9WZJV61JESTexXmjirUX0I1ottSOAP2j0pPtdPkJjTwX1WRxGU8MsTGjbvudYMxnDQB29UX2YT-12mpT7wWCvzDT4CoyQrzWnI9eImwneyjW4Hq4EnJbpLlzKj5URKPWZFq-DJitkOFNQYRjw6cNTjdNtUIzzAgcAHq9FXbfj62t5LprzlYEZTBnU2ZsR_lYC2hpJ9doWJ8Jz7BE_JDgR-wNQf1gT5GVQEYqIjDhTx0ptwgj-Z-htlRkZxC4KhuBaIti13i3sXgNBH1QJAlDw0yz3-tANzcHFAl_rQPtTgIbQ'

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_add_movie(self):
        res = self.client().post('/movies', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.payload}')
            ], json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)

    def test_400_add_movie(self):
        res = self.client().post('/movies', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.payload}')
            ], json=json.dumps({'movie': 'wont load'}))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)

    def test_add_actor(self):
        res = self.client().post('/actors', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.payload}')
            ], json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)

    def test_400_add_actor(self):
        res = self.client().post('/actors', headers=[
                ('Content-Type', 'application/json'),
                ('Authorization', f'Bearer {self.payload}')
            ], json=json.dumps({'actor': 'wont load'}))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)

    def test_get_movies(self):
        res = self.client().get('/movies', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'], True)

    def test_400_get_movies(self):
        res = self.client().get('/movies', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ])
        data = json.loads(res.data)

        self.assertNotEqual(res.status_code, 400)

    def test_get_actors(self):
        res = self.client().get('/actors', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'], True)

    def test_400_get_actors(self):
        res = self.client().get('/actors', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ])
        data = json.loads(res.data)

        self.assertNotEqual(res.status_code, 400)

    def test_edit_movie(self):
        res = self.client().patch('/movies/8', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ], json=self.edited_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movie'], True)

    def test_400_edit_movie(self):
        res = self.client().patch('/movies/1000', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ], json=self.edited_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)

    def test_edit_actor(self):
        res = self.client().patch('/actors/6', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ], json=self.edited_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actor'], True)

    def test_400_edit_actor(self):
        res = self.client().patch('/actors/1000', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ], json=self.edited_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)

    def test_delete_movie(self):
        res = self.client().delete('/movies/8', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movie'], True)

    def test_400_delete_movie(self):
        res = self.client().delete('/movies/1000', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)

    def test_delete_actor(self):
        res = self.client().delete('/actors/6', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actor'], True)

    def test_400_delete_actor(self):
        res = self.client().delete('/actors/6', headers=[
                    ('Content-Type', 'application/json'),
                    ('Authorization', f'Bearer {self.payload}')
                ])
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)


# Run tests
if __name__ == "__main__":
    unittest.main()
