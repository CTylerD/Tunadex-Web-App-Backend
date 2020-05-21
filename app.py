import os
from flask import Flask, jsonify
from models import setup_db
from flask_cors import CORS
from auth import requires_auth


def create_app(text_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    return app

app = create_app()

def dummy_data():
    string = "hi!"
    return jsonify(string)

@app.route('/')
def home():
    return dummy_data()

if __name__ == '__main__':
    app.run()
