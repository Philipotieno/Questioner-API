"""Creates database and tables"""
from psycopg2 import connect
import os


def connect_to_db(config=None):
	''' Function to create a connection to the right database'''
	if config == 'testing':
		db_name = 'testdb'
	else:
		db_name = 'questioner'

	host = 'localhost'
	user = 'mitch'
	password = 'mufasa2019'

	return connect(
        database=db_name,
        host=host,
        user=user,
        password=password
    )

def create_users_table(cur):
	cur.execute(
		"""CREATE TABLE users(
		user_id serial PRIMARY KEY,
		firstname VARCHAR NOT NULL UNIQUE,
		lastname VARCHAR NOT NULL UNIQUE,
		username VARCHAR NOT NULL UNIQUE,
		phone_number INT NOT NULL,
		email VARCHAR NOT NULL UNIQUE,
		password VARCHAR NOT NULL,
		admin bool);""")

def create_meetups_table(cur):
	cur.execute(
		"""CREATE TABLE meetups(
		meetup_id serial PRIMARY KEY,
		topic VARCHAR NOT NULL UNIQUE,
		location VARCHAR NOT NULL UNIQUE,
		happening_on TIMESTAMP,
		created_on TIMESTAMP);""")

def create_questions_table(cur):
	cur.execute(
		"""CREATE TABLE questions(
		question_id serial PRIMARY KEY,
		user_id INTEGER REFERENCES users(user_id),
		meetup_id INTEGER REFERENCES meetups(meetup_id),
		title VARCHAR NOT NULL UNIQUE,
		body VARCHAR NOT NULL UNIQUE,
		created_on TIMESTAMP);""")

def main(config=None):
	conn = connect_to_db(config=config)
	conn.set_session(autocommit=True)
	cur = conn.cursor() #cursor to perform database operations
	cur.execute("""DROP TABLE IF EXISTS users CASCADE""")
	cur.execute("""DROP TABLE IF EXISTS meetups CASCADE""")
	cur.execute("""DROP TABLE IF EXISTS questions CASCADE""")

	create_users_table(cur)
	create_meetups_table(cur)
	create_questions_table(cur)

	cur.close() #close communication with the database
	conn.commit() # Make the changes to the database persistent
	conn.close()
	print('Database created')

if __name__ == '__main__':
    main()