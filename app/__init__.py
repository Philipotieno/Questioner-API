from flask import Flask, jsonify

from instance.config import app_config
from app.api.v2.views.usersviews import v2_user
from app.api.v2.views.meetupviews import v2_meetups
from app.api.v2.views.questionsviews import v2_questions

def create_app(env_name):
	""" Cretae app """

	#app ininitialization

	app = Flask(__name__)
	app.config.from_object(app_config[env_name])
	app.register_blueprint(v2_user, url_prefix='/api/v1/auth')
	app.register_blueprint(v2_meetups, url_prefix='/api/v1/meetups')
	app.register_blueprint(v2_questions, url_prefix='/api/v1/questions')

	@app.route('/')
	def index():
		return jsonify({"Message" : "welcome to questioner"})

	return app