import os
from flask import Flask, jsonify, redirect, render_template, session, url_for, request, abort
import json
from models import setup_db
from flask_cors import CORS
from auth import requires_auth, AUTH0_AUTHORIZE_URL
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, Tune, Composer, Mastery, Key, Playlist, Playlist_Tune


app = Flask(__name__)
app.secret_key = 'app'
setup_db(app)
CORS(app)

migrate = Migrate(app, db)


def return_composer(composer_name):
    composer_entry = Composer.query.filter_by(name=composer_name).first()
    if composer_entry is None:
        new_composer = Composer(name=composer_name)
        try:
            new_composer.insert()
            composer_entry = Composer.query.filter_by(name=composer_name)\
                                           .first()
        except Exception as e:
            print("Composer failed to insert")
            abort(400)
    return composer_entry


@app.route('/')
def index():
    return render_template('/pages/index.html', auth_url=AUTH0_AUTHORIZE_URL)


@app.route('/home/')
def home(jwt):
    token = request.get('token')
    print(token)
    return 0


@app.route('/tunes/', methods=['GET'])
def all_tunes():
    # Returns a list of all tunes from database.
    try:
        tunes_list = Tune.query.order_by(Tune.title).all()
        library = {'tunes': {}}
        for tune in tunes_list:
            library['tunes'][tune.title] = {}
            library['tunes'][tune.title]['composer'] = tune.composer
            library['tunes'][tune.title]['key'] = tune.key
            library['tunes'][tune.title]['mastery'] = tune.mastery
            print
        return json.dumps(library)
    except Exception as e:
        print(e)
        abort(400)


@app.route('/tunes/<id>', methods=['GET'])
def tune_info(id):
    # Returns the requested tune from database.
    try:
        tune = Tune.query.filter_by(id=id).first()
        library = {}
        library['title'] = tune.title
        library['composer'] = tune.composer
        library['key'] = tune.key
        library['mastery'] = tune.mastery
        return json.dumps(library)
    except Exception as e:
        print(e)
        abort(400)


@app.route('/tunes/', methods=['POST'])
def add_tune():
    # Retrieves the tune metadata from the request.
    tune_data = json.loads(request.data.decode('utf-8'))

    # Determines whether or not the tune is already in the database.
    tune_exists = Tune.query.filter_by(title=tune_data['title']).first()
    if tune_exists is not None:
        print("A tune with this title already exists!")
        abort(409)

    # Retrieves the composer and key objects, for determining their IDs.
    composer = return_composer(tune_data['composer'])
    key = Key.query.filter_by(key=tune_data['key']).first()
    
    # Builds the new tune object and insert into the database.
    new_tune = Tune(title=tune_data['title'],
                    composer=composer.id,
                    key=key.id,
                    mastery=tune_data['mastery']
                    )
    try:
        new_tune.insert()
        return json.dumps({'success': True,
                           'new tune': new_tune.format()})
    except Exception as e:
        print(e)
        abort(400)


@app.route('/tunes/<id>', methods=['PATCH'])
def edit_tune(id):
    data = json.loads(request.data.decode('utf-8'))
    tune = Tune.query.filter_by(id=id).first()
    if tune is None:
        abort(404)
    if data.get('title'):
        tune.title = data['title']
    if data.get('composer'):
        tune.composer = data['composer']
    if data.get('key'):
        tune.key = data['key']
    if data.get('mastery'):
        tune.mastery = data['mastery']
    try:
        tune.update()
        return json.dumps({'success': True, "updated tune": tune.format()})
    except Exception as e:
        print(e)
        abort(400)


@app.route('/tunes/<id>', methods=['DELETE'])
def delete_tune(id):
    tune = Tune.query.filter_by(id=id).first()

    try:
        tune.delete()
    except Exception as e:
        print(e)
        abort(400)
    return json.dumps({'success': True, "deleted tune": tune.format()})



@app.route('/playlists', methods=['GET'])
def all_playlists():
    return "not implemented"


@app.route('/playlists/<id>', methods=['GET'])
def playlist_info(id):
    return "not implemented"


@app.route('/playlists/<id>', methods=['POST'])
def add_playlist(id):
    return "not implemented"


@app.route('/playlists/<id>', methods=['PATCH'])
def edit_playlist(id):
    return "not implemented"


@app.route('/playlists/<id>', methods=['DELETE'])
def delete_playlist(id):
    return "not implemented"


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable"
                    }), 422


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404


@app.errorhandler(400)
def resource_not_found(error):
    return jsonify({
                    "success": False,
                    "error": 400,
                    "message": "bad request"
                    }), 400


@app.errorhandler(401)
def auth_error_handler(error):
    return jsonify({
                    "success": False,
                    "error": 401,
                    "message": "not authorized"
    }), 401


@app.errorhandler(409)
def auth_error_handler(error):
    return jsonify({
                    "success": False,
                    "error": 409,
                    "message": "conflict"
    }), 409


if __name__ == '__main__':
    app.run()
