import json
import urllib2

class Video():
	"""
	On init, calls omdb API with title to return video info,
	then parses returned JSON.
	Parent of: movie.Movie and tvshow.TvShow
	"""
	def __init__(self, title, trailer_url):
		results = urllib2.urlopen("http://www.omdbapi.com/?t=" + urllib2.quote(title) + "&y=&plot=short&r=json")
		self.json_data = json.loads(results.read())
		self.title = self.json_data["Title"]
		self.year = self.json_data["Year"]
		self.plot = self.json_data["Plot"]
		self.poster_url = self.json_data["Poster"]
		self.trailer_url = trailer_url
