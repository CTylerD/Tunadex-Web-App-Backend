import os
from flask import Flask, jsonify, redirect, render_template, session, url_for
from models import setup_db
from flask_cors import CORS, cross_origin
from auth import requires_auth, AUTH0_AUTHORIZE_URL
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
app.secret_key = 'app'
setup_db(app)
CORS(app)

migrate = Migrate(app, db)

#    return app


# app = create_app()
# app.secret_key = 'very secret key'


@app.route('/')
def index():
    return render_template('/pages/index.html', auth_url=AUTH0_AUTHORIZE_URL)


# @app.route('/login/')
# def login():
#     return auth0.authorize_redirect(redirect_uri=REDIRECT_URI)


@app.route('/home/')
# @cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth('get:tunes')
def home(jwt):
    return jsonify('hi')


if __name__ == '__main__':
    app.run()
