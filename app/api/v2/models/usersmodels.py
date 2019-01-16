import os
import psycopg2
from app.api.v2.models.db import Database

db = Database()
cur = db.conn.cursor()

class User(object):

    """ Implements user class"""

    def __init__(self, firstname, lastname, username, phone, email, password, admin=False):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.admin = admin
        
    def check_if_user_exists(self, username):
        pass

    def register_user(self):
        pass
        
    @staticmethod
    def get_user_by_id(user_id):
    	pass