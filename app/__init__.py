from flask import Flask

from instance.config import app_config
from app.api.v1.views.usersviews import v1_user

def create_app(env_name):
	""" Cretae app """

	#app ininitialization

	app = Flask(__name__)
	app.config.from_object(app_config[env_name])
	app.register_blueprint(v1_user, url_prefix='/v1')


	return app