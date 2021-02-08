import os
from flask import Flask
from config import app_config
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)
env_name = os.getenv('FLASK_ENV')
application.config.from_object(app_config[env_name])


# initialize our db
db = SQLAlchemy(application)
#application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

from views import DataView
DataView.register(application, route_prefix='/api/v1/')

if __name__ == '__main__':
    with application.app_context():
        application.run()