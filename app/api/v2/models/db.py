"""Creates database and tables"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash

class Database:
    '''constructor initialize environment'''
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USERNAME')
        self.password = os.getenv('DB_PASSWORD')
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                dbname=self.name,
                user=self.user,
                password=self.password)
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            print("successfully connected")
        except:
            print("Unable to connect to the database")

    def create_tables(self):
        """ Method to create tables """
        users = '''CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY,
                    firstname VARCHAR NOT NULL,
                    lastname VARCHAR NOT NULL,
                    username VARCHAR UNIQUE NOT NULL,
                    phone_number INT NOT NULL,
                    email VARCHAR NOT NULL,
                    password VARCHAR NOT NULL,
                    admin bool);'''

        meetups = '''CREATE TABLE IF NOT EXISTS meetups(
                    meetup_id SERIAL PRIMARY KEY,
                    topic VARCHAR NOT NULL,
                    location VARCHAR NOT NULL,
                    tags VARCHAR NOT NULL,
                    happening_on TIMESTAMP,
                    created_on TIMESTAMP);'''

        questions = '''CREATE TABLE IF NOT EXISTS questions(
                    question_id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
                    meetup_id INTEGER REFERENCES meetups(meetup_id)ON DELETE CASCADE,
                    title VARCHAR NOT NULL,
                    body VARCHAR NOT NULL,
                    votes INT DEFAULT 0,
                    created_on TIMESTAMP);'''

        comments = '''CREATE TABLE IF NOT EXISTS comments(
                    comment_id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
                    question_id INTEGER REFERENCES meetups(meetup_id)ON DELETE CASCADE,
                    body VARCHAR NOT NULL,
                    created_on TIMESTAMP);'''

        rsvps = '''CREATE TABLE IF NOT EXISTS rsvps(
                    rsvp_id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
                    meetup_id INTEGER REFERENCES meetups(meetup_id) ON DELETE CASCADE,
                    response VARCHAR NOT NULL,
                    created_on TIMESTAMP);'''

        votes = '''CREATE TABLE IF NOT EXISTS votes(
                    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
                    question_id INTEGER REFERENCES questions(question_id) ON DELETE CASCADE,
                    vote VARCHAR NOT NULL);'''

        queries = [users, meetups, questions, comments, rsvps, votes]
        for q in queries:
            self.cur.execute(q)
            self.conn.commit()
        print("All tables created successfully!")
        # def insert_admin(self):
        try:
            query = """SELECT * FROM
            users WHERE username = 'wiseadmin'"""
            self.cur.execute(query)
            admin = self.cur.fetchone()

            if not admin:
                insert_admin = """INSERT INTO
                        users (firstname, lastname, username, phone_number,
                        email, password,
                        admin)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        RETURNING user_id, email, username, admin;"""
                hashed_password = generate_password_hash("1qQ@1234")
                data = ('superuser', 'superadmin', 'wiseadmin',
                        '0703454545', 'admin@gmail.com', hashed_password,
                        'TRUE')

                self.cur.execute(insert_admin, data)
                self.conn.commit()
                print("Admin added successfully!")
        except Exception as e:
            print(str(e))
            self.cur.close() #close communication with the database

    def drop_tables(self):
        '''Method to drop tables'''
        query = "DROP TABLE users, meetups, questions, comments, rsvps, votes;"
        self.cur.execute(query)
        self.conn.commit()
        print("All tables dropped successfully!")
        self.cur.close()

p = Database()
p.create_tables()