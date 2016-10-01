from video import Video

class TvShow(Video):
	"""
	Gathers IMDB information and Youtube URL for a TV series
	Usage: ("title of tv series", "url of corresponding youtube trailer")
	Attributes: json_data, title, year, plot, poster_url, trailer_url, seasons
	"""
	def __init__(self, title, youtube_url):
		Video.__init__(self, title, youtube_url)
		self.seasons = self.json_data["totalSeasons"] + " season"
		print(self.seasons[0])
		if int(self.seasons[0]) != 1:
			self.seasons += "s"
