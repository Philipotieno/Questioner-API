import datetime
now  = datetime.datetime.now()

class Question():
	"""Adds questions class"""
	def __init__(self):
		self.questions = {}

	def ask_question(self, createdon, user, meetup, title, body):
		question_id = str(len(self.questions) + 1)
		asked_qn = {
			"id":question_id,
			"user": user,
			"meetup":meetup,
			"title":title,
			"body":body,
			"createdon":now
	
		}

		self.questions[question_id] = asked_qn
		return self.questions