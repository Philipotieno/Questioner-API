from flask import Flask

from instance.config import app_config
from app.api.v1.views.usersviews import v1_user
from app.api.v1.views.meetupviews import v1_meetups
from app.api.v1.views.questionsviews import v1_questions

def create_app(env_name):
	""" Cretae app """

	#app ininitialization

	app = Flask(__name__)
	app.config.from_object(app_config[env_name])
	app.register_blueprint(v1_user, url_prefix='/v1')
	app.register_blueprint(v1_meetups, url_prefix='/v1/meetups')
	app.register_blueprint(v1_questions, url_prefix='/api/v1/questions')


	return app