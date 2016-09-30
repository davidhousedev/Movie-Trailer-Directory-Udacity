from video import Video

class Movie(Video):
	"""
	Gathers IMDB information and Youtube URL for a Movie
	Usage: ("title of tv series", "url of corresponding youtube trailer")
	Attributes: json_data, title, year, plot, poster_url, trailer_url, run_time
	"""
	def __init__(self, title, trailer_url):
		Video.__init__(self, title, trailer_url)
		self.run_time = self.json_data["Runtime"]
		
