from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
import os

db = SQLAlchemy()

# Production database URL
DATABASE_URL = ('postgres://ewjgvziegmlphb:4958d4551c9c85a92b84ecfc8bd2057c44'
                '3ae30cfe1f5e323b6686cadcc3fb46@ec2-50-17-90-177.compute-1.am'
                'azonaws.com:5432/d4ljtq026pifi9')


def setup_db(app, database_path=DATABASE_URL):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Tune(db.Model):
    __tablename__ = 'tune'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    composer = db.Column(db.Integer, db.ForeignKey('composer.id'))
    mastery = db.Column(db.Integer, db.ForeignKey('mastery.id'))
    key = db.Column(db.Integer, db.ForeignKey('key.id'))

    def __init__(self, title, composer, mastery, key):
        self.title = title
        self.composer = composer
        self.mastery = mastery
        self.key = key

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "title": self.title,
            "composer": self.composer,
            "key": self.key,
            "mastery": self.mastery
        }


class Composer(db.Model):
    __tablename__ = 'composer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return json.dumps({
            "name": self.name
        })


class Mastery(db.Model):
    __tablename__ = 'mastery'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String, nullable=False)

    def __init__(self, level):
        self.level = level

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return json.dumps({
            "level": self.level
        })


class Key(db.Model):
    __tablename__ = 'key'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, nullable=False)

    def __init__(self, key):
        self.key = key

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return json.dumps({
            "key": self.key
        })


class Playlist(db.Model):
    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return json.dumps({
            "playlist": self.name
        })


class Playlist_Tune(db.Model):
    __tablename__ = 'playlist_tune'

    id = db.Column(db.Integer, primary_key=True)
    playlist = db.Column(db.Integer, db.ForeignKey('playlist.id'),
                         nullable=False)
    tune = db.Column(db.Integer, db.ForeignKey('tune.id'), nullable=False)

    def __init__(self, playlist, tune):
        self.playlist = playlist
        self.tune = tune

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return json.dumps({
            "playlist": self.playlist,
            "tune": self.tune
        })
