import os
import unittest
import json
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
from models import setup_db, Tune, Playlist, Composer, Key, Mastery, Playlist_Tune
from sqlalchemy.engine import reflection
from sqlalchemy.schema import MetaData, Table, DropTable, ForeignKeyConstraint, DropConstraint
from app import app


teacher_auth_header = {
                        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNmRmZTlkMTA4ODViMGNhNmE5YzYwYyIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA3MDgxMTEsImV4cCI6MTU5MDc5NDUxMSwiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpzZXRsaXN0IiwiZGVsZXRlOnR1bmVzIiwiZ2V0OnNldGxpc3QiLCJnZXQ6dHVuZXMiLCJwYXRjaDpzZXRsaXN0IiwicGF0Y2g6dHVuZXMiLCJwb3N0OnNldGxpc3QiLCJwb3N0OnR1bmVzIl19.PKvHTxRFkocpcm3PHMuGGWf-v8h1tsfyZoRUQx0j7qVYlMBXpj8MFCsuzKwBtLQTLwtScdUqMsBi428tkSdwHonPJ6URnAETBcRjmxcYUz1FXAFLupZH-yt311pMuhoN_3qXTFqDFHvkAWHRS5DitKoU40tRyAejcDlYEX1uPV94i3qjFzP3zh2EJrsAw6RVLsAr3rhL5fGSk-PUbISN1vyjx8mNDlEpSU2VJ05DRst3qKR6tIPOhlZ8AQyQUHQYIhi--fcKjenXYlh5MilTnpVBNt5rG-9TilN5VxRGm4nOvC_tCiffc__7AhhPftw5i8Vwo8Ps8AO7XX9BHKsyQw'
}

student_auth_header = {
                       'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzZlYzE0ZDY2ZTFjMGJmNDUzMGM4ZSIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA3MDgwNTIsImV4cCI6MTU5MDc5NDQ1MiwiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpzZXRsaXN0IiwiZ2V0OnR1bmVzIl19.In-uEyLuPid4frLeG8oe4iLhf-DtW6e64m1IDTA3onOKg95M2X1BbBPH_hSfihlYj6Kc4OhHyLc3uaf9407VdiT02l_Odz98-QGodWrKfim9YBh-DfGoaCTbtvJZR6sL17KqDnaRALDU2PcEWZ9WLmZQHDXGcG8Vr0Hy-d2L8KiknjhPQGKwRh3GHHDTrxpfi-fMgaMdPd8nl1nHiXlOZ2uZXiKSHt7akSEWqw6iat_EFrteVOg3oEcXOk7gEGSXXVpokHaA9Yr6dbFdwAu7qkImU11SyWeORkPbONe1UzACYyYtBo4R3-DPOeM8BJAbNIKRnBUn8MZZAqJa48s2_g'
}

class TunesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        # self.app.app_context().push()
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgresql://postgres:postgres@{}/{}".format('localhost:5432', self.database_name)
        self.engine = create_engine(self.database_path)
        setup_db(self.app, self.database_path)
        

        self.tune_data = [Tune(
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
                                      "Billy Strayhorn"
                              ),
                              Composer(
                                      "Johnny Green, Edward Heyman, Robert Sour, Frank Eyton"
                              ),
                              Composer(
                                      "Miles Davis"
                              )
        ]
        
        self.key_data = [Key(
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
                                    level="Not in ear, but can read"
                                    ),
                            Mastery(
                                    level="In ear, but not memorized"
                                    ),
                            Mastery(
                                    level="Memorized, but actively thinking"
                                    ),
                            Mastery(
                                    level="Mastered, know it cold"
                                    )
        ]

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
        self.assertEqual(data["success"], True)
        self.assertTrue(data["tunes"])

    def test_get_all_tunes_student(self):
        res = self.client().get('/tunes/', headers=student_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["tunes"])

    def test_get_tune_by_id_teacher(self):
        res = self.client().get('/tunes/1/', headers=teacher_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data.get("tune"))

    def test_get_tune_by_id_student(self):
        res = self.client().get('/tunes/1/', headers=student_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data.get("tune"))

    def test_404_get_tune_by_id_teacher(self):
        res = self.client().get('/tunes/10000/', headers=teacher_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertFalse(data.get("tune"))
        self.assertTrue(data.get['message'], "resource not found")

    def test_404_get_tune_by_id_student(self):
        res = self.client().get('/tunes/10000/', headers=student_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertFalse(data.get("tune"))
        self.assertTrue(data.get['message'], "resource not found")

    def test_400_get_tune_by_id_teacher(self):
        res = self.client().get('/tunes/abc/', headers=teacher_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertFalse(data.get("tune"))
        self.assertTrue(data.get['message'], "bad request")
        
    def test_400_get_tune_by_id_student(self):
        res = self.client().get('/tunes/abc/', headers=student_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertFalse(data.get("tune"))
        self.assertTrue(data.get['message'], "bad request")

    def test_post_new_tune_teacher(self):
        res = self.client().post('/tunes/', headers=teacher_auth_header, json=self.new_tune_4)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data.get("new tune"))

    def test_401_post_new_tune_student(self):
        res = self.client().post('/tunes/', headers=teacher_auth_header, json=self.new_tune_4)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertFalse(data.get("new tune"))
        self.assertTrue(data.get['message'], "not authorized")

    def test_405_post_new_tune_teacher(self):
        res = self.client().post('/tunes/200', headers=teacher_auth_header, json=self.new_tune_4)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], True)
        self.assertTrue(data.get("new tune"))
    
    def test_delete_tune_teacher(self):
        res = self.client().delete('/tunes/1', headers=teacher_auth_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data.get("deleted tune"))
    

if __name__ == '__main__':
    unittest.main()