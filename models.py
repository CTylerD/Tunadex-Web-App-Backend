from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os
from app import app

db = SQLAlchemy()

database_path = "postgres://wdspwndlbhdcvj:d09f9e19edf9fb71d9879d37bde38c70415ba6a65a58dd695d3a7e075c2d1617@ec2-35-171-31-33.compute-1.amazonaws.com:5432/d3ib0ohrcrh0lh"

# setup_db(app)

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
