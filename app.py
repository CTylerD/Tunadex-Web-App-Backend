import os
from flask import Flask, jsonify, redirect, render_template, session, url_for
from models import setup_db
from flask_cors import CORS
from auth import requires_auth, AUTH0_AUTHORIZE_URL
from authlib.integrations.flask_client import OAuth


def create_app(text_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    return app

app = create_app()
app.secret_key = 'very secret key'


@app.route('/')
def index():
    return jsonify('hi')


@app.route('/home')
@requires_auth('get:tunes')
def home(jwt):
    return jsonify('hi')


@app.route('/login')
def login():
    return redirect(AUTH0_AUTHORIZE_URL)


if __name__ == '__main__':
    app.run()
