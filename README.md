# Tunadex: Track your tune knowledge!
---

Tunadex allows music students to keep track of the songs that they're learning! It can be nearly impossible to keep up with the tunes you'd like the learn, the tunes you're actively learning, and the tunes you already know, and countless professional musicians have messy spreadsheets that have fallen into disrepair after trying to do just that. Enter...TUNADEX!

Tunadex is a place for you to store and neatly categorize all of these tunes. You will be able to add a tune, categorize it according to how well you know it, and even organize playlists of tunes that you might be learning for specific gigs, lessons, or teachers.

## Getting Started
---
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

Then, to set up the local database, run the following commands:

```
createdb tunadex_local_dev

## Testing
---
A unittest suite can be found in `testing.py`, which runs a full battery of tests on Tunadex's API. The test suite can be run with the following command:

```
python3 testing.py
```



What steps need to be taken
what should theduser already have installed/ onfigured
wha tmight they have arhad time understanidng right waay


Contributing




LICENSE