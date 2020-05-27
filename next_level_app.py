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
    playlist = Playlist.query.filter_by(id=id).first()

    try:
        playlist.delete()
    except Exception as e:
        print(e)
        abort(400)
    return json.dumps({'success': True, "deleted playlist": playlist.format()})

