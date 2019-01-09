class Meetup():
	def __init__(self):
		self.meetups = {}

	def create_meetup(self, topic, location, happeningOn, tags):
		meetup_id = str(len(self.meetups) + 1)
		new_meetup = {
			"id" : meetup_id,
				"topic" : topic,
				"location" : location,
				"tags" : tags,
				"happeningOn" : happeningOn
		}

		self.meetups[meetup_id] = new_meetup
		return self.meetups

	def get_all_meetups(self):
		'''Method to fetch all meetups'''
		if self.meetups:
			return self.meetups

	def get_specific_meetup(self, meetup_id):
		""" Fetch a specific meet using meetup_id"""
		if self.meetups:
			for mtups in self.meetups.values():
				if mtups["id"] == meetup_id:
					return mtups