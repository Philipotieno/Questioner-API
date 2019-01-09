class Meetup():
	def __init__(self):
		self.meetups = {}

	def create_meetup(self, topic, location, happeningOn, tags):
		meetup_id = str(len(self.meetups) + 1)
		new_meetup = {
			"id" : meetup_id,
				"topic" : topic,
				"location" : location,
				"tags" : tags
				"happeningOn" : "happeningOn"
		}

		self.meetups[meetup_id] = new_meetup
		return self.meetups