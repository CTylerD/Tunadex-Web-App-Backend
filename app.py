import os
from flask import Flask, jsonify
from models import setup_db
from flask_cors import CORS

app = Flask(__name__)

def create_app(text_config=None):
    setup_db(app)
    CORS(app)

    return app

def dummy_data(string):
    return jsonify(string)

string = "hi!"
dummy_data(string)
