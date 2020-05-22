import os
from flask import Flask, jsonify, redirect, render_template, session, url_for
from models import setup_db
from flask_cors import CORS
from auth import requires_auth, AUTH0_AUTHORIZE_URL
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db


def create_app(text_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    return app


app = create_app()
# app.secret_key = 'very secret key'

migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('/pages/index.html', auth_url=AUTH0_AUTHORIZE_URL)


@app.route('/login')
def login():
    return redirect(AUTH0_AUTHORIZE_URL)

@app.route('/home')
@requires_auth('get:tunes')
def home(jwt):
    return jsonify('hi')


if __name__ == '__main__':
    app.run()
