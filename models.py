from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
import os

db = SQLAlchemy()

database_name = 'tunadex'
database_path = 'postgres://wdspwndlbhdcvj:d09f9e19edf9fb71d9879d37bde38c70415ba6a65a58dd695d3a7e075c2d1617@ec2-35-171-31-33.compute-1.amazonaws.com:5432/d3ib0ohrcrh0lh'


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

# db_drop_and_create_all()


class Tune(db.Model):
    __tablename__ = 'tune'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    composer = Column(Integer, ForeignKey('composer.id'))
    mastery = Column(Integer, ForeignKey('mastery.id'))
    key = Column(Integer, ForeignKey('key.id'))

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
            'title': self.title,
            'composer': self.composer,
            'mastery': self.mastery,
            'key': self.key
        }


class Composer(db.Model):
    __tablename__ = 'composer'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

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
        return {
            'id': self.id,
            'name': self.name
        }


class Mastery(db.Model):
    __tablename__ = 'mastery'

    id = Column(Integer, primary_key=True)
    level = Column(String, nullable=False)

    def __init__(self, id, level):
        self.id = id
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
        return {
            'id': self.id,
            'level': self.level
        }


class Key(db.Model):
    __tablename__ = 'key'

    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)

    def __init__(self, key):
        self.id = id
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
            'id': self.id,
            'key': self.key
        }


class Playlist(db.Model):
    __tablename__ = 'playlist'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __init__(self, id, name):
        self.id = id
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
        return {
            'id': self.id,
            'playlist': self.name
        }


class Playlist_Tune(db.Model):
    __tablename__ = 'playlist_tune'

    id = Column(Integer, primary_key=True)
    playlist = Column(Integer, ForeignKey('playlist.id'), nullable=False)
    tune = Column(Integer, ForeignKey('tune.id'), nullable=False)

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
        return {
            'playlist': self.playlist,
            'tune': self.tune
        }
