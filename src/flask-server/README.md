# Run Flask Server

### Run flask
$ flash run

#### You can make the server available on your private network by adding --host=0.0.0.0 to the command:
$ flask run --host=0.0.0.0


### Environment variables
#### Tell flask how to import the app by setting FLASK_APP
$ export FLASK_APP=app.py

#### Enable development features by setting FLASK_ENV
$ export FLASK_ENV=development


This is done automatically by setting the environment variables in .flaskenv with the help of python-dotenv

