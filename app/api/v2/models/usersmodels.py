'''User models'''
from app.api.v2.models.db import Database

db = Database()
cur = db.cur

class User:

    """ Implements user class"""

    def __init__(self, firstname, lastname, username, phone_number, email, password, admin=False):
        '''initializez the class'''
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.admin = admin
    def check_if_user_exists(self, username):
        '''Method to checks if username exists'''
        query = "SELECT username from users WHERE username=%s;"
        cur.execute(query, (username,))
        the_user = cur.fetchone()
        if the_user:
            return True

    def register_user(self):
        '''Method to register a new user'''
        if self.check_if_user_exists(self.username):
            return False
        query = "INSERT INTO users \
        (firstname, lastname, username, phone_number, email, password, admin) \
        VALUES (%s, %s, %s, %s, %s, %s, %s) \
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
    def get_user_by_name(username):
        '''Method to get user by username'''
        query = "SELECT * FROM users WHERE username=%s;"
        cur.execute(query, (username, ))
        user = cur.fetchone()
        if user:
            return user
        return False
