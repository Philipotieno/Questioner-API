from flask import Flask,Blueprint
from flask import Flask, jsonify

from instance.config import app_config
from app.api.v1.views.usersviews import v1_user
from app.api.v2.views.usersviews import v2_user
from app.api.v1.views.meetupviews import v1_meetups
from app.api.v2.views.meetupviews import v2_meetups
from app.api.v1.views.questionsviews import v1_questions
from app.api.v2.views.questionsviews import v2_questions
from app.api.v2.views.commentsview import v2_comments
from app.api.v2.views.rsvpviews import v2_rsvps
from flask_jwt_extended import (JWTManager)

def create_app(env_name):
	""" Cretae app """

	#app ininitialization

	app = Flask(__name__)
	app.config.from_object(app_config[env_name])
	app.url_map.strict_slashes = False

	jwt = JWTManager(app)
	
	app.register_blueprint(v1_user, url_prefix='/api/v1/users')
	app.register_blueprint(v2_user, url_prefix='/api/v2/auth')
	app.register_blueprint(v1_meetups, url_prefix='/api/v1/meetups')
	app.register_blueprint(v2_meetups, url_prefix='/api/v2/meetups')
	app.register_blueprint(v1_questions, url_prefix='/api/v1/questions')
	app.register_blueprint(v2_questions, url_prefix='/api/v2/questions')
	app.register_blueprint(v2_comments, url_prefix='/api/v2/comments')
	app.register_blueprint(v2_rsvps, url_prefix='/api/v2/meetups/<int:meetup_id>/rsvp')

	@app.route('/')
	def index():
		return jsonify({"Message" : "welcome to questioner"})

	@app.errorhandler(400)
	def bad_request(error):
		return jsonify({'message': 'Please input all required fields!'}), 400

	@app.errorhandler(404)
	def not_found(error):
		return jsonify({'message': 'The requested URL was not found, please check your spelling and try again'}), 404

	@app.errorhandler(405)
	def not_allowed(error):
		return jsonify({'message': 'Method not allowed!'}), 405

	return app