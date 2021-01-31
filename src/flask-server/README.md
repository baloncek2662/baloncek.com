# Run Flask Server

### Run flask
$ flash run

##### You can make the server available on your private network by adding --host=0.0.0.0 to the command:
$ flask run --host=0.0.0.0


### Environment variables
##### Tell flask how to import the app by setting FLASK_APP
$ export FLASK_APP=app.py

##### Enable development features by setting FLASK_ENV
$ export FLASK_ENV=development

##### Determine which config mode to use 
$ export APP_SETTINGS="config.DevelopmentConfig"
Valid inputs: ["DevelopmentConfig", "StagingConfig", "ProductionConfig", "TestingConfig"]

##### Set Postgres connection URL
$ export DATABASE_URL="postgresql://{user}:{password}@{host}:{5432|port}/{DB}"

The above steps are done automatically by setting the environment variables in .flaskenv with the help of python-dotenv.
`.flaskenv`

    FLASK_APP=main.py
    FLASK_ENV=development
    APP_SETTINGS="config.DevelopmentConfig"
    DATABASE_URL="postgresql://{USER}:{PASSWORD}@{HOST}:{PORT|5432}/{DB}"

### Migrations
To perform migrations APP_SETTINGS and DATABASE_URL must be manually exported!!
Then execute:
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade