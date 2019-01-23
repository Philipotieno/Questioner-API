import os
from app.api.v2.models.db import Database

db = Database()
cur = db.cur

class User(object):

    """ Implements user class"""

    def __init__(self, firstname, lastname, username, phone_number, email, password, admin=False):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.admin = admin
        
    def check_if_user_exists(self, username):
        query = "SELECT username from users WHERE username=%s;"
        cur.execute(query, (username,))
        the_user = cur.fetchone()
        if the_user:
            return True

    def register_user(self):
        if self.check_if_user_exists(self.username):
            return False
        query = "INSERT INTO users (firstname, lastname, username, phone_number, email, password, admin) VALUES (%s, %s, %s, %s, %s, %s, %s) \
        RETURNING user_id, firstname, lastname, username, phone_number, email;"
        cur.execute(
            query,
            (self.firstname,
             self.lastname,
             self.username,
             self.phone_number,
             self.email,
             self.password,
             self.admin))
        user = cur.fetchone()
        db.conn.commit()
        return user
        
    @staticmethod
    def get_user_by_id(user_id):
        query = "SELECT * FROM users WHERE user_id=%s;"
        cur.execute(query, (user_id, ))
        user = cur.fetchone()
        if user:
            return user
        return False