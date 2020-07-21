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

        self.casting_assistant = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdoWEk2TnB6dGVPTEtHcl9mZ0NKeCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMTNmMThmZjNiMTU1MDAxOTMzYjkwOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTk1MTgyNDAxLCJleHAiOjE1OTUxODk2MDEsImF6cCI6IjlhY3pxMFVlS21lZlNaVWJhZEk4bnBsa1Ywd1ZaQlFOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.SN7Nmiodfq1Wq0BFiodYtutk4UpaaIIQ3g0Rte_TfdV05LkHCXnsRf8634grvGbPDwmsxHx0qs6eJ1iliNUjbyxQh35Eej9CCwLj0yZFH7Qn2SYHWepMCS2XN0KjBY7s-0EMGapGbdyAV0NjqcCs-phjt4jXTNeKDgg_7j5V8WCOr89pxIRgypr1O-ku0IPoN9MhFaLyM2Ldi21Fl4Qopx8RJ4dYQ37EPvd0ULd-uympKP0MXkSDMxW_tlPJcd10y1kGosy8QYxHkuaeIt_VLq5CbHgLd_FpotnbhGrKsoQPVBQ57yudytxUfcD_yfnY7VX4MRfya_kIZa38enJDNw"
        self.casting_director = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdoWEk2TnB6dGVPTEtHcl9mZ0NKeCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMTQwMmQ2Yjc3NWM4MDAxM2E1MGMxMiIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTk1MTc5MDkzLCJleHAiOjE1OTUxODYyOTMsImF6cCI6IjlhY3pxMFVlS21lZlNaVWJhZEk4bnBsa1Ywd1ZaQlFOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIl19.ruYUqBkMU9vD49WpBrRczPAq7vw7f9nK6rYKkKugLB_iTbIH4HUKayCKZlclhRHJD97KwVSC9R7GBF9RTj1_eyIFuu7uMlgD1Qx0AQJmyyL4VdpuydtbWhtr2kNUUrTd6VYGhLWpRtTY4VtRVm3aY09h3ndq4-Dd1pW8XgWO09_88zEZsP8ftkaHpGd3VKFwGmzEZQ25LO0c1Gva5bKhuK1tTOVZef-z8cFmNMXGyi-8pcBJLVzUr52k6m7kKDbJ_IBTpl4uuzQqt3eN2maluuWsuNcwiiwwGdRogJqgGj1H5-tXzCXx1lYLD06eaN6hVpm5vMYKMO45b5XQuFn4Ow"
        self.executive_producer = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdoWEk2TnB6dGVPTEtHcl9mZ0NKeCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMTQwOGM4MDUxN2M1MDAxM2I3Y2JhZCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTk1MTc5NTE3LCJleHAiOjE1OTUxODY3MTcsImF6cCI6IjlhY3pxMFVlS21lZlNaVWJhZEk4bnBsa1Ywd1ZaQlFOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.CXze-Ay9zb-ID9l5bHZnqahhY5AbDMCjfP7kSgdERlGClLjpmeygt53-By_-UF5QkiRmvcfEg_V2jV2nfoKlIFxFUhP27FP6qrHjiFFY0cqGp27AhZr32lx0gYuGP__NlwdJ_PyCYnhneMkOv5V6fQfQfkQpttCmJk-F9bCuVDK9ia15WEpKjid2UTidz-oTfKG36qt0BtBXG7cTowWXHoX6WaVZ85A2CUIvXIld7DUny-jRkraq0qQNDHBUM-9exECRGtw_OXVAyUVmjGnE_5GxMoYQFJWRApG3e8erUTRVd9eE5Bs1qbUiF7jXgeHJzcT1zR75x424lWUpt268SQ"
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
