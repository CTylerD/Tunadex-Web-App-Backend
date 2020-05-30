import os
import unittest
import json
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .models import (setup_db, Tune, Playlist, Composer, Key, Mastery,
                    Playlist_Tune)
from .app import app
from .auth import AuthError


teacher_auth_header = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNmRmZTlkMTA4ODViMGNhNmE5YzYwYyIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA4NjQyNzksImV4cCI6MTU5MDk1MDY3OSwiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpzZXRsaXN0IiwiZGVsZXRlOnR1bmVzIiwiZ2V0OnNldGxpc3QiLCJnZXQ6dHVuZXMiLCJwYXRjaDpzZXRsaXN0IiwicGF0Y2g6dHVuZXMiLCJwb3N0OnNldGxpc3QiLCJwb3N0OnR1bmVzIl19.KReJOWxzzRawoYm52sRr69TdwQFwn97Jeo_C0DdHhHsg4ha22Ak-FHLoIrIYUy5gp2YxQaQ69gxQOjmnoSlY4_hwfZjSfEXdzcU3WjhGD94G3t2LbuH1E1uBcZU7acw2Dp2naE0IscMqEdmncSxBRd1Dsle6rawkz_vEKISo-EqYTdD-YeWSusouEEeVZx8sRxh7PAdUXfIG533bZEdSUTxf52vtmI5ZsRnYLQzhqdwzM8fdtCtVcj7lUXKvzBTAxt-hwMlLptaiE1Nw4xzGAUigxuGiFkY4vY30TOE3h8rjCcErQH8-r1W1EYZioq6b7sgLqWxdTkJ61x5paDFlHA'
}

student_auth_header = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzZlYzE0ZDY2ZTFjMGJmNDUzMGM4ZSIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA4NjQxODEsImV4cCI6MTU5MDk1MDU4MSwiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpzZXRsaXN0IiwiZ2V0OnR1bmVzIl19.hijClFAtRnd6jrM7xSTDhFWvllgYjnCj11YExK-PQzWclpTLr4VwM3Ixxy58oiwZdoXjw5Pw1TN4U_2xoKQRSFX7KiXL9q4M9EzgSOGy2jFWa3_z_3Lj1EHed0NQq-9Z2av84VJj9mf67jN2z_62qHZVHtePFqUI8mjCHfW9ZYVkKgnd3u2mi_n1hxDpms_DB6fA1DCLPI5JfOJwMgsUyNiKs4igFnD4xs_CTIA5mWiqOB1cUklE0m0uHc9-LSlJ5TM03WJ99bRFtfhPv0mIOw9BKotWAldZugyAobSAyD2BTp8jq2_Dr1CEeq5abSNHraQgfXbqTLvRi_HN_ZzpNA'
}


class TunesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.database_name = "tunadex_local_db"
        # self.database_path = ("postgresql://postgres:postgres@localhost:5432"
                              # f"/{self.database_name}")
        self.database_path = "postgres://ewjgvziegmlphb:4958d4551c9c85a92b84ecfc8bd2057c443ae30cfe1f5e323b6686cadcc3fb46@ec2-50-17-90-177.compute-1.amazonaws.com:5432/d4ljtq026pifi9"
        setup_db(self.app, self.database_path)

        self.tune_data = [
            Tune(
                title='Lush Life',
                composer=1,
                key=6,
                mastery=4
            ),
            Tune(
                title='Body and Soul',
                composer=2,
                key=6,
                mastery=5
            ),
            Tune(
                title='Freddie the Freeloader',
                composer=3,
                key=3,
                mastery=5
            )
        ]

        self.composer_data = [
            Composer(
                'Billy Strayhorn'
            ),
            Composer(
                'Johnny Green, Edward Heyman, Robert Sour, Frank Eyton'
            ),
            Composer(
                'Miles Davis'
            )
        ]

        self.key_data = [
            Key(
                key='C Major'
            ),
            Key(
                key='F Major'
            ),
            Key(
                key='B-flat Major'
            ),
            Key(
                key='E-flat Major'
            ),
            Key(
                key='A-flat Major'
            ),
            Key(
                key='D-flat Major'
            ),
            Key(
                key='G-flat Major'
            ),
            Key(
                key='C-flat Major'
            ),
            Key(
                key='C-sharp Major'
            ),
            Key(
                key='F-sharp Major'
            ),
            Key(
                key='B Major'
            ),
            Key(
                key='E Major'
            ),
            Key(
                key='A Major'
            ),
            Key(
                key='D Major'
            ),
            Key(
                key='G Major'
            ),
            Key(
                key='A Minor'
            ),
            Key(
                key='D Minor'
            ),
            Key(
                key='G Minor'
            ),
            Key(
                key='C Minor'
            ),
            Key(
                key='F Minor'
            ),
            Key(
                key='B-flat Minor'
            ),
            Key(
                key='E-flat Minor'
            ),
            Key(
                key='A-flat Minor'
            ),
            Key(
                key='A-sharp Minor'
            ),
            Key(
                key='D-sharp Minor'
            ),
            Key(
                key='G-sharp Minor'
            ),
            Key(
                key='C-sharp Minor'
            ),
            Key(
                key='F-sharp Minor'
            ),
            Key(
                key='B Minor'
            ),
            Key(
                key='E Minor'
            )
        ]

        self.mastery_data = [
            Mastery(
                level="Don't know at all"
            ),
            Mastery(
                level='Not in ear, but can read'
            ),
            Mastery(
                level='In ear, but not memorized'
            ),
            Mastery(
                level='Memorized, but actively thinking'
            ),
            Mastery(
                level='Mastered, know it cold'
            )
        ]

        self.tune_3_patch = {
            "title": "Lush Life",
            "composer": "Billy Strayhorn",
            "key": "D-flat Major",
            "mastery": 5
        }

        self.new_tune_4 = {
            "title": "Footprints",
            "composer": "Wayne Shorter",
            "key": "C Minor",
            "mastery": 5
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.reflect()
            self.db.drop_all()
            self.db.create_all()
            self.db.init_app(self.app)

        for composer in self.composer_data:
            composer.insert()
        for key in self.key_data:
            key.insert()
        for mastery in self.mastery_data:
            mastery.insert()
        for tune in self.tune_data:
            tune.insert()

    def tearDown(self):
        # In the event that any part of the testing process fails prior to
        # this point and tearDown isn't run, the database is reset in setUp
        # with self.db.reflect() / self.db.drop_all() / self.db.create_all().
        pass

    def test_index_page(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_all_tunes_teacher(self):
        res = self.client().get('/tunes/', headers=teacher_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['tunes'])

    def test_get_all_tunes_student(self):
        res = self.client().get('/tunes/', headers=student_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['tunes'])

    def test_get_tune_by_id_teacher(self):
        res = self.client().get('/tunes/1/', headers=teacher_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data.get('tune'))

    def test_get_tune_by_id_student(self):
        res = self.client().get('/tunes/1/', headers=student_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['tune'])

    def test_404_get_tune_with_nonexistant_id_teacher(self):
        res = self.client().get('/tunes/10000/', headers=teacher_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertFalse(data.get('tune'))
        self.assertTrue(data['message'], 'resource not found')

    def test_404_get_tune_with_nonexistant_id_student(self):
        res = self.client().get('/tunes/10000/', headers=student_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertFalse(data.get('tune'))
        self.assertTrue(data['message'], 'resource not found')

    def test_400_get_tune_with_non_int_id_teacher(self):
        res = self.client().get('/tunes/abc/', headers=teacher_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertFalse(data.get('tune'))
        self.assertTrue(data['message'], 'bad request')

    def test_400_get_tune_with_non_int_id_student(self):
        res = self.client().get('/tunes/abc/', headers=student_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertFalse(data.get('tune'))
        self.assertTrue(data['message'], 'bad request')

    def test_post_new_tune_teacher(self):
        res = self.client().post('/tunes/', headers=teacher_auth_header,
                                 json=self.new_tune_4)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new tune'])

    def test_403_post_tune_student(self):
        res = self.client().post('/tunes/', headers=student_auth_header,
                                 json=self.new_tune_4)

        self.assertRaises(AuthError)

    def test_405_post_tune_with_id_teacher(self):
        res = self.client().post('/tunes/200', headers=teacher_auth_header,
                                 json=self.new_tune_4)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'method not allowed')

    def test_update_tune_teacher(self):
        res = self.client().patch('tunes/1', headers=teacher_auth_header,
                                  json=self.tune_3_patch)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated tune'])

    def test_403_update_tune_student(self):
        res = self.client().patch('/tunes/1000', headers=student_auth_header,
                                  json=self.tune_3_patch)

        self.assertRaises(AuthError)

    def test_404_update_tune_with_nonexistant_id_teacher(self):
        res = self.client().patch('tunes/1000', headers=teacher_auth_header,
                                  json=self.tune_3_patch)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'resource not found')

    def test_403_update_tune_with_nonexistant_id_student(self):
        res = self.client().patch('/tunes/1000', headers=student_auth_header,
                                  json=self.tune_3_patch)

        self.assertRaises(AuthError)

    def test_delete_tune_teacher(self):
        res = self.client().delete('/tunes/1', headers=teacher_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted tune'])

    def test_422_delete_tune_does_not_exist_teacher(self):
        res = self.client().delete('/tunes/100', headers=teacher_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'resource not found')

    def test_403_delete_tune_student(self):
        res = self.client().delete('/tunes/2', headers=student_auth_header)

        self.assertRaises(AuthError)


if __name__ == '__main__':
    unittest.main()
