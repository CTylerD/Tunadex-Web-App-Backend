oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id='WJsA7RsGClFh95xdmI0Q7R2yIy78QHHf',
    client_secret='SlhN6jjXS1-eU8LIQR2m3MFwGwX60Qfzy0nQVFXkEW91gQtMpu9SUHA_KDF0XKYu',
    api_base_url='https://tunadex-dev.herokuapp.com/',
    access_token_url='https://tunadex-dev.herokuapp.com/oauth/token',
    authorize_url='https://tunadex-dev.herokuapp.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)


@app.route('/login-results')
def callback_handling():
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/home')



database_path = os.environ.get('DATABASE_URL')
if not database_path:
    print("Running local db")
    database_path = "postgres://localhost:5432/tunadex"


@app.route('/login')
def login():
    return redirect(AUTH0_AUTHORIZE_URL)