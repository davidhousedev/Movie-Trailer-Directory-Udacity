

import SimpleHTTPServer
import SocketServer

from movie import Movie
from tvshow import TvShow

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

do_GET():
	got = TvShow("game of thrones", "http://www.google.com")