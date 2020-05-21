from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

db = SQLAlchemy()

database_path = os.environ.get('DATABASE_URL')
if not database_path:
    print("Running local db")
    database_path = "postgres://localhost:5432/tunadex"

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
