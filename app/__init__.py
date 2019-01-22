from flask import Flask,Blueprint
from flask import Flask, jsonify

from instance.config import app_config
from app.api.v1.views.usersviews import v1_user
from app.api.v2.views.usersviews import v2_user
from app.api.v1.views.meetupviews import v1_meetups
from app.api.v2.views.meetupviews import v2_meetups
from app.api.v1.views.questionsviews import v1_questions
from app.api.v2.views.questionsviews import v2_questions
from flask_jwt_extended import (JWTManager)

def create_app(env_name):
	""" Cretae app """

	#app ininitialization

	app = Flask(__name__)
	app.config.from_object(app_config[env_name])

	jwt = JWTManager(app)
	
	app.register_blueprint(v1_user, url_prefix='/api/v1/auth')
	app.register_blueprint(v2_user, url_prefix='/api/v2/auth')
	app.register_blueprint(v1_meetups, url_prefix='/api/v1/meetups')
	app.register_blueprint(v2_meetups, url_prefix='/api/v2/meetups')
	app.register_blueprint(v1_questions, url_prefix='/api/v1/questions')
	app.register_blueprint(v2_questions, url_prefix='/api/v2/questions')

	@app.route('/')
	def index():
		return jsonify({"Message" : "welcome to questioner"})

	return app