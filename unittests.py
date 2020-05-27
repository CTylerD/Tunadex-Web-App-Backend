import os
import unittest
import json
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Tune, Playlist, Composer, Key, Mastery, Playlist_Tune
from app import app

teacher_auth_header = {
                            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNmRmZTlkMTA4ODViMGNhNmE5YzYwYyIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA2MDUzNzYsImV4cCI6MTU5MDYxMjU3NiwiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpzZXRsaXN0IiwiZGVsZXRlOnR1bmVzIiwiZ2V0OnNldGxpc3QiLCJnZXQ6dHVuZXMiLCJwYXRjaDpzZXRsaXN0IiwicGF0Y2g6dHVuZXMiLCJwb3N0OnNldGxpc3QiLCJwb3N0OnR1bmVzIl19.GFonjWyXxL74e37Muomd8O28vZJLVL4eydVtgCNzQBaECfVe6-RIE75zIyMHwoWWMvHXbAcSMhqITqUA2gegSqLZzhyU8CnyxbkJgd26t1fYHm-40bI73yoEg0h6A__rPyAp9MHlQocZQwOjntgC0VdQxilVw9KISzTN12Kq77YG49fQMqBO1_-NFJHT_XhQxblVutpdjbqdW4cTPoUvFBN0ZD-xMLCxn6n5PeJR48iBOBdJ3jUq-yZBeBy9VxOFh6jwmDDc6QdTRGc3m-2zpZt5Sar14fTwwQ7k3HZYMo3hsZBm4oYLvFVytW-PAX71ODyGx91AZeBTanH3SgZawA'
}

student_auth_header = {
                       'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzZlYzE0ZDY2ZTFjMGJmNDUzMGM4ZSIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA2MDU1MTMsImV4cCI6MTU5MDYxMjcxMywiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpzZXRsaXN0IiwiZ2V0OnR1bmVzIl19.EJhX2KxOd6r-q-zKM_tCZnDNFyMdin2ZC2Mvq7GXZj93V86msSQcxWpqkdKlPk0lx91xdOO2TN5AxH3oLRPJ060Y3xbYMIUD7be9ymDFz8cFde-3OpxSCrpgBPtlyWAqz0vYeduKNhanJnZkTn3yYRMtWRS51yvL0uMH7FQpchBj8pWYlFgMEm_0K78pai4sfha-bx_7AzavBSWkWxQrS9EpEiu7Rl-I9EkGpQ5xDv19BgvRJh78ZaopmnSgzssmOOEo1iEwkavVISYZuFlRlE4ZSJIJv8BdvH0BPY-T8865ga15fzQWUZiqfdy5_pKEAmtdwKEqSALKe2D1qbR5HQ'
}


class TunesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_tune_1 = {
            'title': 'Lush Life',
            'composer': 'Billy Strayhorn',
            'key': 'D-flat Major',
            'mastery': 4
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass


    def test_index_page(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_all_tunes(self):
        res = self.client().get('/tunes/', headers=teacher_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["tunes"])

if __name__ == '__main__':
    unittest.main()