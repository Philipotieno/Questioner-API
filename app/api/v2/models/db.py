"""Creates database and tables"""
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash

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
                    firstname VARCHAR NOT NULL,
                    lastname VARCHAR NOT NULL,
                    username VARCHAR UNIQUE NOT NULL,
                    phone_number INT NOT NULL,
                    email VARCHAR NOT NULL UNIQUE,
                    password VARCHAR NOT NULL,
                    admin bool);'''

        meetups = '''CREATE TABLE IF NOT EXISTS meetups(
                    meetup_id serial PRIMARY KEY,
                    topic VARCHAR NOT NULL,
                    location VARCHAR NOT NULL,
                    tags VARCHAR NOT NULL,
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
        # def insert_admin(self):
        try:
            username = "wiseadmin"
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
                hashed_password = generate_password_hash("123432103")
                data = ('superuser', 'superadmin', 'wiseadmin',
                        '0703454545', 'admin@gmail.com', hashed_password,
                        'TRUE')

                self.cur.execute(insert_admin, data)
                self.conn.commit()
                print("Admin added successfully!")
                self.cur.close() #close communication with the database
        except Exception as e:
            print(str(e))

    def drop_tables(self):
        query = "DROP TABLE users, meetups, questions;"
        self.cur.execute(query)
        self.conn.commit()
        print("All tables dropped successfully!")
        self.cur.close()

p = Database()
p.create_tables()
# p.insert_admin()