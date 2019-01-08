import datetime

class User():
	"""Adds user class"""

	def __init__(self):
		self.users = {}

	def register_user(self, firstname, lastname, username, email, phone, registered, password):
		user_id = str(len(self.users) + 1)
		reg_user = {
			"id" : user_id,
			"firstname" : firstname,
			"lastname" : lastname,
			"username" : username,
			"email" : email,
			"phone" : phone,
			"password" : password,
			"registered" : datetime.datetime.now()
			# "admin": False
		}

		self.users[username] = reg_user
		return self.users