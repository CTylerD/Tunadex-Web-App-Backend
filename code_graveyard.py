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



# app = create_app()
# app.secret_key = 'very secret key'




self.new_tune_1 = Tune(
                        title='Lush Life',
                        composer='Billy Strayhorn',
                        key='D-flat Major',
                        mastery=4
        )

        self.new_tune_2 = Tune(
                        title='Body and Soul',
                        composer='Johnny Green, Edward Heyman, Robert Sour, Frank Eyton',
                        key='D-flat Major',
                        mastery=5
        )

        self.new_tune_3 = Tune(
                        title='Freddie the Freeloader',
                        composer='Miles Davis',
                        key='Bb Major',
                        mastery=5
        )

        self.new_tune_4 = {
                    "title": "Footprints",
                    "composer": "Wayne Shorter",
                    "key": "C Minor",
                    "mastery": 5
        }




        # Uncomment the following line if a db testing occurs
        # and the database is not wiped clean after a test:
        # clear_database(self.db)
        print('test')


def clear_database(db):
    connection = db.engine.connect()
    transaction = connection.begin()
    inspector = reflection.Inspector.from_engine(db.engine)
    metadata = MetaData()

    tables = []
    foreign_keys = []

    for table_name in inspector.get_table_names():
        foreign_key_list = []
        for foreign_key in inspector.get_foreign_keys(table_name):
            if not foreign_key['name']:
                continue
            foreign_key_list.append(
                ForeignKeyConstraint((),(),name=foreign_key['name'])
                )
        table = Table(table_name, metadata, *foreign_key_list)
        tables.append(table)
        foreign_keys.extend(foreign_key_list)

    for foreign_key in foreign_keys:
        connection.execute(DropConstraint(foreign_key))

    for table in tables:
        connection.execute(DropTable(table))

    transaction.commit()