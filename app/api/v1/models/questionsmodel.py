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
			"createdon":now,
			"upvotes" : 0,
			"downvotes" : 0
	
		}

		self.questions[question_id] = asked_qn
		return self.questions

	def get_all_questions(self):
		'''Method to fetch all questions'''
		if self.questions:
			return self.questions

	def get_specific_question(self, question_id):
		""" Fetch a specific question using given id"""
		if self.questions:
			for qns in self.questions.values():
				if qns["id"] == question_id:
					return qns

	def upvote_qn(self, question_id, upvotes):
		""" Method to upvote a specific question"""
		asked_qns = self.get_specific_question(question_id)
		if asked_qns:
			asked_qns["upvotes"] = upvotes
			return asked_qns

	def downvote_qn(self, question_id, downvotes):
		""" Method to downvote a specific question"""
		asked_qns = self.get_specific_question(question_id)
		if asked_qns:
			asked_qns["downvotes"] = downvotes
			return asked_qns