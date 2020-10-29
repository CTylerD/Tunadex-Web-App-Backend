# Tunadex: Track your tune knowledge!

## Udacity Full Stack Web Development Nanodegree - Capstone Project

### Stack
The API was written in Python using the Flask framework, supported by a database in SQLAlchemy and authentication using Auth0.
---

Tunadex allows music students to keep track of the songs that they're learning! It can be nearly impossible to keep up with the tunes you'd like the learn, the tunes you're actively learning, and the tunes you already know, and countless professional musicians have messy spreadsheets that have fallen into disrepair after trying to do just that. Enter...TUNADEX!

Tunadex is a place for you to store and neatly categorize all of these tunes. You will be able to add a tune, categorize it according to how well you know it, and even organize playlists of tunes that you might be learning for specific gigs, lessons, or teachers.

## Getting Started

### Prerequisites and Dependencies

Clone [this Github repository](https://www.github.com/ctylerd/tunadex) and run `pip install -r requirements.txt` in your shell to install the required dependencies

### Installation and Setup

Tunadex is hosted on Heroku and you can access the latest build [here](https://www.tunadex.herokuapp.com/). The frontend of Tunadex is currently under construction, but the API is fully functional and can be accessed as described in the API documentation below.

To run Tunadex locally, use the following commands to initialize the application and start the server:
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
This application is run locally on `https://127.0.0.1:5000/` by default.

To set up the local database, run the following commands:
```
createdb tunadex_local_dev
flask db init
flask db migrate
flask db upgrade
```

## Testing

A unittest suite can be found in `testing.py`, which runs a full battery of tests on Tunadex's API. The test suite can be run with the following command:
```
python3 testing.py
```

All tests are stored in this file and will be maintained as updates are made to the app functionality

## API Reference


### Getting Started
---
This reference will provide all of the necessary information for data stored in the Tunadex.

The base URL for this project is http://tunadex.herokuapp.com/.

**Authentication:**
Tunadex uses Auth0 as a third-party authentication platform, and temporary keys for testing purposes are located in `testing.py` or `setup.sh`.

### Error Handling
---
**HTTP response codes in use:**

- 200 - OK
- 400 - Bad Request
- 404 - Not Found
- 405 - Method Not Allowed
- 422 - Unprocessable Entity

**Error Formatting**

Error messages will be returned in the following format:

    {
                "success": False, 
                "error": 404,
                "message": "resource not found"
            }
            
### Endpoint Library
---
Prior to using the curl requests provided, you will need to initialize the provided JWT that authenticates these requests by retrieving the TEACHER_TOKEN from the setup.sh file and using the following command:
```
TEACHER_TOKEN=<Token string from setup.sh file>
```

**GET /tunes**

- General
    * Requests a list of all tunes from the database
    * Returns a success message indicating the success of the request and a list of all tunes currently in the database, with their title, composer, key, and mastery level

- Sample
```
curl -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" https://tunadex.herokuapp.com/tunes/
```

```
{
    "success": true, "tunes": {
        "Body and Soul": {
            "composer": 1, "key": 6, "mastery": 5
        },
        "All the Things You Are": {
            "composer": 2, "key": 5, "mastery": 5
        },
        "Summertime": {
            "composer": 3, "key": 17, "mastery": 5
        },
        "Round Midnight": {
            "composer": 4, "key": 22, "mastery": 2
        },
        "I Can't Get Started (With You)": {
            "composer": 5, "key": 1, "mastery": 2
        },
        "Four": {
            "composer": 6, "key": 4, "mastery": 5
        },
        "Footprints": {
            "composer": 7, "key": 19, "mastery": 5
        },
        "Reflections": {
            "composer": 4, "key": 5, "mastery": 2
        }
    }
}
```

**GET /tunes/<tune_id>**

- General
    * Requests the data on a specific tune in the database
    * Returns a success message indicating the success of the request and the title, composer, key, and mastery level of the requested tune

- Sample
```
curl -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" https://tunadex.herokuapp.com/tunes/1/
```
```
{
    "success": true, "tune": {
        "Body and Soul": {
            "composer": 1,
            "key": 6,
            "mastery": 5
        }
    }
}
```

**POST /tunes/**

- General
    * Adds a new tune to the database
    * Returns a success message indicating the success of the request and the title, composer, key, and mastery level of the added tune

- Sample
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" -d '{"title": "Ruby, My Dear", "composer": "Thelonious Monk", "key": "F Minor", "mastery": 3}' https://tunadex.herokuapp.com/tunes/
```

```
{
    "success": true,
    "new tune": {
        "title": "Ruby, My Dear", 
        "composer": 4,
        "key": 20,
        "mastery": 3
    }
}
```

**PATCH /tunes/<tune_id>**

- General
    * Updates a tune currently in the database
    * Returns a success message indicating the success of the request and the title, composer, key, and mastery level of the updated tune

- Sample
```
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" -d '{"mastery": 5}' https://tunadex.herokuapp.com/tunes/5/
```

```
{
    "success": true,
    "updated tune": {
        "title": "I Can't Get Started (With You)", 
        "composer": 5,
        "key": 1,
        "mastery": 5
    }
}
```

**DELETE /tunes/<tune_id>/**

- General
    * Deletes a tune currently in the database
    * Returns a success message indicating the success of the request and the title, composer, key, and mastery level of the deleted tune

- Sample
```
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" https://tunadex-dev.herokuapp.com/tunes/2
```

```
{
    "success": true,
    "deleted tune": {
        "title": "All the Things You Are)", 
        "composer": 2,
        "key": 4,
        "mastery": 5
    }
}
```

## Contributing Authors

C. Tyler Dennis

## Licensing

This project is released under the [MIT License](https://opensource.org/licenses/MIT)
