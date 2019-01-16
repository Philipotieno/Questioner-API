"""Creates database and tables"""
import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    # constructor initialize environment
    def __init__(self):
        self.host = 'localhost'
        self.name = 'questioner'
        self.user = 'mitch'
        self.password = 'mufasa2019'

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
                    user_id serial PRIMARY KEY,
                    firstname VARCHAR NOT NULL UNIQUE,
                    lastname VARCHAR NOT NULL UNIQUE,
                    username VARCHAR NOT NULL UNIQUE,
                    phone_number INT NOT NULL,
                    email VARCHAR NOT NULL UNIQUE,
                    password VARCHAR NOT NULL,
                    admin bool);'''

        meetups = '''CREATE TABLE IF NOT EXISTS meetups(
                    meetup_id serial PRIMARY KEY,
                    topic VARCHAR NOT NULL UNIQUE,
                    location VARCHAR NOT NULL UNIQUE,
                    happening_on TIMESTAMP,
                    created_on TIMESTAMP);'''

        questions = '''CREATE TABLE IF NOT EXISTS questions(
                    question_id serial PRIMARY KEY,
                    user_id INTEGER REFERENCES users(user_id),
                    meetup_id INTEGER REFERENCES meetups(meetup_id),
                    title VARCHAR NOT NULL UNIQUE,
                    body VARCHAR NOT NULL UNIQUE,
                    created_on TIMESTAMP);'''

        queries = [users, meetups, questions]
        for q in queries:
            self.cur.execute(q)
            self.conn.commit()
        print("All tables created successfully!")
        self.cur.close() #close communication with the database

    def drop_tables(self):
        query = "DROP TABLE users, meetups, questions;"
        self.cur.execute(query)
        self.conn.commit()
        print("All tables dropped successfully!")
        self.cur.close()

p = Database()
p.create_tables()