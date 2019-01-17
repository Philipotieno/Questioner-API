import os
from flask_script import Manager #class for handling a set of commands

from app.api.v2.models.db import Database
from app import create_app
env_name = os.getenv('FLASK_ENV')

app = create_app(env_name)

manager = Manager(app)

@manager.command
def create_tables():
    db.create_tables()

@manager.command
def drop_tables():
    db.drop_tables()

if __name__ == '__main__':
    manager.run() 