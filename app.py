import os
from flask import Flask, jsonify, redirect, render_template, session, url_for, request, abort
import json
from models import setup_db
from flask_cors import CORS
from auth import requires_auth, AUTH0_AUTHORIZE_URL
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, Tune, Composer, Mastery, Key, Playlist, Playlist_Tune

def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    return app

app = create_app()
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
            abort(400, "Composer failed to insert!")
    return composer_entry

def tunes_to_dict(tune_list):
    library = {}
    for tune in tune_list:
        library[tune.title] = {}
        library[tune.title]['composer'] = tune.composer
        library[tune.title]['key'] = tune.key
        library[tune.title]['mastery'] = tune.mastery
    return library


@app.route('/')
def index():
    return render_template('/pages/index.html', auth_url=AUTH0_AUTHORIZE_URL)


@app.route('/tunes/', methods=['GET'])
@requires_auth("get:tunes")
def all_tunes(jwt):
    # Returns a list of all tunes from database.
    try:
        tune_list = Tune.query.all()
        if tune_list is None:
            abort(404, 'There are no tunes in the database!')

        library = tunes_to_dict(tune_list)
        return json.dumps({
            "success": True,
            "tunes": library
        }), 200
    except Exception as e:
        print(e)
        abort(400)


@app.route('/tunes/<id>/', methods=['GET'])
@requires_auth("get:tunes")
def single_tune_info(jwt, id):
    try:
        id = int(id)
        tune = Tune.query.filter_by(id=id).first()

        if tune is None:
            abort(404, "Tune with this id not found!")

        library = tunes_to_dict([tune])
        return json.dumps({
            "success": True,
            "tune": library
        }), 200
    except ValueError:
        abort(400, "Tune id must be an integer")
    except Exception as e:
        if tune is None:
            print(e)
            abort(404)
        else: 
            print(e)
            abort(400)


@app.route('/tunes/', methods=['POST'])
@requires_auth("post:tunes")
def add_tune(jwt):
    # Retrieves the tune metadata from the request.
    tune_data = json.loads(request.data.decode('utf-8'))

    # Determines whether or not the tune is already in the database.
    tune_exists = Tune.query.filter_by(title=tune_data['title']).first()
    if tune_exists is not None:
        abort(409, "A tune with this title already exists!")

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
@requires_auth("patch:tunes")
def edit_tune(jwt, id):
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
        return json.dumps({'success': True, "updated tune": tune.format()}), 200
    except Exception as e:
        print(e)
        abort(400)


@app.route('/tunes/<id>', methods=['DELETE'])
@requires_auth("delete:tunes")
def delete_tune(jwt, id):
    tune = Tune.query.filter_by(id=id).first()

    try:
        tune.delete()
        db.session.commit()
    except Exception as e:
        print(e)
        abort(400)
    return json.dumps({'success': True, "deleted tune": tune.format()})


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
