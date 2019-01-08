class User():
	"""Adds user class"""

	def __init__(self):
		self.users = {}

	def register_user(self, fname, lname, username, email, password):
		user_id = str(len(self.users) + 1)
		reg_user = {
			"id" : user_id,
			"firstname" : fname,
			"lastname" : lname,
			"username" : username,
			"email" : email,
			"phone" : phone,
			"password" : password,
			"registered" : registered,
			"admin": False
		}

		self.users[username] = reg_user
		return self.users