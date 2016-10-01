
import socket
import SimpleHTTPServer
import SocketServer

from movie import Movie
from tvshow import TvShow
import fresh_tomatoes

PORT = 8000


class MyTCPServer(SocketServer.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)


# borrowed MyRequestHandler syntax from: http://stackoverflow.com/questions/10607621/a-simple-website-with-python-using-simplehttpserver-and-socketserver-how-to-onl
class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
		got = TvShow("game of thrones", "https://www.youtube.com/watch?v=EI0ib1NErqg")
		hot_fuzz = Movie("hot fuzz", "https://www.youtube.com/watch?v=ayTnvVpj9t4")
		best_in_show = Movie("best in show", "https://www.youtube.com/watch?v=yeifMjqpsg0")
		monty_python = Movie("monty python and the holy grail", "https://www.youtube.com/watch?v=LG1PlkURjxE")
		budapest = Movie("the grand budapest hotel", "https://www.youtube.com/watch?v=1Fg5iWmQjwk")
		the_office = TvShow("the office", "https://www.youtube.com/watch?v=oCs3ihow7CU")
		amadeus = Movie("amadeus", "https://www.youtube.com/watch?v=yIzhAKtEzY0")
		spirited = Movie("spirited away", "https://www.youtube.com/watch?v=ByXuk9QqQkk")
		prestige = Movie("the prestige", "https://www.youtube.com/watch?v=o4gHCmTQDVI")

		videos = [got, hot_fuzz, best_in_show, monty_python, budapest, the_office, amadeus, spirited, prestige]

		fresh_tomatoes.open_videos_page(videos)

		return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)



Handler = MyRequestHandler
httpd = MyTCPServer(("0.0.0.0", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()


