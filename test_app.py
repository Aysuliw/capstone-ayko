import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'ayko1999', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.casting_assistant = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdoWEk2TnB6dGVPTEtHcl9mZ0NKeCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMTNmMThmZjNiMTU1MDAxOTMzYjkwOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTk1MzQwNTE1LCJleHAiOjE1OTU0MjY5MTEsImF6cCI6IjlhY3pxMFVlS21lZlNaVWJhZEk4bnBsa1Ywd1ZaQlFOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.uYlURQgB3uaY8-9J5H1yik1mQ4bE4oeZ3cKd-nZEF-53ZldlA_0UwFHiVu4UkB41OYIA9g9VT0YEyPaBgNxvpE-7rvlMLYO4XL8dBDF3G2_vzuXdF6fP8oAsqJI2KmfUwjcHTRGP7J0tcYhiIlV3oY1EQWH9vqFs12Dd8owBJrT5e6a5A-KhXD7erbjMX6Qn-fTuM0mgit0V8R2m3SUHFE9a7W75s7LcJlqiabHK_rxYIfhdOvHYHHbscpiUNVhX8V22cI2ycXcUDdgMk929pVUGdLt5pS16yZt00N0YccENj-7rbi2Aud2imNmJZIamBEvxAGZT8jx7OIaPSKfuMg"
        self.casting_director = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdoWEk2TnB6dGVPTEtHcl9mZ0NKeCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMTQwMmQ2Yjc3NWM4MDAxM2E1MGMxMiIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTk1MzQwNzIzLCJleHAiOjE1OTU0MjcxMTksImF6cCI6IjlhY3pxMFVlS21lZlNaVWJhZEk4bnBsa1Ywd1ZaQlFOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIl19.KmGGK7uicxwXsDSWJl51nZqTnLvWN08u-ss_GghyeGZjxassKSbzoJPGvtwytHFAou3LVA0LzklinUVjloparlZ1o1t9Zg2W88VX4ylvQCm5UuDlX-UKXvfvTwrs1kbdHTH3_bVhFjeQsmwnFZZOA1uwlL-2NLNEqh6y-zHHhyuaJ68L-K8a74JAxwDsn2r-9aBO95ZzHbJAmlUJcOxN8wVQpWbYUf_zl7CywMg1y_3DQxv_GEBn7siAUvoohu5q2rsUg-khZbIpej82KeChZM9fKtivJvCnGNkpjXb-CGf63LATHhmH01E3vLIdxfO_mIEoYsIFqA_NwD-8bMyCvA"
        self.executive_producer = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdoWEk2TnB6dGVPTEtHcl9mZ0NKeCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMTQwOGM4MDUxN2M1MDAxM2I3Y2JhZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTk1MzQwNzg3LCJleHAiOjE1OTU0MjcxODMsImF6cCI6IjlhY3pxMFVlS21lZlNaVWJhZEk4bnBsa1Ywd1ZaQlFOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.jf9NemULxDyfcvIE-0pDO4eOMlf_Cad84RNurHrq2HUwtaQpT_VPkCHh3CkfT7_CkATkYV5twhnbZWbMva8G939TwoA5djvqo1-rmOZkwpN3BpfKjOLJJB5t1DrbU01-DXmb-l780HAr-c_NXaP6G7GVWEOuZ356HRZd2ySTXerROJONTRGuf45j_Uq_yIfAKWvlckt2Fuj8TDcGSjdLlADgpduBrX_aLOQUeQskyzo08Kl3p4_G-z5fETyvDzok5_AyCJsH6Hf8u_vIhCksWVXn1cvwpHs9TZeSB7pb8Nd9zjFYKEfaKa7oP2gCJQ2_vj4-ywJu7Tz-WRMlKQQNyw"
        self.new_movie = {
            'title': 'The Greatest Showman',
            'release_date': '2017'
        }
        self.new_actor = {
            'name': 'Hugh Jackman',
            'age': '51',
            'gender': 'Male'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Testing GET request

    def test_get_actors_casting_assistant(self):
        res = self.client().get(
            '/actors',
            headers={
                "Authorization": "Bearer " +
                self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_405_get_actors_method_not_allowed(self):
        res = self.client().get(
            '/actors/1000',
            headers={
                "Authorization": "Bearer " +
                self.executive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    # Testing POST request

    def test_add_actor(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                "Authorization": "Bearer " +
                self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_405_if_movie_creation_not_allowed(self):
        res = self.client().post(
            '/movies/100',
            json=self.new_movie,
            headers={
                "Authorization": "Bearer " +
                self.executive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_post_403_permission_not_found(self):
        res = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                "Authorization": "Bearer " +
                self.casting_director})

        self.assertEqual(res.status_code, 403)

    # Testing PATCH request

    def test_patch_actor(self):
        res = self.client().patch(
            '/actors/1',
            json={
                'age': '25'},
            headers={
                "Authorization": "Bearer " +
                self.executive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_patch_403_permission_not_found(self):
        res = self.client().patch(
            '/movies/1',
            json={
                'title': 'The Greatest Showman'},
            headers={
                "Authorization": "Bearer " +
                self.casting_assistant})

        self.assertEqual(res.status_code, 403)

    # Testing DELETE request

    def test_delete_actors(self):
        res = self.client().delete(
            '/actors/3',
            headers={
                "Authorization": "Bearer " +
                self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 3)

    def test_422_if_actor_does_not_exist(self):
        res = self.client().delete(
            '/actors/1000',
            headers={
                "Authorization": "Bearer " +
                self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
