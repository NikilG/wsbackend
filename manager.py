import os
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from config import app_config

# app initiliazation
application = Flask(__name__)

env_name = os.getenv('FLASK_ENV')
application.config.from_object(app_config[env_name])
#app.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(application) # Loading DB while starting the server

migrate = Migrate(application, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()