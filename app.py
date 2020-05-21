import os
from flask import Flask, jsonify
from models import setup_db
from flask_cors import CORS



def create_app(text_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    return app

def dummy_data(string):
    return jsonify(string)

string = "hi!"
dummy_data(string)

app = create_app()

if __name__ == '__main__':
    app.run()
